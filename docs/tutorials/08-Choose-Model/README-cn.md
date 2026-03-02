# 选择你的 Gemini Model

> 学习如何在 Gemini CLI 中选择合适的 AI model，平衡能力和成本。

## 为什么要学这个

想象一下：你正在和 Gemini CLI 聊得很顺，问题一个接一个，进度飞快。然后你发现回复变慢了，或者去 Google AI Studio 一看——免费 quota 消耗得比想象中快很多。

这是因为不同的 model 消耗资源的速度差别很大。最强大的 model 并不总是最好的选择——尤其是你在学习、试验、或者做一些简单任务的时候。

好消息是：Gemini CLI 让你自己选 model。选对了 model，你能得到更快的响应、更低的成本、更顺畅的体验。

## 认识 Gemini 的 Model

Gemini CLI 给你提供了几个 model。你可以把它们想象成不同级别的同事：

- **Gemini 2.5 Pro** 是你的资深架构师。它擅长复杂推理、多步分析、以及需要深度理解大型代码库的任务。它有巨大的 1M token context window。能力强大，但成本更高、响应更慢。把它留给真正需要的时候。

- **Gemini 2.5 Flash** 是你最常用的高级工程师。它快速、能干、性价比高——input token 的价格大约是 Pro 的八分之一。Flash 可以轻松应对大部分编码任务、概念解释和学习对话。这是你的默认选择。

- **Gemini 2.5 Flash-Lite** 是你的快速响应队友。最快也最便宜的选项，适合简单查询、格式化任务、以及速度比深度更重要的快速提问。

关键洞察：**学习阶段，Flash 通常绰绰有余**。它快速、实惠，而且能力比你想象的强。把 Pro 留给真正难的问题。

---

## 核心概念

### /model 命令

Gemini CLI 提供了一个交互式的 `/model` 命令，让你随时切换 model。在 Gemini CLI session 中输入 `/model`，你会看到一个选择菜单。你可以选择：

- **Auto 模式** — Gemini 根据任务复杂度自动在 Pro 和 Flash 之间切换
- **Manual 模式** — 你自己指定具体的 model

学习阶段，手动选择 Flash 是能力和效率的最佳平衡。

### 设置保存在哪里

当你切换 model 时，Gemini CLI 会保存你的偏好。有两个位置：

- **项目级别：** 项目目录下的 `.gemini/settings.json`（优先级更高）
- **用户级别：** 主目录下的 `~/.gemini/settings.json`（全局生效）

一个典型的设置文件长这样：

```json
{
  "model": "gemini-2.5-flash"
}
```

你也可以直接编辑这个文件——修改 model 的值然后保存即可。Gemini CLI 启动时会读取这个文件，使用你保存的偏好。

### 命令行覆盖

你也可以在启动 Gemini CLI 时指定 model，而不改变保存的设置：

```bash
gemini --model gemini-2.5-flash
```

当你只想在单次 session 中临时使用不同 model 时，这很有用。

---

## 动手练习

### 练习 1：切换到 Flash

**目标：** 使用 `/model` 命令切换到 Gemini 2.5 Flash。

**操作步骤：**

1. 在终端中打开 Gemini CLI
2. 输入 `/model` 然后按 Enter
3. 当选择菜单出现时，选择 Flash
4. 问 Gemini 一个简单的问题，确认它正常工作

**你会注意到：**

Flash 响应很快，处理学习类问题毫无压力。在这门课程中，你要做的大部分事情，Flash 都是正确的选择。

> **关键洞察：** 能胜任你的任务的最快、最便宜的 model，永远是最佳选择。不要为用不到的能力付费。

---

### 练习 2：验证你的设置

**目标：** 检查你的 model 偏好保存在哪里。

**操作步骤：**

1. 用 `/model` 切换 model 后，在编辑器中打开 `.gemini/settings.json`
2. 确认 `model` 字段显示的是你的选择
3. 试试直接编辑这个文件来更改 model，然后重启 Gemini CLI 看变化是否生效

**你会注意到：**

设置文件是普通的 JSON——简单、可读。如果需要，你随时可以手动检查或修改。

> **关键洞察：** 了解工具把配置存在哪里，能让你有更多控制权。当出了问题时，检查配置文件通常是最快的调试方式。

---

## 回顾：我们学到了什么

Model 选择就是让工具匹配任务：

- **Flash** — 你的日常主力，用于学习、编码帮助和一般问题。快速且实惠。
- **Pro** — 留给复杂的架构决策、大代码库的深度分析、以及真正需要更强推理能力的问题。
- **Flash-Lite** — 速度至上、不需要深度的快速任务。
- **Auto** — 让 Gemini 自己决定，当你不确定该用哪个 model 时很有用。

选择合适 model 的习惯不只适用于 AI 工具——它是你使用任何技术时都应该有的资源意识。

---

## 导师寄语

当我刚开始使用 AI 编程工具时，我总是选最强大的 model。既然有更好的，为什么要将就呢？

但随着时间推移，我学到了一件重要的事：为任务选择合适的工具，是一项基本的工程技能。

用 Pro 来回答一个简单问题，就像开卡车去买菜——能用，但浪费还更慢。我认识的最优秀的工程师都很懂得利用资源——他们理解约束，并在约束中创造性地工作。

Flash 是真的很能干。不要因为它便宜就小看它。

这个 right-sizing 工具的习惯适用于工程的方方面面：为你的场景选择合适的数据库，为你的项目选择合适的框架，为你的代码选择合适的抽象层次。从现在开始培养这个习惯，就从 model 选择这么简单的事情做起。

---

## 快速参考

**切换 model：**
```
/model
```

**启动时指定 model：**
```
gemini --model gemini-2.5-flash
```

**Model 能力：** Pro > Flash > Flash-Lite

**成本：** Pro > Flash > Flash-Lite

**速度：** Flash-Lite > Flash > Pro

**关键文件：**
- `.gemini/settings.json` — 项目级别的 model 偏好
- `~/.gemini/settings.json` — 用户级别的 model 偏好

## 延伸阅读

- [Gemini CLI GitHub Repository](https://github.com/google-gemini/gemini-cli)
- [Gemini Models Overview](https://ai.google.dev/gemini-api/docs/models)
