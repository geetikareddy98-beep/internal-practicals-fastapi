"""Assert behavior before relying on a refactoring."""

import pytest

from app.numeric import total


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], 0),
        ([None, None], 0),
        ([1, None, 2], 3),
        ([-4, None, 2], -2),
        ([1.5, None, 2.25], 3.75),
        ([0, None, 0], 0),
    ],
)
def test_total(values, expected):
    assert total(values) == pytest.approx(expected)


def test_total_does_not_modify_input():
    values = [1, None, 2]
    total(values)
    assert values == [1, None, 2]


def test_unsupported_string_raises():
    with pytest.raises(TypeError):
        total([1, "2"])


def test_decimal_precision():
    """Copilot suggested this case to account for floating-point rounding."""
    assert total([0.1, 0.2, None]) == pytest.approx(0.3)
