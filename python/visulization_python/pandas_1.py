#!/usr/bin/env python
#%%
from pathlib import Path
import numpy as np
import pandas as pd

# %%
def ComputDistance(coordlista, coordlistb):
    vectora = np.array(coordlista)
    vectorb = np.array(coordlistb)
    EucDis = np.linalg.norm(vectora - vectorb)
    return EucDis


def Getcoor(pdbinfo):
    _ = pdbinfo[31:].strip().split()[0:3]
    x = float(pdbinfo[31:38].strip())
    y = float(pdbinfo[38:46].strip())
    z = float(pdbinfo[46:54].strip())
    xyz = [x, y, z]
    return xyz


def WashData(lista, listb):
    listc = [lista[i] for i in range(len(lista)) if i not in listb]
    return listc


def Cut_bins(label, frame, definedbins):
    a, b = pd.cut(x=frame[label], bins=definedbins, right=True, retbins=True)
    return a, b


#%%
# 6715 files
datafilepaths = list(Path("/tmp/lzeng/halogen").glob("*"))
calfilepaths = []
caldistance = []
calhalotypes = []
for datafile in datafilepaths:
    with datafile.open() as f:
        lines = f.readlines()
        try:
            if "LYS" not in lines[0]:
                continue
            elif "HETATM" not in lines[-1]:
                continue
        # some files do not include halogen information in pdb, eg. pdb1ppg.halo.pdb
        except IndexError:
            continue
        lysfcoor = []
        halogcoor = []
        halotypes = []
        for line in lines:
            if "LYS" in line:
                lysfcoor.append(Getcoor(line))
            elif "HETATM" in line:
                halogcoor.append(Getcoor(line))
        # calhalotypes.append(halotypes)
        calfilepaths.append(datafile)
        halo_lysDis_perfile = []
        for m in range(len(halogcoor)):
            h = halogcoor[m]
            halo_lysDis = []
            for lys in lysfcoor:
                EucDist = ComputDistance(h, lys)
                if EucDist <= 3 or EucDist > 10:
                    continue
                if 3 < EucDist <= 10:
                    halo_lysDis.append(EucDist)
            if not halo_lysDis:
                continue
            halo_lysDis_perfile.append(halo_lysDis)
            halotypes.append(line.strip().split()[-1])
        caldistance.append(halo_lysDis_perfile)
        calhalotypes.append(halotypes)


# %%
# 3053 files
nointeraction = []
for d in range(len(caldistance)):
    if not caldistance[d]:
        nointeraction.append(d)
rmnointerfilep = WashData(calfilepaths, nointeraction)
rmnointerhalotype = WashData(calhalotypes, nointeraction)
rmnointerdist = WashData(caldistance, nointeraction)
# %%
# for p in range(len(rmnointerfilep)):
#     pdbid = rmnointerfilep[p].name.split('.')[0]
#%%
# do not consider the source pdbfile
#
dis_BR = []
dis_CL = []
dis_I = []
for p in range(len(rmnointerhalotype)):
    atypes = rmnointerhalotype[p]
    dists = rmnointerdist[p]
    for i in range(len(atypes)):
        atype = atypes[i].strip()
        if "BR" in atype:
            dis_BR += dists[i]
        elif atype == "CL":
            dis_CL += dists[i]
        elif atype == "I":
            dis_I += dists[i]
        else:
            pass
# %%
# 其实不用排序，后续pd.value_counts()会自动排序
dis_BR.sort()  # 3540
dis_CL.sort()  # 12648
dis_I.sort()  # 1237

# %%
distframeI = pd.DataFrame(data={"I": dis_I,})
distframeBR = pd.DataFrame(data={"BR": dis_BR,})
distframeCL = pd.DataFrame(data={"CL": dis_CL,})
# %%
dis_All = dis_CL + dis_I + dis_BR
dis_All.sort()  # 17425
distframeAll = pd.DataFrame(data={"AllHalogens": dis_All,})
# %%
# 划分区间
dis_bins = [round(i, 1) for i in np.arange(3.0, 10.1, 0.1)]
AllHalocut, AllHalobins = Cut_bins("AllHalogens", distframeAll, dis_bins)
BRcut, BRbins = Cut_bins("BR", distframeBR, dis_bins)
CLcut, CLbins = Cut_bins("CL", distframeCL, dis_bins)
Icut, Ibins = Cut_bins("I", distframeI, dis_bins)
# %%
# 统计每个区间有多少个数据
AllHalocut_counts = AllHalocut.value_counts(ascending=True)
BRcut_counts = BRcut.value_counts(ascending=True)
CLcut_counts = CLcut.value_counts(ascending=True)
Icut_counts = Icut.value_counts(ascending=True)
#%%
AllHalocut_counts.to_csv("AllHalocut_counts.csv", index=True, index_label="interval")
BRcut_counts.to_csv("BRcut_counts.csv", index=True, index_label="interval")
CLcut_counts.to_csv("CLcut_counts.csv", index=True, index_label="interval")
Icut_counts.to_csv("Icut_counts.csv", index=True, index_label="interval")
# %%
