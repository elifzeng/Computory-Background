# HDF5 for Python
See more in `User_Guide.pdf` and a [Quick Start](https://docs.h5py.org/en/stable/quick.html#quick) 
[HDF5](https://portal.hdfgroup.org/display/HDF5/HDF5) （Hierarchical Data Format）is a data model, library, and file format for storing and managing data.  
An HDF5 file is a container for two kinds of objects: **datasets**, which are array-like collections of data, and **groups**, which are folder-like containers that hold datasets and other groups. The most fundamental thing to remember when using h5py is:  
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
