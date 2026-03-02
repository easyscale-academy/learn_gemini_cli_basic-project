# 费用分析器

> 通过构建一个 Python 费用分析器来练习 AI 辅助开发 —— 刻意使用你不熟悉的技术栈。

## 概述

这个练习与之前的课程不同。你不是在学习某个特定的 Gemini CLI 功能，而是在练习使用 Gemini CLI 作为开发伙伴，用你可能不熟悉的工具来构建真实项目。

你将使用 **Python**、**Polars**（一个快速的 DataFrame 库）和 **SQL 查询**来分析费用数据。如果这些对你来说很陌生——这正是练习的意义所在。目标不是精通 Python 或 Polars，而是练习一种可迁移的技能：**与 AI 协作来应对不熟悉的领域**。

这就是现实世界中 AI 辅助开发的样子。你描述你想要什么，AI 帮你构建，你通过提问来学习。

## 学习目标

完成这个练习后，你将练习到：

1. **清晰描述任务** —— 将需求拆解为具体、可执行的请求
2. **请求解释** —— 不只是接受代码，而是理解*为什么*这样做
3. **测试驱动的迭代** —— 用失败的测试来指导实现，一次一个函数
4. **分而治之的思维** —— 通过逐个解决小问题来应对复杂任务

## 前提条件

开始这个练习之前，你需要：

- **命令行基础** —— 能够进行目录导航和运行命令
- **一个 AI 助手**（Gemini CLI、Cursor 等）—— 已安装并可用
- **愿意尝试的心态** —— 不需要 Python 经验；AI 会帮助你

> **注意：** 你不需要事先了解 Python、Polars 或 SQL。通过 AI 辅助来学习使用不熟悉的工具，正是我们要练习的技能。

---

## 你将构建什么

一个 Python 函数，能够：
1. 读取一个 TSV（制表符分隔）费用交易文件
2. 筛选出仅属于 2025 年第三季度（7月-9月）的交易
3. 找出每个类别中的最高支出
4. 将结果作为字典返回

**示例输出：**
```python
{
    'Dining': 320.0,
    'Entertainment': 199.0,
    'Groceries': 198.5,
    'Shopping': 156.0,
    'Transport': 52.4,
    'Utilities': 145.8
}
```

---

## 核心概念

在开始之前，这里是你将会遇到的工具的简要概述。不用担心记住这些——你会在实践中学习，随时可以向 Gemini 提问。

### Python 项目结构

```
expense_analyzer/
├── __init__.py          # 使这个目录成为 Python 包
├── impl.py              # 你的实现（你写代码的地方）
├── impl_example.py      # 参考实现（先别偷看！）
├── expense.tsv          # 数据文件（119 条交易记录）
├── tests/
│   └── test_impl.py     # 验证你代码正确性的测试
├── pyproject.toml       # 项目配置和依赖
└── mise.toml            # 任务运行器配置
```

### uv —— Python 包管理器

**uv** 是一个快速的 Python 包管理器（类似于 Python 版的 npm）。我们通过 mise 使用它：

- `mise run venv-create` —— 创建隔离的 Python 环境
- `mise run inst` —— 安装 `pyproject.toml` 中列出的依赖

### Polars —— 数据处理库

**Polars** 是一个快速的 Python DataFrame 库。可以把它想象成代码中的超级电子表格：

```python
import polars as pl

# 将文件读取为 DataFrame
df = pl.read_csv("data.tsv", separator="\t")

# 访问列、筛选行、聚合数据
```

### SQL 接口

Polars 允许你用 SQL 查询 DataFrame——一种为数据问题设计的语言：

```python
# 注册 DataFrame 用于 SQL 查询
ctx = pl.SQLContext({"expenses": df})

# 用 SQL 提问
result = ctx.execute("SELECT * FROM expenses WHERE amount > 100").collect()
```

### pytest —— 测试框架

**pytest** 运行你的测试并告诉你哪些部分工作正常：

```bash
mise run test
```

绿色 = 通过。红色 = 失败，并附有有用的错误信息。

### 分而治之

不是一次构建所有东西，而是一次实现一个函数：

1. `load_expense_data()` —— 只负责读取文件
2. `preview_first_rows()` —— 只负责显示几行
3. `filter_q3_data()` —— 只负责按日期筛选
4. `find_max_expense_per_category()` —— 只负责找最大值

每个函数都建立在前一个之上。每个都可以独立测试。

---

## 练习

### 练习 1：设置开发环境

**目标：** 让项目准备就绪。

**怎么做：**

请 Gemini 帮你设置：

```
看看 mise.toml 和 pyproject.toml。帮我设置这个项目的开发环境。
```

**应该发生什么：**
1. 运行 `mise run venv-create` 创建 Python 虚拟环境
2. 查看 `pyproject.toml`——注意 Polars 依赖被注释掉了
3. 取消注释 Polars 依赖行
4. 运行 `mise run inst` 安装依赖

**验证是否成功：**
```bash
mise run test
```

你应该会看到测试失败——这是预期的！函数还没实现。但如果测试*能运行*（即使失败），说明你的环境设置正确了。

> **关键收获：** 环境设置是常见的阻碍。AI 助手擅长阅读配置文件并引导你完成设置步骤。不要一个人苦苦挣扎——描述你看到的情况，然后寻求帮助。

---

### 练习 2：实现 `load_expense_data()`

**目标：** 将 TSV 文件读取为 Polars DataFrame。

**打开 `expense_analyzer/impl.py`** 找到 `load_expense_data()` 函数。里面有 TODO 注释说明要做什么。

**向 Gemini 求助：**

```
看看 expense_analyzer/impl.py。帮我实现 load_expense_data() 函数。
我需要将 expense.tsv（制表符分隔）读取为 Polars DataFrame。
```

**实现之后，请 Gemini 解释：**

```
/teach-explain pl.read_csv() 如何处理 TSV 文件？为什么需要 separator="\t"？
```

> **关键收获：** 不要只是接受代码。问"为什么"和"怎么做"——理解方法比记住具体语法更有价值。

---

### 练习 3：实现 `preview_first_rows()`

**目标：** 使用 SQL 从 DataFrame 中选择前 N 行。

**向 Gemini 求助：**

```
帮我实现 impl.py 中的 preview_first_rows()。
它应该使用 Polars SQL 来选择前 N 行。看看 TODO 了解细节。
```

**探索核心概念：**

```
/teach-explain Polars 中的 SQL 上下文是什么？为什么要在查询之前注册 DataFrame？
```

> **关键收获：** SQL 是一门强大的数据查询语言。即使你从未用过它，语法读起来几乎像英语：`SELECT * FROM expenses LIMIT 5`。

---

### 练习 4：实现 `filter_q3_data()`

**目标：** 筛选出仅属于 2025 年第三季度的交易（7月1日 - 9月30日）。

**向 Gemini 求助：**

```
帮我实现 impl.py 中的 filter_q3_data()。
我需要使用 SQL WHERE 子句对日期列进行筛选，只保留 2025 年第三季度（7-9月）的数据。
```

**测试你的进度：**
```bash
mise run test
```

你应该开始看到一些测试通过了！

> **关键收获：** 日期筛选是现实世界中的常见任务。SQL 让它变得易读：`WHERE date >= '2025-07-01' AND date <= '2025-09-30'`。

---

### 练习 5：实现 `find_max_expense_per_category()`

**目标：** 使用 SQL GROUP BY 找出每个类别中的最高支出。

**向 Gemini 求助：**

```
帮我实现 impl.py 中的 find_max_expense_per_category()。
我需要按类别 GROUP BY 并找出 2025 年第三季度数据中每个类别的 MAX(amount)，然后返回字典。
```

**探索 SQL 概念：**

```
/teach-explain SQL 中的 GROUP BY 做什么？MAX() 如何与它配合使用？
```

> **关键收获：** GROUP BY + 聚合函数（MAX、SUM、AVG）是数据分析的基础。理解这个模式可以解答大量现实世界的数据问题。

---

### 练习 6：运行所有测试

**目标：** 验证一切正常工作。

```bash
mise run test
```

**预期结果：** 3 个测试全部通过。

如果测试失败，用 Gemini 调试：

```
/teach-debug 这是我的测试输出：[粘贴错误信息]。帮我找出问题所在。
```

**当所有测试通过后**，运行：
```
/teach-check
```

---

## 反思

完成练习后，思考以下问题：

1. **你是如何向 Gemini 描述任务的？** 你的提示词随着练习推进是否变得更具体了？
2. **通过问"为什么"你学到了什么？** 哪些解释让你感到意外？
3. **失败的测试如何帮助了你？** 错误信息是否引导了你的下一步？
4. **你能把这个方法应用到其他不熟悉的技术栈吗？**（比如 Rust、Go、一个新框架）

你练习的这个方法——描述、实现、测试、追问——适用于任何技术。这才是真正的技能。

---

## 导师的话

**为什么这个练习很重要：**

我见过经验丰富的开发者在遇到不熟悉的技术栈时僵住。"我不会 Python"变成了一堵无法逾越的墙。

但事实是：**你不再需要事先了解所有东西了**。AI 助手改变了这个等式。真正重要的技能是知道如何*协作*——如何描述你想要什么，如何提出正确的问题，如何验证答案是否正确。

这个练习刻意将你推出舒适区。Python、Polars 和 SQL 只是载体。你真正在练习的是：

- **将问题拆解为小块** —— 不是"构建一个费用分析器"，而是"读取这个文件、筛选这些行、按这个列分组"
- **清晰沟通** —— 模糊的提示得到模糊的回答。具体的提示得到可用的代码。
- **通过测试来学习** —— 测试在你完全理解代码之前就能告诉你是否走在正确的路上。
- **逐步建立理解** —— 你不需要一次理解所有东西。每个函数都教会你更多一点。

这些技能可以迁移到任何技术、任何项目、任何团队。这就是这个练习存在的意义。

---

## 快速参考

**环境设置：**
```bash
mise run venv-create    # 创建虚拟环境
mise run inst           # 安装依赖
```

**运行测试：**
```bash
mise run test           # 运行所有测试
```

**教学命令：**
```
/teach-start            # 开始引导式学习
/teach-code             # 获取代码帮助 + 学习笔记
/teach-explain          # 理解概念或代码
/teach-debug            # 带引导地调试错误
/teach-check            # 验证你的作业
/teach-brainstorm       # 理清想法
```

**中文教学命令：**
```
/teach-start-cn         # 开始引导式学习（中文）
/teach-code-cn          # 获取代码帮助 + 学习笔记（中文）
/teach-explain-cn       # 理解概念或代码（中文）
/teach-debug-cn         # 带引导地调试错误（中文）
/teach-check-cn         # 验证你的作业（中文）
/teach-brainstorm-cn    # 理清想法（中文）
```

**关键文件：**
- `expense_analyzer/impl.py` —— 你的实现
- `expense_analyzer/impl_example.py` —— 参考实现（尽量不要偷看！）
- `expense.tsv` —— 数据
- `tests/test_impl.py` —— 测试

---

## 参考实现

完整的可运行实现在 `expense_analyzer/impl_example.py` 中提供。

**我们的建议：** 先尝试在 AI 辅助下实现每个函数。只有在真正卡住且 AI 解释无法帮助时才查看参考实现。学习发生在探索和对话中，而不是在复制答案中。
