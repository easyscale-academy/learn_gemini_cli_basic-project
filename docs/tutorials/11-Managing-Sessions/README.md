# Managing Sessions

> Learn how Gemini CLI sessions work and how to manage conversation history across multiple conversations.

## Why This Matters

Imagine you've been working with Gemini CLI for thirty minutes, building up context about your project. You've explained your architecture, discussed a tricky bug, and you're close to a solution. Then your terminal crashes. Or you need to step away for lunch.

Without session management, all that context is gone. You'd have to start over, re-explaining everything from scratch.

With sessions, Gemini CLI automatically saves your conversation. You can pick up exactly where you left off — no re-explaining, no lost context. It's like having a notebook that remembers everything, even when you close it.

---

## What Are Sessions?

A **session** is a single conversation with Gemini CLI, including everything you've said and everything Gemini has responded. Think of it like a page in a notebook:

- Each time you start Gemini CLI, you get a **new page** (a new session)
- Everything you discuss goes on that page
- When you exit, the page is saved automatically
- Next time you start, you get a fresh page — unless you choose to flip back to a previous one

---

## Understanding Session Persistence

Here's the key thing to understand: **sessions are isolated by default**. Each new session starts with a blank slate.

**Session 1:**
```
                        Let me tell you: my favorite food is pizza
Got it! Your favorite food is pizza. I'll remember that.

                        What's my favorite food?
Your favorite food is pizza.
(Exit Gemini CLI - Session saved)
```

**Session 2:** (New session, fresh start)
```
                        What's my favorite food?
I don't know what your favorite food is. We haven't discussed this.
```

This is by design. Each new session is independent, which means:
- Gemini won't accidentally mix up context from different tasks
- You get a clean starting point every time
- Previous conversations don't slow things down

But when you *want* continuity, you can resume a previous session.

---

## Session Commands

### Command Mapping Table

**IMPORTANT:** Gemini CLI's flags work differently from some other CLI tools. Here's a clear mapping:

| Action | Gemini CLI | What It Does |
|--------|-----------|--------------|
| Start new session | `gemini` | Opens a fresh conversation |
| Continue last session | `gemini --resume` or `gemini -r` | Resumes where you left off |
| Browse past sessions | `/resume` (inside CLI) | Interactive session picker with search |
| List all sessions | `gemini --list-sessions` | Shows session history in terminal |
| Exit | `Ctrl+D` or type `exit` | Saves and exits current session |

### `--resume` / `-r` — Continue Last Session

```bash
gemini --resume
# or shorter:
gemini -r
```

This **continues** the last session you were in. All the context from your previous conversation comes back. Use this when you step away and want to pick up where you left off.

**When to use it:**
- You closed the terminal by accident
- You took a break and want to continue
- You need to follow up on something from your last conversation

### `/resume` — Browse Session History (Inside CLI)

While inside Gemini CLI, type:
```
/resume
```

This shows an interactive list of all your past sessions. You can:
- **Search** through sessions to find a specific conversation
- **Select** any past session to resume it
- **Delete** sessions you no longer need

**When to use it:**
- You want to go back to a conversation from yesterday or last week
- You remember discussing something but can't recall which session
- You want to clean up old sessions

### `--list-sessions` — View Session History

```bash
gemini --list-sessions
```

This prints a list of your sessions directly in the terminal, without entering the CLI. Useful for a quick overview of your session history.

---

## Hands-on Exercise 1: Understanding Session Isolation

**Goal:** Experience how sessions are independent by default.

**Part A — Within a session:**

1. Start Gemini CLI:
   ```bash
   gemini
   ```
2. Tell Gemini:
   ```
   Let me tell you: my favorite food is cheese burger
   ```
3. Ask:
   ```
   What's my favorite food?
   ```
4. Gemini should answer correctly: "cheese burger"

**Part B — Across sessions:**

5. Exit Gemini CLI (press `Ctrl+D` or type `exit`)
6. Start a fresh session:
   ```bash
   gemini
   ```
7. Ask:
   ```
   What's my favorite food?
   ```
8. Gemini **doesn't remember** — it has no context from the previous session

**What you learned:** Each new session starts with a blank slate. Context doesn't carry over automatically.

---

## Hands-on Exercise 2: Resuming with `--resume`

**Goal:** Use `--resume` to continue a previous session.

**Part A — Create a session with context:**

1. Start Gemini CLI:
   ```bash
   gemini
   ```
2. Tell Gemini:
   ```
   Let me tell you my favorite programming language is Python
   ```
3. Exit (press `Ctrl+D` or type `exit`)

**Part B — Resume and verify:**

4. Resume the last session:
   ```bash
   gemini --resume
   ```
   (or shorter: `gemini -r`)
5. Ask:
   ```
   What programming language do I like?
   ```
6. Gemini **remembers** — the context from your previous conversation is restored!

**What you learned:** The `--resume` flag continues your last session with all context intact.

---

## Hands-on Exercise 3: Browsing with `/resume`

**Goal:** Use the interactive session browser to find and resume a past session.

1. Start Gemini CLI:
   ```bash
   gemini
   ```
2. Type the command:
   ```
   /resume
   ```
3. Browse through your past sessions in the interactive picker
4. Select an earlier session (like the one where you mentioned your favorite food)
5. Verify that the context from that session is restored by asking a question about it

**What you learned:** The `/resume` command gives you a visual way to browse all your sessions, search through them, and pick any one to continue.

---

## Quick Reference

- **New session:** `gemini` (default)
- **Continue last session:** `gemini --resume` or `gemini -r`
- **Browse sessions (inside CLI):** `/resume`
- **List sessions:** `gemini --list-sessions`
- **Exit:** `Ctrl+D` or type `exit`
- **Session storage:** Automatic
- **Context isolation:** Each new session starts fresh unless you resume

---

## Common Scenarios

### Scenario 1: "I was debugging something yesterday"
You remember making progress on a bug yesterday but didn't finish. Use `gemini --resume` to jump back into that conversation, or use `/resume` inside the CLI to browse through your sessions and find the right one.

### Scenario 2: "I need to start fresh"
You've been going back and forth, and the conversation has gotten confused. Simply exit and start a new session with `gemini`. Clean slate, fresh start.

### Scenario 3: "Which session had that discussion?"
You discussed something important a few days ago but aren't sure which session it was in. Start Gemini CLI and type `/resume` to browse through your session history. The interactive browser lets you search and preview sessions.

---

## Mentor's Note: Organizing Your Thinking

Session management might seem like a small feature, but it reflects something deeper about how professionals work.

Good developers don't just write code — they organize their thinking. They know when to start fresh and when to build on previous work. They keep context when it's valuable and clear it when it's getting in the way.

Here's my advice:

- **Start a new session for each distinct task.** Working on a bug? New session. Switching to a feature? New session. This keeps your conversations focused and your context clean.
- **Resume when you're continuing the same work.** If you're picking up where you left off on the same task, resume. The context you've already built up is valuable.
- **Don't be afraid to start over.** If a conversation has gotten confusing or gone off track, a fresh session is often more productive than trying to correct course.

The best engineers I know are intentional about their tools. They don't just use features — they think about *when* and *why* to use them.

---

## Further Reading

- [Gemini CLI Documentation](https://github.com/google-gemini/gemini-cli)
