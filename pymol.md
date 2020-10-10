`10.7 schodinger教学笔记`
### fandamental operation
- download pdb file from pdb
    from pdb website or `GET PDB`
- open file with `file-import structure`
- menu （很多可以自己尝试，将光标停留在按钮上也会显示其功能说明）
    - 指向四角图表表示将结构放到界面中心
    - `[L]` 将ligand放到界面中心 
    - 右下角加号-clipping plane：小窗显示
    从左到右，从上到下
    - `A Atoms` 选中 P:protein/L:ligand/S:strain
    - `style 颜料盘` 各种显示方式，如隐藏、颜色、显示氢原子等
        - try `surface - right mouse - disply option`，该surface 可在右下角网状图标上关闭
    - `present 滑块` - `apply custom preset`
    - 下面一行小选项可以从右侧`Tasks`中搜索选出，点亮星标，就能显示出来
- mouse
    left 选中
    right 拖动

### 小分子对接 (all the status and output file can be seen in monitor)
*如果结果与预想的不一样，可能是在工作区中的structure选错了*
- protein preparation (add H, etc)
    - 默认设置 - click `preprocess` to run
- 创建pocket `receptor grid generation`
    - 左侧工作栏选择 `proteinx - minimized`
    - `receptor grid generation - pick to identity the ligand`，用鼠标在视图界面选择ligand
- ligPrep(ligand preparation)
    - use structures from `Workspace (1 included entry)` - run
- ligand docking (docking)
    - in `receptor grid` choose file generated in `创建pocket`
    - in `use ligands from ` choose file  generated in `ligPrep` 
    - run
- score 
    - `Table - show Props - docking score` 一般为负值，负得越多越好。just for reference and choose the top 100 frags to explore.
- present
    - select pocket and ligand simultaneosly
    - `style - surface - rught mouse - dislay options - color scheme - electrostatic potential - OK`
- draw a new ligand as you like and dock it
    - `ligand interaction`（或者直接右键左下角选择view in 2D sketcher） 
    - draw and `save as new`
    - now a new ligand is genetated and you can dock it as described before.
