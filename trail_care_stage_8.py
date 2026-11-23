# === Stage 8: Генерация идентификаторов ===
# Project: TrailCare
"""Модуль TrailCare.id: генерация уникальных идентификаторов с префиксом проекта.

Идентификаторы имеют вид trailcare-<6 символов>.
Функция generate_id создаёт уникальный id, проверяя его на коллизию
с уже сгенерированными идентификаторами через переданный колбэк.
"""

import random
import string

PROJECT_PREFIX = "trailcare"


def generate_id(existing_ids=None):
    """Сгенерировать уникальный идентификатор с префиксом проекта.

    existing_ids: набор или итерируемый объект уже занятых идентификаторов.
    Возвращает строку вида 'trailcare-<6 символов>'.
    """
    existing = set(existing_ids) if existing_ids is not None else set()
    while True:
        random_string = "".join(random.choices(string.ascii_letters + string.digits, k=6))
        candidate = f"{PROJECT_PREFIX}-{random_string}"
        if candidate not in existing:
            existing.add(candidate)
            return candidate


def make_batch(count=10, existing_ids=None):
    """Сгенерировать список из count уникальных идентификаторов.

    existing_ids: начальный набор занятых идентификаторов.
    """
    existing = set(existing_ids) if existing_ids is not None else set()
    batch = []
    for _ in range(count):
        batch.append(generate_id(existing))
    return batch


if __name__ == "__main__":
    print(generate_id())
    print(generate_id({"trailcare-abc123"}))
    print(make_batch(5))
    print(make_batch(5, existing_ids={"trailcare-abc123"}))
