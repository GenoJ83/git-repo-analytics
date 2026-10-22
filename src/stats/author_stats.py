import collections
def summarize_authors(commits: list):
    counts = collections.Counter(c.author for c in commits)
    return dict(counts)
