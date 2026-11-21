# === Stage 7: Связи между сущностями ===
# Project: TrailCare
trail_works = [
    {"id": "w1", "trail_id": "trailA", "type": "debris", "status": "done"},
    {"id": "w2", "trail_id": "trailB", "type": "marker", "status": "pending"},
    {"id": "w3", "trail_id": "trailA", "type": "cut", "status": "in_progress"},
    {"id": "w4", "trail_id": "trailC", "type": "debris", "status": "pending"},
]

trail_sections = [
    {"id": "trailA", "name": "Северный холм", "length": 1200, "status": "good", "checked_on": "2024-01-15"},
    {"id": "trailB", "name": "Лесная роща", "length": 800, "status": "ok", "checked_on": "2024-01-16"},
    {"id": "trailC", "name": "Ручей", "length": 500, "status": "ok", "checked_on": "2024-01-17"},
]


def get_trail_works(trail_id):
    """Получить все работы для участка и проверить целостность связи."""
    works = [w for w in trail_works if w.get("trail_id") == trail_id]
    return works


def check_integrity(trail_id):
    """Проверить, что все работы относятся к существующим участкам."""
    valid_trails = {t["id"] for t in trail_sections}
    problems = []
    for work in trail_works:
        if work.get("trail_id") not in valid_trails:
            problems.append(f"Работа {work['id']} ссылается на несуществующий участок {work['trail_id']}")
    return problems


def volunteer_works(trail_id):
    """Получить работы участника по участку."""
    volunteer_id = "vol1"
    trail = next((t for t in trail_sections if t["id"] == trail_id), None)
    if not trail:
        return []
    return [w for w in trail_works if w.get("trail_id") == trail_id]


def trail_works_summary(trail_id):
    """Сводка по работам на участке."""
    works = get_trail_works(trail_id)
    problems = check_integrity(trail_id)
    return {
        "trail_id": trail_id,
        "works_count": len(works),
        "problems": problems,
    }


if __name__ == "__main__":
    print(trail_works_summary("trailA"))
    print(trail_works_summary("trailB"))
    print(trail_works_summary("trailZ"))
