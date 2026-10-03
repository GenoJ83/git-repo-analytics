from pydantic import BaseModel
class GitCommit(BaseModel):
    hash: str
    author: str
    email: str
    timestamp: int
    message: str
    insertions: int = 0
    deletions: int = 0
