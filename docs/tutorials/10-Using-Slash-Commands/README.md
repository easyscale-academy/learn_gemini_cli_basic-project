# Using Slash Commands

> Learn how slash commands and skills let you quickly execute pre-built prompt templates without typing long instructions every time.

## Why This Matters

Imagine this: you're working with Gemini CLI and need to do a currency conversion. You know exactly what you want Gemini to do, but the instruction is detailed — specifying exchange rates, formatting rules, calculation steps.

You could type all of that every single time. Or you could type it once, save it as a command, and invoke it with a single line forever after.

That's what slash commands do. They turn complex, multi-paragraph prompts into simple one-line shortcuts. It's the difference between giving someone directions from scratch every time vs. saving the address and saying "take me there."

---

## What Are Slash Commands?

Think of a slash command as a **prompt template shortcut**. It's a quick way to inject pre-written prompts without typing them manually.

Here's how it works:

1. A slash command contains a **prompt template** — detailed instructions for Gemini
2. You type `/command-name arguments` in Gemini CLI
3. Gemini automatically loads the prompt and processes your arguments

**Important:** You don't need to memorize slash commands. When you type `/` and start typing, Gemini CLI shows you a list of available commands.

---

## Gemini CLI's Dual System: Commands + Skills

Gemini CLI has two ways to create reusable prompts:

### Commands (`.gemini/commands/*.toml`)

Commands are TOML files that define slash commands. They use `{{args}}` as a placeholder for user input.

Example: `.gemini/commands/convert-currency.toml`

```toml
[command]
prompt = """You are a currency conversion assistant. Your task is to convert currency amounts accurately using the provided exchange rates.

## Exchange Rates (base currency: USD)

- United States Dollar (USD): 1.00
- Euro (EUR): 0.92
- British Pound Sterling (GBP): 0.79
- Chinese Yuan Renminbi (CNY): 7.22
- Japanese Yen (JPY): 155.50

## Instructions

When the user asks: {{args}}

1. Parse the amount and currencies from the user's request
2. Convert using the exchange rates
3. Show the result with clear formatting

## Example

Input: "$763.45 USD to EUR"
Output: $763.45 USD = 702.37 EUR (calculation: 763.45 x 0.92 = 702.374)

Be precise with decimal places and round to 2 decimal places."""
```

### Skills (`.gemini/skills/name/SKILL.md`)

Skills are markdown files that provide context and instructions. They're activated through natural language — just mention the skill's purpose and Gemini loads it.

Example: `.gemini/skills/convert-currency/SKILL.md`

```markdown
You are a currency conversion assistant. Your task is to convert currency amounts accurately using the provided exchange rates.

[... same prompt content as above but WITHOUT {{args}} ...]
```

### When to Use Which?

- **Commands** — When you want a quick `/slash-command` shortcut with arguments
- **Skills** — When you want Gemini to have background knowledge available for natural conversations

---

## The `{{args}}` Placeholder

In command TOML files, `{{args}}` is a placeholder that gets replaced with whatever you type after the command name.

For example:

- Command: `/convert-currency How much is $180 USD in Euro?`
- `{{args}}` becomes: `How much is $180 USD in Euro?`

This is how your input flows into the prompt template.

---

## Hands-on Exercise: Practice 1 (Manual Way)

**Goal:** See what it's like to manually type the full system prompt.

**What to do:**

1. Open Gemini CLI in your terminal
2. Copy the entire system prompt below (everything inside the box)
3. Paste it into Gemini CLI

```
You are a currency conversion assistant. Your task is to convert currency amounts accurately using the provided exchange rates.

## Exchange Rates (base currency: USD)

- United States Dollar (USD): 1.00
- Euro (EUR, official common currency of the Eurozone): 0.92
- British Pound Sterling (GBP): 0.79
- Chinese Yuan Renminbi (CNY): 7.22
- Japanese Yen (JPY): 155.50

## Instructions

When the user asks: How much is $180 USD in Euro?

1. Parse the amount and currencies from the user's request
2. Convert the amount using the provided exchange rates:
   - If converting FROM USD: multiply the amount by the target currency rate
   - If converting TO USD: divide the amount by the source currency rate
   - If converting between non-USD currencies: convert to USD first, then to the target currency
3. Provide the result with clear formatting, showing:
   - The original amount and currency
   - The converted amount and currency
   - The calculation used (optional, for transparency)

## Example

Input: "$763.45 USD to EUR"
Output: $763.45 USD = 702.37 EUR (calculation: 763.45 x 0.92 = 702.374)

Be precise with decimal places and round to 2 decimal places for currency amounts.
```

**What you'll notice:**

That's a lot of copying and pasting. It works — Gemini will give you a perfect answer. But imagine doing this every time you need a currency conversion. That's where slash commands save the day.

---

## Hands-on Exercise: Practice 2 (Using Slash Command)

**Goal:** Do the exact same thing, but with a slash command.

**What to do:**

1. In Gemini CLI, simply type:

```
/convert-currency How much is $180 USD in Euro?
```

2. Press Enter

**What you'll notice:**

You get the same high-quality answer as Practice 1, but you typed one line instead of a wall of text. The slash command loaded the entire system prompt for you and plugged in your question where `{{args}}` was.

**Compare Practice 1 vs Practice 2** — same result, a fraction of the effort.

---

## How Slash Commands Work Behind the Scenes

When you type `/convert-currency How much is $180 USD in Euro?`, here's what Gemini CLI does:

1. Searches for matching commands in `.gemini/commands/`
2. Shows autocomplete suggestions as you type
3. Loads the prompt from the matching TOML file (`convert-currency.toml`)
4. Replaces `{{args}}` with your input (`How much is $180 USD in Euro?`)
5. Sends the assembled prompt to the AI model
6. Returns the response

It's just automation — nothing magical. The slash command is a shortcut for something you could do manually (and just did in Practice 1).

---

## Why We're Starting Simple

This currency converter example is deliberately simple. We're using slash commands to do something straightforward so you understand the mechanics clearly.

But here's the thing: slash commands and skills are the gateway to much more powerful workflows. In later lessons, you'll use them to:

- Automate code reviews
- Generate documentation
- Run multi-step analysis workflows
- Create project-specific assistants

What you're learning now — the pattern of saving prompts and invoking them quickly — is the foundation for all of that. This is maybe 10% of what the system can do. Master this 10% first, and the rest will come naturally.

---

## Quick Reference

- **Autocomplete:** Type `/` to see available commands
- **Syntax:** `/command-name arguments`
- **View a command:** `cat .gemini/commands/[command-name].toml`
- **View a skill:** `cat .gemini/skills/[skill-name]/SKILL.md`
- **Concept:** Commands = prompt templates + quick `/` access; Skills = background context for natural language
- **Benefit:** Execute complex workflows with minimal typing

---

## Mentor's Note: Automating Repetitive Workflows

Every experienced developer eventually learns the same lesson: if you do something more than twice, automate it.

Slash commands are one of the simplest forms of automation. You're taking a prompt you'd type repeatedly and saving it once. That's it. No fancy scripting, no complex setup — just a TOML file with your instructions.

But this simple habit compounds. When you start creating commands for your own workflows — code reviews, documentation generation, debugging patterns — you'll notice something: you're not just saving keystrokes. You're encoding your best practices into reusable templates.

The developers who get the most out of AI tools aren't the ones who type the longest prompts. They're the ones who build a library of well-crafted commands and skills that capture their expertise. Start building yours today.

---

## Further Reading

- [Gemini CLI Documentation](https://github.com/google-gemini/gemini-cli)
