---
name: ian-xiaohei-illustrations
description: Generate Ian-style in-article illustrations — use when the user asks for absurd, Xiaohei, hand-drawn, in-article illustrations, article illustrations, illustration suggestions, a shot list, or remove title / edit image tasks for articles, posts, blogs, Notion docs, workflow docs, methodologies, processes, structures, states, metaphors, or opinions; defaults to the Xiaohei IP, pure white hand-drawn style, a few red/orange/blue annotations, and a clean, uncluttered yet wildly imaginative visual style.
---

# Ian Xiaohei Absurd In-Article Illustrations

## Core Positioning

Design and generate 16:9 landscape in-article illustrations for articles. The goal is not commercial illustration, PPT infographics, or cute cartoons — it is turning an article's key judgments, workflows, structures, states, or metaphors into one hand-drawn explanatory image that is clean, absurd, creative, and readable but not an instruction manual.

The default visual IP is Xiaohei (小黑, "Little Black"): solid black, white dot eyes, thin legs, blank expression, earnestly doing one absurd but coherent thing. Xiaohei must take part in the frame's core action — never just standing off to the side as decoration.

## Read These References First

Load what the task needs — don't stuff the whole context at once:

- `references/style-dna.md`: style DNA, color, text, taboos.
- `references/xiaohei-ip.md`: the Xiaohei IP's look, personality, action library, and taboos.
- `references/composition-patterns.md`: structure types, original metaphor method, and anti-replication rules.
- `references/prompt-template.md`: the single-image generation prompt template.
- `references/qa-checklist.md`: post-generation checks and iteration rules.
- `assets/examples/`: low-frequency visual calibration only — never part of the default generation path. Do not copy these examples' compositions, props, or annotations.

## Workflow

### 1. Digest the Article

First read what the user provides — article text, links, Notion pages, Markdown files, or screenshot content. Distill:

- What the core argument is
- Which paragraphs carry the cognitive turning points
- Which content is best explained with an image
- Which parts work as text only and need no image

Don't spread illustrations evenly. Prioritize cognitive anchors, for example: core judgment; two breakpoints; input-output loop; branching; before-after contrast; one fish, many uses; handoff path; common pitfalls; character state changes.

### 2. Illustration Strategy First

If the user only says "analyze how to illustrate / think through where illustrations are needed", give a shot list first. For each image, spell out:

- Which paragraph it goes after
- The image's subject
- The core meaning
- The structure type
- What Xiaohei is doing in it
- Suggested elements
- Suggested labels

Default is 4-8 images. Very short articles get 1-3; even long ones should rarely exceed 9. Just enough is plenty — don't turn the article into a picture book.

### 3. Generate One at a Time

If the user explicitly says "generate / output / make the images / generate them for me", don't stop to wait for confirmation; use the built-in `image_gen` to generate each image separately. Never combine multiple images into one.

Each image tells exactly one core structure. The prompt must include:

- 16:9 landscape in-article illustration
- Pure white background
- Black hand-drawn line art
- A few red/orange/blue handwritten annotations (in the article's language)
- Generous white space
- Xiaohei as the core action subject
- No PPT, no commercial illustration, no childish cuteness, no complex architecture, no top-left category titles

Never replicate past examples. Examples supply only the style density and how Xiaohei participates — existing compositions like "conveyor-belt breakpoint / Xiaohei pulling a line / material fish / stamping toolbox / common-pitfalls path" are off-limits unless the user explicitly asks to replicate a specific image. Reinvent a strange but coherent metaphor from the current article every single time.

### 4. Check and Iterate

After generating, check against `references/qa-checklist.md`. If any of these problems appear, prioritize regenerating or spot-editing:

- Xiaohei is mere decoration
- The frame is too crowded
- Looks too much like a flowchart/PPT
- Too much in-image text or serious typos
- Titles like "common pitfalls / flowchart / system architecture diagram" appear in the top-left corner
- The style is too cute, childish, or stiff
- The background is not clean white

### 5. Save and Deliver

If the user is working inside a workspace, copy the final images to:

```text
assets/<article-slug>-illustrations/
```

Name them in order:

```text
01-topic-name.png
02-topic-name.png
```

Keep the original generated files. Never overwrite existing assets unless the user explicitly asks for a replacement.

## Output Discipline

Pre-generation strategy output should be short and precise. Post-generation delivery must include:

- How many images were generated
- What each image is for
- The save path
- Which images are the safest bets and which are optional

No long-winded style theory; let the images speak for themselves.
