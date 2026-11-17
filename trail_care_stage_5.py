# === Stage 5: Удаление и восстановление ===
# Project: TrailCare
from datetime import date


class TrailSection:
    """Участок тропы с мягким удалением и восстановлением."""

    def __init__(self, name, length, state, checked_on):
        self.name = name
        self.length = length
        self.state = state
        self.checked_on = checked_on
        self.deleted = False
        self.deleted_at = None

    def __repr__(self):
        return f"TrailSection(name={self.name!r}, deleted={self.deleted})"

    def restore(self):
        """Восстанавливает удалённый участок."""
        if self.deleted:
            self.deleted = False
            self.deleted_at = None
            return True
        return False

    def delete(self):
        """Мягкое удаление: сущность помечается, а не исчезает."""
        if not self.deleted:
            self.deleted = True
            self.deleted_at = date.today()
            return True
        return False


class TrailRepository:
    """Хранит участки с поддержкой мягкого удаления и восстановления."""

    def __init__(self):
        self._sections = []

    def add(self, section):
        self._sections.append(section)

    def get(self, name):
        for section in self._sections:
            if section.name == name:
                return section
        return None

    def list_active(self):
        return [s for s in self._sections if not s.deleted]

    def list_deleted(self):
        return [s for s in self._sections if s.deleted]

    def delete(self, name):
        section = self.get(name)
        if section is not None:
            section.delete()
            return True
        return False

    def restore(self, name):
        section = self.get(name)
        if section is not None:
            section.restore()
            return True
        return False

    def count(self):
        return len(self._sections)
