"""
Модуль для злиття двох відсортованих масивів у один.

Цей модуль містить функцію merge_lists, яка приймає два відсортовані масиви
цілих чисел і об'єднує їх в один відсортований масив, використовуючи 
алгоритм злиття з алгоритму сортування злиттям.
"""

from typing import List

def merge_lists(left: List[int], right: List[int]) -> List[int]:
    """
    Зливає два відсортовані підмасиви в один відсортований масив.

    Аргументи:
    - left (List[int]): Відсортований лівий підмасив.
    - right (List[int]): Відсортований правий підмасив.

    Повертає:
    - List[int]: Відсортований об'єднаний масив.
    """
    merged = []
    left_idx = right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        merged.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        merged.append(right[right_idx])
        right_idx += 1

    return merged
