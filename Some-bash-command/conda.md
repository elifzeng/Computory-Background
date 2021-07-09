# Create a virtual environment for your project
[see more](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)
```bash
$ conda create -n yourenvname python=X.Y.Z anaconda
```
and activate the environment
```bash
$ conda activate yourenvname
```
## Install additional Python packages to a virtual environment
```bash
$ conda install -n yourenvname [package]
```
## Deactivate a virtual environment
```bash
$ conda deactivate
```
## Delete a no longer needed virtual environment
```bash
$ conda remove -n yourenvname --all
```
## List environment you created 
```bash
conda env list
```
# Install some package or version not in official library with [conda-forge](https://github.com/conda-forge/conda-forge.github.io)
what's [conda-forge](https://cloud.tencent.com/developer/article/1035806) ?
```bash
conda install [package] -c conda-forge 
```
## Check available package version 
```bash
conda search package
```
## Install miniconda
https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html#install-macos-silent
## 将一些环境变量和virtual environment绑定在一起
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#macos-and-linux

## environments I usuallly use
```bash
#since now htmd only support python <=3.8.0.a1
conda create -n python python=3.7
conda install -c acellera -c conda-forge htmd
htmd_register
conda install -c conda-forge ase -y
conda create -n chemtools
conda activate chemtools
conda create -n chemtools -c conda-forge rdkit ambertools
conda install --name chemtools pylint -y
/home/zenglj/opt/miniconda/envs/chemtools/bin/python /home/zenglj/.vscode-server/extensions/ms-python.python-2021.1.502429796/pythonFiles/pyvsc-run-isolated.py /home/zenglj/.vscode-server/extensions/ms-python.python-2021.1.502429796/pythonFiles/shell_exec.py conda install --name chemtools ipykernel -y /tmp/tmp-7649pNQu3yEeN5vE.log
/home/zenglj/opt/miniconda/envs/chemtools/bin/python
source activate /home/zenglj/opt/miniconda/envs/chemtools
conda create -n qm
conda install --name qm pylint -y
# the context of the two .sh file is shown below
cat /home/zenglj/opt/miniconda/envs/qm/etc/conda/activate.d/env_vars.sh
cat /home/zenglj/opt/miniconda/envs/qm/etc/conda/deactivate.d/env_vars.sh
conda create -n deepchem python=3.7 anaconda
conda activate deepchem
conda install -c rdkit rdkit

```
and the `.bashrc`  
```bash
(base) [zenglj@x021 ~]$ cat .bashrc
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/zenglj/opt/miniconda/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/zenglj/opt/miniconda/etc/profile.d/conda.sh" ]; then
        . "/home/zenglj/opt/miniconda/etc/profile.d/conda.sh"
    else
        export PATH="/home/zenglj/opt/miniconda/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

# User specific environment
export PATH=/home/zenglj/Downloads/plop25:$PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions

# #NMRCLUST
# export PATH='/home/zenglj/data/nmrclust':$PATH
# alias nmrclust='/home/zenglj/data/nmrclust/nmrclust'
```
```bash
(base) [zenglj@x021 OptProgram]$ cat /home/zenglj/opt/miniconda/envs/qm/etc/conda/activate.d/env_vars.sh
#!/bin/sh

# Quantum Chem

# Gaussian
export g16root=/home/zenglj/gaussian
export GAUSS_SCRDIR=/home/zenglj/gaussian/g16/scratch
source /home/zenglj/gaussian/g16/bsd/g16.profile

# fullspace
# export PYTHONPATH=$PYTHONPATH:/home/zenglj/git/fullspace/examples/grepPDB/fpdb

# Orca
export PATH=/home/zenglj/data/orca_4_1_2:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/zenglj/data/orca_4_1_2
export ORCA_PATH=/home/zenglj/data/orca_4_1_2
alias orca='/home/zenglj/data/orca_4_1_2'

# Vaspkit
export PATH=$HOME/opt/vaspkit.1.2.4/bin:$PATH
```
```bash
(base) [zenglj@x021 OptProgram]$ cat /home/zenglj/opt/miniconda/envs/qm/etc/conda/deactivate.d/env_vars.sh
#!/bin/sh

echo "It's hard to undo the changes which g16.profile makes on like \$PATH, \$LD_LIBRARY_PATH and so on."
echo "Please exit this shell and open a new one".
```
