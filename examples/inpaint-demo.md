INPAINT DEMO

Source image used for demo: examples/images/04-handoff-path.png
Fusion reference: examples/images/fusion-reference.png

This demo demonstrates the recommended inpaint prompt and parameters to replace the default character with the user's fusion IP while preserving composition and line style.

Prompt (english):
Edit the provided image. Replace the character "Little Black" with the fusion IP: cat-bodied main silhouette with integrated duck head/neck/wing elements scaled smaller (follow examples/images/fusion-reference.png for proportions). Keep the hand-drawn wobbly black outline (medium thickness), flat white fill, and preserve all labels and props. Do not add shadows or gradients. Mask: tight to the character area. Denoising: 0.35. Steps: 30. Sampler: DPM++ SDE Karras (or default available). Guidance scale: 7.5.

Mask instructions:
- Create a tight mask around the current character pixels (use feather 2-6 px depending on resolution).
- Invert mask if tool requires.

Notes:
- If the model renders duck elements too large, explicitly add the negative prompt: "duck larger than cat, two separate characters, photorealistic, high detail textures".
