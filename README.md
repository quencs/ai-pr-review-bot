# AI PR Review Bot — Automatic Code Reviews with Local LLMs

Lightweight, open-source AI reviewer that comments directly on pull requests.

Works with:
- GitHub Actions
- Local LLM (vLLM)
- Python

🚀 No external API required

---

## Features

- automatic PR review
- hallucination filtering
- repo-aware analysis
- security risk detection
- performance suggestions
- line-by-line improvement suggestions

---

## Architecture

PR → diff analysis → symbol index → risk detection → AI review → GitHub comment

This design prevents LLM hallucinations by restricting analysis to real repository symbols.

---

## Quickstart

```bash
git clone https://github.com/quencs/ai-pr-review-bot
cd ai-pr-review-bot

pip install -r requirements.txt

python cli/review_pr.py
```

---

## Core Functions

### `generate_fix(code, issue)`

Generates a fixed version of code using the LLM based on the identified issue.

```python
def generate_fix(code, issue):
    prompt = f"""
You are a senior engineer.

Fix the issue in the following code.

Issue:
{issue}

Code:
{code}

Return ONLY the fixed code.
No explanation.
"""
    return ask_llm(prompt)
```

**Parameters:**
- `code` (str): The problematic code to fix
- `issue` (str): Description of the issue to fix

**Returns:**
- (str): Fixed code from the LLM

### `format_suggestion(fixed_code)`

Formats fixed code as a GitHub suggestion that can be applied directly to pull requests.

```python
def format_suggestion(fixed_code):
    return f"""```suggestion
{fixed_code}
```"""
```

**Parameters:**
- `fixed_code` (str): The corrected code to suggest

**Returns:**
- (str): Formatted GitHub suggestion markdown

---

## Roadmap

- [ ] PR summary generation
- [ ] inline code suggestions
- [ ] multi-language support
- [ ] plugin system