# Install Gemini CLI with mise

## Objective

Install Google's Gemini CLI using mise so that typing `gemini` in your terminal launches the CLI and shows help information. This lesson focuses only on installation — authentication and first use will be covered in the next lesson.

Read the tutorial: [Install Gemini CLI](https://github.com/easyscale-academy/learn_gemini_cli_basic-project/tree/02-Install-Gemini-CLI)

## Actionable Items

1. Fork the teaching repository and create a Codespace on the `02-Install-Gemini-CLI` branch
2. Run `mise trust`, `mise activate`, and `mise install` to install Gemini CLI via the pre-configured `mise.toml`
3. Run `which gemini` to confirm the installation path, then run `gemini` to verify you see the CLI help output

**Estimated time:** 10-15 minutes

## Checklist

- [ ] **Fork and Codespace** - Forked the repo and created a Codespace on the `02-Install-Gemini-CLI` branch
- [ ] **mise setup** - Ran `mise trust`, `mise activate`, and `mise install` successfully
- [ ] **Verify installation path** - Ran `which gemini` and saw a mise-managed path in the output
- [ ] **Launch Gemini CLI** - Ran `gemini` and saw the CLI interface or help information

## Grading Rubric

- **Installation method:** Student installed Gemini CLI through mise (not `npm install -g`). Verify by checking that `which gemini` output contains `mise/installs` in the path.
- **Tool verification:** Student can run `gemini` and see the CLI help output or interactive interface. The goal is only installation — authentication and actual usage are NOT required for this lesson.
- **Conceptual understanding:** Student can explain why mise-managed installation is preferred over a global npm install (version management, clean uninstall, smart reuse).
