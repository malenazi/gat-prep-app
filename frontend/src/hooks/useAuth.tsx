import { useState, useEffect, createContext, useContext, useCallback, type ReactNode } from 'react';
import { api, setToken, clearToken } from '@/lib/api';
import type { ApiUser, ForgotPasswordResponse, ResetPasswordResponse } from '@/types';

interface AuthContextType {
  user: ApiUser | null;
  isLoading: boolean;
  login: (email: string, password: string) => Promise<ApiUser | null>;
  register: (name: string, email: string, password: string) => Promise<ApiUser | null>;
  requestPasswordReset: (email: string) => Promise<ForgotPasswordResponse>;
  resetPassword: (email: string, resetToken: string, newPassword: string) => Promise<ResetPasswordResponse>;
  logout: () => void;
  loadUser: () => Promise<ApiUser | null>;
}

const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<ApiUser | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  const loadUser = useCallback(async (): Promise<ApiUser | null> => {
    try {
      const data = await api.me();
      setUser(data);
      return data;
    } catch (e: unknown) {
      // Only clear token on auth errors (401 triggers redirect in api.ts)
      // Network errors should not log the user out
      if (e instanceof Error && e.message === 'unauthorized') {
        clearToken();
      }
      setUser(null);
      return null;
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
    return loadUser();
  };

  const register = async (name: string, email: string, password: string) => {
    const res = await api.register({ name, email, password });
    setToken(res.token);
    return loadUser();
  };

  const requestPasswordReset = async (email: string) => api.forgotPassword({ email });

  const resetPassword = async (email: string, resetToken: string, newPassword: string) =>
    api.resetPassword({ email, reset_token: resetToken, new_password: newPassword });

  const logout = () => {
    clearToken();
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, isLoading, login, register, requestPasswordReset, resetPassword, logout, loadUser }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used within AuthProvider');
  return ctx;
};
