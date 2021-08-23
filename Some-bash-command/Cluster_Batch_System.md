# 集群批处理系统
## [Glossary](https://info.hpc.sussex.ac.uk/hpc-guide/glossary.html#term-tasks)
Meaning of `queues` `slots` `job script` `job id` `array job` `tasks` `modules`.
其他可见`Hand Book`

## Example1
This is a job script named *test1.sh*.
```bash
#$ -q honda
#$ -o /home/lzeng02/qusb-test/log/
#$ -e /home/lzeng02/qusb-test/log/

for i in $(seq 1 5); do
     echo -ne "\r########## $i"
     sleep 1
done

echo -e  "\n\nCompleted."
```
echo `-n` 表示不打印出换行符，`-e`表示启用转义。
run `qsub test1.sh` and `qstat` (or `watch qstat`)on terminal:  
![image](https://user-images.githubusercontent.com/52747634/71582419-23b4a300-2b45-11ea-84c9-030032c65a94.png)  

and check the output or error by `cat log/*o613355` and `cat log/*e613355`.The two files are created by commands in test1.sh.  
if there is something wrong, the state `Eqw` can be seen:  

![image](https://user-images.githubusercontent.com/52747634/71582541-a89fbc80-2b45-11ea-91f2-899d36ca120c.png)  
and you can track its state and error by jobID `qstat -j jobID`. Track all users' job array by `qstat -u \*`. And Delete this job by `qdel jobID`

## Example2
This is a job script named *qsub-test*. You can see more commmands pf `qsub` by `man qsub`.
```bash
#! /bin/bash
#$ -q honda   #-q <queue_name> 指定任务队列
##$ -pe honda 10 #-pe <parallel_environment_name> <num_core> 设定并行环境 parallel_environment是啥见handbook最下 Submit CPU job
#$ -l hostname=n125.hn.org  # 若要指定不使用哪台主机，则为-l hostname=！n125.hn.org 
#$ -t 100-125 # <FIRST>-<LAST>:<STEPSIZE> 用于提交 只该改变参数的重复任务
#$ -o /home/lzeng02/qsub-test/log/ # output 
#$ -wd /home/lzeng02/ # work directory

##$ -e /home/lzeng02/qsub-test/log/ # 标准错误输出路径
#$ -j y # -j y[es]|n[o] Specifies whether or not the standard error stream of the job is merged into the standard output stream.

printf "%10s: %10s\n" "JOB_ID" "$JOB_ID" # 这些变量的名字都是由qsub定义好的，具体参见man qsub
printf "%10s: %10s\n" "JOB_NAME" "$JOB_NAME"
printf "%10s: %10s\n" "TASK_ID" "$SGE_TASK_ID"
printf "%10s: %10s\n" "NHOSTS" "$NHOSTS"
printf "%10s: %10s\n" "NQUEUES" "$NQUEUES"
printf "%10s: %10s\n" "NSLOTS" "$NSLOTS"
printf "%10s: %10s\n" "QUEUE" "$QUEUE"
printf "%10s: %10s\n" "HOSTNAME" "$HOSTNAME"
# printf "%10s: %10s" "" "$"
# printf "%10s: %10s" "" "$"

for i in $(seq 1 5); do
     echo -ne "\r########## $i"
     sleep 1
done

echo -e  "\n\nCompleted."
```
# A Instance Example

```bash
#! /bin/bash
#$ -q honda
#$ -pe honda 20   
#$ -l hostname=n110.hn.org  
#$ -o /home/lzeng02/qsub-test/log/ 
#$ -e /home/lzeng02/qsub-test/log/


for i in $(ls /home/lzeng02/data/extra_1/superimp_pair/ACEM*) 
do
python make_matrix.py $i > matrix
touch log
nmrclust < nmrclust.inp > log
j=$(printf $i | cut -d '/' -f 7| cut -d '.' -f 1)
k="${j}_log"
mv log $k
mv $k /home/lzeng02/data/extra_1/nmrclust_log/
done
```
# A Parallel Example
```bash
#!/bin/bash
#$ -q benz
#$ -pe benz 32  
#$ -o /pubhome/lzeng/gnu_parallel/log
#$ -e /pubhome/lzeng/gnu_parallel/log
source ~/.bashrc # 以后每个脚本都记得要先source & conda activate personal_env
conda activate py37

filelist=() # create a vacuum list
function TravelDir(){
    for file in `ls $1`
    do
        if [ -d "$1/$file" ]
        then
            TravelDir "$1/$file"
        else
            filelist[${#filelist[@]}]="$1/$file" #相当于append
        fi
    done
}
TravelDir $1

function ProcessFile(){
        python /pubhome/lzeng/CPFrags/pdb2FragsPair.py -p $1 -o "/pubhome/lzeng/gnu_parallel/output/"$(printf $1 | cut -d '/' -f 6-) --splitSaveFrags --pairSDF
}

# for f in ${filelist[@]}
# do
#     echo $f
# done

export -f ProcessFile # remember to add this command
parallel ProcessFile ::: ${filelist[@]} # ::: is a parallel command symbol and follow parameter you want to transfer
# parallel echo ::: ${filelist[@]} |parallel  ProcessFile



#qsub ./run?.sh /tmp/lzeng02/pdb4 
#notice: do not end with '/', like './run.sh /tmp/lzeng02/pdb4/'
```
**应用情景**  
1. 实验室要求储存时最好不要在同一个文件夹下放很多文件，所以我对文件进行了分层储存(方法见[Some-bash-command/reorganise_files.sh](https://github.com/elifzeng/Computory-Background/blob/3591349295b7f09fa86235313a31baaa45f41a4a/Some-bash-command/reorganise_files.sh))，因此需要遍历找到多层文件夹下的所有文件。  
2. 提交任务后充分跑满32个核，拒绝占着茅坑不拉屎 💩现象。高级说法：使用并行计算  
**代码思路**  
用`function TravelDir`实现找到多层文件夹下所有pdb文件。[Bash append to array](https://linuxhint.com/bash_append_array/)  
中间遍历了一下列表，检查列表元素正确  
用[GNU_parallel](https://www.gnu.org/software/parallel/man.html#EXAMPLE:-Calling-Bash-functions)实现并行，借鉴了[这里](https://www.jianshu.com/p/c5a2369fa613)。  
先创建一个数组，存下所有文件的绝对路径，然后遍历传递给`function ProcessFile`处理。  
此处使用了`$1`，使得脚本的普适性更高。一般用法:
```bash
qsub parallel_run.sh //tmp/lzeng02/pdb4
```
参数为储存所有文件的大文件夹。
