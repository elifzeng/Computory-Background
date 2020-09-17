'''grep electronic information from sdf files
'''
# https://docs.python.org/zh-cn/3/library/pathlib.html
# the official manual of pathlib
from pathlib import Path

fpath = Path('the_dir_path_of_files')
for file in sorted(fpath.glob('*.sdf')): #遍历该文件夹下所有sdf文件
    with file.open() as f:
        for line in f.readlines():
            if line.startswith('M  CHG'):
                line = line.strip()
                line = line.split()
                atom_num = int(line[2])
                counter = 4
                charge = []
                for i in range(atom_num):
                    charge.append(int(line[counter]))
                    counter +=2
                
                assert len(charge) == atom_num, 'something wrong'
                total_charge = sum(charge)

# 怎么把每个文件的结果储存到一起什么的你自己搞吧