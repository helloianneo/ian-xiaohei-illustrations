---
name: technical-lineart-illustrations
description: 生成 Black-and-White Technical Line Art 风格的中文正文配图。用于技术/产品/流程类内容的清晰黑白线描插画。
---

# Black-and-White Technical Line Art Skill (风格分支)

## 核心定位

为中文技术文章生成 16:9 横版的黑白技术线描插图。本 Skill 强调信息传达与结构化表达：把文章里的判断、流程、组件关系或隐喻转换为清晰、可读的黑白技术线描图。

默认视觉风格为 Black-and-White Technical Line Art：纯白背景、黑色线描、结构化符号与简洁示意元素。本分支支持将原有“小黑”风格替换为技术线描示意元素，或同时保留为可选视觉 IP。

## 先读这些参考

- `references/technical-lineart.md`：风格规范、线条与注记规则。
- `references/style-dna.md`：风格 DNA 与导出约束。
- `references/composition-patterns.md`：构图类型与示例模板。
- `references/prompt-template.md`：单张生图提示词模板（已适配 technical-lineart）。
- `references/qa-checklist.md`：生成后检查与迭代规则（保留核心 QA 要点）。

## 工作流（保持原有流程）

1. 消化正文并提炼认知锚点。
2. 输出 shot list（优先核心判断、前后对比、输入输出闭环、承接路径等）。
3. 单张生成：每张图只讲一个核心结构或动作；提示词必须包含：16:9、纯白背景、黑色技术线描、简洁中文注记（可选）。
4. 检查并迭代：参照 `references/qa-checklist.md`。
5. 保存交付到 `assets/<article-slug>-illustrations/`。

## 单张生成约束（示例）

- 16:9 横版 PNG，纯白背景；
- 黑色技术线描（#000000），线条清晰但保留轻微手绘抖动；
- 禁止渐变、阴影、丰富颜色填充；默认不使用彩色注记；
- 每张图只表达一个核心动作/结构；主角或示意元素必须承担核心动作或说明；
- 中文注记尽量精简（每张最多 5 处短词）。

## 输出口径

- 生成后报告包含：生成张数、用途、保存路径、稳妥与可选版本说明。

