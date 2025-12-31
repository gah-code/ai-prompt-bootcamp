## Section 4: Standard Text Model Practices

## Standard Text Model Practices — Advanced Prompting Patterns

This study note documents reliable, repeatable prompting techniques for standard text-based language models. It is intended as a practical reference for designing prompts, diagnosing failures, and scaling from single prompts to structured workflows and agent systems.

---

## 1. Role Prompting

Role Prompting is a technique in which the user assigns a role or persona to the model to improve performance. For example, a user might ask the model to solve a math problem as a math teacher, or to write a poem as a poet.

**What it is**  

- Explicitly assigning a role to the model to shape perspective, priorities, and tone.
- Assigning a role to shape how the model behaves (tone, priorities, decision criteria).

**Why it works**  
Roles compress expectations and reduce ambiguity about _how_ to approach the task.

**Best practice**  

- Always pair a role with a concrete objective. A role alone provides flavor, not direction.
- Define the role **and** the job-to-be-done. A role without a task is cosplay.

**Template**

`You are a [role]. Your task is to [goal]. Constraints: [rules]. Output format: [shape]. Success criteria: [what “good” means].`

**Example**

`You are a senior QA engineer. Identify likely edge cases in this feature description. Constraints: focus on user-impacting failures; avoid implementation details. Output format: table with columns: Risk, Scenario, Why it matters, Suggested test.`
