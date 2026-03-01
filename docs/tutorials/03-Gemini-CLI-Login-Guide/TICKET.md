# Log into Gemini CLI with your Google Account

## Objective

Authenticate Gemini CLI using your Google account so that you can interact with the AI assistant. By the end, typing `who are you?` in Gemini CLI should return a self-introduction response.

Read the tutorial: [Gemini CLI Login Guide](https://github.com/easyscale-academy/learn_gemini_cli_basic-project/tree/03-Gemini-CLI-Login-Guide)

## Actionable Items

1. Open the Codespace on the `03-Gemini-CLI-Login-Guide` branch, then run `gemini` in the Terminal
2. Walk through the initial prompts (Codespaces extension, folder trust) and select "Login with Google" as the authentication method
3. Complete the Google OAuth flow (open the URL, authorize, paste the code back), then type `who are you?` to confirm the AI responds

**Estimated time:** 10-15 minutes

## Checklist

- [ ] **Launch Gemini CLI** - Ran `gemini` and saw the GEMINI ASCII art welcome screen
- [ ] **Folder trust** - Selected "Trust folder" when prompted
- [ ] **Login with Google** - Selected "Login with Google" and completed the Google OAuth authorization flow
- [ ] **Logged in** - Saw "Logged in with Google" with your email and "Plan: Gemini Code Assist for individuals"
- [ ] **AI responds** - Typed `who are you?` and received a self-introduction response from Gemini CLI

## Submission & Verification

When you're done, run `/teach-check` to verify your work against the checklist. Say "ship it" when complete to generate RESULT.md, then share the RESULT.md file GitHub link with your instructor.

## Grading Rubric

> **For instructors and /teach-check assistant** — Students may skip this section.

- **Authentication method:** Student logged in via "Login with Google" (not API Key or Vertex AI). Verify by checking the Terminal shows "Logged in with Google:" followed by their email address.
- **Plan confirmation:** Terminal displays "Plan: Gemini Code Assist for individuals", confirming the free tier is active.
- **AI interaction:** Student typed `who are you?` (or similar) and received a coherent response from Gemini CLI. This confirms the full auth flow completed successfully.
- **Conceptual understanding:** Student can explain what OAuth does (grants Gemini CLI permission without sharing the Google password) and why the folder trust prompt exists (security check before loading project configurations).
