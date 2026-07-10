from app.gen_29 import value_29


def test_value_29():
    assert value_29(2) == 2 * 5 + 3
    assert value_29(0) == 3
