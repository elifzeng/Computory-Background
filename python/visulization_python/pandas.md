## [How to Add a Column to a Pandas DataFrame](https://www.statology.org/add-column-pandas-dataframe/#:~:text=You%20can%20use%20the%20assign%20%28%29%20function%20to,to%20a%20specific%20location%20in%20a%20pandas%20DataFrame%3A)
## [read csv](https://zhuanlan.zhihu.com/p/340441922)
```python
cluster_summary = pd.read_csv('CltResults/temp/cluster_summary.csv',index_col=0)
print(cluster_summary.to_string)
```
## [csv operation](https://www.runoob.com/pandas/pandas-csv-file.html)
[简单的读写索引](https://blog.csdn.net/Parzival_/article/details/114240650)

## [DataFrame operation]
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
