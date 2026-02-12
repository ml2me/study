#  Пузырьковая сортировка (по неубыванию)
#  Для сортировки по невозрастанию - поменять знак на "<"

def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        srtd = False
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:  #  Для сортировки по невозрастанию - поменять знак на "<"
                lst[j], lst[j+1] = lst[j+1], lst[j]
                srtd = True
        if not srtd:  #  если элементы отсортированы
            break

# Пример
nums = [3, 4, 1, 2, 5]
bubble_sort(nums)

print(nums)
