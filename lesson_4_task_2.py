def test_iter(*args):
    prev = -1 * float('inf')
    for num in args:
        if num > prev:
            yield num
        prev = num
    pass


if __name__ == '__main__':
    assert list(test_iter(1, 2, 3, 4, 5, 6, 7, 8,)) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert list(test_iter(-1, 3, 6, 12, -5, 0, 2, 7)) == [-1, 3, 6, 12, 0, 2, 7];