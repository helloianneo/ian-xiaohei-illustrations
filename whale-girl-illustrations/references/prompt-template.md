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

## 小红书首图模板

```text
Generate one Xiaohongshu cover in a strict 3:4 vertical canvas, 1080x1440, using the supplied whale-girl reference image for the exact character identity and the supplied layout reference only for its hand-drawn editorial energy.

Cover job:
Make the topic understandable at thumbnail size. Preserve only this short hook: {精确标题}. Add at most one supporting fact/result: {项目名、数字或一句事实}. Do not place the full article, feature list or tutorial on the cover.

Composition:
Near-white warm paper, deep navy loose border, pale blue title brush, strong but not oversized Chinese title in the upper safe area, one clear visual action, and one smaller whale-girl on the right or lower-right occupying about 20%-30% of the canvas. The whale-girl may point, react, hold or inspect one relevant object, but the title and evidence remain readable.

Series lock:
{整组轮播共享的边框、底刷、颜色、字体层级、纸感和角色参考。}

Text handling:
Render exact Chinese, project names and numbers in post-typesetting whenever possible. Leave clean areas for text instead of generating fake Chinese.

Negative constraints:
No 2:3, no huge character, no huge prop, no full article, no crowded feature list, no generic whale-girl, no repeated whale motifs, no watermark, no signature, no "by ian and 小黑".
```

## 小红书轮播单页模板

```text
Generate page {页码}/{总页数} of a Xiaohongshu carousel in a strict 3:4 vertical canvas, 1080x1440. Use the supplied whale-girl reference image to preserve the same character identity as the cover. Use the same series lock: {边框、底刷、颜色、字体层级、纸感}.

This page's one takeaway:
{读者看完这一页要记住的一句话}

Page role:
{问题 / 亮点 / 证据 / 使用步骤 / 判断 / 总结}

Exact copy:
Title: {页标题}
Body: {2-4 short lines or short bullets, compressed from the source}
Evidence: {official screenshot, project name, star count or supplied fact, only when relevant}

Layout:
Keep the text and evidence as the main reading area. Let the whale-girl occupy about 8%-18% when the page is information-heavy, appearing as a small reaction, partial figure, hand, face or tail if that preserves space. Give her a concrete relation to the page topic. Avoid repeating the cover pose.

Text handling:
Exact Chinese, numbers, code, project names and stars must be added by post-typesetting or carefully checked after rendering. Never invent text or metrics.

Negative constraints:
No 2:3, no long-poster crop, no equal card wall, no full article, no oversized character, no decorative whale stamp on every object, no watermark, no signature, no "by ian and 小黑".
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
