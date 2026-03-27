import { useState } from 'react';
import { api } from '@/lib/api';

interface FeedbackModalProps {
  trigger: string;
  onClose: () => void;
}

const emojis = [
  { value: 1, emoji: '😡', label: 'Bad' },
  { value: 2, emoji: '😕', label: 'Poor' },
  { value: 3, emoji: '😐', label: 'Average' },
  { value: 4, emoji: '🙂', label: 'Good' },
  { value: 5, emoji: '😍', label: 'Excellent' },
];

const triggerLabels: Record<string, string> = {
  session_complete: 'How was today\'s session?',
  diagnostic: 'How was the diagnostic test experience?',
  phase_change: 'How do you feel about your progress?',
  streak: 'What do you think of the app so far?',
};

export function FeedbackModal({ trigger, onClose }: FeedbackModalProps) {
  const [rating, setRating] = useState(0);
  const [comment, setComment] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [sending, setSending] = useState(false);
  const [error, setError] = useState('');

  const submit = async () => {
    if (!rating) return;
    setSending(true);
    try {
      await api.submitFeedback({ rating, comment: comment || undefined, trigger, page: window.location.pathname });
      setSubmitted(true);
      localStorage.setItem('lastFeedbackDate', new Date().toISOString().split('T')[0]);
      setTimeout(onClose, 1500);
    } catch {
      setError('An error occurred, please try again');
      setSending(false);
      return;
    }
  };

  const dismiss = () => {
    localStorage.setItem('lastFeedbackDate', new Date().toISOString().split('T')[0]);
    onClose();
  };

  if (submitted) return (
    <div className="fixed inset-0 bg-slate-900/40 backdrop-blur-sm flex items-end sm:items-center justify-center z-50 p-4">
      <div className="bg-white rounded-2xl p-8 w-full max-w-sm text-center shadow-card-lg animate-slide-up">
        <div className="text-5xl mb-3">💚</div>
        <p className="text-slate-800 font-bold">Thank you for your feedback!</p>
      </div>
    </div>
  );

  return (
    <div className="fixed inset-0 bg-slate-900/40 backdrop-blur-sm flex items-end sm:items-center justify-center z-50 p-4">
      <div className="bg-white rounded-2xl p-6 w-full max-w-sm shadow-card-lg animate-slide-up">
        <p className="text-slate-800 font-bold text-lg mb-1">{triggerLabels[trigger] || 'Your opinion matters'}</p>
        <p className="text-slate-500 text-sm mb-5">Help us improve the experience</p>

        <div className="flex justify-center gap-3 mb-5">
          {emojis.map(e => (
            <button key={e.value} onClick={() => setRating(e.value)}
              className={`flex flex-col items-center gap-1 p-2 rounded-xl transition-all
                ${rating === e.value ? 'bg-teal-50 scale-110 shadow-sm' : 'hover:bg-slate-50'}`}>
              <span className="text-3xl">{e.emoji}</span>
              <span className={`text-sm ${rating === e.value ? 'text-teal-600 font-bold' : 'text-slate-500'}`}>{e.label}</span>
            </button>
          ))}
        </div>

        {rating > 0 && (
          <div className="mb-4 animate-slide-up">
            <textarea value={comment} onChange={e => setComment(e.target.value)}
              placeholder="Any additional comments? (optional)"
              rows={2}
              className="w-full bg-slate-50 border border-slate-200 rounded-xl px-4 py-3 text-slate-700 text-sm placeholder-slate-500 focus:outline-none focus:border-teal-500 focus:ring-2 focus:ring-teal-500/20 transition resize-none" />
          </div>
        )}

        {error && (
          <div className="mb-3 p-2.5 rounded-xl bg-red-50 border border-red-200 text-red-600 text-sm text-center">
            {error}
          </div>
        )}

        <div className="flex gap-3">
          <button onClick={dismiss} className="flex-1 text-slate-500 text-sm font-medium py-2.5 hover:text-slate-700 transition">Later</button>
          {rating > 0 && (
            <button onClick={submit} disabled={sending}
              className="flex-1 bg-gradient-to-l from-teal-600 to-teal-500 text-white font-bold py-2.5 rounded-xl shadow-brand transition-all disabled:opacity-50">
              {sending ? '...' : 'Send'}
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
