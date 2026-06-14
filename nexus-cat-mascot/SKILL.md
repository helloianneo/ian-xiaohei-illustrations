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
