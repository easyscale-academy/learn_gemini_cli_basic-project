# Read Files with @ in Gemini CLI

## Objective

Learn how to use the `@` symbol with relative file paths in Gemini CLI to have the AI read and analyze your project files. This is the most fundamental skill for collaborating with an AI coding agent.

Read the tutorial: [Gemini CLI Basics: Getting AI to Read Your Files with @](https://github.com/easyscale-academy/learn_gemini_cli_basic-project/tree/04-Read-Files)

## Actionable Items

1. Read the tutorial (`@README.md`) to understand the `@` file referencing syntax
2. Open Gemini CLI and complete all four exercises in the tutorial
3. Work through every item in the Checklist below

**Estimated time:** 10-15 minutes

## Checklist

- [ ] **Read the tutorial** — Understand the difference between absolute and relative paths, and why Gemini CLI uses `@` + relative paths
- [ ] **Master Copy Relative Path** — In the Codespace Explorer panel, right-click any file and use "Copy Relative Path" (not "Copy Path")
- [ ] **Exercise 1: Read a single file** — Run `Summarize what this file is about: @README.md` in Gemini CLI and get a summary back
- [ ] **Exercise 2: Ask a specific question** — Use `@` to reference a file and ask a targeted question about its contents
- [ ] **Exercise 3: Reference multiple files** — Use two or more `@` references in a single prompt
- [ ] **Exercise 4: Summarize the tutorial** — Run `summarize @README.md` and confirm the summary matches what you learned

## Submission & Verification

When you're done, run `/teach-check` to verify your work against the checklist. Say "ship it" when complete to generate RESULT.md, then share the RESULT.md file GitHub link with your instructor.

## Grading Rubric

> **For instructors and /teach-check assistant** — Students may skip this section.

- **@ syntax understanding:** Student can explain that `@` + relative path tells Gemini CLI to read a file. They understand why relative paths (not absolute) are used in Gemini CLI.
- **Copy Relative Path skill:** Student used "Copy Relative Path" from the Codespace context menu (not "Copy Path"). They can demonstrate this on any file.
- **Single file reference:** Student successfully ran a prompt with `@README.md` (or another file) and received a content-based response from Gemini CLI.
- **Targeted question:** Student asked a specific question about a file using `@` and got an answer grounded in the file's actual contents (not a generic response).
- **Multiple file references:** Student used two or more `@` references in one prompt and Gemini read both files to produce a combined response.
- **Self-summary exercise:** Student ran `summarize @README.md` and can confirm the AI's summary reflects the tutorial content.
