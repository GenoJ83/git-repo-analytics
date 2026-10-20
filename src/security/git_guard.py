import os
def ensure_git_repo(path: str) -> bool:
    if not os.path.exists(os.path.join(path, '.git')):
        raise ValueError('Target path is not a valid git repository')
    return True
