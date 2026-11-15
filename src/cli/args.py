import argparse
def get_parser():
    p = argparse.ArgumentParser(prog='git-analytics')
    p.add_argument('--repo', default='.')
    p.add_argument('--days', type=int, default=90)
    return p
