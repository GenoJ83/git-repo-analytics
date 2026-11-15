from src.models.commit import GitCommit
def parse_raw_commit_line(line: str):
    parts = line.strip().split('|')
    if len(parts) >= 5:
        return GitCommit(hash=parts[0], author=parts[1], email=parts[2], timestamp=int(parts[3]), message=parts[4])
    return None
