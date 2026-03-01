# Installing Claude Code with mise: A Step-by-Step Guide to Efficient Tool Management

## 📋 What You'll Learn

- Why mise is the recommended way to install Claude Code
- How to get Claude Code up and running through mise
- How to verify that everything worked

## 🎯 Why Does This Matter?

Claude Code is Anthropic's command-line AI coding assistant — it lives right in your Terminal and can help you write code, debug, and refactor. Since we know it's that powerful, let's give it a spin!

The first step? Getting it installed.

## 📝 Prerequisites

This tutorial assumes you're already familiar with:

- How to use mise (the "package manager for package managers")
- How to work inside a GitHub Codespace

If you're not yet comfortable with mise, we recommend learning the basics first.

## 📖 Why Not the Official Install Command?

You may have seen this on the [Claude Code website](https://claude.ai/download/claude-code):

```
curl -fsSL https://claude.ai/install-cli.sh | sh

```

It works fine, but we **don't recommend** it. Here's why:

**The official command performs a "global install"** — it drops Claude Code into a fixed location on your machine. That creates a few problems:

1. **Upgrades are a hassle** — When a new version comes out, you have to deal with it manually.
2. **Multiple versions don't coexist** — If an older project needs an older Claude Code while a newer project needs the latest, a global install simply can't handle that.
3. **Uninstalling is messy** — The official script scatters files across your system, making a clean removal difficult.

**Installing with mise is a different story entirely:**

1. **Switch versions effortlessly** — Different projects can pin different versions.
2. **Upgrade in one command** — mise takes care of everything.
3. **Stay tidy** — All your tools live in one place. Want to remove something? Done.

Since we've already learned mise — our "universal tool manager" — let's do things the right way from the start and save ourselves headaches down the road.

## 💻 Hands-On: Installing Claude Code with mise

We've prepared a teaching repository with a pre-configured `` mise.toml `` file.

### Preparation: Fork the Teaching Repository

1. Go to the teaching repository: [https://github.com/MacHu-GWU/learn_claude_code_basic-project](https://github.com/MacHu-GWU/learn_claude_code_basic-project)
2. Click the **Fork** button in the upper-right corner to copy it to your own GitHub account.
3. Navigate to your forked repository.
4. Switch to the `` 01-install-and-configure-claude-code `` branch.

On the repository page, you'll see a dropdown near the top-left showing the current branch name (likely `` main `` by default). Click it and select `` 01-install-and-configure-claude-code ``.

### Launch the Codespace

Once you're on the correct branch, click the green **Code** button, go to the **Codespaces** tab, and click **Create codespace on 01-install-and-configure-claude-code**.

> **Important:** After the Codespace starts, check the bottom-left corner or status bar to confirm you're on the `` 01-install-and-configure-claude-code `` branch. If not, switch before continuing.

### First, a Look at mise.toml

Before touching anything, let's peek at the key file in this project. Open `` mise.toml `` and you'll see something like this:

```
[tools]
claude = "latest"

```

That's it! This single line says: **this project needs the latest version of Claude Code**.

This is where mise shines — you declare "I need this tool at this version" in a config file, and mise handles the installation, management, and switching for you.

### Step 1: Confirm mise Is Installed and Trust the Config

If this is a freshly created Codespace, first verify that mise is available:

```
mise

```

If you see help output, you're good. If you see `` command not found ``, you'll need to install mise first.

Then run the trust command:

```
mise trust

```

**What does **`` mise trust ``** do?**

Think about it: you've just downloaded a project from the internet, and it contains a `` mise.toml `` config file. That file could tell mise to install tools, set environment variables, run scripts… If mise executed all of that without asking, what happens when the config contains something malicious?

That's why mise has a **safety mechanism**: you need to explicitly tell it, "I trust this file — go ahead and do what it says." That's `` mise trust ``.

You only need to do this once per project.

### Step 2: Activate mise

```
mise activate

```

**What does "activate" mean?**

`` mise activate `` tells mise: "Keep an eye on this directory — whenever `` mise.toml `` changes, apply the updates automatically."

Think of it this way:

- Before activation, mise is a butler you have to summon every single time.
- After activation, mise becomes an assistant that's always on standby, responding on its own.

Activation persists until you delete the Codespace (essentially a fresh start). You only need to do it once per project.

### Step 3: Install the Tools

Now run:

```
mise install

```

mise reads the `` [tools] `` section in `` mise.toml `` and automatically downloads and installs every declared tool — in our case, the latest version of Claude Code.

**Smart Reuse**

Here's an important advantage worth calling out: **mise reuses installations intelligently to save disk space**.

Say you have 10 projects that all need Claude Code at the latest version. mise won't install 10 separate copies — it installs one and lets all 10 projects point to it.

What if the latest version gets updated? mise installs the new one (so briefly you'll have two), but the old one can be easily cleaned up. And if some older project still depends on the previous version, it keeps working just fine.

### Step 4: Verify the Installation

```
which claude

```

If you see a path like this:

```
/home/codespace/.local/share/mise/installs/claude/latest/bin/claude

```

🎉 **Congratulations — Claude Code is installed!**

The exact path may vary, but as long as you see output (rather than `` claude not found ``), you're all set.

## 👨‍🏫 Mentor's Note: From "Copying" to "Referencing" — A Mental Upgrade

Now that installation is behind us, let's step back and talk about a deeper concept: **the version management dilemma**, and how mise solves it elegantly.

### The Problem with Global Installs

The traditional global install approach (like the `` curl ... | sh `` command) has a fundamental limitation: **your entire machine can only have one version**.

In practice, this causes real headaches:

- Project A needs Python 3.9 (a dependency doesn't support newer versions)
- Project B needs Python 3.11 (it uses newer language features)
- Project C needs Python 3.12 (it's a brand-new project)

If you can only have one version globally, what do you do? Reinstall every time you switch projects? Obviously impractical.

### The Waste of Per-Project Installs

What about the opposite — every project installs its own copy?

The problem: many projects need the exact same version. If 20 projects all use Python 3.11, do you really want 20 identical copies? That's a massive waste of disk space.

### mise's Solution: Reference, Don't Copy

mise's core philosophy is: **keep one physical copy, and have everything else reference it**.

- Claude Code latest? One copy on disk.
- 10 projects need it? They all point to that same copy.
- New version released? Install it alongside the old one (some projects might still need it).
- Done with the old version? Clean it up with a single command.

This "one copy, many references" mindset will serve you well beyond just tool management.

### Where Else This Thinking Applies

Even outside software engineering, this mental model is remarkably useful.

Think about how many situations work the same way:

- **One document used in multiple places** — Do you make 10 copies, or keep one and link to it everywhere?
- **Preserving version history** — Do you make a full backup each time, or just save what changed?
- **Multiple people collaborating** — Does everyone keep a separate copy, or does everyone edit the same one?

Modern cloud storage, version control, and knowledge management tools all rely on this idea under the hood:

- Google Docs shared links (one document, many viewers)
- Git's delta storage (only the diffs)
- Notion's database relations (references, not duplicates)

What mise teaches us isn't just how to install tools — it's a way of thinking about managing resources efficiently.

## ✅ Completion Checklist

- [ ] Forked the teaching repository to your own account
- [ ] Switched to the `` 01-install-and-configure-claude-code `` branch
- [ ] Created a Codespace on the correct branch
- [ ] Confirmed the Codespace is on the right branch
- [ ] Ran `` mise `` to confirm it's installed
- [ ] Ran `` mise trust `` to trust the config file
- [ ] Ran `` mise activate `` to activate mise
- [ ] Ran `` mise install `` to install Claude Code
- [ ] Ran `` which claude `` and saw a path in the output

## 💡 Key Takeaways

1. **Use mise for Claude Code** — More flexible and cleaner than the official global install.
2. **mise.toml declares your tooling** — List what you need and at what version under `` [tools] ``.
3. **Three steps: trust → activate → install** — Trust the config, activate monitoring, install the tools.
4. **Smart reuse** — Identical versions are stored once, saving disk space.
5. `` which claude ``** to verify** — If you see a path, you're all set.