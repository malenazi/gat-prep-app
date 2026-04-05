import { Component, Suspense, lazy, useState } from 'react';
import type { ErrorInfo, ReactNode } from 'react';
import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom';
import { ThemeProvider } from 'next-themes';

import { AuthProvider, useAuth } from '@/hooks/useAuth';

class ErrorBoundary extends Component<{ children: ReactNode }, { hasError: boolean }> {
  state = { hasError: false };
  static getDerivedStateFromError() { return { hasError: true }; }
  componentDidCatch(error: Error, info: ErrorInfo) {
    console.error('App error boundary caught:', error, info.componentStack);
  }
  render() {
    if (this.state.hasError) {
      return (
        <div className="min-h-screen flex items-center justify-center bg-slate-50 dark:bg-slate-950 p-6">
          <div className="text-center max-w-sm">
            <div className="text-5xl mb-4">⚠️</div>
            <h1 className="text-xl font-bold text-slate-800 dark:text-slate-100 mb-2">Something went wrong</h1>
            <p className="text-slate-500 dark:text-slate-400 text-sm mb-6">An unexpected error occurred. Please refresh the page.</p>
            <button onClick={() => window.location.reload()} className="bg-teal-600 text-white font-bold py-2.5 px-8 rounded-xl shadow-brand">
              Refresh Page
            </button>
          </div>
        </div>
      );
    }
    return this.props.children;
  }
}
import { ThemeToggle } from '@/components/theme/ThemeToggle';
import { Toaster } from '@/components/ui/sonner';

const LandingPage = lazy(() => import('@/components/LandingPage').then(module => ({ default: module.LandingPage })));
const AuthForm = lazy(() => import('@/components/AuthForm').then(module => ({ default: module.AuthForm })));
const AppShell = lazy(() => import('@/components/layout/AppShell'));
const Diagnostic = lazy(() => import('@/pages/Diagnostic'));
const Dashboard = lazy(() => import('@/pages/Dashboard'));
const Practice = lazy(() => import('@/pages/Practice'));
const Plan = lazy(() => import('@/pages/Plan'));
const Analytics = lazy(() => import('@/pages/Analytics'));
const Admin = lazy(() => import('@/pages/Admin'));
const MockExam = lazy(() => import('@/pages/MockExam'));

function Spinner() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-50 dark:bg-slate-950">
      <div className="text-center">
        <div className="text-sm font-semibold uppercase tracking-[0.18em] text-teal-600 dark:text-teal-300">
          Loading
        </div>
        <div className="mt-4 w-8 h-8 border-3 border-teal-400 border-t-transparent rounded-full animate-spin mx-auto" />
      </div>
    </div>
  );
}

function AppRoutes() {
  const { user, isLoading } = useAuth();
  const [showAuth, setShowAuth] = useState(false);

  if (isLoading) return <Spinner />;

  if (!user) {
    if (showAuth) {
      return (
        <Routes>
          <Route path="*" element={<AuthForm onBack={() => setShowAuth(false)} />} />
        </Routes>
      );
    }

    return (
      <Routes>
        <Route
          path="*"
          element={
            <LandingPage
              onStart={() => setShowAuth(true)}
            />
          }
        />
      </Routes>
    );
  }

  if (!user.diagnostic_completed) {
    return (
      <Routes>
        <Route path="*" element={<Diagnostic />} />
      </Routes>
    );
  }

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
        <Route path="*" element={<Navigate to={defaultRoute} replace />} />
      </Route>
    </Routes>
  );
}

export default function App() {
  return (
    <ErrorBoundary>
    <AuthProvider>
      <ThemeProvider attribute="class" defaultTheme="light" enableSystem={false} storageKey="qudra-theme">
        <BrowserRouter>
          <Suspense fallback={<Spinner />}>
            <ThemeToggle />
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
          </Suspense>
        </BrowserRouter>
      </ThemeProvider>
    </AuthProvider>
    </ErrorBoundary>
  );
}
