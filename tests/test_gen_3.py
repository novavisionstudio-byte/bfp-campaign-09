from app.gen_3 import value_3


def test_value_3():
    assert value_3(2) == 2 * 6 + 2
    assert value_3(0) == 2
