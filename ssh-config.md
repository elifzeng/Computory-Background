`~/.ssh/config`  
`chmod 600 config` (otherwise the error `Bad owner or permissions on /home/zenglj/.ssh/config` will be rose)

```bash
Host x25402
    HostName x254.hn.org
    User lzeng02
    IdentityFile /home/test/.ssh/id_rsa.pub

Host x254
    HostName x254.hn.org
    User lzeng02
    IdentityFile /home/test/.ssh/id_rsa.pub
```

Now you can ssh by `ssh x254` rather than `ssh lzeng@x254`
