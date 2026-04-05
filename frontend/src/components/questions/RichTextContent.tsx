import clsx from 'clsx';
import ReactMarkdown from 'react-markdown';
import rehypeKatex from 'rehype-katex';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';

import type { QuestionContentFormat } from '@/types';
import { shouldUseMarkdownMath } from '@/lib/questionPresentation';

interface RichTextContentProps {
  content: string;
  contentFormat?: QuestionContentFormat | null;
  className?: string;
  inline?: boolean;
}

export function RichTextContent({
  content,
  contentFormat = 'plain',
  className,
  inline = false,
}: RichTextContentProps) {
  if (!content.trim()) return null;

  if (!shouldUseMarkdownMath(contentFormat, content)) {
    const PlainTag = inline ? 'span' : 'div';
    return <PlainTag className={clsx('whitespace-pre-line', className)}>{content}</PlainTag>;
  }

  const Wrapper = inline ? 'span' : 'div';

  return (
    <Wrapper className={clsx('question-rich-text', inline && 'question-rich-inline', className)}>
      <ReactMarkdown
        remarkPlugins={[remarkGfm, remarkMath]}
        rehypePlugins={[[rehypeKatex, { output: 'htmlAndMathml', throwOnError: false }]]}
        components={{
          p: ({ children }) => (inline ? <span>{children}</span> : <p>{children}</p>),
          li: ({ children }) => <li>{children}</li>,
          table: ({ children }) => <table>{children}</table>,
        }}
      >
        {content}
      </ReactMarkdown>
    </Wrapper>
  );
}
