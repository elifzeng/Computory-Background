# 集群批处理系统
## [Glossary](https://info.hpc.sussex.ac.uk/hpc-guide/glossary.html#term-tasks)
Meaning of `queues` `slots` `job script` `job id` `array job` `tasks` `modules`.
其他可见`Hand Book`

## Example
This is a job script named *qsub-test*.
```bash
#! /bin/bash
#$ -q honda   #-q <queue_name> 指定任务队列
##$ -pe honda 10 #-pe <parallel_environment_name> <num_core> parallel_environment设定并行环境
#$ -l hostname=n125.hn.org  # 若要指定不使用哪台主机，则为-l hostname=！n125.hn.org 
#$ -t 100-125 # <FIRST>-<LAST>:<STEPSIZE>
#$ -o /home/lzeng02/qsub-test/log/

##$ -e /home/lzeng02/qsub-test/log/
#$ -j y

printf "%10s: %10s\n" "JOB_ID" "$JOB_ID"
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
