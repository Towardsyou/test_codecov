import pytest

from test_codecov.calculator import add, divide, is_even


def test_add_returns_sum_of_two_numbers():
    assert add(2, 3) == 5


def test_divide_returns_quotient():
    assert divide(8, 2) == 4


def test_divide_rejects_zero_divisor():
    with pytest.raises(ValueError, match="divisor cannot be zero"):
        divide(8, 0)


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (2, True),
        (3, False),
        (0, True),
    ],
)
def test_is_even_identifies_even_numbers(number, expected):
    assert is_even(number) is expected

