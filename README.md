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

## Roadmap

- [ ] PR summary generation
- [ ] inline code suggestions
- [ ] multi-language support
- [ ] plugin system
