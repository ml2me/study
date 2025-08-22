# binary search (Бинарный поиск) метод деления отрезка пополам
# Данный метод применим только к отсортированным (в данном случае по возрастанию) спискам
# elem – искомое значение, sorted_array – отсортированный по возрастанию массив значений
def binary_search(elem, sorted_array):
    if len(sorted_array) == 0:
        return -1
    elif elem < sorted_array[0]:
        return -1
    elif elem > sorted_array[-1]:
        return -1
    else:
        start = 0
        end = len(sorted_array) - 1
        while start <= end:
            search_index = start + (end - start) // 2 # используем, чтобы избежать переполнения для больших значений
            if sorted_array[search_index] == elem:
                return search_index
            elif sorted_array[search_index] < elem:
                start = search_index + 1
            else:
                end = search_index - 1
        return -1

#  Пример вызова:
print(binary_search(3,[]))  #  -1