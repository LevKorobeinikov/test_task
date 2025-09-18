from collections import defaultdict
from csv import DictReader, Error
from pathlib import Path
from typing import Dict, List

from src.constants import FILE_NOT_FOUND, GRADE, STUDENT_NAME


def parse_csv_files(file_paths: List[Path]) -> Dict[str, List[int]]:
    """Читает несколько CSV-файлов.

    Args:
        file_paths: Список путей к CSV-файлам.

    Returns:
        Словарь {students_name: [grades]} с агрегированными оценками.

    Raises:
        ValueError: Если файл не найден или неверный формат.

    """
    student_grades = defaultdict(list)
    for file_path in file_paths:
        if not file_path.exists():
            raise FileNotFoundError(f'{FILE_NOT_FOUND} {file_path}')
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = DictReader(file)
                required_fields = {STUDENT_NAME, GRADE}
                if not required_fields.issubset(reader.fieldnames):
                    raise ValueError(
                        f'Файл {file_path} не содержит колонки: '
                        f'{required_fields - set(reader.fieldnames)}',
                    )
                for row in reader:
                    try:
                        grade = int(row[GRADE].strip())
                        if 1 <= grade <= 5:
                            student_grades[row[STUDENT_NAME].strip()].append(
                                grade,
                            )
                    except ValueError:
                        pass
        except Error as error:
            raise ValueError(f'Ошибка чтения {file_path}: {error}')
    return dict(student_grades)
