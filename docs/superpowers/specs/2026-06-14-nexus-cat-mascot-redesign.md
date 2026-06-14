# Nexus Cat Mascot Redesign

Date: 2026-06-14

## Summary

Redesign this Codex Skill package from the Xiaohei article-illustration system into a Nexus Cat kawaii mascot prompt pack.

The new default character is a consistent mascot named "Nexus Cat": a chubby gray-and-white cat with big round eyes, blush cheeks, simple black outlines, minimal shading, and a hoodie marked with `</>`. Nexus Cat should act as a friendly guide, assistant, and developer companion. The same character design must repeat across every generated image and panel.

## Decisions Confirmed

- Direction: full kawaii mascot prompt pack, not a sparse article-illustration system.
- Rename scope: complete rename, including Skill name, directory, README, examples, and install instructions.
- Old example images: remove from README display for now so the new package is not visually anchored to Xiaohei.
- Implementation approach: mascot package rewrite, not a dual-mode compatibility layer.

## New Project Positioning

The package should become a reusable Nexus Cat generation Skill for article illustrations, stickers, documentation companions, tutorial panels, and product-support visuals.

The focus shifts from "turning cognitive structures into strange whiteboard metaphors" to "keeping one cute assistant mascot visually consistent across many scenes." It may still support article and document illustrations, but the center of gravity is the mascot itself: greeting, explaining, pointing, debugging, carrying code, reviewing dashboards, holding signs, and guiding the reader through steps.

## File Structure And Naming

Rename the Skill directory:

```text
ian-xiaohei-illustrations/ -> nexus-cat-mascot/
```

Rename the Skill:

```text
ian-xiaohei-illustrations -> nexus-cat-mascot
```

Rewrite or replace the reference files:

- `references/nexus-cat-ip.md`: fixed character DNA, appearance, personality, action library, and forbidden drift.
- `references/style-dna.md`: kawaii mascot visual style, clean white or transparent background, simple outlines, minimal shading, developer-assistant feel.
- `references/composition-patterns.md`: scene and panel patterns such as greeting, guiding, debugging, workflow helper, reaction, tutorial panel, and product companion.
- `references/prompt-template.md`: single-image prompt template that repeats the fixed Nexus Cat identity.
- `references/qa-checklist.md`: checks for character consistency, hoodie `</>`, gray-and-white fur, chubby body, friendly assistant role, and simple clean rendering.

Keep old image assets on disk unless implementation finds they are explicitly referenced by user-facing docs. Do not display them in the rewritten README.

## README And Examples

Rewrite `README.md` to describe:

- What Nexus Cat Mascot is.
- What it generates.
- When to use it.
- When not to use it.
- The fixed mascot design.
- Installation path using `nexus-cat-mascot`.
- Example prompts for planning and direct image generation.

Update `examples/prompts.md` so every example uses Nexus Cat. Remove Xiaohei wording, old "not cute" constraints, and old "absurd worker" positioning.

## Workflow Behavior

The new Skill workflow:

1. Read the user's theme, article, product context, scene, or desired mascot action.
2. If the user asks for planning only, output a Nexus Cat shot list. Each shot should include purpose, scene, Nexus Cat action, expression, props, background complexity, and optional text labels.
3. If the user explicitly asks to generate images, call the image model for each image separately. Do not combine multiple requested images into one sheet unless the user explicitly asks for a multi-panel image.
4. In every prompt, repeat the fixed Nexus Cat identity: chubby gray-and-white cat, big round eyes, blush cheeks, simple black outlines, minimal shading, hoodie with `</>`.
5. For multi-image or multi-panel work, require the same character design repeated across all panels.
6. Treat text labels as optional. For Chinese article use cases, allow short Chinese labels, but the mascot scene is the main output.
7. After generation, check for character consistency, friendliness, hoodie symbol, simple rendering, and lack of unwanted background complexity.

## Prompting Rules

The prompt template must explicitly prevent character drift:

- Do not change the character species, fur pattern, hoodie, body shape, eye style, or overall silhouette between panels.
- Do not make Nexus Cat realistic, overly detailed, scary, gritty, or heavily shaded.
- Do not replace the hoodie symbol with random text.
- Do not turn the image into a dense infographic, formal flowchart, or generic sticker sheet unless requested.

Allowed visual traits:

- Kawaii, friendly, rounded, approachable.
- Clean white or transparent background.
- Minimal props that support the scene.
- Developer and assistant motifs such as code snippets, terminal windows, bug icons, dashboards, arrows, check marks, and small signs.

## QA Criteria

A generated image passes if:

- Nexus Cat is clearly the same character as the fixed design.
- The body is chubby and round.
- Fur is gray-and-white.
- Eyes are large and round.
- Cheeks have blush.
- Hoodie includes `</>`.
- Outlines are simple black lines.
- Shading is minimal.
- Nexus Cat is acting as a friendly guide or assistant.
- The scene is easy to understand without visual clutter.

Failure signals:

- The cat becomes a different species, color pattern, body type, or clothing design.
- The hoodie symbol disappears or mutates into unrelated text.
- The image becomes realistic, complex, dark, gritty, or heavily rendered.
- The character is only a tiny decoration when the user asked for a mascot scene.
- Old Xiaohei constraints remain, especially "not cute", "deadpan", "absurd worker", or "black solid creature".

## Verification Plan

After implementation:

- Run `rg` for `小黑`, `Xiaohei`, `xiaohei`, `ian-xiaohei`, and `Ian Xiaohei` in user-facing docs and Skill files.
- Confirm README installation instructions use `nexus-cat-mascot`.
- Confirm `SKILL.md` name and description match the new package.
- Confirm references do not contradict the kawaii mascot direction.
- Confirm old example images are not shown in the README.

## Out Of Scope

- Generating a new full example image set during the rewrite.
- Deleting historical image assets unless they are directly harmful to the new user-facing docs.
- Maintaining a Xiaohei compatibility mode.
- Building a frontend app or browser UI.
