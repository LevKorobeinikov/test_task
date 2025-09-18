from statistics import mean
from typing import List, Tuple


class StudentPerformanceReport:
    """Отчёт по успеваемости студентов.
    Cредняя оценка по всем предметам, сортировка по убыванию.
    """

    @staticmethod
    def generate(
        student_grades: dict[str, list[int]],
    ) -> List[Tuple[str, float]]:
        """Генерирует отчёт.

        Args:
            student_grades: {student_name: [grades]} из data_parser.

        Returns:
            List[(str, float)] — отсортированный список.

        Notes:
            Если у студента нет оценок, он исключается из отчёта.

        """
        report_data = []
        for student, grades in student_grades.items():
            if grades:
                report_data.append((student, mean(grades)))
        report_data.sort(key=lambda x: x[1], reverse=True)
        return report_data
