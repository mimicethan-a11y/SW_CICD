from calculate import add_f


def test_add_f():
    assert add_f(1, 2) == 3
    assert add_f(0, 0) == 0
    assert add_f(-1, -2) == -3
