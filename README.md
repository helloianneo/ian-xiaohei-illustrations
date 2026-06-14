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
