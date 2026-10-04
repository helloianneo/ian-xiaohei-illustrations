# 生图提示词模板

每张图单独生成。根据正文内容替换变量，不要把多张图拼在一起。

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Visual DNA:
Crisp pixel-art illustration with visible square pixels, stepped edges, and a limited palette. Orange is the dominant subject color; black, white, and dark gray are supporting colors. Include a simple pixel-art environment that clearly fits the current theme, place, and action. Keep the environment low-detail and low-contrast so it supports the story without competing with 橘子头. Preserve a calm open area for visual breathing room. Sparse, readable Chinese pixel-font annotations. No anti-aliasing, smooth vector edges, gradients, glow, paper texture, irrelevant or complex background, PPT infographic look, 3D rendering, or realistic UI.

Recurring IP character required:
橘子头, a chibi pixel-art person with an oversized head and small body, voluminous tousled orange short hair, light face, simple vertical black pixel eyes, tiny nose and smile, subtle orange freckles, thick stepped black pixel outline, loose black jacket, white shirt, dark trousers, and white sneakers with small orange details. Match the identity anchors in the provided reference image. 橘子头 must perform the core conceptual action, not decorate the scene. Keep the expression simple, calm, and focused.

Theme:
{正文配图主题}

Structure type:
{结构类型：Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Core idea:
{这张图要表达的核心意思}

Composition:
{具体画面：橘子头在哪里、正在做什么、主要物件是什么、信息如何流动}

Scene background:
{符合当前画面的背景：发生地点、必要环境元素、前中后景关系；不要使用与主题无关的装饰}

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese pixel-font labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4} / {可选标注词5}

Color use:
Orange for 橘子头's hair, the main subject, key path, and focal accents. Black for pixel outlines and primary text. White for highlights and open areas. Dark gray for limited secondary depth. The scene background may use a few muted supporting colors when the setting requires them, but no background color should be stronger than orange.

Constraints:
One image explains only one core structure. Keep the main subject and core objects around 40%-65% of the canvas. Give the background enough scene information to establish the setting, while preserving one calm open area. Do not leave 橘子头 floating on an empty canvas unless a pure white background is explicitly requested. Use at most 5-8 short Chinese pixel-font labels. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, game screenshot, or dense explainer. Do not copy the reference image's standing pose, composition, or background; invent a fresh visual metaphor and matching environment for this specific article. Keep every character, object, arrow, label, and background element on the same pixel grid. It should be clear, interesting, and not childish.
```

## 图像编辑提示

去掉左上角标题：

```text
Edit the provided image. Remove only the pixel-font title "{要删除的文字}" and its underline from the top-left corner. Fill that area with the same clean white background. Preserve everything else exactly: characters, labels, paths, pixel style, composition, aspect ratio, and image quality. Do not add any new text or objects.
```

增强角色参与感：

```text
Regenerate this illustration with the same core meaning and simple layout, but make 橘子头 more central to the conceptual action. 橘子头 should be doing the work that explains the idea, not standing beside the diagram. Add a simple pixel-art background that matches the current setting and action, while keeping it low-detail and secondary. Preserve the orange hair, chibi proportions, simple pixel face, black-and-white outfit, crisp pixel grid, and orange-dominant palette.
```
