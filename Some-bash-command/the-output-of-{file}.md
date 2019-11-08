# file

Today I use `file`in bash:

```bash
[zenglj@x026 ~]$ file -b /usr/bin/ls
ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=937708964f0f7e3673465d7749d6cf6a2601dea2, stripped, too many notes (256)
```

But I don not understand the meaning of the output content, so some explaination are as follows.

## ELF(Executable and Linking Format)

[ELF](https://www.maixj.net/ict/elf-o-20705)是一种对象文件的格式，用于定义不同类型的对象文件（Object files）中都放了什么东西、以及都以什么样的格式去放这些东西。
有三种常见的ELF对象未见类型：

1. 可重定位的对象文件（Relocatable file）
这是由汇编器汇编生成的 .o 文件。
后面的链接器（linker）拿一些 Relocatable object files 作为输入，经链接处理后，生成一个可执行的对象文件 (Executable file) 或者一个可被共享的对象文件(Shared object file)。我们可以使用 ar 工具将众多的 .o Relocatable object files 归档(archive)成 .a 静态库文件。

2. 可执行的对象文件（Executable file）
这我们见的多了，就是编译器生产的可执行程序。
文本编辑器vi、调式用的工具gdb、播放mp3歌曲的软件mplayer等等都是Executable object file。
主要要跟shell脚本，或者python脚本区分，这些脚本也是可执行的，但是它们的结构不是Executable file，它们只是文本，由文件的第一行#!（shebang）定义系统应该调用那个程序来执行这个文本。

3. 可被共享的对象文件（Shared object file）
这些就是所谓的动态库文件，也即 .so 文件。如果拿前面的静态库来生成可执行程序，那每个生成的可执行程序中都会有一份库代码的拷贝。如果在磁盘中存储这些可执行程序，那就会占用额外的磁盘空间；另外如果拿它们放到Linux系统上一起运行，也会浪费掉宝贵的物理内存。如果将静态库换成动态库，那么这些问题都不会出现。

这里有[详细解释](https://wiki.jikexueyuan.com/project/c-study-notes/system.html)