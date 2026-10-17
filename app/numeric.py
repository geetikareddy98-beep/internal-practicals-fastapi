"""Numeric refactoring exercise from Exam 2."""


def total(values: list[int | float | None]) -> int | float:
    """Sum numeric values, ignoring None entries.

    Args:
        values: Integers, floats and None entries.

    Returns:
        Their sum, or zero for an empty or all-None list.

    Raises:
        TypeError: If an unsupported value such as a string is added.
    """
    return sum(value for value in values if value is not None)
