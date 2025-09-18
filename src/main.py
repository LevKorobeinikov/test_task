import argparse
import logging
from pathlib import Path

from tabulate import tabulate

from src.constants import (
    CONFIG,
    DESCRIPTION_FOR_PARSER,
    FILES,
    HELP_FOR_FILES,
    HELP_FOR_REPORT,
    LOGS,
    NO_DATA,
    OUTPUT,
    REPORT,
)
from src.data_parser import parse_csv_files
from src.reports import REPORT_REGISTRY
from src.utils import save_csv, setup_logging


def main() -> None:
    """Основаная функция."""
    parser = argparse.ArgumentParser(
        description=DESCRIPTION_FOR_PARSER,
    )
    parser.add_argument(
        FILES,
        nargs='+',
        required=True,
        type=Path,
        help=HELP_FOR_FILES,
    )
    parser.add_argument(
        REPORT,
        required=True,
        choices=list(REPORT_REGISTRY.keys()),
        help=HELP_FOR_REPORT,
    )
    parser.add_argument(
        CONFIG,
        type=Path,
        help=HELP_FOR_FILES,
    )
    args = parser.parse_args()
    script_dir = Path(__file__).parent
    setup_logging(script_dir.parent / LOGS)
    args.files = [
        script_dir.parent / file if file.is_absolute() else file
        for file in args.files
    ]
    report_class = REPORT_REGISTRY[args.report]
    report_data = report_class.generate(parse_csv_files(args.files))
    logging.info(f'Отчёт: {args.report.upper()}')
    if not report_data:
        logging.info(NO_DATA)
        return
    table = [[name, f'{avg:.2f}'] for name, avg in report_data]
    output_dir = script_dir.parent / OUTPUT
    print(
        tabulate(
            table, headers=['Student', 'Average Grade'],
            tablefmt='grid',
            showindex=range(1, len(table) + 1),
        ),
    )
    logging.info(
        f'Отчёт сохранён в: {save_csv(report_data, output_dir, args.report)}',
    )


if __name__ == '__main__':
    main()
