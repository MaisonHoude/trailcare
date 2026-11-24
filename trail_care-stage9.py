# === Stage 9: Фильтрация записей ===
# Project: TrailCare
from datetime import date


def filter_sections_by_length(sections, min_length=None, max_length=None):
    result = []
    for section in sections:
        if min_length is not None and section['length'] < min_length:
            continue
        if max_length is not None and section['length'] > max_length:
            continue
        result.append(section)
    return result


def filter_sections_by_date_range(sections, start_date=None, end_date=None):
    result = []
    for section in sections:
        check_date = section['check_date']
        if start_date is not None and check_date < start_date:
            continue
        if end_date is not None and check_date > end_date:
            continue
        result.append(section)
    return result


def filter_sections(sections, min_length=None, max_length=None,
                    start_date=None, end_date=None):
    filtered_by_length = filter_sections_by_length(sections,
                                                    min_length, max_length)
    filtered_by_date = filter_sections_by_date_range(filtered_by_length,
                                                     start_date, end_date)
    return filtered_by_date


if __name__ == '__main__':
    demo_sections = [
        {'name': 'Северная', 'length': 1200, 'state': 'хорошо',
         'check_date': date(2024, 1, 15)},
        {'name': 'Западная', 'length': 800, 'state': 'плохо',
         'check_date': date(2024, 2, 20)},
        {'name': 'Восточная', 'length': 2500, 'state': 'средне',
         'check_date': date(2024, 3, 10)},
        {'name': 'Южная', 'length': 1500, 'state': 'хорошо',
         'check_date': date(2023, 11, 5)},
    ]

    print('Длиной от 1000 до 2000:')
    for section in filter_sections(demo_sections, 1000, 2000):
        print(f"  {section['name']} ({section['length']} м)")

    print('Проверенные с 1 января 2024:')
    for section in filter_sections(demo_sections, start_date=date(2024, 1, 1)):
        print(f"  {section['name']} ({section['check_date']})")

    print('Длиной от 1000 до 2000 и проверенные в 2024:')
    for section in filter_sections(demo_sections, 1000, 2000,
                                   start_date=date(2024, 1, 1),
                                   end_date=date(2024, 12, 31)):
        print(f"  {section['name']} ({section['length']} м, "
              f"{section['check_date']})")
