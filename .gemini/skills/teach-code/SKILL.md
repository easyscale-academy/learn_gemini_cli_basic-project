# Skill: teach-code

Write code as requested by the student. After completing the code, generate a learning note.

## Workflow

1. If the user request is empty, ask what they want to build
2. Read the relevant source files to understand context
3. Write the code as requested
4. After completing, generate a learning note at `./tmp/notes/YYYY-MM-DD-HH-MM-SS-{topic}.md`

## Learning Note Format

The note should explain (300-500 words):
- **What we did** — Summary of the code written
- **Why this approach** — Reasoning behind design choices
- **How it works** — Step-by-step explanation of the logic
- **Key concepts** — Important ideas the student should remember

## Important

- Follow the Mentor role in `.gemini/MENTOR.md`
- Always explain the code, not just write it
- Create the `./tmp/notes/` directory if it doesn't exist
