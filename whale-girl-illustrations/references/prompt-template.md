# 鲸鱼娘生图与编辑模板

## 使用前

先读取 `whale-girl-ip.md` 和对应资产。生成鲸鱼娘时把下面的实际文件作为 image reference 传给图像工具：

```text
assets/whale-girl-reference/whale-girl-neutral.jpg
assets/whale-girl-reference/whale-girl-smile.jpg
assets/whale-girl-reference/whale-girl-wave.jpg
```

`assets/layout-reference/content-card-spirit.png` 只在内容卡片模式中作为构图和气质参考。不要把参考图当成提示词的替代物，也不要把参考图中的具体中文内容复制到新图。

## 内容卡片模式模板

```text
Generate one standalone Chinese article illustration in a strict 3:4 vertical aspect ratio, not 2:3. Use the supplied whale-girl character reference image to preserve the exact character identity, outfit, hair, whale fin ears, blue tail and refined chibi face. Use the supplied content-card reference only for hand-drawn editorial energy, text hierarchy and asymmetrical spacing, not for its exact copy or composition.

Mode:
Hand-drawn Chinese editorial content card with readable medium-density text. This is not a rigid PPT dashboard, but it may contain a headline, a short subheadline, 2-4 irregular information areas, one speech/reaction bubble and an optional CTA.

Exact copy to preserve:
Headline: {用户指定标题}
Subheadline: {短副标题}
Information blocks: {2-4 short blocks, compressed from only the most important 20%-30% of the source}
CTA or question: {only if supplied or genuinely supported by the source}

Layout:
Near-white warm paper background, deep navy hand-drawn border, pale blue title brush, varied text blocks with clear hierarchy, and one smaller whale-girl placed on the right or lower-right, usually 20%-35% of the canvas. She is thinking, pointing, holding, observing, reacting to or presenting one element. Keep enough area for text. Do not make the whale-girl or a valve/tool the largest object.

Character:
Use the actual supplied reference image, not a generic whale-girl prompt. Keep the navy-blue hair, white frilled maid headband, side blue bow, fin-like ears, navy-and-white maid dress, white apron, blue tail and polished chibi face. Vary only expression, pose and task-related props.

Hand-drawn details:
Deep navy loose border, pale blue brush marks, a few conversational bubbles, small underlines, arrows and restrained doodles. At most one small whale character or one to two tiny whale doodles when they add feedback or rhythm. Never stamp whale symbols on every prop.

Color:
Deep navy/black for structure and main text, blue for character and state, red-orange only for a key conclusion or warning. Background almost white and lightly paper-textured, never yellow, gray or dirty.

Text handling:
Do not invent project names, numbers, stars, labels or extra headlines. If exact Chinese rendering is unreliable, leave clean hand-drawn text areas for post-typesetting instead of replacing the required copy with random text.

Negative constraints:
No 2:3, no horizontal canvas, no huge character, no huge valve or tool, no giant empty illustration with only four labels, no rigid grid, no equal cards, no dashboard, no UI screenshot, no full article, no dense flowchart, no multiple main whale-girls, no generic character without the reference identity, no full-body sketch, no repeated whale logos, no watermark, no signature, no "by ian and 小黑".
```

## 场景隐喻模式模板

```text
Generate one standalone Chinese article illustration in a strict 3:4 vertical aspect ratio, not 2:3. Use the supplied whale-girl reference image as the identity reference.

Core information budget:
Select only about 20%-30% of the source's most important meaning. Express one judgement, one physical action, one relationship and one visible result. Do not summarize the full article.

Visual concept:
{一句话写出唯一物理隐喻}

Whale-girl event:
The referenced whale-girl is {具体动作} on {物件/阻力}, making {核心关系/结果} visible. She is not standing beside the scene as decoration.

Composition:
{角色、物件、动作、留白和视线流向。角色通常 35%-55%，但不要挤掉必要文字。}

Text:
{必要的一句判断或少量短标签。用户给出的精确标题/数字不得改写；必要时后期排版。}

Background and style:
Very pale warm white paper, refined chibi character, hand-drawn border/brush/bubbles/arrows/props, deep navy and black structure, blue character/state, red-orange only for one key result.

Negative constraints:
No 2:3, no huge tool, no PPT card wall, no full article, no multiple characters, no generic whale-girl, no full-body sketch, no repeated whale motifs, no yellow/gray background, no watermark, no signature, no "by ian and 小黑".
```

## 编辑模板

```text
Edit the supplied image into a strict 3:4 vertical final composition. Preserve the whale-girl identity from the supplied reference, the pale warm-white background, deep-navy hand-drawn structure and the existing text hierarchy. Change only {需要修正的对象}. Reduce the whale-girl/tool if it blocks the text, restore readable text regions, and keep the character polished. Do not add extra characters, repeated whale motifs, invented numbers, watermark, signature or "by ian and 小黑".
```

## 生成前草稿

```text
模式：
核心判断：
必须保留的精确文字：
鲸鱼娘参考图：
鲸鱼娘作用与比例：
构图：
后期排版：
```
