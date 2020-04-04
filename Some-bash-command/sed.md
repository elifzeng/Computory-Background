# Sed

`sed` 是一个管线命令，可以用于分析stout。此外，`sed`还可以将数据进行取代、删除、新增、撷取特定行等功能。鸟叔书上列举功能
不是很全，所以在这里贴一个讲解比较详细的[链接](https://man.linuxde.net/sed)。  



所有在模板test和check所确定的范围内的行都被打印：  
```bash
sed -n '/test/,/check/p' file
sed -n '/MODEL        17$/,/ENDMDL/p' PRPA_PRPA.origin.pdb > a # 17后加$表示以17结尾
```
