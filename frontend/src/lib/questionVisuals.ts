import type { QuestionTable } from '@/types';

const ALLOWED_SVG_TAGS = new Set([
  'svg',
  'g',
  'line',
  'rect',
  'circle',
  'ellipse',
  'polygon',
  'polyline',
  'path',
  'text',
  'tspan',
  'style',
]);

const ALLOWED_SVG_ATTRS = new Set([
  'xmlns',
  'viewBox',
  'width',
  'height',
  'x',
  'y',
  'x1',
  'x2',
  'y1',
  'y2',
  'cx',
  'cy',
  'r',
  'rx',
  'ry',
  'd',
  'points',
  'fill',
  'stroke',
  'stroke-width',
  'stroke-linecap',
  'stroke-linejoin',
  'stroke-dasharray',
  'opacity',
  'fill-opacity',
  'stroke-opacity',
  'transform',
  'font-size',
  'font-family',
  'font-weight',
  'text-anchor',
  'dominant-baseline',
  'preserveAspectRatio',
  'class',
]);

const BLOCKED_SVG_VALUE_SNIPPETS = ['javascript:', 'data:', 'url('];

function localName(name: string) {
  const colonIndex = name.indexOf(':');
  return colonIndex >= 0 ? name.slice(colonIndex + 1) : name;
}

export function sanitizeInlineSvg(svgMarkup?: string | null) {
  if (!svgMarkup?.trim() || typeof DOMParser === 'undefined') return null;

  const parser = new DOMParser();
  const documentNode = parser.parseFromString(svgMarkup, 'image/svg+xml');
  const parseError = documentNode.getElementsByTagName('parsererror')[0];
  const root = documentNode.documentElement;

  if (parseError || !root || root.tagName.toLowerCase() !== 'svg') return null;

  const nodes = [root, ...Array.from(root.querySelectorAll('*'))];
  for (const node of nodes) {
    const tag = localName(node.tagName).toLowerCase();
    if (!ALLOWED_SVG_TAGS.has(tag)) return null;

    for (const attribute of Array.from(node.attributes)) {
      const attr = localName(attribute.name);
      const value = attribute.value.toLowerCase();
      if (attr.startsWith('on')) return null;
      if (!ALLOWED_SVG_ATTRS.has(attr)) return null;
      if (BLOCKED_SVG_VALUE_SNIPPETS.some((snippet) => value.includes(snippet))) return null;
    }
  }

  return new XMLSerializer().serializeToString(root);
}

export function parseTableEditorValue(rawValue: string) {
  if (!rawValue.trim()) return { value: null as QuestionTable | null, error: '' };

  try {
    const parsed = JSON.parse(rawValue) as QuestionTable;
    if (!Array.isArray(parsed.headers) || !parsed.headers.length) {
      return { value: null, error: 'Table headers must be a non-empty array.' };
    }
    if (!Array.isArray(parsed.rows) || !parsed.rows.length) {
      return { value: null, error: 'Table rows must be a non-empty array.' };
    }
    const width = parsed.headers.length;
    for (const row of parsed.rows) {
      if (!Array.isArray(row) || row.length !== width || row.some((cell) => typeof cell !== 'string')) {
        return { value: null, error: 'Each row must match the header count and contain only strings.' };
      }
    }
    return { value: parsed, error: '' };
  } catch {
    return { value: null, error: 'Table JSON is invalid.' };
  }
}
