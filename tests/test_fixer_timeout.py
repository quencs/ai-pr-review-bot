import time
import unittest

from bot.fixer import generate_fix, validate_fix


class TestFixerTimeoutHandling(unittest.TestCase):
    def test_generate_fix_returns_llm_output_when_call_succeeds(self):
        def llm(prompt):
            self.assertIn("Fix the issue", prompt)
            return "fixed code"

        self.assertEqual(generate_fix(llm, "bad code", "bug"), "fixed code")

    def test_generate_fix_returns_original_code_when_llm_times_out(self):
        def slow_llm(prompt):
            time.sleep(0.05)
            return "late fix"

        original_code = "bad code"
        self.assertEqual(
            generate_fix(slow_llm, original_code, "bug", timeout_seconds=0.01),
            original_code,
        )

    def test_generate_fix_returns_original_code_when_llm_raises(self):
        def failing_llm(prompt):
            raise RuntimeError("LLM unavailable")

        original_code = "bad code"
        self.assertEqual(generate_fix(failing_llm, original_code, "bug"), original_code)

    def test_validate_fix_returns_false_when_llm_times_out(self):
        def slow_llm(prompt):
            time.sleep(0.05)
            return "YES"

        self.assertFalse(validate_fix(slow_llm, "bad", "fixed", timeout_seconds=0.01))

    def test_validate_fix_returns_false_when_llm_raises(self):
        def failing_llm(prompt):
            raise RuntimeError("LLM unavailable")

        self.assertFalse(validate_fix(failing_llm, "bad", "fixed"))


if __name__ == "__main__":
    unittest.main()
