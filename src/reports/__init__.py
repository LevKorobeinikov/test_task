from typing import Dict, Type

from src.constants import STUDENT_PERFORMANCE
from src.reports.student_performance import StudentPerformanceReport

REPORT_REGISTRY: Dict[str, Type[StudentPerformanceReport]] = {
    STUDENT_PERFORMANCE: StudentPerformanceReport,
    # Добавьте новые: 'teacher-performance': TeacherPerformanceReport,
}
