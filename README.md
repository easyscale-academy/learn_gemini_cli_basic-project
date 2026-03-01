# Claude Code Basics (Part 3): Show AI What You See with Screenshots

[Extension: com.atlassian.confluence.macro.core/toc]

## Why This Matters

Imagine you hit an error screen and want to ask AI for help. You could try describing it in words: "There's this red box with a bunch of English text in it, something about an error..."

That's both tedious and imprecise. **A much better approach: just show AI the screenshot.**

A picture is worth a thousand words — and Claude Code can actually *read* images, including:

- Error message screenshots
- UI screenshots
- Code screenshots
- Flowcharts and architecture diagrams

Once you learn to communicate with AI through screenshots, you'll get answers faster and more accurately.

---

## Step-by-Step Instructions

### Step 1: Take a Screenshot and Save It Locally

**On Mac:**

- `` Cmd + Shift + 4 `` — drag to capture a selected area
- The screenshot is automatically saved to your Desktop (or wherever you've set as the default location)

**On Windows:**

- `` Win + Shift + S `` — drag to capture a selected area
- The screenshot is saved to your clipboard — you'll need to paste it into a file and save it

**In a Codespace (browser-based):**

- Use your operating system's built-in screenshot tool
- Save the screenshot somewhere you can easily find it

### Step 2: Upload the Screenshot to Your Codespace

If you're using a Codespace in the browser, you'll need to upload the screenshot:

1. In the Explorer panel on the left side of your Codespace, find the folder where you want to put the screenshot
2. **Right-click the folder → select "Upload..."**
3. Choose the screenshot file you just saved
4. Wait for the upload to finish

### Step 3: Copy the Screenshot's Absolute Path

Once uploaded, the screenshot will appear in your file list:

1. **Right-click the screenshot file**
2. **Select "Copy Path"** (same as copying the path of any code file)

You'll get something like:

```
/workspaces/my-project/screenshots/error-message.png

```

### Step 4: Send the Path to AI

Type something like this in the Claude Code input field:

```
请看一下这个截图，告诉我这个错误是什么意思，怎么解决：
/workspaces/my-project/screenshots/error-message.png

```

AI will "look at" the image and answer your question.

---

## Hands-On Exercise

**Goal:** Get Claude Code to interpret a screenshot of your interface

**Steps:**

1. **Take a screenshot:** Capture anything on your current Codespace screen — the file tree on the left, for example
2. **Upload it:** In the Codespace Explorer panel, right-click a folder → Upload, and upload your screenshot
3. **Copy the path:** Right-click the uploaded screenshot → Copy Path
4. **Ask AI:** Type the following in Claude Code:

```
请看一下这个截图，告诉我截图里显示的是什么界面：[paste the path you copied]

```

5. Press Enter to send

**Expected result:** AI will describe what it sees in the screenshot — something like "This is the VS Code file explorer panel showing your project's file structure..."

---

## Screenshot Best Practices

**Keep it sharp:**

- Make sure all text is legible
- Don't crop too tightly — important details should be easy to read

**Keep it focused:**

- Capture only the relevant area, not your entire screen
- If it's an error message, screenshot just the error dialog — not the whole IDE

**Name files descriptively:**

- Use meaningful names like `` error-npm-install.png ``
- Avoid default names like `` Screenshot 2024-01-15 at 10.30.45.png ``

---

## Quick Recap

- Screenshot → upload to Codespace → copy the path → send it to AI
- AI can read images — error messages, UI elements, code, and more
- A screenshot beats a thousand words: faster and more precise than trying to describe what you see

In the next article, we'll learn how to tell AI exactly where to write its output.