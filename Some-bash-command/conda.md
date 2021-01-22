# Create a virtual environment for your project
[see more](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)
```bash
$ conda create -n yourenvname python=X.Y.Z anoconda
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
$ conda remove -n yourenvname -all
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
