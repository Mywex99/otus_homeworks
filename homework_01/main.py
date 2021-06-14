"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    pow_list = [number**2 for number in args]
    return pow_list


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(list_of_numbers, props):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if props == "even":
        list_of_evens = (filter(lambda even: even % 2 == 0, list_of_numbers))
        return list(list_of_evens)
    elif props == "odd":
        list_of_odds = (filter(lambda odd: odd % 2 != 0, list_of_numbers))
        return list(list_of_odds)
    elif props == "prime":
        list_of_primes = []
        for number in list_of_numbers:
            if number > 1:
                for x in range(2, number):
                    if (number % x) == 0:
                        break
                else:
                    list_of_primes.append(number)
        return list_of_primes
