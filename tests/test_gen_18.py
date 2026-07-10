from app.gen_18 import value_18


def test_value_18():
    assert value_18(2) == 2 * 5 + 6
    assert value_18(0) == 6
