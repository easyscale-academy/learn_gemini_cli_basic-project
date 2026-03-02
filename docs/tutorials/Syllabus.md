# Syllabus

A hands-on course that teaches you how to use Gemini CLI — Google's free, open-source AI coding agent — to boost your productivity. You'll go from understanding what an agent is to using one effectively in real projects.

## 01-What-Is-Coding-Agent

Learn the fundamental difference between an AI chatbot and an AI agent. Understand the ReAct loop (Reason, Act, Observe, Repeat) that powers tools like Gemini CLI. No code — just the mental model you need before getting hands-on.

## 02-Install-Gemini-CLI

Install Google's Gemini CLI using mise instead of the official `npm install -g` approach. Learn why declarative tooling (`mise.toml`) beats imperative global installs — version flexibility, smart reuse, clean management. By the end, running `gemini` in your terminal shows the CLI interface.

## 03-Gemini-CLI-Login-Guide

Building on the installation from 02, authenticate Gemini CLI using Google OAuth. Walk through the full login flow in GitHub Codespaces — folder trust, auth method selection, OAuth authorization, and verification. Learn what OAuth is and why it's more secure than passwords. By the end, typing `who are you?` gets a live AI response.

## 04-Read-Files

Now that Gemini CLI is installed and authenticated, learn the most fundamental interaction skill: referencing files with `@`. Understand absolute vs. relative paths, use `@` + relative path to feed files into the AI, and practice with four exercises — reading, questioning, comparing files, and summarizing the tutorial itself.

## 05-Read-URLs

Building on file references from 04, learn to feed web URLs directly to Gemini CLI. Paste any public URL into your prompt and the AI fetches, reads, and answers questions about the page. Practice summarizing docs, asking targeted questions, and extracting specific details — turning Gemini into your research assistant.

## 06-Read-Screenshots

Complete your context-feeding toolkit by learning to share screenshots with Gemini CLI. Take a screenshot, upload it to your Codespace, copy the relative path, and reference it with `@`. Practice having the AI describe interfaces and interpret error messages — faster and more precise than text descriptions.

## 07-Write-Files

Now that you can feed context into Gemini CLI, learn to control its output. Use absolute paths to tell the AI exactly where to create or modify files, and request changelog documents that explain what changed and why. Practice creating a script and its documentation in one prompt, and establish a `docs/changes/` folder habit for tracking AI-driven modifications.

## 08-Choose-Model

Learn to select the right Gemini model for each task. Understand the trade-offs between Pro (powerful, expensive), Flash (fast, affordable), and Flash-Lite (fastest, cheapest). Use the `/model` command to switch models, check `.gemini/settings.json` to see where preferences are stored, and build the habit of right-sizing your tools — defaulting to Flash for learning.

## 10-Using-Slash-Commands

Learn how Gemini CLI's dual system of Commands (`.gemini/commands/*.toml`) and Skills (`.gemini/skills/*/SKILL.md`) lets you create reusable prompt templates. Practice with a currency converter command — first manually pasting the full prompt, then using `/convert-currency` to see the power of automation. Understand `{{args}}` placeholders and when to use commands vs. skills.
