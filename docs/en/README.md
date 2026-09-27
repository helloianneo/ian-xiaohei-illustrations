> **English translation** of the project README. 中文原版 → [README.md](../../README.md)

# Ian Xiaohei Illustrations

> Turn the judgments, flows, states, and metaphors in your articles into white-background, hand-drawn, absurd-but-clean in-article illustrations.
>
> 16:9 landscape | Xiaohei IP | pure-white hand-drawn | sparse red/orange/blue annotations | Codex Skill

---

## What this repo is

Ian Xiaohei Illustrations is a Codex Skill that guides an AI Agent to generate in-article illustrations for articles, posts, blogs, Notion docs, and methodology content (originally built for Chinese content).

It is not a generic illustration prompt, and it is not a PPT infographic template. Its core goal: first understand the cognitive anchors in the article, then turn one judgment, flow, structure, state, or metaphor into a memorable 16:9 hand-drawn explainer image.

The default visual IP is Xiaohei (小黑, "Little Black"): a small character with a solid black body, white dot eyes, thin legs, and a blank expression. Xiaohei is not a mascot, not a sticker, and not a decoration standing in the corner — Xiaohei is an absurd worker earnestly keeping the system running.

In one sentence: **don't let the AI just "add a picture" — make it draw one key cognitive move from the article.**

---

## Who it's for

Especially good for:

- People who write articles and need in-article illustrations and article illustrations
- People making knowledge content, methodology content, or AI workflow content
- People who want to turn abstract judgments into concrete metaphors
- People who want an illustration style that's lighter, weirder, and more personally recognizable than PPT infographics
- People producing content with Codex who want one visual language they can reuse reliably

Not for:

- People who want commercial illustration, brand KVs, or polished flat illustration
- People who want traditional PPT infographics, complex architecture diagrams, or flowcharts
- People who want kids' cartoons, cute IPs, or sticker-pack styles
- People who want to cram long body text, extended explanations, or full course pages into one image
- People who need strictly editable vector source files

---

## What it produces

Default output:

- 16:9 landscape in-article illustrations
- A shot list of 4-8 images per article
- For each image: theme, core meaning, structure type, Xiaohei's action, and suggested labels
- Final PNG images, saved to `assets/<article-slug>-illustrations/` in the workspace

Not output by default:

- PPTX / PDF / Keynote
- SVG / HTML / Canvas editable graphics
- Commercial posters or cover KVs
- Text-heavy infographics

---

## Visual style

By default this skill uses Ian's "absurd Xiaohei in-article illustration" style:

- Pure white background — no paper texture, beige, shadows, or gradients
- Black hand-drawn line art, thin lines, slightly wobbly
- Plenty of white space — the subject fills only about 40%-60% of the frame
- Sparse red, orange, and blue handwritten annotations (in the article's language)
- One image expresses one core action, structure, state, or metaphor
- Xiaohei must take part in the core action, never just decorate
- Absurd, creative, clean — but never childish, never acting cute

---

## Examples

### Two Breakpoints

![Two Breakpoints](../../examples/images/01-two-breakpoints.png)

### Sort by Purpose

![Sort by Purpose](../../examples/images/02-sort-by-purpose.png)

### One Fish, Many Uses

![One Fish, Many Uses](../../examples/images/03-one-fish-many-uses.png)

### Handoff Path

![Handoff Path](../../examples/images/04-handoff-path.png)

### Information Well

![Information Well](../../examples/images/05-information-well.png)

### Idea Press

![Idea Press](../../examples/images/06-idea-press.png)

### Content Fermentation

![Content Fermentation](../../examples/images/07-content-fermentation.png)

### Trust Bridge

![Trust Bridge](../../examples/images/08-trust-bridge.png)

These images are style-calibration samples, not composition templates. When you use the skill, reinvent the metaphor from the current article — don't copy the objects and compositions of old examples.

---

## Install

Clone the repo:

```bash
git clone https://github.com/helloianneo/ian-xiaohei-illustrations.git
cd ian-xiaohei-illustrations
```

Copy the **English skill** into your Codex skills directory, then add the style-calibration images from the original skill:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./docs/en/skill/ian-xiaohei-illustrations "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R ./ian-xiaohei-illustrations/assets "${CODEX_HOME:-$HOME/.codex}/skills/ian-xiaohei-illustrations/"
```

(This installs the English-language runtime — instructions, references, and prompts in English, with in-image labels following the article's language. To install the original Chinese skill instead, copy `./ian-xiaohei-illustrations`.)

After installing, use it in Codex:

```text
Use $ian-xiaohei-illustrations to design and generate 5 absurd Xiaohei in-article illustrations for this article.
```

---

## How to use

### Plan illustrations only

```text
Use $ian-xiaohei-illustrations but don't generate images yet.
Analyze the article below for spots worth illustrating, and output a shot list of about 5 images.
For each image, spell out: which paragraph it goes after, theme, core meaning, structure type, what Xiaohei is doing, and suggested labels.

<paste article>
```

### Generate in-article illustrations directly

```text
Use $ian-xiaohei-illustrations to generate 4 absurd Xiaohei in-article illustrations for the article below.
Requirements: 16:9 landscape, pure white background, black hand-drawn line art, sparse red/orange/blue handwritten annotations.

<paste article>
```

### Generate one image for a single concept

```text
Use $ian-xiaohei-illustrations to generate one in-article illustration for "trust isn't shouted into existence — it's laid down one piece of evidence at a time".
Make it absurd but clean, and Xiaohei must carry the core action.
```

### Remove a title or wrong text from an image

```text
Use $ian-xiaohei-illustrations to edit this image: remove the "Flowchart" title in the top-left corner and keep everything else unchanged.
```

More examples in [examples/prompts.md](examples/prompts.md).

---

## Workflow

The skill's flow:

1. Read the article, Markdown, Notion content, screenshots, or a topic the user gives
2. Distill core ideas, cognitive turning points, process structures, and passages that fit visualization
3. Output a shot list first: one cognitive anchor per image
4. Pick a structure type for each image: Workflow, System close-up, Before-after contrast, Character states, Concept metaphor, Method layers, Map route, or Mini comic panels
5. Reinvent a low-tech, absurd but coherent physical metaphor
6. Give Xiaohei the core action
7. Generate each image with its own image-model call
8. Check against the QA checklist: white background, white space, Xiaohei's action, annotations, no PPT feel, no old-example clones
9. Save the final PNGs and report each image's purpose and path

---

## Directory structure

```text
.
├── README.md
├── LICENSE
├── NOTICE.md
├── assets/
│   └── ian-wechat-qr.jpg
├── docs/
│   └── en/
│       ├── README.md
│       ├── examples/prompts.md
│       └── skill/ian-xiaohei-illustrations/   ← installable English skill
├── examples/
│   ├── images/
│   │   ├── 01-two-breakpoints.png
│   │   ├── 02-sort-by-purpose.png
│   │   └── ...
│   └── prompts.md
└── ian-xiaohei-illustrations/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── assets/
    │   └── examples/
    └── references/
        ├── style-dna.md
        ├── xiaohei-ip.md
        ├── composition-patterns.md
        ├── prompt-template.md
        └── qa-checklist.md
```

What you actually install into Codex is one skill directory — the English edition:

```text
docs/en/skill/ian-xiaohei-illustrations/
```

or the original Chinese edition:

```text
ian-xiaohei-illustrations/
```

The root-level README, LICENSE, NOTICE, and examples are GitHub-facing docs.

---

## Notes

- The shorter the in-image text, the more stable the result.
- One core structure per image — don't turn the article into an instruction manual.
- Xiaohei must carry the core action; if the image still fully works with Xiaohei removed, Xiaohei is too decorative.
- Example images are only for calibrating line density, white space, color restraint, and how Xiaohei participates — don't clone their compositions.
- AI image models can produce typos, hallucinated labels, style drift, or stray titles — check every generation.
- If typos are severe, cut down the labels first and regenerate.

---

## Related projects

- [Ian Handdrawn PPT](https://github.com/helloianneo/ian-handdrawn-ppt) — a Skill for generating hand-drawn Chinese tech PPT-style page images
- [Awesome Claude Code Skills](https://github.com/helloianneo/awesome-claude-code-skills) — a curated collection of Claude Code Skills / Agents / Plugins
- [Obsidian + Claude AI Second Brain](https://github.com/helloianneo/obsidian-ai-second-brain) — a guide to building a personal knowledge base with Obsidian + Claude AI

---

## About the author

**Ian (伊恩)** — Product Designer / One-Person Company Practitioner / AI Builder

Building a one-person company with a team of AIs.

- GitHub: [helloianneo](https://github.com/helloianneo)
- X/Twitter: [@ianneo_ai](https://x.com/ianneo_ai)
- Website: [www.ianneo.xyz](https://www.ianneo.xyz)
- WeChat: `ianneoxyz`
- Email: hello.neoc@gmail.com

---

## Keep exploring

This Xiaohei illustration Skill is just one small tool in the personal production system I'm building with AI.

If you're also using AI for content, knowledge bases, workflows, or productization, keep reading on my website: [www.ianneo.xyz](https://www.ianneo.xyz).

Just want to watch first? Follow me on [X/Twitter](https://x.com/ianneo_ai).

Curious about Indie Builders Club? Add me on WeChat: `ianneoxyz` and mention "OPC".

<p>
  <img src="../../assets/ian-wechat-qr.jpg" alt="Ian WeChat QR code" width="120">
</p>

Can't scan? Search WeChat for `ianneoxyz`.

---

## License

MIT License. See [LICENSE](../../LICENSE).
