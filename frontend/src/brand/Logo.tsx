import React from 'react';

interface LogoProps {
  size?: number;
  variant?: 'full' | 'icon' | 'wordmark';
  className?: string;
}

export const Logo: React.FC<LogoProps> = ({ size = 40, variant = 'full', className = '' }) => {
  const gradientId = `logoGradient-${Math.random().toString(36).substr(2, 9)}`;
  
  if (variant === 'icon') {
    return (
      <svg width={size} height={size} viewBox="0 0 100 100" className={className}>
        <defs>
          <linearGradient id={gradientId} x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#0d9488" />
            <stop offset="50%" stopColor="#14b8a6" />
            <stop offset="100%" stopColor="#06b6d4" />
          </linearGradient>
          <filter id={`glow-${gradientId}`}>
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
              <feMergeNode in="coloredBlur"/>
              <feMergeNode in="SourceGraphic"/>
            </feMerge>
          </filter>
        </defs>
        
        {/* Outer hexagon */}
        <polygon 
          points="50,5 90,25 90,75 50,95 10,75 10,25" 
          fill={`url(#${gradientId})`}
          filter={`url(#glow-${gradientId})`}
        />
        
        {/* Inner shape - Book/Brain symbol */}
        <g transform="translate(25, 25)" fill="white">
          {/* Book pages */}
          <path d="M25 5 C15 5, 5 10, 5 20 L5 45 C5 48, 8 50, 10 50 L25 45 L40 50 C42 50, 45 48, 45 45 L45 20 C45 10, 35 5, 25 5 Z" />
          {/* Center line */}
          <line x1="25" y1="5" x2="25" y2="45" stroke="#0d9488" strokeWidth="2" />
          {/* Page lines */}
          <line x1="12" y1="18" x2="22" y2="16" stroke="#0d9488" strokeWidth="1.5" />
          <line x1="12" y1="25" x2="22" y2="23" stroke="#0d9488" strokeWidth="1.5" />
          <line x1="12" y1="32" x2="22" y2="30" stroke="#0d9488" strokeWidth="1.5" />
          <line x1="28" y1="16" x2="38" y2="18" stroke="#0d9488" strokeWidth="1.5" />
          <line x1="28" y1="23" x2="38" y2="25" stroke="#0d9488" strokeWidth="1.5" />
          <line x1="28" y1="30" x2="38" y2="32" stroke="#0d9488" strokeWidth="1.5" />
        </g>
        
        {/* Sparkle accents */}
        <circle cx="15" cy="20" r="3" fill="#fbbf24" />
        <circle cx="85" cy="30" r="2" fill="#fbbf24" />
        <circle cx="75" cy="80" r="2.5" fill="#fbbf24" />
      </svg>
    );
  }
  
  if (variant === 'wordmark') {
    return (
      <svg width={size * 2.5} height={size} viewBox="0 0 250 100" className={className}>
        <defs>
          <linearGradient id={gradientId} x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stopColor="#0d9488" />
            <stop offset="100%" stopColor="#14b8a6" />
          </linearGradient>
        </defs>
        <text 
          x="50%" 
          y="50%" 
          dominantBaseline="middle" 
          textAnchor="middle" 
          fill={`url(#${gradientId})`}
          fontSize="72"
          fontWeight="900"
          fontFamily="Tajawal, sans-serif"
        >
          Qudra Academy
        </text>
      </svg>
    );
  }

  // Full logo with icon and wordmark
  return (
    <svg width={size * 3.5} height={size} viewBox="0 0 350 100" className={className}>
      <defs>
        <linearGradient id={gradientId} x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#0d9488" />
          <stop offset="50%" stopColor="#14b8a6" />
          <stop offset="100%" stopColor="#06b6d4" />
        </linearGradient>
        <filter id={`glow-${gradientId}`}>
          <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
          <feMerge>
            <feMergeNode in="coloredBlur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>
      </defs>

      {/* Icon */}
      <g transform="translate(0, 0)">
        <polygon
          points="50,5 90,25 90,75 50,95 10,75 10,25"
          fill={`url(#${gradientId})`}
          filter={`url(#glow-${gradientId})`}
        />
        <g transform="translate(25, 25)" fill="white">
          <path d="M25 5 C15 5, 5 10, 5 20 L5 45 C5 48, 8 50, 10 50 L25 45 L40 50 C42 50, 45 48, 45 45 L45 20 C45 10, 35 5, 25 5 Z" />
          <line x1="25" y1="5" x2="25" y2="45" stroke="#0d9488" strokeWidth="2" />
          <line x1="12" y1="18" x2="22" y2="16" stroke="#0d9488" strokeWidth="1.5" />
          <line x1="12" y1="25" x2="22" y2="23" stroke="#0d9488" strokeWidth="1.5" />
          <line x1="12" y1="32" x2="22" y2="30" stroke="#0d9488" strokeWidth="1.5" />
          <line x1="28" y1="16" x2="38" y2="18" stroke="#0d9488" strokeWidth="1.5" />
          <line x1="28" y1="23" x2="38" y2="25" stroke="#0d9488" strokeWidth="1.5" />
          <line x1="28" y1="30" x2="38" y2="32" stroke="#0d9488" strokeWidth="1.5" />
        </g>
        <circle cx="15" cy="20" r="3" fill="#fbbf24" />
        <circle cx="85" cy="30" r="2" fill="#fbbf24" />
      </g>

      {/* Wordmark */}
      <text
        x="120"
        y="55"
        dominantBaseline="middle"
        fill="#1e293b"
        fontSize="56"
        fontWeight="900"
        fontFamily="Tajawal, sans-serif"
      >
        Qudra Academy
      </text>
      
      {/* Tagline */}
      <text 
        x="120" 
        y="78" 
        fill="#64748b"
        fontSize="14"
        fontWeight="500"
        fontFamily="Tajawal, sans-serif"
      >
        Your Path to Success
      </text>
    </svg>
  );
};

// Logo mark for small spaces (favicon style)
export const LogoMark: React.FC<{ size?: number; className?: string }> = ({ size = 32, className = '' }) => (
  <svg width={size} height={size} viewBox="0 0 100 100" className={className}>
    <defs>
      <linearGradient id="markGradient" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stopColor="#0d9488" />
        <stop offset="50%" stopColor="#14b8a6" />
        <stop offset="100%" stopColor="#06b6d4" />
      </linearGradient>
    </defs>
    <polygon 
      points="50,5 90,25 90,75 50,95 10,75 10,25" 
      fill="url(#markGradient)"
    />
    <g transform="translate(25, 25)" fill="white">
      <path d="M25 5 C15 5, 5 10, 5 20 L5 45 C5 48, 8 50, 10 50 L25 45 L40 50 C42 50, 45 48, 45 45 L45 20 C45 10, 35 5, 25 5 Z" />
      <line x1="25" y1="5" x2="25" y2="45" stroke="#0d9488" strokeWidth="2" />
    </g>
  </svg>
);

// Animated logo for loading states
export const AnimatedLogo: React.FC<{ size?: number; className?: string }> = ({ size = 60, className = '' }) => (
  <div className={`relative ${className}`} style={{ width: size, height: size }}>
    <svg width={size} height={size} viewBox="0 0 100 100" className="animate-pulse">
      <defs>
        <linearGradient id="animatedGradient" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#0d9488">
            <animate attributeName="stop-color" values="#0d9488;#14b8a6;#06b6d4;#14b8a6;#0d9488" dur="3s" repeatCount="indefinite" />
          </stop>
          <stop offset="100%" stopColor="#14b8a6">
            <animate attributeName="stop-color" values="#14b8a6;#06b6d4;#0d9488;#06b6d4;#14b8a6" dur="3s" repeatCount="indefinite" />
          </stop>
        </linearGradient>
      </defs>
      <polygon 
        points="50,5 90,25 90,75 50,95 10,75 10,25" 
        fill="url(#animatedGradient)"
      />
      <g transform="translate(25, 25)" fill="white">
        <path d="M25 5 C15 5, 5 10, 5 20 L5 45 C5 48, 8 50, 10 50 L25 45 L40 50 C42 50, 45 48, 45 45 L45 20 C45 10, 35 5, 25 5 Z" />
        <line x1="25" y1="5" x2="25" y2="45" stroke="#0d9488" strokeWidth="2" />
      </g>
    </svg>
    {/* Rotating ring */}
    <div className="absolute inset-0 border-2 border-dashed border-teal-300/50 rounded-full animate-spin" style={{ animationDuration: '8s' }} />
  </div>
);

export default Logo;
