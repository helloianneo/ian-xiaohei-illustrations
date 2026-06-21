# Ian Xiaohei Illustrations — Cat / Duck IP variant

简介
此仓库是用于生成“正文配图”的 Skill。该分支将默认视觉 IP 从“小黑”替换为用户自定义的 Cat / Duck / Cat+Duck Duo。文档、prompt 模板与 QA 已更新以保证 IP 的视觉一致性。

如何使用（快速）
- 克隆仓库并把子目录复制到你的 Codex Skills 目录（示例不变）。  
- 在使用 prompt 时明确指定 IP，例如： Use $ian-xiaohei-illustrations 把下面这篇文章生成 4 张正文配图。默认角色：{IP=duck}

重要说明（迁移）
- 本次变更是文档与模板级别的替换；示例图片保持参考用。若你在旧工作流程里依赖“小黑”请用 {IP=cat|duck|fusion} 变量迁移 prompt。

更多
- 查看 references/ 中的 style-dna.md、xiaohei-ip.md（现定义为 Cat/Duck IP）、prompt-template.md、qa-checklist.md 获取详细规范与可复制 prompt。
