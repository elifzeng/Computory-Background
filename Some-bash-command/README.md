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

令人昏厥的[vim命令总结](https://www.cnblogs.com/yangjig/p/6014198.html)

今天把CPU负荷跑爆了orz
```bash
$ w
```
Show who is logged on and what they are doing.  `w`:qq  displays  information  about  the  users currently on the machine, and their processes.  The header shows, in this order, the current time, how long the system has been running, how many users are currently logged on, and the system [load averages](https://en.wikipedia.org/wiki/Load_(computing)) for the past 1, 5, and 15 minutes.(如果这三个数从左到右依次递增，则说明CPU占用率在下降，反之亦然。)  
![image](https://user-images.githubusercontent.com/52747634/72409311-4dee9d80-37a0-11ea-9050-3e7f1f8d5988.png)  

```bash
$ free
```
Display amount of free and used memory in the system. `free` displays  the  total amount of free and used physical and swap memory in the system, as well as the buffers and caches used by the kernel. The information is gathered by parsing /proc/meminfo.  
![image](https://user-images.githubusercontent.com/52747634/72409599-349a2100-37a1-11ea-816e-698a0df0754d.png)  

```bash
$ ps -xfa
```
`ps` report a snapshot of the current processes. `ps` displays information about a selection of the active processes.  If you want a repetitive update of the selection and the displayed information, use `top` instead.  
`-a`     Select all processes except both session leaders (see getsid(2)) and processes not associated with a terminal.  
`-f`     Do full-format listing. This option can be combined with many other UNIX-style options to add additional
       columns.  It also causes the command arguments to be printed.  When used with -L, the NLWP (number of threads)
              and LWP (thread ID) columns will be added.  See the c option, the format keyword args, and the format keyword
              `comm`.  
`-x`  Register format.
