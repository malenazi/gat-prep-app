#!/usr/bin/env node
/**
 * SVG & Recharts hardcoded color audit.
 * Flags hex colors in TSX that won't adapt to dark mode.
 *
 * Run: node frontend/scripts/check-svg-colors.cjs
 */

const fs = require('fs');
const path = require('path');

const SRC_DIR = path.join(__dirname, '..', 'src');

// Brand colors that work in both light and dark mode — allowed
const ALLOWED_COLORS = new Set([
  '#00c8a0', '#00a888', '#0d9488', '#14b8a6', '#0891b2',  // teal/brand
  '#22c55e', '#10b981', '#059669',                          // green/emerald
  '#3b82f6', '#2563eb',                                     // blue
  '#8b5cf6', '#7c3aed',                                     // violet
  '#f59e0b', '#d97706', '#fbbf24',                          // amber
  '#ef4444', '#dc2626',                                     // red
  '#06b6d4',                                                // cyan
  '#ec4899',                                                // pink
  '#94a3b8', '#64748b',                                     // slate mid-tones (visible in both)
]);

// Patterns that indicate "safe" usage
const SAFE_PATTERNS = [
  /stopColor/,           // SVG gradient stops
  /linearGradient/,
  /radialGradient/,
  /<style>/,             // SVG CSS blocks
  /class="/,             // Using CSS classes (good)
  /className="/,         // React className
  /currentColor/,
  /url\(#/,              // SVG gradient reference
  /fillOpacity/,
  /strokeOpacity/,
];

// Colors that are KNOWN BAD in dark mode — always flag
const BAD_COLORS = new Set([
  '#e2e8f0', '#f1f5f9', '#f8fafc',  // slate-200/100/50 — invisible in dark
  '#ffffff', '#fff',                   // pure white fills
  '#f9fafb', '#f3f4f6', '#e5e7eb',   // gray-50/100/200
]);

function getAllTsxFiles(dir) {
  const files = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) files.push(...getAllTsxFiles(fullPath));
    else if (entry.name.endsWith('.tsx')) files.push(fullPath);
  }
  return files;
}

const warnings = [];

for (const file of getAllTsxFiles(SRC_DIR)) {
  const relPath = path.relative(path.join(__dirname, '..', '..'), file);
  const lines = fs.readFileSync(file, 'utf-8').split('\n');

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // Skip safe patterns
    if (SAFE_PATTERNS.some(p => p.test(line))) continue;

    // Find hardcoded hex colors in stroke/fill attributes and JS objects
    const hexMatches = line.matchAll(/(stroke|fill)(?:="|:\s*')#([0-9a-fA-F]{3,8})/g);
    for (const match of hexMatches) {
      const hex = `#${match[2].toLowerCase()}`;
      if (ALLOWED_COLORS.has(hex)) continue;

      const severity = BAD_COLORS.has(hex) ? 'ERROR' : 'WARN';
      warnings.push({ file: relPath, line: i + 1, color: hex, attr: match[1], severity });
    }
  }
}

// Report
const errors = warnings.filter(w => w.severity === 'ERROR');
const warns = warnings.filter(w => w.severity === 'WARN');

if (errors.length > 0) {
  console.error(`\n❌ SVG color audit: ${errors.length} error(s), ${warns.length} warning(s)\n`);
  console.error('ERRORS (known bad colors for dark mode):');
  for (const e of errors) {
    console.error(`  ${e.file}:${e.line} — ${e.attr}="${e.color}"`);
  }
  if (warns.length > 0) {
    console.error(`\nWARNINGS (unlisted colors — verify they work in dark mode):`);
    for (const w of warns.slice(0, 10)) {
      console.error(`  ${w.file}:${w.line} — ${w.attr}="${w.color}"`);
    }
  }
  process.exit(1);
} else if (warns.length > 0) {
  console.log(`⚠️  SVG color audit: ${warns.length} warning(s) — verify these colors work in dark mode`);
  for (const w of warns.slice(0, 10)) {
    console.log(`  ${w.file}:${w.line} — ${w.attr}="${w.color}"`);
  }
  process.exit(0); // Warnings don't block
} else {
  console.log('✅ SVG color audit passed — no hardcoded colors found');
  process.exit(0);
}
