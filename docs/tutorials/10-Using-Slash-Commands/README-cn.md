# 使用斜杠命令

> 学习如何通过斜杠命令和技能快速执行预构建的提示模板，无需每次都输入冗长的指令。

## 为什么要学这个

想象一下：你正在使用 Gemini CLI，需要做一次货币换算。你清楚地知道想让 Gemini 做什么，但指令很详细——要指定汇率、格式规则、计算步骤。

你可以每次都完整输入这些内容。或者，你可以只输入一次，保存为命令，以后只需一行就能调用。

这就是斜杠命令的作用。它们把复杂的、多段落的提示变成简单的一行快捷方式。就好比每次都从头给人指路，和保存地址后直接说"带我去那里"的区别。

---

## 什么是斜杠命令？

斜杠命令就是一个**提示模板的快捷方式**。它能帮你快速注入预写好的提示，无需手动输入。

它是这样工作的：

1. 斜杠命令包含一个**提示模板**——给 Gemini 的详细指令
2. 你在 Gemini CLI 中输入 `/command-name arguments`
3. Gemini 自动加载提示并处理你的参数

**重要提示：** 你不需要记住斜杠命令的名字。当你输入 `/` 并开始打字时，Gemini CLI 会显示可用命令的列表。

---

## Gemini CLI 的双重系统：命令 + 技能

Gemini CLI 有两种方式来创建可复用的提示：

### 命令（`.gemini/commands/*.toml`）

命令是定义斜杠命令的 TOML 文件。它们使用 `{{args}}` 作为用户输入的占位符。

示例：`.gemini/commands/convert-currency.toml`

```toml
[command]
prompt = """You are a currency conversion assistant. Your task is to convert currency amounts accurately using the provided exchange rates.

## Exchange Rates (base currency: USD)

- United States Dollar (USD): 1.00
- Euro (EUR): 0.92
- British Pound Sterling (GBP): 0.79
- Chinese Yuan Renminbi (CNY): 7.22
- Japanese Yen (JPY): 155.50

## Instructions

When the user asks: {{args}}

1. Parse the amount and currencies from the user's request
2. Convert using the exchange rates
3. Show the result with clear formatting

## Example

Input: "$763.45 USD to EUR"
Output: $763.45 USD = 702.37 EUR (calculation: 763.45 x 0.92 = 702.374)

Be precise with decimal places and round to 2 decimal places."""
```

### 技能（`.gemini/skills/name/SKILL.md`）

技能是提供上下文和指令的 markdown 文件。它们通过自然语言激活——只需提到技能的用途，Gemini 就会加载它。

示例：`.gemini/skills/convert-currency/SKILL.md`

```markdown
You are a currency conversion assistant. Your task is to convert currency amounts accurately using the provided exchange rates.

[... 与上面相同的提示内容，但不包含 {{args}} ...]
```

### 什么时候用哪个？

- **命令** — 当你想要一个带参数的 `/斜杠命令` 快捷方式时
- **技能** — 当你想让 Gemini 在自然对话中拥有某种背景知识时

---

## `{{args}}` 占位符

在命令 TOML 文件中，`{{args}}` 是一个占位符，会被你在命令名称后输入的内容替换。

例如：

- 命令：`/convert-currency How much is $180 USD in Euro?`
- `{{args}}` 变成：`How much is $180 USD in Euro?`

这就是你的输入流入提示模板的方式。

---

## 动手练习：练习 1（手动方式）

**目标：** 体验手动输入完整系统提示是什么感觉。

**操作步骤：**

1. 在终端中打开 Gemini CLI
2. 复制下面方框中的整段系统提示
3. 粘贴到 Gemini CLI 中

```
You are a currency conversion assistant. Your task is to convert currency amounts accurately using the provided exchange rates.

## Exchange Rates (base currency: USD)

- United States Dollar (USD): 1.00
- Euro (EUR, official common currency of the Eurozone): 0.92
- British Pound Sterling (GBP): 0.79
- Chinese Yuan Renminbi (CNY): 7.22
- Japanese Yen (JPY): 155.50

## Instructions

When the user asks: How much is $180 USD in Euro?

1. Parse the amount and currencies from the user's request
2. Convert the amount using the provided exchange rates:
   - If converting FROM USD: multiply the amount by the target currency rate
   - If converting TO USD: divide the amount by the source currency rate
   - If converting between non-USD currencies: convert to USD first, then to the target currency
3. Provide the result with clear formatting, showing:
   - The original amount and currency
   - The converted amount and currency
   - The calculation used (optional, for transparency)

## Example

Input: "$763.45 USD to EUR"
Output: $763.45 USD = 702.37 EUR (calculation: 763.45 x 0.92 = 702.374)

Be precise with decimal places and round to 2 decimal places for currency amounts.
```

**你会注意到：**

要复制粘贴的内容真不少。虽然能用——Gemini 会给你一个完美的答案。但想象一下每次需要货币换算都这样做。这就是斜杠命令大显身手的地方。

---

## 动手练习：练习 2（使用斜杠命令）

**目标：** 用斜杠命令完成同样的事情。

**操作步骤：**

1. 在 Gemini CLI 中，直接输入：

```
/convert-currency How much is $180 USD in Euro?
```

2. 按 Enter

**你会注意到：**

你得到了和练习 1 一样高质量的答案，但你只输入了一行，而不是一大段文字。斜杠命令帮你加载了整个系统提示，并把你的问题插入到 `{{args}}` 的位置。

**对比练习 1 和练习 2** — 相同的结果，极少的操作。

---

## 斜杠命令的幕后工作原理

当你输入 `/convert-currency How much is $180 USD in Euro?` 时，Gemini CLI 做了这些事情：

1. 在 `.gemini/commands/` 中搜索匹配的命令
2. 在你输入时显示自动补全建议
3. 从匹配的 TOML 文件（`convert-currency.toml`）中加载提示
4. 将 `{{args}}` 替换为你的输入（`How much is $180 USD in Euro?`）
5. 将组装好的提示发送给 AI 模型
6. 返回响应

这只是自动化——没有什么魔法。斜杠命令是你手动操作的快捷方式（你刚在练习 1 中就手动操作过了）。

---

## 为什么从简单的例子开始

这个货币换算的例子是特意设计得很简单的。我们用斜杠命令来做一件直白的事情，这样你就能清楚地理解其中的机制。

但事实是：斜杠命令和技能是通往更强大工作流的大门。在后续课程中，你将用它们来：

- 自动化代码审查
- 生成文档
- 运行多步分析工作流
- 创建项目专属助手

你现在学到的——保存提示并快速调用的模式——是所有这些的基础。这可能只是这个系统能做的事情的 10%。先掌握这 10%，剩下的自然水到渠成。

---

## 快速参考

- **自动补全：** 输入 `/` 查看可用命令
- **语法：** `/command-name arguments`
- **查看命令：** `cat .gemini/commands/[command-name].toml`
- **查看技能：** `cat .gemini/skills/[skill-name]/SKILL.md`
- **概念：** 命令 = 提示模板 + 快速 `/` 访问；技能 = 自然语言对话的背景上下文
- **好处：** 用最少的输入执行复杂的工作流

---

## 导师寄语：自动化重复性工作流

每个有经验的开发者最终都会学到同一个教训：如果你做一件事超过两次，就把它自动化。

斜杠命令是最简单的自动化形式之一。你把一个会反复输入的提示保存了一次。就这么简单。不需要花哨的脚本，不需要复杂的配置——只是一个包含你指令的 TOML 文件。

但这个简单的习惯会产生复利效应。当你开始为自己的工作流创建命令——代码审查、文档生成、调试模式——你会注意到一件事：你不只是在省键盘敲击次数。你是在把自己的最佳实践编码成可复用的模板。

从 AI 工具中获益最多的开发者，不是那些打最长提示的人。而是那些建立了一个精心设计的命令和技能库、把自己的专业知识固化下来的人。从今天开始建立你的吧。

---

## 延伸阅读

- [Gemini CLI 文档](https://github.com/google-gemini/gemini-cli)
