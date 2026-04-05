#!/usr/bin/env node
/**
 * Dark mode audit script.
 * Scans .tsx files for Tailwind color classes missing dark: variants.
 * Run: node frontend/scripts/check-dark-mode.js
 */

const fs = require('fs');
const path = require('path');

const SRC_DIR = path.join(__dirname, '..', 'src');

// Patterns that MUST have a dark: counterpart when used in className
const RULES = [
  { pattern: /\bbg-white\b/, dark: 'dark:bg-slate-', description: 'bg-white without dark:bg-*' },
  { pattern: /\btext-slate-800\b/, dark: 'dark:text-slate-', description: 'text-slate-800 without dark:text-*' },
  { pattern: /\bborder-slate-200\b/, dark: 'dark:border-', description: 'border-slate-200 without dark:border-*' },
  { pattern: /\bborder-slate-100\b/, dark: 'dark:border-', description: 'border-slate-100 without dark:border-*' },
  { pattern: /\bbg-slate-50\b/, dark: 'dark:bg-slate-', description: 'bg-slate-50 without dark:bg-*' },
];

// Patterns to skip (false positives)
const SKIP_PATTERNS = [
  /hover:bg-white/,
  /bg-white\//,       // bg-white/75 etc (opacity variants often in glass)
  /border-white/,
  /backdrop/,
  /glass/,
  /stopColor/,
  /linearGradient/,
  /fill="white"/,
];

function getAllTsxFiles(dir) {
  const files = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...getAllTsxFiles(fullPath));
    } else if (entry.name.endsWith('.tsx')) {
      files.push(fullPath);
    }
  }
  return files;
}

function shouldSkipLine(line) {
  return SKIP_PATTERNS.some(p => p.test(line));
}

let totalViolations = 0;
const violations = [];

for (const file of getAllTsxFiles(SRC_DIR)) {
  const relPath = path.relative(path.join(__dirname, '..', '..'), file);
  const lines = fs.readFileSync(file, 'utf-8').split('\n');

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // Skip lines that already have dark: variant or are in skip patterns
    if (line.includes('dark:') || shouldSkipLine(line) || !line.includes('className')) continue;

    for (const rule of RULES) {
      if (rule.pattern.test(line) && !line.includes(rule.dark)) {
        totalViolations++;
        violations.push({
          file: relPath,
          line: i + 1,
          rule: rule.description,
          content: line.trim().substring(0, 100),
        });
      }
    }
  }
}

if (violations.length > 0) {
  console.error(`\n❌ Dark mode audit: ${totalViolations} violation(s) found\n`);
  for (const v of violations.slice(0, 20)) {
    console.error(`  ${v.file}:${v.line} — ${v.rule}`);
    console.error(`    ${v.content}...`);
  }
  if (violations.length > 20) {
    console.error(`  ... and ${violations.length - 20} more`);
  }
  // Warn but don't block CI (set to process.exit(1) once all violations are fixed)
  console.error(`\n⚠️  Fix these before adding new components.\n`);
  process.exit(0);
} else {
  console.log('✅ Dark mode audit passed — no violations found');
  process.exit(0);
}
