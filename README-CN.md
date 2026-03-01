# 选择你的 Claude Model

> 学习如何在 Claude Code 中选择合适的 AI model，平衡能力和 quota 消耗。

## 为什么要学这个

想象一下：你正在学习，和 Claude Code 聊得很顺，进度飞快。突然，屏幕上弹出一条消息——"Quota exhausted. Please wait 5 hours."

五个小时。你的学习节奏被打断了，这个 session 就这样结束了。

这是因为 Claude Code 使用 quota 系统。你问的每个问题都会消耗 quota，而越强大的 model 消耗得越多。在 Team Plan 上，quota 是团队成员共享的，所以可能比你预期的更快用完。

好消息是：你可以控制这一点。选择合适的 model，你的 quota 可以用得更久，避免那令人沮丧的等待。

## 认识三个 Model

Claude Code 提供三个 model。你可以把它们想象成三个不同级别的同事：

- **Opus** 是你的行业顶尖专家：把最难、最关键的问题交给它——深层架构决策、悬而未决的边界情况 bug、需要原创推理和跨领域洞察的研究。把 Opus 想象成顶级科技公司的 Distinguished Engineer / Fellow 级别的技术专家——定义标准、撰写白皮书、塑造技术方向的那种人。能力强大，但最好省着用。
- **Sonnet** 是你的 Principal 级工程师：擅长设计和实现复杂系统，编写和审查高质量代码，把抽象想法变成可上线的解决方案。Sonnet 对应 Principal 或 Senior Staff Engineer——严肃工程工作的中坚力量，大多数高级任务的最佳选择。
- **Haiku** 是你的 Senior 工程师：非常适合学习、提问和高效执行定义明确的任务。Haiku 可靠、清晰、性价比高——当问题已经理解清楚、重点是执行的时候，它是完美的选择。

关键洞察：**学习阶段，Haiku 通常就够用了**。把 Opus 留给真正需要它的时候。

## 如何切换 Model

在 Claude Code 中切换 model 只需要几秒钟。

在终端中打开 Claude Code。输入 `/model` 然后按 Enter。你会看到一个有三个选项的菜单。用方向键选择你想要的 model，然后按 Enter 确认。

就这样，你的 model 已经切换了。

你可以通过查看 prompt 区域来验证切换——Claude Code 会在那里显示你当前的 model。

## 设置保存在哪里

当你切换 model 时，Claude Code 会记住你的选择。它把这个偏好保存在项目目录下的 `.claude/settings.json` 文件中。

如果你打开这个文件，会看到类似这样的内容：

```json
{
  "model": "haiku"
}
```

当你重启 Claude Code 时，它会读取这个文件并使用你保存的 model。你也可以直接编辑这个文件——修改值然后保存即可。

知道这一点很有用，因为如果 model 选择出了什么问题，你可以随时检查这个文件，看看实际配置的是什么。

## 动手练习

让我们练习一下你学到的内容。

**你的任务：** 切换到 Haiku 并验证切换成功。

在终端中启动 Claude Code。输入 `/model` 然后按 Enter。当菜单出现时，选择 Haiku。确认后，检查 prompt 区域是否显示 Haiku 作为你当前的 model。

如果你想更进一步，在编辑器中打开 `.claude/settings.json`，确认 `model` 字段显示的是 `haiku`。

## 常见问题

**输入 `/model` 后菜单没有出现**

确保你在输入命令后按了 Enter。slash command 需要提交，而不是只输入。

**Model 总是重置成别的**

检查 `.claude/settings.json` 是否存在且可写。如果文件不存在或 Claude Code 无法写入，你的偏好就不会被保存。

**你看到 "quota exhausted" 消息**

立即切换到 Haiku 以减少消耗。如果你已经在用 Haiku，那就需要等待 quota 刷新——在 Team Plan 上通常大约 5 小时。

## 导师寄语：选择合适的工具

当我刚开始使用 AI 工具时，我总是选最强大的 model。既然有更好的，为什么要将就呢？

但随着时间推移，我学到了一件重要的事：为任务选择合适的工具，是一项基本的工程技能。

用 Opus 来回答一个简单问题，就像开卡车去买菜——能用，但很浪费。我认识的最优秀的工程师都很懂得利用资源——他们理解约束，并在约束中创造性地工作。

这个道理适用于工程的方方面面：为你的场景选择合适的数据库，为你的项目选择合适的框架，为你的代码选择合适的抽象层次。从现在开始培养这个习惯，就从 model 选择这么简单的事情做起。

## 快速参考

- `/model` — 打开 model 选择菜单
- Model 能力：Opus > Sonnet > Haiku
- Quota 消耗：Opus > Sonnet > Haiku
- 设置文件：`.claude/settings.json`

## 延伸阅读

- [Claude Code Documentation](https://code.claude.com/docs)
- [Understanding Claude Models](https://platform.claude.com/docs/en/about-claude/models/overview)
