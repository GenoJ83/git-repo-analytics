def filter_by_author(commits: list, author_name: str):
    return [c for c in commits if author_name.lower() in c.author.lower()]
