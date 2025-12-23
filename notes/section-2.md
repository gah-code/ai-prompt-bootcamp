# Section 2: How Does AI Work?

## How Does AI Work? — Study Notes

This note explains how modern AI systems (especially large language models) function at both practical and conceptual levels. The goal is not mathematical depth, but operational understanding—enough to reason about behavior, limits, and failure modes.

---

## 1. What Is an AI Model?

A modern AI language model is a **statistical pattern engine** trained on vast amounts of text. It does not store facts in a database, reason symbolically by default, or understand meaning the way humans do. Instead, it learns probabilities: given a sequence of text, what token is most likely to come next?
At runtime, the model:

1. Reads input as tokens
2. Computes probabilities based on learning patterns
3. Produces the next token
4. Repeats until an answer emerges

**Key insight**
AI does not “know” things—it predicts language that _resembles knowing_.

----

## 2. What Are Tokens?

**Tokens** are the basic units of text that the model processes. They are not words, but chunks of text that may represent:

- Whole words
- Parts of words
- Punctuation
- Spaces or symbols

Examples:

- "computer" → `computer` (1 token)
- "unbelievable" → `un` + `believable` (multiple tokens)
- " ChatGPT" → leading space may be its own token

**Why tokens matter**

- Context limits are measured in tokens, not characters
- Cost and latency scale with token count
- Model behavior can subtly change based on token boundaries

**Takeaway**  
Tokens are the language the model actually speaks. Humans see sentences; models see token sequences.

-----

## 3. AI Hallucinations

An AI hallucination occurs when a model produces output that sounds confident and coherent but is factually incorrect, fabricated, or unverifiable.

**Why hallucinations happen**

- The model optimizes for _plausibility_, not truth
- Missing information is filled with statistically likely patterns
- Ambiguous or underspecified prompts increase risk

**Common hallucination patterns**

- Invented citations or URLs
- Confident explanations of nonexistent concepts
- Mixing correct facts with subtle errors

How to reduce hallucinations

- Provide clear constraints and context
- Ask for sources or uncertainty markers
- Break tasks into smaller steps
- Use evaluation loops or external verification

**Key insight**  
Hallucination is not a bug—it is a predictable consequence of probabilistic text generation.

-----

## 4. Chat Models vs Reasoning Models

### Chat Models

**Purpose**
Optimized for conversation, helpfulness, and fluent responses.

**Strengths**

- Natural dialogue
- Broad knowledge recall
- Good for brainstorming, drafting, and explanation

**Limitations**

- May skip reasoning steps
- Can appear confident without verification
- Less reliable for multi-step logic under ambiguity

### Reasoning Models

**Purpose**
Optimized to perform structured, multi-step reasoning before answering.

**Strengths**

- Better performance on logic-heavy tasks
- More consistent in math, planning, and analysis
- Reduced error rates on complex problems

**Limitations**

- Slower and more resource-intensive
- Less conversational
- Still bound by training data and token limits

**Mental model**
Chat models speak smoothly. Reasoning models think longer before speaking.

------

## 5. Practical Mental Model

AI systems are:

- Token-based
- Proability-driven
- Sensitive to structure and context
- Capable of reasoning when explicitly guided

They are not:

- Databases of truth
- Conscious agents
- Guaranteed to be correct

------

## Obsidian Usage Tips

- Tags: `#ai-foundations #llm-basics #prompt-engineering`
- Link this note to prompt principles, evaluation logs, and agent design notes
- Revisit this when diagnosing surprising or incorrect outputs

-----

## One-Line Heuristic

> AI outputs are not answers—they are hypotheses that need structure, testing, and verification.

----
