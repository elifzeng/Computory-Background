# 数据重定向
See [Here](https://www.cnblogs.com/chengmo/archive/2010/10/20/1855805.html)  
linux shell 下常用输入输出操作符为：  
1. 标准输入   (stdin) ：代码为 0 ，使用 < 或 << ； /dev/stdin -> /proc/self/fd/0   0代表：/dev/stdin
2. 标准输出   (stdout)：代码为 1 ，使用 > 或 >> ； /dev/stdout -> /proc/self/fd/1  1代表：/dev/stdout
3. 标准错误输出(stderr)：代码为 2 ，使用 2> 或 2>> ； /dev/stderr -> /proc/self/fd/2 2代表：/dev/stderr

## 读取文件并进行后续操作
```bash
#!/bin/bash

# 定义一个空数组用于存储文件的每一行
lines=()

# 逐行读取文件，并将每一行作为数组的一个元素
while IFS= read -r line; do
    lines+=("$line")
done < "/pubhome/lzeng/nequip/run_model/filelist1.txt"  # 替换成你要读取的文件名

# 打印数组中的所有元素
for item in "${lines[@]}"; do
    echo "$item"
done
```
