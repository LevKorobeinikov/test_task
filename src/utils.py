import csv
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Tuple

from src.constants import INFO


def setup_logging(log_dir: Path, log_level: str = INFO) -> None:
    """Логирование в консоль и файл.

    Args:
        log_dir: Папка для логов.
        log_level: Уровень логов.

    """
    log_dir.mkdir(exist_ok=True)
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(
                log_dir / f'app_{datetime.now()}.log',
                encoding='utf-8',
            ),
            logging.StreamHandler(),
        ],
    )


def save_csv(
    report_data: List[Tuple[str, float]],
    output_dir: Path,
    report_name: str,
) -> Path:
    """Сохраняет данные отчета в фай.

    Args:
        report_data: Список кортежей.
        output_dir:  Путь для сохранения.
        report_name:  Название отчета.

    Returns:
        Path: Путь к файлу.

    """
    output_dir.mkdir(exist_ok=True)
    csv_file = output_dir / f'{report_name}_{datetime.now()}.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Student', 'Average Grade'])
        for name, avg in report_data:
            writer.writerow([name, f'{avg:.2f}'])
    return csv_file
