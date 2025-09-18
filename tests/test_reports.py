from src.reports.student_performance import (
    StudentPerformanceReport,
)


def test_generate_report() -> None:
    """Тест генерации отчёта."""
    assert StudentPerformanceReport.generate({
        'Student A': [5, 4, 5],
        'Student B': [3],
        'Student C': [],
    }) == [
        ('Student A', 4.666666666666667),
        ('Student B', 3.0),
    ]


def test_empty_data() -> None:
    """Тест пустых данных."""
    assert StudentPerformanceReport.generate({}) == []
