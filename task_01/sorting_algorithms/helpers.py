"""
Модуль для створення майже відсортованого масиву та форматування часу.

Цей модуль містить функції для створення майже відсортованого масиву шляхом перемішування
випадкових елементів у вже відсортованому масиві, а також для форматування часу в зручний для виведення формат.
"""

import random
from typing import List

def create_almost_sorted_data(original_data: List[int], num_elements: int = 100, num_shuffles: int = 5) -> List[int]:
    """
    Створює майже відсортований масив, перемішуючи випадкові елементи в вже відсортованому масиві.

    Параметри:
    ----------
    original_data : list[int]
        Початковий масив, з якого буде створено майже відсортований масив.
    num_elements : int, optional
        Кількість випадкових елементів для перемішування в кожній ітерації. За замовчуванням 100.
    num_shuffles : int, optional
        Кількість разів, які випадкові елементи будуть перемішані. За замовчуванням 5.

    Повертає:
    ---------
    list[int]
        Майже відсортований масив.
    """
    # Сортуємо початковий масив
    sorted_data = sorted(original_data)

    for _ in range(num_shuffles):
        # Вибираємо num_elements випадкових елементів
        indices_to_shuffle = random.sample(range(len(sorted_data)), num_elements)
        # Перемішуємо вибрані елементи
        sub_array = [sorted_data[i] for i in indices_to_shuffle]
        random.shuffle(sub_array)

        # Повертаємо перемішані елементи назад на свої місця
        for i, idx in enumerate(sorted(indices_to_shuffle)):
            sorted_data[idx] = sub_array[i]

    return sorted_data

def format_time(time_in_seconds: float) -> str:
    """
    Форматує час у секундах у мілісекунди з двома десятковими знаками.

    Параметри:
    ----------
    time_in_seconds : float
        Час у секундах, який потрібно перетворити.

    Повертає:
    ---------
    str
        Відформатований рядок з часом у мілісекундах із точністю до двох десяткових знаків.
    """
    time_in_ms = time_in_seconds * 1000  # Перетворення у мілісекунди
    return f"{time_in_ms:.2f}"  # Форматування до 2 знаків після коми
