## [How to Create DataFrame](https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/)
## [How to Add a Column to a Pandas DataFrame](https://www.statology.org/add-column-pandas-dataframe/#:~:text=You%20can%20use%20the%20assign%20%28%29%20function%20to,to%20a%20specific%20location%20in%20a%20pandas%20DataFrame%3A)
## [read csv](https://zhuanlan.zhihu.com/p/340441922)
```python
cluster_summary = pd.read_csv('CltResults/temp/cluster_summary.csv',index_col=0)
print(cluster_summary.to_string)
```
## [csv operation](https://www.runoob.com/pandas/pandas-csv-file.html)
[简单的读写索引](https://blog.csdn.net/Parzival_/article/details/114240650)

## DataFrame operation
当用`pd.read_csv()`读入文件数据后，数据类型变为`DataFrame`。

## Example
### Write .csv
```python
# in python2
def report_save(infpath, cl, random_labels):
	'''report clustering results and save outputs'''
	import json

	cluster_labels = ["cluster " + str(x) for x in range(len(cl.clusters))]
	# cluster_n = 0
	sizes = []
	representatives = []
	members_cl = [] # type: list of list
	spreads = []
	for c in cl.clusters:
		sizes.append(c.size)
		representatives.append(int(cl.representative(c)))
		members_cl.append(c.members())
		spreads.append(c.spread)
	
	sizes.append(len(random_labels))
	representatives.append('None')
	members_cl.append('None')
	spreads.append('None')

	outDf = pd.DataFrame(
		{ "representative":representatives, "spread":spreads, "size":sizes, "members":members_cl}, 
		index=cluster_labels + ["global"],
	)
	oupath = str(infpath.parent / 'cluster_summary.csv')
	jsonpath = str(infpath.parent / 'label_index.json')

	
	outDf.to_csv(oupath)
  print 'cluster summary saved in ' + oupath
```
```python
#!/usr/bin/env python
#%%
import pandas as pd
import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap

# %%
allhalogen = pd.read_csv("AllHalocut_counts.csv")
BRs = pd.read_csv("BRcut_counts.csv")
CLs = pd.read_csv("CLcut_counts.csv")
Is = pd.read_csv("Icut_counts.csv")
# %%
# merge four dataframes
dataframes = [BRs, CLs, Is]
allatoms = allhalogen
for frame in dataframes:
    allatoms = pd.merge(allatoms, frame)
# %%
# 绘图，改变横坐标刻度间距，使得横坐标不重叠
graph = allatoms.plot.bar(x="interval", figsize=(17,9),width=1)
graph.set_xlabel('Distance(Å)',Fontsize=18)
graph.set_ylabel('Number',Fontsize=18)
graph.set_title('Distance between halogen atom and lysine side chain nitrogen atom',Fontsize=18)
# cmap = ListedColormap([])
# plt.savefig('ddd.jpg')
plt.legend(fontsize=15)# 设置左上图例说明大小
plt.xticks(rotation=80)
plt.savefig('Halogen_LysN_Dist.jpg')
plt.show()
```
## Sort by one column
```python
# coding=utf-8
import pandas as pd
 
 
# read_csv读取csv格式的数据，返回DataFrame
df = pd.read_csv("./dogNames.csv")
print(type(df))   # <class 'pandas.core.frame.DataFrame'>
# print(df.head(10))  # head(10) 显示前10条数据，默认前5条
 
 
# dataFrame中排序的方法
df = df.sort_values(by="Count_AnimalName",ascending=False)  # by指定按哪列排序。ascending表示是否升序
print(df.head())
'''
      Row_Labels  Count_AnimalName
1149       BELLA              1195
9133         MAX              1153
2653     CHARLIE               856
3244        COCO               852
12361      ROCKY               823
'''
 ```
