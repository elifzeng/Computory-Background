在遍历list的时候，删除符合条件的数据，结果不符合预期
```python
num_list = [1, 2, 2, 2, 3]
print(num_list)
for item in num_list:
    if item == 2:
        num_list.remove(item)
    else:
        print(item)

print(num_list)
# [1, 2, 2, 2, 3]
# 1
# [1, 2, 3]
```
或者
```python
for i, vali_data in enumerate(validation_set):
    if i in rand_sel_index:
        append_data_list.append(vali_data)
        del validation_set[i]
```
这种遍历删除是错误的，因为List删除一个元素的同时索引已经变了。
正确做法：
[ref](https://www.cnblogs.com/34fj/p/6351458.html#:~:text=Python%E9%81%8D%E5%8E%86%E5%88%97%E8%A1%A8%E5%88%A0%E9%99%A4%E5%A4%9A%E4%B8%AA%E5%88%97%E8%A1%A8%E5%85%83%E7%B4%A0%201%20%E6%8A%8A%E5%88%97%E8%A1%A8%E6%8B%B7%E8%B4%9D%EF%BC%8C%E7%84%B6%E5%90%8E%E5%AF%B9%E5%8E%9F%E5%88%97%E8%A1%A8%E8%BF%9B%E8%A1%8C%E5%88%A0%E9%99%A4%E6%93%8D%E4%BD%9C%E5%B0%B1%E6%B2%A1%E9%97%AE%E9%A2%98%E4%BA%86,2%20%E4%BB%8E%E5%90%8E%E5%BE%80%E5%89%8D%E9%81%8D%E5%8E%86%E5%88%97%E8%A1%A8%EF%BC%8C%E5%88%A0%E9%99%A4%203%20filter%E5%87%BD%E6%95%B0)
```python
# 从后往前倒序遍历删除
# reversed()
validation_num = len(validation_set)
for i in reversed(range(-validation_num,0)):
    if validation_num + i in rand_sel_index:
        append_data_list.append(validation_set[i])
        del validation_set[validation_num + i]
```
