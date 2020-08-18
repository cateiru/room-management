import pytest

from src.operation import surveillance


@pytest.mark.parametrize(
    'people, light, status, output', [
        (True, 100, 0, 2),
        (True, 150, 2, 0),
        (True, 40, 2, 1),
        (False, 40, 1, 0),
        (True, 40, 1, 0),
        (True, 60, 1, 2)
    ]
)
def test_surveillance(people: bool, light: int, status: int, output: int):
    assert surveillance(people, light, status) == output
