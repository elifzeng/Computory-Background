run:
```bash
code xxx.txt
```
error:
```bash
Unable to connect to VS Code server: Error in request.
Error: connect ENOENT /run/user/5056/vscode-ipc-2d90051b-b011-4d07-9690-411c2e1356b1.sock
    at PipeConnectWrap.afterConnect [as oncomplete] (node:net:1157:16) {
  errno: -2,
  code: 'ENOENT',
  syscall: 'connect',
  address: '/run/user/5056/vscode-ipc-2d90051b-b011-4d07-9690-411c2e1356b1.sock'
}
```
resolution:
run on bash:`VSCODE_IPC_HOOK_CLI=$( lsof | grep $UID/vscode-ipc | awk '{print $(NF-1)}' | head -n 1 )`  
[ref](https://github.com/microsoft/vscode-remote-release/issues/6997#issue-1319650016) 🐈‍

