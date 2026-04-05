import clsx from 'clsx';
import { useState } from 'react';

import { RichTextContent } from '@/components/questions/RichTextContent';
import { sanitizeInlineSvg } from '@/lib/questionVisuals';
import type { QuestionAppearance } from '@/lib/questionPresentation';
import {
  defaultQuestionAppearance,
  getQuestionContrastClass,
  getQuestionDensityClass,
  getQuestionTextScale,
} from '@/lib/questionPresentation';
import type { ComparisonColumns, QuestionContentFormat, QuestionTable } from '@/types';

function normalizeFigureCaption(figureAlt?: string | null, questionText?: string) {
  const raw = figureAlt?.trim();
  if (!raw) return null;

  const cleaned = raw
    .replace(/^Figure for .*?:\s*/i, '')
    .replace(/\s+/g, ' ')
    .trim();

  if (!cleaned || cleaned.length > 120) {
    return null;
  }

  const normalizedQuestion = (questionText ?? '').replace(/\s+/g, ' ').trim().toLowerCase();
  const normalizedCaption = cleaned.toLowerCase().replace(/\.$/, '');
  if (normalizedQuestion && normalizedCaption.startsWith(normalizedQuestion.slice(0, Math.min(normalizedQuestion.length, 40)))) {
    return null;
  }

  return cleaned;
}

interface QuestionPromptProps {
  passage_ar?: string | null;
  table_ar?: QuestionTable | null;
  table_caption?: string | null;
  figure_svg?: string | null;
  figure_alt?: string | null;
  text_ar: string;
  content_format?: QuestionContentFormat | null;
  comparison_columns?: ComparisonColumns | null;
  testIdPrefix: string;
  passageClassName?: string;
  questionClassName?: string;
  figureFrameClassName?: string;
  compact?: boolean;
  appearance?: QuestionAppearance;
}

export function QuestionPrompt({
  passage_ar,
  table_ar,
  table_caption,
  figure_svg,
  figure_alt,
  text_ar,
  content_format = 'plain',
  comparison_columns,
  testIdPrefix,
  passageClassName = 'rounded-2xl border border-blue-100 bg-blue-50/40 p-4 text-sm text-slate-700 shadow-sm dark:border-slate-800 dark:bg-slate-900 dark:text-slate-300',
  questionClassName = 'text-base font-bold leading-relaxed text-slate-800 lg:text-2xl dark:text-slate-100',
  figureFrameClassName = 'rounded-2xl border border-slate-200 bg-white p-4 shadow-sm dark:border-slate-800 dark:bg-slate-950',
  compact = false,
  appearance = defaultQuestionAppearance,
}: QuestionPromptProps) {
  const [passageExpanded, setPassageExpanded] = useState(false);
  const safeSvg = sanitizeInlineSvg(figure_svg);
  const hasLongPassage = Boolean(passage_ar && passage_ar.length > 220 && !compact);
  const densityClass = getQuestionDensityClass(appearance.density);
  const scaleClass = getQuestionTextScale(appearance.textSize);
  const contrastClass = getQuestionContrastClass(appearance.contrast);
  const tableTextSize = compact ? 'text-xs' : 'text-sm';
  const figureCaption = normalizeFigureCaption(figure_alt, text_ar);
  const promptHeadingClass = appearance.textSize === 'large'
    ? 'text-2xl font-black leading-[1.35] text-slate-900 lg:text-[2.3rem] dark:text-slate-50'
    : 'text-xl font-black leading-[1.45] text-slate-900 lg:text-[1.95rem] dark:text-slate-50';
  const supportSurfaceClass = compact
    ? 'rounded-[1.75rem] border border-slate-200/80 bg-white/95 p-4 shadow-[0_18px_45px_-32px_rgba(15,23,42,0.24)] dark:border-slate-800 dark:bg-slate-950/95'
    : 'rounded-[2rem] border border-slate-200/80 bg-white/95 p-5 lg:p-7 shadow-[0_24px_55px_-34px_rgba(15,23,42,0.24)] dark:border-slate-800 dark:bg-slate-950/95';

  const promptBody = (
    <div className={clsx('space-y-5', densityClass, scaleClass, contrastClass)}>
      {(table_ar || safeSvg) && (
        <div className="space-y-5" data-testid={`${testIdPrefix}-supporting-data`}>
          {table_ar && (
            <div
              className="overflow-x-auto rounded-[2rem] border border-slate-200/80 bg-white shadow-[0_22px_55px_-38px_rgba(15,23,42,0.3)] dark:border-slate-800 dark:bg-slate-950"
              data-testid={`${testIdPrefix}-table`}
            >
              <div className="flex flex-wrap items-center gap-3 border-b border-slate-100 bg-gradient-to-r from-slate-50 via-white to-blue-50/50 px-4 py-3.5 lg:px-5 dark:border-slate-800 dark:from-slate-950 dark:via-slate-950 dark:to-slate-900">
                <span className="rounded-full bg-blue-100 px-3 py-1 text-[11px] font-black uppercase tracking-[0.18em] text-blue-700">
                  Data Table
                </span>
                {table_caption && (
                  <div className="text-sm font-semibold text-slate-600 dark:text-slate-300">
                    {table_caption}
                  </div>
                )}
              </div>
              <table className="min-w-full border-collapse" dir="auto">
                {table_caption && <caption className="sr-only">{table_caption}</caption>}
                <thead>
                  <tr className="bg-slate-50 dark:bg-slate-900">
                    {table_ar.headers.map((header) => (
                      <th key={header} className={`border-b border-slate-200 px-3 py-2 text-left font-bold text-slate-700 dark:border-slate-800 dark:text-slate-200 ${tableTextSize}`}>
                        {header}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {table_ar.rows.map((row, rowIndex) => (
                    <tr key={`${testIdPrefix}-row-${rowIndex}`} className={rowIndex % 2 === 0 ? 'bg-white dark:bg-slate-950' : 'bg-slate-50/50 dark:bg-slate-900/70'}>
                      {row.map((cell, cellIndex) => (
                        <td key={`${testIdPrefix}-cell-${rowIndex}-${cellIndex}`} className={`border-b border-slate-100 px-3 py-2 text-slate-700 dark:border-slate-800 dark:text-slate-200 ${tableTextSize}`}>
                          <RichTextContent content={cell} contentFormat={content_format} inline className="leading-relaxed" />
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}

          {safeSvg && (
            <div className={clsx(figureFrameClassName, supportSurfaceClass, 'overflow-hidden bg-gradient-to-br from-slate-50 via-white to-teal-50/60 dark:from-slate-950 dark:via-slate-950 dark:to-teal-950/40')} data-testid={`${testIdPrefix}-figure`}>
              <div className="mb-4 flex flex-wrap items-center justify-between gap-3">
                <div>
                  <p className="text-[11px] font-black uppercase tracking-[0.2em] text-teal-600">Reference Diagram</p>
                  <p className="mt-1 text-sm font-semibold text-slate-700 dark:text-slate-200">
                    Study the figure before choosing your answer.
                  </p>
                </div>
                <span className="rounded-full border border-teal-200 bg-white/85 px-3 py-1 text-xs font-semibold text-teal-700 shadow-sm dark:border-teal-900 dark:bg-slate-900/80 dark:text-teal-300">
                  Visual Support
                </span>
              </div>
              <div
                role="img"
                aria-label={figure_alt || 'Question figure'}
                className="mx-auto flex min-h-[15rem] max-w-[34rem] items-center justify-center lg:min-h-[18rem] [&_svg]:h-auto [&_svg]:max-h-[24rem] [&_svg]:w-full"
                dangerouslySetInnerHTML={{ __html: safeSvg }}
              />
              {figureCaption && <p className="mt-4 text-sm leading-relaxed text-slate-500 dark:text-slate-400">{figureCaption}</p>}
            </div>
          )}
        </div>
      )}

      <div className="rounded-[2rem] border border-slate-200/80 bg-white/95 p-5 shadow-[0_24px_55px_-36px_rgba(15,23,42,0.26)] lg:p-7 dark:border-slate-800 dark:bg-slate-950/95" data-testid={`${testIdPrefix}-text-card`}>
        <div className="mb-3 flex flex-wrap items-center gap-3">
            <span className="rounded-full bg-slate-100 px-3 py-1 text-[11px] font-black uppercase tracking-[0.18em] text-slate-500 dark:bg-slate-800 dark:text-slate-300">
            Question
          </span>
          {safeSvg && (
              <span className="rounded-full border border-amber-200 bg-amber-50 px-3 py-1 text-xs font-semibold text-amber-700 dark:border-amber-900 dark:bg-amber-500/10 dark:text-amber-300">
              Use the diagram
            </span>
          )}
          {table_ar && (
              <span className="rounded-full border border-blue-200 bg-blue-50 px-3 py-1 text-xs font-semibold text-blue-700 dark:border-blue-900 dark:bg-blue-500/10 dark:text-blue-300">
              Use the table
            </span>
          )}
        </div>
        <div className={clsx(questionClassName, promptHeadingClass)} data-testid={`${testIdPrefix}-text`}>
          <RichTextContent content={text_ar} contentFormat={content_format} />
        </div>
      </div>

      {comparison_columns && (
        <div className="grid gap-3 lg:grid-cols-2" data-testid={`${testIdPrefix}-comparison`}>
          {([
            ['a', 'Column A', comparison_columns.a],
            ['b', 'Column B', comparison_columns.b],
          ] as const).map(([key, label, value]) => (
            <div key={key} className="rounded-[1.75rem] border border-slate-200 bg-white p-4 shadow-[0_18px_45px_-34px_rgba(15,23,42,0.26)] dark:border-slate-800 dark:bg-slate-950">
              <p className={`text-xs font-black uppercase tracking-[0.16em] ${key === 'a' ? 'text-blue-600' : 'text-violet-600'}`}>
                {label}
              </p>
              <RichTextContent
                content={value}
                contentFormat={content_format}
                className="mt-3 text-sm font-semibold leading-relaxed text-slate-700 lg:text-base"
              />
            </div>
          ))}
        </div>
      )}
    </div>
  );

  return (
    <div className="space-y-4">
      {passage_ar && (
        hasLongPassage ? (
          <div className="grid gap-4 lg:grid-cols-[minmax(0,1.1fr)_minmax(0,0.9fr)]">
            <div className={`relative ${passageClassName}`} data-testid={`${testIdPrefix}-passage`}>
              <button type="button" onClick={() => setPassageExpanded(v => !v)} className="absolute top-3 right-3 z-10 text-xs font-bold text-teal-600 hover:text-teal-700 bg-white dark:bg-slate-800 dark:text-teal-400 shadow-sm px-2.5 py-1 rounded-lg border border-teal-200 dark:border-teal-800 transition-all hover:shadow-md">
                {passageExpanded ? '↗ Collapse' : '↙ Expand'}
              </button>
              <p className="mb-3 text-xs font-black uppercase tracking-[0.16em] text-slate-400">Passage</p>
              <RichTextContent content={passage_ar} contentFormat={content_format} className={`${passageExpanded ? 'max-h-none' : 'max-h-[28rem]'} overflow-y-auto leading-[1.9] text-[0.94rem]`} />
            </div>
            <div>{promptBody}</div>
          </div>
        ) : (
          <>
            <div className={passageClassName} data-testid={`${testIdPrefix}-passage`}>
              <p className="mb-3 text-xs font-black uppercase tracking-[0.16em] text-slate-400">Passage</p>
              <RichTextContent content={passage_ar} contentFormat={content_format} className="leading-relaxed" />
            </div>
            {promptBody}
          </>
        )
      )}

      {!passage_ar && promptBody}
    </div>
  );
}
