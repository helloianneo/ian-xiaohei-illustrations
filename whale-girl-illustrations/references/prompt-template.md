# 鲸鱼娘单张生图提示词模板

## 使用方式

先完成信息提炼和构图，再把变量填入模板。每次只生成一张图，不把多个候选构图写进同一次提示词。中文标签应尽量短；如果模型容易错字，宁可去掉标签，后期再局部编辑或排版。

## 单张生成模板

```text
Generate one standalone Chinese article illustration in a strict 3:4 vertical aspect ratio, for example 1080x1440. Do not use 2:3 as the default ratio.

Core information budget:
Use only about 20%-30% of the source text's most important information. Express one core judgement, one main action, one relationship, and at most one visible result. Do not summarize or restate the full article.

Visual concept:
{用一句话写出本图唯一的视觉隐喻}

Whale-girl event:
Whale-girl is the main character and must perform the central action: {拉 / 捞 / 修 / 接 / 分流 / 守门 / 测量 / 递交 / 打开 / 其他具体动作}. She is acting on {主要物件或阻力}, so the viewer can see {核心关系或结果}. Do not make her a decorative character standing beside the scene.

Character style:
One refined chibi whale-girl as the default main subject. Precise, clean, readable face, hands, hair, clothing and whale features. About 70% polished chibi character illustration and 30% light hand-drawn feeling. Keep the character refined and complete; do not turn the whole body into a rough sketch.

Optional small whale:
{none / one small whale only if it expresses input, feedback, companionship, scale, or result}. Do not add it only as decoration.

Composition:
{描述纵向画面中角色、物件、动作、留白和视觉流向。不要写成网格、卡片或正式流程图。}

Background and material:
Very pale warm white, almost white, with an extremely subtle paper feel. Clean and airy. No obvious yellow, gray, brown, dirty vintage paper, heavy grain, dark background, or large shadow.

Line and supporting hand-drawn elements:
Refined clean character linework. Light hand-drawn texture may appear in the border, pale blue title brush, speech bubble, arrows, props and paper feel. Keep the character itself polished, not fully sketchy.

Color rules:
Use dark navy and black for structure, outlines and main text. Use blue for the whale-girl, water, state and feedback. Use red-orange only for one key conclusion, warning, resistance or result. Keep all colors restrained.

Chinese labels:
{0-4 short labels, each 2-8 Chinese characters, only if necessary}. Do not add paragraphs, a table, a legend, a numbered list, a watermark or a signature.

Negative constraints:
No 2:3 default output, no horizontal canvas, no PPT infographic, no card wall, no dashboard, no UI screenshot, no dense flowchart, no course slide, no nine-panel layout, no full article text, no multiple main whale-girls, no whale pattern repeated on every prop, no decorative whale stickers everywhere, no cute mascot pose, no childish cartoon, no fully rough-sketch character, no obvious yellow or gray background, no heavy vintage paper, no plastic 3D, no excessive gradients, no large shadows, no "by ian and 小黑", no watermark, no signature.
```

## 图片编辑模板

```text
Edit the provided image into a strict 3:4 vertical final composition. Preserve the core whale-girl event, refined character quality, pale warm-white background and restrained colors. Remove only {要删除或修正的对象}. Do not add new characters, extra whale motifs, dense text, watermark, signature, or "by ian and 小黑". Keep the character polished and keep the final image from becoming a PPT card wall.
```

## 提示词生成前的四行草稿

```text
核心判断：
鲸鱼娘动作：
唯一隐喻：
必要标签：
```

如果这四行里出现多个判断、多个主角或超过 4 个必要标签，先回到 `visual-distillation.md`，不要直接生成。
