#!/usr/python/env python
"""
Make pairs overlap by coordinates transformation. 
Cluster analysis based on rmsd. 
Finally, select the representative conformation of the clusters.
"""
#%%
# from numpy.core.fromnumeric import reshape
# from numpy.linalg.linalg import norm
from operator import index, le
from types import ClassMethodDescriptorType
from numpy.random import sample
from rdkit import Chem
import numpy as np
from sklearn import metrics
# import sklearn
# import argparse
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import calinski_harabasz_score
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
# from sklearn.utils.extmath import cartesian
# import matplotlib as mpl
import random
# %%
# ETSH_MIME as example
def Getxyz(mol):
    # frag_num = mol.GetProp("FRAG_ATOM_NUM")
    # fraga_num = int(frag_num.strip().split()[1])
    conf = mol.GetConformer()
    mol_pos = [conf.GetAtomPosition(i) for i in range(mol.GetNumAtoms())]
    mol_xyz = np.asarray(
        [[mol_pos[i].x, mol_pos[i].y, mol_pos[i].z] for i in range(mol.GetNumAtoms())]
    )
    # fraga_xyz = mol_xyz[:fraga_num]
    # fragb_xyz = mol_xyz[fraga_num:]
    # return mol_xyz, fraga_xyz, fragb_xyz, fraga_num
    return mol_xyz


#%%
allmol_xyz = list()

with Chem.SDMolSupplier('/home/elifzeng/Documents/tmp/rot_ETAM_ETSH.sdf', removeHs=False) as suppl:
    for mol in suppl:
        mol_xyz = Getxyz(mol)
        allmol_xyz.append(mol_xyz)
    
    allmol_xyz = np.asarray(allmol_xyz)
#%%
# 评估聚类效果，选择聚类数
CHscore = list()
SHscore = list()
inertia = list()
sample, atom, xyz = allmol_xyz.shape
reshape_xyz = allmol_xyz.reshape(sample, atom * xyz)
for i in range(2, 15):
    kmeans = KMeans(n_clusters=i, n_jobs=-1)
    kmeans.fit(reshape_xyz)
    inertia.append(kmeans.inertia_)
    CHscore.append(calinski_harabasz_score(reshape_xyz, kmeans.labels_))
    SHscore.append(silhouette_score(reshape_xyz, kmeans.labels_, metric='euclidean'))

#%%
# 可视化评估分数
plt.plot(range(2, 15), inertia, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('inertia')
plt.show()
# %%
kmeans = KMeans(n_clusters=4, n_jobs=-1)
# sample, atom, xyz = allmol_xyz.shape
# reshape_xyz = allmol_xyz.reshape(sample, atom * xyz)
kmeans.fit(reshape_xyz)
labels = kmeans.labels_
centers = kmeans.cluster_centers_
inertia = kmeans.inertia_
#%%
# 方法二，尝试用PCA降维
pca = PCA(n_components=3)
# 每一个pair有atomnum * 3 维，现在将其降到2维，也就是用一个点表征一个pair
newchara = pca.fit_transform(reshape_xyz)
# 查看转换后每个特征的方差百分比，即现在的每个特征值能描述整个数据集的程度
# explained variance ratio 之和应该介于60% 和100% 之间
# 一般在80%左右是最好的，因此在这里选择n_components = 3
print(pca.explained_variance_ratio_)
# %%
fig_pca = plt.figure(figsize=(12,10))
ax_pca = fig_pca.add_subplot(111, projection='3d')
ax_pca.set_xlabel('first principal component', fontsize=15)
ax_pca.set_ylabel('second principal component', fontsize=15)
ax_pca.set_zlabel('third principal component', fontsize=15)
fig_pca.suptitle('PCA for ETAM-ETSH Interaction Conformation', fontsize=20)
# %%
# label_newchar = dict()
# for i in range(len(labels)):
#     label = labels[i]
#     if label not in label_newchar:
#         label_newchar[label] = [newchara[i]]
#     elif label in label_newchar:
#         label_newchar[label].append(newchara[i])
# %%
# colors = plt.cm.Spectral(np.random.randint(0, len(labels), size=20))
N = len(labels)
# define the colormap
cmap = plt.cm.jet
# extract all colors from the .jet map
cmaplist = [cmap(i) for i in range(cmap.N)]
# create the new map
cmap = cmap.from_list('Custom cmap', cmaplist, cmap.N)

# define the bins and normalise
bounds = np.linspace(0, N, N+1)
# norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

# make the scatter
scat = ax_pca.scatter(newchara[:,0], newchara[:,1], newchara[:,2], c=labels, s=5, cmap=cmap, alpha=0.4)
# create the colorbar
cb = fig_pca.colorbar(scat, spacing='proportional', ticks=bounds)
cb.set_label('Custom cbar')
# fig_pca.legend()
# fig_pca
#%%
# for c in label_newchar:
#     data = np.asarray(label_newchar[c])
#     labelname =  f'cluster{c}'
#     ax_pca.scatter(data[:,0], data[:,1], data[:,2], alpha=0.4,edgecolor='none',s=5, label=labelname,c=colors[c])
# %%
# make the scatter for center points
center_newchar = pca.transform(centers)
ax_pca.scatter(center_newchar[:,0], center_newchar[:,1], center_newchar[:,2], s=30, c='black', marker='+')
#%%
# 找到离cluster center 最近的样本
# squared distance to cluster center
X_dist = kmeans.transform(reshape_xyz) ** 2
sample_dist = [np.min(i) for i in X_dist]
closet_sample = dict()# {label:[dist, index]}
label_sampindex = dict() # label:index
for k in range(len(centers)):
    closet_sample[k] = [float('inf'), float('inf')] 
    label_sampindex[k] = list()
for i in range(len(labels)):
    label = labels[i]
    label_sampindex[label].append(i)
    if sample_dist[i] < closet_sample[label][0]:
        closet_sample[label] = [sample_dist[i], i]
#%%
# 将距离cluster center 最近的样本坐标输出为sdf文件
# 同时，从每个cluster中随机选出1/10样本输出为sdf文件
clust_10pct = dict()
for i in range(len(centers)):
    sample_num = int(len(label_sampindex[i]) / 10) + 1
    clust_10pct[i] = random.sample(label_sampindex[i], sample_num)

closet_sample_index = [closet_sample[i][1] for i in closet_sample]
clust_10pct_index = list()
for j in clust_10pct:
    clust_10pct_index += clust_10pct[j]

oup_center = Chem.SDWriter('./center.sdf')
oup_10pct = Chem.SDWriter('./random_10pct.sdf')
suppl_index = 0
with Chem.SDMolSupplier('/home/elifzeng/Documents/tmp/rot_ETAM_ETSH.sdf', removeHs=False) as suppl:
    for mol in suppl:
        if suppl_index in closet_sample_index:
            oup_center.write(mol)
        if suppl_index in clust_10pct_index:
            oup_10pct.write(mol)
        suppl_index += 1 

oup_center.close()
oup_center.close()
# %%
# plt.subplot(221) # 表示将整个图像窗口分为2行2列，当前位置为1

# # %%
# # 将聚类结果可视化
# # 方法一，3D图
# # Visualizing4-D mix data using scatter plots
# fig = plt.figure(figsize=(40,10))
# title = fig.suptitle('atom-label', fontsize=14) # 添加居中标题
# #返回Axes实例, projection参数指定子图投影方式
# #可通过matplotlib.projections.get_projection_names()查看所有可用投影方式
# ax = fig.add_subplot(121,projection='3d') 
# ax2 = fig.add_subplot(122,projection='3d')
# ax2.set_xlim(-8, 8)
# ax2.set_ylim(-8, 8)
# ax2.set_zlim(-8, 8)
# # %%
# # 以每个片段的几何中心点画图
# xs = list()
# ys = list()
# zs = list()
# fraga_num = int(mol.GetProp('FRAG_ATOM_NUM').split()[1])
# # fragb_num = mol.GetNumAtoms() - fraga_num
# for i in allmol_xyz:
#     center_pointa = np.mean(i[:fraga_num], axis=0)
#     center_pointb = np.mean(i[fraga_num:], axis=0)
#     ax2.scatter(i[:fraga_num][:,0], i[:fraga_num][:,1], i[:fraga_num][:,2],alpha=0.4, edgecolor='none')
#     # ax.plot(center_pointa, center_pointb, color='grey')
#     xs += [center_pointa[0], center_pointb[0]]
#     ys += [center_pointa[1], center_pointb[1]]
#     zs += [center_pointa[2], center_pointb[2]]
# data_points = [[x, y, z] for x, y, z in zip(xs, ys, zs)]
# #%%
# # colors  = [??]
# # for data, color in zip(data_points, colors):
# #     x, y, z = data
# #     ax.scatter(x, y, z, alpha = 0.4, c=color, edgecolors='none', s=20)
# # 以fraga和fragb的几何中心为点画图，这样容易找到ref
# # 每一个cluster渲染一次
# devide_cluster = dict() # {'label' : [[x,y,z],...],...}
# for i in range(len(labels)):
#     if labels[i] not in devide_cluster:
#         devide_cluster[labels[i]] = [data_points[2*i]]
#         devide_cluster[labels[i]].append(data_points[2*i+1])
#     elif labels[i] in devide_cluster:
#         devide_cluster[labels[i]].append(data_points[2*i])
#         devide_cluster[labels[i]].append(data_points[2*i+1])
# #%%
# for lab in devide_cluster:
#     data = np.asarray(devide_cluster[lab])
#     labelname = f'cluster{lab}'
#     ax.scatter(data[:,0], data[:,1], data[:,2], alpha=0.4, edgecolor='none', label=labelname)

# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
# fig.legend()
# # fig.savefig('ddd')
