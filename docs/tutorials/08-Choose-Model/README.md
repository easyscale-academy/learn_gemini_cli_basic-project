# Choosing Your Gemini Model

> Learn how to select the right AI model in Gemini CLI to balance capability and cost.

## Why This Matters

Imagine this: you're in the middle of a productive learning session with Gemini CLI. You're asking great questions, making real progress. Then you notice responses getting slower, or you check your Google AI Studio dashboard and realize you've burned through a surprising amount of your free quota.

This happens because different models consume resources at very different rates. The most powerful model isn't always the right choice — especially when you're learning, experimenting, or doing straightforward tasks.

The good news? Gemini CLI lets you choose your model. By picking the right one for each task, you get faster responses, lower costs, and a smoother workflow.

## Understanding the Gemini Models

Gemini CLI gives you access to several models. Think of them as colleagues with different strengths:

- **Gemini 2.5 Pro** is your senior architect. It handles complex reasoning, multi-step analysis, and tasks that require deep understanding across large codebases. It has a massive 1M token context window. Powerful, but it costs more and responds slower. Save it for when you truly need it.

- **Gemini 2.5 Flash** is your go-to senior engineer. It's fast, capable, and cost-effective — roughly 8x cheaper than Pro for input tokens. Flash handles most coding tasks, explanations, and learning conversations with ease. This is your default choice.

- **Gemini 2.5 Flash-Lite** is your quick-response teammate. The fastest and cheapest option, great for simple lookups, formatting tasks, and quick questions where speed matters more than depth.

Here's the key insight: **for learning, Flash is usually more than enough**. It's fast, affordable, and surprisingly capable. Save Pro for genuinely hard problems.

---

## Key Concepts

### The /model Command

Gemini CLI provides an interactive `/model` command to switch models on the fly. Type `/model` in your Gemini CLI session, and you'll see a selection menu. You can choose between:

- **Auto mode** — Gemini intelligently picks Pro or Flash based on task complexity
- **Manual mode** — You pick a specific model yourself

For learning, manually selecting Flash gives you the best balance of capability and efficiency.

### Where Settings Are Stored

When you switch models, Gemini CLI saves your preference. There are two locations:

- **Project-level:** `.gemini/settings.json` in your project directory (overrides user-level)
- **User-level:** `~/.gemini/settings.json` in your home directory (applies globally)

A typical settings file looks like:

```json
{
  "model": "gemini-2.5-flash"
}
```

You can also edit this file directly — just change the model value and save. When Gemini CLI starts, it reads this file and uses your saved preference.

### Command-Line Override

You can also specify a model when launching Gemini CLI without changing your saved settings:

```bash
gemini --model gemini-2.5-flash
```

This is useful when you want to temporarily use a different model for a single session.

---

## Exercises

### Exercise 1: Switch to Flash

**Goal:** Use the `/model` command to switch to Gemini 2.5 Flash.

**What to do:**

1. Open Gemini CLI in your terminal
2. Type `/model` and press Enter
3. When the selection menu appears, choose Flash
4. Ask Gemini a simple question to confirm it's working

**What you'll notice:**

Flash responds quickly and handles learning questions well. For most of what you'll do in this course, Flash is the right choice.

> **Key insight:** The fastest, cheapest model that can handle your task is always the best choice. Don't pay for power you don't need.

---

### Exercise 2: Verify Your Settings

**Goal:** Check where your model preference is stored.

**What to do:**

1. After switching models with `/model`, open `.gemini/settings.json` in your editor
2. Confirm the `model` field shows your selection
3. Try editing the file directly to change the model, then restart Gemini CLI to see the change take effect

**What you'll notice:**

The settings file is plain JSON — simple and human-readable. You can always check or change it manually if needed.

> **Key insight:** Understanding where tools store their configuration gives you more control. When something seems wrong, checking the config file is often the fastest way to debug.

---

## Reflection: What Did We Learn?

Model selection is about matching the tool to the task:

- **Flash** — Your daily driver for learning, coding help, and general questions. Fast and affordable.
- **Pro** — Reserve for complex architectural decisions, deep analysis across large codebases, and problems that genuinely require more reasoning power.
- **Flash-Lite** — Quick tasks where speed is everything and depth doesn't matter.
- **Auto** — Let Gemini decide, useful when you're not sure which model fits.

The habit of choosing the right model extends beyond AI tools — it's about being resourceful with any technology you use.

---

## Mentor's Note

**Why this exercise matters:**

When I started using AI coding tools, I always reached for the most powerful model. Why settle for less, right?

But over time, I learned something important: choosing the right tool for the job is a fundamental engineering skill.

Using Pro to answer a simple question is like driving a truck to buy groceries. It works, but it's wasteful and slower. The best engineers I know are resourceful — they understand constraints and work within them creatively.

**Key insights:**

- Model selection is a daily decision, not a one-time setup. Get comfortable switching based on what you're doing.
- Flash is genuinely capable. Don't underestimate it just because it's cheaper.
- This habit of right-sizing your tools applies everywhere in engineering: choosing the right database, the right framework, the right level of abstraction.

**Next steps:**

As you continue through this course, default to Flash. Switch to Pro only when you hit a problem that Flash can't handle well — you'll develop an intuition for this over time.

---

## Quick Reference

**Switch models:**
```
/model
```

**Launch with a specific model:**
```
gemini --model gemini-2.5-flash
```

**Model capability:** Pro > Flash > Flash-Lite

**Cost:** Pro > Flash > Flash-Lite

**Speed:** Flash-Lite > Flash > Pro

**Key files:**
- `.gemini/settings.json` — Project-level model preference
- `~/.gemini/settings.json` — User-level model preference

## Further Reading

- [Gemini CLI GitHub Repository](https://github.com/google-gemini/gemini-cli)
- [Gemini Models Overview](https://ai.google.dev/gemini-api/docs/models)
