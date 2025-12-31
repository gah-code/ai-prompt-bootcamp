# AI Prompt Bootcamp — Local Lab Starter

A lightweight, hands-on starter repository for an **AI Prompt Engineering Bootcamp**.

This project uses **Jupyter Notebooks** as the primary learning surface and is designed to scale gradually into more advanced topics such as structured prompting, LangChain chains, evaluations, and agent workflows.

Learning practical coding skills for working professionally with AI, including GPT-5, Veo3, Midjourney, & GitHub Copilot.

---

## What This Repository Is

- A **local lab environment** for experimenting with prompt engineering
- A **teaching scaffold** for learning how prompts behave in practice
- A **foundation** you can extend into a full course or internal training program

---

## Tech Stack

- **Python** (3.9+)
- **Jupyter Lab**
- **OpenAI API**
- **LangChain** (introduced progressively)
- **GitHub Copilot** (used as a learning companion)

---

## Repository Structure

```text
ai-prompt-bootcamp/
├── notebooks/
│   ├── 00_lab_sanity_test first.ipynb   # Sanity test - verify local environment
│   ├── 01-prompt-lab.ipynb              # Prompt lab - core prompt experiments
│   ├── core_features_walkthrough.ipynb  # Core walkthrough - guided feature tour
│   └── responses_api_and_messages.ipynb # Responses API - messages and handling
├── src/
│   └── prompt_utils.py                  # Prompt utilities - shared helpers
├── requirements.txt                     # Dependencies - Python package list
├── anaconda_projects/
│   └── db/                              # Database files - Anaconda project assets
├── notes/
│   ├── section-1.md                     # Prompting principles - five core principles
│   ├── section-2.md                     # LLM foundations - tokens, hallucinations, model types
│   ├── section-3.md                     # ChatGPT platform - tools, modes, workflows
│   └── section-4.md                     # Text model practices - advanced prompting patterns
├── .env.example                         # Environment template - sample variables
├── .gitignore                           # Git ignore - excluded files
└── README.md                            # Project overview - setup and usage
```

---

## Prerequisites

- Python **3.9 or higher**
  (Python 3.10+ recommended if you encounter dependency issues later)
- macOS, Linux, or Windows
- An **OpenAI API key** (only required for OpenAI-related notebooks)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<YOUR_USERNAME>/ai-prompt-bootcamp.git
cd ai-prompt-bootcamp
```

---

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

> Windows (PowerShell):
>
> ```powershell
> venv\Scripts\Activate.ps1
> ```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Register the Jupyter Kernel (Recommended)

This ensures notebooks run using the project’s virtual environment.

```bash
python -m ipykernel install \
  --user \
  --name ai-prompt-bootcamp \
  --display-name "Python (ai-prompt-bootcamp)"
```

---

## Environment Variables

Create a local `.env` file (this file is ignored by git):

```bash
cp .env.example .env
```

Edit `.env` and add your API key:

```env
OPENAI_API_KEY=YOUR_API_KEY_HERE
```

---

## Running the Lab

Start Jupyter Lab from the project root:

```bash
jupyter lab
```

Open notebooks in this order:

1. **`00_lab_sanity_test.ipynb`**
   Confirms your environment, kernel, and localhost networking are healthy.

2. **`01_prompt_lab.ipynb`**
   The main prompt engineering lab.

---

## Stopping Jupyter Cleanly

In the terminal running Jupyter:

```text
Ctrl + C
y
```

To confirm no servers are running:

```bash
jupyter server list
```

---

## Notes on `.ipynb_checkpoints`

Jupyter automatically creates `.ipynb_checkpoints/` directories for autosave recovery.

- These files are expected
- They are ignored via `.gitignore`
- Do not edit or commit them

---

## Version Control & Best Practices

- Virtual environments (`venv/`) are excluded from git
- Environment variables (`.env`) are excluded from git
- Notebooks are treated as **learning artifacts**, not production code
- Shared logic lives in `src/` to reduce notebook duplication

---

## Roadmap (Optional)

This starter is intentionally minimal. Possible future expansions include:

- LangChain prompt templates and chains
- Prompt evaluation and regression testing
- Agent-based workflows
- Dataset-driven experiments
- CI checks for notebook execution

---

## License

This project is intended for educational use.
Add a license file if you plan to distribute or monetize the course.

---

## Getting Help

If you encounter issues:

- Re-run `00_lab_sanity_test.ipynb`
- Verify your Python version and active kernel
- Confirm your `.env` file is correctly configured

---

Happy experimenting.
