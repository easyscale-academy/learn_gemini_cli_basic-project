# Gemini CLI Basics: Show AI What You See with Screenshots

> Learn how to share screenshots with Gemini CLI so the AI can see error messages, UI elements, and diagrams — just like showing your screen to a colleague.

## Overview

You hit an error screen and want to ask the AI for help. You could try describing it in words: "There's this red box with a bunch of text, something about an error..." But that's tedious and imprecise.

A much better approach: just show the AI the screenshot. Gemini CLI can read images — error messages, UI screenshots, code screenshots, flowcharts, architecture diagrams. Once you learn to communicate with screenshots, you'll get answers faster and more accurately.

## Learning Objectives

Think about the last time you tried to describe a bug to someone over text. You probably spent five minutes typing out what was on your screen, only for them to say "can you just send me a screenshot?" Screenshots cut through ambiguity instantly. The same applies when working with AI — instead of struggling to describe what you see, just show it.

By the end of this exercise, you will:

1. Know how to take a screenshot and save it to your project
2. Upload screenshots to your Codespace and get their file path
3. Send a screenshot path to Gemini CLI and have the AI interpret what it sees

## Prerequisites

- Gemini CLI installed and authenticated (completed in previous lessons)
- A GitHub Codespace with this project open
- Completed Lesson 04 (reading files with `@`) and Lesson 05 (reading URLs)

## What You'll Build

No code this time — this is a skill exercise. You'll practice sharing screenshots with Gemini CLI, which is essential for debugging errors, getting UI feedback, and communicating visual information to the AI.

---

## Key Concepts

### Why Screenshots Beat Text Descriptions

When you describe an error in words, you might miss key details — the exact error code, the stack trace, or context clues in the surrounding UI. A screenshot captures everything at once, exactly as it appears. The AI can read text in images, identify UI elements, understand layouts, and even interpret diagrams.

### The Workflow: Screenshot to AI

The process has four steps:

1. **Take a screenshot** on your computer
2. **Upload it** to your Codespace (if working in a browser)
3. **Copy the file path** of the uploaded screenshot
4. **Send the path** to Gemini CLI with your question

### How to Take a Screenshot

**On Mac:**
- `Cmd + Shift + 4` — drag to capture a selected area
- The screenshot saves automatically to your Desktop (or your configured default location)

**On Windows:**
- `Win + Shift + S` — drag to capture a selected area
- The screenshot goes to your clipboard — paste it into a file and save it

**In a Codespace (browser-based):**
- Use your operating system's built-in screenshot tool
- Save the screenshot somewhere you can easily find it

### How to Upload to Your Codespace

If you're working in a browser-based Codespace, you need to get the screenshot file into the Codespace:

1. In the Explorer panel on the left, find the folder where you want to put the screenshot
2. **Right-click the folder → select "Upload..."**
3. Choose the screenshot file you saved
4. Wait for the upload to finish

### How to Get the File Path

Once your screenshot is in the Codespace:

1. **Right-click the screenshot file** in the Explorer panel
2. **Select "Copy Relative Path"**

You'll get something like `img/error-message.png`. Then use it with `@` in Gemini CLI, just like referencing any other file.

---

## Exercises

### Exercise 1: Have AI Describe Your Screen

**Goal:** Take a screenshot of your Codespace and have Gemini CLI describe what it sees.

**What to do:**

1. Take a screenshot of your current Codespace screen — the file tree on the left, the editor, whatever is visible
2. Upload the screenshot to your project (right-click a folder in Explorer → Upload)
3. Right-click the uploaded file → Copy Relative Path
4. Open Gemini CLI and type:

```
Look at this screenshot and tell me what interface is shown: @img/your-screenshot.png
```

(Replace `img/your-screenshot.png` with your actual file path)

5. Press Enter

**What you'll notice:**

Gemini describes what it sees — something like "This is the VS Code editor showing your project's file structure in the Explorer panel on the left..." It reads text, identifies UI elements, and understands the layout.

> **Key insight:** The AI can "see" images just like it can read text files. Screenshots give it visual context that's impossible to convey in words alone.

---

### Exercise 2: Get Help with an Error

**Goal:** Capture an error message and ask Gemini CLI to explain it.

**What to do:**

1. Find or trigger any error message in your development environment (a terminal error, a browser error, a linter warning — anything works)
2. Take a screenshot of just the error
3. Upload it to your Codespace and copy the relative path
4. In Gemini CLI, type:

```
Look at this screenshot and tell me what this error means and how to fix it: @img/your-error.png
```

5. Press Enter

**What you'll notice:**

Gemini reads the error message from the image, explains what it means, and suggests how to fix it. This is often faster than copying the error text manually, especially for complex error dialogs with multiple pieces of information.

> **Key insight:** For debugging, screenshots are your fastest path to help. The AI reads the error text, spots the error code, and sees surrounding context — all from one image.

---

## Reflection: What Did We Learn?

- The workflow is: **screenshot → upload to Codespace → copy relative path → send to Gemini CLI with `@`**
- Gemini CLI can read images — error messages, UI elements, code, diagrams
- Screenshots are faster and more precise than describing what you see in words
- Use `@` with the screenshot's relative path, just like referencing any other file

---

## Mentor's Note

**Why this exercise matters:**

You now have three ways to feed context to the AI: local files (`@`), web URLs, and screenshots. Together, these cover almost every situation where you need the AI to understand something. Files for code, URLs for documentation, screenshots for anything visual. This is the complete toolkit for giving AI the context it needs to help you effectively.

**Key insights:**

- Screenshots remove the "lost in translation" problem. When you show the AI exactly what you see, there's no room for miscommunication. This is especially valuable for debugging — the AI sees the same error you do, with all the details intact.
- The best developers I know are great communicators. Using screenshots to communicate with AI is no different — clear, precise context leads to clear, precise answers.

**Next steps:**

Build the habit: whenever you encounter a visual problem — an error dialog, a broken layout, a confusing UI — screenshot it and ask Gemini CLI. You'll be surprised how often a screenshot gets you an answer in seconds.

---

## Quick Reference

**Screenshot workflow:**
1. Take screenshot (`Cmd+Shift+4` on Mac, `Win+Shift+S` on Windows)
2. Upload to Codespace (right-click folder → Upload)
3. Copy Relative Path (right-click file → Copy Relative Path)
4. Send to Gemini CLI: `@img/screenshot.png`

**Example prompts:**
```
What does this error mean? @img/error.png
Describe what you see in this screenshot: @img/screen.png
What's wrong with this UI? @img/broken-layout.png
```

**Screenshot best practices:**
- Keep text legible — don't crop too tight
- Capture only the relevant area, not the entire screen
- Use descriptive file names like `error-npm-install.png`, not `Screenshot 2024-01-15.png`
