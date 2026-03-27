import React from 'react';

// Floating Shapes Component
export const FloatingShapes: React.FC = () => (
  <div className="absolute inset-0 overflow-hidden pointer-events-none">
    {/* Circle 1 */}
    <div className="absolute top-[10%] left-[5%] w-32 h-32 rounded-full border-2 border-teal-200/40 animate-float" />
    <div className="absolute top-[12%] left-[7%] w-20 h-20 rounded-full bg-gradient-to-br from-teal-300/20 to-cyan-300/20 animate-float" style={{ animationDelay: '0.5s' }} />
    
    {/* Circle 2 */}
    <div className="absolute top-[30%] right-[8%] w-40 h-40 rounded-full border-2 border-amber-200/40 animate-float" style={{ animationDelay: '1s' }} />
    <div className="absolute top-[32%] right-[10%] w-24 h-24 rounded-full bg-gradient-to-br from-amber-300/20 to-orange-300/20 animate-float" style={{ animationDelay: '1.5s' }} />
    
    {/* Square */}
    <div className="absolute bottom-[20%] left-[10%] w-24 h-24 rounded-xl border-2 border-violet-200/40 rotate-12 animate-float" style={{ animationDelay: '2s' }} />
    <div className="absolute bottom-[22%] left-[12%] w-14 h-14 rounded-lg bg-gradient-to-br from-violet-300/20 to-purple-300/20 rotate-12 animate-float" style={{ animationDelay: '2.5s' }} />
    
    {/* Triangle-like shape */}
    <div className="absolute bottom-[35%] right-[5%] w-0 h-0 border-l-[30px] border-l-transparent border-r-[30px] border-r-transparent border-b-[50px] border-b-rose-200/30 animate-float" style={{ animationDelay: '0.8s' }} />
    
    {/* Dots pattern */}
    <div className="absolute top-[50%] left-[3%] grid grid-cols-3 gap-2 animate-float" style={{ animationDelay: '1.2s' }}>
      {[...Array(9)].map((_, i) => (
        <div key={i} className="w-2 h-2 rounded-full bg-teal-300/40" />
      ))}
    </div>
    
    <div className="absolute top-[15%] right-[15%] grid grid-cols-4 gap-1.5 animate-float" style={{ animationDelay: '2.2s' }}>
      {[...Array(16)].map((_, i) => (
        <div key={i} className="w-1.5 h-1.5 rounded-full bg-cyan-300/40" />
      ))}
    </div>
    
    {/* Ring */}
    <div className="absolute bottom-[10%] right-[20%] w-28 h-28 rounded-full border-4 border-dashed border-emerald-200/40 animate-spin" style={{ animationDuration: '20s' }} />
    
    {/* Plus signs */}
    <div className="absolute top-[25%] left-[20%] text-teal-300/40 text-2xl animate-pulse">+</div>
    <div className="absolute top-[60%] right-[25%] text-amber-300/40 text-xl animate-pulse" style={{ animationDelay: '1s' }}>+</div>
    <div className="absolute bottom-[30%] left-[30%] text-violet-300/40 text-lg animate-pulse" style={{ animationDelay: '2s' }}>+</div>
    
    {/* Wave lines */}
    <svg className="absolute top-[40%] left-0 w-32 h-16 opacity-20" viewBox="0 0 100 40">
      <path d="M0 20 Q25 0, 50 20 T100 20" stroke="#0d9488" strokeWidth="2" fill="none" />
      <path d="M0 30 Q25 10, 50 30 T100 30" stroke="#14b8a6" strokeWidth="2" fill="none" />
    </svg>
    
    <svg className="absolute bottom-[15%] right-0 w-40 h-20 opacity-20" viewBox="0 0 100 50">
      <path d="M0 25 Q25 5, 50 25 T100 25" stroke="#f59e0b" strokeWidth="2" fill="none" />
      <path d="M0 35 Q25 15, 50 35 T100 35" stroke="#fbbf24" strokeWidth="2" fill="none" />
    </svg>
  </div>
);

// Hero Illustration
export const HeroIllustration: React.FC = () => (
  <div className="relative w-full max-w-lg mx-auto">
    <svg viewBox="0 0 400 300" className="w-full h-auto">
      {/* Background blob */}
      <ellipse cx="200" cy="180" rx="150" ry="100" fill="url(#blobGradient)" opacity="0.3" />
      
      {/* Person silhouette */}
      <g transform="translate(160, 80)">
        {/* Head */}
        <circle cx="40" cy="30" r="25" fill="#f8fafc" stroke="#0d9488" strokeWidth="2" />
        {/* Body */}
        <path d="M40 55 L40 100" stroke="#0d9488" strokeWidth="3" strokeLinecap="round" />
        {/* Arms */}
        <path d="M40 65 L15 85" stroke="#0d9488" strokeWidth="2.5" strokeLinecap="round" />
        <path d="M40 65 L65 85" stroke="#0d9488" strokeWidth="2.5" strokeLinecap="round" />
        {/* Legs */}
        <path d="M40 100 L25 140" stroke="#0d9488" strokeWidth="2.5" strokeLinecap="round" />
        <path d="M40 100 L55 140" stroke="#0d9488" strokeWidth="2.5" strokeLinecap="round" />
        {/* Book */}
        <rect x="55" y="75" width="20" height="25" rx="2" fill="#fbbf24" stroke="#d97706" strokeWidth="1.5" />
        <line x1="60" y1="82" x2="70" y2="82" stroke="#d97706" strokeWidth="1" />
        <line x1="60" y1="88" x2="70" y2="88" stroke="#d97706" strokeWidth="1" />
        <line x1="60" y1="94" x2="68" y2="94" stroke="#d97706" strokeWidth="1" />
      </g>
      
      {/* Floating elements */}
      <circle cx="80" cy="100" r="15" fill="#14b8a6" opacity="0.6" />
      <text x="76" y="106" fill="white" fontSize="14" fontWeight="bold">+</text>
      
      <circle cx="320" cy="80" r="12" fill="#f59e0b" opacity="0.6" />
      <text x="316" y="85" fill="white" fontSize="12" fontWeight="bold">×</text>
      
      <circle cx="300" cy="200" r="18" fill="#8b5cf6" opacity="0.5" />
      <text x="294" y="207" fill="white" fontSize="16" fontWeight="bold">÷</text>
      
      {/* Stars */}
      <polygon points="120,50 123,58 132,58 125,64 128,73 120,68 112,73 115,64 108,58 117,58" fill="#fbbf24" />
      <polygon points="280,140 282,146 288,146 283,150 285,156 280,152 275,156 277,150 272,146 278,146" fill="#fbbf24" />
      
      {/* Gradients */}
      <defs>
        <linearGradient id="blobGradient" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#14b8a6" />
          <stop offset="100%" stopColor="#06b6d4" />
        </linearGradient>
      </defs>
    </svg>
  </div>
);

// Feature Icon Backgrounds
export const FeatureIconBg: React.FC<{ color: string; children: React.ReactNode }> = ({ color, children }) => (
  <div className={`relative w-20 h-20 rounded-2xl overflow-hidden`}>
    <div className={`absolute inset-0 bg-gradient-to-br ${color}`} />
    <div className="absolute inset-0 flex items-center justify-center">
      {children}
    </div>
    {/* Decorative circles */}
    <div className="absolute -top-2 -right-2 w-6 h-6 rounded-full bg-white/20" />
    <div className="absolute -bottom-1 -left-1 w-4 h-4 rounded-full bg-white/20" />
  </div>
);

// Progress Ring
export const ProgressRing: React.FC<{ progress: number; size?: number; strokeWidth?: number }> = ({ 
  progress, 
  size = 120, 
  strokeWidth = 8 
}) => {
  const radius = (size - strokeWidth) / 2;
  const circumference = radius * 2 * Math.PI;
  const offset = circumference - (progress / 100) * circumference;
  
  return (
    <div className="relative" style={{ width: size, height: size }}>
      <svg width={size} height={size} className="-rotate-90">
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          fill="none"
          stroke="#e2e8f0"
          strokeWidth={strokeWidth}
        />
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          fill="none"
          stroke="url(#progressGradient)"
          strokeWidth={strokeWidth}
          strokeLinecap="round"
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          className="transition-all duration-1000 ease-out"
        />
        <defs>
          <linearGradient id="progressGradient" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stopColor="#0d9488" />
            <stop offset="100%" stopColor="#14b8a6" />
          </linearGradient>
        </defs>
      </svg>
      <div className="absolute inset-0 flex items-center justify-center">
        <span className="text-2xl font-black text-slate-800">{progress}%</span>
      </div>
    </div>
  );
};

// Decorative Divider
export const DecorativeDivider: React.FC = () => (
  <div className="flex items-center justify-center gap-4 my-8">
    <div className="h-px w-16 bg-gradient-to-r from-transparent to-teal-300" />
    <div className="flex gap-2">
      <div className="w-2 h-2 rounded-full bg-teal-400" />
      <div className="w-2 h-2 rounded-full bg-cyan-400" />
      <div className="w-2 h-2 rounded-full bg-teal-400" />
    </div>
    <div className="h-px w-16 bg-gradient-to-l from-transparent to-teal-300" />
  </div>
);

// Stats Card Background Pattern
export const StatsPattern: React.FC<{ color: string }> = ({ color }) => (
  <svg className="absolute inset-0 w-full h-full opacity-10" viewBox="0 0 100 100" preserveAspectRatio="none">
    <defs>
      <pattern id={`grid-${color}`} width="10" height="10" patternUnits="userSpaceOnUse">
        <circle cx="5" cy="5" r="1" fill={color} />
      </pattern>
    </defs>
    <rect width="100" height="100" fill={`url(#grid-${color})`} />
  </svg>
);

// Animated Checkmark
export const AnimatedCheckmark: React.FC = () => (
  <svg className="w-16 h-16" viewBox="0 0 50 50">
    <circle cx="25" cy="25" r="23" fill="#22c55e" opacity="0.2" />
    <circle cx="25" cy="25" r="20" fill="none" stroke="#22c55e" strokeWidth="3" />
    <path
      d="M15 25 L22 32 L35 18"
      fill="none"
      stroke="#22c55e"
      strokeWidth="3"
      strokeLinecap="round"
      strokeLinejoin="round"
      className="animate-draw"
      style={{
        strokeDasharray: 40,
        strokeDashoffset: 40,
        animation: 'draw 0.5s ease-out forwards'
      }}
    />
    <style>{`
      @keyframes draw {
        to { stroke-dashoffset: 0; }
      }
    `}</style>
  </svg>
);

// Trophy Animation
export const AnimatedTrophy: React.FC = () => (
  <div className="relative">
    <svg className="w-24 h-24" viewBox="0 0 100 100">
      {/* Trophy body */}
      <defs>
        <linearGradient id="trophyGold" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#fbbf24" />
          <stop offset="50%" stopColor="#f59e0b" />
          <stop offset="100%" stopColor="#d97706" />
        </linearGradient>
      </defs>
      <path
        d="M30 20 L30 15 L70 15 L70 20 Q85 20 85 35 Q85 50 70 55 L70 65 Q75 70 80 75 L80 80 L20 80 L20 75 Q25 70 30 65 L30 55 Q15 50 15 35 Q15 20 30 20"
        fill="url(#trophyGold)"
        stroke="#d97706"
        strokeWidth="2"
      />
      {/* Shine effect */}
      <ellipse cx="45" cy="35" rx="8" ry="12" fill="white" opacity="0.3" />
    </svg>
    {/* Sparkles around trophy */}
    <div className="absolute -top-2 -left-2 text-yellow-400 text-lg animate-pulse">✨</div>
    <div className="absolute -top-1 -right-1 text-yellow-400 text-sm animate-pulse" style={{ animationDelay: '0.3s' }}>✨</div>
    <div className="absolute bottom-0 -right-2 text-yellow-400 text-lg animate-pulse" style={{ animationDelay: '0.6s' }}>✨</div>
  </div>
);

// Wave Background
export const WaveBackground: React.FC = () => (
  <div className="absolute bottom-0 left-0 right-0 overflow-hidden">
    <svg viewBox="0 0 1440 120" className="w-full h-auto" preserveAspectRatio="none">
      <path
        d="M0,60 C360,120 720,0 1080,60 C1260,90 1380,30 1440,60 L1440,120 L0,120 Z"
        fill="url(#waveGradient)"
        opacity="0.3"
      />
      <path
        d="M0,80 C240,40 480,100 720,60 C960,20 1200,80 1440,50 L1440,120 L0,120 Z"
        fill="url(#waveGradient2)"
        opacity="0.2"
      />
      <defs>
        <linearGradient id="waveGradient" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stopColor="#14b8a6" />
          <stop offset="100%" stopColor="#06b6d4" />
        </linearGradient>
        <linearGradient id="waveGradient2" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stopColor="#0d9488" />
          <stop offset="100%" stopColor="#14b8a6" />
        </linearGradient>
      </defs>
    </svg>
  </div>
);

// Question Type Badge Icon
export const QuestionTypeIcon: React.FC<{ type: 'verbal' | 'quantitative' }> = ({ type }) => (
  <div className={`w-10 h-10 rounded-xl flex items-center justify-center ${
    type === 'verbal' 
      ? 'bg-violet-100 text-violet-600' 
      : 'bg-cyan-100 text-cyan-600'
  }`}>
    {type === 'verbal' ? (
      <svg className="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
        <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
        <line x1="8" y1="7" x2="16" y2="7" />
        <line x1="8" y1="11" x2="14" y2="11" />
        <line x1="8" y1="15" x2="12" y2="15" />
      </svg>
    ) : (
      <svg className="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <rect x="4" y="4" width="16" height="16" rx="2" />
        <path d="M8 8h8M8 12h8M8 16h5" />
        <path d="M16 16l2 2" />
        <circle cx="17" cy="7" r="1" fill="currentColor" />
      </svg>
    )}
  </div>
);

// Streak Fire Animation
export const StreakFire: React.FC<{ count: number }> = ({ count }) => (
  <div className="relative flex items-center gap-2">
    <div className="relative">
      <svg className="w-8 h-8 animate-fire" viewBox="0 0 24 24" fill="url(#fireGradient)">
        <defs>
          <linearGradient id="fireGradient" x1="0%" y1="100%" x2="0%" y2="0%">
            <stop offset="0%" stopColor="#ef4444" />
            <stop offset="50%" stopColor="#f97316" />
            <stop offset="100%" stopColor="#fbbf24" />
          </linearGradient>
        </defs>
        <path d="M12 2C8 6 6 10 6 13c0 3.31 2.69 6 6 6s6-2.69 6-6c0-3-2-7-6-11z" />
        <path d="M12 6c-2 3-3 5-3 7 0 1.66 1.34 3 3 3s3-1.34 3-3c0-2-1-4-3-7z" fill="#fef3c7" opacity="0.8" />
      </svg>
      {/* Glow effect */}
      <div className="absolute inset-0 bg-orange-400 rounded-full blur-lg opacity-40 animate-pulse" />
    </div>
    <span className="text-xl font-black text-orange-600">{count}</span>
  </div>
);

// XP Star Animation
export const XPStar: React.FC<{ xp: number }> = ({ xp }) => (
  <div className="relative flex items-center gap-2">
    <div className="relative">
      <svg className="w-8 h-8" viewBox="0 0 24 24" fill="url(#starGradient)">
        <defs>
          <linearGradient id="starGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#fbbf24" />
            <stop offset="100%" stopColor="#f59e0b" />
          </linearGradient>
        </defs>
        <polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26" />
      </svg>
      {/* Sparkle effects */}
      <div className="absolute -top-1 -right-1 w-2 h-2 bg-yellow-300 rounded-full animate-ping" />
    </div>
    <span className="text-xl font-black text-amber-600">{xp.toLocaleString()}</span>
  </div>
);
