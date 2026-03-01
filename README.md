# Choosing Your Claude Model

> Learn how to select the right AI model in Claude Code to balance capability and quota usage.

## Why This Matters

Imagine this: you're in the middle of learning, asking Claude Code questions, making good progress. Suddenly, a message pops up — "Quota exhausted. Please wait 5 hours."

Five hours. Your momentum is gone. Your learning session is over.

This happens because Claude Code uses a quota system. Every question you ask consumes quota, and more powerful models consume more. On a Team Plan, your quota is shared among team members, so it can run out faster than you expect.

The good news? You have control. By choosing the right model for your task, you can stretch your quota much further and avoid that frustrating wait.

## Understanding the Three Models

Claude Code offers three models. Think of them as three colleagues with different levels of expertise:

- **Opus** is your industry-top expert: Give it the hardest and most critical problems: deep architectural decisions, unresolved edge-case bugs, and research that requires original reasoning and cross-domain insight. Think of Opus as a Distinguished Engineer / Fellow-level technologist at a top tech company — someone who defines standards, writes whitepapers, and shapes technical direction. Powerful, but best used sparingly.
- **Sonnet** is your Principal-level engineer: It excels at designing and implementing complex systems, writing and reviewing high-quality code, and turning abstract ideas into production-ready solutions. Sonnet maps to a Principal or Senior Staff Engineer — the backbone of serious engineering work and the best choice for most advanced tasks. 
- **Haiku** is your Senior engineer: Ideal for learning, asking questions, and executing well-defined tasks efficiently. Haiku is reliable, clear, and cost-effective — perfect when the problem is understood and execution matters.

Here's the key insight: **for learning, Haiku is usually enough**. Save Opus for when you truly need it.

## How to Switch Models

Switching models in Claude Code takes just a few seconds.

Open Claude Code in your terminal. Type `/model` and press Enter. You'll see a menu with three options. Use your arrow keys to highlight the model you want, then press Enter to confirm.

That's it. Your model is now changed.

You can verify the change by looking at the prompt area — Claude Code displays your current model there.

## Where Settings Are Stored

When you switch models, Claude Code remembers your choice. It saves this preference in a file called `.claude/settings.json` in your project directory.

If you open this file, you'll see something like:

```json
{
  "model": "haiku"
}
```

When you restart Claude Code, it reads this file and uses your saved model. You can also edit this file directly if you prefer — just change the value and save.

This is useful to know because if something seems wrong with your model selection, you can always check this file to see what's actually configured.

## Hands-on Exercise

Let's practice what you've learned.

**Your task:** Switch to Haiku and verify the change.

Start Claude Code in your terminal. Type `/model` and press Enter. When the menu appears, select Haiku. After confirming, check that the prompt area shows Haiku as your current model.

If you want to go further, open `.claude/settings.json` in your editor and confirm that the `model` field shows `haiku`.

## Common Issues

**The model menu doesn't appear after typing `/model`**

Make sure you press Enter after typing the command. The slash command needs to be submitted, not just typed.

**Your model keeps resetting to something else**

Check if `.claude/settings.json` exists and is writable. If the file doesn't exist or Claude Code can't write to it, your preference won't be saved.

**You see a "quota exhausted" message**

Switch to Haiku immediately to reduce consumption. If you're already on Haiku, you'll need to wait for the quota to refresh — typically about 5 hours on a Team Plan.

## Mentor's Note: The Right Tool for the Job

When I started using AI tools, I always reached for the most powerful model. Why settle for less, right?

But over time, I learned something important: choosing the right tool for the job is a fundamental engineering skill.

Using Opus to answer a simple question is like driving a truck to buy groceries. It works, but it's wasteful. The best engineers I know are resourceful — they understand constraints and work within them creatively.

This applies everywhere in engineering: choosing the right database for your use case, the right framework for your project, the right level of abstraction for your code. Start building this habit now, with something as simple as model selection.

## Quick Reference

- `/model` — Opens the model selection menu
- Model capability: Opus > Sonnet > Haiku
- Quota consumption: Opus > Sonnet > Haiku
- Settings file: `.claude/settings.json`

## Further Reading

- [Claude Code Documentation](https://code.claude.com/docs)
- [Understanding Claude Models](https://platform.claude.com/docs/en/about-claude/models/overview)
