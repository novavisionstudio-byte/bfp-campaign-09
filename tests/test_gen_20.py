from app.gen_20 import value_20


def test_value_20():
    assert value_20(2) == 2 * 4 + 9
    assert value_20(0) == 9
