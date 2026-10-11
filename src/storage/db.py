def store_commit_snapshot(path: str, data: str):
    with open(path, 'w') as f: f.write(data)
