---
name: ian-xiaohei-illustrations-en
description: Use when the user wants English-language Ian Xiaohei-style article illustrations, hand-drawn conceptual diagrams, absurd white-background editorial images, shot lists, or image edits for blog posts, notes, workflows, methods, processes, structures, states, metaphors, or opinions.
---

# Ian Xiaohei Illustrations, English Variant

## Purpose

Design and generate 16:9 editorial illustrations for English articles, posts, notes, workflow docs, and methodology writing.

This is not a general illustration prompt, brand key visual, polished vector graphic, or PPT infographic. The goal is to turn one key judgment, process, structure, state, or metaphor from the source text into a clean, strange, memorable hand-drawn explanation image.

The recurring character is Xiaohei, Ian's small solid-black visual character with white dot eyes, tiny thin legs, a blank serious expression, and a slightly uneven hand-drawn body. Xiaohei must participate in the central conceptual action. If Xiaohei could be removed and the image still works, the concept is not strong enough.

This variant adapts Ian Xiaohei Illustrations for English-language article labels and English user workflows. Keep attribution to Ian and the original `Ian Xiaohei Illustrations` project in derived docs.

## Read As Needed

- `references/prompt-template.md`: image prompt template for one illustration.
- `references/qa-checklist.md`: post-generation quality checks and iteration rules.
- Original repository examples: visual calibration only. Do not copy the objects, layout, or labels from examples.

## Workflow

### 1. Understand The Source

Read the article, Markdown, notes, screenshot, or topic. Extract:

- the central claim
- cognitive turns or surprises
- process, state, or structure worth visualizing
- sections that should stay text-only

Do not illustrate evenly. Pick cognitive anchors: a core judgment, input-output loop, bottleneck, split path, before/after shift, handoff, common trap, missing bridge, role-state change, or useful metaphor.

### 2. Plan Before Generating

If the user asks for analysis, planning, or a shot list, do not generate images yet. Return a compact shot list.

For each shot include:

- placement in the article
- theme
- core idea
- structure type
- what Xiaohei is doing
- suggested elements
- suggested English labels

Default to 4-8 shots. Use 1-3 for short pieces. Avoid more than 9 unless the user explicitly wants a larger series.

### 3. Generate One Image At A Time

If the user asks to generate, make, output, or create images, call `image_gen` once per image. Do not combine multiple illustrations into one canvas.

Each prompt must include:

- 16:9 horizontal English article illustration
- pure white background
- minimalist black hand-drawn line art
- sparse red, orange, and blue handwritten English labels
- lots of empty space
- Xiaohei as the central action subject
- no PPT look, no commercial vector style, no cute mascot poster, no dense architecture diagram, no top-left diagram title

Each image should explain one structure only. Re-invent a fresh physical metaphor for the current text. Use examples only for style density and Xiaohei participation, never for composition reuse.

### 4. QA And Iterate

After generation, check `references/qa-checklist.md`. Regenerate or edit when:

- Xiaohei is only decorative
- the canvas is too full
- it looks like a slide, flowchart, or formal architecture diagram
- text is too long or misspelled
- a top-left title appears
- the style is cute, childish, glossy, or too polished
- the background is not clean white

### 5. Save

When working in a workspace, save final PNGs under:

```text
assets/<article-slug>-illustrations/
```

Use ordered names:

```text
01-topic-name.png
02-topic-name.png
```

Report only what matters: how many images, each image's intended use, saved paths, and any images that may need another pass.
