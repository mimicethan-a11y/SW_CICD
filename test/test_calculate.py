from calculate import add_f, sub_f, mut_f


def test_add_f():
    assert add_f(1, 2) == 3
    assert add_f(0, 0) == 0
    assert add_f(-1, -2) == -3


def test_sub_f():
    assert sub_f(2, 1) == 1
    assert sub_f(0, 0) == 0
    assert sub_f(-2, -1) == -1


def test_mut_f():
    assert mut_f(2, 1) == 1
    assert mut_f(0, 1) == 0
    assert mut_f(-2, -1) == 2
