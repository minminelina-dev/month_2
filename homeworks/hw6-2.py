# Часть 2 — Алгоритм (LeetCode) — Two Sum
# Решение с помощью двух вложенных циклов (без оптимизаций),
# как требуется в задании.


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Находит индексы двух чисел из nums, сумма которых равна target.
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # если решения нет


if __name__ == "__main__":
    # Пример из задания
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"nums = {nums}, target = {target}")
    print(f"Результат: {result}")  # Ожидаем [0, 1], т.к. 2 + 7 = 9

    # Дополнительные проверки
    print(two_sum([3, 2, 4], 6))      # [1, 2]  -> 2 + 4 = 6
    print(two_sum([3, 3], 6))         # [0, 1]  -> 3 + 3 = 6