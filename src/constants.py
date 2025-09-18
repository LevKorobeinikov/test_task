FILE_NOT_FOUND = 'Файл не найден: '
GRADE = 'grade'
STUDENT_NAME = 'student_name'
STUDENT_PERFORMANCE = 'student-performance'
DESCRIPTION_FOR_PARSER = (
    'Обработка файлов с данными об успеваемости студентов.'
)
FILES = '--files'
REPORT = '--report'
CONFIG = '--config'
HELP_FOR_FILES = 'Пути к CSV-файлам.'
HELP_FOR_REPORT = 'Название отчёта.'
LOGS = 'logs'
OUTPUT = 'output'
STDOUT = 'stdout'
INFO = 'INFO'
NO_DATA = 'Нет данных.'
TEST_SAMPLE = """student_name,subject,teacher_name,date,grade
Коробейникова Елена,Английский язык,Ковалева Анна,2023-10-10,5
Титов Владислав,География,Орлов Сергей,2023-10-12,4
Коробейникова Алина,Биология,Ткаченко Наталья,2023-10-15,5
Коробейникова Елена,Математика,Иванов Петр,2023-10-20,4
"""
TEST_PARSE = {
    'Коробейникова Елена': [5, 4],
    'Титов Владислав': [4],
    'Коробейникова Алина': [5],
}
TEST_INVALID_GRDE = """student_name,subject,teacher_name,date,grade
Test Student,Math,Teacher,2023-01-01,abc
"""
TEST_MISSING_COLUMNS = """name,subject,date,grade
Student,Math,2023-01-01,5
"""
