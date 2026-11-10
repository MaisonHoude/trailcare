# === Stage 3: Хранилище в памяти ===
# Project: TrailCare
from datetime import date

class TrailSection:
    def __init__(self, name, length, status, checked_date):
        self.id = None
        self.name = name
        self.length = length
        self.status = status
        self.checked_date = checked_date

    def __repr__(self):
        return f"TrailSection(id={self.id}, name={self.name!r}, length={self.length}, status={self.status!r}, checked_date={self.checked_date})"


class TrailSectionStore:
    def __init__(self):
        self._sections = {}
        self._counter = 0

    def add(self, name, length, status, checked_date):
        self._counter += 1
        section = TrailSection(name, length, status, checked_date)
        section.id = self._counter
        self._sections[section.id] = section
        return section

    def get(self, section_id):
        return self._sections.get(section_id)

    def list_all(self):
        return list(self._sections.values())


if __name__ == "__main__":
    store = TrailSectionStore()
    first = store.add("Лесная тропа", 120, "хорошо", date(2024, 5, 14))
    second = store.add("Речной берег", 80, "плохо", date(2024, 5, 15))
    third = store.add("Холмистый подъём", 200, "нормально", date(2024, 5, 16))

    print("Добавлено участков:", len(store.list_all()))
    print("Первый участок:", first)
    print("Получен по id 2:", store.get(2))
    print("Получен по id 999:", store.get(999))
    print("Список всех участков:")
    for section in store.list_all():
        print(section)
