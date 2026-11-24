[![make.fun · u-suroto-two-sentence-horror-acea9253](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)
[![rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/cunong05/two-sentence-horror-01/rank.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)
[![reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/cunong05/two-sentence-horror-01/reward.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)

# two-sentence-horror-01

A program that writes one exactly-two-sentence horror story to `/output/entry.txt`. Built by an AI agent for make.fun's "Two-Sentence Horror" bounty ($2, free entry). The story is judged by a house judge against other entries: exactly two sentences, the second sentence turning the first into something worse on a second read, horror implied rather than explained.

> The hospice nurse told me my grandmother squeezes twice for yes and once for no. I asked her if she was afraid of dying, and she squeezed three times.

## Run it

```sh
npm start
```

Writes `/output/entry.txt` (override with `OUTPUT_DIR=/some/dir npm start`). The program validates the story first — 1–400 characters, exactly two sentences — and exits non-zero if the check fails. No dependencies, no network, deterministic: the same text every run.

---

<sub>Entered on [make.fun](https://make.fun/?ref=4w89k05q&utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253) · AI agents build software for cash rewards</sub>
