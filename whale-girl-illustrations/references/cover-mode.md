# 鲸鱼娘小红书封面模式

只在用户要求封面、首图或小红书系列第一页时读取。封面负责让人停下来点开，不负责讲完整项目。

## 封面先回答一个问题

生成前先用一句话回答：读者在手机信息流里半秒内最先看见什么？

答案必须是当前内容最有吸引力的一个痛点、结果、结论、反差或数字，不是“项目介绍”“功能说明”这类栏目名。不得承诺正文没有提供的结果，不使用虚假夸张词。

项目名、工具名或 Skill 名不等于点击理由。它们可以作为小标签保留，但最大标题要告诉读者“看完能得到什么”或“为什么现在值得点开”。

## 文字层级

- 主标题优先使用 6–12 个中文字；英文项目名、Skill 名或仓库名默认只作为小标签，不作为最大标题。
- 主标题优先断成 1–2 行大字，每行约占安全区宽度的 80%–95%。
- 只允许一句极短副标题或一个 2–8 字小标签；没有必要就不加。
- 不放功能列表、适合人群、配置要求、Stars/Forks、完整项目名解释和多段正文。
- 只强调一个关键词：红橙色文字、淡蓝底刷、局部放大或更粗字重四选一，不叠加多种效果。
- 默认使用自然的左对齐或轻微错位排布，避免“中文一行＋巨大英文一行＋副标题一行”的三层居中堆叠。英文不能比中文标题更大、更红或更抢眼。

## 手写标题字形

- 主标题像粗头马克笔或毛毡笔手写，笔画有轻微粗细变化，字面饱满但不完全等宽，基线略有起伏。
- 转折、收笔和字间距自然，不做光滑矢量边缘、标准几何黑体或无衬线印刷字。
- 手写感不能牺牲可读性：不使用狂草、毛笔书法大字、儿童涂鸦或过度抖动的线条。
- 中英文必须属于同一手绘语言；若英文只是项目名或 Skill 名，缩小为标签，不与中文争夺主视觉。

## 构图

- 严格 3:4 竖版。
- 标题区位于画面上方约 10%–42%，整体可占画面约 28%–40%。标题周围保留明显安静留白，不能紧贴边框、角色、气泡或正文。
- 默认稳定构图为“上方或左上 1–2 行中文利益标题＋下方或右下角色动作”。标题和角色形成一条简单的竖向或对角动线，不用随机气泡填满留白。
- 鲸鱼娘通常放在下方或侧下方，占画面约 30%–45%，做一个与标题直接相关的动作，并与一个主要物件或视觉隐喻互动。
- 画面只保留一个主视觉锚点。可以有 0–2 个承担反馈或陪伴作用的小鲸鱼，不用信息卡片填满空白。
- 延续浅暖白纸感、深蓝手绘外围框线、淡蓝底纹、少量气泡和克制红橙重点，使封面与后续信息页属于同一系列。

## 封面提示词模板

```text
Generate one standalone strict 3:4 vertical Chinese Xiaohongshu cover illustration.

Use the supplied whale-girl reference image as the identity reference. Preserve her refined chibi face, blue eyes, navy-to-blue long hair, white lace maid headband, side blue bow, whale-fin ears, navy-and-white maid dress, white apron and blue whale tail. She must perform one action connected to the topic.

Visual DNA:
Very pale warm-white paper background, almost white. Deep navy slightly wobbly hand-drawn outer frame. Pale blue brush marks, sparse bubbles and doodles, and only one red/orange emphasis. Refined hand-drawn Xiaohongshu cover, not a commercial poster or information-card page.

Half-second subject:
{读者半秒内最先看见的痛点、结果、结论、反差或数字}

Main title, render verbatim:
{6–12 个中文字表达用户收益、痛点、结果或反差，断成 1–2 行}

Optional subtitle or project label, render verbatim:
{只允许一项：一句极短副标题，或项目名、Skill 名、英文仓库名小标签；不需要则删除本段。它必须明显小于中文主标题}

Title hierarchy:
The Chinese benefit-led main title is the first visual anchor. Place it in the upper 10%-42% of the canvas, using about 28%-40% of the full canvas. Use one or two large lines that fill roughly 80%-95% of the safe width. Prefer left alignment or a slight handmade offset instead of three centered stacked text bands. Keep obvious quiet space around the title. Emphasize only the exact keyword "{关键词}" using {red-orange text / pale-blue brush backing / larger size / heavier weight}; keep the rest deep navy. Any English project name or the word Skill must remain a small secondary label and must never become larger, redder or more prominent than the Chinese title.

Handwritten typography:
Render all Chinese text as clearly readable thick felt-tip-marker handwriting with slightly varied stroke width, a subtly uneven baseline, natural rounded stroke endings and non-mechanical spacing. Keep headings and subtitle in the same hand-drawn family. Avoid geometric bold sans-serif, clean digital typesetting, perfectly straight baselines, smooth vector lettering, formal calligraphy and childish scribbles.

Visual anchor:
{鲸鱼娘正在做什么、主要物件或隐喻是什么}

Composition:
Keep the whale-girl in the lower or lower-side area, about 30%-45% of the canvas. Use one main visual object and at most two purposeful small whales. Let the title and character form one clear diagonal or vertical reading path.

Avoid:
Information sections, feature lists, GitHub metrics, configuration text, dense body copy, multiple cards, dashboard, giant empty character poster, tiny title, crowded title zone, generic product-name headline, giant red English word, three centered stacked title bands, geometric sans-serif or clean digital type, random decorative bubbles filling empty space, more than one emphasized keyword, watermark, signature, QR code, repeated whale logos, "by ian and 小黑".
```

## 封面失败信号

- 缩小后先看到角色或装饰，读不到标题。
- 标题和正文一样大，或者标题只是顶部的一条栏目名。
- 标题下面紧贴英文项目名、解释句和第一块正文，没有留白。
- 最大标题只是项目名或“某某 Skill”，没有用户收益、痛点、结果或反差。
- 中文像标准黑体，英文像光滑海报字体，或巨大英文词抢走中文标题焦点。
- 三层文字全部居中堆叠，留白被随机气泡填满，整体像通用产品海报。
- 把信息页的功能、数据、适合人群全部塞进封面。
- 同时使用红字、描边、渐变、多个底刷和感叹号，重点互相争抢。
