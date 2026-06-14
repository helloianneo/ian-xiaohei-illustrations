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
