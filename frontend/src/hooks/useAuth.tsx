import { useState, useEffect, createContext, useContext, useCallback, type ReactNode } from 'react';
import { api, setToken, clearToken } from '@/lib/api';
import type { ApiUser } from '@/types';

interface AuthContextType {
  user: ApiUser | null;
  isLoading: boolean;
  login: (email: string, password: string) => Promise<void>;
  register: (name: string, email: string, password: string) => Promise<void>;
  logout: () => void;
  loadUser: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<ApiUser | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  const loadUser = useCallback(async () => {
    try {
      const data = await api.me();
      setUser(data);
    } catch (e: unknown) {
      // Only clear token on auth errors (401 triggers redirect in api.ts)
      // Network errors should not log the user out
      if (e instanceof Error && e.message === 'unauthorized') {
        clearToken();
      }
      setUser(null);
    }
  }, []);

  // On mount: if token exists, fetch user
  useEffect(() => {
    const token = localStorage.getItem('gat_token');
    if (token) {
      loadUser().finally(() => setIsLoading(false));
    } else {
      setIsLoading(false);
    }
  }, [loadUser]);

  const login = async (email: string, password: string) => {
    const res = await api.login({ email, password });
    setToken(res.token);
    await loadUser();
  };

  const register = async (name: string, email: string, password: string) => {
    const res = await api.register({ name, email, password });
    setToken(res.token);
    await loadUser();
  };

  const logout = () => {
    clearToken();
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, isLoading, login, register, logout, loadUser }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used within AuthProvider');
  return ctx;
};
