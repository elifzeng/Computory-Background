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
# %%

# %%
