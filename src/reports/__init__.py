import pkgutil
from abc import ABC, abstractmethod
from importlib import import_module
from pathlib import Path
from typing import Dict, Type

REPORT_REGISTRY: Dict[str, Type['BaseReport']] = {}


class BaseReport(ABC):
    """Контракт для отчётов."""

    @staticmethod
    @abstractmethod
    def generate(
        student_grades: dict[str, list[int]],
    ) -> list[tuple[str, float]]: ...


def register_report(name: str):
    """Декоратор для регистрации класса отчёта в REPORT_REGISTRY."""

    def decorator(cls):
        REPORT_REGISTRY[name] = cls
        return cls

    return decorator


def load_reports(package_name: str = __name__):
    """Импортирует все модули в пакете, чтобы регистрировались классы."""
    pkg = import_module(package_name)
    for finder, modname, ispkg in pkgutil.iter_modules([
        str(Path(pkg.__file__).parent),
    ]):
        if modname.startswith('_'):
            continue
        import_module(f'{package_name}.{modname}')
