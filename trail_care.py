# === Stage 1: Каркас модуля ===
# Project: TrailCare
trailcare_terrain.py

from datetime import date


def create_demo_sections():
    return [
        Section(
            name="Лесная тропа к озеру",
            length=1200.0,
            condition="хорошее",
            checked_on=date(2024, 1, 15),
        ),
        Section(
            name="Песчаная тропа на перевал",
            length=3400.0,
            condition="плохое",
            checked_on=date(2024, 1, 10),
        ),
        Section(
            name="Лазерная разметка в ущелье",
            length=850.0,
            condition="среднее",
            checked_on=date(2024, 1, 20),
        ),
    ]


def main():
    sections = create_demo_sections()

    print("TrailCare — содержание троп")
    print("=" * 40)

    for section in sections:
        print(f"Участок: {section.name}")
        print(f"  Длина:      {section.length} м")
        print(f"  Состояние: {section.condition}")
        print(f"  Проверка:  {section.checked_on}")
        print("-" * 40)


if __name__ == "__main__":
    main()
