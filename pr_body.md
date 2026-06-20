Replace default IP (小黑) with user-provided cat/duck IP and update prompts

- Summary: Replace the default visual IP (Little Black) with the user's provided IP (cat/duck/fusion), update prompt templates to support {IP=cat|duck|fusion}, and add explicit fusion proportion guidance (reference image 8).
- Files changed:
  - ian-xiaohei-illustrations/references/xiaohei-ip.md
  - ian-xiaohei-illustrations/references/prompt-template.md
  - README.md

Purpose: Enable the Skill to generate and edit illustrations centered on the user's IP while preserving Ian's hand-drawn visual language (wobbly black outlines, abundant whitespace, minimal accent colors). Provide clear inpaint/edit prompts so existing images that contain Little Black can be replaced by the user's IP.
