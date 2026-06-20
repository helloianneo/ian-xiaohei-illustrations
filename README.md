# Ian Xiaohei Illustrations

> 把中文文章里的判断、流程、状态和隐喻，变成一张张白底、手绘、怪诞但清爽的正文配图。
>
> 16:9 横版 | 自定义 IP（猫 / 鸭 / 合体）| 纯白手绘 | 少量红橙蓝中文批注 | Codex Skill

---

## 这个仓库是什么

Ian Xiaohei Illustrations 是一个 Codex Skill，用来指导 AI Agent 为中文文章、帖子、博客、Notion 文档和方法论内容生成正文配图。

它不是通用插画 prompt，也不是 PPT 信息图模板。它的核心目标是：先理解文章里的认知锚点，再把其中一个判断、流程、结构、状态或隐喻，变成一张有记忆点的 16:9 手绘解释图。

默认视觉 IP（已替换）
- 本仓库默认视觉 IP 已由原先的“小黑”替换为用户自定义 IP：图1（猫）、图2（鸭）、图3/4（猫+鸭 合体/场景）。在使用时可在 prompt 中指定 {IP=cat}、{IP=duck} 或 {IP=fusion}。  
- 一句话：让 AI 不只是“配一张图”，而是把文章里的一个关键认知动作交给猫/鸭/合体来做。

---

## 适合谁用

特别适合：

- 写中文文章，需要正文配图和文章插图的人
- 做知识型内容、方法论内容、AI 工作流内容的人
- 想把抽象判断画成具体隐喻的人
- 想要一种比 PPT 信息图更轻、更怪、更有个人识别度的配图风格的人
- 用 Codex 做内容生产，希望稳定复用一套视觉语言的人

不适合：

- 想要商业插画、品牌 KV 或精致扁平插画的人
- 想要传统 PPT 信息图、复杂架构图或流程图的人
- 想要儿童卡通、可爱 IP、表情包风格的人
- 想把大量正文、长段解释或完整课程页塞进一张图里的人
- 需要严格可编辑矢量源文件的人

---

## 它会产出什么

默认输出：

- 16:9 横版正文配图
- 一篇文章的 4-8 张 shot list
- 每张图的主题、核心意思、结构类型、IP 在图中的动作和中文标注建议
- 最终 PNG 图片，保存到 workspace 的 `assets/<article-slug>-illustrations/`

默认不输出：

- PPTX / PDF / Keynote
- SVG / HTML / Canvas 可编辑图
- 商业海报或封面 KV
- 大段文字型信息图

---

## 视觉风格（以你的 IP 为核心）

- 纯白背景，不要纸纹、米色、阴影、渐变
- 黑色手绘线稿，细线，轻微抖动
- 大量留白，主体只占画面约 40%-60%
- 少量红色、橙色、蓝色中文手写批注
- 每张图只表达一个核心动作、结构、状态或隐喻
- IP（猫 / 鸭 / 合体）必须参与核心动作，不能只是装饰
- 怪诞、有创意、清爽，但不幼稚、不卖萌

---

## 示例效果（保持原 examples 可参考）
（images/... 保持示例图片不变，但示例说明中默认角色从小黑更换为猫/鸭）

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
cp -R ./ian-xiaohei-illustrations "${CODEX_HOME:-$HOME/.codex}/skills/"
```

安装后，在 Codex 里使用（示例）：

```text
Use $ian-xiaohei-illustrations 为这篇中文文章设计并生成 5 张配图，默认角色改为 {IP=cat}。
```

---

## 怎么用（示例 prompts）
### 只做配图规划

```text
Use $ian-xiaohei-illustrations 先不要生图。
请分析下面这篇文章哪里值得配图，输出 5 张左右的 shot list。
每张图写清楚：放在哪段后、主题、核心意思、结构类型、IP 在图里做什么、建议中文标注词。

<粘贴文章>
```

### 直接生成正文配图

```text
Use $ian-xiaohei-illustrations 把下面这篇文章生成 4 张正文配图。
要求：16:9 横版、纯白背景、黑色手绘线稿、少量黄色/粉/蓝中文手写批注。
默认角色：{IP=duck}
```

### 为单个概念生成一张图

```text
Use $ian-xiaohei-illustrations 为“信任不是喊出来的，而是一块证据一块证据铺过去”生成一张正文配图。
画面要怪诞但清爽，角色必须承担核心动作（指定 {IP=cat}）。
```

### 去掉图里的标题或错误文字

```text
Use $ian-xiaohei-illustrations 帮我编辑这张图，去掉左上角的“流程图”标题，其他内容保持不变。
```

---

## 工作流程（简要）
1. 读取文章 / Markdown / Notion 内容 / 截图或用户给的主题
2. 提炼核心观点、认知转折、流程结构和适合视觉化的段落
3. 输出 shot list：每张图只选一个认知锚点
4. 选择结构类型：Workflow、系统局部、前后对比等
5. 发明新的低科技、怪诞但成立的物理隐喻
6. 指定角色（{IP=cat|duck|fusion}）承担核心动作
7. 单张调用图像模型生成，并按 QA 检查（线条、留白、角色参与感）
8. 保存最终 PNG，并报告用途和路径

---

## 注意事项（与 IP 替换相关）
- 图片里的中文文字越短越稳定。
- 每张图只讲一个核心结构，不要把文章做成说明书。
- 角色必须承担核心动作；如果去掉角色仍然完全成立，说明角色太装饰了。
- 示例图只用于校准线条密度、留白、颜色克制和角色参与方式，不要复刻构图。
- AI 图像模型可能出现错字、幻觉标签、风格漂移或多余标题，生成后需要检查。
- 若中文错字严重，优先减少标注词并重生成。

---

## 相关项目

- [Ian Handdrawn PPT](https://github.com/helloianneo/ian-handdrawn-ppt) — 中文手绘技术 PPT-style 页面图生成 Skill
- [Awesome Claude Code Skills](https://github.com/helloianneo/awesome-claude-code-skills) — Claude Code Skills / Agents / Plugins 精选合集
- [Obsidian + Claude AI Second Brain](https://github.com/helloianneo/obsidian-ai-second-brain) — Obsidian + Claude AI 个人知识库搭建指南

---

## 关于作者

**Ian (伊恩)** — 产品设计师 / 一人公司实践者 / AI Builder

用 AI 团队打造一人公司。

- GitHub: [helloianneo](https://github.com/helloianneo)
- X/Twitter: [@ianneo_ai](https://x.com/ianneo_ai)
- 网站: [www.ianneo.xyz](https://www.ianneo.xyz)
- 微信: `ianneoxyz`
- 邮箱: hello.neoc@gmail.com

---

## 继续探索

这套小黑配图 Skill，只是我用 AI 搭建个人生产系统里的一个小工具。

如果你也在用 AI 做内容、知识库、工作流或产品化，可以继续看我的网站：[www.ianneo.xyz](https://www.ianneo.xyz)。

只想先观察，可以关注我的 [X/Twitter](https://x.com/ianneo_ai)。

想了解 Indie Builders Club，加微信：`ianneoxyz`，备注「OPC」。

<p>
  <img src="assets/ian-wechat-qr.jpg" alt="Ian 微信二维码" width="120">
</p>

不方便扫码也可以搜索微信：`ianneoxyz`。

---

## License

MIT License. See [LICENSE](LICENSE).
