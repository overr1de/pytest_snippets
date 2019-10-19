import pytest


@pytest.mark.parametrize("a,b,result", [(1,2,3), (2,3,4), (3,3,7), (4,4,8)])
def test_summarize(a, b, result, skip_list):
    if 'test_summarize' in skip_list:
        pytest.skip('skipped!')
    assert sum([a, b]) == result
