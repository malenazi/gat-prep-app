import { useState, useEffect, useRef, useCallback } from 'react';
import { ScoreRing } from '@/components/shared/ScoreRing';
import { Clock, BookOpen, Calculator, CheckCircle, XCircle, Sparkles, Shield, BarChart3 } from 'lucide-react';

/* ───────────────────── Types ───────────────────── */

interface TrialSessionProps {
  onRegister: () => void;
  onBack: () => void;
}

interface TrialQuestion {
  id: string;
  skill_name: string;
  skill_id: string;
  section: 'verbal' | 'quantitative';
  text_ar: string;
  passage_ar?: string;
  options: { key: string; label: string; text_ar: string }[];
  correct_option: string;
  explanation_ar: string;
}

interface AnswerRecord {
  qid: string;
  selected: string;
  correct: string;
  isCorrect: boolean;
  skill_id: string;
  section: 'verbal' | 'quantitative';
}

type SessionPhase = 'intro' | 'diagnostic' | 'diagnostic-feedback' | 'diagnostic-results' | 'practice' | 'practice-feedback' | 'final-report';

interface TrialState {
  phase: SessionPhase;
  diagnosticIndex: number;
  practiceIndex: number;
  diagnosticAnswers: AnswerRecord[];
  practiceAnswers: AnswerRecord[];
}

/* ───────────────────── Constants ───────────────────── */

const TRIAL_KEY = 'trial_session_v2';
const DIAG_TIMER = 60;
const PRAC_TIMER = 90;
const XP_CORRECT = 10;
const XP_WRONG = 5;

/* ───────────────────── Questions: Diagnostic (14) ───────────────────── */

const DIAGNOSTIC_QUESTIONS: TrialQuestion[] = [
  // ── Reading Comprehension (2) ──
  {
    id: 'd1', skill_name: 'Reading Comprehension', skill_id: 'reading', section: 'verbal',
    passage_ar: 'Studies indicate that reading for thirty minutes daily enhances linguistic abilities and develops vocabulary, while also improving concentration and long-term memory for all age groups.',
    text_ar: 'According to the text, what is the direct benefit of daily reading?',
    options: [
      { key: 'a', label: 'A', text_ar: 'Obtaining an academic degree' },
      { key: 'b', label: 'B', text_ar: 'Enhancing linguistic abilities and concentration' },
      { key: 'c', label: 'C', text_ar: 'Reducing required sleep hours' },
      { key: 'd', label: 'D', text_ar: 'Replacing traditional education' },
    ],
    correct_option: 'b',
    explanation_ar: 'The text states that daily reading "enhances linguistic abilities and develops vocabulary" and improves concentration and memory.',
  },
  {
    id: 'd2', skill_name: 'Reading Comprehension', skill_id: 'reading', section: 'verbal',
    passage_ar: 'Fresh water has become a scarce resource in many parts of the world due to industrial pollution and rapid population growth. Governments are turning to seawater desalination as a strategic solution despite its high cost.',
    text_ar: 'According to the text, what is the main cause of fresh water scarcity?',
    options: [
      { key: 'a', label: 'A', text_ar: 'High desalination costs' },
      { key: 'b', label: 'B', text_ar: 'Lack of rain worldwide' },
      { key: 'c', label: 'C', text_ar: 'Industrial pollution and population growth' },
      { key: 'd', label: 'D', text_ar: 'Using water only for agriculture' },
    ],
    correct_option: 'c',
    explanation_ar: 'The text mentions that the cause is "industrial pollution and rapid population growth".',
  },
  // ── Verbal Analogy (2) ──
  {
    id: 'd3', skill_name: 'Verbal Analogy', skill_id: 'analogy', section: 'verbal',
    text_ar: 'Pen : Writing',
    options: [
      { key: 'a', label: 'A', text_ar: 'Hammer : Construction' },
      { key: 'b', label: 'B', text_ar: 'Car : Road' },
      { key: 'c', label: 'C', text_ar: 'Book : Shelf' },
      { key: 'd', label: 'D', text_ar: 'School : Student' },
    ],
    correct_option: 'a',
    explanation_ar: 'Relationship: Tool → Function. A pen is a tool for writing, and a hammer is a tool for construction.',
  },
  {
    id: 'd4', skill_name: 'Verbal Analogy', skill_id: 'analogy', section: 'verbal',
    text_ar: 'Eye : Vision',
    options: [
      { key: 'a', label: 'A', text_ar: 'Hand : Body' },
      { key: 'b', label: 'B', text_ar: 'Ear : Hearing' },
      { key: 'c', label: 'C', text_ar: 'Head : Thinking' },
      { key: 'd', label: 'D', text_ar: 'Foot : Walking' },
    ],
    correct_option: 'b',
    explanation_ar: 'Relationship: Sensory organ → Sensory function. The eye is for vision, and the ear is for hearing.',
  },
  // ── Sentence Completion (1) ──
  {
    id: 'd5', skill_name: 'Sentence Completion', skill_id: 'completion', section: 'verbal',
    text_ar: 'Patience is the key to _____ , and whoever is patient will succeed.',
    options: [
      { key: 'a', label: 'A', text_ar: 'Loss' },
      { key: 'b', label: 'B', text_ar: 'Relief' },
      { key: 'c', label: 'C', text_ar: 'Sadness' },
      { key: 'd', label: 'D', text_ar: 'Hesitation' },
    ],
    correct_option: 'b',
    explanation_ar: 'The context is positive (whoever is patient will succeed), so patience is the key to relief — a famous Arabic expression.',
  },
  // ── Contextual Error (1) ──
  {
    id: 'd6', skill_name: 'Contextual Error', skill_id: 'context-error', section: 'verbal',
    text_ar: 'The scientist is distinguished by humility and (arrogance) in dealing with others.',
    options: [
      { key: 'a', label: 'A', text_ar: 'is distinguished' },
      { key: 'b', label: 'B', text_ar: 'humility' },
      { key: 'c', label: 'C', text_ar: 'arrogance' },
      { key: 'd', label: 'D', text_ar: 'dealing' },
    ],
    correct_option: 'c',
    explanation_ar: 'Arrogance contradicts humility. The context is positive, so the correct word should be "courtesy" or "good manners" instead of "arrogance".',
  },
  // ── Odd Word Out (1) ──
  {
    id: 'd7', skill_name: 'Odd Word Out', skill_id: 'odd-word', section: 'verbal',
    text_ar: 'Which of the following words does not belong to the group?',
    options: [
      { key: 'a', label: 'A', text_ar: 'Apple' },
      { key: 'b', label: 'B', text_ar: 'Banana' },
      { key: 'c', label: 'C', text_ar: 'Carrot' },
      { key: 'd', label: 'D', text_ar: 'Grape' },
    ],
    correct_option: 'c',
    explanation_ar: 'Apple, Banana, Grape are fruits. Carrot is a vegetable. The odd word: Carrot.',
  },
  // ── Arithmetic (2) ──
  {
    id: 'd8', skill_name: 'Arithmetic', skill_id: 'arithmetic', section: 'quantitative',
    text_ar: 'If the price of 3 books = 45 riyals\nWhat is the price of 7 books?',
    options: [
      { key: 'a', label: 'A', text_ar: '90 riyals' },
      { key: 'b', label: 'B', text_ar: '105 riyals' },
      { key: 'c', label: 'C', text_ar: '115 riyals' },
      { key: 'd', label: 'D', text_ar: '120 riyals' },
    ],
    correct_option: 'b',
    explanation_ar: 'Price of one book = 45 ÷ 3 = 15 riyals\nPrice of 7 books = 15 × 7 = 105 riyals',
  },
  {
    id: 'd9', skill_name: 'Arithmetic', skill_id: 'arithmetic', section: 'quantitative',
    text_ar: 'What is the result: 25% of 240?',
    options: [
      { key: 'a', label: 'A', text_ar: '48' },
      { key: 'b', label: 'B', text_ar: '60' },
      { key: 'c', label: 'C', text_ar: '72' },
      { key: 'd', label: 'D', text_ar: '80' },
    ],
    correct_option: 'b',
    explanation_ar: '25% of 240 = 240 × 0.25 = 60',
  },
  // ── Geometry (2) ──
  {
    id: 'd10', skill_name: 'Geometry', skill_id: 'geometry', section: 'quantitative',
    text_ar: 'A square with side length of 9 cm.\nWhat is its perimeter?',
    options: [
      { key: 'a', label: 'A', text_ar: '18 cm' },
      { key: 'b', label: 'B', text_ar: '27 cm' },
      { key: 'c', label: 'C', text_ar: '36 cm' },
      { key: 'd', label: 'D', text_ar: '81 cm' },
    ],
    correct_option: 'c',
    explanation_ar: 'Perimeter of square = 4 × side length = 4 × 9 = 36 cm',
  },
  {
    id: 'd11', skill_name: 'Geometry', skill_id: 'geometry', section: 'quantitative',
    text_ar: 'A right triangle, hypotenuse = 13 cm and one side = 5 cm.\nWhat is the length of the third side?',
    options: [
      { key: 'a', label: 'A', text_ar: '8 cm' },
      { key: 'b', label: 'B', text_ar: '10 cm' },
      { key: 'c', label: 'C', text_ar: '12 cm' },
      { key: 'd', label: 'D', text_ar: '14 cm' },
    ],
    correct_option: 'c',
    explanation_ar: 'Using Pythagorean theorem:\nSide² = Hypotenuse² − Other side²\nSide² = 13² − 5² = 169 − 25 = 144\nSide = 12 cm',
  },
  // ── Algebra (1) ──
  {
    id: 'd12', skill_name: 'Algebra', skill_id: 'algebra', section: 'quantitative',
    text_ar: 'If:\n3x − 5 = 16\nWhat is the value of x?',
    options: [
      { key: 'a', label: 'A', text_ar: '3' },
      { key: 'b', label: 'B', text_ar: '5' },
      { key: 'c', label: 'C', text_ar: '7' },
      { key: 'd', label: 'D', text_ar: '9' },
    ],
    correct_option: 'c',
    explanation_ar: '3x − 5 = 16\n3x = 16 + 5 = 21\nx = 21 ÷ 3 = 7',
  },
  // ── Statistics (1) ──
  {
    id: 'd13', skill_name: 'Statistics', skill_id: 'statistics', section: 'quantitative',
    text_ar: 'What is the arithmetic mean of the numbers:\n10, 20, 30, 40?',
    options: [
      { key: 'a', label: 'A', text_ar: '20' },
      { key: 'b', label: 'B', text_ar: '25' },
      { key: 'c', label: 'C', text_ar: '30' },
      { key: 'd', label: 'D', text_ar: '35' },
    ],
    correct_option: 'b',
    explanation_ar: 'Mean = Sum of values ÷ Count\n= (10 + 20 + 30 + 40) ÷ 4\n= 100 ÷ 4 = 25',
  },
  // ── Comparison (1) ──
  {
    id: 'd14', skill_name: 'Comparison', skill_id: 'comparison', section: 'quantitative',
    text_ar: 'Compare between:\nFirst value: 3⁴\nSecond value: 4³',
    options: [
      { key: 'a', label: 'A', text_ar: 'First is greater' },
      { key: 'b', label: 'B', text_ar: 'Second is greater' },
      { key: 'c', label: 'C', text_ar: 'Equal' },
      { key: 'd', label: 'D', text_ar: 'Cannot be determined' },
    ],
    correct_option: 'a',
    explanation_ar: '3⁴ = 81\n4³ = 64\nThe first value (81) is greater than the second (64).',
  },
];

/* ───────────────────── Questions: Practice (20) ───────────────────── */

const PRACTICE_QUESTIONS: TrialQuestion[] = [
  // ── Reading Comprehension (3) ──
  {
    id: 'p1', skill_name: 'Reading Comprehension', skill_id: 'reading', section: 'verbal',
    passage_ar: 'Saudi Arabia has witnessed a major economic transformation under Vision 2030, diversifying income sources away from total dependence on oil, with tourism, entertainment, and technology sectors emerging as new economic drivers.',
    text_ar: 'According to the text, what is the main goal of the economic transformation?',
    options: [
      { key: 'a', label: 'A', text_ar: 'Increasing oil production' },
      { key: 'b', label: 'B', text_ar: 'Diversifying income sources' },
      { key: 'c', label: 'C', text_ar: 'Reducing population' },
      { key: 'd', label: 'D', text_ar: 'Closing the private sector' },
    ],
    correct_option: 'b',
    explanation_ar: 'The text clarifies that the transformation aims to "diversify income sources away from total dependence on oil".',
  },
  {
    id: 'p2', skill_name: 'Reading Comprehension', skill_id: 'reading', section: 'verbal',
    passage_ar: 'Scientists discovered that bees communicate through precise dances known as the "waggle dance," through which they determine the direction of the nectar source and its distance from the hive with amazing accuracy.',
    text_ar: 'What is the function of the waggle dance in bees?',
    options: [
      { key: 'a', label: 'A', text_ar: 'Entertainment inside the hive' },
      { key: 'b', label: 'B', text_ar: 'Driving enemies away from the hive' },
      { key: 'c', label: 'C', text_ar: 'Determining direction and distance of nectar source' },
      { key: 'd', label: 'D', text_ar: 'Regulating hive temperature' },
    ],
    correct_option: 'c',
    explanation_ar: 'The text mentions that bees "determine through it the direction of the nectar source and its distance from the hive".',
  },
  {
    id: 'p3', skill_name: 'Reading Comprehension', skill_id: 'reading', section: 'verbal',
    passage_ar: 'Psychologists believe that learning by practice is more effective than learning by memorization, as the brain creates stronger neural connections when applying information practically compared to merely repeating it verbally.',
    text_ar: 'Why is learning by practice more effective according to the text?',
    options: [
      { key: 'a', label: 'A', text_ar: 'Because it requires no time' },
      { key: 'b', label: 'B', text_ar: 'Because it creates stronger neural connections' },
      { key: 'c', label: 'C', text_ar: 'Because it relies on memorization' },
      { key: 'd', label: 'D', text_ar: 'Because it reduces the need for a teacher' },
    ],
    correct_option: 'b',
    explanation_ar: 'The text clarifies that the brain "creates stronger neural connections when applying information practically".',
  },
  // ── Verbal Analogy (2) ──
  {
    id: 'p4', skill_name: 'Verbal Analogy', skill_id: 'analogy', section: 'verbal',
    text_ar: 'Sun : Day',
    options: [
      { key: 'a', label: 'A', text_ar: 'Moon : Night' },
      { key: 'b', label: 'B', text_ar: 'Star : Sky' },
      { key: 'c', label: 'C', text_ar: 'Cloud : Rain' },
      { key: 'd', label: 'D', text_ar: 'Sea : Wave' },
    ],
    correct_option: 'a',
    explanation_ar: 'Relationship: Celestial body → Time period associated with it. The sun is associated with day, and the moon is associated with night.',
  },
  {
    id: 'p5', skill_name: 'Verbal Analogy', skill_id: 'analogy', section: 'verbal',
    text_ar: 'Wing : Bird',
    options: [
      { key: 'a', label: 'A', text_ar: 'Tail : Horse' },
      { key: 'b', label: 'B', text_ar: 'Fin : Fish' },
      { key: 'c', label: 'C', text_ar: 'Feather : Chicken' },
      { key: 'd', label: 'D', text_ar: 'Nest : Sparrow' },
    ],
    correct_option: 'b',
    explanation_ar: 'Relationship: Movement organ → Living being. The wing is the bird\'s means of movement, and the fin is the fish\'s means of movement.',
  },
  // ── Sentence Completion (2) ──
  {
    id: 'p6', skill_name: 'Sentence Completion', skill_id: 'completion', section: 'verbal',
    text_ar: 'Whoever strives hard _____ , and whoever plants will harvest.',
    options: [
      { key: 'a', label: 'A', text_ar: 'fails' },
      { key: 'b', label: 'B', text_ar: 'succeeds' },
      { key: 'c', label: 'C', text_ar: 'regrets' },
      { key: 'd', label: 'D', text_ar: 'loses' },
    ],
    correct_option: 'b',
    explanation_ar: 'Famous Arabic proverb: "Whoever strives hard succeeds." The context is positive, matching "whoever plants will harvest."',
  },
  {
    id: 'p7', skill_name: 'Sentence Completion', skill_id: 'completion', section: 'verbal',
    text_ar: 'Cooperation among colleagues strengthens _____ and achieves shared goals.',
    options: [
      { key: 'a', label: 'A', text_ar: 'disputes' },
      { key: 'b', label: 'B', text_ar: 'bonds' },
      { key: 'c', label: 'C', text_ar: 'competition' },
      { key: 'd', label: 'D', text_ar: 'isolation' },
    ],
    correct_option: 'b',
    explanation_ar: 'The context is positive (strengthens + achieves goals). Cooperation strengthens "bonds" between colleagues.',
  },
  // ── Contextual Error (2) ──
  {
    id: 'p8', skill_name: 'Contextual Error', skill_id: 'context-error', section: 'verbal',
    text_ar: 'Success requires (laziness), determination, and continuous perseverance.',
    options: [
      { key: 'a', label: 'A', text_ar: 'Success' },
      { key: 'b', label: 'B', text_ar: 'laziness' },
      { key: 'c', label: 'C', text_ar: 'determination' },
      { key: 'd', label: 'D', text_ar: 'continuous' },
    ],
    correct_option: 'b',
    explanation_ar: '"Laziness" contradicts the context of success and determination. The correct word should be "diligence" or "hard work".',
  },
  {
    id: 'p9', skill_name: 'Contextual Error', skill_id: 'context-error', section: 'verbal',
    text_ar: 'Smoking contributes to (improving) human health and causing serious diseases.',
    options: [
      { key: 'a', label: 'A', text_ar: 'contributes' },
      { key: 'b', label: 'B', text_ar: 'improving' },
      { key: 'c', label: 'C', text_ar: 'health' },
      { key: 'd', label: 'D', text_ar: 'serious' },
    ],
    correct_option: 'b',
    explanation_ar: 'The sentence context is negative (causing serious diseases). The correct word should be "destroying" or "weakening" instead of "improving".',
  },
  // ── Odd Word Out (1) ──
  {
    id: 'p10', skill_name: 'Odd Word Out', skill_id: 'odd-word', section: 'verbal',
    text_ar: 'Which of the following words does not belong to the group?',
    options: [
      { key: 'a', label: 'A', text_ar: 'Riyadh' },
      { key: 'b', label: 'B', text_ar: 'Jeddah' },
      { key: 'c', label: 'C', text_ar: 'Nile' },
      { key: 'd', label: 'D', text_ar: 'Dammam' },
    ],
    correct_option: 'c',
    explanation_ar: 'Riyadh, Jeddah, Dammam are Saudi cities. The Nile is a river in Egypt. The odd word: Nile.',
  },
  // ── Arithmetic (3) ──
  {
    id: 'p11', skill_name: 'Arithmetic', skill_id: 'arithmetic', section: 'quantitative',
    text_ar: 'Ahmed bought 5 pens at 3 riyals each, and 3 notebooks at 8 riyals each.\nWhat is the total amount?',
    options: [
      { key: 'a', label: 'A', text_ar: '39 riyals' },
      { key: 'b', label: 'B', text_ar: '41 riyals' },
      { key: 'c', label: 'C', text_ar: '45 riyals' },
      { key: 'd', label: 'D', text_ar: '48 riyals' },
    ],
    correct_option: 'a',
    explanation_ar: 'Cost of pens = 5 × 3 = 15 riyals\nCost of notebooks = 3 × 8 = 24 riyals\nTotal = 15 + 24 = 39 riyals',
  },
  {
    id: 'p12', skill_name: 'Arithmetic', skill_id: 'arithmetic', section: 'quantitative',
    text_ar: 'If an employee\'s salary = 9000 riyals, and received a 15% raise\nWhat is the new salary?',
    options: [
      { key: 'a', label: 'A', text_ar: '9750 riyals' },
      { key: 'b', label: 'B', text_ar: '10350 riyals' },
      { key: 'c', label: 'C', text_ar: '10500 riyals' },
      { key: 'd', label: 'D', text_ar: '11000 riyals' },
    ],
    correct_option: 'b',
    explanation_ar: 'Raise amount = 9000 × 0.15 = 1350 riyals\nNew salary = 9000 + 1350 = 10350 riyals',
  },
  {
    id: 'p13', skill_name: 'Arithmetic', skill_id: 'arithmetic', section: 'quantitative',
    text_ar: 'A train travels at 120 km/h.\nHow many kilometers does it cover in 45 minutes?',
    options: [
      { key: 'a', label: 'A', text_ar: '60 km' },
      { key: 'b', label: 'B', text_ar: '80 km' },
      { key: 'c', label: 'C', text_ar: '90 km' },
      { key: 'd', label: 'D', text_ar: '100 km' },
    ],
    correct_option: 'c',
    explanation_ar: '45 minutes = 45 ÷ 60 = 0.75 hour\nDistance = Speed × Time = 120 × 0.75 = 90 km',
  },
  // ── Geometry (3) ──
  {
    id: 'p14', skill_name: 'Geometry', skill_id: 'geometry', section: 'quantitative',
    text_ar: 'A circle with radius = 7 cm.\nWhat is its approximate area? (π = ²²⁄₇)',
    options: [
      { key: 'a', label: 'A', text_ar: '44 cm²' },
      { key: 'b', label: 'B', text_ar: '154 cm²' },
      { key: 'c', label: 'C', text_ar: '22 cm²' },
      { key: 'd', label: 'D', text_ar: '308 cm²' },
    ],
    correct_option: 'b',
    explanation_ar: 'Area = π × r²\n= ²²⁄₇ × 7²\n= ²²⁄₇ × 49\n= 22 × 7 = 154 cm²',
  },
  {
    id: 'p15', skill_name: 'Geometry', skill_id: 'geometry', section: 'quantitative',
    text_ar: 'Parallelogram: Base = 10 cm, Height = 6 cm.\nWhat is its area?',
    options: [
      { key: 'a', label: 'A', text_ar: '16 cm²' },
      { key: 'b', label: 'B', text_ar: '30 cm²' },
      { key: 'c', label: 'C', text_ar: '60 cm²' },
      { key: 'd', label: 'D', text_ar: '120 cm²' },
    ],
    correct_option: 'c',
    explanation_ar: 'Area of parallelogram = Base × Height\n= 10 × 6 = 60 cm²',
  },
  {
    id: 'p16', skill_name: 'Geometry', skill_id: 'geometry', section: 'quantitative',
    text_ar: 'A cube with side length = 4 cm.\nWhat is its volume?',
    options: [
      { key: 'a', label: 'A', text_ar: '16 cm³' },
      { key: 'b', label: 'B', text_ar: '48 cm³' },
      { key: 'c', label: 'C', text_ar: '64 cm³' },
      { key: 'd', label: 'D', text_ar: '96 cm³' },
    ],
    correct_option: 'c',
    explanation_ar: 'Volume of cube = side³\n= 4³ = 4 × 4 × 4 = 64 cm³',
  },
  // ── Algebra (2) ──
  {
    id: 'p17', skill_name: 'Algebra', skill_id: 'algebra', section: 'quantitative',
    text_ar: 'If:\nx + y = 12\nx − y = 4\nWhat is the value of x?',
    options: [
      { key: 'a', label: 'A', text_ar: '6' },
      { key: 'b', label: 'B', text_ar: '8' },
      { key: 'c', label: 'C', text_ar: '10' },
      { key: 'd', label: 'D', text_ar: '4' },
    ],
    correct_option: 'b',
    explanation_ar: 'By adding the two equations:\n(x + y) + (x − y) = 12 + 4\n2x = 16\nx = 8',
  },
  {
    id: 'p18', skill_name: 'Algebra', skill_id: 'algebra', section: 'quantitative',
    text_ar: 'If:\nx² − 9 = 0\nWhat are the possible values of x?',
    options: [
      { key: 'a', label: 'A', text_ar: '3 only' },
      { key: 'b', label: 'B', text_ar: '−3 only' },
      { key: 'c', label: 'C', text_ar: '3 or −3' },
      { key: 'd', label: 'D', text_ar: '9 or −9' },
    ],
    correct_option: 'c',
    explanation_ar: 'x² − 9 = 0\nx² = 9\nx = ±3\nPossible values: 3 or −3',
  },
  // ── Statistics (2) ──
  {
    id: 'p19', skill_name: 'Statistics', skill_id: 'statistics', section: 'quantitative',
    text_ar: 'What is the mode (most frequent value) in the following data:\n5, 3, 7, 3, 9, 3, 8?',
    options: [
      { key: 'a', label: 'A', text_ar: '5' },
      { key: 'b', label: 'B', text_ar: '3' },
      { key: 'c', label: 'C', text_ar: '7' },
      { key: 'd', label: 'D', text_ar: '9' },
    ],
    correct_option: 'b',
    explanation_ar: 'The number 3 appears 3 times, which is the most frequent.\nTherefore, the mode = 3',
  },
  {
    id: 'p20', skill_name: 'Statistics', skill_id: 'statistics', section: 'quantitative',
    text_ar: 'If the probability of a student passing the exam = 0.7\nWhat is the probability of failing?',
    options: [
      { key: 'a', label: 'A', text_ar: '0.7' },
      { key: 'b', label: 'B', text_ar: '0.3' },
      { key: 'c', label: 'C', text_ar: '0.5' },
      { key: 'd', label: 'D', text_ar: '1.3' },
    ],
    correct_option: 'b',
    explanation_ar: 'Probability of event + Probability of non-event = 1\nProbability of failing = 1 − 0.7 = 0.3',
  },
];

/* ───────────────────── Skill Map ───────────────────── */

const SKILL_NAMES: Record<string, string> = {
  reading: 'Reading Comprehension',
  analogy: 'Verbal Analogy',
  completion: 'Sentence Completion',
  'context-error': 'Contextual Error',
  'odd-word': 'Odd Word Out',
  arithmetic: 'Arithmetic',
  geometry: 'Geometry',
  algebra: 'Algebra',
  statistics: 'Statistics',
  comparison: 'Comparison',
};

/* ───────────────────── Persistence ───────────────────── */

function loadTrial(): TrialState | null {
  try {
    const s = localStorage.getItem(TRIAL_KEY);
    return s ? JSON.parse(s) : null;
  } catch {
    return null;
  }
}
function saveTrial(state: TrialState) {
  localStorage.setItem(TRIAL_KEY, JSON.stringify(state));
}
function clearTrial() {
  localStorage.removeItem(TRIAL_KEY);
}

/* ───────────────────── Helpers ───────────────────── */

function clamp(v: number, lo: number, hi: number) {
  return Math.max(lo, Math.min(hi, v));
}

function predictScore(correct: number, total: number) {
  const pct = total > 0 ? correct / total : 0;
  return Math.round(clamp(40 + pct * 55, 40, 100));
}

function computeBreakdown(answers: AnswerRecord[]) {
  const verbal = answers.filter(a => a.section === 'verbal');
  const quant = answers.filter(a => a.section === 'quantitative');
  const vPct = verbal.length > 0 ? Math.round((verbal.filter(a => a.isCorrect).length / verbal.length) * 100) : 0;
  const qPct = quant.length > 0 ? Math.round((quant.filter(a => a.isCorrect).length / quant.length) * 100) : 0;
  return { verbal, quant, vPct, qPct };
}

function computeSkillBreakdown(answers: AnswerRecord[]) {
  const map: Record<string, { correct: number; total: number }> = {};
  for (const a of answers) {
    if (!map[a.skill_id]) map[a.skill_id] = { correct: 0, total: 0 };
    map[a.skill_id].total++;
    if (a.isCorrect) map[a.skill_id].correct++;
  }
  return Object.entries(map).map(([id, { correct, total }]) => ({
    id,
    name: SKILL_NAMES[id] || id,
    correct,
    total,
    pct: Math.round((correct / total) * 100),
  }));
}

/* ───────────────────── Component ───────────────────── */

export function TrialSession({ onRegister, onBack }: TrialSessionProps) {
  const [phase, setPhase] = useState<SessionPhase>('intro');
  const [diagIndex, setDiagIndex] = useState(0);
  const [pracIndex, setPracIndex] = useState(0);
  const [selected, setSelected] = useState<string | null>(null);
  const [diagAnswers, setDiagAnswers] = useState<AnswerRecord[]>([]);
  const [pracAnswers, setPracAnswers] = useState<AnswerRecord[]>([]);
  const [countdown, setCountdown] = useState(DIAG_TIMER);
  const [streak, setStreak] = useState(0);
  const feedbackTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  // ── Restore session ──
  useEffect(() => {
    const saved = loadTrial();
    if (saved) {
      setPhase(saved.phase);
      setDiagIndex(saved.diagnosticIndex);
      setPracIndex(saved.practiceIndex);
      setDiagAnswers(saved.diagnosticAnswers);
      setPracAnswers(saved.practiceAnswers);
    }
  }, []);

  // ── Save on change ──
  const persist = useCallback(() => {
    saveTrial({
      phase,
      diagnosticIndex: diagIndex,
      practiceIndex: pracIndex,
      diagnosticAnswers: diagAnswers,
      practiceAnswers: pracAnswers,
    });
  }, [phase, diagIndex, pracIndex, diagAnswers, pracAnswers]);

  useEffect(() => {
    if (phase !== 'intro') persist();
  }, [persist, phase]);

  // ── Timer ──
  useEffect(() => {
    if (phase !== 'diagnostic' && phase !== 'practice') return;
    const limit = phase === 'diagnostic' ? DIAG_TIMER : PRAC_TIMER;
    setCountdown(limit);
    const interval = setInterval(() => {
      setCountdown(prev => (prev <= 0 ? 0 : prev - 1));
    }, 1000);
    return () => clearInterval(interval);
  }, [phase, diagIndex, pracIndex]);

  // ── Auto-advance when timer hits 0 ──
  useEffect(() => {
    if (countdown !== 0) return;
    if (phase === 'diagnostic' && !selected) {
      handleDiagAnswer('__timeout__');
    } else if (phase === 'practice' && !selected) {
      handlePracAnswer('__timeout__');
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [countdown]);

  // ── Cleanup feedback timer ──
  useEffect(() => {
    return () => {
      if (feedbackTimerRef.current) clearTimeout(feedbackTimerRef.current);
    };
  }, []);

  // ── Current question helpers ──
  const diagQ = DIAGNOSTIC_QUESTIONS[diagIndex] || null;
  const pracQ = PRACTICE_QUESTIONS[pracIndex] || null;

  // ── Diagnostic answer (no explanation, auto-advance after 800ms) ──
  const handleDiagAnswer = (key: string) => {
    if (selected) return;
    setSelected(key);
    const q = DIAGNOSTIC_QUESTIONS[diagIndex];
    const isCorrect = key === q.correct_option;
    const rec: AnswerRecord = {
      qid: q.id, selected: key, correct: q.correct_option, isCorrect,
      skill_id: q.skill_id, section: q.section,
    };
    const newAnswers = [...diagAnswers, rec];
    setDiagAnswers(newAnswers);
    setPhase('diagnostic-feedback');

    feedbackTimerRef.current = setTimeout(() => {
      setSelected(null);
      if (diagIndex + 1 >= DIAGNOSTIC_QUESTIONS.length) {
        setPhase('diagnostic-results');
      } else {
        setDiagIndex(diagIndex + 1);
        setPhase('diagnostic');
      }
    }, 800);
  };

  // ── Practice answer (with explanation, manual advance) ──
  const handlePracAnswer = (key: string) => {
    if (selected) return;
    setSelected(key);
    const q = PRACTICE_QUESTIONS[pracIndex];
    const isCorrect = key === q.correct_option;
    const rec: AnswerRecord = {
      qid: q.id, selected: key, correct: q.correct_option, isCorrect,
      skill_id: q.skill_id, section: q.section,
    };
    const newAnswers = [...pracAnswers, rec];
    setPracAnswers(newAnswers);

    if (isCorrect) {
      setStreak(prev => prev + 1);
    } else {
      setStreak(0);
    }

    setPhase('practice-feedback');
  };

  const nextPracticeQuestion = () => {
    setSelected(null);
    if (pracIndex + 1 >= PRACTICE_QUESTIONS.length) {
      setPhase('final-report');
    } else {
      setPracIndex(pracIndex + 1);
      setPhase('practice');
    }
  };

  // ── Start helpers ──
  const startDiagnostic = () => {
    setDiagIndex(0);
    setPracIndex(0);
    setDiagAnswers([]);
    setPracAnswers([]);
    setSelected(null);
    setStreak(0);
    clearTrial();
    setPhase('diagnostic');
  };

  const startPractice = () => {
    setSelected(null);
    setStreak(0);
    setPhase('practice');
  };

  const resetAndGoHome = () => {
    clearTrial();
    onBack();
  };

  const resetAndRegister = () => {
    clearTrial();
    onRegister();
  };

  // ── Computed values ──
  const diagCorrect = diagAnswers.filter(a => a.isCorrect).length;
  const pracCorrect = pracAnswers.filter(a => a.isCorrect).length;
  const allAnswers = [...diagAnswers, ...pracAnswers];
  const allCorrect = allAnswers.filter(a => a.isCorrect).length;
  const totalXP = pracAnswers.reduce((sum, a) => sum + (a.isCorrect ? XP_CORRECT : XP_WRONG), 0);

  // ── Section Icon/Color ──
  const getSectionStyle = (section: 'verbal' | 'quantitative') => ({
    Icon: section === 'verbal' ? BookOpen : Calculator,
    bg: section === 'verbal' ? 'bg-blue-600' : 'bg-violet-600',
    lightBg: section === 'verbal' ? 'bg-blue-100' : 'bg-violet-100',
    text: section === 'verbal' ? 'text-blue-600' : 'text-violet-600',
  });

  /* ════════════════════════════════════════════════════
     RENDER PHASES
     ════════════════════════════════════════════════════ */

  // ── INTRO ──
  if (phase === 'intro') {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center p-4" dir="ltr">
        <div className="max-w-md w-full text-center">
          <div className="w-20 h-20 bg-gradient-to-br from-teal-500 to-teal-600 rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-lg">
            <Sparkles className="w-10 h-10 text-white" />
          </div>
          <h1 className="text-3xl font-black text-slate-800 mb-3">Try the Course for Free</h1>
          <p className="text-slate-500 mb-6">A complete two-phase experience — diagnostic test then training day — no registration required</p>

          <div className="bg-white dark:bg-slate-900 border border-slate-200 rounded-2xl p-5 mb-6 text-left space-y-4">
            {/* Phase 1 */}
            <div>
              <div className="flex items-center gap-2 mb-2">
                <span className="w-6 h-6 bg-teal-600 text-white rounded-full flex items-center justify-center text-xs font-bold">1</span>
                <span className="font-bold text-slate-800">Diagnostic Test</span>
              </div>
              <div className="flex items-center gap-3 ml-8">
                <div className="w-8 h-8 bg-blue-100 rounded-lg flex items-center justify-center"><BookOpen className="w-4 h-4 text-blue-600" /></div>
                <div><p className="text-sm text-slate-600">7 Verbal + 7 Quantitative questions</p><p className="text-xs text-slate-400">60 seconds per question — no explanation</p></div>
              </div>
            </div>
            {/* Phase 2 */}
            <div>
              <div className="flex items-center gap-2 mb-2">
                <span className="w-6 h-6 bg-teal-600 text-white rounded-full flex items-center justify-center text-xs font-bold">2</span>
                <span className="font-bold text-slate-800">First Day Experience</span>
              </div>
              <div className="flex items-center gap-3 ml-8">
                <div className="w-8 h-8 bg-violet-100 rounded-lg flex items-center justify-center"><Calculator className="w-4 h-4 text-violet-600" /></div>
                <div><p className="text-sm text-slate-600">20 practice questions with detailed explanation</p><p className="text-xs text-slate-400">90 seconds per question — comprehensive report at the end</p></div>
              </div>
            </div>
          </div>

          <button onClick={startDiagnostic}
            className="w-full bg-gradient-to-l from-teal-600 to-teal-500 text-white font-bold text-lg py-4 rounded-xl shadow-brand hover:shadow-lg transition-all active:scale-[0.98] mb-3">
            Start Trial
          </button>
          <button onClick={onBack} className="text-slate-400 text-sm hover:text-slate-600 transition">Back to Home</button>
        </div>
      </div>
    );
  }

  // ── DIAGNOSTIC QUESTION ──
  if ((phase === 'diagnostic' || phase === 'diagnostic-feedback') && diagQ) {
    const sec = getSectionStyle(diagQ.section);
    const isUrgent = countdown < 10;
    const lastAnswer = diagAnswers[diagAnswers.length - 1];
    const showingFeedback = phase === 'diagnostic-feedback' && lastAnswer;

    return (
      <div className="min-h-screen bg-slate-50 flex flex-col" dir="ltr">
        {/* Header */}
        <div className={`px-4 py-3 flex items-center justify-between ${sec.bg} text-white`}>
          <div className="flex items-center gap-2">
            <sec.Icon className="w-5 h-5" />
            <span className="font-bold text-sm">{diagQ.skill_name}</span>
            <span className="text-xs opacity-75">— Question {diagIndex + 1} of {DIAGNOSTIC_QUESTIONS.length}</span>
          </div>
          <div className={`flex items-center gap-1.5 font-mono font-bold ${isUrgent ? 'text-red-200 animate-pulse' : ''}`}>
            <Clock className="w-4 h-4" />
            {Math.floor(countdown / 60)}:{(countdown % 60).toString().padStart(2, '0')}
          </div>
        </div>
        {/* Progress */}
        <div className="h-1 bg-slate-200">
          <div className="h-full bg-teal-500 transition-all duration-300" style={{ width: `${((diagIndex + 1) / DIAGNOSTIC_QUESTIONS.length) * 100}%` }} />
        </div>
        {/* Trial badge */}
        <div className="px-4 py-2 bg-amber-50 border-b border-amber-200 text-xs text-amber-700 text-center font-medium">
          <Shield className="w-3.5 h-3.5 inline mr-1" /> Phase 1: Diagnostic Test — User: Trial
        </div>

        {/* Question body or brief feedback */}
        <div className="flex-1 p-3 lg:p-8 max-w-3xl mx-auto w-full flex flex-col">
          {showingFeedback ? (
            <div className="flex-1 flex items-center justify-center">
              <div className={`text-center ${lastAnswer.isCorrect ? 'text-emerald-500' : 'text-red-500'}`}>
                {lastAnswer.isCorrect
                  ? <CheckCircle className="w-20 h-20 mx-auto mb-3" />
                  : <XCircle className="w-20 h-20 mx-auto mb-3" />}
                <p className="text-2xl font-black">
                  {lastAnswer.isCorrect ? 'Correct' : 'Incorrect'}
                </p>
              </div>
            </div>
          ) : (
            <>
              {diagQ.passage_ar && (
                <div className="bg-white dark:bg-slate-900 border border-slate-200 rounded-xl p-3 lg:p-5 mb-3 text-xs lg:text-sm text-slate-600 leading-relaxed">
                  {diagQ.passage_ar}
                </div>
              )}
              <h2 className="text-base lg:text-xl font-bold text-slate-800 mb-4 lg:mb-6 leading-relaxed whitespace-pre-line math-text">{diagQ.text_ar}</h2>
              <div className="space-y-2 lg:space-y-3">
                {diagQ.options.map(opt => (
                  <button key={opt.key} onClick={() => handleDiagAnswer(opt.key)} disabled={!!selected}
                    className="w-full text-left border-2 rounded-xl p-3 lg:p-4 transition-all bg-white dark:bg-slate-900 border-slate-200 hover:border-teal-300 disabled:opacity-60">
                    <div className="flex items-start gap-3">
                      <span className="w-8 h-8 lg:w-9 lg:h-9 rounded-lg flex items-center justify-center text-xs lg:text-sm font-bold shrink-0 bg-slate-100 text-slate-600">{opt.label}</span>
                      <span className="text-sm lg:text-base text-slate-700 leading-relaxed">{opt.text_ar}</span>
                    </div>
                  </button>
                ))}
              </div>
            </>
          )}
        </div>
      </div>
    );
  }

  // ── DIAGNOSTIC RESULTS ──
  if (phase === 'diagnostic-results') {
    const predicted = predictScore(diagCorrect, DIAGNOSTIC_QUESTIONS.length);
    const { vPct, qPct } = computeBreakdown(diagAnswers);

    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center p-4" dir="ltr">
        <div className="max-w-lg w-full text-center">
          <div className="w-16 h-16 bg-gradient-to-br from-teal-500 to-teal-600 rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-lg">
            <BarChart3 className="w-8 h-8 text-white" />
          </div>
          <h1 className="text-2xl lg:text-3xl font-black text-slate-800 mb-2">Diagnostic Test Completed</h1>
          <p className="text-slate-500 mb-6">{diagCorrect} correct answers out of {DIAGNOSTIC_QUESTIONS.length}</p>

          <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 p-6 mb-6">
            <ScoreRing score={predicted} size={140} label="Predicted Score" />
          </div>

          {/* Breakdown */}
          <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 p-5 mb-6 text-left space-y-4">
            <div>
              <div className="flex justify-between items-center mb-1">
                <span className="text-sm font-bold text-slate-700 flex items-center gap-1"><BookOpen className="w-4 h-4 text-blue-500" /> Verbal</span>
                <span className="text-xs font-bold text-blue-600">{vPct}%</span>
              </div>
              <div className="h-3 bg-slate-100 rounded-full overflow-hidden">
                <div className="h-full bg-blue-500 rounded-full transition-all duration-500" style={{ width: `${vPct}%` }} />
              </div>
            </div>
            <div>
              <div className="flex justify-between items-center mb-1">
                <span className="text-sm font-bold text-slate-700 flex items-center gap-1"><Calculator className="w-4 h-4 text-violet-500" /> Quantitative</span>
                <span className="text-xs font-bold text-violet-600">{qPct}%</span>
              </div>
              <div className="h-3 bg-slate-100 rounded-full overflow-hidden">
                <div className="h-full bg-violet-500 rounded-full transition-all duration-500" style={{ width: `${qPct}%` }} />
              </div>
            </div>
          </div>

          <button onClick={startPractice}
            className="w-full bg-gradient-to-l from-teal-600 to-teal-500 text-white font-bold text-lg py-4 rounded-xl shadow-brand hover:shadow-lg transition-all active:scale-[0.98] mb-3">
            Start First Day Experience
          </button>
          <button onClick={resetAndGoHome} className="text-slate-400 text-sm hover:text-slate-600 transition">Back to Home</button>
        </div>
      </div>
    );
  }

  // ── PRACTICE QUESTION ──
  if (phase === 'practice' && pracQ) {
    const sec = getSectionStyle(pracQ.section);
    const isUrgent = countdown < 15;

    return (
      <div className="min-h-screen bg-slate-50 flex flex-col" dir="ltr">
        {/* Header with live stats */}
        <div className={`px-4 py-3 flex items-center justify-between ${sec.bg} text-white`}>
          <div className="flex items-center gap-2">
            <sec.Icon className="w-5 h-5" />
            <span className="font-bold text-sm">{pracQ.skill_name}</span>
            <span className="text-xs opacity-75">— Question {pracIndex + 1} of {PRACTICE_QUESTIONS.length}</span>
          </div>
          <div className={`flex items-center gap-1.5 font-mono font-bold ${isUrgent ? 'text-red-200 animate-pulse' : ''}`}>
            <Clock className="w-4 h-4" />
            {Math.floor(countdown / 60)}:{(countdown % 60).toString().padStart(2, '0')}
          </div>
        </div>
        {/* Live stats bar */}
        <div className="px-4 py-2 bg-white dark:bg-slate-900 border-b border-slate-200 flex items-center justify-between text-xs font-medium text-slate-600">
          <div className="flex items-center gap-4">
            <span className="flex items-center gap-1"><CheckCircle className="w-3.5 h-3.5 text-emerald-500" /> {pracCorrect}/{pracAnswers.length}</span>
            <span className="flex items-center gap-1"><Sparkles className="w-3.5 h-3.5 text-amber-500" /> {totalXP} XP</span>
            {streak >= 2 && <span className="text-orange-500 font-bold">Streak {streak}</span>}
          </div>
          <span className="text-slate-400">User: Trial</span>
        </div>
        {/* Progress */}
        <div className="h-1 bg-slate-200">
          <div className="h-full bg-teal-500 transition-all duration-300" style={{ width: `${((pracIndex + 1) / PRACTICE_QUESTIONS.length) * 100}%` }} />
        </div>
        {/* Trial badge */}
        <div className="px-4 py-2 bg-amber-50 border-b border-amber-200 text-xs text-amber-700 text-center font-medium">
          <Shield className="w-3.5 h-3.5 inline mr-1" /> Phase 2: First Day Experience
        </div>

        {/* Question */}
        <div className="flex-1 p-3 lg:p-8 max-w-3xl mx-auto w-full">
          {pracQ.passage_ar && (
            <div className="bg-white dark:bg-slate-900 border border-slate-200 rounded-xl p-3 lg:p-5 mb-3 text-xs lg:text-sm text-slate-600 leading-relaxed">
              {pracQ.passage_ar}
            </div>
          )}
          <h2 className="text-base lg:text-xl font-bold text-slate-800 mb-4 lg:mb-6 leading-relaxed whitespace-pre-line math-text">{pracQ.text_ar}</h2>
          <div className="space-y-2 lg:space-y-3">
            {pracQ.options.map(opt => (
              <button key={opt.key} onClick={() => handlePracAnswer(opt.key)} disabled={!!selected}
                className="w-full text-left border-2 rounded-xl p-3 lg:p-4 transition-all bg-white dark:bg-slate-900 border-slate-200 hover:border-teal-300 disabled:opacity-60">
                <div className="flex items-start gap-3">
                  <span className="w-8 h-8 lg:w-9 lg:h-9 rounded-lg flex items-center justify-center text-xs lg:text-sm font-bold shrink-0 bg-slate-100 text-slate-600">{opt.label}</span>
                  <span className="text-sm lg:text-base text-slate-700 leading-relaxed">{opt.text_ar}</span>
                </div>
              </button>
            ))}
          </div>
        </div>
      </div>
    );
  }

  // ── PRACTICE FEEDBACK ──
  if (phase === 'practice-feedback' && pracQ) {
    const lastAnswer = pracAnswers[pracAnswers.length - 1];
    const isCorrect = lastAnswer?.isCorrect;
    const sec = getSectionStyle(pracQ.section);

    return (
      <div className="min-h-screen bg-slate-50 flex flex-col" dir="ltr">
        <div className={`px-4 py-3 ${sec.bg} text-white text-center font-bold text-sm`}>
          {pracQ.skill_name} — Question {pracIndex + 1} of {PRACTICE_QUESTIONS.length}
        </div>
        {/* Live stats bar */}
        <div className="px-4 py-2 bg-white dark:bg-slate-900 border-b border-slate-200 flex items-center justify-between text-xs font-medium text-slate-600">
          <div className="flex items-center gap-4">
            <span className="flex items-center gap-1"><CheckCircle className="w-3.5 h-3.5 text-emerald-500" /> {pracCorrect}/{pracAnswers.length}</span>
            <span className="flex items-center gap-1"><Sparkles className="w-3.5 h-3.5 text-amber-500" /> {totalXP} XP</span>
            {streak >= 2 && <span className="text-orange-500 font-bold">Streak {streak}</span>}
          </div>
          <span className="text-slate-400">User: Trial</span>
        </div>

        <div className="flex-1 p-4 lg:p-8 max-w-3xl mx-auto w-full flex flex-col items-center justify-center">
          <div className={`text-center mb-4 ${isCorrect ? 'text-emerald-500' : 'text-red-500'}`}>
            {isCorrect
              ? <CheckCircle className="w-16 h-16 mx-auto mb-2" />
              : <XCircle className="w-16 h-16 mx-auto mb-2" />}
            <h2 className="text-2xl font-black">
              {isCorrect ? 'Correct Answer!' : 'Incorrect Answer'}
            </h2>
            <p className="text-sm mt-1 text-slate-500">
              {isCorrect ? `+${XP_CORRECT} XP` : `+${XP_WRONG} XP`}
            </p>
          </div>

          <div className={`w-full rounded-xl p-4 lg:p-6 ${isCorrect ? 'bg-emerald-50 border border-emerald-200' : 'bg-amber-50 border border-amber-200'}`}>
            <p className="text-sm text-slate-700 leading-relaxed whitespace-pre-line">{pracQ.explanation_ar}</p>
          </div>

          <button onClick={nextPracticeQuestion}
            className="w-full mt-6 bg-gradient-to-l from-teal-600 to-teal-500 text-white font-bold py-4 rounded-xl shadow-brand transition-all active:scale-[0.98]">
            {pracIndex + 1 < PRACTICE_QUESTIONS.length ? 'Next' : 'View Final Report'}
          </button>
        </div>
      </div>
    );
  }

  // ── FINAL REPORT ──
  if (phase === 'final-report') {
    const overallPct = allAnswers.length > 0 ? Math.round((allCorrect / allAnswers.length) * 100) : 0;
    const predicted = predictScore(allCorrect, allAnswers.length);
    const { vPct, qPct } = computeBreakdown(allAnswers);
    const skills = computeSkillBreakdown(allAnswers);

    return (
      <div className="min-h-screen bg-slate-50 p-4" dir="ltr">
        <div className="max-w-2xl mx-auto">
          {/* Title */}
          <div className="text-center mb-6 pt-6">
            <h1 className="text-2xl lg:text-3xl font-black text-slate-800 mb-1">Final Report</h1>
            <p className="text-slate-500 text-sm">14 diagnostic + 20 practice questions — User: Trial</p>
          </div>

          {/* Score Ring */}
          <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 p-6 mb-4 text-center">
            <ScoreRing score={overallPct} size={150} label={`${allCorrect} of ${allAnswers.length}`} />
            <p className="text-sm text-slate-500 mt-3">Predicted GAT Score: <span className="font-black text-teal-600 text-lg">{predicted}</span></p>
          </div>

          {/* Section Breakdown */}
          <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 p-5 mb-4 space-y-4">
            <h3 className="font-bold text-slate-800 flex items-center gap-2"><BarChart3 className="w-5 h-5 text-teal-600" /> Section Analysis</h3>
            <div>
              <div className="flex justify-between items-center mb-1">
                <span className="text-xs font-bold text-blue-600">{vPct}%</span>
                <span className="text-sm font-bold text-slate-700 flex items-center gap-1"><BookOpen className="w-4 h-4 text-blue-500" /> Verbal</span>
              </div>
              <div className="h-3 bg-slate-100 rounded-full overflow-hidden">
                <div className="h-full bg-blue-500 rounded-full transition-all duration-500" style={{ width: `${vPct}%` }} />
              </div>
            </div>
            <div>
              <div className="flex justify-between items-center mb-1">
                <span className="text-xs font-bold text-violet-600">{qPct}%</span>
                <span className="text-sm font-bold text-slate-700 flex items-center gap-1"><Calculator className="w-4 h-4 text-violet-500" /> Quantitative</span>
              </div>
              <div className="h-3 bg-slate-100 rounded-full overflow-hidden">
                <div className="h-full bg-violet-500 rounded-full transition-all duration-500" style={{ width: `${qPct}%` }} />
              </div>
            </div>
          </div>

          {/* Per-Skill Table */}
          <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 p-5 mb-4">
            <h3 className="font-bold text-slate-800 mb-3">Skill Details</h3>
            <div className="space-y-2">
              {skills.map(s => (
                <div key={s.id} className="flex items-center gap-3 text-sm">
                  <span className="flex-1 text-slate-700 font-medium text-left">{s.name}</span>
                  <span className="text-slate-500 text-xs">{s.correct}/{s.total}</span>
                  <div className="w-24 h-2 bg-slate-100 rounded-full overflow-hidden">
                    <div
                      className={`h-full rounded-full transition-all duration-500 ${s.pct >= 70 ? 'bg-emerald-500' : s.pct >= 40 ? 'bg-amber-500' : 'bg-red-400'}`}
                      style={{ width: `${s.pct}%` }}
                    />
                  </div>
                  <span className={`text-xs font-bold w-10 text-left ${s.pct >= 70 ? 'text-emerald-600' : s.pct >= 40 ? 'text-amber-600' : 'text-red-500'}`}>{s.pct}%</span>
                </div>
              ))}
            </div>
          </div>

          {/* XP */}
          <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 p-5 mb-4 flex items-center justify-between">
            <span className="font-bold text-slate-700 flex items-center gap-2"><Sparkles className="w-5 h-5 text-amber-500" /> Experience Points Earned</span>
            <span className="text-2xl font-black text-amber-600">{totalXP} XP</span>
          </div>

          {/* CTA */}
          <div className="bg-gradient-to-br from-teal-600 to-teal-700 rounded-2xl p-6 text-white mb-4">
            <Sparkles className="w-8 h-8 mx-auto mb-3 text-teal-200" />
            <h3 className="font-black text-xl mb-2 text-center">Register now and get 30 days of full training</h3>

            <div className="grid grid-cols-2 gap-3 mt-4 mb-5 text-sm">
              <div className="bg-white/10 rounded-xl p-3 text-center">
                <p className="text-teal-200 text-xs mb-1">Trial</p>
                <p className="font-bold">34 Questions</p>
              </div>
              <div className="bg-white/10 rounded-xl p-3 text-center">
                <p className="text-teal-200 text-xs mb-1">Full Course</p>
                <p className="font-bold">+1500 Questions</p>
              </div>
              <div className="bg-white/10 rounded-xl p-3 text-center">
                <p className="text-teal-200 text-xs mb-1">Trial</p>
                <p className="font-bold">One Report</p>
              </div>
              <div className="bg-white/10 rounded-xl p-3 text-center">
                <p className="text-teal-200 text-xs mb-1">Full Course</p>
                <p className="font-bold">Daily Analysis</p>
              </div>
              <div className="bg-white/10 rounded-xl p-3 text-center col-span-2">
                <p className="text-teal-200 text-xs mb-1">Full Subscription Includes</p>
                <p className="font-bold text-xs">Diagnostic Test + 30-Day Plan + Adaptive Training + Badges + Final Mock Exam</p>
              </div>
            </div>

            <button onClick={resetAndRegister}
              className="w-full bg-white dark:bg-slate-900 text-teal-700 font-bold py-3 rounded-xl hover:bg-teal-50 transition text-lg">
              Register Now — 199 <img src="/sar-symbol.svg" alt="SAR" className="inline-block h-[0.75em] w-auto ml-0.5" />
            </button>
          </div>

          <div className="text-center pb-8">
            <button onClick={resetAndGoHome} className="text-slate-400 text-sm hover:text-slate-600 transition">
              Back to Home
            </button>
          </div>
        </div>
      </div>
    );
  }

  return null;
}
