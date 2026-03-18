def generate_fix(llm, code, issue):
    prompt = f"""
You are a senior engineer.

Fix the issue in the following code.

Issue:
{issue}

Code:
{code}

Return ONLY the fixed code.
"""
    return llm(prompt)

def validate_fix(llm, original, fix):
    prompt = f"""
Check if the fix correctly resolves the issue.

Original:
{original}

Fix:
{fix}

Answer YES or NO only.
"""
    result = llm(prompt)
    return "YES" in result.upper()

def format_suggestion(fixed_code):
    return f"""```suggestion
{fixed_code}
```"""