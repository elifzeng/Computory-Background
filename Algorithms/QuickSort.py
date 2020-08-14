lista = [1, 9, 2, 4, 6]

# 递归计算列表元素之和
def sum(arr):
    total = 0
    if arr == []:
        return 0
    else:
        firstn = arr[0]
        del arr[0]
        return firstn + sum(arr)


# print(sum(lista))

# 递归计算列表包含元素数
def count(arr):
    numb = 0
    if arr == []:
        return 0
    else:
        del arr[0]
        return 1 + count(arr)


# print(count(lista))

# 递归找出列表中最大的数字
def Max(arr):
    if len(arr) == 0:
        return float("-inf")
    else:
        largest = arr[0]
        # print(arr[1:])
        if largest < Max(arr[1:]):
            largest = Max(arr[1:])
        return largest


# print(Max(lista))

# 快速排序


def quicksort(array):
    if len(array) < 2:
        return array  # 基准条件：为空或者只包含一个元素的数组是“有序”的
    else:
        privo = array[0]  # 选择基准值
        less = [i for i in array[1:] if i <= privo]  # 由所有大于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > privo]  # 大于基准值元素的元素组成
        return quicksort(less) + [privo] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))

