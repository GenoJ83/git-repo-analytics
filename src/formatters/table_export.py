def format_top_contributors(authors: dict) -> str:
    sorted_authors = sorted(authors.items(), key=lambda x: x[1], reverse=True)[:10]
    return '\n'.join(f'{name}: {count} commits' for name, count in sorted_authors)
