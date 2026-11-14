# === Stage 4: Редактирование записей ===
# Project: TrailCare
from datetime import date


ALLOWED_TRAIL_FIELDS = ("name", "length", "state", "inspection_date")


class TrailUpdateError(ValueError):
    """Ошибка при некорректном обновлении участка."""


def _validate_trail(trail):
    if not isinstance(trail, dict):
        raise TrailUpdateError("Участок должен быть словарём")
    if "id" not in trail:
        raise TrailUpdateError("Участок не имеет идентификатора")
    for field in ALLOWED_TRAIL_FIELDS:
        if field not in trail:
            raise TrailUpdateError(f"Участок не имеет поля '{field}'")


def _coerce_length(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        raise TrailUpdateError("Длина должна быть числом")


def _coerce_date(value):
    if value is None:
        return None
    if isinstance(value, date) and value.year <= date.today().year:
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            raise TrailUpdateError("Дата проверки должна быть в формате ГГГГ-ММ-ДД")
    raise TrailUpdateError("Дата проверки должна быть строкой или датой")


def update_trail(trail, **changes):
    """Обновляет допустимые поля участка по идентификатору.

    Принимаются только поля из ALLOWED_TRAIL_FIELDS.
    """
    _validate_trail(trail)
    allowed = set(changes) & set(ALLOWED_TRAIL_FIELDS)
    if not allowed:
        raise TrailUpdateError("Нет допустимых полей для изменения")

    for field in allowed:
        if field == "length":
            trail[field] = _coerce_length(changes[field])
        elif field == "inspection_date":
            trail[field] = _coerce_date(changes[field])
        else:
            trail[field] = changes[field]

    return trail
