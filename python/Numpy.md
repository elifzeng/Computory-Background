记录一些numpy技巧
## 花式索引
```python
row_index = [1,1,2,7]
col_index = [0,2,4,8]
M[row_index,col_index] # 选出(1,0)(1,2)(2,4)(7,8)位置的元素
M[row_index,:][:,col_index] # 选出4行4列
```
### example
```python
ref_xyz = 
array([[30.582 , 11.728 , 19.983 ],
       [31.027 , 12.6   , 20.127 ],
       [30.353 , 11.298 , 20.844 ],
       [29.653 , 11.9115, 19.4432],
       [31.542 , 10.831 , 19.257 ],
       [31.079 ,  9.781 , 18.465 ],
       [30.103 ,  9.627 , 18.364 ],
       [31.976 ,  8.934 , 17.802 ],
       [31.619 ,  8.183 , 17.238 ],
       [33.346 ,  9.137 , 17.93  ],
       [33.986 ,  8.537 , 17.458 ],
       [33.82  , 10.186 , 18.722 ],
       [34.813 , 10.34  , 18.823 ],
       [32.919 , 11.024 , 19.379 ],
       [33.264 , 11.773 , 19.944 ]])
cycleC_index = [4,5,7,9,11,13]
>>ref_xyz[cycleC_index]
array([[31.542, 10.831, 19.257],
       [31.079,  9.781, 18.465],
       [31.976,  8.934, 17.802],
       [33.346,  9.137, 17.93 ],
       [33.82 , 10.186, 18.722],
       [32.919, 11.024, 19.379]])
```
## 布尔索引
```pythob
row_index = (M[:,0] >= 20) & (M[:,0] <= 80)
col_index = M[0,:] >= 5
M[row_index,:][:,col_index]
```
注意：不能在同一个方括号中对列和行都使用布尔索引。新词我们必须先在行方向上进行布尔选择，然后重新打开方括号进行第二次选择，这一次集中在列方向上选择  
如果需要对数组元素进行全局选择，可以
```python
mask = (M >= 20) & (M <= 90) & ((M / 10) % 1 >= 0.5)
M[mask]
```
## axis
[ref](https://zhuanlan.zhihu.com/p/30960190)  
最直白地来说的话，就是“最外面的括号代表着 axis=0，依次往里的括号对应的 axis 的计数就依次加 1”

![image](https://user-images.githubusercontent.com/52747634/160524135-c7d4c439-62c1-4018-adba-d1ad74e7b1a3.png)
![image](https://user-images.githubusercontent.com/52747634/160524306-ce9e6e1b-7008-4d77-b38a-c02c74b2f8c7.png)
![image](https://user-images.githubusercontent.com/52747634/160524371-448a0d14-f2c9-43d8-8beb-220c4985fa02.png)

## Numpy.transpose()
[python中的Numpy.transpose()](https://zhuanlan.zhihu.com/p/154203624#:~:text=np.transpose,%281%2C0%2C2%29%E8%A1%A8%E7%A4%BA%E5%B0%860%E8%BD%B4%E5%92%8C1%E8%BD%B4%E7%BD%AE%E6%8D%A2%E3%80%82%20%E5%9C%A8%E5%9B%BE%E4%B8%AD%E5%8D%B3%E8%A1%A8%E7%A4%BA%E7%BA%A2%E8%89%B2%E8%BF%99%E4%B8%80%E5%88%97%E4%B8%8E%E7%BB%BF%E8%89%B2%E8%BF%99%E4%B8%80%E5%88%97%E4%BA%92%E6%8D%A2%EF%BC%8C%E5%85%B6%E4%BB%96%E4%BD%8D%E7%BD%AE%E4%B8%8D%E5%8F%98%EF%BC%8C%E5%9B%A0%E7%BD%AE%E6%8D%A2%E5%AF%BC%E8%87%B4%E7%B4%A2%E5%BC%95%E9%A1%BA%E5%BA%8F%E5%8F%98%E5%8C%96%EF%BC%8C%E5%8E%9F%E6%9D%A5%E7%9A%841%E8%BD%B4%E5%8F%98%E6%88%90%E6%96%B0%E7%9A%840%E8%BD%B4%EF%BC%8C%E5%8E%9F%E6%9D%A5%E7%9A%840%E8%BD%B4%E5%8F%98%E6%88%90%E6%96%B0%E7%9A%841%E8%BD%B4%EF%BC%8C%E9%87%8D%E6%96%B0%E6%8C%89%E6%96%B0%E7%9A%84%EF%BC%880-1-2%EF%BC%89%E8%BD%B4%E6%8E%92%E5%BA%8F%EF%BC%8C%E5%8D%B3%E5%8F%AF%E5%BE%97%E5%88%B0%E6%9C%80%E7%BB%88%E7%BB%93%E6%9E%9C%E3%80%82)  
```python
coord.transpose()
```
当transpose()不传任何参数时，作用与T属性类似，arr.T即可完成数组arr的转置.transpose()接受的是含所有轴编号的元组，例如三维数组的np.transpose(1,0,3)，即表示将0轴和1轴置换。其他可参见参考文章链接。  
## 搜索非零元素
场景：n * n个nodes的邻接矩阵,nodei, nodej相连则为True,不相连则为False。现在需要返回有link的nodes的坐标。
```python
>>> c = np.arange(16).reshape(4,4)
>>>c
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])
>>> c > 5
>>> d = c > 5
>>> d
array([[False, False, False, False],
       [False, False,  True,  True],
       [ True,  True,  True,  True],
       [ True,  True,  True,  True]])

>>> np.transpose(np.nonzero(d))
# 当为一维矩阵时，可以用np.nonzero(a)[0]
array([[1, 2],
       [1, 3],
       [2, 0],
       [2, 1],
       [2, 2],
       [2, 3],
       [3, 0],
       [3, 1],
       [3, 2],
       [3, 3]])
```
## `numpy.setdiff1d()` 从b中删除存在于a中的元素
[ref](https://www.delftstack.com/zh/howto/numpy/numpy-remove-element-from-array/)  
该函数接受三个参数，ar1、ar2 和 assume_unique。ar1 和 ar2 是两个 NumPy 数组。assume_unique 是一个可选的布尔参数。其默认值为 False。当其为 True 时，则假定两个输入数组是唯一的，并且此假设可以加快计算时间。  
setdiff1d() 返回 ar1 中不在 ar2 中的唯一值。  
```python
import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
indexes = [3, 5, 7]
modifiedArray = np.setdiff1d(myArray, indexes)
print(modifiedArray)
# output
[ 1  2  4  6  8  9 10]
```
## [numpy.sort()](https://numpy.org/doc/stable/reference/generated/numpy.sort.html) 排序
`numpy.sort(a, axis=- 1, kind=None, order=None)` return a sorted copy of an array.  
axis值为int，表示沿着哪个轴排序，当axis设定为`None`时，表示先把array进行flatten处理后（就是降成一维）再排序。
```python
>>> a = np.array([[1,4],[3,1]])
>>> np.sort(a)                # sort along the last axis
array([[1, 4],
       [1, 3]])
>>> np.sort(a, axis=None)     # sort the flattened array
array([1, 1, 3, 4])
>>> np.sort(a, axis=0)        # sort along the first axis
array([[1, 1],
       [3, 4]])
```
## [矩阵上三角或下三角](https://numpy.org/devdocs/reference/generated/numpy.tril.html)
场景：rmsd矩阵中，Rij和Rji相等，只取其中一个值可以减少后续计算量，若只取 `i > j`的值，则为rmsd矩阵对角线以上的上三角区域。  
`numpy.tril(m, k=0)` Lower triangle of an array.  
`numpy.triu(m, k=0)` Upper triangle of an array.  
> k: int, optional
> Diagonal above which to zero elements. k = 0 (the default) is the main diagonal, k < 0 is below it and k > 0 is above.

```python
>>> np.tril([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], k=-1)
array([[ 0,  0,  0],
       [ 4,  0,  0],
       [ 7,  8,  0],
       [10, 11, 12]])
>>> np.triu([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], k=1)
array([[0, 2, 3],
       [0, 0, 6],
       [0, 0, 0],
       [0, 0, 0]])
>>> np.triu([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], k=0)
array([[1, 2, 3],
       [0, 5, 6],
       [0, 0, 9],
       [0, 0, 0]])
```
## Merge two numpy arrays
`np.concatenate`
```python
import numpy as np

first = np.array([[650001.88, 300442.2,   18.73,  0.575,  
                   650002.094, 300441.668, 18.775],
                  [650001.96, 300443.4,   18.7,   0.65,   
                   650002.571, 300443.182, 18.745],
                  [650002.95, 300442.54,  18.82,  0.473,  
                   650003.056, 300442.085, 18.745]])

second = np.array([[1],
                   [2],
                   [3]])

np.concatenate((first, second), axis=1)
```
## 储存numpy
[Python数据存储与压缩](https://blog.csdn.net/songbinxu/article/details/84942095#:~:text=Python%E5%B8%B8%E7%94%A8%E6%95%B0%E6%8D%AE%E5%AD%98%E5%82%A8%E4%B8%8E%E5%8E%8B%E7%BC%A9%E6%96%B9%E5%BC%8F%201.%20numpy.save%20%2F%20numpy.savez%20%E5%88%A9%E7%94%A8%20np.save%20%28file%2C,obj%29%20%E5%B0%86%E5%8D%95%E4%B8%AATensor%E4%BF%9D%E5%AD%98%E4%B8%BA.npy%20%E6%96%87%E4%BB%B6%EF%BC%8C%E5%88%A9%E7%94%A8%20np.save%20%28file%2C%20%2A%2Aobj%29%20%E5%B0%86%E5%A4%9A%E4%B8%AATensor%E4%BB%A5%E5%AD%97%E5%85%B8%E7%9A%84%E5%BD%A2%E5%BC%8F%E5%AD%98%E5%82%A8%E4%B8%BA.npz%20%E6%96%87%E4%BB%B6%EF%BC%8C%E5%8F%AF%E5%AE%9E%E7%8E%B0%E5%A4%9ATensor%E5%AD%98%E5%82%A8%E3%80%82)  
`.npz`文件相当于一个字典。
```python
'''np.savez'''
data = {'X':X, 'Y':Y}
np.savez("test/data.npz", **data)

'''from .npz'''
data = np.load("test/data.npz")
X, Y = data['X'], data['Y']
print X.shape, type(X)
print Y.shape, type(Y)

# savez_compressed 用法相同（我使用的是savez_compressed），但
# savez_compressed  Save several arrays into a single file in compressed .npz format
# savez Save several arrays into an uncompressed .npz file format
test_array = np.random.rand(3, 2)
test_vector = np.random.rand(4)
np.savez_compressed('/tmp/123', a=test_array, b=test_vector)
loaded = np.load('/tmp/123.npz')
```
### Example
```python
import pickle
import numpy as np
# convert coordinates data to  numpy array 
# and saved in .npz format
with open('dataset_final.pkl','rb') as f:
    dataset = pickle.load(f)

training = dataset['training']

dicta = {}
for i, j in enumerate(training):
    # notice that the keys for savez can only be string
    dicta[str(i)] = j['coordinates']

np.savez_compressed('/tmp/123', **dicta)
# load data
loada = np.load('/tmp/123.npz')
>>> type(loada)
# <class 'numpy.lib.npyio.NpzFile'>
>>> list(loada.keys())
# ['0', '1', '2', '3', '4', '5', ...]
>>> loada['1']
# array([[ 5.2726e+00,  2.6682e+00,  3.3760e+00],
#        [ 4.7571e+00,  2.2762e+00,  4.1348e+00],
#        [ 5.3766e+00,  3.6514e+00,  3.5093e+00],
#        [ 6.2664e+00,  2.2204e+00,  3.3785e+00],
#        [ 4.4510e+00,  2.4668e+00,  2.1189e+00],
#        [ 4.7846e+00,  1.5355e+00,  1.3184e+00],
#        [ 3.4558e+00,  3.2181e+00,  1.9703e+00],
#        [ 2.9152e+00,  3.1209e+00,  1.1843e+00],
#        [-1.2409e+00, -7.5740e-01,  0.0000e+00],
#        [-1.2027e+00, -1.4677e+00, -6.9380e-01],
#        [-2.0086e+00, -1.4810e-01, -1.6550e-01],
#        [-1.4114e+00, -1.2451e+00,  9.5980e-01],
#        [ 0.0000e+00,  0.0000e+00,  0.0000e+00],
#        [-8.0000e-02,  1.0233e+00,  2.0000e-04],
#        [ 1.2409e+00, -4.9300e-01, -0.0000e+00],
#        [ 1.4775e+00, -1.7939e+00, -8.8300e-02],
#        [ 7.1150e-01, -2.4342e+00, -1.7810e-01],
#        [ 2.4154e+00, -2.1379e+00, -6.6600e-02],
#        [ 2.2726e+00,  3.3250e-01,  9.2400e-02],
#        [ 2.1195e+00,  1.3220e+00,  1.4190e-01],
#        [ 3.2051e+00, -2.7600e-02,  1.1170e-01]])
>>> type(loada['1'])
# <class 'numpy.ndarray'>
```
