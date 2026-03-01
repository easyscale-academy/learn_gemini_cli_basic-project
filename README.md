# Claude Code Basics (Part 4): Directing AI Output Exactly Where You Want It

## Why This Matters

You ask AI to write some code, it writes the code… now what?

If you don't tell AI where to put the code, you're stuck copying and pasting it yourself. Worse, if AI modifies existing code without clearly explaining what changed, you're left guessing what it actually touched.

**The fix: always tell AI exactly where to write its output, and have it produce a changelog along the way.**

This is a key technique for working with AI effectively — not just getting it to do the work, but getting it to document *what* it did and *why*. That way, you learn something in the process and have a clear trail to look back on.

---

## Specifying the Output Path

When you ask AI to create or modify files, use absolute paths to be explicit:

**Creating a new file:**

```
Write me a simple Python script that prints "Hello World"
Save it to /workspaces/my-project/scripts/hello.py

```

**Modifying an existing file:**

```
Modify /workspaces/my-project/src/config.json
Change the debug field from false to true

```

AI will create or modify the file right where you specified — no manual copy-paste needed.

---

## Having AI Write a Changelog

Here's an incredibly useful practice: **every time AI makes changes, have it write a summary document.**

Why bother?

- **Learning opportunity:** When AI explains what it changed and why, you absorb the underlying principles
- **Traceability:** You can look back later and see exactly what each change was about
- **No more black boxes:** You'll never be in the "AI changed something, but I have no idea what" situation

### How to Do It

Append something like this to your request:

```
After you're done, create a markdown file in /workspaces/my-project/docs/changes/
that documents:
1. Which files you changed
2. What specifically was changed
3. Why you made those changes
4. The underlying concepts or principles involved

```

### Example Request

```
Optimize the database queries in /workspaces/my-project/src/api/user.py
to reduce the number of queries being made.

When you're done, create a file called optimize-user-query.md
in /workspaces/my-project/docs/changes/ that documents:
1. What you changed
2. How you changed it
3. Why these changes improve performance
4. The relevant database query principles

```

AI will:

1. Modify the code file you specified
2. Create a detailed changelog document

---

## Hands-On Exercise: Try It Yourself

**Goal:** Have AI create a file and write an accompanying documentation file

**Steps:**

1. Open Claude Code
2. Enter the following (adjust the project path to match yours):

```
Create a simple Python script:- Save it to /workspaces/[your-project-name]/scripts/greet.py- It should accept a name as an argument and print "Hello, [name]!"Then create a file called greet-script-notes.md in /workspaces/[your-project-name]/docs/ that explains:1. What this script does2. How to run it3. What Python concepts the code uses

```

3. Press Enter to send

**What you should see:**

- AI creates the `` greet.py `` script
- AI also creates the `` greet-script-notes.md `` documentation file
- Both new files appear in your file browser

---

## Building a Changelog Habit

I recommend creating a dedicated folder in your project for changelogs:

```
my-project/
├── src/           # Source code
├── docs/          # Documentation
│   └── changes/   # AI changelogs ← this is the one
├── scripts/       # Scripts
└── ...

```

Every time AI makes a significant change, have it create a record in `` docs/changes/ ``.

**Naming suggestions:** Use dates or task names, for example:

- `` 2024-01-15-fix-login-bug.md ``
- `` optimize-database-query.md ``
- `` add-user-authentication.md ``

---

## The Complete AI Collaboration Workflow

Putting it all together, here's the full workflow for collaborating with AI effectively:

1. **Input — Give AI the context it needs:**
- Use file paths so AI can read the relevant code
- Use URLs so AI can read reference documentation
- Use screenshots so AI can see the UI or error messages
2. **Process — Tell AI what to do:**
- Be explicit about the task
- Specify absolute paths for all output files
3. **Output — Have AI document its work:**
- Request a changelog
- Capture what was done, why, and the principles behind it

This way, you're not just getting tasks done efficiently — you're learning along the way and keeping a complete record of everything.

---

## Recap

- Use **absolute paths** to direct AI output to specific locations
- Have AI write **changelog documents** that capture what changed and why
- Set up a `` docs/changes/ `` folder and make documenting changes a habit
- Input → Process → Output: the complete AI collaboration workflow

---

Congratulations — you've finished the Claude Code Basics series!

Here's what you now know how to do:

- ✅ Use file paths to have AI read files
- ✅ Use URLs to have AI read web pages
- ✅ Use screenshots to give AI visual context
- ✅ Direct AI output to specific locations and generate documentation

These are the foundational skills for working with AI. Master them, and your development productivity will take a serious leap forward.