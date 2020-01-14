# Some-bash-command
record some bash command  

查看某文件中特定字符的匹配数：
```bash
cat file | grep string | wc -l
```
`wc -l `表示统计输出信息的行数，统计结果就是输出信息的行数，一行信息对应一个找到的字符，所以就是字符的个数。（**但该方法有漏洞，比如一行有多余一个同种字符**）另一种方法为用vim 打开文件后输入`:%s/string//ng`。

查看文件夹下文件数：
```bash
$ ls -l | grep "^-" | wc -l
```
该指令不包括子目录，若要查看子目录见[link](http://noahsnail.com/2017/02/07/2017-02-07-Linux%E7%BB%9F%E8%AE%A1%E6%96%87%E4%BB%B6%E5%A4%B9%E4%B8%8B%E7%9A%84%E6%96%87%E4%BB%B6%E6%95%B0%E7%9B%AE/)。
