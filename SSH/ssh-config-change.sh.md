Annotation for `ssh-config-change.sh`.所里的wifi为内网，所外的为外网。在外网里需要先访问`www.huanglab.org.cn`跳板机进入内网再连到自己的主机。在内网需要
访问`www.huanglab.org.cn(k058)`再连到主机，而`huangniu54`是实验室内部的子网，直接可以连`x021`。需要注意的是，由于实验室的设置，连有线时，`username@xn`后面会自动补全域
名`hn.org`。（关于域名的解释可见[此处](https://news.west.cn/60534.html)）。但连wifi时需要手动补全`username@xn.hn.org`。
```bash
#!/usr/bin/bash

ssh-config-change(){
    if [[ $# -ne 1 ]]; then
        echo "ERROR: Number of arguments is not 1."
        exit 1
    fi

    locate=$1

    if [[ $locate == "home" ]]; then
        cp $HOME/.ssh/config.home $HOME/.ssh/config
        message="home"
    elif [[ $locate == "lab" ]]; then
        cp $HOME/.ssh/config.lab $HOME/.ssh/config
        message="at lab"
    fi

    printf "SSH config file have been changed for working %s.\n" "$message"
}
```

#6 `$#`传递给脚本或函数的参数个数。`-ne`为不等于(其他比较符号见[page](https://blog.csdn.net/qiuyoungster/article/details/46999559))。  
#13 `$1`为传递给脚本的第一个参数。  

