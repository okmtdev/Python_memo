from my_funcs import add, sub


def test_add():
    assert add(1, 2) == 3


def test_sub():
    assert sub(3, 1) == 2


class TestCase:
    def test_true(self):
        assert True

    def test_add_zero(self):
        assert add(1, 0) == 1