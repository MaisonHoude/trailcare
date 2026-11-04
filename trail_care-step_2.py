# === Stage 2: Проверка полей ===
# Project: TrailCare
module = "trailcare"

class TrailSection:
    def __init__(self, name, length, state, check_date):
        self.name = normalize_name(name)
        self.length = normalize_length(length)
        self.state = normalize_state(state)
        self.check_date = normalize_date(check_date)

    def __str__(self):
        return (f"Участок '{self.name}', длина {self.length}, "
                f"состояние '{self.state}', проверка {self.check_date}")


def normalize_name(name):
    if name is None:
        raise ValueError("Название участка обязательно")
    name = str(name).strip()
    if not name:
        raise ValueError("Название участка не может быть пустым")
    return name


def normalize_length(length):
    if length is None:
        raise ValueError("Длина участка обязательна")
    try:
        value = float(length)
    except (TypeError, ValueError):
        raise ValueError("Длина должна быть числом")
    if value <= 0:
        raise ValueError("Длина участка должна быть положительной")
    return value


def normalize_state(state):
    if state is None:
        raise ValueError("Состояние участка обязательно")
    state = str(state).strip().lower()
    valid = {"хорошее", "среднее", "плохое", "проходимое", "заблокированное", "завалено"}
    if state not in valid:
        raise ValueError(
            f"Недопустимое состояние '{state}'. "
            f"Допустимые: {', '.join(sorted(valid))}"
        )
    return state


def normalize_date(check_date):
    if check_date is None:
        raise ValueError("Дата проверки обязательна")
    try:
        return str(check_date).strip()
    except (TypeError, ValueError):
        raise ValueError("Дата проверки должна быть строкой в формате ДД.ММ.ГГГГ")
