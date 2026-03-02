# Understanding Context

> Learn what context is, why it matters, and how to manage it effectively to get better results from Gemini CLI.

## Why This Matters

Imagine this: you've been chatting with Gemini CLI for an hour. You've explored a topic in depth, asked follow-up questions, refined your understanding. Then you ask a question about something you discussed 30 minutes ago, and Gemini gives you a vague or slightly off answer.

What happened? You ran into **context pressure**.

Every message you send, every response Gemini gives, every file you reference — it all accumulates in the **context window**. When that window gets crowded, the quality of responses can suffer. Understanding this is the first step to using Gemini CLI effectively over long sessions.

## What Is Context?

In everyday conversation, "context" means the background information that helps someone understand what you're talking about. If you say "it's broken," the other person needs context to know what "it" refers to.

AI works the same way. When you talk to Gemini CLI, it doesn't have memory between sessions. Everything it knows about your current conversation exists in the **context** — the complete text of your conversation so far, plus any files or information you've referenced.

Think of it like a whiteboard in a meeting room:
- At the start, it's clean
- As you discuss things, you write on it
- Everything written helps the conversation
- But the whiteboard has a fixed size

## The Context Window

Gemini has a **context window** — the maximum amount of information it can process at once.

Think of it like RAM on a computer:
- Limited size
- Everything you're actively using takes up space
- When it fills up, performance degrades

Gemini's context window is very large — up to **1,000,000 tokens** with Gemini Flash and Pro models. That's roughly 5x more than many other AI tools. But it's still not infinite.

### What's a Token?

A token is roughly:
- **1 word** in English (approximately)
- **3-4 characters** on average
- A code snippet of 10 lines might be **50-100 tokens**

So 1,000,000 tokens is roughly **750,000 words** — about 10 full-length novels. That's a lot! But in practice, with files and back-and-forth conversation, it fills up faster than you might think.

## What Consumes Context?

Everything in your session takes up space:

```
+--------------------------------------+
| System Prompt (skills/commands)      | ~500 tokens
+--------------------------------------+
| Your first question                  | ~50 tokens
| Gemini's first answer                | ~200 tokens
+--------------------------------------+
| Your second question                 | ~60 tokens
| Gemini's second answer               | ~180 tokens
+--------------------------------------+
| File you asked Gemini to read        | ~1,000 tokens
+--------------------------------------+
| Your third question                  | ~70 tokens
| Gemini's third answer                | ~220 tokens
+--------------------------------------+
| Total in use: ~2,280 tokens          |
| Remaining: ~997,720 tokens (99.8%)   |
+--------------------------------------+
```

This looks tiny — and it is, for three exchanges. But real sessions can grow fast:

- A long conversation (50+ exchanges): **10,000-50,000 tokens**
- Reading a large file: **5,000-20,000 tokens**
- Reviewing multiple files in a project: **50,000-200,000+ tokens**

## Problems with Long Context

### Problem 1: Context Pressure

Even with 1M tokens, context pressure is real. The longer the context:
- Earlier information may become "buried" and less accessible
- The model may lose focus on key details from earlier in the conversation
- Quality of responses can degrade with extremely long contexts

Think of it like a long meeting. Even if you have unlimited time, after 4 hours, people start losing track of what was said at the beginning. The same thing happens with AI — more context doesn't always mean better responses.

**Bottom line:** A larger context window doesn't eliminate the need for good context management habits. It just gives you more room before problems appear.

### Problem 2: Token Waste

When you start a new question but carry 50,000 tokens of old conversation, Gemini has to process all of it — even the parts that aren't relevant anymore.

This means:
- **Slower responses** — more text to process
- **Higher cost** — tokens cost money (or quota) to process
- **Diluted focus** — important information competes with irrelevant history

It's like having a meeting where someone reads the minutes from every previous meeting before discussing today's agenda. Technically complete, but wasteful.

## Why Managing Sessions Matters

This is why session management matters. Use:
- `gemini` — New session = clean context
- `gemini --resume` or `gemini -r` — Continue last session when needed
- `/resume` — Browse and pick from past sessions

**When to start fresh:**
- Switching to a different topic
- Starting a new task
- When responses seem confused or repetitive

**When to resume:**
- Continuing the exact same task from before
- Needing the AI to remember what you were working on
- Multi-step projects that span breaks

## The Solution: Documentation Strategy

Here's the key insight that separates beginners from effective AI users:

> **Context is not memory. Documents are.**

Instead of relying on long conversation history, extract important information into documents. Then start a fresh session and reference those documents.

### How It Works

**Step 1:** Have a productive conversation
```
You: What are some good low-calorie foods that actually taste good?
Gemini: [Detailed recommendations]

You: Which ones are easiest to prepare?
Gemini: [Preparation tips]

You: I think I'll go with these five. How should I organize my weekly meal prep?
Gemini: [Meal prep plan]
```

**Step 2:** Before ending, extract to a document
```
You: Based on our discussion about nutrition, I think the key points are:
- Low-calorie options that taste good
- Easy preparation methods
- My chosen foods to try

Please create a concise markdown document (300-500 words) summarizing the key
recommendations and the foods I decided to try. Format it nicely so I can save
it as docs/nutrition-plan.md.

Gemini: [Generates concise summary markdown]
```

**Step 3:** In the next session, reference the document
```
@docs/nutrition-plan.md
I want to adjust my meal prep schedule. Can you suggest changes based on my plan?
```

(Note: In Gemini CLI you can use `@` to reference files directly)

Now you have a clean context with just the relevant information — no 50,000 tokens of old conversation, just a focused 500-token document.

## How Manual Context Compression Works

Think of documentation as **compression**. You're taking a long, rambling conversation and compressing it into a focused summary.

| Before (raw conversation) | After (document) |
|---|---|
| 50,000 tokens | 500 tokens |
| Includes false starts, tangents | Only final decisions |
| Mixed topics | Focused on one topic |
| Hard to reference later | Easy to reference anytime |

This is exactly what professionals do:
- Meeting notes summarize 1-hour meetings into 1-page docs
- Architecture Decision Records capture decisions without the full debate
- Changelogs summarize dozens of commits into readable summaries

You're applying the same principle to AI conversations.

## When You Need Long Context

Sometimes you genuinely need a long context window — and this is where Gemini's 1M token capacity really shines:

- **Exploring a large codebase** — Reading multiple files to understand architecture
- **Deep research sessions** — Building on many previous exchanges
- **Complex refactoring** — Holding multiple files in context simultaneously

In these cases, don't fight the context. Use it. Gemini's generous context window makes these workflows practical in ways that smaller windows cannot.

The key is knowing the difference:
- **Long context for exploration** — Let it grow naturally
- **Documentation for knowledge** — Compress and save for later

## Hands-on Exercise: Create Your First Documentation

Let's practice the documentation strategy.

### Part A: Have a Conversation (5-8 exchanges)

1. Start a Gemini CLI session: `gemini`
2. Ask: "What are some healthy, low-calorie foods that actually taste good?"
3. Follow up with questions about:
   - Preparation methods
   - Which ones you'd personally try
   - How to organize a weekly plan
4. Have at least 5-8 back-and-forth exchanges

### Part B: Extract to Documentation

After your conversation, ask Gemini:

```
Based on our discussion, please create a concise markdown document
(300-500 words) that summarizes:
- The recommended foods
- Preparation tips
- My weekly plan

Format it as a clean markdown file I can save as docs/my-nutrition-plan.md
```

Save the generated content to `docs/my-nutrition-plan.md`.

### Part C: Test It

1. Open a new session: `gemini`
2. Reference your document:
   ```
   @docs/my-nutrition-plan.md
   I want to make some adjustments to my nutrition plan. What would you suggest?
   ```
3. Notice how Gemini can work with your plan **without** needing the full conversation history

### What You Should Observe

- The new session starts clean — fast and focused
- Gemini understands your plan from the document alone
- You lost nothing important — the key decisions are preserved
- The conversation feels more productive than continuing a long old session

## Quick Reference

- **Context** — Everything Gemini is currently processing
- **Context Window** — Maximum capacity (up to ~1,000,000 tokens for Gemini Flash/Pro)
- **Context Pressure** — Even with 1M tokens, long contexts can bury important information
- **Session Management** — Keep conversations focused; use `gemini -r` to resume, `/resume` to browse
- **Documentation** — Extract key points from conversations into reusable documents
- **Manual Compression** — Ask Gemini to condense important information

## Mentor's Note: Building Sustainable Workflows

The documentation strategy might feel like extra work at first. Why write things down when you can just keep chatting?

Here's why it matters: **context is not memory. Documents are.**

A conversation is temporary. When you start a new session, it's gone. But a document persists. It's searchable, referenceable, and shareable.

The students who develop this habit early get compounding benefits:
- Their projects accumulate useful documentation naturally
- They can onboard new AI sessions instantly with relevant context
- They build a personal knowledge base as a side effect of working

This isn't just an AI skill — it's a professional skill. The best engineers I know are relentless documenters. They write things down not because they have to, but because they know that knowledge compounds when it's captured.

Start small. After your next productive AI conversation, take 2 minutes to ask the AI to summarize the key points into a document. That's it. One small habit that pays off enormously over time.

## Further Reading

- [Gemini Models Overview](https://ai.google.dev/gemini-api/docs/models)
- [Gemini CLI Documentation](https://github.com/google-gemini/gemini-cli)
