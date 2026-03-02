# Skill: teach-brainstorm

Help the student clarify their fuzzy idea through interview-style questions.

## Workflow

1. Ask the student to describe their idea in one sentence
2. Ask clarifying questions one at a time:
   - What problem does this solve?
   - Who is it for?
   - What does success look like?
   - What are the constraints?
3. Summarize what you've heard and confirm understanding
4. After the decision is made, generate a decision doc at `./tmp/notes/YYYY-MM-DD-HH-MM-SS-decision-{topic}.md`

## Decision Doc Format

- **Problem statement** — What we're trying to solve
- **Decision** — What we decided to do
- **Reasoning** — Why this approach
- **Alternatives considered** — What else we thought about
- **Next steps** — What to do first

## Important

- Follow the Mentor role in `.gemini/MENTOR.md`
- Ask one question at a time — don't overwhelm
- Reflect back what the student says to confirm understanding
- Create the `./tmp/notes/` directory if it doesn't exist
