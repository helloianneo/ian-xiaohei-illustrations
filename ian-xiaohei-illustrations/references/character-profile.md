# 自定义角色 Profile

当用户想用自己的形象做正文配图时，先把描述、头像、照片、logo 或品牌角色整理成一个简短角色卡。角色卡用于整篇文章的所有图片，避免每张图的人物都漂移。

## 用户输入

如果用户没有提供角色信息，但明确要求自定义形象，只问一次：

```text
请用一句话描述你想放进配图里的个人形象，例如：黑色卫衣、圆眼镜、拿小电脑、冷静的独立开发者。也可以说“用默认小黑”。
```

如果用户上传图片，从图片里提炼 3-6 个稳定、可手绘复现的特征。不要追求真实肖像复刻。

## 角色卡模板

```text
name:
source:
appearance:
personality:
core_actions:
signature_props:
constraints:
prompt_phrase:
```

## 字段说明

- `name`：角色名。用户没给时用“个人角色”。
- `source`：来自文字描述、头像、照片、插画、logo、品牌角色或默认小黑。
- `appearance`：3-6 个稳定外形特征，避免细碎五官。
- `personality`：角色气质，服务画面表达。
- `core_actions`：适合这个角色反复做的动作。
- `signature_props`：0-3 个识别道具。
- `constraints`：明确不要画成什么。
- `prompt_phrase`：可直接放进生图提示词的一段英文描述。

## 提炼规则

优先保留：

- 轮廓：圆、瘦长、方、豆状、头发形状、眼镜、帽子、衣服大轮廓。
- 识别物：背包、围巾、耳机、电脑、笔、相机、工具。
- 气质：冷静、认真、松弛、怪诞、观察者、工程师感、创作者感。
- 动作倾向：搬运、拉线、分拣、记录、修补、开门、压缩、搭桥。

避免：

- 真实身份隐私。
- 过细的五官、肤质和肖像相似度。
- 复杂服装、复杂道具、商业插画细节。
- 可爱吉祥物、儿童卡通、超级英雄化。

## 示例

用户描述：

```text
黑色卫衣、圆眼镜、拿小电脑、冷静的独立开发者。
```

角色卡：

```text
name: 独立开发者角色
source: user description
appearance: simple hand-drawn human-like character, black hoodie, small round glasses, calm blank face, tiny laptop
personality: quiet product-builder energy, serious, deadpan, slightly absurd
core_actions: connect, sort, debug, carry, label, open doors, repair machines
signature_props: tiny laptop
constraints: not cute, not superhero, not realistic portrait, no detailed facial likeness, no glossy tech UI
prompt_phrase: a simple hand-drawn human-like character in a black hoodie with small round glasses, calm blank face, holding a tiny laptop, serious deadpan product-builder energy
```

## 使用标准

角色必须承担核心动作。如果去掉角色，图的核心隐喻仍然完全成立，说明角色太装饰了；要重写提示词。
