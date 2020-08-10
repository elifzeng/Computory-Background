#!/usr/bin/python
def binary_search(list1, item):
    low = 0
    high = len(list1) - 1

    while low <= high:
        mid = int((low + high) / 2)
        # print("mid", mid)
        guess = list1[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


lista = [1, 3, 5, 7, 9]

print(binary_search(lista, 3))
print(binary_search(lista, -1))
