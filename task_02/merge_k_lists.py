"""
Модуль для об'єднання k відсортованих списків у один відсортований список.

Цей модуль містить функції для рекурсивного злиття кількох відсортованих списків
в один відсортований список.
"""

from typing import List
from merge_lists import merge_lists

def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Рекурсивно об'єднує k відсортованих списків в один відсортований список.

    Параметри:
    lists (List[List[int]]): Список відсортованих списків.

    Повертає:
    List[int]: Один відсортований список, що містить всі елементи.
    """
    if not lists:
        return []
    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2
    left = merge_k_lists(lists[:mid])
    right = merge_k_lists(lists[mid:])

    return merge_lists(left, right)

if __name__ == "__main__":
    sorted_lists = [[3, 4, 5], [2, 3, 4], [1, 6]]
    merged_list = merge_k_lists(sorted_lists)
    print("Відсортований список:", merged_list)
