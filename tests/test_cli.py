from src.cli.args import get_parser
def test_cli():
    p = get_parser()
    args = p.parse_args(['--days', '30'])
    assert args.days == 30
