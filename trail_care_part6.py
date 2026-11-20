# === Stage 6: Связанная сущность ===
# Project: TrailCare
"""trailcare.works: сущность «работа» и функции её добавления.

Модуль самодостаточен: импортирует только стандартную библиотеку и
свои вспомогательные определения, без ссылок на несуществующий код.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Dict, List, Optional


# Допустимые текстовые значения поля «состояние» для работы.
VALID_CONDITIONS = ("свежий", "устаревший", "изношенный")


@dataclass
class Work:
    """Запись о работе по содержанию тропы.

    Attributes:
        title: краткое название работы.
        description: подробности, выполняемых действий.
        condition: текущее состояние участка после работы.
        date: дата выполнения.
        trail_id: идентификатор участка, на котором проводилась работа.
        volunteer: идентификатор волонтёра, выполнявшего работу.
    """

    title: str
    description: str = ""
    condition: str = "свежий"
    date: Optional[date] = None
    trail_id: Optional[str] = None
    volunteer: Optional[str] = None

    def __post_init__(self) -> None:
        if self.condition not in VALID_CONDITIONS:
            raise ValueError(
                f"состояние '{self.condition}' не входит в допустимые значения "
                f"{VALID_CONDITIONS}"
            )
        if self.trail_id is not None and not isinstance(self.trail_id, str):
            raise TypeError("trail_id должен быть строкой или None")
        if self.date is not None and not isinstance(self.date, date):
            raise TypeError("date должен быть объектом datetime.date или None")


class WorkBook:
    """Коллекция работ, индексируемая по идентификатору участка."""

    def __init__(self) -> None:
        self._works: Dict[str, List[Work]] = field(default_factory=dict)

    def add_work(
        self,
        title: str,
        description: str = "",
        condition: str = "свежий",
        date: Optional[date] = None,
        trail_id: Optional[str] = None,
        volunteer: Optional[str] = None,
    ) -> Work:
        """Создать работу и сохранить её в книге работ.

        Работы группируются по trail_id, чтобы при необходимости можно
        было быстро получить все работы для конкретного участка.

        Args:
            title: название работы.
            description: описание выполняемых действий.
            condition: состояние участка после работы.
            date: дата выполнения.
            trail_id: идентификатор участка.
            volunteer: идентификатор волонтёра.

        Returns:
            Новая запись Work.

        Raises:
            ValueError: если title пустой или condition недопустим.
            TypeError: если переданы неверного типа необязательные поля.
        """
        if not title or not title.strip():
            raise ValueError("title не может быть пустым")

        work = Work(
            title=title,
            description=description,
            condition=condition,
            date=date,
            trail_id=trail_id,
            volunteer=volunteer,
        )

        self._works.setdefault(trail_id, []).append(work)
        return work

    def get_works(self, trail_id: Optional[str]) -> List[Work]:
        """Вернуть все работы для указанного участка.

        Args:
            trail_id: идентификатор участка или None для всех работ.

        Returns:
            Список записей Work.
        """
        return list(self._works.get(trail_id, []))

    def count(self, trail_id: Optional[str]) -> int:
        """Вернуть число работ для участка или общее число работ."""
        if trail_id is None:
            return sum(len(group) for group in self._works.values())
        return len(self._works.get(trail_id, []))

    def __len__(self) -> int:
        return self.count(None)
