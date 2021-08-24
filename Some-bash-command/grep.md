# Grep
## 正则表达式和通配符的区别
通配符用于**匹配文件名**，完全匹配  
[Linux grep 命令和通配符](https://abcfy2.gitbooks.io/linux_basic/content/first_sense_for_linux/command_learning/wildcard.html)  

![image](https://user-images.githubusercontent.com/52747634/124849182-e13d1380-dfd0-11eb-99a2-62386dc4b026.png)

正则表达式用于**匹配字符串**，包含匹配  
[Grep中的正则表达式](https://m.linuxidc.com/Linux/2020-05/163192.htm#:~:text=Grep%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%20%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%88%96%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%98%AF%E4%B8%8E%E4%B8%80%E7%BB%84%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%8C%B9%E9%85%8D%E7%9A%84%E6%A8%A1%E5%BC%8F%E3%80%82%E6%A8%A1%E5%BC%8F%E7%94%B1%E8%BF%90%E7%AE%97%E7%AC%A6%EF%BC%8C%E6%9E%84%E9%80%A0%E6%96%87%E5%AD%97%E5%AD%97%E7%AC%A6%E5%92%8C%E5%85%83%E5%AD%97%E7%AC%A6%E7%BB%84%E6%88%90%EF%BC%8C%E5%AE%83%E4%BB%AC%E5%85%B7%E6%9C%89%E7%89%B9%E6%AE%8A%E7%9A%84%E5%90%AB%E4%B9%89%E3%80%82,GNU%20grep%E6%94%AF%E6%8C%81%E4%B8%89%E7%A7%8D%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E8%AF%AD%E6%B3%95%EF%BC%8CBasic%EF%BC%8CExtended%E5%92%8CPerl%E5%85%BC%E5%AE%B9%E3%80%82)  
![image](https://user-images.githubusercontent.com/52747634/124849380-409b2380-dfd1-11eb-9dfb-7b18f734a4b6.png)

## Example
```bash
# 一行字符串中匹配多个字段
# -E 是使用拓展正则表达式，^表示以HETATM开头，".*"表示匹配任意数量任何字符
$ grep -E '^HETATM.*FUN.*CL' pdb1z9y.ent
HETATM 2030 CL1  FUN A 500      14.452   5.808  17.337  1.00 13.12          CL
```
```txt
# part of pdb1z9y.ent
HETATM 2024  N1  FUN A 500      15.638   1.427  16.184  1.00  9.06           N  
HETATM 2025  S1  FUN A 500      15.137   2.679  16.784  1.00 10.54           S  
HETATM 2026  O1  FUN A 500      13.659   2.616  16.733  1.00 11.02           O  
HETATM 2027  O2  FUN A 500      15.713   2.917  18.087  1.00 10.56           O  
HETATM 2028  C1  FUN A 500      15.610   3.973  15.675  1.00 12.13           C  
HETATM 2029  C2  FUN A 500      15.293   5.320  15.885  1.00  8.91           C  
HETATM 2030 CL1  FUN A 500      14.452   5.808  17.337  1.00 13.12          CL  
HETATM 2031  C3  FUN A 500      15.637   6.352  15.001  1.00 12.46           C  
HETATM 2032  C4  FUN A 500      16.404   6.027  13.888  1.00 19.10           C  
HETATM 2033  N2  FUN A 500      16.779   6.993  12.936  1.00 16.58           N  
HETATM 2034  C5  FUN A 500      16.423   8.403  13.146  1.00 24.52           C  
HETATM 2035  C6  FUN A 500      17.421   9.022  14.085  1.00 28.78           C  
HETATM 2036  C7  FUN A 500      18.622   9.482  13.738  1.00 26.50           C  
```
