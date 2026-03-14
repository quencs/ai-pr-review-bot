import requests

class GitHubCommentBot:
    def __init__(self, repo_owner, repo_name):
        self.repo_owner = repo_owner
        self.repo_name = repo_name

    def post_comment(self, issue_number, comment, token):
        url = f'https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/issues/{issue_number}/comments'
        headers = {'Authorization': f'token {token}', 'Accept': 'application/vnd.github.v3+json'}
        try:
            response = requests.post(url, json={'body': comment}, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'An error occurred: {err}') 

# Example usage
#bot = GitHubCommentBot('owner_name', 'repo_name')
#bot.post_comment(issue_number=1, comment='This is a comment.', token='your_access_token')
