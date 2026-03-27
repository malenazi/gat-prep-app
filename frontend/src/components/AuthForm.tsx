import { useState } from 'react';
import { useAuth } from '@/hooks/useAuth';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Eye, EyeOff, Mail, Lock, User, ArrowLeft, Sparkles, Shield } from 'lucide-react';

interface AuthFormProps {
  onBack?: () => void;
}

const demoAccounts = [
  { email: 'student@gat.sa', password: '123456', name: 'New Student', desc: 'Has not started diagnostic yet', day: 0, icon: '🆕', color: 'border-slate-200 hover:border-teal-400 bg-white' },
  { email: 'sara@gat.sa', password: '123456', name: 'Sara Al-Mutairi', desc: 'Day 5 • Foundation Phase', day: 5, icon: '🌱', color: 'border-blue-200 hover:border-blue-400 bg-blue-50/50' },
  { email: 'mohammed@gat.sa', password: '123456', name: 'Mohammed Al-Ghamdi', desc: 'Day 15 • Reinforcement Phase', day: 15, icon: '⚡', color: 'border-amber-200 hover:border-amber-400 bg-amber-50/50' },
  { email: 'lujain@gat.sa', password: '123456', name: 'Lujain Al-Harbi', desc: 'Day 25 • Mastery Phase', day: 25, icon: '💎', color: 'border-purple-200 hover:border-purple-400 bg-purple-50/50' },
  { email: 'admin@gat.sa', password: 'admin123', name: 'System Admin', desc: 'Admin Dashboard', day: -1, icon: '🛡️', color: 'border-teal-200 hover:border-teal-400 bg-teal-50/50', isAdmin: true },
];

export function AuthForm({ onBack }: AuthFormProps) {
  const { login, register } = useAuth();
  const [isLogin, setIsLogin] = useState(true);
  const [showPassword, setShowPassword] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [loadingEmail, setLoadingEmail] = useState('');
  const [error, setError] = useState('');
  const [formData, setFormData] = useState({ name: '', email: '', password: '' });

  const updateField = (field: string, value: string) => {
    setFormData(prev => ({ ...prev, [field]: value }));
    if (error) setError('');
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setIsLoading(true);
    try {
      if (isLogin) {
        await login(formData.email, formData.password);
      } else {
        await register(formData.name, formData.email, formData.password);
      }
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setIsLoading(false);
    }
  };

  const quickLogin = async (email: string, password: string) => {
    setError('');
    setLoadingEmail(email);
    try {
      await login(email, password);
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoadingEmail('');
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4 lg:p-6 relative overflow-hidden">
      {/* Background */}
      <div className="absolute inset-0">
        <div className="absolute inset-0 bg-gradient-to-br from-teal-50 via-white to-cyan-50" />
        <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-teal-200/20 rounded-full blur-[120px] translate-x-1/3 -translate-y-1/3" />
        <div className="absolute bottom-0 left-0 w-[400px] h-[400px] bg-cyan-200/20 rounded-full blur-[100px] -translate-x-1/3 translate-y-1/3" />
      </div>

      <div className="relative z-10 w-full max-w-4xl">
        {/* Back Button */}
        {onBack && (
          <button onClick={onBack}
            className="mb-4 flex items-center gap-2 text-slate-600 hover:text-teal-600 transition-colors bg-white/70 backdrop-blur-sm px-4 py-2 rounded-xl">
            <ArrowLeft className="w-5 h-5" />
            <span>Back</span>
          </button>
        )}

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* ── Left: Demo Accounts ── */}
          <div>
            <div className="mb-4">
              <h2 className="text-xl font-black text-slate-800 mb-1">Demo Accounts</h2>
              <p className="text-sm text-slate-500">Choose an account to log in directly and view progress</p>
            </div>

            <div className="space-y-2.5">
              {/* Register new account button */}
              <button
                onClick={() => { setIsLogin(false); setError(''); }}
                className="w-full border-2 border-dashed border-teal-300 hover:border-teal-500 bg-teal-50/50 hover:bg-teal-50 rounded-xl p-3.5 transition-all text-left hover:shadow-md active:scale-[0.98]">
                <div className="flex items-center gap-3">
                  <span className="text-2xl shrink-0">✨</span>
                  <div className="flex-1 min-w-0">
                    <p className="font-bold text-teal-700 text-sm">Create New Account</p>
                    <p className="text-xs text-teal-500">Register now and start your journey</p>
                  </div>
                  <ArrowLeft className="w-4 h-4 text-teal-400 shrink-0 rotate-180" />
                </div>
              </button>

              <p className="text-sm text-slate-400 text-center">Or log in with a ready demo account</p>

              {demoAccounts.map(acc => (
                <button
                  key={acc.email}
                  onClick={() => quickLogin(acc.email, acc.password)}
                  disabled={!!loadingEmail}
                  className={`w-full border-2 rounded-xl p-3.5 transition-all text-right ${acc.color} ${loadingEmail === acc.email ? 'scale-[0.98] opacity-70' : 'hover:shadow-md active:scale-[0.98]'}`}
                >
                  <div className="flex items-center gap-3">
                    <span className="text-2xl shrink-0">{acc.icon}</span>
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center gap-2">
                        <p className="font-bold text-slate-800 text-sm">{acc.name}</p>
                        {acc.isAdmin && <Shield className="w-3.5 h-3.5 text-teal-500" />}
                      </div>
                      <p className="text-sm text-slate-500">{acc.desc}</p>
                    </div>
                    {loadingEmail === acc.email ? (
                      <div className="w-5 h-5 border-2 border-teal-400 border-t-transparent rounded-full animate-spin shrink-0" />
                    ) : (
                      acc.day >= 0 && (
                        <div className="text-left shrink-0">
                          <div className="h-1.5 w-16 bg-slate-100 rounded-full overflow-hidden">
                            <div className="h-full bg-teal-500 rounded-full" style={{ width: `${(acc.day / 30) * 100}%` }} />
                          </div>
                          <p className="text-xs text-slate-400 mt-0.5">{acc.day}/30</p>
                        </div>
                      )
                    )}
                  </div>
                </button>
              ))}
            </div>

            {error && (
              <div className="mt-3 p-3 rounded-xl bg-red-50 border border-red-200 text-red-600 text-sm text-center">
                {error}
              </div>
            )}
          </div>

          {/* ── Right: Login/Register Form ── */}
          <div className="bg-white/90 backdrop-blur-xl rounded-2xl shadow-card-lg border border-white/50 p-6 lg:p-8 relative overflow-hidden">
            <div className="absolute top-0 right-0 w-24 h-24 bg-gradient-to-br from-teal-100/50 to-cyan-100/50 rounded-full -translate-y-1/2 translate-x-1/2" />

            <div className="text-center mb-6 relative">
              <div className="w-14 h-14 rounded-xl bg-gradient-to-br from-teal-500 to-cyan-500 flex items-center justify-center mx-auto mb-3 shadow-brand">
                <Sparkles className="w-7 h-7 text-white" />
              </div>
              <h2 className="text-lg font-black text-slate-800 mb-1">
                {isLogin ? 'Sign In' : 'Create Account'}
              </h2>
              <p className="text-sm text-slate-500">
                {isLogin ? 'Or choose a demo account from the left' : 'Create your account and start your journey'}
              </p>
            </div>

            <form onSubmit={handleSubmit} className="space-y-4 relative">
              {!isLogin && (
                <div className="space-y-1.5">
                  <Label htmlFor="name" className="text-slate-700 font-medium text-sm">Full Name</Label>
                  <div className="relative">
                    <User className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                    <Input id="name" type="text" placeholder="John Doe" value={formData.name}
                      onChange={e => updateField('name', e.target.value)}
                      className="pr-10 h-11 rounded-lg border-slate-200 text-sm" required />
                  </div>
                </div>
              )}

              <div className="space-y-1.5">
                <Label htmlFor="email" className="text-slate-700 font-medium text-sm">Email Address</Label>
                <div className="relative">
                  <Mail className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                  <Input id="email" type="email" placeholder="your@email.com" dir="ltr"
                    value={formData.email} onChange={e => updateField('email', e.target.value)}
                    className="pr-10 h-11 rounded-lg border-slate-200 text-sm text-left" required />
                </div>
              </div>

              <div className="space-y-1.5">
                <Label htmlFor="password" className="text-slate-700 font-medium text-sm">Password</Label>
                <div className="relative">
                  <Lock className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                  <Input id="password" type={showPassword ? 'text' : 'password'} placeholder="••••••••" dir="ltr"
                    value={formData.password} onChange={e => updateField('password', e.target.value)}
                    className="pr-10 pl-10 h-11 rounded-lg border-slate-200 text-sm text-left" required />
                  <button type="button" onClick={() => setShowPassword(!showPassword)}
                    className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600">
                    {showPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                  </button>
                </div>
              </div>

              <Button type="submit" disabled={isLoading} className="w-full btn-primary h-11 text-sm">
                {isLoading ? (
                  <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                ) : (
                  isLogin ? 'Sign In' : 'Create Account'
                )}
              </Button>
            </form>

            <div className="mt-4 text-center relative">
              <button onClick={() => { setIsLogin(!isLogin); setError(''); }}
                className="text-teal-600 hover:text-teal-700 font-medium text-sm transition-colors">
                {isLogin ? "Don't have an account? Register now" : 'Already have an account? Sign in'}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
