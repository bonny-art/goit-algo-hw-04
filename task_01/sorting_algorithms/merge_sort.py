"""
Модуль для реалізації алгоритму сортування злиттям (Merge Sort).
Алгоритм працює за допомогою рекурсії, розділяючи вхідний масив на підмасиви
і зливаючи їх в один відсортований масив.
"""

from typing import List

def merge(left: List[int], right: List[int]) -> List[int]:
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


def merge_sort(arr: List[int]) -> List[int]:
    """
    Сортує масив за допомогою алгоритму сортування злиттям.

    Аргументи:
    - arr (List[int]): Масив для сортування.

    Повертає:
    - List[int]: Відсортований масив.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))
