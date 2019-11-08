# Undo some command you ran before

Today I installed a software, using "sudo yum install". Then I want to uninstall it.
This approach undo the command directly, so it can be used in other circumstances.

```bash
sudo yum install redhat-lsb #这就是那个我随后要卸载的软件
```

```bash
yum history -h # 查看history 的帮助界面，看到usage里有个list
#也可以通过 yun history -h | less 对帮助界面的内容进行查找
sudo yum history list # 可不加list.显示yum命令运行历史列表，在我现在这台机子上看到install redhat-lsb的ID为138。
sudo yum history info 138 # 查看ID为138的transaction（可译为事务）的详细信息，其中包括了redhat-lsb安装时一起安装（变更）的包，Packages Altered。
sudo yum history undo 138 # 撤销该事务
#再查看yum history, 第139号命令为history undo 138
```

除了undo，还可以redo，好奇心驱使我又装一遍。。。stupid clever operation...

```bash
sudo yum history redo 138 # install that sofrware again
# Then I choose 'N' to aborte the operation.
```

每次运行命令后都会出现这三行指令：

```bash
Failed loading plugin: upload-profile
Failed loading plugin: subscription-manager
Failed loading plugin: product-id
```

插件加载失败，据说是权限问题，但我在网上没有找到答案。
