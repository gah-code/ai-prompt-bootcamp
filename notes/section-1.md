# Section 1: Five Principles of Prompting

## Opening Summary

Prompting is fundamentally a design activity, not just an act of inspiration. Large language models don’t react solely to intent; they respond to structure, constraints, and signals. The quality of output depends more on how precisely the task is defined than on the model’s intelligence.

This article highlights five core principles that transform prompting from a spontaneous directive into a dependable, repeatable system: **Give Direction, Specify Format, Provide Examples, Evaluate Quality, and Divide Labor**. Each principle helps lessen ambiguity by shaping intent, enforcing structure, illustrating patterns, validating results, or breaking down complex tasks.

Implementing these principles provides a practical framework for collaborating with language models as partners rather than merely as sources of answers. They support iterative tuning, empirical assessment, and deliberate task design. The goal isn’t to craft clever prompts but to develop dependable ones that make model behavior predictable, auditable, and ready for real-world application.

# Prompt Engineering Principles — Study Notes

Mental model you can revisit when designing prompts, agents, or evaluation loops.

---

## 0. Naive Prompt

**Idea**  
Start with the simplest possible instruction that describes the task.

**Why it matters**  
A naive prompt establishes a baseline. Without it, you can’t tell whether later improvements are actually improvements.

**Typical outcome**  
Responses are generic, variable in length, and loosely aligned with intent.

**Takeaway**  
Always begin here. This is your control group.

---

## 1. Give Direction

**Idea**  
Explicitly describe the desired style, tone, or constraints, or reference a known pattern.

**What changes**  
The model starts to align with _how_ you want the answer, not just _what_ you want.

**Example lever**  
Seed words, tone cues, and audience description.

**Takeaway**  
Direction narrows the search space. You’re steering, not micromanaging.

---

## 2. Specify Format

**Idea**  
Define rules for structure and output shape.

**What changes**  
The response becomes predictable and machine-usable.

**Examples**  
Comma-separated lists, bullet points, JSON, tables.

**Takeaway**  
If the output will be parsed, reused, or compared, format is non-negotiable.

---

## 3. Provide Examples (Few-Shot)

**Idea**  
Show the model what _good_ looks like by example.

**What changes**  
The model generalizes from patterns rather than guessing intent.

**Best practice**  
Examples should be consistent in style, format, and complexity.

**Takeaway**  
Examples are stronger than instructions. They act like training data in miniature.

---

## 4. Evaluate Quality

**Idea**  
Actively assess outputs for errors, consistency, and usefulness.

**Techniques**  
Run the same prompt multiple times, rate responses, compare variance.

**Why it matters**  
Prompt engineering is empirical. You are testing a system, not casting a spell.

**Takeaway**  
If you don’t evaluate, you’re just writing prompts—you’re not engineering them.

---

## Mental Model Summary

Naive → Direction → Format → Examples → Evaluation

Each step reduces ambiguity and increases reliability.

---

## Obsidian Usage Tips

- Tag with: `#prompt-engineering #llm-systems #ai-notes`

- Link this note to agent specs, evaluation logs, or experiment notes.

- Treat each principle as a checklist when a prompt underperforms.

---

## One-Line Heuristic

> If a prompt feels clever instead of testable, it’s not done yet.

---
