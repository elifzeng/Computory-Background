#!/usr/bin/python3
# 选择排序 Selection sort, 将数组元素按从小到大的顺序排列。

# find the smallest item in array
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# sort the array using seleciton sort method
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        # print(smallest,arr.pop(smallest))
        newArr.append(arr.pop(smallest))  # list.pop()移除一个元素并返回该元素的值，参数为索引值
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))

