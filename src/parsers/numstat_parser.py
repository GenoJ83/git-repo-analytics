def parse_numstat_line(line: str):
    parts = line.split('\t')
    if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit():
        return int(parts[0]), int(parts[1]), parts[2]
    return 0, 0, None
