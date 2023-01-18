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
and you can track its state and error by jobID `qstat -j jobID`. Track all users' job array by `qstat -u \*`. And Delete this job by `qdel jobID`.Or delete all Eqw jobs at once by 
```bash
qstat | grep Eqw| cut -b 1-7|xargs qdel
```
降低优先级`qalter {jobid} -p -80`  
![image](https://user-images.githubusercontent.com/52747634/159194937-20ee00ca-c006-4a79-a101-8195fae451d6.png)  
```bash
# 批量降低优先级
qstat -u \* |grep MPHE.*qw | cut -b 1-7 | xargs qalter -p -80
```
指定某几台机器运行任务  
```bash
指定只在n120-n129
qstat -q honda -u lzeng02 | awk '{print $1}' | xargs -I jobid qalter jobid -l hostname=n12[0-9]
指定不在n120-n129
qstat -q honda -u lzeng02 | awk '{print $1}' | xargs -I jobid qalter jobid -l hostname=!(n12[0-9])
```
可以添加`-R y`选项，这样当你的优先级比别人的高理论上可以把空闲节点锁住，直到有（指定的）28个空闲节点，把你的任务提交上去，在此期间优先级低于你但是申请核数少的任务是抢不过你的。  
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
## Disk quota exceeded
先查看磁盘使用情况
```bash
$ lfs quota -hu lzeng /pubhome/
Disk quotas for usr lzeng (uid 5056):
     Filesystem    used   quota   limit   grace   files   quota   limit   grace
      /pubhome/  1.667T      0k      0k       - 3500000* 3000000 3500000       -
uid 5056 is using default block quota setting
```
上面可以看到，是文件数超额里，接下来怎么解决自己想办法吧。。。  
## mpirun
k队列上跑orca内存不够。因此采取“占据32核，实际跑20核”的办法。需要[使用mpirun](https://www.cnblogs.com/devilmaycry812839668/p/15132333.html)。  
示例：
```bash
#! /bin/bash
##$ -N wb97
#$ -q opel
#$ -pe opel 32
#$ -o /pubhome/lzeng/data/error
#$ -e /pubhome/lzeng/data/error
#$ -wd /pubhome/lzeng/CPFrags/run_orca/qm_selection

source ~/.bashrc
conda activate py37

# for i in $(ls ~/data/pair25/redun_coord/??*.npz);do qsub -N $( basename $i )wb97 ～/CPFrags/run_orca/qm_selection/cal_energy_npz.sh $i; done

# get input file and output path

filebase=$( basename $1 )
m=$( echo $filebase | cut -d "." -f 1 )
oup="/pubhome/lzeng/data/QM_energy/wb97rot_$m"
echo Processing $filebase
mpirun -np 20 python /pubhome/lzeng/CPFrags/run_orca/qm_selection/cal_energy_npz.py $1 -o $oup
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
# Parallel Example 1
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

# Parallel Example 2
```bash
#!/bin/bash
##$ -N qmcal_n
#$ -q mazda
#$ -pe mazda 32
#$ -o /pubhome/lzeng/data/error
#$ -e /pubhome/lzeng/data/error
#$ -wd /pubhome/lzeng/CPFrags/run_orca/cal_energy

source ~/.bashrc
conda activate py37

#qsub -N qmcal_n calc_energy.sh /pubhome/lzeng/data/extra_25/pdb0 no "/" in the end
# using/pubhome/lzeng/data/extra_25/pdb0 to run example

# get input file and output path
filelist=()
outputlist=()
function TravelDir(){
    for file in `ls $1`
    do
        if [ -d "$1/$file" ]
        then
            echo $1/$file
            TravelDir "$1/$file"
        else
            filebase=$( basename $file )
            # echo $file
            # echo $1
            if [[ $filebase = pdb*.ent.*.sdf ]] # do not add "" to wildcard character（通配符）
            then
                filelist[${#filelist[@]}]="$1/$file"
                m=$( echo $filebase | cut -d "." -f 1 )
                n=$( echo $filebase | cut -d "." -f 3-4 )
                i=$( echo $1/$file | cut -d "/" -f 6-7 )
                outputlist[${#outputlist[@]}]="/pubhome/lzeng/data/QM_energy/$i/$m.$n.json.gz"
            elif [[ $filebase = pdb????.ent.sdf ]]
            then
                echo 
            elif [[ $filebase = pdb????.*.sdf ]]
            then
                filelist[${#filelist[@]}]="$1/$file"
                a=$( echo $1/$file | cut -d "/" -f 6-)
                outputlist[${#outputlist[@]}]="/pubhome/lzeng/data/QM_energy/$a.jzon.gz"
            fi
        fi
    done
}
TravelDir $1

# for q in ${outputlist[@]}
# do
#     echo aaaaa
#     echo $q
# done

# run sdf2qm.py parallelly
function CalculateEng(){
    echo Processing $1
    python /pubhome/lzeng/CPFrags/run_orca/cal_energy/sdf2qm.py $1 -o $2
    echo Results are saved 'in' $2
}

export -f Calc90ulateEng
parallel --link CalculateEng ::: ${filelist[@]} ::: ${outputlist[@]} # 传两个参数（no combination）
```
传参参考了[这里](https://blog.csdn.net/weixin_29602351/article/details/116863908)

# GPU task commitment
命令不懂的可以搜索`man qsub`。
```bash
#!/usr/bin/env bash
#$ -q cuda 
#$ -l ngpus=1
#$ -cwd # current work directory
#$ -o /pubhome/lzeng/data/log/
#$ -e /pubhome/lzeng/data/log/
#$ -N zinctest
source /usr/bin/startcuda.sh
MY COMMAND
source /usr/bin/end_cuda.sh
```
## chack all ampere status
查看每台机器上哪张gpu卡已经被使用了。
```bash
pdsh -w ssh:k[224-233] ' nvidia-smi|grep MiB|grep -v %'|sort
```

# GPU/CPU sleep
先占领几个core，然后再在上面运行测试程序
```bash
#!/bin/bash
#$ -q ampere
#$ -pe ampere 18
# 或者只占一个gpu
#$ -l ngpus=1
#$ -cwd
#$ -o /dev/null
#$ -e /dev/null
#$ -N graphormer
source /usr/bin/startcuda.sh
sleep 7d
source /usr/bin/end_cuda.sh
```
## 新cluster 机器
![image](https://user-images.githubusercontent.com/52747634/213122049-18d72365-9992-4cb3-a880-964b64efc851.png)
