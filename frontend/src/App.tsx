import { useState } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from '@/hooks/useAuth';
import { Toaster } from '@/components/ui/sonner';
import { LandingPage } from '@/components/LandingPage';
import { AuthForm } from '@/components/AuthForm';
import { TrialSession } from '@/components/TrialSession';
import AppShell from '@/components/layout/AppShell';
import Diagnostic from '@/pages/Diagnostic';
import Dashboard from '@/pages/Dashboard';
import Practice from '@/pages/Practice';
import Plan from '@/pages/Plan';
import Analytics from '@/pages/Analytics';
import Admin from '@/pages/Admin';
import MockExam from '@/pages/MockExam';

function Spinner() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-50">
      <div className="text-center">
        <div className="text-5xl mb-4 animate-float">🎯</div>
        <div className="w-8 h-8 border-3 border-teal-400 border-t-transparent rounded-full animate-spin mx-auto" />
      </div>
    </div>
  );
}

function AppRoutes() {
  const { user, isLoading } = useAuth();
  const [showAuth, setShowAuth] = useState(false);
  const [showTrial, setShowTrial] = useState(false);

  if (isLoading) return <Spinner />;

  // Not authenticated — show landing, auth, or trial
  if (!user) {
    if (showTrial) {
      return (
        <Routes>
          <Route path="*" element={
            <TrialSession
              onRegister={() => { setShowTrial(false); setShowAuth(true); }}
              onBack={() => setShowTrial(false)}
            />
          } />
        </Routes>
      );
    }
    if (showAuth) {
      return (
        <Routes>
          <Route path="*" element={<AuthForm onBack={() => setShowAuth(false)} />} />
        </Routes>
      );
    }
    return (
      <Routes>
        <Route path="*" element={
          <LandingPage
            onStart={() => setShowAuth(true)}
            onTrial={() => setShowTrial(true)}
          />
        } />
      </Routes>
    );
  }

  // Diagnostic not completed — force diagnostic
  if (!user.diagnostic_completed) {
    return (
      <Routes>
        <Route path="*" element={<Diagnostic />} />
      </Routes>
    );
  }

  // Authenticated with diagnostic complete
  // Admin users go to /admin by default
  const defaultRoute = user.is_admin ? '/admin' : '/';

  return (
    <Routes>
      {user.is_admin && <Route path="/admin" element={<Admin />} />}
      <Route path="/mock" element={<MockExam />} />
      <Route element={<AppShell />}>
        <Route path="/" element={<Dashboard />} />
        <Route path="/practice" element={<Practice />} />
        <Route path="/plan" element={<Plan />} />
        <Route path="/analytics" element={<Analytics />} />
        <Route path="*" element={<Navigate to={defaultRoute} />} />
      </Route>
    </Routes>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <AppRoutes />
        <Toaster
          position="top-center"
          toastOptions={{
            style: {
              direction: 'ltr',
              fontFamily: 'Poppins, sans-serif',
            },
          }}
        />
      </BrowserRouter>
    </AuthProvider>
  );
}
