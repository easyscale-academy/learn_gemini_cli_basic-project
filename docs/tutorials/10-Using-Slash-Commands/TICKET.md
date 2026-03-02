# Learn Gemini CLI Basic 10 - Learn to Use Slash Commands in Gemini CLI

## Objective

Learn how slash commands and skills let you quickly execute pre-built prompt templates without typing long instructions every time. Understand the dual system of Commands (TOML files) and Skills (markdown files).

Read the tutorial: [Using Slash Commands](https://github.com/easyscale-academy/learn_gemini_cli_basic-project/tree/10-Using-Slash-Commands/)

## Actionable Items

1. Read the tutorial in `README.md`
2. View the command: `cat .gemini/commands/convert-currency.toml`
3. View the skill: `cat .gemini/skills/convert-currency/SKILL.md`
4. **Practice 1 (Manual):** Copy the system prompt from the tutorial, replace `{{args}}` with "How much is $180 USD in Euro?", and paste into Gemini CLI
5. **Practice 2 (Slash Command):** Type `/convert-currency How much is $180 USD in Euro?` into Gemini CLI
6. Compare the two approaches — notice how slash commands reduce typing
7. Leave a comment on this ticket to let your mentor know you've completed it

**Estimated time:** 10-15 minutes

## Key Concepts to Understand

- Slash commands are **shortcuts for prompt templates**
- You don't need to memorize command names — use autocomplete (type `/` and search)
- The `{{args}}` placeholder in TOML commands gets replaced with your input
- Skills provide context via natural language activation
- This is 10% of what the system can do; we'll explore more advanced features later

## Checklist

- [ ] **Read tutorial** - Finished reading the README.md
- [ ] **View command file** - Ran `cat .gemini/commands/convert-currency.toml` and saw the prompt template
- [ ] **View skill file** - Ran `cat .gemini/skills/convert-currency/SKILL.md` and saw the skill content
- [ ] **Practice 1 (Manual)** - Copied the system prompt and manually sent a currency conversion request
- [ ] **Practice 2 (Slash Command)** - Used `/convert-currency` command and compared it with Practice 1
- [ ] **Understand the benefit** - Know why slash commands are faster than typing full prompts
- [ ] **Notify mentor** - Left a comment saying "Done" or describing what you learned
