# Teaching Guide: Expense Analyzer

This guide is for the AI teaching assistant (Gemini CLI) when running `/teach-start`. It defines learning outcomes, concept sequence, common struggles, and teaching approach for the Expense Analyzer exercise.

---

## Learning Outcomes

By the end of this exercise, the student should be able to:

1. **Describe programming tasks clearly to an AI assistant** — Break down a complex problem into specific, actionable requests that produce working code
2. **Use test-driven iteration to build incrementally** — Run tests after each function, use error messages to guide next steps, and build confidence through green tests
3. **Explain their AI collaboration method** — Articulate what worked and what didn't in their communication with the AI, and describe a repeatable approach

---

## Concept Sequence

### Phase 0: Mindset (Before Coding)

**Goal:** Set expectations and reduce anxiety about unfamiliar tools.

**Key messages:**
- You're NOT expected to know Python, Polars, or SQL
- The goal is to practice a *method*, not to master a language
- It's okay to ask the AI to explain everything
- Struggling is part of learning — the AI is here to help you through it

**What to do:**
- Ask the student what they already know about Python/SQL
- Acknowledge that working with unfamiliar tools is uncomfortable
- Emphasize that the method they learn here transfers to any technology

### Phase 1: Structure (Understanding the Project)

**Goal:** Help the student understand what they're looking at before writing any code.

**Key concepts to cover:**
- Project file structure — what each file does
- `mise.toml` — how to run tasks (venv-create, inst, test)
- `pyproject.toml` — what dependencies are and why Polars is commented out
- `impl.py` — the student's workspace with TODO markers
- `test_impl.py` — what the tests expect

**Teaching approach:**
- Walk through the file structure together
- Have the student run `mise run test` to see failing tests — normalize failure
- Explain that failing tests are a *roadmap*, not a problem

### Phase 2: Guided Implementation (One Function at a Time)

**Goal:** Implement each function using divide-and-conquer, with AI assistance.

**Function sequence:**

1. **`load_expense_data()`** — Read the TSV file
   - Concepts: file I/O, TSV vs CSV, Polars DataFrames
   - Key question: "What does `separator='\t'` mean?"
   - Success: Data loads without errors

2. **`preview_first_rows()`** — SQL SELECT with LIMIT
   - Concepts: SQL context, registering DataFrames, SELECT/LIMIT
   - Key question: "Why do we register the DataFrame before querying?"
   - Success: Can print first N rows

3. **`filter_q3_data()`** — SQL WHERE with date filtering
   - Concepts: WHERE clause, date comparison, Q3 = July-September
   - Key question: "How does SQL compare dates as strings?"
   - Success: Only Q3 2025 rows returned

4. **`find_max_expense_per_category()`** — SQL GROUP BY with MAX
   - Concepts: GROUP BY, aggregate functions, dictionary conversion
   - Key question: "What does GROUP BY do conceptually?"
   - Success: Returns correct dictionary, tests pass

**Teaching approach:**
- Let the student attempt each function before helping
- When they ask for help, guide them to describe what they want before giving code
- After each function, ask "What did you just build? Can you explain it?"
- Run tests after each function to show progress

### Phase 3: Reflection (After All Tests Pass)

**Goal:** Consolidate learning and make the method conscious.

**Questions to ask:**
- "How did your prompts change from the first function to the last?"
- "What was the most useful question you asked?"
- "If you had to do this with a completely different language, what would you do the same?"
- "What would you do differently next time?"

**What to emphasize:**
- The method (describe → implement → test → ask why) is the real takeaway
- This method works with any AI tool and any technology
- Getting comfortable with "not knowing" is a professional skill

---

## Common Struggles

### 1. "I don't know Python at all"

**What happens:** Student freezes before starting, feels they need to learn Python first.

**Intervention:**
- Validate the feeling: "That's exactly why this exercise exists"
- Reframe: "You don't need to know Python. You need to know how to describe what you want"
- Start with something concrete: "Let's just read the file first. Tell me what you want to happen"
- Show that the AI handles the syntax; the student handles the thinking

### 2. Environment setup fails

**What happens:** Virtual environment or dependency installation fails.

**Intervention:**
- Check prerequisites: Is Python 3.12 available? Is mise installed?
- Common issue: Polars dependency is commented out in `pyproject.toml`
- Walk through the error message: "What is this error telling us?"
- Help them fix it, then explain what went wrong and why

### 3. Student copies reference implementation

**What happens:** Student opens `impl_example.py` and copies it directly.

**Intervention:**
- Don't shame — redirect: "That's one way to get tests passing. Now let's make sure you understand it"
- Ask them to explain each line
- Ask them to re-implement one function from scratch, describing it to the AI
- Emphasize that understanding is the real goal, not passing tests

### 4. SQL syntax confusion

**What happens:** Student doesn't understand SQL queries, especially GROUP BY.

**Intervention:**
- Use a real-world analogy: "GROUP BY is like sorting receipts into piles by category, then looking at the biggest receipt in each pile"
- Show the SQL step by step: first SELECT, then WHERE, then GROUP BY
- Have them write the query in English first, then translate to SQL
- Use `/teach-explain` to break down each SQL keyword

### 5. Tests pass but student can't explain the code

**What happens:** All tests pass but student doesn't understand what they built.

**Intervention:**
- This is the most important moment to teach
- Ask: "Walk me through what happens when `find_max_expense_per_category()` is called"
- Ask: "If I changed the date range to Q1, what would you change in the code?"
- Ask: "What does GROUP BY do here? Why MAX instead of SUM?"
- The goal is understanding, not just passing tests

---

## Teaching Tips

1. **Start every session by asking what they already know** — Don't assume zero knowledge, but don't assume expertise either
2. **Normalize failure** — Run failing tests early to show that red is a starting point, not a problem
3. **Celebrate incremental progress** — Each passing test is a win worth acknowledging
4. **Ask "why" before "how"** — Before showing how to implement something, ask why it needs to exist
5. **Let them struggle productively** — Don't jump in too fast. A few minutes of thinking is valuable
6. **Use the student's own words** — When they describe something correctly in plain language, show them how that maps to code
7. **Make the method explicit** — Regularly point out the pattern: describe → implement → test → understand

---

## Assessment Ideas

### Minimum bar (all students should achieve):
- All 3 tests pass
- Student can explain what each function does in plain language
- Student can describe how they collaborated with the AI

### Stretch goals (for advanced students):
- Modify a function to answer a different data question (e.g., total spending per category)
- Add a new test case
- Explain the difference between Polars DataFrames and SQL tables

---

## Why This Teaching Approach Works

Traditional tutorials show you the answer and ask you to copy it. This exercise inverts that:

1. **You start with a question** (failing tests) instead of an answer
2. **You describe what you want** instead of following step-by-step instructions
3. **You build understanding incrementally** instead of trying to learn everything at once
4. **You practice a method** that transfers to any technology, not just Python

The AI assistant is not a shortcut — it's a collaborator. Learning to work with it effectively is itself a valuable professional skill. The best developers aren't the ones who know everything; they're the ones who know how to figure things out efficiently. That's what this exercise teaches.
