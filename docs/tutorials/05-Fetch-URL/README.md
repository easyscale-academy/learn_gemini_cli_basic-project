# Gemini CLI Basics: Getting AI to Read Web Pages for You

> Learn how to feed URLs to Gemini CLI so the AI can read, summarize, and explain web pages on the spot.

## Overview

You find a great technical doc online and want AI to help you make sense of it. The old-school approach: copy the whole thing, paste it into the AI, realize it's way too long, give up.

There's a much better way: just hand the AI a link and let it read the page itself. Gemini CLI can fetch and read web pages directly — drop in a URL, and it'll read the content and answer your questions. Easily 10x faster than copy-pasting.

## Learning Objectives

You're going to run into this situation all the time: you find a doc, a tutorial, a GitHub README, and you need to understand it quickly. Maybe it's a library you've never used. Maybe it's a colleague's project page. Instead of spending 20 minutes reading and re-reading, you can hand the URL to Gemini CLI and get a summary in seconds. This skill turns the AI into your personal research assistant.

By the end of this exercise, you will:

1. Know how to feed a URL to Gemini CLI and have it read the page
2. Use different prompt styles to summarize, explain, or extract specific info from a web page
3. Understand which pages the AI can and can't access

## Prerequisites

- Gemini CLI installed and authenticated (completed in previous lessons)
- A GitHub Codespace with this project open
- Completed Lesson 04 (reading files with `@`)

## What You'll Build

No code this time — this is a skill exercise. You'll practice feeding URLs to Gemini CLI to read web pages, which is essential for quickly researching docs, libraries, and technical references.

---

## Key Concepts

### How URL Fetching Works

When you paste a URL into Gemini CLI, the AI does three things:

1. **Visits the web page** — it sends a request to the URL, just like a browser would
2. **Reads the contents** — it extracts the text from the page
3. **Answers your question** — it uses the page contents to respond to whatever you asked

You don't need any special syntax. Just paste the URL right into your prompt alongside your question.

### The Basic Pattern

```
[your question] [URL]
```

Or flip it around:

```
[URL] [your question]
```

Both work. The AI figures out which part is the URL and which part is your question.

### What the AI Can and Can't Read

**Pages that work:**
- Any publicly accessible page (no login required)
- Technical docs, blog posts, GitHub READMEs, news articles
- API documentation, tutorials, wiki pages

**Pages that won't work:**
- Anything behind a login wall (your Gmail inbox, private Slack channels)
- Paywalled or members-only content
- Sites that block automated access

If the AI says it can't reach a page, you've probably hit one of these limitations. In that case, copy and paste the content manually.

---

## Exercises

### Exercise 1: Read a Web Page

**Goal:** Get Gemini CLI to fetch and summarize a public web page.

**What to do:**

1. Open Gemini CLI in your terminal (type `gemini` and press Enter)
2. Type the following prompt and press Enter:

```
Read this page and give me the key takeaways: https://github.com/google-gemini/gemini-cli
```

3. Observe how Gemini fetches the page and summarizes it for you

**What you'll notice:**

Gemini visits the URL, reads through the page content, and comes back with a summary. You didn't have to open a browser, read the whole page, or copy anything.

> **Key insight:** Just paste a URL into your prompt and the AI reads the page for you. No special syntax needed.

---

### Exercise 2: Ask a Specific Question About a Web Page

**Goal:** Use a URL to ask the AI a targeted question about a page's contents.

**What to do:**

1. In Gemini CLI, type:

```
https://docs.github.com/en/codespaces/overview
What exactly is a GitHub Codespace? Explain it in plain English, in 3 sentences.
```

2. Press Enter and see how Gemini answers based on the page content

**What you'll notice:**

Instead of a generic answer, Gemini gives you an explanation grounded in the actual page content. This is more accurate than asking a general question without a source.

> **Key insight:** Combining a URL with a specific question turns Gemini into a research assistant that answers based on actual sources, not just its training data.

---

### Exercise 3: Extract Specific Details

**Goal:** Have Gemini dig into a page and pull out specific information.

**What to do:**

1. Pick any public technical docs page that interests you (for example, Python docs, React docs, or any GitHub README)
2. In Gemini CLI, type:

```
[paste your chosen URL here]
Does this page mention anything about installation or getting started? Walk me through the steps.
```

3. Press Enter and see how Gemini finds and presents the specific information

**What you'll notice:**

Gemini doesn't just summarize — it can find specific sections and details within a page. This is great for quickly locating the information you need without reading an entire document.

> **Key insight:** You can ask targeted questions about any part of a web page. The AI acts like a search engine that actually understands the content.

---

## Reflection: What Did We Learn?

- **Paste a URL** into your Gemini CLI prompt and the AI fetches and reads the page for you
- You can ask it to **summarize**, **explain**, or **find specific details** on any public page
- This works with any publicly accessible web page — docs, blogs, GitHub pages, articles
- Pages behind login walls or paywalls are off-limits
- Way faster than copying and pasting the whole thing

---

## Mentor's Note

**Why this exercise matters:**

This might seem like a convenience feature, but it's actually a fundamental shift in how you work. Before this, researching a new library meant opening tabs, skimming docs, and trying to piece things together. Now you have an AI that reads the docs for you and answers your questions about them in real time. That's not just faster — it changes the way you learn and explore new technology.

**Key insights:**

- URL fetching turns Gemini CLI from a code assistant into a research partner. Whenever you encounter something new — a library, a framework, an API — your first move can be: paste the docs URL and ask questions.
- The combination of file references (`@` from the previous lesson) and URL fetching gives you two powerful ways to feed context to the AI: local files and web pages. Together, they cover most situations you'll face.

**Next steps:**

Make it a habit: whenever you're reading technical docs online, try pasting the URL into Gemini CLI and asking it to summarize or explain. Compare the AI's summary with your own understanding — it's a great way to check comprehension and catch things you might have missed.

---

## Quick Reference

**Summarize a page:**
```
Read this page and give me the key takeaways: https://example.com/docs
```

**Explain a concept from a page:**
```
https://example.com/docs
What does this page say about [topic]? Explain it simply.
```

**Extract specific info:**
```
https://example.com/docs
Does this page mention [specific thing]? Walk me through it.
```

**Key limitations:**
- Only public pages (no login required)
- No paywalled or members-only content
- If blocked, copy-paste the content manually
