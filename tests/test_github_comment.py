import unittest
from unittest.mock import patch, Mock
from github_comment_bot import GitHubCommentBot  # Assuming this is the correct import

class TestGitHubCommentBot(unittest.TestCase):
    def setUp(self):
        self.bot = GitHubCommentBot("mock_repo", "mock_owner", "mock_token")

    @patch('github_comment_bot.requests.post')
    def test_comment_success(self, mock_post):
        # Mock a successful response
        mock_post.return_value = Mock(status_code=200)
        
        response = self.bot.comment_on_pr(1, "Great work!")
        self.assertEqual(response.status_code, 200)
        mock_post.assert_called_once()

    @patch('github_comment_bot.requests.post')
    def test_comment_failure(self, mock_post):
        # Mock a failure response
        mock_post.return_value = Mock(status_code=400, text="Bad Request")
        
        response = self.bot.comment_on_pr(1, "This comment should fail.")
        self.assertEqual(response.status_code, 400)
        self.assertIn("Bad Request", response.text)

    @patch('github_comment_bot.requests.post')
    def test_authentication_error(self, mock_post):
        # Mock an authentication error response
        mock_post.return_value = Mock(status_code=401, text="Unauthorized")
        
        response = self.bot.comment_on_pr(1, "Trying to comment without auth.")
        self.assertEqual(response.status_code, 401)
        self.assertIn("Unauthorized", response.text)

    @patch('github_comment_bot.requests.post')
    def test_http_error_handling(self, mock_post):
        # Mock an HTTP 500 error response
        mock_post.return_value = Mock(status_code=500, text="Internal Server Error")
        
        response = self.bot.comment_on_pr(1, "This should handle server errors.")
        self.assertEqual(response.status_code, 500)
        self.assertIn("Internal Server Error", response.text)

if __name__ == "__main__":
    unittest.main()