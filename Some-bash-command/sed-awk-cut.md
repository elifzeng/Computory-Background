# Sed

`sed` 是一个管线命令，可以用于分析stout。此外，`sed`还可以将数据进行取代、删除、新增、撷取特定行等功能。鸟叔书上列举功能
不是很全，所以在这里贴一个讲解比较详细的[链接](https://man.linuxde.net/sed)。  

### An example
```bash
#!/bin/bash

function ExtraHalo() {
    for file in $(ls $1)
    do
        filepath=$1/$file
        # liginfo=$(sed -n '/^FORMUL/p' $filepath | sed -n '/BR/p')
        if [ "$(sed -n '/^FORMUL/p' $filepath | sed -n '/BR/p')" != '' ]; then
            echo $filepath
            echo $(sed -n '/^FORMUL/p' $filepath | sed -n '/BR/p')
        elif [ "$(sed -n '/^FORMUL/p' $filepath | sed -n '/CL/p')" != '' ]; then
            echo $filepath
            echo $(sed -n '/^FORMUL/p' $filepath | sed -n '/CL/p')
        elif [ "$(sed -n '/^FORMUL/p' $filepath | sed -n '/I/p')" != '' ]; then
            echo $filepath
            echo $(sed -n '/^FORMUL/p' $filepath | sed -n '/I/p')
        fi
    done
}

function Unzip() {
    for file in $(ls $1)
    do
        filepath=$1/$file
        gunzip -c $filepath >/tmp/lzeng/pdb/$2/${file:0:11}
    done
}

# for i in {0..9}{0..9}; do
#     echo $i 
#     if [ -d /pubhome/pdb/PDB/$i ]; then
#         mkdir /tmp/lzeng/pdb/$i 
#         j="/pubhome/pdb/PDB/$i"
#         # ExtraHalo "$j"
#         # Unzip "$j" "$i"
#     fi
# done

for i in {a..z}{0..9}; do
    # echo $i 
    if [ -d /tmp/lzeng/pdb/$i ]; then
        j="/tmp/lzeng/pdb/$i"
        ExtraHalo "$j"
    fi
done
```

所有在模板test和check所确定的范围内的行都被打印：  
```bash
sed -n '/test/,/check/p' file
sed -n '/MODEL        17$/,/ENDMDL/p' PRPA_PRPA.origin.pdb > a # 17后加$表示以17结尾
```
# Cut
`cut`命令从文件的每一行剪切字节、字符和字段并将这些字节、字符和字段写至标准输出。  
（1）其语法格式为：  
```bash
cut  [-bn] [file] 或 cut [-c] [file]  或  cut [-df] [file]
```
这里贴一个讲解比较详细的[链接](https://www.jianshu.com/p/1bbdbf1aa1bd)(awk, printf也有涉及)
