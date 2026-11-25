import pytest
pytest.importorskip("pydantic")
from src.parsers.log_parser import parse_raw_commit_line
def test_log_parser():
    line = 'abc1234|Geno|geno@test.com|1700000000|feat: init'
    c = parse_raw_commit_line(line)
    assert c.hash == 'abc1234'
    assert c.author == 'Geno'
