import { useState } from 'react';
import { ChevronDown } from 'lucide-react';

const FAQ_ITEMS = [
  {
    q: 'How long is the course?',
    a: 'The course is designed for 30 days of intensive study, but you can adjust the pace based on your schedule. Each day requires 60-90 minutes of focused practice.',
  },
  {
    q: 'Is the course suitable for my level?',
    a: 'Yes! Our smart diagnostic test identifies your current level and creates a personalized plan. Whether you\'re a beginner or advanced, the adaptive system ensures optimal challenge.',
  },
  {
    q: 'What happens after 30 days?',
    a: 'The 30-day path is the core guided journey. During the beta period you can revisit your work and continue practicing while access remains available.',
  },
  {
    q: 'Are the questions similar to the real test?',
    a: 'The question bank is written to reflect the style, pacing, and skill mix learners commonly prepare for in the GAT.',
  },
  {
    q: 'Do I need prior knowledge?',
    a: 'No prior knowledge is required. Our Foundation phase covers all basics, and the adaptive system ensures you start at the right level for you.',
  },
  {
    q: 'How does the adaptive system work?',
    a: 'After the diagnostic test, the system uses IRT (Item Response Theory) to estimate your ability per skill. Questions are selected to maximize learning — not too easy, not too hard. Difficulty calibrates automatically as you practice.',
  },
  {
    q: 'What are streak freezes?',
    a: 'You start with 2 streak freezes. If you miss a day, a freeze is used automatically to protect your streak. Once used, freezes do not regenerate.',
  },
  {
    q: 'How is my predicted score calculated?',
    a: 'Your predicted score is based on your performance across all 9 skills, weighted by their importance on the actual exam. It updates after every practice session.',
  },
];

interface FAQAccordionProps {
  className?: string;
}

export function FAQAccordion({ className = '' }: FAQAccordionProps) {
  const [openIndex, setOpenIndex] = useState<number | null>(null);

  return (
    <div className={`space-y-2 ${className}`} data-testid="faq-accordion">
      {FAQ_ITEMS.map((faq, i) => {
        const isOpen = openIndex === i;
        return (
          <div
            key={i}
            className="rounded-xl border border-slate-200 bg-white overflow-hidden dark:border-slate-700 dark:bg-slate-800"
          >
            <button
              type="button"
              onClick={() => setOpenIndex(isOpen ? null : i)}
              className="w-full flex items-center justify-between gap-3 px-4 py-3 text-left text-sm font-bold text-slate-700 hover:bg-slate-50 transition dark:text-slate-200 dark:hover:bg-slate-700/50"
              data-testid={`faq-item-${i}`}
            >
              <span>{faq.q}</span>
              <ChevronDown
                className={`h-4 w-4 shrink-0 text-slate-400 transition-transform dark:text-slate-500 ${isOpen ? 'rotate-180' : ''}`}
              />
            </button>
            {isOpen && (
              <div className="px-4 pb-3 text-sm text-slate-600 leading-relaxed animate-slide-down dark:text-slate-300">
                {faq.a}
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
}
