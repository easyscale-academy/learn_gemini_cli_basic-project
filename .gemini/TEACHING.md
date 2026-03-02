# Teaching Guide: Currency Converter App — Your First Vibe Coding Experience

## Overview

This lesson introduces students to "vibe coding" — building software by describing what you want to an AI coding agent rather than writing code manually. Through three progressive exercises, students discover the fundamental principle that **input quality determines output quality**, and learn the interview technique to clarify fuzzy ideas.

**Duration:** 15-30 minutes
**Level:** Beginner
**Prerequisites:** Gemini CLI installed and authenticated (lessons 02-03), basic familiarity with commands (lessons 04-08)

---

## Learning Outcomes

By the end of this lesson, students will be able to:

1. **Build a working app using vibe coding** — Describe what they want and let the AI implement it
2. **Articulate why clear requirements matter** — Explain, from their own experience, how input quality affects output quality
3. **Use the interview technique** — Turn a fuzzy idea into a concrete plan through structured conversation with AI
4. **Recognize the communication bottleneck** — Understand that "what to build" is now harder than "how to build"
5. **Choose the right approach for the situation** — Know when to use vague exploration, clear specs, or interview-style brainstorming

---

## Concept Sequence

### Phase 1: See the Target (5 minutes)

**Objective:** Give students a concrete mental model of the end goal.

**What happens:**
- Students run `streamlit run app-example.py` to see the reference implementation
- They interact with the app — enter amounts, switch currencies, see conversions
- This creates a clear "before" snapshot they'll compare against later

**Teaching notes:**
- Let students play with the app for a minute. Don't rush this.
- Ask: "What do you notice about the app? What features does it have?"
- This establishes the target so they can evaluate their own results later.

**Key question to ask:** "If you had to describe this app to someone who hasn't seen it, what would you say?"

---

### Phase 2: The Vague Approach — Exercise 1 (5-7 minutes)

**Objective:** Let students experience the consequences of vague communication firsthand.

**What happens:**
- Students start Gemini CLI with `gemini`
- They use `/teach-code build me a currency converter` — intentionally vague
- Gemini builds something based on its interpretation
- Students run the result and compare with the reference implementation

**Teaching notes:**
- **Do NOT warn students** that this will produce poor results. The surprise is the lesson.
- Let them discover the gap between what they imagined and what they got.
- Common reactions: "That's not what I wanted," "It made a command-line tool," "It's missing error handling"
- These reactions ARE the learning moment.

**Key question to ask:** "What did Gemini assume about your request? Were those assumptions correct?"

**What to watch for:**
- Students who blame the AI ("it's dumb") — redirect to the input quality
- Students who get frustrated — normalize it: "This is exactly what's supposed to happen"
- Students who accidentally get a good result — ask them to try again with a different vague prompt

---

### Phase 3: The Clear Spec Approach — Exercise 2 (5-7 minutes)

**Objective:** Demonstrate the dramatic improvement that clear communication produces.

**What happens:**
- Students start a new Gemini session with `gemini`
- They use `/teach-code READ app-spec.md to understand the currency converter app requirement, then write the python app at app.py, and teach me how to run it.`
- Gemini reads the spec and builds a much closer match to the reference
- Students compare Exercise 1 vs Exercise 2 results

**Teaching notes:**
- The contrast between Exercise 1 and Exercise 2 is the core "aha moment" of this lesson.
- Ask students to open `app-spec.md` and read it. It's only ~40 lines.
- Point out: "Same AI, same task. The only thing that changed was your input."
- This is where the principle "better input = better output" becomes visceral, not abstract.

**Key question to ask:** "How long would it take to write a spec like `app-spec.md`? How much time did it save?"

**What to watch for:**
- Students who say "but writing a spec takes time" — yes! That's the tradeoff. 5 minutes of clarity vs. 30 minutes of back-and-forth.
- Students who want to skip the spec and just iterate — valid approach, but more expensive. Discuss tradeoffs.

---

### Phase 4: The Interview Technique — Exercise 3 (7-10 minutes)

**Objective:** Teach the most powerful technique in this lesson — using AI to clarify your own thinking.

**What happens:**
- Students start a new Gemini session with `gemini`
- They use `/teach-brainstorm I want to build a currency converter app but I'm not sure exactly what features it should have or how to structure it`
- Gemini asks clarifying questions (What problem? What constraints? What are you optimizing for?)
- Students answer the questions, gradually forming a clear plan
- They then use `/teach-code` to implement the plan

**Teaching notes:**
- This is the most important exercise. The first two set up the context; this one delivers the transferable skill.
- The interview technique works because questions force structured thinking.
- Point out: this is exactly what good product managers and senior engineers do — they ask questions before building.
- The AI is serving as a "thinking partner," not just a code generator.

**Key question to ask:** "How did answering those questions change your understanding of what you wanted to build?"

**What to watch for:**
- Students who give minimal answers to Gemini's questions — encourage them to engage fully
- Students who find the questions annoying — explain that discomfort means the questions are surfacing things they hadn't thought about
- Students who love it — these are your future product managers!

---

### Phase 5: Reflection and Synthesis (5 minutes)

**Objective:** Help students articulate what they learned and connect it to broader skills.

**What happens:**
- Students compare all three results side by side
- Discussion about when to use each approach
- Connection to professional software development

**Teaching notes:**
- Ask students to explain the lesson in their own words. If they can articulate "better input = better output" without prompting, the lesson landed.
- Connect to real-world scenarios: requirements documents, user stories, design specs.
- Emphasize: the interview technique is valuable even without AI — it's a communication skill.

**Key questions to ask:**
- "When would you use the vague approach? The spec approach? The interview approach?"
- "How does this change the way you think about what 'programming skill' means?"

---

## Concept Map

```
Vibe Coding
├── Input Quality → Output Quality
│   ├── Vague input → Unpredictable output
│   ├── Clear input → Predictable output
│   └── Interview → Clarity when unsure
├── The Communication Bottleneck
│   ├── "What to build" is now harder than "how to build"
│   └── Communication skills = coding skills
└── The Interview Technique
    ├── Start with fuzzy idea
    ├── AI asks clarifying questions
    ├── Answers force structured thinking
    └── Converge on concrete plan
```

---

## Common Student Struggles

### 1. "The AI should just know what I want"

**Why it happens:** Students are used to Google search, which works well with vague queries. AI coding is different — it generates, not retrieves.

**How to address:** Ask: "When you order food at a restaurant, do you say 'bring me food' or do you specify what you want? Same principle."

### 2. "Writing specs takes too long"

**Why it happens:** They see the spec as overhead, not investment.

**How to address:** Time the comparison: 5 minutes writing spec vs. 20+ minutes iterating on vague results. Show the math.

### 3. "I don't know enough to write a spec"

**Why it happens:** This is actually the most honest reaction, and it's the perfect segue to Exercise 3.

**How to address:** "That's exactly what the interview technique is for. You don't need to know the answers — you just need to be willing to think through the questions."

### 4. "My Exercise 1 result was actually good"

**Why it happens:** Sometimes the AI gets lucky, or the student's vague request happened to align with common patterns.

**How to address:** Ask them to try a different vague prompt (e.g., "make a currency tool"). Or ask: "Would it produce the same result every time? Can you rely on it?" Consistency matters.

### 5. "I can just iterate — keep asking for changes"

**Why it happens:** This is a valid approach and students shouldn't be discouraged from it.

**How to address:** Acknowledge it works, but discuss cost: "Each iteration takes time and context. Starting clear is like writing tests first — more upfront effort, less total effort."

---

## Teaching Tips

1. **Don't pre-explain the lesson** — The surprise of Exercise 1 producing unexpected results IS the lesson. If you explain "clear input matters" before they experience it, the lesson loses its impact.

2. **Let them struggle with Exercise 1** — Resist the urge to help. The gap between expectation and reality is the teaching moment.

3. **Time the exercises** — If students notice that Exercise 2 took less total time (including spec writing) than Exercise 1 (including iterations), the argument for clarity becomes concrete.

4. **Make it personal** — After Exercise 3, ask: "Think of a project idea you've been wanting to build. What questions would you need to answer before starting?"

5. **Celebrate the "aha moment"** — When a student says "oh, I see why the spec matters," acknowledge it specifically. This is the core learning happening in real time.

---

## Common Misconceptions

1. **"AI replaces the need to think clearly"** — Actually the opposite. AI amplifies your thinking quality. Clear thinking → clear output. Fuzzy thinking → fuzzy output.

2. **"More detail is always better"** — Not necessarily. Over-specified prompts can be as problematic as under-specified ones. The goal is the right level of detail for the task.

3. **"The interview technique only works with AI"** — It works with humans too! Senior engineers have been doing this for decades. The AI just makes it accessible to everyone.

4. **"Vague prompts are always bad"** — Not true. Vague prompts are great for exploration, brainstorming, and learning. The issue is using them when you need precision.

---

## Assessment Ideas

### Quick Check (in-session)
- Can the student explain why Exercise 2 produced better results than Exercise 1?
- Can the student describe a situation where they'd use each approach?
- Did the student engage meaningfully with the interview questions in Exercise 3?

### Deeper Assessment
- Ask the student to write a spec for a different app (e.g., a todo list, a weather dashboard) — evaluate the clarity and completeness of their spec
- Have students pair up and use the interview technique on each other's project ideas
- Ask students to rate their own prompts on a "vague to clear" scale and justify the rating

### Portfolio Evidence
- The `app.py` file they created
- Notes from the brainstorming session (generated in `./tmp/notes/`)
- Their RESULT.md from `/teach-check`

---

## Troubleshooting

### Streamlit won't run
- Check that dependencies are installed: `mise run inst`
- Check Python version: `python --version` (should be 3.12+)
- Try: `mise run venv-create && mise run inst`

### Gemini CLI not responding
- Check authentication: try a simple prompt first
- Check model: use `/model` to verify Flash is selected
- Restart: exit and run `gemini` again

### Student got stuck in a session
- Start a new session: exit Gemini CLI and run `gemini` again
- Resume a previous session: `gemini -r` or `gemini --resume`
- Browse sessions: use `/resume` inside Gemini CLI

### Exercise 1 produced a great result
- This can happen! Ask the student to try with a different vague prompt
- Or discuss: "Even if this worked once, would it work reliably every time?"
- The lesson is about consistency, not just one-time success

---

## Extensions

### For Advanced Students
- **Write their own spec** for a different app and build it using Exercise 2's approach
- **Compare multiple interview sessions** — run Exercise 3 twice with different answers and compare the plans
- **Build on the currency converter** — add features like historical rates, charts, or API integration

### For Students Who Finish Early
- **Explore `app-spec.md`** — discuss what makes a good spec vs. a bad spec
- **Try the Chinese commands** — use `/teach-code-cn` or `/teach-brainstorm-cn` to experience the same lesson in Chinese
- **Help a classmate** — pair up and practice the interview technique on a real project idea

### Cross-Curricular Connections
- **Writing/Communication:** The spec-writing skill transfers directly to technical writing
- **Business/Product:** The interview technique is how product managers gather requirements
- **Psychology:** The lesson touches on cognitive biases — we assume others understand our mental model

---

## Key Takeaways

1. **Vibe coding works** — you can build real apps by describing what you want
2. **Input quality = output quality** — this is the fundamental law of AI-assisted development
3. **The interview technique** is the most powerful tool for unclear requirements
4. **Communication clarity** is becoming as valuable as coding ability
5. **Choose the right approach** — vague for exploration, spec for precision, interview for clarity

---

## Verifying Student Submissions

When checking student work (via `/teach-check` or manual review):

### Must Have
- [ ] `app.py` exists and runs with `streamlit run app.py`
- [ ] Student can explain the difference between Exercise 1 and Exercise 2 results
- [ ] Student attempted Exercise 3 (interview technique)
- [ ] Student can articulate "better input = better output" in their own words

### Nice to Have
- [ ] Notes in `./tmp/notes/` from the teaching commands
- [ ] `RESULT.md` generated from `/teach-check`
- [ ] Student can describe when they'd use each approach in a real project

### Red Flags
- Student copied `app-example.py` to `app.py` without going through the exercises
- Student can't explain what happened in the exercises
- Student skipped Exercise 3 — this is the most important one!

---

## Resources for Teachers

- **Streamlit documentation:** https://docs.streamlit.io/
- **Gemini CLI repository:** https://github.com/google-gemini/gemini-cli
- **This tutorial:** https://github.com/easyscale-academy/learn_gemini_cli_basic-project/tree/13-Currency-Converter-App/
