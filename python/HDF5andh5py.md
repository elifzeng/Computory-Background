# HDF5 for Python
See more in `User_Guide.pdf` and a [Quick Start](https://docs.h5py.org/en/stable/quick.html#quick).  
[HDF5](https://portal.hdfgroup.org/display/HDF5/HDF5) （Hierarchical Data Format）is a data model, library, and file format for storing and managing data.  
An HDF5 file is a container for two kinds of objects: **datasets**, which are array-like collections of data, and [**groups**](https://docs.h5py.org/en/stable/high/group.html#group), which are folder-like containers that hold datasets and other groups. The most fundamental thing to remember when using h5py is:  
**Groups work like dictionaries, and datasets work like NumPy arrays**  
## File Object
|r|Readonly, file must exist|
|:---:|:---:|
|r+|Read/write, file must exist|
|w|Create file, truncate if exists|
|w- or x |Create file, fail if exists|
|a |Read/write if exists, create otherwise (default)|

## Datatype
The HDF5 datatype object describes the layout of a single data element.The `datatype class` tells what the element means, and
the `datatype` describes how it is stored.Data types are categorized into 11 classes of datatype.  
![image](https://user-images.githubusercontent.com/52747634/71513812-e814a180-28d6-11ea-8fb3-450afc6a5295.png)

## Attributes
_See more in chapter 8 in User\_Guide_  
One of the best features of HDF5 is that you can **store metadata right next to the data it describes**. All groups and datasets support attached named bits of data called `attributes`.  
An attribute has two parts: name and value(s).
`dataset.attr['dtype'] = 'integer'` to create a attribute (the same for group), and `dataset.attr.get('dtype')` to retrieve name.  

## [String in h5py](http://docs.h5py.org/en/stable/strings.html)
**All strings in HDF5 hold encoded text.**
`h5py` exposes Fixed-length ASCII (NumPy `S` type) , **Variable-length UTF-8 (Python 2 `unicode`, Python 3 `str`)** and Variable-length ASCII (Python 2 `str`, Python 3 `bytes`)  
To understand `Fixed-length` and some other terms of string, see [this](https://tech.youzan.com/strings/). And then learn how h5py [represent special type](http://docs.h5py.org/en/2.9.0/strings.html?highlight=string).  
```ipython
In [7]: dt = h5py.special_dtype(vlen=str)  

In [8]: ds1_2 = f.create_dataset('ds1_2',(20,), dtype=dt)  
Out[8]: <HDF5 dataset "ds1_2": shape (20,), type "|O">  

In [10]: ds1_2  
Out[10]: <HDF5 dataset "ds1_2": shape (20,), type "|O">  

In [17]: ds1_2[:]  
Out[17]: 
array(['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
       '', '', ''], dtype=object)  
```
## Dtype
```python
# example
dict(d2.items())
# {'coordinates': <HDF5 dataset "coordinates": shape (5400, 5, 3), type "<f4">,
#  'coordinatesHE': <HDF5 dataset "coordinatesHE": shape (0, 5, 3), type "<f4">,
#  'energies': <HDF5 dataset "energies": shape (5400,), type "<f8">,
#  'energiesHE': <HDF5 dataset "energiesHE": shape (0,), type "<f8">,
#  'smiles': <HDF5 dataset "smiles": shape (17,), type "|S1">,
#  'species': <HDF5 dataset "species": shape (5,), type "|S1">}
```
![image](https://user-images.githubusercontent.com/52747634/169926698-252f7c95-cfbb-462f-b449-2957c1647c45.png)    
[float32和float63的区别](https://www.cnblogs.com/HappyTeemo/p/15405577.html)  简单来说就是float32能表示小数点后6位，float64能表示小数点后15位。


## give data to dataset
```python
arr = numpy.arange(100).reshape((10,10))
dset = f.create_dataset("MyDataset", data=arr)
```
## Examples
```python
# read h5 file
import h5py
import numpy as np
f = h5py.File('/pubhome/lzeng/torchani/dataset/ani1-up_to_gdb4/ani_gdb_s01.h5','r')
# %%
list(f.keys())
d1 = f['gdb11_s01']
d2 = d1['gdb11_s01-0']
dict(d2.items())
# {'coordinates': <HDF5 dataset "coordinates": shape (5400, 5, 3), type "<f4">,
#  'coordinatesHE': <HDF5 dataset "coordinatesHE": shape (0, 5, 3), type "<f4">,
#  'energies': <HDF5 dataset "energies": shape (5400,), type "<f8">,
#  'energiesHE': <HDF5 dataset "energiesHE": shape (0,), type "<f8">,
#  'smiles': <HDF5 dataset "smiles": shape (17,), type "|S1">,
#  'species': <HDF5 dataset "species": shape (5,), type "|S1">}

d2['coordinates'][()] # check contents in d2['coordinates']
coords = np.array(d2['coordinates'])
energies = np.array(d2['energies'])
smiles = np.array(d2['smiles'])
species = np.array(d2['species'])

# write h5 file
with h5py.File("test.h5", 'w') as h5f:
    #  get data
    for i, name in enumerate(inteng.keys()):
        j = i * 3 # index in universal_data
        m = universal_data[j]
        species = [SPECIES_NUM[int(a)] for a in m["atomic_nums"]]
        # convert distance unit from bohr used in orca to Å used in torchani
        coords = np.around(np.asarray(m["coord"]) * 0.5291772083, decimals=4)
        energy = inteng[name]
        grp = h5f.create_group(name) # create group
        grp.create_dataset("species", data=species, dtype='|S1') # create dataset, you can also specify dtype
        grp.create_dataset("coordinates", data=coords)
        grp.create_dataset("energy", data=energy)

```


