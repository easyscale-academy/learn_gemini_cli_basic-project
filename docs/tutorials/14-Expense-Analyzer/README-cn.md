# 费用分析器

> 通过构建一个 Python 费用分析器来练习 AI 辅助开发 —— 刻意使用你不熟悉的技术栈。

## 概述

这个练习与之前的课程不同。你不是在学习某个特定的 Gemini CLI 功能，而是在练习使用 Gemini CLI 作为开发伙伴，用你可能不熟悉的工具来构建真实项目。

你将使用 **Python**、**Polars**（一个快速的 DataFrame 库）和 **SQL 查询**来分析费用数据。目标不是精通 Python 或 Polars，而是练习一种可迁移的技能：**与 AI 协作来应对不熟悉的领域**。

## 你将构建什么

一个 Python 函数，能够：
1. 读取一个 TSV 费用交易文件
2. 筛选出 2025 年第三季度（7-9月）的交易
3. 找出每个类别中的最高支出
4. 将结果作为字典返回

## 学习目标

1. **清晰描述任务** —— 将需求拆解为具体的请求
2. **请求解释** —— 理解代码*为什么*这样写，而不只是接受它
3. **测试驱动的迭代** —— 用失败的测试来指导实现
4. **分而治之的思维** —— 逐个解决小问题

## 练习

1. 设置开发环境
2. 实现 `load_expense_data()` —— 读取 TSV 文件
3. 实现 `preview_first_rows()` —— SQL SELECT + LIMIT
4. 实现 `filter_q3_data()` —— SQL WHERE 筛选日期
5. 实现 `find_max_expense_per_category()` —— SQL GROUP BY + MAX
6. 运行所有测试并验证

## 开始

切换到分支并阅读完整教程：

```bash
git checkout 14-Expense-Analyzer
```

然后打开 `README.md` 查看完整的教程指南。
