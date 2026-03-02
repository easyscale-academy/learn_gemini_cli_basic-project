# Learn Gemini CLI Basic 11 - Learn to Manage Sessions in Gemini CLI

## Objective

Learn how Gemini CLI sessions work, how to manage conversation history, and how to use session commands (`--resume` and `/resume`) to resume or browse past conversations.

Read the tutorial: [Managing Sessions](https://github.com/easyscale-academy/learn_gemini_cli_basic-project/tree/11-Managing-Sessions/)

## Actionable Items

1. Read the tutorial in `README.md`
2. **Practice 1 (Session Isolation):**
   - Start Gemini CLI: `gemini`
   - Tell Gemini: `Let me tell you: my favorite food is cheese burger`
   - Ask: `What's my favorite food?` (Gemini answers correctly)
   - Exit (Ctrl+D or type `exit`)
   - Start again: `gemini`
   - Ask: `What's my favorite food?` (Gemini doesn't remember)

3. **Practice 2 (Resuming with --resume):**
   - Start: `gemini`
   - Tell: `Let me tell you my favorite programming language is Python`
   - Exit
   - Resume: `gemini --resume` (or `gemini -r`)
   - Ask: `What programming language do I like?` (Gemini remembers)

4. **Practice 3 (Browsing with /resume):**
   - Inside Gemini CLI, type `/resume`
   - Browse and select a past session
   - Verify context is restored

5. Leave a comment on this ticket

**Estimated time:** 15-20 minutes

## Key Concepts

- A **session** is a single conversation with all context saved
- Sessions are **isolated** by default (new session = blank slate)
- **`gemini --resume`** or **`gemini -r`** continues your last session
- **`/resume`** (inside CLI) lets you browse and pick from past sessions
- **`gemini --list-sessions`** lists all sessions in the terminal

## Checklist

- [ ] **Read tutorial** - Finished reading README.md
- [ ] **Practice 1** - Experienced session isolation
- [ ] **Practice 2** - Used `--resume` to resume and verified context restored
- [ ] **Practice 3** - Used `/resume` to browse sessions
- [ ] **Understand the concept** - Know the difference between `--resume` and `/resume`
- [ ] **Notify mentor** - Left a comment
