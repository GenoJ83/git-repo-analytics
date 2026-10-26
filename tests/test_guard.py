import pytest
from src.security.git_guard import ensure_git_repo
def test_git_guard():
    with pytest.raises(ValueError):
        ensure_git_repo('/tmp/nonexistent_git_dir_1234')
