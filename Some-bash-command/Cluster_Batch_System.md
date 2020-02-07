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
and you can track its state by jobID `qstat -j jobID`.And Delete this job by `qdel jobID`

## Example2
This is a job script named *qsub-test*. You can see more commmands pf `qsub` by `man qsub`.
```bash
#! /bin/bash
#$ -q honda   #-q <queue_name> 指定任务队列
##$ -pe honda 10 #-pe <parallel_environment_name> <num_core> 设定并行环境 parallel_environment是啥见handbook最下 Submit CPU job
#$ -l hostname=n125.hn.org  # 若要指定不使用哪台主机，则为-l hostname=！n125.hn.org 
#$ -t 100-125 # <FIRST>-<LAST>:<STEPSIZE> 用于提交 只该改变参数的重复任务
#$ -o /home/lzeng02/qsub-test/log/ # output 

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
