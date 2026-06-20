# Prompt 模板（替换稿：支持你的 IP）

本模板为生成与编辑正文配图的可复用 prompt 结构，已将 Skill 中的“小黑”替换为可选 IP（{IP=cat}、{IP=duck}、{IP=fusion}）。在使用时把 {IP=...} 替换为需要的角色。

注意：每张图单独生成，保持 16:9 横版，中文短标注。

---

## 基本生成模板（中文）
Generate one standalone 16:9 horizontal Chinese article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines. Lots of empty white space. Sparse yellow/pink/blue handwritten Chinese annotations. Clean absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex background, no commercial vector style, no PPT infographic look, no cute mascot poster, no children's illustration, no realistic UI.

Recurring IP character required:
Use {IP=cat} or {IP=duck} or {IP=fusion}. The character is a white-bodied, black-marked simplified creature with small white-dot or line eyes and thin legs/appendages. It must perform the core conceptual action — not merely decorate the scene. Keep the character deadpan, slightly odd, and not cute.

Theme:
{正文配图主题 — 用一句话描述图要表达的核心概念}

Structure type:
{Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Core idea:
{一句话核心意图}

Composition:
{具体画面：IP 在哪里、正在做什么、主要物件是什么、信息如何流动}

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese handwritten labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4} / {可选标注词5}

Color use:
Black for main line art and IP markings. Yellow for main flow/path/arrows or IP beak/feet/highlights. Red only for key warnings/problems/results. Blue only for secondary notes or feedback/system state. Keep palette minimal (black/white + up to 2 emphasis colors).

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, or dense explainer. Do not copy prior examples or reuse known case compositions unless explicitly requested; invent a fresh visual metaphor for this specific article. It should be clear but not instructional, interesting but not childish, strange but clean.

---

## 图像编辑提示（inpaint / edit）
场景：把已有图里的“小黑”替换为你的 IP。

Edit the provided image. Replace every occurrence of the character “小黑” with the user's chosen IP character (use {IP=cat} / {IP=duck} / {IP=fusion}). Keep composition, line style, color palette, and all other elements unchanged. Match the hand-drawn black outline stroke (medium thickness, slightly wobbly). Keep the white background and any handwritten Chinese labels intact. Do not add new text or objects.

具体中文指令示例：
请编辑这张图：把画面里所有的小黑位置逐个替换成图1（猫）/ 图2（鸭） / 图3（合体）。替换要求：
- 保持原轮廓线笔触（中等粗、略抖动、黑色），线条收尾圆润。
- 新角色保留其典型特征（猫的黑斑/胡须，鸭的黄色喙/脚），但填色要与画面一致（平涂、无渐变）。
- 保留相同动作与朝向（直接替换姿势），如需微调以匹配动作可小幅修改，但不要改变主体占比或构图。
- 保留所有注释文字与装饰，只替换角色区域并确保边缘自然过渡。
- 不要新增文字或元素。

---

## 生成/编辑的技术提示（建议）
- 线条笔感：使用中等粗、略有 jitter 的墨线笔刷，避免平滑光滑的矢量线。  
- 色彩控制：限定强调色为黄色/粉/淡蓝，避免引入其他高饱和色。  
- img2img 参数建议（仅作参考）：denoising 0.35–0.5，steps 20–40，mask 为角色区域。  
- QA：替换后检查角色是否承担核心动作、是否过度可爱、线条与背景是否匹配、中文标注是否≤5 条。

---

## Prompt 示例（可直接复制）
1) 单张生成（使用猫）：
Use $ian-xiaohei-illustrations 为“从想法到发布的承接路径”生成一张 16:9 横版正文配图。视觉风格：纯白背景、手绘黑线、少量黄色/粉/蓝批注。将 Skill 默认角色替换为我的 IP（{IP=cat}），让猫承担牵线/承接动作。中文标注不超过 5 个简短词。

2) 编辑（inpaint）现有图：
Edit the provided image. Replace the character “小黑” with the user's IP: {IP=duck}. Keep all other elements unchanged. Match the medium-thick wobbly black outline and white-fill style. Do not add or remove labels.

（结束）
