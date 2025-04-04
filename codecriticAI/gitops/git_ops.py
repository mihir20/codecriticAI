import subprocess
from pathlib import Path

class GitOps:
    def __init__(self, repo_path: Path = None, base_branch: str = 'master'):
        self.repo_path = repo_path or Path.cwd()
        self.base_branch = base_branch

    def get_git_diff(self) -> str:
        try:
            diff = subprocess.check_output(
                ['git', 'diff', '-u', self.base_branch, '--', self.repo_path],
                stderr=subprocess.STDOUT
            )
            return diff.decode('utf-8')
        except subprocess.CalledProcessError as e:
            print(f"Error getting git diff: {e.output.decode('utf-8')}")
            exit(1)