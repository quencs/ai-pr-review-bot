# AI PR Review Bot

AI-powered pull request reviewer for GitHub.

Automatically reviews pull requests using a local LLM and posts feedback directly on PRs.

Built with:

- vLLM
- GitHub Actions
- Python
- Local LLM

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