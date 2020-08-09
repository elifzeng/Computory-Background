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

`generate ssh key`

1st, check if ssh-key already exist. If not, genetate a new ssh-key.  
```bash
ssh-keygen -t rsa
# Creates a new ssh key
Generating public/private rsa key pair.
Enter file in which to save the key (/your_home_path/.ssh/id_rsa):
Enter passphrase (empty for no passphrase): 
#
The last step can be skipped.
```
