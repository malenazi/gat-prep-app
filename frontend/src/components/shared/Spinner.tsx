export function Spinner({ className = '' }: { className?: string }) {
  return <div className={`w-8 h-8 border-3 border-teal-400 border-t-transparent rounded-full animate-spin ${className}`} />;
}
