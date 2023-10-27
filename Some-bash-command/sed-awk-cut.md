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
sed -n '2p' aa.txt # 打印aa.txt的第二行
sed -n '23,34p' aa.txt >>bb.txt # 打印aa.txt的23～34行并输出到bb.txt中
```
# Cut
`cut`命令从文件的每一行剪切字节、字符和字段并将这些字节、字符和字段写至标准输出。  
（1）其语法格式为：  
```bash
cut  [-bn] [file] 或 cut [-c] [file]  或  cut [-df] [file]
# -d 后接分割字符，-f 后接数字，表示取出第几段
cut -d 'separate symbol' -f field
```
这里贴一个讲解比较详细的[链接](https://www.jianshu.com/p/1bbdbf1aa1bd)(awk, printf也有涉及)
# Awk
sdf文件中每个frame用"$$$$"分隔，读取文件，并截取第1个frame:
```bash
awk 'BEGIN { RS="\\$\\$\\$\\$" } NR==1 { print }' ACEH_MBZ_noproxim.sdf
# 同时把$$$$一并加到末尾
awk 'BEGIN { RS="\\$\\$\\$\\$" } NR==1 { print $0 "$$$$" }' ACEH_MBZ_noproxim.sdf
# 读取多段，且每个frame间没有多余空行，并输出到temp.sdf文件中
awk 'BEGIN { RS="\\$\\$\\$\\$" } NR==1 || NR==2 || NR==4 { printf("%s$$$$", $0) }' ACEH_MBZ_noproxim.sdf >../test/temp.sdf
# 读取前128个frame，没有多余空行，同时把$$$$一并加到末尾
awk 'BEGIN{RS="\\$\\$\\$\\$"} {if(NR<=128) {printf "%s%s", $0, (NR==128?"":"$$$$")}}' MBZ_N1PA_01_nequipwb.sdf > 128.sdf
```
传递一个列表
```bash
#!/bin/bash
lista=(260228 558920 731921 743844 748656 876950 1046778 1193718 1199211 1261589)

for i in "${lista[@]}"
do
    awk -v i="$i" 'BEGIN { RS="\\$\\$\\$\\$" } NR==i { printf("%s$$$$", $0) }' /pubhome/lzeng/data/pair25/ProximityEffect/MBZ_NMA_noproxim.sdf >> /pubhome/lzeng/data/pair25/test/temp.sdf
done
```
_Notice_: the first line of output is empty line, may be unreadable for chimera. Delete it and everything will be fine.
