# Gemini CLI Basics: Getting AI to Read Your Files with @

> Learn how to reference files in Gemini CLI using the `@` symbol so the AI can read and understand your code.

## Overview

When you're working with Gemini CLI, you'll constantly need the AI to look at specific files — a config file, a script, a component. But just saying "check that file" won't cut it. The AI doesn't know which file you mean.

Gemini CLI solves this with a simple convention: type `@` followed by the file's relative path, like `@README.md` or `@src/main.py`. That's all it takes to hand the AI a file to read.

## Learning Objectives

Imagine you have a project with dozens of files. You need the AI to review your database config, but there are three config files in different folders. Without a precise way to point to the right file, you're stuck explaining yourself over and over. The `@` syntax gives you a direct, unambiguous way to say "read this exact file" — and it works every time.

By the end of this exercise, you will:

1. Understand the difference between absolute and relative file paths
2. Use `@` + relative path to reference files in Gemini CLI
3. Combine `@` references with natural language prompts to get useful AI responses

## Prerequisites

- Gemini CLI installed and authenticated (completed in previous lesson)
- A GitHub Codespace with this project open
- Basic comfort with typing commands in a terminal

## What You'll Build

Nothing to build this time — this is a skill exercise. You'll practice referencing files so the AI can read them, which is the foundation for every future task where you ask the AI to analyze, edit, or explain your code.

---

## Key Concepts

### Absolute Path vs. Relative Path

Every file on your computer has an address called a **path**. There are two kinds:

- **Absolute path** — starts from the system root, like `/workspaces/my-project/src/main.py`. It's the file's full address, globally unique.
- **Relative path** — starts from your current directory, like `src/main.py` or `./src/main.py`. It's shorter and depends on where you are right now.

Think of it like giving directions. An absolute path is a full street address: "123 Main Street, Springfield, IL." A relative path is like saying "two blocks down on the left" — it only makes sense if you know where you're starting from.

### Why Gemini CLI Uses Relative Paths

Gemini CLI runs inside your project folder, so it already knows where "here" is. That means relative paths work perfectly — you don't need to type out the full address every time. Just tell it the path from your project root.

For example, if your project looks like this:

- `README.md`
- `src/main.py`
- `src/config.json`
- `tests/test_main.py`

You can reference any file using its path from the project root: `@README.md`, `@src/main.py`, `@src/config.json`.

### The @ Symbol: Your File Reference Tool

In Gemini CLI, the `@` symbol is how you tell the AI "I'm pointing to a file." When Gemini sees `@src/main.py` in your prompt, it reads that file and includes its contents in the conversation.

**The pattern is simple:**

```
@<relative-path-to-file>
```

**Real examples:**

```
@README.md
@src/main.py
@src/components/Button.tsx
@tests/test_config.py
```

You drop these `@` references right into your natural language prompt, and Gemini handles the rest.

### How to Find the Relative Path in Codespace

In the GitHub Codespace file browser (the Explorer panel on the left):

1. **Find your file** in the file tree
2. **Right-click the file name** — a context menu pops up
3. **Select "Copy Relative Path"** — this copies the path relative to your project root

You'll get something like `src/components/Button.tsx` on your clipboard. Then just add `@` in front of it when typing your prompt.

> **Important:** In Codespace, you'll also see a "Copy Path" option that copies the absolute path. For Gemini CLI, you want **"Copy Relative Path"** instead.

---

## Exercises

### Exercise 1: Read a Single File

**Goal:** Get Gemini CLI to read and summarize a file in your project.

**What to do:**

1. Open Gemini CLI in your terminal (type `gemini` and press Enter)
2. Type the following prompt and press Enter:

```
Summarize what this file is about: @README.md
```

3. Observe how Gemini reads the file and gives you a summary

**What you'll notice:**

Gemini reads the entire file contents and responds with a plain-language summary. You didn't have to copy-paste anything — just the `@` reference was enough.

> **Key insight:** The `@` symbol turns a file path into a file reference. Gemini automatically reads the file and includes its contents in the conversation.

---

### Exercise 2: Ask a Specific Question About a File

**Goal:** Use `@` to reference a file and ask a targeted question about it.

**What to do:**

1. In Gemini CLI, pick any file in your project (like `TICKET.md` or `CLAUDE.md`)
2. Right-click it in the Explorer panel and select **Copy Relative Path**
3. Type a specific question using the `@` reference:

```
What are the checklist items in @TICKET.md?
```

4. Press Enter and see how Gemini answers based on the file's actual contents

**What you'll notice:**

Gemini doesn't guess — it reads the file and answers based on what's actually in there. This is how you get precise, grounded answers instead of generic ones.

> **Key insight:** Combining `@` references with specific questions lets you interrogate your codebase through natural conversation.

---

### Exercise 3: Reference Multiple Files

**Goal:** Reference more than one file in a single prompt.

**What to do:**

1. In Gemini CLI, type a prompt that references two files:

```
Compare @README.md and @TICKET.md — what's the difference between these two documents?
```

2. Press Enter and see how Gemini reads both files and compares them

**What you'll notice:**

Gemini reads both files and gives you a comparison. You can reference as many files as you need in a single prompt.

> **Key insight:** You're not limited to one `@` reference per prompt. Use as many as you need to give Gemini the full picture.

---

### Exercise 4: Summarize This Tutorial

**Goal:** Use Gemini CLI to summarize the very tutorial you're reading right now.

**What to do:**

1. In Gemini CLI, type exactly this:

```
summarize @README.md
```

2. Press Enter and read the summary Gemini gives you

**What you'll notice:**

Gemini reads the tutorial file you've been following and produces a concise summary. This is a great way to check your own understanding — does the AI's summary match what you think you learned?

> **Key insight:** You can use `@` to reference any file, including the tutorial itself. This is a handy trick for quickly reviewing long documents without re-reading them top to bottom.

---

## Reflection: What Did We Learn?

- **Relative paths** start from your project root and are shorter than absolute paths — perfect for working inside a project
- The **@ symbol** in Gemini CLI tells the AI to read a specific file
- The syntax is `@<relative-path>` — drop it anywhere in your prompt
- You can use **"Copy Relative Path"** in Codespace to quickly get the right path
- Multiple `@` references in one prompt let you give the AI broader context

---

## Mentor's Note

**Why this exercise matters:**

I know this lesson might feel almost too simple — type `@`, paste a path, done. But here's why I think it's one of the most important skills you'll learn: the quality of your AI interaction depends entirely on the context you provide. An AI without context is just guessing. An AI with the right files loaded? That's a collaborator.

**Key insights:**

- The `@` syntax is your primary tool for grounding AI responses in reality. Without it, the AI works from memory and assumptions. With it, the AI works from your actual code.
- Getting comfortable with file references now will pay off massively later. Every advanced technique — code review, refactoring, debugging — starts with pointing the AI at the right files.

**Next steps:**

Try using `@` references in your daily workflow. Whenever you ask Gemini CLI a question about your code, include the relevant file references. You'll notice the answers get dramatically more useful.

---

## Quick Reference

**Reference a file:**
```
@README.md
@src/main.py
@path/to/any/file.txt
```

**Use in a prompt:**
```
Explain what @src/config.json does
What's wrong with @tests/test_main.py?
Compare @src/old.py and @src/new.py
```

**Copy a relative path in Codespace:**
Right-click file → "Copy Relative Path" → paste into prompt with `@` prefix

**Key files in this project:**
- `README.md` - This tutorial
- `TICKET.md` - Your task card with checklist
- `CLAUDE.md` - Project configuration for AI assistants
