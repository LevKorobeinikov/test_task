from pathlib import Path

import pytest

from src.constants import TEST_INVALID_GRDE, TEST_MISSING_COLUMNS, TEST_PARSE
from src.data_parser import parse_csv_files


def test_parse_valid_csv(tmp_path: Path, sample_csv_data) -> None:
    """Тест  парсинга."""
    file_path = tmp_path / 'test.csv'
    file_path.write_text(sample_csv_data.getvalue())
    assert parse_csv_files([file_path]) == TEST_PARSE


def test_parse_invalid_grade(tmp_path: Path) -> None:
    """Тест игнора невалидных оценок."""
    file_path = tmp_path / 'invalid.csv'
    file_path.write_text(TEST_INVALID_GRDE)
    assert parse_csv_files([file_path]) == {}


def test_missing_file() -> None:
    """Тест отсутствующего файла."""
    with pytest.raises(FileNotFoundError):
        parse_csv_files([Path('nonexistent.csv')])


def test_missing_columns(tmp_path: Path) -> None:
    """Тест отсутствующих колонок."""
    file_path = tmp_path / 'bad_cols.csv'
    file_path.write_text(TEST_MISSING_COLUMNS)
    with pytest.raises(ValueError):
        parse_csv_files([file_path])
