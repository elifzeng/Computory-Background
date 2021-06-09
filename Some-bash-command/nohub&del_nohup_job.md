## 终端关闭时继续运行与后台运行
```bash
nohup python test.py [ARG] &>log6.txt &
```
`nohup` - run a command immune to hangups, with output to a non-tty  
`&>file`意思是把**标准输出**和**标准错误输出**都重定向到文件`log6.txt`中。最末`&`表示在后台运行

## 忘了pid怎么办
每次运行完nohup后会返回一个pid，用`kill  -9 pid`就可以杀死该命令。  
如果忘了pid比较麻烦，因为top只会显示当前运行的命令，如果nohub运行的是一个脚本，htop只会显示脚本中的命令，而无法显示`nohup x.sh`命令本身。  
解决办法是运行
```bash
ps aux | less
```
找到那个`nohup x.sh`命令的pid，再杀掉。
