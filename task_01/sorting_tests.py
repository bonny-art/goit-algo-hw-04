"""
Модуль для тестування та порівняння ефективності алгоритмів сортування.
Цей модуль генерує дані різних розмірів, запускає алгоритми сортування 
і виводить результати в текстовому вигляді, а також побудовує графік для 
порівняння часу виконання.

Алгоритми:
- Сортування злиттям
- Сортування вставками
- Бульбашкове сортування (базове)
- Оптимізоване бульбашкове сортування
- Timsort (вбудоване в Python)
"""

import random
import timeit

# pylint: disable=import-error
import matplotlib.pyplot as plt

from sorting_algorithms.bubble_sort_basic import bubble_sort_basic
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.bubble_sort_optimized import bubble_sort_optimized
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.helpers import create_almost_sorted_data, format_time

def reset_data() -> dict:
    """Скидає дані для тестування.

    Returns:
        dict: Словник з копіями даних різних розмірів.
    """
    return {
        "tiny_data_copy": tiny_data[:],
        "small_data_copy": small_data[:],
        "medium_data_copy": medium_data[:],
        "large_data_copy": large_data[:],
        "almost_sorted_data_copy": almost_sorted_data[:]
    }

def run_tests() -> None:
    """Запускає тести для порівняння алгоритмів сортування.

    Виводить результати тестування у текстовому вигляді 
    та будує графік часу виконання для кожного алгоритму.
    """
    sizes = [
        "Tiny (10)",
        "Small (100)",
        "Medium (1000)",
        "Large (10000)",
        "Almost Sorted (10000)"
    ]
    data_keys = [
        "tiny_data_copy", 
        "small_data_copy", 
        "medium_data_copy", 
        "large_data_copy", 
        "almost_sorted_data_copy"
    ]
    algorithms = [
        "Merge Sort",
        "Insertion Sort",
        "Bubble Sort Basic",
        "Bubble Sort Optimized",
        "Timsort (sorted)"
    ]

    results = {algo: [] for algo in algorithms}

    # Функція для додавання результатів у список
    def add_result(algorithm: str, time_taken: float) -> None:
        """Додає результат тестування до словника результатів.

        Args:
            algorithm (str): Назва алгоритму.
            time_taken (float): Час виконання алгоритму.
        """
        results[algorithm].append(float(format_time(time_taken)))

    # Тестування для різних розмірів масивів
    for label, size in zip(sizes, data_keys):
        data = reset_data()

        print(f"\nСортування масиву {label} [мс]:")

        # Використання параметрів для передачі значень data і size у лямбда
        add_result(
            "Merge Sort",
            timeit.timeit(lambda data=data, size=size: merge_sort(data[size]), number=10)
        )
        add_result(
            "Insertion Sort",
            timeit.timeit(lambda data=data, size=size: insertion_sort(data[size]), number=10)
        )
        add_result(
            "Bubble Sort Basic",
            timeit.timeit(lambda data=data, size=size: bubble_sort_basic(data[size]), number=10)
        )
        add_result(
            "Bubble Sort Optimized",
            timeit.timeit(lambda data=data, size=size: bubble_sort_optimized(data[size]), number=10)
        )
        add_result(
            "Timsort (sorted)",
            timeit.timeit(lambda data=data, size=size: sorted(data[size]), number=10)
        )

    # Виведення результатів у текстовому вигляді
    for algo in algorithms:
        print(f"\nРезультати для {algo}:")
        for size, time in zip(sizes, results[algo]):
            print(f"{size}: {time} мс")

    # Побудова графіку
    for algo in algorithms:
        plt.plot(sizes, results[algo], label=algo)

    plt.yscale('log')  # Змінюємо шкалу осі Y на логарифмічну
    plt.xlabel("Розмір масиву")
    plt.ylabel("Час виконання (мс, логарифмічна шкала)")
    plt.title("Порівняння ефективності алгоритмів сортування")
    plt.legend()
    plt.show()

# Генерація даних для тестів
tiny_data = random.sample(range(100), 10)
small_data = random.sample(range(1000), 100)
medium_data = random.sample(range(10000), 1000)
large_data = random.sample(range(100000), 10000)
almost_sorted_data = create_almost_sorted_data(large_data)[:]

# Запуск тестів
if __name__ == "__main__":
    run_tests()
