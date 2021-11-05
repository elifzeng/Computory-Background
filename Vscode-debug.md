# How to debug in vscode
[Python debugging in VS Code](https://code.visualstudio.com/docs/python/debugging)
1. select `Run and Debug`
2. click the small gear on the right to create and configure the `launch.json` file
![image](https://user-images.githubusercontent.com/52747634/140479018-03f68da5-dc7d-4fab-9847-91dfd2481302.png)
3. the meaning of `launch.json` file
`Ctrl+space` to see available parameters.  
![image](https://user-images.githubusercontent.com/52747634/140479288-54740e5a-7f8b-42a8-9dec-75d9125570e2.png)  
`name`:file needed to be debugged  
`args`:command in terminal, use `""` and `,` to separate  
4. run with breakpoint
click sidebar to set breakpoint  
![image](https://user-images.githubusercontent.com/52747634/140480085-e838d488-f5cb-4058-8c96-aa6be4ce940c.png)  
5.`F5` or click Triangle icon to start debug  
![image](https://user-images.githubusercontent.com/52747634/140479902-d13ef8b8-5a52-45ae-aeae-e65067d6c612.png)  
![image](https://user-images.githubusercontent.com/52747634/140480330-09c30016-8bf2-4f14-a5e6-dbe311cb2c0f.png)  
1st icon: **Continue**, run to next breakpoint  
2nd icon: **Step over**, run to next line  
3rd icon: **Step into**, run into the called function  
4th icon: **Step out**, run out from the called function
