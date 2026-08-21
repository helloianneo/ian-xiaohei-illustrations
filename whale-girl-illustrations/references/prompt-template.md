# 鲸鱼娘单张生图提示词模板

每张图单独生成。用户明确要求生成时直接调用内置 `image_gen`，不把多张图拼在一张里。

## 主模板

```text
Generate one standalone 3:4 vertical Chinese article illustration.

Visual DNA:
Very pale warm-white background, almost white. Deep navy slightly wobbly hand-drawn outer frame. Pale blue brush marks, handwritten underlines and a few speech bubbles. Sparse blue notes and small red/orange emphasis. Clean hand-drawn editorial/product-sketch feeling. One clear core action or visual metaphor. Keep a calm blank area. No gradients, no strong shadows, no dirty yellow paper, no gray background, no PPT infographic, no equal card grid, no UI screenshot, no commercial flat illustration.

Recurring IP character required:
Use the supplied whale-girl reference image as the identity reference. She is a refined chibi blue-haired whale girl with a white lace maid headband, side blue bow, whale-fin ears, navy-and-white maid dress, white apron and blue whale tail. Preserve her face, outfit, hair, fins and tail. She must perform the core conceptual action, not stand beside the scene as decoration.

Small whales:
Normally include 0-1 small whale. Add 2-4 only when group, scale, feedback, water flow, companionship, result or continuous action is genuinely needed; add more only when the scene cannot read without them. Vary their size and action. Do not stamp whale symbols on every object.

Theme:
{当前文案的主题}

Structure type:
{Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Core idea:
{这张图唯一要表达的核心意思}

Composition:
{鲸鱼娘在哪里、正在做什么、主要物件是什么、信息如何流动、留白在哪里}

Chinese handwritten labels:
{3-8 个短标注；只有用户明确提供的短标题、项目名和数字才保留；不要完整文章，不要结构类型标题}

Color use:
Deep navy/black for line art, outer frame and main structure. Blue for the whale-girl, small whales, state and feedback. Pale blue for brush marks, underlines and bubbles. Red/orange only for a few key warnings, results or paths.

Constraints:
Strict 3:4 vertical canvas. One image explains one core structure. Keep the main subject group around 40%-60% of the canvas and leave a quiet blank area. Make the whale-girl and small whales interact with the object or path. Use short handwritten Chinese labels with varied placement, not a typed dashboard. If a user-supplied headline is needed, render it as a modest hand-drawn caption, never a giant top-left title.

Avoid:
2:3, horizontal canvas, rigid card wall, equal boxes, dashboard, formal flowchart, dense explainer, long paragraphs, giant title, giant prop, pure character standing pose, generic blue girl without the reference identity, full-body sketch, repeated whale logos, plastic 3D, strong gradients, gray/yellow background, watermark, signature, QR code, "by ian and 小黑".
```

## 生成前短草稿

```text
主题：
结构类型：
核心意思：
鲸鱼娘动作：
小鲸鱼动作和数量：
主要物件：
短标注：
```

## 编辑模板

```text
Edit the supplied image while preserving the strict 3:4 vertical composition, the refined whale-girl identity, the very pale warm-white background, deep navy hand-drawn frame, pale blue brush marks and the existing core action. Change only {需要修正的对象}. Keep the image sparse, hand-drawn and readable. Do not add a card wall, giant title, extra main character, repeated whale symbols, watermark, signature or "by ian and 小黑".
```
