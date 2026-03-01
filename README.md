# Gemini CLI Login Guide: Connecting to Your AI Coding Assistant

## Overview

Gemini CLI is Google's open-source command-line AI coding assistant. Before you can start using it, you need to prove who you are — that's what authentication is all about. This guide walks you through the complete login process, from launching Gemini CLI for the first time to verifying that your AI assistant is ready to work.

## Learning Objectives

Picture this: you've got a powerful AI coding assistant that can write code, fix bugs, and explore entire codebases. But here's the catch — how does it know you're allowed to use it?

That's the problem authentication solves. And here's the good news: Gemini CLI offers a **free tier** (Gemini Code Assist for individuals) that anyone with a Google account can use. No credit card required. Whether you're on your own laptop or working in a cloud environment like GitHub Codespaces, you can sign in and get to work.

By the end of this exercise, you will:

1. Understand the three ways to authenticate Gemini CLI (Google login, API key, Vertex AI)
2. Complete the full login flow in a GitHub Codespaces environment using Google OAuth
3. Grasp the basics of how OAuth authorization works behind the scenes

## Prerequisites

- You already have Gemini CLI installed (running `` gemini `` in your Terminal doesn't throw an error)
- You have a Google account (a free Gmail account works — no paid subscription required)
- You know how to open a Terminal (command line)

## What You'll Build

By the end of this guide, you'll have a fully authenticated Gemini CLI session. You'll be able to type a question, get an AI-generated response, and start using Gemini as your command-line coding assistant.

---

## Key Concepts

### Google OAuth: Why Not Just a Password?

You might wonder: why can't you just type in a username and password to log into Gemini CLI?

This is where a security mechanism called **OAuth** comes in. Here's a real-world analogy:

Imagine you live in a gated community (your Google account). A delivery driver (Gemini CLI) shows up with your food order.

- **The old-school way:** You give the driver a copy of your house key. Risky! What if they lose it?
- **The OAuth way:** The driver arrives at the gate, and the security guard (Google's authorization system) calls you: "Someone named Gemini CLI wants to come in to make a delivery. Do you approve?" You say yes, the guard lets them in — but never hands over your key.

The benefits:

- Gemini CLI never learns your Google password
- You can revoke access at any time from your Google account settings
- Even if Gemini CLI had a security flaw, your Google account stays safe

You've been using this mechanism every time you tap "Sign in with Google" in other apps. Today, you'll walk through the flow manually for the first time.

### Three Authentication Methods

Gemini CLI supports three ways to authenticate:

1. **Login with Google** — Uses your Google account via OAuth. This is the easiest option and works with the free tier (Gemini Code Assist for individuals). **Most learners should pick this one.**
2. **Use Gemini API Key** — For developers who want to use a manually generated API key from Google AI Studio.
3. **Vertex AI** — For enterprise users working within Google Cloud Platform projects.

### Folder Trust: A Safety Feature

When you first launch Gemini CLI in a project, it asks whether you trust the files in that folder. Why? Because projects can contain configuration files (like custom commands, skills, hooks, and MCP servers) that Gemini CLI will load and potentially execute. This is a safety check — you're telling Gemini CLI: "Yes, I know what's in this folder, and it's safe to load these configurations."

---

## Exercises

### Exercise 1: Launch Gemini CLI and Handle Initial Prompts

**Goal:** Start Gemini CLI in your Codespaces Terminal and navigate through the initial setup prompts.

**What to do:**

1. Open your Terminal in GitHub Codespaces.
2. Type `` gemini `` and press Enter. You'll see the GEMINI ASCII art logo and some tips for getting started.

![03-Gemini-CLI-Login-Guide-1.png](img/03-Gemini-CLI-Login-Guide/03-Gemini-CLI-Login-Guide-1.png)

3. Gemini CLI first asks: **"Do you want to connect GitHub Codespaces to Gemini CLI?"** This prompt offers to install a VS Code extension that lets the CLI access your open files and display diffs directly in Codespaces.

```
> Do you want to connect GitHub Codespaces to Gemini CLI?
If you select Yes, we'll install an extension that allows the CLI to access your
open files and display diffs directly in GitHub Codespaces.

● 1. Yes
  2. No (esc)
  3. No, don't ask again
```

Select **Yes** and press Enter. You may see a message saying "No installer is available for GitHub Codespaces. Please install the 'Gemini CLI Companion' extension manually from the marketplace." — that's fine, just continue.

4. Next, you'll see the **"Do you trust the files in this folder?"** prompt:

![03-Gemini-CLI-Login-Guide-2.png](img/03-Gemini-CLI-Login-Guide/03-Gemini-CLI-Login-Guide-2.png)

```
Do you trust the files in this folder?

Trusting a folder allows Gemini CLI to load its local configurations, including
custom commands, hooks, MCP servers, agent skills, and settings.
These configurations could execute code on your behalf or change the behavior of the CLI.

This folder contains:
  • Commands (1): tell-me-a-joke-cmd
  • Skills (1): tell-me-a-joke
  • Setting overrides (3): general, ide, model

● 1. Trust folder (learn_gemini_cli_basic-project)
  2. Trust parent folder (workspaces)
  3. Don't trust
```

Select **1. Trust folder** and press Enter. This tells Gemini CLI it's safe to load the project's local configurations.

**What you'll notice:**

After handling these two prompts, Gemini CLI moves on to the authentication step. These prompts only appear on the first launch in a new project folder.

> **Key insight:** The folder trust mechanism is a security feature. It prevents malicious project configurations from automatically running when you open a folder. Always review what a folder contains before trusting it.

---

### Exercise 2: Choose Your Authentication Method

**Goal:** Select "Login with Google" as your authentication method.

**What to do:**

1. After the trust prompt, Gemini CLI asks: **"How would you like to authenticate for this project?"**

![03-Gemini-CLI-Login-Guide-3.png](img/03-Gemini-CLI-Login-Guide/03-Gemini-CLI-Login-Guide-3.png)

```
? Get started

How would you like to authenticate for this project?

● 1. Login with Google
  2. Use Gemini API Key
  3. Vertex AI

No authentication method selected.

(Use Enter to select)

Terms of Services and Privacy Notice for Gemini CLI
https://geminicli.com/docs/resources/tos-privacy/
```

2. Select **1. Login with Google** and press Enter.

**What you'll notice:**

- Below the options, you'll see a link to the Terms of Services and Privacy Notice. It's good practice to read these, especially the first time.
- The "No authentication method selected." message in red is just a status indicator — it disappears once you make your selection.

> **Key insight:** "Login with Google" uses the free Gemini Code Assist for individuals plan. You don't need a paid subscription — any Google account works. This is the recommended path for learners.

---

### Exercise 3: Complete the Google OAuth Authorization

**Goal:** Authorize Gemini CLI to access your Google account by completing the OAuth flow.

**What to do:**

1. After selecting "Login with Google," the Terminal displays a long Google OAuth URL and a prompt:

![03-Gemini-CLI-Login-Guide-4.png](img/03-Gemini-CLI-Login-Guide/03-Gemini-CLI-Login-Guide-4.png)

```
Please visit the following URL to authorize the application:

https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=...&scope=...&client_id=...(a very long URL)

Enter the authorization code:
```

2. **If you're in Codespaces with VS Code**, a popup dialog may appear asking **"Do you want Code to open the external website?"** — this shows the Google OAuth URL.

![03-Gemini-CLI-Login-Guide-5.png](img/03-Gemini-CLI-Login-Guide/03-Gemini-CLI-Login-Guide-5.png)

Click **Open** to launch the authorization page in your browser. (You can also click **Copy** and paste the URL into any browser manually.)

3. In your browser, Google will ask you to sign in (if you're not already) and then ask you to grant permissions to Gemini CLI. Review the permissions and click **Allow** or **Continue**.

4. After you approve, Google will display an **authorization code** — a long string that starts with something like `` 4/0A... ``.

5. **Copy the authorization code** from your browser.

6. **Paste it into the Terminal** after the `` Enter the authorization code: `` prompt, and press Enter.

![03-Gemini-CLI-Login-Guide-6.png](img/03-Gemini-CLI-Login-Guide/03-Gemini-CLI-Login-Guide-6.png)

**What you'll notice:**

If the code is valid, Gemini CLI completes the login silently and moves to the main interface. There's no dramatic "Login successful!" banner — it just works.

> **Key insight:** The authorization code is a one-time token. It's only valid for a few minutes and can only be used once. If it expires, just restart Gemini CLI (`` gemini ``) and go through the flow again.

---

### Exercise 4: Verify Your AI Assistant Is Working

**Goal:** Confirm that Gemini CLI is properly authenticated and responding to your commands.

**What to do:**

1. After successful login, you'll see the Gemini CLI main interface showing:
   - **Logged in with Google:** your-email@gmail.com
   - **Plan:** Gemini Code Assist for individuals
   - Tips for getting started
   - An input prompt (`` > ``) at the bottom

![03-Gemini-CLI-Login-Guide-7.png](img/03-Gemini-CLI-Login-Guide/03-Gemini-CLI-Login-Guide-7.png)

2. Type the following into the input field:

```
who are you?
```

3. Press Enter. Gemini CLI should reply with something like:

```
I am Gemini CLI, an interactive assistant specialized in software engineering.
I can help you explore codebases, implement features, fix bugs, and automate
workflows directly from your terminal.

In this workspace, I have access to tools for searching and editing files,
running shell commands, and utilizing specialized skills (like the tell-me-a-joke
skill I see in your .gemini directory). How can I help you with your project today?
```

If you see a response like this, congratulations — your AI coding assistant is officially online!

**What you'll notice:**

- The bottom status bar shows your project path, sandbox mode, and the current model (e.g., `` gemini-3-flash-preview ``).
- Gemini CLI is aware of your project's `` .gemini `` folder and its contents (skills, commands, etc.).

> **Key insight:** The "Plan: Gemini Code Assist for individuals" confirms you're on the free tier. Google may change plans and quotas over time (as of March 2026, the free tier is available), so check the [official Gemini CLI documentation](https://geminicli.com) for the latest information.

---

## Reflection: What Did We Learn?

Let's recap the complete login flow you just walked through:

1. **Launch** — Typed `` gemini `` to start the CLI
2. **Codespaces Extension** — Chose whether to connect the VS Code extension
3. **Folder Trust** — Told Gemini CLI it's safe to load project configurations
4. **Authentication Method** — Selected "Login with Google"
5. **OAuth Authorization** — Copied a URL, authorized in the browser, pasted the code back
6. **Verification** — Confirmed the AI is responding with `` who are you? ``

The key difference from other CLI tools: Gemini CLI uses Google OAuth, which means you never give it your password directly. Instead, Google acts as a trusted middleman that confirms your identity.

---

## Mentor's Note

**Why this exercise matters:**

You might think — login is just login, what's worth discussing?

Let me explain why there's real product design wisdom hiding behind this seemingly simple process.

**Key insights:**

- **Free AI for everyone.** Unlike many AI coding tools that require a paid subscription, Gemini CLI's free tier (Gemini Code Assist for individuals) means anyone with a Google account can access a powerful coding assistant. This is a deliberate choice by Google to lower the barrier to entry for AI-assisted development.

- **The command line is the most universal interface.** Your MacBook, your company's Linux servers, a Codespaces instance in the cloud, a Raspberry Pi running Ubuntu — if it has a Terminal, Gemini CLI can run on it. When you need to debug on a production server, troubleshoot inside a Docker container, or automate tasks in a CI/CD pipeline, you'll appreciate that Gemini CLI chose the command line.

- **Your first hands-on encounter with Google OAuth.** Today you walked through a complete Google OAuth authorization flow with your own hands. You've gone from "I've heard of OAuth" to "I've actually used OAuth." When you're building your own app someday and need to integrate "Sign in with Google," you'll think back to today and understand exactly what's happening behind that button.

- **Folder trust is a security mindset.** The "Do you trust the files in this folder?" prompt teaches an important principle: don't blindly execute code from untrusted sources. This mindset will serve you well throughout your career, whether you're reviewing pull requests, installing npm packages, or opening downloaded projects.

**Next steps:**

Now that you're connected, it's time to start creating with Gemini CLI. Try asking it to explain a piece of code in your project, write a simple function, or help you debug something. The more you use it, the more natural the workflow becomes.

---

## Quick Reference

**Launch Gemini CLI:**
```
gemini
```

**Re-authenticate (if needed):**
```
gemini auth login
```

**Check current auth status:**
```
gemini auth status
```

**Key files:**
- `` .gemini/ `` — Project-level Gemini CLI configuration directory
- `` GEMINI.md `` — Project instructions file that Gemini CLI reads for context

---

## Completion Checklist

- [ ] Successfully ran `` gemini `` in Terminal and saw the GEMINI ASCII art welcome screen
- [ ] Responded to the "Connect GitHub Codespaces" prompt
- [ ] Trusted the project folder when prompted
- [ ] Selected "Login with Google" as the authentication method
- [ ] Completed Google OAuth authorization (opened URL, granted permissions, pasted code)
- [ ] Saw "Logged in with Google" with your email address and plan information
- [ ] Typed `` who are you? `` and received a full self-introduction response from Gemini CLI

## Key Takeaways

1. **Three auth methods:** Login with Google (free, recommended), Gemini API Key, and Vertex AI — most learners should pick the first one.
2. **Folder trust:** Gemini CLI asks you to trust a folder before loading its configurations — this is a security feature, not a nuisance.
3. **OAuth in action:** Google acts as a trusted middleman. Gemini CLI gets permission to work on your behalf without ever seeing your password.
4. **Free tier available:** As of March 2026, Gemini Code Assist for individuals is free with any Google account.
5. **Command line wins:** Gemini CLI runs anywhere there's a Terminal — that's the whole point.
