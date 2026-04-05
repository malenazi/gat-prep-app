import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { ArrowLeft, Eye, EyeOff, KeyRound, Lock, Mail, Sparkles, User } from 'lucide-react';

import { useAuth } from '@/hooks/useAuth';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';

interface AuthFormProps {
  onBack?: () => void;
}

type AuthMode = 'login' | 'register' | 'forgot';

interface BrowserCredentialDetails {
  email: string;
  password: string;
  name?: string;
}

const DUPLICATE_REGISTRATION_MESSAGE = 'Email already registered';

function isDuplicateRegistrationError(message: string) {
  return message.toLowerCase().includes(DUPLICATE_REGISTRATION_MESSAGE.toLowerCase());
}

function normalizeEmailInput(email: string) {
  return email.trim().toLowerCase();
}

export function AuthForm({ onBack }: AuthFormProps) {
  const { login, register, requestPasswordReset, resetPassword } = useAuth();
  const navigate = useNavigate();
  const [mode, setMode] = useState<AuthMode>('login');
  const [showPassword, setShowPassword] = useState(false);
  const [showResetPassword, setShowResetPassword] = useState(false);
  const [saveInBrowser, setSaveInBrowser] = useState(true);
  const [showResetCodeForm, setShowResetCodeForm] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  const [resetRequestMessage, setResetRequestMessage] = useState('');
  const [resetSupportEmail, setResetSupportEmail] = useState<string | null>(null);
  const [resetPreviewToken, setResetPreviewToken] = useState<string | null>(null);
  const [resetExpiryMinutes, setResetExpiryMinutes] = useState<number | null>(null);
  const [formData, setFormData] = useState({ name: '', email: '', password: '' });
  const [resetData, setResetData] = useState({
    email: '',
    token: '',
    newPassword: '',
    confirmPassword: '',
  });

  const isLogin = mode === 'login';
  const isForgotPassword = mode === 'forgot';

  const clearMessages = () => {
    setError('');
    setSuccessMessage('');
  };

  const resetForgotPasswordState = (email = '') => {
    setResetRequestMessage('');
    setResetSupportEmail(null);
    setResetPreviewToken(null);
    setResetExpiryMinutes(null);
    setShowResetCodeForm(false);
    setResetData({
      email,
      token: '',
      newPassword: '',
      confirmPassword: '',
    });
  };

  const saveCredentialsToBrowser = async ({ email, password, name }: BrowserCredentialDetails) => {
    if (!saveInBrowser) return;

    const credentialsApi = (
      navigator as Navigator & {
        credentials?: {
          store?: (credential: Credential) => Promise<Credential | null>;
        };
      }
    ).credentials;

    const PasswordCredentialCtor = (
      window as Window & {
        PasswordCredential?: new (data: {
          id: string;
          password: string;
          name?: string;
        }) => Credential;
      }
    ).PasswordCredential;

    if (!credentialsApi?.store || !PasswordCredentialCtor) {
      return;
    }

    try {
      const credential = new PasswordCredentialCtor({
        id: email.trim().toLowerCase(),
        password,
        name: name?.trim() || undefined,
      });
      await credentialsApi.store(credential);
    } catch {
      // Fall back to the browser's default autofill/save behavior.
    }
  };

  const updateField = (field: 'name' | 'email' | 'password', value: string) => {
    setFormData(prev => ({ ...prev, [field]: value }));
    clearMessages();
  };

  const updateResetField = (field: 'email' | 'token' | 'newPassword' | 'confirmPassword', value: string) => {
    setResetData(prev => ({ ...prev, [field]: value }));
    clearMessages();
  };

  const switchMode = (nextMode: AuthMode) => {
    setMode(nextMode);
    setShowPassword(false);
    setShowResetPassword(false);
    clearMessages();

    if (nextMode === 'forgot') {
      resetForgotPasswordState(formData.email.trim().toLowerCase());
      return;
    }

    resetForgotPasswordState('');
  };

  const redirectAfterAuth = (isAdmin: boolean) => {
    navigate(isAdmin ? '/admin' : '/', { replace: true });
  };

  const handleAuthSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    clearMessages();
    setIsLoading(true);

    try {
      const normalizedEmail = normalizeEmailInput(formData.email);
      const authenticatedUser = isLogin
        ? await login(normalizedEmail, formData.password)
        : await register(formData.name, normalizedEmail, formData.password);

      await saveCredentialsToBrowser({
        email: normalizedEmail,
        password: formData.password,
        name: formData.name,
      });
      redirectAfterAuth(Boolean(authenticatedUser?.is_admin));
    } catch (err: unknown) {
      const message = err instanceof Error ? err.message : 'An error occurred';

      if (!isLogin && isDuplicateRegistrationError(message)) {
        const normalizedEmail = normalizeEmailInput(formData.email);

        try {
          const authenticatedUser = await login(normalizedEmail, formData.password);
          await saveCredentialsToBrowser({
            email: normalizedEmail,
            password: formData.password,
            name: formData.name,
          });
          redirectAfterAuth(Boolean(authenticatedUser?.is_admin));
        } catch {
          switchMode('login');
          setFormData(prev => ({
            ...prev,
            email: normalizedEmail,
            password: '',
          }));
          setError('This email already has an account. Sign in with your existing password, or use Forgot your password to reset it.');
        }
      } else {
        setError(message);
      }
    } finally {
      setIsLoading(false);
    }
  };

  const handleForgotPasswordRequest = async (e: React.FormEvent) => {
    e.preventDefault();
    clearMessages();
    setIsLoading(true);

    try {
      const response = await requestPasswordReset(resetData.email);
      setResetRequestMessage(response.message);
      setResetSupportEmail(response.support_email ?? null);
      setResetPreviewToken(response.reset_token_preview ?? null);
      setResetExpiryMinutes(response.expires_in_minutes ?? null);
      setShowResetCodeForm(true);

      if (response.reset_token_preview) {
        setResetData(prev => ({ ...prev, token: response.reset_token_preview ?? prev.token }));
      }
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : 'Unable to start password reset');
    } finally {
      setIsLoading(false);
    }
  };

  const handleResetPasswordSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    clearMessages();

    if (resetData.newPassword !== resetData.confirmPassword) {
      setError('New password and confirmation do not match');
      return;
    }

    setIsLoading(true);
    try {
      await resetPassword(resetData.email, resetData.token, resetData.newPassword);
      await saveCredentialsToBrowser({
        email: resetData.email,
        password: resetData.newPassword,
      });

      setFormData(prev => ({
        ...prev,
        email: resetData.email.trim().toLowerCase(),
        password: resetData.newPassword,
      }));
      switchMode('login');
      setSuccessMessage('Password updated. Sign in with your new password.');
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : 'Unable to reset password');
      setShowResetCodeForm(true);
    } finally {
      setIsLoading(false);
    }
  };

  const saveInBrowserLabel = isForgotPassword
    ? 'Save the new password in this browser'
    : 'Save email and password in this browser';

  const introHeading = isForgotPassword
    ? 'Reset your password and get back to your plan'
    : isLogin
      ? 'Welcome back to your GAT training'
      : 'Create your account and start today';

  const introCopy = isForgotPassword
    ? 'Use your account email to request a reset. If self-serve reset is available, you can choose a new password right away. Otherwise the academy team can share a one-time reset code.'
    : isLogin
      ? 'Sign in with your saved email and password to continue your diagnostic, plan, and practice sessions.'
      : 'Register once and your browser can save your email and password for the next visit.';

  return (
    <div className="min-h-screen flex items-center justify-center p-4 lg:p-6 relative overflow-hidden text-slate-800 dark:text-slate-100" data-testid="auth-page">
      <div className="absolute inset-0">
        <div className="absolute inset-0 bg-gradient-to-br from-teal-50 via-white to-cyan-50 dark:from-slate-950 dark:via-slate-950 dark:to-slate-900" />
        <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-teal-200/20 rounded-full blur-[120px] translate-x-1/3 -translate-y-1/3 dark:bg-teal-500/15" />
        <div className="absolute bottom-0 left-0 w-[400px] h-[400px] bg-cyan-200/20 rounded-full blur-[100px] -translate-x-1/3 translate-y-1/3 dark:bg-cyan-500/10" />
      </div>

      <div className="relative z-10 w-full max-w-5xl">
        {onBack && (
          <button
            onClick={onBack}
            data-testid="auth-back"
            className="mb-4 flex items-center gap-2 text-slate-600 hover:text-teal-600 transition-colors bg-white/70 backdrop-blur-sm px-4 py-2 rounded-xl dark:bg-slate-900/80 dark:text-slate-300 dark:hover:text-teal-300"
          >
            <ArrowLeft className="w-5 h-5" />
            <span>Back</span>
          </button>
        )}

        <div className="grid grid-cols-1 lg:grid-cols-[1.1fr_0.9fr] gap-6">
          <section className="bg-white/75 backdrop-blur-xl rounded-3xl border border-white/60 shadow-card-lg p-6 lg:p-8 dark:border-slate-800/80 dark:bg-slate-950/80">
            <div className="inline-flex items-center gap-2 rounded-full bg-teal-50 dark:bg-teal-950/30 text-teal-700 dark:text-teal-300 px-3 py-1 text-xs font-bold uppercase tracking-[0.18em]">
              <Sparkles className="w-3.5 h-3.5" />
              Soft Launch Access
            </div>

            <h1 className="mt-5 text-3xl lg:text-4xl font-black text-slate-900 leading-tight dark:text-slate-50">
              {introHeading}
            </h1>

            <p className="mt-4 text-sm lg:text-base text-slate-600 leading-relaxed max-w-xl dark:text-slate-300">
              {introCopy}
            </p>

            <div className="mt-8 grid grid-cols-1 sm:grid-cols-3 gap-3">
              <div className="rounded-2xl bg-slate-50 border border-slate-100 p-4 dark:border-slate-800 dark:bg-slate-900">
                <p className="text-xs font-bold uppercase tracking-wide text-slate-500 dark:text-slate-400">
                  {isForgotPassword ? '1. Request Help' : '1. Register'}
                </p>
                <p className="mt-2 text-sm text-slate-700 dark:text-slate-200">
                  {isForgotPassword
                    ? 'Enter your email to request reset help or start a self-serve reset when available.'
                    : 'Create a learner account with your name, email, and password.'}
                </p>
              </div>
              <div className="rounded-2xl bg-slate-50 border border-slate-100 p-4 dark:border-slate-800 dark:bg-slate-900">
                <p className="text-xs font-bold uppercase tracking-wide text-slate-500 dark:text-slate-400">
                  {isForgotPassword ? '2. Get A Code' : '2. Save Access'}
                </p>
                <p className="mt-2 text-sm text-slate-700 dark:text-slate-200">
                  {isForgotPassword
                    ? 'Use a one-time reset code and choose a new password that meets the learner policy.'
                    : 'Your browser can offer to save your credentials after a successful sign-in or sign-up.'}
                </p>
              </div>
              <div className="rounded-2xl bg-slate-50 border border-slate-100 p-4 dark:border-slate-800 dark:bg-slate-900">
                <p className="text-xs font-bold uppercase tracking-wide text-slate-500 dark:text-slate-400">
                  {isForgotPassword ? '3. Continue Fast' : '3. Continue Fast'}
                </p>
                <p className="mt-2 text-sm text-slate-700 dark:text-slate-200">
                  {isForgotPassword
                    ? 'Sign in again and keep studying without losing progress.'
                    : 'Come back later and sign in quickly with browser autofill.'}
                </p>
              </div>
            </div>

            {isLogin && (
              <button
                type="button"
                onClick={() => switchMode('register')}
                data-testid="auth-create-account-shortcut"
                className="mt-8 w-full sm:w-auto border-2 border-dashed border-teal-300 dark:border-teal-700 hover:border-teal-500 bg-teal-50/70 dark:bg-teal-950/30 hover:bg-teal-50 rounded-2xl px-5 py-4 transition-all text-left hover:shadow-md active:scale-[0.98]"
              >
                <p className="font-bold text-teal-700 dark:text-teal-300 text-sm">Create New Account</p>
                <p className="text-xs text-teal-500 dark:text-teal-400 mt-1">Switch to registration and begin your study plan.</p>
              </button>
            )}
          </section>

          <section className="bg-white/90 backdrop-blur-xl rounded-3xl shadow-card-lg border border-white/50 p-6 lg:p-8 relative overflow-hidden dark:border-slate-800/80 dark:bg-slate-950/90">
            <div className="absolute top-0 right-0 w-24 h-24 bg-gradient-to-br from-teal-100/50 to-cyan-100/50 rounded-full -translate-y-1/2 translate-x-1/2 dark:from-teal-500/10 dark:to-cyan-500/5" />

            <div className="text-center mb-6 relative">
              <div className="w-14 h-14 rounded-xl bg-gradient-to-br from-teal-500 to-cyan-500 flex items-center justify-center mx-auto mb-3 shadow-brand">
                {isForgotPassword ? <KeyRound className="w-7 h-7 text-white" /> : <Sparkles className="w-7 h-7 text-white" />}
              </div>
              <h2 className="text-lg font-black text-slate-800 mb-1 dark:text-slate-50">
                {isForgotPassword ? 'Reset Password' : isLogin ? 'Sign In' : 'Create Account'}
              </h2>
              <p className="text-sm text-slate-500 dark:text-slate-400">
                {isForgotPassword
                  ? 'Request a reset code, then choose a new password'
                  : isLogin
                    ? 'Use your account credentials to continue learning'
                    : 'Create your account and start your journey'}
              </p>
            </div>

            {!isForgotPassword ? (
              <form
                onSubmit={handleAuthSubmit}
                className="space-y-4 relative"
                data-testid="auth-form"
                autoComplete="on"
              >
                {!isLogin && (
                  <div className="space-y-1.5">
                    <Label htmlFor="name" className="text-slate-700 dark:text-slate-200 font-medium text-sm">Full Name</Label>
                    <div className="relative">
                      <User className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                      <Input
                        id="name"
                        name="name"
                        type="text"
                        placeholder="John Doe"
                        value={formData.name}
                        data-testid="auth-name"
                        autoComplete="name"
                        onChange={e => updateField('name', e.target.value)}
                        className="pr-10 h-11 rounded-lg border-slate-200 dark:border-slate-700 text-sm"
                        required
                      />
                    </div>
                  </div>
                )}

                <div className="space-y-1.5">
                  <Label htmlFor="email" className="text-slate-700 dark:text-slate-200 font-medium text-sm">Email Address</Label>
                  <div className="relative">
                    <Mail className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                    <Input
                      id="email"
                      name="email"
                      type="email"
                      placeholder="your@email.com"
                      dir="ltr"
                      data-testid="auth-email"
                      value={formData.email}
                      autoComplete="username"
                      onChange={e => updateField('email', e.target.value)}
                      className="pr-10 h-11 rounded-lg border-slate-200 dark:border-slate-700 text-sm text-left"
                      required
                    />
                  </div>
                </div>

                <div className="space-y-1.5">
                  <Label htmlFor="password" className="text-slate-700 dark:text-slate-200 font-medium text-sm">Password</Label>
                  <div className="relative">
                    <Lock className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                    <Input
                      id="password"
                      name="password"
                      type={showPassword ? 'text' : 'password'}
                      placeholder="••••••••"
                      dir="ltr"
                      data-testid="auth-password"
                      value={formData.password}
                      autoComplete={isLogin ? 'current-password' : 'new-password'}
                      onChange={e => updateField('password', e.target.value)}
                      className="pr-10 pl-10 h-11 rounded-lg border-slate-200 dark:border-slate-700 text-sm text-left"
                      required
                    />
                    <button
                      type="button"
                      onClick={() => setShowPassword(!showPassword)}
                      className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 dark:text-slate-300"
                    >
                      {showPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                    </button>
                  </div>
                </div>

                {isLogin && (
                  <div className="flex justify-end">
                    <button
                      type="button"
                      onClick={() => switchMode('forgot')}
                      data-testid="auth-forgot-password"
                      className="text-sm font-medium text-teal-600 hover:text-teal-700 dark:text-teal-300 transition-colors"
                    >
                      Forgot your password?
                    </button>
                  </div>
                )}

                <label
                  htmlFor="save-in-browser"
                  className="flex items-start gap-3 rounded-2xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 px-4 py-3 cursor-pointer"
                >
                  <input
                    id="save-in-browser"
                    name="save_in_browser"
                    type="checkbox"
                    checked={saveInBrowser}
                    onChange={e => setSaveInBrowser(e.target.checked)}
                    className="mt-0.5 h-4 w-4 rounded border-slate-300 accent-teal-600"
                  />
                  <div>
                    <p className="text-sm font-semibold text-slate-700 dark:text-slate-200">
                      {saveInBrowserLabel}
                    </p>
                    <p className="text-xs text-slate-500">
                      Uses your browser&apos;s password manager when supported.
                    </p>
                  </div>
                </label>

                {error && (
                  <div className="animate-slide-down rounded-xl bg-red-50 dark:bg-red-950/30 border border-red-200 dark:border-red-800 text-red-600 text-sm text-center p-3" data-testid="auth-error">
                    {error}
                  </div>
                )}

                {successMessage && (
                  <div className="animate-slide-down rounded-xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800 text-emerald-700 dark:text-emerald-300 text-sm text-center p-3" data-testid="auth-success">
                    {successMessage}
                  </div>
                )}

                <Button type="submit" disabled={isLoading} className="w-full btn-primary interactive-press h-11 text-sm" data-testid="auth-submit">
                  {isLoading ? (
                    <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                  ) : (
                    isLogin ? 'Sign In' : 'Create Account'
                  )}
                </Button>
              </form>
            ) : (
              <div className="space-y-4" data-testid="forgot-password-form">
                <form onSubmit={handleForgotPasswordRequest} className="space-y-4" autoComplete="on">
                  <div className="space-y-1.5">
                    <Label htmlFor="forgot-email" className="text-slate-700 dark:text-slate-200 font-medium text-sm">Account Email</Label>
                    <div className="relative">
                      <Mail className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                      <Input
                        id="forgot-email"
                        name="forgot_email"
                        type="email"
                        placeholder="your@email.com"
                        dir="ltr"
                        data-testid="forgot-email"
                        value={resetData.email}
                        autoComplete="username"
                        onChange={e => updateResetField('email', e.target.value)}
                        className="pr-10 h-11 rounded-lg border-slate-200 dark:border-slate-700 text-sm text-left"
                        required
                      />
                    </div>
                  </div>

                  <Button
                    type="submit"
                    disabled={isLoading}
                    className="w-full btn-primary interactive-press h-11 text-sm"
                    data-testid="forgot-request-submit"
                  >
                    {isLoading ? (
                      <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                    ) : (
                      'Request Reset Help'
                    )}
                  </Button>
                </form>

                {error && (
                  <div className="animate-slide-down rounded-xl bg-red-50 dark:bg-red-950/30 border border-red-200 dark:border-red-800 text-red-600 text-sm text-center p-3" data-testid="auth-error">
                    {error}
                  </div>
                )}

                {resetRequestMessage && (
                  <div className="rounded-2xl border border-emerald-200 dark:border-emerald-800 bg-emerald-50 dark:bg-emerald-950/30 p-4 text-sm text-emerald-800 dark:text-emerald-200" data-testid="forgot-request-message">
                    <p className="font-semibold">Reset request received</p>
                    <p className="mt-1">{resetRequestMessage}</p>
                    {resetSupportEmail && (
                      <p className="mt-2 text-emerald-700 dark:text-emerald-300">
                        Support contact: <span className="font-semibold">{resetSupportEmail}</span>
                      </p>
                    )}
                    {resetPreviewToken && (
                      <div className="mt-3 rounded-xl border border-emerald-200 bg-white/80 p-3">
                        <p className="text-xs font-bold uppercase tracking-wide text-emerald-700 dark:text-emerald-300">One-time reset code</p>
                        <p className="mt-2 font-mono text-sm text-slate-800 dark:text-slate-100 break-all" data-testid="forgot-preview-token">
                          {resetPreviewToken}
                        </p>
                        {resetExpiryMinutes && (
                          <p className="mt-2 text-xs text-slate-500">
                            Expires in about {resetExpiryMinutes} minutes.
                          </p>
                        )}
                      </div>
                    )}
                  </div>
                )}

                <div className="rounded-2xl border border-slate-200 dark:border-slate-700 bg-slate-50/80 dark:bg-slate-900 p-4">
                  <div className="flex items-center justify-between gap-3">
                    <div>
                      <p className="text-sm font-semibold text-slate-800 dark:text-slate-100">Have a reset code?</p>
                      <p className="text-xs text-slate-500 mt-1">
                        Enter your one-time code and choose a new password.
                      </p>
                    </div>
                    <button
                      type="button"
                      onClick={() => setShowResetCodeForm(prev => !prev)}
                      data-testid="forgot-have-code"
                      className="text-sm font-medium text-teal-600 hover:text-teal-700 dark:text-teal-300 transition-colors"
                    >
                      {showResetCodeForm ? 'Hide reset form' : 'I already have a reset code'}
                    </button>
                  </div>

                  {showResetCodeForm && (
                    <form onSubmit={handleResetPasswordSubmit} className="mt-4 space-y-4" autoComplete="on">
                      <div className="space-y-1.5">
                        <Label htmlFor="reset-token" className="text-slate-700 dark:text-slate-200 font-medium text-sm">Reset Code</Label>
                        <Input
                          id="reset-token"
                          name="reset_token"
                          type="text"
                          placeholder="Paste your one-time code"
                          dir="ltr"
                          data-testid="forgot-reset-token"
                          value={resetData.token}
                          autoComplete="one-time-code"
                          onChange={e => updateResetField('token', e.target.value)}
                          className="h-11 rounded-lg border-slate-200 dark:border-slate-700 text-sm text-left font-mono"
                          required
                        />
                      </div>

                      <div className="space-y-1.5">
                        <Label htmlFor="new-password" className="text-slate-700 dark:text-slate-200 font-medium text-sm">New Password</Label>
                        <div className="relative">
                          <Lock className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                          <Input
                            id="new-password"
                            name="new_password"
                            type={showResetPassword ? 'text' : 'password'}
                            placeholder="Choose a new password"
                            dir="ltr"
                            data-testid="forgot-new-password"
                            value={resetData.newPassword}
                            autoComplete="new-password"
                            onChange={e => updateResetField('newPassword', e.target.value)}
                            className="pr-10 pl-10 h-11 rounded-lg border-slate-200 dark:border-slate-700 text-sm text-left"
                            required
                          />
                          <button
                            type="button"
                            onClick={() => setShowResetPassword(!showResetPassword)}
                            className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 dark:text-slate-300"
                          >
                            {showResetPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                          </button>
                        </div>
                      </div>

                      <div className="space-y-1.5">
                        <Label htmlFor="confirm-password" className="text-slate-700 dark:text-slate-200 font-medium text-sm">Confirm New Password</Label>
                        <Input
                          id="confirm-password"
                          name="confirm_new_password"
                          type={showResetPassword ? 'text' : 'password'}
                          placeholder="Re-enter your new password"
                          dir="ltr"
                          data-testid="forgot-confirm-password"
                          value={resetData.confirmPassword}
                          autoComplete="new-password"
                          onChange={e => updateResetField('confirmPassword', e.target.value)}
                          className="h-11 rounded-lg border-slate-200 dark:border-slate-700 text-sm text-left"
                          required
                        />
                      </div>

                      <label
                        htmlFor="save-in-browser"
                        className="flex items-start gap-3 rounded-2xl border border-slate-200 bg-white dark:bg-slate-900 px-4 py-3 cursor-pointer"
                      >
                        <input
                          id="save-in-browser"
                          name="save_in_browser"
                          type="checkbox"
                          checked={saveInBrowser}
                          onChange={e => setSaveInBrowser(e.target.checked)}
                          className="mt-0.5 h-4 w-4 rounded border-slate-300 accent-teal-600"
                        />
                        <div>
                          <p className="text-sm font-semibold text-slate-700 dark:text-slate-200">
                            {saveInBrowserLabel}
                          </p>
                          <p className="text-xs text-slate-500">
                            Uses your browser&apos;s password manager when supported.
                          </p>
                        </div>
                      </label>

                      <Button
                        type="submit"
                        disabled={isLoading}
                        className="w-full btn-primary interactive-press h-11 text-sm"
                        data-testid="forgot-reset-submit"
                      >
                        {isLoading ? (
                          <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                        ) : (
                          'Set New Password'
                        )}
                      </Button>
                    </form>
                  )}
                </div>
              </div>
            )}

            {!isForgotPassword && (
              <div className="mt-4 text-center relative">
                <button
                  type="button"
                  onClick={() => switchMode(isLogin ? 'register' : 'login')}
                  data-testid="auth-mode-toggle"
                  className="text-teal-600 hover:text-teal-700 dark:text-teal-300 font-medium text-sm transition-colors"
                >
                  {isLogin ? "Don't have an account? Register now" : 'Already have an account? Sign in'}
                </button>
              </div>
            )}

            {isForgotPassword && (
              <div className="mt-4 text-center relative">
                <button
                  type="button"
                  onClick={() => switchMode('login')}
                  data-testid="forgot-back-to-sign-in"
                  className="text-teal-600 hover:text-teal-700 dark:text-teal-300 font-medium text-sm transition-colors"
                >
                  Back to sign in
                </button>
              </div>
            )}
          </section>
        </div>
      </div>
    </div>
  );
}
