import katex from 'katex';

import type { QuestionContentFormat } from '@/types';

export type TextSize = 'normal' | 'large';
export type Density = 'comfortable' | 'compact';
export type Contrast = 'default' | 'high';

export interface QuestionAppearance {
  textSize: TextSize;
  density: Density;
  contrast: Contrast;
  answerMasking: boolean;
}

const STORAGE_KEY = 'question_view_preferences';

export const defaultQuestionAppearance: QuestionAppearance = {
  textSize: 'normal',
  density: 'comfortable',
  contrast: 'default',
  answerMasking: false,
};

export function loadQuestionAppearance(): QuestionAppearance {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return defaultQuestionAppearance;
    const parsed = JSON.parse(raw) as Partial<QuestionAppearance>;
    return {
      textSize: parsed.textSize === 'large' ? 'large' : 'normal',
      density: parsed.density === 'compact' ? 'compact' : 'comfortable',
      contrast: parsed.contrast === 'high' ? 'high' : 'default',
      answerMasking: parsed.answerMasking === true,
    };
  } catch {
    return defaultQuestionAppearance;
  }
}

export function saveQuestionAppearance(value: QuestionAppearance) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(value));
}

export function getQuestionTextScale(textSize: TextSize) {
  return textSize === 'large' ? 'question-text-large' : 'question-text-normal';
}

export function getQuestionDensityClass(density: Density) {
  return density === 'compact' ? 'question-density-compact' : 'question-density-comfortable';
}

export function getQuestionContrastClass(contrast: Contrast) {
  return contrast === 'high' ? 'question-contrast-high' : 'question-contrast-default';
}

export function isMarkdownMath(contentFormat?: QuestionContentFormat | null) {
  return contentFormat === 'markdown_math';
}

const probableMathPatterns = [
  /\$[^$]+\$/s,
  /\\(?:frac|pi|sqrt|times|div|leq|geq|neq|pm|theta|alpha|beta|gamma|cdot|approx|left|right)\b/,
];

export function shouldUseMarkdownMath(contentFormat?: QuestionContentFormat | null, content?: string | null) {
  if (isMarkdownMath(contentFormat)) {
    return true;
  }

  const value = content?.trim();
  if (!value) {
    return false;
  }

  return probableMathPatterns.some((pattern) => pattern.test(value));
}

export function validateMarkdownMathFields(fields: Array<{ label: string; value?: string | null }>) {
  const issues: string[] = [];
  const mathPattern = /\${1,2}([\s\S]+?)\${1,2}/g;

  for (const field of fields) {
    const value = field.value?.trim();
    if (!value) continue;

    let match: RegExpExecArray | null;
    mathPattern.lastIndex = 0;
    while ((match = mathPattern.exec(value)) !== null) {
      try {
        katex.renderToString(match[1], { throwOnError: true, output: 'htmlAndMathml' });
      } catch (error) {
        issues.push(`${field.label}: ${(error as Error).message}`);
        break;
      }
    }
  }

  return issues;
}
