// two-sentence-horror-01
// Writes one exactly-two-sentence horror story to <OUTPUT_DIR>/entry.txt
// (OUTPUT_DIR defaults to /output, the path the make.fun grader reads).
// No dependencies, no network, deterministic: the same text every run.

import { mkdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const STORY =
  "The hospice nurse told me my grandmother squeezes twice for yes and once for no. I asked her if she was afraid of dying, and she squeezed three times.";

// Gate: the entry must be 1-400 characters, not only whitespace,
// and exactly two sentences.
const sentenceEndings = (STORY.match(/\./g) || []).length;
if (STORY.length < 1 || STORY.length > 400) {
  console.error(`error: story is ${STORY.length} characters, must be 1-400`);
  process.exit(1);
}
if (STORY.trim().length === 0) {
  console.error("error: story is only whitespace");
  process.exit(1);
}
if (sentenceEndings !== 2) {
  console.error(`error: story has ${sentenceEndings} sentence-ending periods, must be exactly 2`);
  process.exit(1);
}

const outDir = process.env.OUTPUT_DIR || "/output";
mkdirSync(outDir, { recursive: true });
const outPath = join(outDir, "entry.txt");
writeFileSync(outPath, STORY, "utf8"); // no trailing newline
console.log(`wrote ${STORY.length} characters to ${outPath}`);
