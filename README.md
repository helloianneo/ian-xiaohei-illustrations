# Black-and-White Technical Line Art Illustrations

> 将技术内容（流程、架构、判断、隐喻）转为黑白技术线描插画，适用于技术文档、产品文档、博客与方法论文章的正文配图。
>
> 16:9 横版 | 纯白背景 | 黑色技术线描 | 强调结构与动作 | Codex Skill（风格分支）

---

## 特色示例（用户提供）

下面的示例使用了用户上传的 Black-and-White 线描图（存放于 examples/images/）。

![Featured technical line art](examples/images/Gemini_Generated_Image_e5wl1re5wl1re5wl.png)

---

## 这个仓库是什么

本仓库是对原有 Ian Xiaohei Illustrations 的风格分支，目标是支持 "Black-and-White Technical Line Art" 风格的正文配图生成。它为 Codex Skill 提供风格规范、示例、提示模板与可复用资产，帮助 AI Agent 将文章中的判断、流程、结构或隐喻可视化为清晰的黑白技术线描插画。

该分支关注点：

- 纯白背景，黑色线条为主，线条清晰且保留少量手绘抖动感以维持人手绘质感；
- 强调技术感与信息传达（适合架构、工作流、系统说明类内容）；
- 每张图只表达一个核心认知动作或结构，避免变成说明书式的信息密集图；
- 插画中应包含主角或示意元素来承担核心动作（技术示意符号、人物轮廓或设备原型均可）；

---

## 输出内容

默认输出：

- 16:9 横版 PNG 插画（黑白技术线描）
- 一篇文章的 4-8 张 shot list（由 Agent 提供）
- 每张图的主题说明、核心意思、结构类型与简短中文标注建议
- 最终 PNG 图片保存路径： `assets/<article-slug>-illustrations/`

默认不输出：

- PPTX / PDF / Keynote 源文件
- 可编辑矢量源（如 AI / SVG 作为交付）
- 彩色商业海报或复杂信息图

---

## 使用示例与安装

克隆仓库并使用：

```bash
git clone https://github.com/Yukiki0219/ian-xiaohei-illustrations.git
cd ian-xiaohei-illustrations
```

在 Codex 中使用示例：

```text
Use $ian-xiaohei-illustrations 以 Black-and-White Technical Line Art 风格为这篇文章生成 4 张插图。
要求：16:9 横版、纯白背景、黑色技术线描、简短中文注记（如需）。
```

更多示例请查看 `examples/images/`。

---

## License

MIT License. See [LICENSE](LICENSE).
