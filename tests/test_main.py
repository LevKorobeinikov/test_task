import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import src.main as main_mod
from src.constants import STDOUT, STUDENT_PERFORMANCE
from src.main import main


@patch('src.main.tabulate', autospec=True)
@patch('src.main.parse_csv_files', autospec=True)
@patch('argparse.ArgumentParser', autospec=True)
def test_main_full_pipeline(
    mock_argparse_cls,
    mock_parse,
    mock_tabulate,
) -> None:
    """Полный пайплайн."""
    mock_args = MagicMock()
    mock_args.files = [Path('data.csv')]
    mock_args.report = STUDENT_PERFORMANCE
    mock_parser = mock_argparse_cls.return_value
    mock_parser.parse_args.return_value = mock_args
    mock_data = {'Test': [5]}
    mock_parse.return_value = mock_data
    mock_report_class = MagicMock()
    mock_report_class.generate.return_value = [('Test', 5.0)]
    main_mod.REPORT_REGISTRY.clear()
    main_mod.REPORT_REGISTRY[STUDENT_PERFORMANCE] = mock_report_class
    with patch.object(sys, STDOUT, new=MagicMock()):
        with patch(
            'src.main.save_csv',
            return_value=Path('out.csv'),
        ) as mock_save:
            main()
    mock_parse.assert_called_once_with(mock_args.files)
    mock_report_class.generate.assert_called_once_with(mock_data)
    mock_tabulate.assert_called_once()
    mock_save.assert_called_once()
