def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
    p_s = (result, incorrect_data)
    return p_s


def calculate_average(numbers):
    try:
        if isinstance(numbers, str):
            for i in numbers:
                print(f'Некорректный тип данных для подсчёта суммы - {i}')
        average = personal_sum(numbers)[0]/(len(numbers) - personal_sum(numbers)[1])
        return average
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
