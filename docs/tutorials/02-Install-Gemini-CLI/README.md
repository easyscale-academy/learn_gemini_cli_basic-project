# Installing Gemini CLI with mise: A Step-by-Step Guide to Efficient Tool Management

> Learn how to install Google's Gemini CLI — a free, open-source AI coding agent — using mise for clean, version-managed tooling.

## Overview

In the previous lesson, you learned what a coding agent is and how it differs from a regular chatbot. Now it's time to get one running on your machine. In this lesson, you'll install Gemini CLI — Google's open-source command-line AI agent — using mise, the universal tool manager you already know.

## Learning Objectives

AI coding agents are becoming essential tools for professional developers. The sooner you get one set up and start building muscle memory, the sooner you'll experience the productivity gains firsthand. But how you install a tool matters just as much as which tool you pick — a messy install today means headaches tomorrow.

By the end of this exercise, you will:

1. Understand why mise is preferred over the official `npm install -g` approach for installing Gemini CLI
2. Install Gemini CLI through mise using a pre-configured `mise.toml`
3. Verify that the installation succeeded and Gemini CLI is ready to use

## Prerequisites

- How to use mise (the "package manager for package managers")
- How to work inside a GitHub Codespace
- Completed the previous lesson: "What Is a Coding Agent?"

If you're not yet comfortable with mise, we recommend learning the basics first.

## What You'll Build

By the end of this lesson, you'll have a working Gemini CLI installation managed by mise — ready to launch and start coding with AI assistance.

---

## Key Concepts

### What Is Gemini CLI?

Gemini CLI is Google's free, open-source AI coding agent. It runs directly in your terminal, powered by Google's Gemini model. Unlike a chatbot you visit in a browser, Gemini CLI is an **agent** — it can read your files, run commands, debug errors, and search the web, all autonomously.

The official way to install it is via npm:

```
npm install -g @google/gemini-cli
```

This works, but it's a **global install** — and as we'll see, that comes with trade-offs.

### Why Not the Official npm Install?

The `npm install -g` command drops Gemini CLI into a single, fixed location on your machine. That creates a few problems:

1. **Upgrades are manual** — When a new version comes out, you have to remember to run the update command yourself.
2. **Multiple versions don't coexist** — If one project needs a specific older version while another needs the latest, a global install can't handle that.
3. **Uninstalling is messy** — Global npm packages scatter files in system directories, making clean removal tricky.

### Why mise Is Better

Installing with mise is a completely different experience:

1. **Switch versions effortlessly** — Different projects can pin different versions in their own `mise.toml`.
2. **Upgrade in one command** — `mise install` takes care of everything.
3. **Stay tidy** — All your tools live in one managed location. Want to remove something? One command, done.

Since you've already learned mise — your "universal tool manager" — let's use it from the start and save ourselves headaches down the road.

### How mise.toml Declares Your Tools

The magic lives in a simple config file. Open `mise.toml` in this project and you'll see:

```toml
[tools]
gemini = "latest"
```

That's it. This single line tells mise: **this project needs the latest version of Gemini CLI**. You declare what you need, and mise handles the rest — downloading, installing, version-switching, cleanup.

---

## Exercises

### Exercise 1: Fork and Launch the Codespace

**Goal:** Get into the teaching environment with everything pre-configured.

**What to do:**

1. Go to the teaching repository: [https://github.com/easyscale-academy/learn_gemini_cli_basic-project](https://github.com/easyscale-academy/learn_gemini_cli_basic-project)
2. Click the **Fork** button in the upper-right corner to copy it to your own GitHub account.
3. Navigate to your forked repository.
4. Switch to the `02-Install-Gemini-CLI` branch. On the repository page, you'll see a dropdown near the top-left showing the current branch name (likely `main` by default). Click it and select `02-Install-Gemini-CLI`.
5. Click the green **Code** button, go to the **Codespaces** tab, and click **Create codespace on 02-Install-Gemini-CLI**.

**What you'll notice:**

After the Codespace starts, check the bottom-left corner or status bar to confirm you're on the `02-Install-Gemini-CLI` branch. If not, switch before continuing.

> **Key insight:** Always verify you're on the correct branch before doing any work. A wrong branch means a wrong starting point.

---

### Exercise 2: Trust the Config and Activate mise

**Goal:** Tell mise it's safe to use this project's configuration, then activate it.

**What to do:**

1. Confirm mise is available by running:

```
mise
```

If you see help output, you're good. If you see `command not found`, you'll need to install mise first.

2. Trust the config file:

```
mise trust
```

3. Activate mise:

```
mise activate
```

**What you'll notice:**

No dramatic output — and that's fine. These commands work silently.

> **Key insight:** `mise trust` is a safety mechanism. You've downloaded a project from the internet containing a `mise.toml` that could install tools, set environment variables, or run scripts. By running `mise trust`, you explicitly say: "I've reviewed this file — go ahead." You only need to do this once per project. `mise activate` tells mise to monitor the directory and automatically apply config changes — like an assistant that's always on standby.

---

### Exercise 3: Install Gemini CLI

**Goal:** Let mise download and install Gemini CLI as declared in `mise.toml`.

**What to do:**

1. Run the install command:

```
mise install
```

mise reads the `[tools]` section in `mise.toml` and automatically downloads and installs every declared tool — in our case, the latest version of Gemini CLI.

2. Verify the installation:

```
which gemini
```

If you see a path like this:

```
/home/codespace/.local/share/mise/installs/gemini/latest/bin/gemini
```

Congratulations — Gemini CLI is installed!

The exact path may vary, but as long as you see output (rather than `gemini not found`), you're all set.

**What you'll notice:**

The path contains `mise/installs` — this tells you mise is managing the installation, not a global npm install.

> **Key insight:** mise's "smart reuse" means if you have 10 projects all needing Gemini CLI at the latest version, mise installs only one copy and lets all 10 projects point to it. When a new version comes out, mise installs it alongside the old one — so older projects that depend on the previous version keep working fine.

---

## Reflection: What Did We Learn?

Let's compare the two approaches side by side:

**Global npm install (`npm install -g @google/gemini-cli`):**

- One version for your entire machine
- Manual upgrades
- Messy uninstall
- No per-project version control

**mise-managed install (`gemini = "latest"` in mise.toml):**

- Per-project version declarations
- One-command upgrades
- Clean, centralized management
- Smart reuse across projects

The pattern is clear: **declarative tooling beats imperative installs**. Instead of running a command and hoping you remember what you installed where, you write down what you need in a config file, and your tool manager handles the rest.

---

## Mentor's Note

**Why this exercise matters:**

I know what you might be thinking — "We spent an entire lesson just to install a tool?" Fair question. But here's the thing: how you set up your tools says a lot about how you'll manage complexity down the road.

The real lesson here isn't about Gemini CLI specifically. It's about the difference between **imperative** and **declarative** approaches to managing your environment.

- **Imperative:** "Run this command to install this thing." You hope you'll remember what you did six months from now.
- **Declarative:** "This config file says what I need." Anyone (including future-you) can look at it and instantly know the project's requirements.

**Key insights:**

- The best tool setup is the one you never have to think about again. mise gives you that by making your tooling reproducible and self-documenting.
- "Reference, don't copy" is a principle that extends far beyond tool management. Google Docs shared links, Git's delta storage, database foreign keys — they all follow the same idea: maintain one source of truth, and point to it from everywhere else.
- Getting comfortable with declarative configuration early in your career pays compound interest. Dockerfiles, CI/CD pipelines, infrastructure-as-code — they all work the same way.

**Next steps:**

Now that Gemini CLI is installed, you're ready to actually use it. In the next lesson, we'll launch Gemini CLI, authenticate with your Google account, and have your first conversation with an AI coding agent right in the terminal.

---

## Quick Reference

**Installation commands:**

```
mise trust        # Trust the project's mise.toml (once per project)
mise activate     # Activate mise monitoring (once per session)
mise install      # Install all declared tools
which gemini      # Verify Gemini CLI is installed
```

**Key files:**

- `mise.toml` - Declares project tools and versions (contains `gemini = "latest"`)

---

## Completion Checklist

- [ ] Forked the teaching repository to your own account
- [ ] Switched to the `02-Install-Gemini-CLI` branch
- [ ] Created a Codespace on the correct branch
- [ ] Confirmed the Codespace is on the right branch
- [ ] Ran `mise` to confirm it's installed
- [ ] Ran `mise trust` to trust the config file
- [ ] Ran `mise activate` to activate mise
- [ ] Ran `mise install` to install Gemini CLI
- [ ] Ran `which gemini` and saw a path in the output
