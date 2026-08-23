# 鲸鱼娘信息丰富单张生图提示词模板

每张图单独生成。用户明确要求生成时直接调用内置 `image_gen`；系列模式也要逐页生成，不把多张图拼成一张。信息丰富模式要增加有用文字和层级，不要把全文缩成不可读的小字墙。

## 主模板

```text
Generate one standalone 3:4 vertical Chinese Xiaohongshu-style hand-drawn content illustration.

Visual DNA:
Very pale warm-white paper background, almost white. Deep navy slightly wobbly hand-drawn outer frame. Pale blue brush marks behind headings, handwritten underlines, a few speech bubbles, sparse blue doodles and only a few red/orange emphases. Refined hand-drawn Chinese content-page feeling with clear hierarchy and breathing room. One main topic and one visual anchor. In rich-information mode, allow 3-5 related hand-drawn content sections around the visual anchor. Do not make a rigid business PPT, dashboard or equal card grid.

Recurring IP character required:
Use the supplied whale-girl reference image as the identity reference. She is a refined chibi blue-haired whale girl with a white lace maid headband, side blue bow, whale-fin ears, navy-and-white maid dress, white apron and blue whale tail. Preserve her face, outfit, hair, fins and tail. She must perform one action connected to the topic, not stand beside the information as decoration. In rich-information mode, keep her usually around 25%-40% of the canvas so the text has room.

Small whales:
Normally include 0-1 small whale. Add 2-4 only when group, scale, feedback, water flow, companionship, result or continuous action is genuinely needed; add more only when the scene cannot read without them. Vary their size and action. Do not stamp whale symbols on every object.

Information density:
{简洁隐喻 / 信息丰富单页 / 信息丰富系列页}
For rich-information mode: use one clear headline, an optional subtitle, 3-5 related content sections, 10-18 short text units, and optional key numbers, conclusion or CTA. Each section should have a short heading plus 1-3 short lines or bullet fragments. Use readable short Chinese lines, not long paragraphs. Preserve user-supplied names, numbers and conclusions exactly; do not invent metrics, stars, versions or dates.

Theme:
{当前文案的主主题}

Structure type:
{信息丰富单页 / 信息丰富系列页 / Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Page or series context:
{单页；或第几页、这一页只讲哪个独立小主题}

Visual anchor:
{鲸鱼娘在哪里、正在做什么、主要物件是什么、读者先看到什么关系}

Headline and subtitle:
{用户提供的标题、副标题；没有就写一个短而具体的标题}

Title hierarchy:
The main headline must be the first visual anchor and clearly larger than every section heading. Reserve a distinct upper title zone, usually about 16%-24% of the canvas. Keep quiet space below the headline before the subtitle or first information section begins. Emphasize only one exact keyword using either red-orange text, a pale-blue brush backing, a slightly larger size, or a heavier weight. Keep project slugs, repository names and one-line descriptions visibly smaller than the main headline.

Content sections:
{3-5 个信息区：每区的小标题、1-3 行短说明、需要强调的数字或关键词}

Footer:
{可选的一句结论、CTA、使用建议或页码}

Color use:
Deep navy/black for line art, outer frame, main headings and structure. Blue for the whale-girl, small whales, state and feedback. Pale blue for brush marks, section underlines, bubbles and supporting areas. Red/orange only for a few key warnings, results or paths.

Constraints:
Strict 3:4 vertical canvas. Keep one main topic and one visual anchor. For rich-information mode, arrange 3-5 related sections with varied sizes and positions, leaving enough blank space between them. The whale-girl and any small whales must interact with the object or path. Use exact short Chinese text in separate readable blocks with clear hierarchy: headline, subtitle, section headings, short body lines, key numbers and optional footer. The headline must be noticed before the sections, but must not consume most of the upper canvas. Keep body text and the first section out of the quiet space around the headline. Use hand-drawn frames, blue under-brushes, bubbles and arrows selectively; do not put every sentence in an identical box.

Avoid:
2:3, horizontal canvas, giant title taking over the page, tiny unreadable text wall, full article, long paragraphs, rigid equal boxes, rigid 3x3 grid, dashboard, formal flowchart, UI screenshot, commercial flat illustration, pure character poster, pure standing pose, generic blue girl without the reference identity, full-body sketch, repeated whale logos, plastic 3D, strong gradients, gray/yellow background, watermark, signature, QR code, "by ian and 小黑".
```

## 生成前短草稿

```text
主题：
密度模式：简洁隐喻 / 信息丰富单页 / 信息丰富系列页
页面主题（系列时填写）：
标题与副标题：
视觉锚点：
鲸鱼娘动作：
小鲸鱼动作和数量：
信息区 1–5：
关键数字或结论：
底部收束句：
```

## 编辑模板

```text
Edit the supplied image while preserving the strict 3:4 vertical composition, the refined whale-girl identity, the very pale warm-white background, deep navy hand-drawn frame, pale blue brush marks, existing text hierarchy and information density. Change only {需要修正的对象}. Keep the exact user-supplied names, numbers and conclusions. Keep the whale-girl doing the core action. Do not turn the image into a sparse character poster, rigid card wall, tiny unreadable text wall, repeated whale symbols, watermark, signature or "by ian and 小黑".
```
