# Nexus Cat Mascot Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把现有 Xiaohei 正文配图 Skill 重构为 `nexus-cat-mascot`，默认生成一致的 Nexus Cat kawaii 开发者助手吉祥物。

**Architecture:** 这是文档型 Codex Skill 包重构，不需要运行时业务代码。实施重点是目录重命名、Skill 元数据重写、reference 规则重写、README/示例同步，以及用全文搜索验证旧 IP 口径已从用户可见文档中移除。

**Tech Stack:** Markdown, YAML, Codex Skill file structure, git, `rg`.

---

## File Structure

最终结构应为：

```text
.
├── README.md
├── examples/
│   ├── images/
│   └── prompts.md
└── nexus-cat-mascot/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── assets/
    │   └── examples/
    └── references/
        ├── composition-patterns.md
        ├── nexus-cat-ip.md
        ├── prompt-template.md
        ├── qa-checklist.md
        └── style-dna.md
```

旧图片资产保留在 `examples/images/` 和 `nexus-cat-mascot/assets/examples/`，但 README 不展示它们。

### Task 1: Rename Skill Package And IP Reference

**Files:**
- Rename: `ian-xiaohei-illustrations/` -> `nexus-cat-mascot/`
- Rename: `nexus-cat-mascot/references/xiaohei-ip.md` -> `nexus-cat-mascot/references/nexus-cat-ip.md`

- [ ] **Step 1: Check current tree**

Run:

```bash
find ian-xiaohei-illustrations -maxdepth 3 -type f | sort
```

Expected: output includes `ian-xiaohei-illustrations/SKILL.md`, `agents/openai.yaml`, and `references/xiaohei-ip.md`.

- [ ] **Step 2: Rename the Skill directory with git**

Run:

```bash
git mv ian-xiaohei-illustrations nexus-cat-mascot
```

Expected: command exits successfully.

- [ ] **Step 3: Rename the IP reference file with git**

Run:

```bash
git mv nexus-cat-mascot/references/xiaohei-ip.md nexus-cat-mascot/references/nexus-cat-ip.md
```

Expected: command exits successfully.

- [ ] **Step 4: Verify renamed paths**

Run:

```bash
find nexus-cat-mascot -maxdepth 3 -type f | sort
```

Expected: output includes `nexus-cat-mascot/SKILL.md` and `nexus-cat-mascot/references/nexus-cat-ip.md`. It should not include `xiaohei-ip.md`.

- [ ] **Step 5: Commit rename**

Run:

```bash
git add nexus-cat-mascot
git commit -m "chore: rename skill package to nexus cat mascot"
```

Expected: commit succeeds.

### Task 2: Rewrite README Positioning And Installation

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Replace README with Nexus Cat positioning**

Replace `README.md` with this content:

````markdown
# Nexus Cat Mascot

> Generate a consistent kawaii developer-assistant mascot named Nexus Cat.
>
> Chubby gray-and-white cat | hoodie with `</>` | friendly guide | same character across every image and panel | Codex Skill

---

## 这个仓库是什么

Nexus Cat Mascot 是一个 Codex Skill，用来指导 AI Agent 生成稳定一致的 kawaii 吉祥物图。

默认视觉 IP 是 Nexus Cat：一只灰白毛色、圆胖身体、大圆眼、脸颊腮红、简单黑色描边、最少阴影、穿着 `</>` hoodie 的友好猫咪助手。

它的核心目标不是做正式流程图，也不是生成随机猫咪贴纸，而是让同一个 Nexus Cat 在不同场景、动作和 panel 里保持一致设计，作为开发者助手、产品向导、文档陪伴者和友好讲解员出现。

一句话：**让每张图里都是同一只 Nexus Cat，在认真帮读者理解或完成一件事。**

---

## 适合谁用

特别适合：

- 需要稳定品牌吉祥物形象的人
- 写产品文档、教程、博客、发布说明，需要友好配图的人
- 做 AI、开发工具、自动化、SaaS、内容工作流相关视觉表达的人
- 想生成同一只角色在不同姿势、表情、动作、场景里的图片的人
- 用 Codex 做内容生产，希望复用一套 mascot prompt 规则的人

不适合：

- 想要真实猫咪摄影的人
- 想要复杂商业 KV、精致 3D 渲染或厚重插画的人
- 想要正式 PPT 信息图、架构图或大量文字解释图的人
- 需要严格可编辑矢量源文件的人
- 不需要角色一致性的随机贴纸生成任务

---

## 它会产出什么

默认输出：

- 单张 Nexus Cat mascot 场景图
- 一组同角色、多动作、多场景 shot list
- 多 panel 教程或说明图的角色设计提示
- 每张图的用途、场景、动作、表情、道具和可选文字标注建议
- 最终 PNG 图片，保存到 workspace 的 `assets/<topic-slug>-nexus-cat/`

默认不输出：

- PPTX / PDF / Keynote
- SVG / HTML / Canvas 可编辑图
- 正式流程图或复杂架构图
- 大段文字型信息图

---

## 固定角色设计

Nexus Cat 必须保持这些特征：

- chubby round body
- gray-and-white fur
- big round eyes
- blush cheeks
- simple black outlines
- minimal shading
- hoodie with `</>` symbol
- friendly guide and assistant behavior
- same character design repeated across all panels

可以改变动作、表情、道具和场景，但不能改变物种、毛色、hoodie、身体轮廓、眼睛风格或整体识别度。

---

## 安装

克隆仓库：

```bash
git clone https://github.com/helloianneo/ian-xiaohei-illustrations.git
cd ian-xiaohei-illustrations
```

复制 skill 到 Codex skills 目录：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./nexus-cat-mascot "${CODEX_HOME:-$HOME/.codex}/skills/"
```

安装后，在 Codex 里使用：

```text
Use $nexus-cat-mascot 为这篇教程设计并生成 4 张 Nexus Cat 吉祥物配图。
```

---

## 怎么用

### 只做 shot list

```text
Use $nexus-cat-mascot 先不要生图。
请为下面这篇产品教程设计 5 张 Nexus Cat 配图。
每张写清楚：用途、场景、Nexus Cat 动作、表情、道具、背景复杂度、可选文字标注。

<粘贴文章>
```

### 直接生成一组图片

```text
Use $nexus-cat-mascot 为“AI 助手帮开发者修复 bug”生成 4 张 Nexus Cat 吉祥物图。
要求同一只角色反复出现：灰白猫、圆胖身体、大圆眼、腮红、黑色描边、深色 hoodie、胸口 `</>`。
```

### 为单个场景生成一张图

```text
Use $nexus-cat-mascot 生成一张图：
Nexus Cat 坐在小终端旁边，把一个红色 bug 图标递给开发者。
风格可爱、干净、简单黑描边、最少阴影、白底。
```

### 多 panel 教程图

```text
Use $nexus-cat-mascot 生成一张 3-panel 教程图：
同一只 Nexus Cat 依次展示“读取需求、写代码、提交结果”。
每个 panel 都必须保持同一角色设计，不要变成不同猫。
```

更多示例见 `examples/prompts.md`。

---

## 工作流程

这个 Skill 的流程是：

1. 读取用户给的主题、文章、产品功能、文档片段或场景描述。
2. 提炼适合 Nexus Cat 出现的场景和动作。
3. 如果用户只要规划，输出 shot list。
4. 如果用户要求生成，逐张调用图像模型，不默认拼图。
5. 每张图都重复 Nexus Cat 的固定角色设定。
6. 多张图或多 panel 时，强制要求 same character design repeated across all panels。
7. 按 QA checklist 检查角色一致性、hoodie、灰白毛色、圆胖体型、友好助手气质和画面简洁度。
8. 保存最终 PNG，并报告用途和路径。
````

- [ ] **Step 2: Verify README no longer displays old example images**

Run:

```bash
rg -n "examples/images|01-two-breakpoints|小黑|Xiaohei|xiaohei|怪诞|不卖萌|不要可爱" README.md
```

Expected: only repository URL text may include `ian-xiaohei-illustrations`; no old image paths, Xiaohei positioning, or anti-cute constraints appear.

- [ ] **Step 3: Commit README rewrite**

Run:

```bash
git add README.md
git commit -m "docs: rewrite readme for nexus cat mascot"
```

Expected: commit succeeds.

### Task 3: Rewrite Skill Metadata And Agent Manifest

**Files:**
- Modify: `nexus-cat-mascot/SKILL.md`
- Modify: `nexus-cat-mascot/agents/openai.yaml`

- [ ] **Step 1: Replace `nexus-cat-mascot/SKILL.md`**

Replace `nexus-cat-mascot/SKILL.md` with this content:

````markdown
---
name: nexus-cat-mascot
description: 生成一致的 Nexus Cat kawaii 吉祥物图片。用于用户要求为文章、教程、产品文档、开发工具、AI 工作流、发布说明、贴纸、panel、助手形象或品牌配图生成同一只灰白猫开发者助手；默认角色是圆胖灰白猫、大圆眼、腮红、黑色描边、最少阴影、穿 `</>` hoodie，并在所有图片和 panel 中保持一致。
---

# Nexus Cat Mascot

## 核心定位

为用户生成稳定一致的 Nexus Cat 吉祥物图。Nexus Cat 是一只 kawaii 开发者助手猫：灰白毛色、圆胖身体、大圆眼、脸颊腮红、简单黑色描边、最少阴影、穿着带 `</>` 符号的 hoodie。

这个 Skill 的目标是让同一只 Nexus Cat 在不同场景中作为友好向导和助手出现。它可以服务文章、教程、文档、产品功能、开发者工具和 AI 工作流配图，但核心不是正式信息图，而是角色一致的 mascot scene。

## 先读这些参考

按任务需要读取，不要一次塞满上下文：

- `references/nexus-cat-ip.md`：Nexus Cat 固定角色设计、性格、动作库和禁止漂移规则。
- `references/style-dna.md`：kawaii mascot 视觉风格、颜色、背景、文字和禁忌。
- `references/composition-patterns.md`：场景类型、panel 类型和多图一致性规则。
- `references/prompt-template.md`：单张图和多 panel 的提示词模板。
- `references/qa-checklist.md`：生成后检查和迭代规则。
- `assets/examples/`：旧资产只作历史文件保留，不作为默认视觉校准来源。

## 工作流

### 1. 消化输入

先读用户给的主题、文章、链接、Markdown、Notion 内容、截图内容或场景描述。提炼：

- 这张图或这组图要服务什么用途
- Nexus Cat 应该帮助读者理解什么
- 需要单张、多个独立场景，还是多 panel
- 是否需要中文或英文短标注
- 是否有产品、开发、AI、文档或教程上下文

### 2. 先出 shot list

如果用户只是说“分析怎么配图 / 先规划 / 先不要生图”，先给 shot list。每张图写清楚：

- 用途
- 场景
- Nexus Cat 动作
- 表情
- 道具
- 背景复杂度
- 可选文字标注

默认 3-6 张。很短的主题 1-3 张；长文也不要轻易超过 8 张。

### 3. 单张生成

如果用户明确要求“生成 / 输出 / 做图 / 帮我生成”，不要停下来等确认；用内置 `image_gen` 每张单独生成。不要把多张图拼在一张里，除非用户明确要求 multi-panel。

每张图的提示词必须包含：

- Nexus Cat, same consistent kawaii mascot character
- chubby round gray-and-white cat
- big round eyes
- blush cheeks
- simple black outlines
- minimal shading
- wearing a hoodie with `</>` symbol
- friendly guide and assistant
- same character design repeated across all panels when multi-panel

### 4. 检查与迭代

生成后检查 `references/qa-checklist.md`。如果出现以下问题，优先重生成或局部编辑：

- Nexus Cat 变成了不同猫、不同毛色或不同衣服
- hoodie 上没有 `</>` 或符号变成乱码
- 身体不圆胖、眼睛不圆、没有腮红
- 画面过于真实、复杂、阴暗或厚重
- 角色只是角落装饰，没有承担助手动作
- 多张图或多 panel 中角色设计不一致

### 5. 保存交付

如果用户在 workspace 内工作，把最终图复制到：

```text
assets/<topic-slug>-nexus-cat/
```

按顺序命名：

```text
01-topic-name.png
02-topic-name.png
```

保留原始生成文件，不要覆盖已有资产，除非用户明确要求替换。

## 输出口径

生成前的策略输出要短而准。生成后的交付要包含：

- 生成了几张
- 每张图的用途
- 保存路径
- 哪些图最稳，哪些图需要继续迭代

不要长篇解释风格理论；重点说明 Nexus Cat 是否保持一致、是否完成了用户要的动作。
````

- [ ] **Step 2: Replace `nexus-cat-mascot/agents/openai.yaml`**

Replace `nexus-cat-mascot/agents/openai.yaml` with this content:

```yaml
interface:
  display_name: "Nexus Cat Mascot"
  short_description: "生成一致的 Nexus Cat kawaii 开发者助手吉祥物图"
  default_prompt: "Use $nexus-cat-mascot to 为这个主题设计并生成几张 Nexus Cat 吉祥物图。"
policy:
  allow_implicit_invocation: true
```

- [ ] **Step 3: Verify metadata**

Run:

```bash
rg -n "ian-xiaohei|小黑|Xiaohei|怪诞|不卖萌|不要可爱" nexus-cat-mascot/SKILL.md nexus-cat-mascot/agents/openai.yaml
```

Expected: no matches.

- [ ] **Step 4: Commit Skill metadata**

Run:

```bash
git add nexus-cat-mascot/SKILL.md nexus-cat-mascot/agents/openai.yaml
git commit -m "feat: define nexus cat mascot skill metadata"
```

Expected: commit succeeds.

### Task 4: Rewrite Reference Documents

**Files:**
- Modify: `nexus-cat-mascot/references/nexus-cat-ip.md`
- Modify: `nexus-cat-mascot/references/style-dna.md`
- Modify: `nexus-cat-mascot/references/composition-patterns.md`
- Modify: `nexus-cat-mascot/references/prompt-template.md`
- Modify: `nexus-cat-mascot/references/qa-checklist.md`

- [ ] **Step 1: Replace `references/nexus-cat-ip.md`**

Use this content:

````markdown
# Nexus Cat IP

## 角色定义

Nexus Cat 是这个 Skill 的固定视觉 IP。

每张图都应该出现同一只 Nexus Cat。它不是随机猫咪，也不是每次重新设计的新角色，而是一个稳定的 kawaii developer assistant mascot。

## 固定外形

- 灰白毛色。
- 圆胖身体。
- 大圆眼。
- 脸颊腮红。
- 简单黑色描边。
- 最少阴影。
- 穿 hoodie。
- hoodie 胸口有 `</>` 符号。
- 整体轮廓圆润、友好、容易识别。

## 性格

- 友好。
- 可靠。
- 像开发者助手和产品向导。
- 有一点可爱和笨拙，但不幼稚。
- 主动帮读者理解、修复、检查、指路或完成任务。

## 常见职责

让 Nexus Cat 承担核心动作：

- 挥手欢迎。
- 指向下一步。
- 举提示牌。
- 拿着代码片段。
- 抱着 bug 图标。
- 坐在终端旁边。
- 推送完成的 checklist。
- 看 dashboard。
- 给文档贴标签。
- 帮用户连接两个步骤。
- 在多 panel 里依次演示流程。

## 禁止漂移

- 不要改变物种。
- 不要改变灰白毛色。
- 不要去掉 hoodie。
- 不要去掉 `</>` 符号。
- 不要把身体画瘦或画成长腿成人比例。
- 不要把眼睛改成写实猫眼。
- 不要变成真实摄影、3D 厚渲染或复杂商业插画。
- 不要在一组图里让 Nexus Cat 看起来像多只不同角色。

## 判断标准

如果把多张图放在一起，读者应该能立刻判断它们是同一只 Nexus Cat。动作可以变，场景可以变，角色识别度不能变。
````

- [ ] **Step 2: Replace `references/style-dna.md`**

Use this content:

````markdown
# 风格 DNA

## 一句话

干净、可爱、圆润、友好、稳定、一致、开发者助手感。

像一只长期陪用户写代码、看文档、修 bug、解释产品流程的 kawaii mascot。

## 必须

- Nexus Cat 是画面主角。
- 同一组图里角色设计必须一致。
- 灰白毛色、圆胖身体、大圆眼、腮红、黑色描边、最少阴影。
- hoodie 胸口有 `</>`。
- 背景干净，可以是白底、透明背景或极简浅色场景。
- 道具少而明确，服务当前动作。
- 画面友好、清晰、轻松。

## 颜色

- 灰白：Nexus Cat 毛色。
- 深蓝或深灰蓝：hoodie 主色。
- 黑色：简单描边、眼睛、少量文字。
- 粉红或浅红：腮红、轻微情绪点。
- 橙色或蓝色：少量辅助道具、箭头、提示、状态。

颜色要稳定，避免每张图换一套主视觉。

## 文字

- 默认不需要大量文字。
- 允许短标签、按钮词、提示牌或极短中文标注。
- 避免大段解释文字。
- hoodie 上必须优先保持 `</>`。

## 不要

- 不要真实猫摄影。
- 不要复杂 3D。
- 不要厚重阴影。
- 不要暗黑、恐怖、赛博朋克或脏乱背景。
- 不要正式 PPT 信息图。
- 不要密集流程图。
- 不要每张图都生成不同猫。
- 不要把 Nexus Cat 缩成角落装饰。

## 审美方向

要可爱但不低幼，专业但不冷硬，像开发者工具和 AI 产品可以长期使用的友好 mascot。
````

- [ ] **Step 3: Replace `references/composition-patterns.md`**

Use this content:

````markdown
# 场景与 Panel 模式

## 基础场景类型

### Greeting

适合：欢迎页、开场图、产品入口、教程开头。

画法：Nexus Cat 正面或 3/4 视角挥手，旁边只有一个小道具或短提示。

### Guide

适合：步骤说明、使用引导、文档导航。

画法：Nexus Cat 指向箭头、按钮、路标、下一步卡片或小地图。

### Debugging Helper

适合：bug 修复、错误解释、开发工具主题。

画法：Nexus Cat 抱着 bug 图标、看终端、递交修复补丁或贴上 check mark。

### Workflow Companion

适合：AI 工作流、自动化、内容流程、开发流程。

画法：Nexus Cat 在 2-4 个轻量步骤之间移动，动作连接流程，但不要变成密集流程图。

### Reaction

适合：状态反馈、成功、失败、提醒、等待。

画法：Nexus Cat 用表情和小道具表达状态，例如开心举牌、困惑看日志、庆祝通过测试。

### Tutorial Panel

适合：多步骤教程、before/after、连续说明。

画法：2-4 个 panel，每格同一只 Nexus Cat 做一个动作。每格保持同样的毛色、hoodie、体型和脸部特征。

### Product Companion

适合：SaaS、AI 工具、开发者产品、文档页配图。

画法：Nexus Cat 和简化 UI 卡片、terminal、dashboard、文档页同框。UI 只做道具，不画真实 App 截图。

## 多图一致性规则

同一组图需要重复这些描述：

- same consistent Nexus Cat character
- chubby gray-and-white cat
- big round eyes
- blush cheeks
- simple black outlines
- minimal shading
- dark hoodie with `</>` symbol
- same character design repeated across all panels

## 道具池

- terminal window
- code snippet card
- bug icon
- checklist
- tiny dashboard
- document page
- arrow sign
- small map
- progress bar
- notification badge
- wrench
- coffee mug
- laptop

每张图选 1-3 个道具即可。

## 反漂移规则

如果一组图里 Nexus Cat 的脸型、毛色、衣服、眼睛或体型明显变了，优先重生成并减少场景复杂度。角色一致性比道具丰富度更重要。
````

- [ ] **Step 4: Replace `references/prompt-template.md`**

Use this content:

````markdown
# 生图提示词模板

每张图单独生成。根据用户主题替换变量，不要默认把多张图拼在一起。

```text
Generate one standalone kawaii mascot illustration.

Fixed character:
Nexus Cat, the same consistent friendly developer-assistant mascot character. A chubby round gray-and-white cat with big round eyes, blush cheeks, simple black outlines, minimal shading, wearing a dark hoodie with a clear `</>` symbol on the chest. Keep the same character design, fur pattern, face, body shape, hoodie, and overall silhouette.

Role:
Nexus Cat acts as a friendly guide and assistant.

Theme:
{主题}

Scene:
{具体场景}

Action:
{Nexus Cat 正在做什么}

Expression:
{表情：friendly / focused / happy / curious / relieved / gently confused}

Props:
{道具1} / {道具2} / {道具3}

Background:
Clean white or transparent background, or a very simple light scene. No clutter.

Optional labels:
{可选短标签，默认少字或无字}

Style:
Kawaii, rounded, clean, approachable, simple black outline, minimal shading, soft colors, developer-tool companion feel.

Constraints:
Do not change Nexus Cat into another character. Do not change the gray-and-white fur, chubby body, big round eyes, blush cheeks, hoodie, or `</>` symbol. Do not make it realistic, dark, gritty, heavily shaded, 3D-rendered, or overly complex. Do not create a dense infographic or formal flowchart. If this is multi-panel, repeat the same character design across all panels.
```

## 多 panel 模板

```text
Generate one clean multi-panel kawaii mascot illustration with {panel_count} panels.

Use the same Nexus Cat character in every panel: chubby round gray-and-white cat, big round eyes, blush cheeks, simple black outlines, minimal shading, dark hoodie with `</>` symbol. The character design must remain identical across panels.

Panel 1:
{panel_1_action}

Panel 2:
{panel_2_action}

Panel 3:
{panel_3_action}

Keep each panel simple, friendly, and uncluttered. Use only short optional labels. Do not make the panels look like different cats.
```

## 图像编辑提示

修复角色漂移：

```text
Edit or regenerate this image so the character matches Nexus Cat exactly: chubby gray-and-white cat, big round eyes, blush cheeks, simple black outlines, minimal shading, dark hoodie with a clear `</>` symbol. Preserve the original scene idea, but make the mascot consistent with the fixed Nexus Cat design.
```

修复 hoodie 符号：

```text
Edit the image so the hoodie chest symbol is clearly `</>`. Preserve the same Nexus Cat character, pose, background, and composition. Do not add extra text.
```
````

- [ ] **Step 5: Replace `references/qa-checklist.md`**

Use this content:

````markdown
# QA Checklist

## 必过项

- 有 Nexus Cat。
- Nexus Cat 是主角或核心助手，不是角落装饰。
- 灰白毛色清楚。
- 身体圆胖。
- 眼睛大而圆。
- 有腮红。
- 有简单黑色描边。
- 阴影很少。
- 穿 hoodie。
- hoodie 胸口有 `</>`。
- 气质友好、可爱、像助手或向导。
- 如果是多张图或多 panel，角色设计保持一致。
- 背景干净，不喧宾夺主。

## 失败信号

出现以下情况，重生成或局部编辑：

- Nexus Cat 变成别的猫、别的动物或人形角色。
- 毛色不是灰白。
- hoodie 丢失。
- `</>` 符号丢失或变成乱码。
- 身体变瘦、变写实或比例不稳定。
- 多张图里像不同角色。
- 画面过暗、过复杂、过写实、过 3D。
- 变成正式流程图或密集信息图。
- 文字太多，盖过角色。

## 迭代方法

- 角色不一致：减少场景和道具，重复固定角色描述。
- hoodie 符号错误：局部编辑 hoodie 胸口，只修 `</>`。
- 太复杂：删背景和文字，只保留 Nexus Cat、一个动作、1-2 个道具。
- 太写实：强调 kawaii mascot, simple black outlines, minimal shading。
- 太像普通贴纸：加强 friendly guide and assistant 的动作，例如指路、递交、检查、解释。

## 交付判断

高质量图应该让读者一眼认出：这是同一只 Nexus Cat，正在友好地帮我完成当前任务。
````

- [ ] **Step 6: Verify references**

Run:

```bash
rg -n "小黑|Xiaohei|xiaohei|怪诞|不卖萌|不要可爱|deadpan|black solid" nexus-cat-mascot/references
```

Expected: no matches.

- [ ] **Step 7: Commit references**

Run:

```bash
git add nexus-cat-mascot/references
git commit -m "feat: rewrite nexus cat reference rules"
```

Expected: commit succeeds.

### Task 5: Rewrite Example Prompts

**Files:**
- Modify: `examples/prompts.md`

- [ ] **Step 1: Replace `examples/prompts.md`**

Use this content:

````markdown
# Prompt Examples

下面这些 prompt 可以直接复制到 Codex 里使用。

## 只做 shot list

```text
Use $nexus-cat-mascot 先不要生图。
请为下面这篇产品教程设计 5 张 Nexus Cat 吉祥物配图。
每张写清楚：
- 用途
- 场景
- Nexus Cat 动作
- 表情
- 道具
- 背景复杂度
- 可选文字标注

<粘贴文章>
```

## 文章或教程配图

```text
Use $nexus-cat-mascot 把下面这篇教程生成 4 张 Nexus Cat 吉祥物配图。
要求同一只 Nexus Cat 在每张图里保持一致：灰白猫、圆胖身体、大圆眼、腮红、简单黑色描边、最少阴影、深色 hoodie、胸口 `</>`。

<粘贴文章>
```

## 单个场景

```text
Use $nexus-cat-mascot 为这个场景生成一张图：

Nexus Cat 坐在终端旁边，认真看一条红色错误日志，一只爪子拿着小扳手。

风格：kawaii、干净白底、简单黑描边、最少阴影、友好开发者助手。
```

## Bug 修复主题

```text
Use $nexus-cat-mascot 生成 3 张同角色图片，主题是“AI 助手帮开发者修 bug”。
三张分别是：
1. Nexus Cat 发现 bug
2. Nexus Cat 递交补丁
3. Nexus Cat 举起通过测试的 checklist

每张都必须是同一只灰白 Nexus Cat，穿带 `</>` 的 hoodie。
```

## 多 panel 教程图

```text
Use $nexus-cat-mascot 生成一张 3-panel 教程图：
Panel 1: Nexus Cat 读取需求
Panel 2: Nexus Cat 写代码
Panel 3: Nexus Cat 提交结果

所有 panel 都必须保持同一只 Nexus Cat：灰白毛色、圆胖身体、大圆眼、腮红、深色 hoodie、胸口 `</>`。
```

## 产品文档陪伴图

```text
Use $nexus-cat-mascot 为“新用户完成第一次配置”生成一张文档配图。
Nexus Cat 站在简化的设置卡片旁边，指向一个绿色 check mark。
背景干净，不要真实 UI 截图，不要复杂流程图。
```

## 改图：修复角色一致性

```text
Use $nexus-cat-mascot 这张图方向对，但角色不像固定 Nexus Cat。
请保持场景含义不变，重生成一版：
灰白猫、圆胖身体、大圆眼、腮红、简单黑描边、最少阴影、深色 hoodie、胸口 `</>`。
```

## 改图：修复 hoodie 符号

```text
Use $nexus-cat-mascot 帮我编辑这张图。
只修复 hoodie 胸口符号，让它清楚显示为 `</>`。
其他角色、动作、背景和构图保持不变。
```
````

- [ ] **Step 2: Verify examples use new Skill**

Run:

```bash
rg -n "ian-xiaohei|小黑|Xiaohei|xiaohei|怪诞|不卖萌|不要可爱" examples/prompts.md
```

Expected: no matches.

- [ ] **Step 3: Commit examples**

Run:

```bash
git add examples/prompts.md
git commit -m "docs: update examples for nexus cat mascot"
```

Expected: commit succeeds.

### Task 6: Final Verification And Cleanup

**Files:**
- Inspect: `README.md`
- Inspect: `examples/prompts.md`
- Inspect: `nexus-cat-mascot/SKILL.md`
- Inspect: `nexus-cat-mascot/agents/openai.yaml`
- Inspect: `nexus-cat-mascot/references/*.md`
- Inspect: `.gitignore`

- [ ] **Step 1: Run old-name scan**

Run:

```bash
rg -n "小黑|Xiaohei|xiaohei|Ian Xiaohei|ian-xiaohei" README.md examples/prompts.md nexus-cat-mascot
```

Expected: the only acceptable match is the GitHub repository URL in `README.md` if the repository has not been renamed externally yet. No Skill name, prose positioning, prompt, reference, or agent manifest should use the old IP.

- [ ] **Step 2: Run old-style scan**

Run:

```bash
rg -n "怪诞|不卖萌|不要可爱|deadpan|black solid|absurd worker|正文结构解释图|小黑怪诞" README.md examples/prompts.md nexus-cat-mascot
```

Expected: no matches.

- [ ] **Step 3: Confirm README does not display old images**

Run:

```bash
rg -n "examples/images|assets/examples|01-two-breakpoints|trust-bridge|information-well" README.md
```

Expected: no matches.

- [ ] **Step 4: Confirm new required names**

Run:

```bash
rg -n "nexus-cat-mascot|Nexus Cat|</>" README.md examples/prompts.md nexus-cat-mascot/SKILL.md nexus-cat-mascot/agents/openai.yaml nexus-cat-mascot/references
```

Expected: multiple matches across README, examples, Skill metadata, agent manifest, and references.

- [ ] **Step 5: Check git status**

Run:

```bash
git status --short
```

Expected: clean working tree after all task commits. If files remain modified, inspect them and commit only intentional project changes.

- [ ] **Step 6: Final report**

Report:

```text
完成：项目已重构为 nexus-cat-mascot。
验证：旧 IP/旧风格扫描通过；README 不再展示旧小黑图片；Skill name、安装路径、示例 prompt 和 reference 文件一致。
保留：旧图片资产仍在仓库中，但不作为 README 展示或默认视觉校准。
```
