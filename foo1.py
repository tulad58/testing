def search_filter():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    geo_log = []
    for el in geo_logs:
      if "Россия" in str(el.values()):
          geo_log.append(el)
    return geo_log


def foo2():
    ids = {
      'user1': [213, 213, 213, 15, 213],
      'user2': [54, 54, 119, 119, 119],
      'user3': [213, 98, 98, 35]
    }
    res = set()
    for values in ids.values():
      res.update(values)
    return list(res)


def word_search_percent():
    queries = [
      'смотреть сериалы онлайн', 'новости спорта', 'афиша кино', 'курс доллара',
      'сериалы этим летом', 'курс по питону', 'сериалы про спорт'
    ]
    res = []
    full = len(queries)
    count = {}
    for el in queries:
      if len(el.split()) not in count:
        count[len(el.split())] = 1
      else:
        count[len(el.split())] += 1

    for key, value in count.items():
        res.append(f"Поисковых запросов из {key} слов(а) - {round(value / full * 100)}%")
    return res


