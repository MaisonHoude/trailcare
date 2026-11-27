# === Stage 10: Сортировка записей ===
# Project: TrailCare
def sort_sections(records, key="name", reverse=False):
    """Возвращает список участков, отсортированный по названию и дате проверки.

    Сортировка устойчивая: сначала по названию, затем по дате проверки,
    с возможностью изменения порядка по возрастанию или убыванию.
    """
    def sort_key(item):
        section, created, checked = item
        name = section.get("name", "")
        date_checked = section.get("checked_date")
        return (name.lower(), date_checked if date_checked else "")

    return sorted(records, key=sort_key, reverse=reverse)


def sort_sections_by_created(records, reverse=False):
    """Возвращает список участков, отсортированный по дате создания.

    Сортировка устойчивая: сначала по дате проверки, затем по дате создания,
    с возможностью изменения порядка по возрастанию или убыванию.
    """
    def sort_key(item):
        section, created, checked = item
        date_checked = section.get("checked_date")
        date_created = created if created else ""
        return (date_checked if date_checked else "", date_created)

    return sorted(records, key=sort_key, reverse=reverse)


if __name__ == "__main__":
    sample = [
        (
            {"name": "Северная тропа", "checked_date": "2024-05-01"},
            "2024-01-15",
            "2024-05-01",
        ),
        (
            {"name": "Южная тропа", "checked_date": "2024-03-10"},
            "2024-01-10",
            "2024-03-10",
        ),
        (
            {"name": "Западная тропа", "checked_date": "2024-04-20"},
            "2024-02-01",
            "2024-04-20",
        ),
    ]

    print("По названию (возрастание):")
    for record in sort_sections(sample):
        print(record[0]["name"], record[2])

    print("По названию (убывание):")
    for record in sort_sections(sample, reverse=True):
        print(record[0]["name"], record[2])

    print("По дате создания (возрастание):")
    for record in sort_sections_by_created(sample):
        print(record[0]["name"], record[1])

    print("По дате создания (убывание):")
    for record in sort_sections_by_created(sample, reverse=True):
        print(record[0]["name"], record[1])
