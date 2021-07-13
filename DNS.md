## DNS Principle and resolution process detailed explanation
[reference](https://zhuanlan.zhihu.com/p/88260838)  
DNS解析是互联网访问的第一步，无论是使用笔记本浏览器访问网络还是打开手机app，访问网络资源的第一步都要经过DNS解析流程。
### What is DNS ?
**DNS就是域名系统**  
> DNS就是域名系统，是因特网中的一项核心服务，是用于实现域名和IP地址相互映射的一个分布式数据库，能够使用户更方便的访问互联网，而不用去记住能够被机器直接读取的IP数串。通过主机名，得到该主机名对应的IP地址的过程叫做域名解析（或主机名解析）。

### 域名结构解析
![image](https://user-images.githubusercontent.com/52747634/116811859-187ce780-ab7e-11eb-9502-d938e1e7a1d9.png)  
如上图所示，域名结构是树状结构，树的最顶端代表根服务器，根的下一层就是由我们所熟知的.com、.net、.cn等通用域和.cn、.uk等国家域组成，称为顶级域。网上注册的域名基本都是二级域名，比如 http://baidu.com、http://taobao.com 等等二级域名

### DNS解析流程
![image](https://user-images.githubusercontent.com/52747634/116811971-c9838200-ab7e-11eb-91ba-e48c7c204e50.png)  
如上图所示，我们将详细阐述DNS解析流程。

1、首先客户端位置是一台电脑或手机，在打开浏览器以后，比如输入http://www.zdns.cn 的域名，它首先是由浏览器发起一个DNS解析请求，如果本地缓存服务器中找不到结果，则首先会向根服务器查询，根服务器里面记录的都是各个顶级域所在的服务器的位置，当向根请求http://www.zdns.cn 的时候，根服务器就会返回.cn服务器的位置信息。

2、递归服务器拿到.cn的权威服务器地址以后，就会寻问cn的权威服务器，知不知道http://www.zdns.cn 的位置。这个时候cn权威服务器查找并返回http://zdns.cn 服务器的地址。

3、继续向http://zdns.cn 的权威服务器去查询这个地址，由http://zdns.cn 的服务器给出了地址：202.173.11.10

4、最终才能进行http的链接，顺利访问网站。

5、这里补充说明，一旦递归服务器拿到解析记录以后，就会在本地进行缓存，如果下次客户端再请求本地的递归域名服务器相同域名的时候，就不会再这样一层一层查了，因为本地服务器里面已经有缓存了，这个时候就直接把http://www.zdns.cn 的A记录返回给客户端就可以了。

### DNS资源记录
![image](https://user-images.githubusercontent.com/52747634/116812676-93e09800-ab82-11eb-9e78-b471f5eadee9.png)  
 记录一条域名信息映射关系，称之为资源记录（RR）。

当我们查询域名http://www.zdns.cn 的时候，查询结果得到的资源记录结构体中有如下数据：

1、TTL，就是生存周期，是递归服务器会在缓存中保存该资源记录的时长。

2、网络/协议类型，它的代表的标识是IN，IN就是internet，目前DNS系统主要支持的协议是IN。

3、type，就是资源记录类型，一般的网站都是都是A记录（IPv4的主机地址）。

4、rdata是资源记录数据，就是域名关联的信息数据。

### DNS服务器的分类
![image](https://user-images.githubusercontent.com/52747634/116812768-0fdae000-ab83-11eb-9b44-8a7bcdcdb5c5.png)  
常见的DNS服务器就是两种：权威解析服务器和递归解析服务器。递归解析服务器也可以叫做localDNS。  

#### 权威解析服务器
DNS权威服务器保存着域名空间中部分区域的数据。如果DNS服务器负责管辖一个或多个区域时，称此DNS服务器为这些区域的权威服务器。

根权威DNS或者二级权威服务器中的资源记录标记被指定为区域权威服务器的DNS服务器。通过资源记录中列出服务器，其他服务器就认为它是该区域的权威服务器。这意味着在 NS 资源记录中指定的任何服务器都被其他服务器当作权威的来源，并且能肯定应答区域内所含名称的查询。

#### 递归服务器
递归服务器在正常情况下，初始的时候里面没有任何域名解析数据，里面所有的域名解析数据都来自于它到权威解析服务器的查询结果，一旦查询完毕，递归服务器就会根据TTL时间在本地形成一条缓存记录，并为用户提供DNS解析的查询服务，这是递归服务器的功能。  
