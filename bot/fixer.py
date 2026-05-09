from queue import Queue
from threading import Thread

DEFAULT_LLM_TIMEOUT_SECONDS = 30


def _call_llm_with_timeout(llm, prompt, timeout_seconds=DEFAULT_LLM_TIMEOUT_SECONDS):
    """Call an LLM function with a bounded wait and clear error handling."""
    if timeout_seconds is None:
        return llm(prompt)

    result_queue = Queue(maxsize=1)

    def run_llm():
        try:
            result_queue.put((True, llm(prompt)))
        except Exception as exc:
            result_queue.put((False, exc))

    worker = Thread(target=run_llm, daemon=True)
    worker.start()
    worker.join(timeout_seconds)

    if worker.is_alive():
        raise TimeoutError(f"LLM call timed out after {timeout_seconds} seconds")

    succeeded, result = result_queue.get()
    if succeeded:
        return result
    raise result


def generate_fix(llm, code, issue, timeout_seconds=DEFAULT_LLM_TIMEOUT_SECONDS):
    prompt = f"""
You are a senior engineer.

Fix the issue in the following code.

Issue:
{issue}

Code:
{code}

Return ONLY the fixed code.
"""
    try:
        return _call_llm_with_timeout(llm, prompt, timeout_seconds)
    except Exception:
        return code


def validate_fix(llm, original, fix, timeout_seconds=DEFAULT_LLM_TIMEOUT_SECONDS):
    prompt = f"""
Check if the fix correctly resolves the issue.

Original:
{original}

Fix:
{fix}

Answer YES or NO only.
"""
    try:
        result = _call_llm_with_timeout(llm, prompt, timeout_seconds)
    except Exception:
        return False

    return "YES" in str(result).upper()


def format_suggestion(fixed_code):
    return f"""```suggestion
{fixed_code}
```"""
