from pytest import mark

from regroup import regroup

a = ['a' + str(n) for n in range(1, 7)]
b = ['b' + str(n) for n in range(1, 5)]
c = ['c' + str(n) for n in range(1, 6)]


@mark.parametrize(
    'n, groups, expected',
    [
        (2, [[1, 2], [3, 4], [5, 6]], ([1, 3, 5], [2, 4, 6])),
        (3, [[1, 2], [3, 4], [5, 6]], ([1, 4], [2, 5], [3, 6])),
        (4, [list(range(7))], ([0, 4], [1, 5], [2, 6], [3])),
        (
            3,
            [a, b, c],
            (
                ['a1', 'a4', 'b1', 'b4', 'c3'],
                ['a2', 'a5', 'b2', 'c1', 'c4'],
                ['a3', 'a6', 'b3', 'c2', 'c5'],
            ),
        ),
        (
            2,
            [a, b, c],
            (
                ['a1', 'a3', 'a5', 'b1', 'b3', 'c1', 'c3', 'c5'],
                ['a2', 'a4', 'a6', 'b2', 'b4', 'c2', 'c4'],
            ),
        ),
        (
            4,
            [a, b, c],
            (
                ['a1', 'a5', 'b3', 'c3'],
                ['a2', 'a6', 'b4', 'c4'],
                ['a3', 'b1', 'c1', 'c5'],
                ['a4', 'b2', 'c2'],
            ),
        ),
        (
            5,
            [a, b, c],
            (
                ['a1', 'a6', 'c1'],
                ['a2', 'b1', 'c2'],
                ['a3', 'b2', 'c3'],
                ['a4', 'b3', 'c4'],
                ['a5', 'b4', 'c5'],
            ),
        ),
        (
            6,
            [a, b, c],
            (
                ['a1', 'b1', 'c3'],
                ['a2', 'b2', 'c4'],
                ['a3', 'b3', 'c5'],
                ['a4', 'b4'],
                ['a5', 'c1'],
                ['a6', 'c2'],
            ),
        ),
    ],
)
def test_regroup(n, groups, expected):
    got = regroup(n, groups)
    assert got == expected
