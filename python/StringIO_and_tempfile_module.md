Yesterday, when I use `SDWriter()` in rdkit, I saw two official examples both of which write data to memory-like file instead of normal file:  
```python
# example 1
from rdkit import Chem
from io import StringIO

mol = Chem.MolFromSmiles("CO")
sio = StringIO()
w = Chem.SDWriter(sio)
w.write(mol)
w = None
print(sio.getvalue())

>>> 
# result
     RDKit          2D

  2  1  0  0  0  0  0  0  0  0999 V2000
    0.0000    0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.2990    0.7500    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0
M  END
$$$$
```
```python
# example 2 (from https://www.rdkit.org/docs/source/rdkit.Chem.PropertyMol.html?highlight=molecular%20property)
from rdkit import Chem
import tempfile, os

pm = PropertyMol(m)
fn = tempfile.NamedTemporaryFile(suffix='.sdf',delete=False).name
w.write(pm)
w=Nonne
with open(fn, 'r') as inf:
  txt = inf.read()
try:
  os.unlink(fn)
except Exception:
  pass
```

> stringio 在内存里，tempfile一般也在内存里，具体看/temp文件夹在内存还是硬盘里。好处是读写快，创建文件开销小。线程独立，任务失败无残余。
> 适合不需要保存结果，或者可能失败的任务，比如测试样例，中间临时文件，还有并行时的中间结果。

## StringIO
The **StringIO** module an in-memory file-like object.  
[More Explanation](https://www.geeksforgeeks.org/stringio-module-in-python/)
## tempfile
Sometimes we need to store data temporarily in a file for doing any task temporarily.It is better to store the data in a temporary file for generating the report to prevent any accidental modification of the original data. A temporary file can also be used for securing sensitive data. Creating a temporary file and doing these types of tasks can be done easily in Python by using **tempfile** module.  
[More Explanation](https://linuxhint.com/tempfile_python/)  
_Notice_ :the temporary files created by `tempfile` module is put into directory `/tmp/`.
