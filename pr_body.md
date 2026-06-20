Replace default IP (小黑) with user-provided cat/duck IP and update prompts

- Summary: Replace the default visual IP (Little Black) with the user's provided IP (cat/duck/fusion), update prompt templates to support {IP=cat|duck|fusion}, and add explicit fusion proportion guidance (see examples/images/fusion-reference.png).
- Files changed:
  - ian-xiaohei-illustrations/references/xiaohei-ip.md
  - ian-xiaohei-illustrations/references/prompt-template.md
  - README.md
  - examples/inpaint-demo.md
  - examples/images/fusion-reference.png

Purpose: Enable the Skill to generate and edit illustrations centered on the user's IP while preserving Ian's hand-drawn visual language (wobbly black outlines, abundant whitespace, minimal accent colors). Provide clear inpaint/edit prompts so existing images that contain Little Black can be replaced by the user's IP.

Notes / QA checklist for reviewers:

- These are documentation and prompt-template changes only; example images added for reference and demo — no production artwork replaced.
- Please confirm the fusion reference image (examples/images/fusion-reference.png) is visible and matches expected proportions.
- Optional demo: examples/inpaint-demo.md documents the recommended inpaint prompt and parameters (mask, denoising, steps). If maintainers want an automated demo image, we can add before/after PNGs produced by your pipeline.

QA checks (recommended before merge):
1. Verify examples/images/fusion-reference.png loads correctly in the PR file viewer and visually matches the intended fusion proportion (cat body dominant, duck elements small and integrated).
2. Confirm prompt-template.md inpaint examples include sufficient negative prompts to avoid generating a second equal-sized duck (e.g., "duck larger than cat, two separate characters").
3. Run a repository-wide search for the string "小黑" to check remaining references; decide whether to keep, annotate as historical example, or replace.
4. Confirm that README change does not break installation or usage examples (these are text-only edits).

cc @helloianneo — This PR updates documentation and prompt templates to support user-provided IPs (cat/duck/fusion). It adds a fusion reference image and an inpaint demo guide. No generated artwork was changed; only reference/example assets were added.
