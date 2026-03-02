# Editing Long Messages

> Learn how to compose and edit long messages efficiently using a markdown file instead of the chat input box.

## Why This Matters

Imagine this: you want to ask Gemini CLI a detailed question. You start typing in the terminal, but it gets awkward fast. You make a typo three lines up and have to retype everything. Or you want to include a code snippet, a file path, and specific instructions — all in one prompt.

Typing long, thoughtful prompts directly in the terminal is frustrating. You lose your train of thought. You can't easily edit what you've written. And once you send it, it's gone — you can't reuse or refine it.

The solution? **Compose your messages in a file first, then paste them into Gemini CLI.** This simple workflow change makes a huge difference in how effectively you communicate with the AI.

## The Message File Approach

Instead of typing directly in Gemini CLI, create a file called `.gemini/gemini-messages.md` in your project. This file serves as your "drafting space" for prompts.

Here's how it works:

1. **Open** `.gemini/gemini-messages.md` in your editor
2. **Write** your message at the bottom of the file, below a separator line
3. **Copy** the message
4. **Paste** it into Gemini CLI
5. **Keep** the file open — your message history stays there for reference

The file acts as a scratchpad. You can see your past prompts, refine your current one, and build up complex requests without fighting the terminal.

### Why a file in `.gemini/`?

The `.gemini/` directory already exists in your project for configuration. Putting your message file here keeps things organized. It's also easy to `.gitignore` if you don't want your drafts in version control.

## Additional Input Methods

Gemini CLI also provides built-in ways to write longer messages without leaving the terminal:

### Shift+Enter / Ctrl+Enter — Multiline Input

Press **Shift+Enter** or **Ctrl+Enter** in the Gemini CLI prompt to start a new line without sending the message. This lets you type multi-line prompts directly in the terminal.

This is great for quick multi-line messages — like when you need two or three lines but don't want to open a file.

### Ctrl+X — Open External Editor

Press **Ctrl+X** to open your default text editor (set by the `$EDITOR` environment variable). Write your full message in the editor, save and close it, and the content is sent to Gemini CLI.

This is ideal for longer, more structured prompts. If you're used to Vim, VS Code, or Nano, this feels natural.

### When to Use Which?

| Method | Best For |
|--------|----------|
| Type directly | Quick, single-line questions |
| Shift+Enter | 2-3 line prompts, quick formatting |
| Ctrl+X | Longer structured prompts, one-off detailed questions |
| Message file | Reusable prompts, maintaining history, complex multi-part instructions |

The message file approach is still the most valuable for serious work — it gives you a history of your prompts and lets you refine them over time.

## Writing from Top to Bottom

When using the message file, always write new messages at the **bottom** of the file. Use separator lines (like `---` or a row of dashes) to visually separate different prompts.

```markdown
------------------------------------------------------------------------------
My first message goes here.
------------------------------------------------------------------------------
My second, refined message goes here.
------------------------------------------------------------------------------
My latest message is at the bottom, ready to copy.
------------------------------------------------------------------------------
```

This way, your file becomes a log of your thinking. You can scroll up to see how your prompts evolved, and the latest one is always at the bottom, ready to copy.

## Referencing Files in Your Messages

When composing prompts in your message file, you can reference project files that you want Gemini to read. In Gemini CLI, use `@` followed by the relative path to include a file's contents:

```
@src/main.py Please review this file and suggest improvements.
```

You can reference multiple files:

```
@src/utils.py @src/config.py Compare these two files and explain how they interact.
```

When you paste this into Gemini CLI, it will read the referenced files and include their contents in the conversation.

**Tip:** Write these file-referencing prompts in your message file first. That way you can double-check the paths before sending.

## Clearing Input and Exiting

A few keyboard shortcuts to know:

- **Ctrl+C** — Cancel the current generation or clear your current input
- **Ctrl+D** or type `exit` — Exit Gemini CLI
- **Starting fresh** — Just run `gemini` again to start a new session

Unlike some tools, Ctrl+C in Gemini CLI cancels the current operation rather than quitting. Use Ctrl+D or type `exit` when you want to leave.

## Hands-on Exercise

Let's practice the message file workflow:

1. Open `.gemini/gemini-messages-example.md` in your editor
2. Look at the structure — notice the separator lines and the sample message at the bottom
3. Copy the sample message (the text between the last two separator lines)
4. Open Gemini CLI in your terminal
5. Paste the message and press Enter
6. Observe how Gemini responds

Now try it yourself:

7. Go back to the example file
8. Below the last separator, write your own message — something specific about this project
9. Copy and paste it into Gemini CLI
10. Notice how much easier it is to compose a thoughtful prompt in your editor

**Bonus:** Try pressing Ctrl+X in Gemini CLI to open your external editor. Write a message there, save, and close — watch it get sent automatically.

## Common Issues

### "My paste doesn't work in the terminal"
Some terminal emulators handle paste differently. Try Ctrl+Shift+V (Linux), Cmd+V (Mac), or right-click to paste. In VS Code's integrated terminal, Ctrl+Shift+V usually works.

### "The message is too long"
Gemini CLI can handle very long prompts, but if you're hitting limits, break your request into smaller, focused questions. This usually gives better results anyway.

### "I lost my message after sending it"
This is exactly why the message file approach is valuable. Your drafts stay in the file even after you paste and send them. You never lose your work.

### "Ctrl+X doesn't open my editor"
Make sure you have the `$EDITOR` environment variable set. For example, add `export EDITOR=nano` (or `vim`, `code --wait`, etc.) to your shell profile (`.bashrc`, `.zshrc`).

## Mentor's Note: Thoughtful Communication

Here's something that might surprise you: **the quality of your prompts matters more than the quality of the AI model.**

A well-composed, specific prompt sent to a fast model will almost always outperform a vague, rushed prompt sent to a powerful model. The time you spend drafting your message is an investment that pays off immediately.

The message file approach isn't just a convenience trick — it's a mindset shift. When you write your prompts in an editor, you naturally:

- Think more carefully about what you're asking
- Provide more context
- Structure your requests more clearly
- Review before sending

These are the same skills that make you a better communicator with humans — in code reviews, documentation, and team discussions. Practicing thoughtful communication with AI is practicing thoughtful communication in general.

**The best prompt is the one you took time to think about.**

## Quick Reference

**Message file location:**
```
.gemini/gemini-messages.md
```

**Multiline input in terminal:**
```
Shift+Enter or Ctrl+Enter
```

**Open external editor:**
```
Ctrl+X
```

**Cancel current generation:**
```
Ctrl+C
```

**Exit Gemini CLI:**
```
Ctrl+D or type "exit"
```

**Reference a file in your prompt:**
```
@path/to/file.py Explain this file
```

**Key files:**
- `.gemini/gemini-messages.md` — Your draft space for composing prompts
- `.gemini/gemini-messages-example.md` — Example message file to get started

## Further Reading

- [Gemini CLI GitHub Repository](https://github.com/google-gemini/gemini-cli)
- [Gemini CLI Documentation](https://googlegemini.github.io/gemini-cli/)
