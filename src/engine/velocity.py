import collections
def group_commits_by_week(commits: list):
    weeks = collections.defaultdict(int)
    for c in commits:
        week_num = c.timestamp // (7 * 86400)
        weeks[week_num] += 1
    return dict(weeks)
