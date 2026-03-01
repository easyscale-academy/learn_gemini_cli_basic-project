# 安装 Claude Code：用 mise 管理你的 Claude Code

## 📋 本节目标

- 理解为什么推荐用 mise 安装 Claude Code
- 通过 mise 完成 Claude Code 的安装
- 验证安装成功

## 🎯 为什么要学这个？

Claude Code 是 Anthropic 推出的命令行 AI 编程助手，可以直接在 Terminal 里帮你写代码、调试、重构。既然我们知道它这么强大，那就来试试吧！

试试的第一步，就是安装。

## 📝 前置知识提示

本教程假设你已经了解：

- 如何使用 mise（"包管理器的包管理器"）
- 如何在 GitHub Codespace 中工作

如果你对 mise 还不熟悉，建议先了解 mise 的基本安装和使用。

## 📖 为什么不用官方安装命令？

你可能在 [Claude Code 官网](https://claude.ai/download/claude-code) 看到过这样的安装命令：

```
curl -fsSL https://claude.ai/install-cli.sh | sh

```

这个命令当然能用，但我们**不推荐**这种方式。原因是：

**官方命令是"全局安装"**——它把 Claude Code 装到你整台电脑的某个固定位置。这带来几个问题：

1. **版本升级麻烦** - 如果以后 Claude Code 有更新，你得手动处理
2. **多版本共存困难** - 如果某个老项目需要旧版本 Claude Code，而新项目需要新版本，全局安装根本做不到
3. **卸载清理困难** - 官方脚本装的东西散落在各处，想彻底卸载很麻烦

**用 mise 安装则完全不同：**

1. **版本切换自如** - 不同项目可以用不同版本
2. **升级一行命令** - mise 自动处理
3. **干净整洁** - 所有工具统一管理，想删就删

既然我们已经学了 mise 这个"万能工具管理器"，那就从一开始就用最靠谱的方式来安装，以后省心省力。

## 💻 实战：用 mise 安装 Claude Code

我们准备了一个教学用的 Repository，里面已经配置好了 mise.toml 文件。

### 准备工作：Fork 教学 Repository

1. 访问教学 Repository：[https://github.com/MacHu-GWU/learn_claude_code_basic-project](https://github.com/MacHu-GWU/learn_claude_code_basic-project)
2. 点击右上角的 **Fork** 按钮，将它复制到你自己的 GitHub 账号下
3. 进入你 Fork 后的 Repository
4. 切换到 `` 01-install-and-configure-claude-code `` 这个 Branch

在 Repository 页面左上方，你会看到一个显示当前 Branch 名称的下拉菜单（默认可能是 `` main ``）。点击它，选择 `` 01-install-and-configure-claude-code ``。

### 启动 Codespace

切换到正确的 Branch 后，点击绿色的 **Code** 按钮，选择 **Codespaces** 标签页，点击 **Create codespace on 01-install-and-configure-claude-code**。

> **重要：** Codespace 启动后，检查一下左下角或底部状态栏显示的 Branch 是不是 `` 01-install-and-configure-claude-code ``。如果不是，点击切换到正确的 Branch 再继续。

### 先观察：mise.toml 文件

在开始操作之前，我们先看看这个项目里的关键文件。打开 `` mise.toml ``，你会看到类似这样的内容：

```
[tools]
claude = "latest"

```

就这么简单！这行配置的意思是：**这个项目需要最新版本的 Claude Code**。

mise 的强大之处就在于：你只需要在配置文件里声明"我需要什么工具、什么版本"，剩下的安装、管理、切换都交给 mise。

### 第一步：确认 mise 已安装并信任配置文件

如果你是新创建的 Codespace，先确认 mise 已经安装：

```
mise

```

如果看到帮助信息，说明 mise 已就绪。如果看到 `` command not found ``，需要先安装 mise。

然后，运行信任命令：

```
mise trust

```

**什么是 **`` mise trust ``**？**

想象一下：你从网上下载了一个项目，里面有个 mise.toml 配置文件。这个文件可能会告诉 mise 安装各种工具、设置环境变量、运行脚本……如果 mise 不问你就自动执行，万一配置文件里有恶意内容怎么办？

所以 mise 有个**安全机制**：对于每个项目的配置文件，你需要明确告诉 mise "我信任这个文件，你可以按它说的做"。这就是 `` mise trust `` 的作用。

这个操作对每个项目只需要做一次。

### 第二步：激活 mise

```
mise activate

```

**什么是"激活"？**

`` mise activate `` 告诉 mise："请监控这个目录，当 mise.toml 有任何更新时，自动让改动生效。"

打个比方：

- 没激活之前，mise 像是一个"需要你每次手动呼叫的管家"
- 激活之后，mise 变成"随时待命、自动响应的智能管家"

激活状态会一直保持，直到你删除这个 Codespace（相当于重装系统）。每个项目只需要激活一次。

### 第三步：安装工具

现在，运行安装命令：

```
mise install

```

mise 会读取 mise.toml 里的 `` [tools] `` 配置，自动下载并安装所有声明的工具——在我们这个例子里，就是最新版本的 Claude Code。

**mise 的智能复用**

这里要说一个 mise 的重要优点：**智能复用，节约磁盘空间**。

假设你有 10 个项目，都需要用到 Claude Code latest 版本。mise 不会傻傻地装 10 份，而是只安装 1 份，然后让 10 个项目都"引用"这同一份。

如果 latest 版本有更新呢？mise 会安装新版本（这时确实会有 2 份），但旧版本可以很容易地清理掉。而且如果某个老项目还需要旧版本，它依然能正常工作。

### 第四步：验证安装成功

```
which claude
```

如果看到类似这样的路径输出：

```
/home/codespace/.local/share/mise/installs/claude/latest/bin/claude
```

> **WARNING**
> 
> 现在是 2026 年 2 月, 从 2026 年 1 月起, Claude Code 的官方包发布方式发生了改变, 所以导致过去的 mise.toml 中的 `` claude = “latest” `` 的方式会有一些小问题. 你安装后打 `` claude `` 可能无法启动 Claude Code. 这时你需要用 `` mise exec -- claude `` 来显式指定用 mise 运行 claude. 希望 Mise 官方能快速跟进修复这个问题.

🎉 **恭喜！Claude Code 安装成功！**

路径的具体内容可能略有不同，但只要有输出（而不是 `` claude not found ``），就说明安装成功了。

## 👨‍🏫 导师寄语：从"拷贝"到"引用"的思维升级

完成安装后，我想和你聊聊一个更深层的概念：**工具版本管理的两难困境**，以及 mise 如何优雅地解决它。

### 全局安装的困境

传统的"全局安装"方式（比如官方的 `` curl ... | sh ``）有一个根本问题：**整台电脑只能有一个版本**。

这在现实工作中会造成很大麻烦：

- 项目 A 需要 Python 3.9（因为某个依赖不支持新版本）
- 项目 B 需要 Python 3.11（因为要用新特性）
- 项目 C 需要 Python 3.12（因为是最新项目）

如果只能全局安装一个版本，你怎么办？每次切换项目都重新安装？这显然不现实。

### 每个项目独立安装的浪费

那反过来，每个项目都独立安装自己的工具呢？

问题是：很多项目需要的版本是相同的。如果你有 20 个项目都用 Python 3.11，难道要装 20 份一模一样的 Python？这太浪费磁盘空间了。

### mise 的解法：引用而非拷贝

mise 的核心思想是：**只维护一份实体，其他都是"引用"**。

- Claude Code latest 版本？只在磁盘上存一份
- 10 个项目都要用？都"指向"这同一份
- 有新版本？安装新的，但旧的不删（因为可能有项目还在用）
- 确定不需要旧版本了？一条命令清理干净

这种"只维护一份，其他都是引用"的思维，可能会伴随你终生。

### 这种思维的迁移价值

哪怕你不做软件工程相关的事情，这个思维模式也非常有用。

想想看，生活中有多少场景是这样的：

- **同一份资料在多个地方用到** - 你是复制 10 份，还是保存 1 份然后到处"链接"到它？
- **需要保留历史版本** - 你是每次都完整备份，还是只保存"变化的部分"？
- **多人协作同一份文档** - 你是每人一份副本各改各的，还是大家都编辑同一份？

现代的云存储、版本控制、知识管理工具，底层都在用类似的思想：

- Google Docs 的共享链接（引用同一份文档）
- Git 的增量存储（只保存变化）
- Notion 的数据库关联（引用而非重复）

mise 教给我们的，不只是一个安装工具的方法，更是一种高效管理资源的思维方式。

## ✅ 完成检查清单

- [ ] Fork 了教学 Repository 到自己的账号
- [ ] 切换到 `` 01-install-and-configure-claude-code `` Branch
- [ ] 在正确的 Branch 上创建了 Codespace
- [ ] 确认 Codespace 里的 Branch 是正确的
- [ ] 运行 `` mise `` 确认 mise 已安装
- [ ] 运行 `` mise trust `` 信任配置文件
- [ ] 运行 `` mise activate `` 激活 mise
- [ ] 运行 `` mise install `` 安装 Claude Code
- [ ] 运行 `` which claude `` 看到路径输出

## 💡 关键要点总结

1. **推荐用 mise 安装 Claude Code** - 比官方全局安装更灵活、更干净
2. **mise.toml 声明工具需求** - `` [tools] `` 里写明需要什么工具、什么版本
3. **三步走：trust → activate → install** - 信任配置、激活监控、安装工具
4. **mise 智能复用** - 相同版本只存一份，节约磁盘空间
5. `` which claude ``** 验证安装** - 有路径输出就说明成功