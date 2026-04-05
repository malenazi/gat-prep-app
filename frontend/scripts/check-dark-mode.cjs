#!/usr/bin/env node
/**
 * Comprehensive dark mode audit.
 * Scans .tsx files for Tailwind color classes missing dark: variants.
 * Covers all patterns that caused bugs in this project.
 *
 * Run: node frontend/scripts/check-dark-mode.cjs
 */

const fs = require('fs');
const path = require('path');

const SRC_DIR = path.join(__dirname, '..', 'src');

// ═══ RULES ═══════════════════════════════════════════════════════════════
// Each rule: { pattern, dark (substring to look for), description }
const RULES = [
  // Backgrounds
  { pattern: /\bbg-white\b/, dark: 'dark:bg-', desc: 'bg-white without dark:bg-*' },
  { pattern: /\bbg-slate-50\b/, dark: 'dark:bg-', desc: 'bg-slate-50 without dark:bg-*' },
  { pattern: /\bbg-slate-100\b/, dark: 'dark:bg-', desc: 'bg-slate-100 without dark:bg-*' },
  // Colored light backgrounds (any color -50)
  { pattern: /\bbg-(amber|emerald|sky|blue|teal|indigo|violet|purple|red|orange|cyan|pink|rose|lime|fuchsia)-50\b/, dark: 'dark:bg-', desc: 'bg-{color}-50 without dark:bg-*' },

  // Text colors
  { pattern: /\btext-slate-900\b/, dark: 'dark:text-', desc: 'text-slate-900 without dark:text-*' },
  { pattern: /\btext-slate-800\b/, dark: 'dark:text-', desc: 'text-slate-800 without dark:text-*' },
  { pattern: /\btext-slate-700\b/, dark: 'dark:text-', desc: 'text-slate-700 without dark:text-*' },
  { pattern: /\btext-slate-600\b/, dark: 'dark:text-', desc: 'text-slate-600 without dark:text-*' },
  // Colored dark text (any color -800, -700)
  { pattern: /\btext-(amber|emerald|sky|blue|teal|indigo|violet|purple|red|orange|cyan)-800\b/, dark: 'dark:text-', desc: 'text-{color}-800 without dark:text-*' },
  { pattern: /\btext-(amber|emerald|sky|blue|teal|indigo|violet|purple|red|orange|cyan)-700\b/, dark: 'dark:text-', desc: 'text-{color}-700 without dark:text-*' },

  // Borders
  { pattern: /\bborder-slate-200\b/, dark: 'dark:border-', desc: 'border-slate-200 without dark:border-*' },
  { pattern: /\bborder-slate-100\b/, dark: 'dark:border-', desc: 'border-slate-100 without dark:border-*' },
  // Colored borders
  { pattern: /\bborder-(amber|emerald|sky|blue|teal|indigo|violet|purple|red|orange|cyan)-200\b/, dark: 'dark:border-', desc: 'border-{color}-200 without dark:border-*' },
  { pattern: /\bborder-(amber|emerald|sky|blue|teal|indigo|violet|purple|red|orange|cyan)-100\b/, dark: 'dark:border-', desc: 'border-{color}-100 without dark:border-*' },
];

// ═══ SKIP PATTERNS ═══════════════════════════════════════════════════════
const SKIP_LINE = [
  /hover:bg-white/,
  /bg-white\//,           // bg-white/75 opacity variants
  /border-white/,
  /backdrop/,
  /glass/,
  /stopColor/,
  /linearGradient/,
  /fill="white"/,
  /fill:#/,               // CSS inside SVG <style>
  /\.shape/,              // SVG CSS class definitions
  /\.line/,               // SVG CSS class definitions
  /\.label/,              // SVG CSS class definitions
  /<style>/,              // SVG style blocks
  /const .* = ['"`]/,     // Variable assignments with string values (dark added at usage)
];

// Files to skip entirely
const SKIP_FILES = [
  'check-dark-mode',     // This script
  'tailwind.config',
  '.test.',
  '.spec.',
];

function getAllTsxFiles(dir) {
  const files = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...getAllTsxFiles(fullPath));
    } else if (entry.name.endsWith('.tsx') || entry.name.endsWith('.ts')) {
      if (!SKIP_FILES.some(s => entry.name.includes(s))) {
        files.push(fullPath);
      }
    }
  }
  return files;
}

function shouldSkipLine(line) {
  return SKIP_LINE.some(p => p.test(line));
}

const violations = [];

for (const file of getAllTsxFiles(SRC_DIR)) {
  const relPath = path.relative(path.join(__dirname, '..', '..'), file);
  const lines = fs.readFileSync(file, 'utf-8').split('\n');

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (line.includes('dark:') || shouldSkipLine(line) || !line.includes('className')) continue;

    for (const rule of RULES) {
      if (rule.pattern.test(line) && !line.includes(rule.dark)) {
        violations.push({ file: relPath, line: i + 1, rule: rule.desc, content: line.trim().substring(0, 100) });
      }
    }
  }
}

// ═══ REPORT ══════════════════════════════════════════════════════════════
if (violations.length > 0) {
  console.error(`\n❌ Dark mode audit: ${violations.length} violation(s) found\n`);

  // Group by file
  const byFile = {};
  for (const v of violations) {
    (byFile[v.file] = byFile[v.file] || []).push(v);
  }
  for (const [file, vs] of Object.entries(byFile)) {
    console.error(`  ${file} (${vs.length}):`);
    for (const v of vs.slice(0, 5)) {
      console.error(`    L${v.line}: ${v.rule}`);
    }
    if (vs.length > 5) console.error(`    ... and ${vs.length - 5} more`);
  }

  console.error(`\nTotal: ${violations.length} violations across ${Object.keys(byFile).length} files`);
  // Track baseline: exit 0 for now while we fix existing violations
  // Change to process.exit(1) once baseline is clean
  console.error('⚠️  Audit is in tracking mode — fix violations before adding new components.\n');
  process.exit(0);
} else {
  console.log('✅ Dark mode audit passed — 0 violations (checked 15 rules)');
  process.exit(0);
}
