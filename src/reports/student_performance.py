from statistics import mean
from typing import List, Tuple

from src.constants import STUDENT_PERFORMANCE
from src.reports import BaseReport, register_report


@register_report(STUDENT_PERFORMANCE)
class StudentPerformanceReport(BaseReport):
    """Отчёт по успеваемости студентов.
    Cредняя оценка по всем предметам, сортировка по убыванию.
    """

    @staticmethod
    def generate(
        student_grades: dict[str, list[int]],
    ) -> List[Tuple[str, float]]:
        report_data = []
        for student, grades in student_grades.items():
            if grades:
                report_data.append((student, mean(grades)))
        report_data.sort(key=lambda x: x[1], reverse=True)
        return report_data
