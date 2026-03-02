# Currency Converter App: Your First Vibe Coding Experience

> Build a real app without writing code yourself. Discover why **communication clarity** is the most valuable skill in AI-assisted development.

![Currency Converter App](img/currency-converter.png)

## Overview

In this lesson, you'll experience "vibe coding" — the practice of building software by describing what you want to an AI agent, rather than writing code manually. You'll build a currency converter app three different ways and discover a fundamental truth: **the quality of your input directly determines the quality of AI's output**.

This isn't about learning a programming language. It's about learning to communicate effectively with an AI coding agent — a skill that's becoming as valuable as coding itself.

---

## Learning Objectives

By the end of this lesson, you will:

1. **Experience vibe coding firsthand** — Build a working app by describing what you want
2. **Discover why clear requirements matter** — Compare vague vs. precise instructions
3. **Learn the interview technique** — Use AI to clarify your own fuzzy ideas
4. **Understand the communication bottleneck** — Recognize that "what to build" matters more than "how to build"

---

## Prerequisites

- Gemini CLI installed and authenticated (lessons 02-03)
- Basic familiarity with Gemini CLI commands (lessons 04-08)
- A terminal open in this project directory

---

## What You'll Build

A simple currency converter web app using Python and Streamlit:

- Enter an amount (e.g., 100)
- Select source currency (e.g., USD)
- Select target currency (e.g., EUR)
- See the converted result instantly

The app is intentionally simple — about 30 lines of Python. The focus isn't on the code itself, but on how you communicate what you want.

---

## Reference Implementation

Before starting, see what a polished version looks like:

```bash
# Install dependencies first
mise run inst

# Run the example app
mise run app
# Or directly: streamlit run app-example.py
```

This opens a browser with the working currency converter. Play with it for a minute — enter different amounts, switch currencies, notice the UI elements. This is what you're aiming for.

> **Note:** The reference implementation (`app-example.py`) is provided so you can see the target. Your job is to get Gemini CLI to build `app.py` for you.

---

## Exercises

### Exercise 1: The Vague Approach

**Goal:** Experience what happens when you give AI a vague, one-liner request.

**What to do:**

1. Start Gemini CLI:
   ```bash
   gemini
   ```

2. Use the teaching command with a vague request:
   ```
   /teach-code build me a currency converter
   ```

3. Let Gemini build whatever it interprets from your vague request.

4. Run the result:
   ```bash
   streamlit run app.py
   ```

5. Compare with the reference implementation (`app-example.py`). Notice the differences.

**What you'll discover:**

The AI will build *something* — but it probably won't match what you had in mind. Maybe it's a command-line tool instead of a web app. Maybe it uses different currencies. Maybe it's missing error handling.

This is the core lesson: **vague input produces unpredictable output**. The AI isn't wrong — it just filled in all the gaps you left with its own assumptions.

> **Key insight:** "Build me a currency converter" has hundreds of valid interpretations. When you don't specify what you want, the AI picks for you — and its choices may not match yours.

---

### Exercise 2: The Clear Spec Approach

**Goal:** Experience the dramatic difference when you provide a clear specification.

**What to do:**

1. Start a new Gemini session:
   ```bash
   gemini
   ```

2. This time, point Gemini to the detailed spec file:
   ```
   /teach-code READ app-spec.md to understand the currency converter app requirement, then write the python app at app.py, and teach me how to run it.
   ```

3. Run the result:
   ```bash
   streamlit run app.py
   ```

4. Compare with Exercise 1's result. Notice how much closer this is to the reference implementation.

**What you'll discover:**

With a clear spec (`app-spec.md`), the AI produces something much closer to what you actually wanted. Same AI, same task, dramatically different result — the only difference was the quality of your input.

> **Key insight:** The spec file (`app-spec.md`) is only ~40 lines long. Writing a clear spec takes 5-10 minutes but saves hours of back-and-forth. This is true for human developers too — clarity up front prevents confusion later.

---

### Exercise 3: The Interview Technique

**Goal:** Learn what to do when you don't *know* what you want yet.

This is the most powerful technique in this lesson. Sometimes you have a fuzzy idea — "I want to build something with currencies" — but you haven't figured out the details. Instead of guessing, you can use AI as a brainstorming partner.

**What to do:**

1. Start a new Gemini session:
   ```bash
   gemini
   ```

2. Use the brainstorming command with your fuzzy idea:
   ```
   /teach-brainstorm I want to build a currency converter app but I'm not sure exactly what features it should have or how to structure it
   ```

3. Answer Gemini's questions honestly. It will ask things like:
   - What problem are you solving?
   - Who is the user?
   - What constraints do you have?
   - What are you optimizing for?

4. Let the conversation naturally lead to a clear plan.

5. Once you have a plan, use `/teach-code` to implement it.

**What you'll discover:**

The interview technique turns a fuzzy idea into a concrete plan through conversation. You don't need to have all the answers before you start — you just need to be willing to think through the questions.

> **Key insight:** The interview technique is valuable beyond AI tools. When a colleague says "I want to build X," the best engineers don't start coding — they ask clarifying questions first. This is the same skill.

---

## Key Concepts

### The Communication Bottleneck

In traditional software development, the bottleneck was often "how to implement" — writing code, debugging, understanding frameworks. AI tools remove much of this friction.

But a new bottleneck emerges: **"what to implement."** The AI can build anything you describe clearly. The challenge is describing it clearly.

This is why communication skills — thinking precisely, writing clearly, asking good questions — are becoming as valuable as coding skills.

### The Spectrum of Input Quality

```
Vague input          →  Unpredictable output
↓                        ↓
"build me a thing"   →  "here's a thing (maybe not what you wanted)"

Clear input          →  Predictable output
↓                        ↓
"build X with Y      →  "here's exactly X with Y and Z"
 and Z, using ..."
```

### The Interview Technique

When you don't know what you want:

1. **Start with a fuzzy idea** — "I want to build something with currencies"
2. **Let AI ask questions** — Use `/teach-brainstorm` to start a structured conversation
3. **Answer honestly** — "I'm not sure" is a valid answer
4. **Converge on a plan** — The questions naturally lead to clarity
5. **Execute with clarity** — Now use `/teach-code` with your clear plan

This technique works because the questions force you to think through aspects you might have overlooked.

---

## Reflection

After completing all three exercises, consider:

1. **Which approach produced the best result?** Why?
2. **How long did the spec take to write vs. how much time it saved?**
3. **When would you use each approach?**
   - Vague: Quick experiments, exploration
   - Spec: Known requirements, production code
   - Interview: Unclear requirements, early-stage ideas

The meta-lesson: AI doesn't replace thinking — it amplifies it. Clear thinking produces clear output. Fuzzy thinking produces fuzzy output.

---

## Mentor's Note

**Why this lesson matters more than you think:**

I've watched hundreds of people try AI coding tools for the first time. The pattern is always the same:

1. They type something vague
2. They get something unexpected
3. They either blame the AI ("it's not smart enough") or blame themselves ("I'm not good at this")

Neither is true. The issue is always **the gap between what they imagined and what they communicated**.

This lesson is designed to make that gap visible. When you see Exercise 1's result next to Exercise 2's, the lesson lands viscerally — not as an abstract principle, but as a lived experience.

**The interview technique is the real gem here.** In professional software development, the hardest part is often figuring out what to build. Requirements are fuzzy. Stakeholders disagree. Nobody has the full picture. The ability to ask the right questions — to take a vague idea and turn it into a concrete plan — is one of the most valuable skills in the industry.

You just practiced that skill with an AI as your conversation partner.

**Next steps:**

As you continue through this course, notice when you're being vague vs. clear in your prompts. The more you practice clear communication with AI, the better your results will be — and the better your communication skills will become in general.

---

## Quick Reference

**Start Gemini CLI:**
```bash
gemini
```

**Teaching commands:**
```
/teach-start          # Begin guided learning session
/teach-code           # Write code + get learning notes
/teach-brainstorm     # Clarify fuzzy ideas through conversation
/teach-check          # Verify your work against the checklist
/teach-explain        # Understand code or concepts
/teach-debug          # Debug errors + learn to read stack traces
```

**Run the app:**
```bash
streamlit run app.py           # Your app
streamlit run app-example.py   # Reference implementation
```

**Session management:**
```bash
gemini                # Start new session
gemini -r             # Resume last session
gemini --resume       # Resume last session (alternative)
```

Inside Gemini CLI:
```
/resume               # Browse and resume previous sessions
```

**Chinese commands:** Add `-cn` suffix (e.g., `/teach-code-cn`, `/teach-start-cn`)

## Further Reading

- [Currency Converter App Tutorial](https://github.com/easyscale-academy/learn_gemini_cli_basic-project/tree/13-Currency-Converter-App/)
- [Gemini CLI GitHub Repository](https://github.com/google-gemini/gemini-cli)
- [Streamlit Documentation](https://docs.streamlit.io/)
