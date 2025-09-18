from io import StringIO

import pytest

from src.constants import TEST_SAMPLE


@pytest.fixture
def sample_csv_data() -> StringIO:
    """Фикстура с тестовыми CSV-данными в памяти."""
    return StringIO(TEST_SAMPLE)
