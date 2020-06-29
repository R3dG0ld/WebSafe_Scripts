# WebSafe_Scripts
## 这是我写的一些小脚本和工具，方面渗透测试人员使用。
**！！！工具仅供安全从业者研究使用！！！**
### 0x1 信息收集
|序号|脚本名称|描述|
|:---:|:---|:---|
|1|[信息收集/findDomain_By_chaziyu.py](信息收集/findDomain_By_chaziyu.py)|解析chaziyu.com取网站域名的小脚本|
|2|[信息收集/fofa_format.py](信息收集/fofa_format.py)|解析fofa的API结果的小脚本(使用时把fofa api的结果进行base64编码，然后替换掉脚本里的，直接运行即可解析出host。)|

### 0x2 漏洞利用
|序号|脚本名称|描述|
|:---:|:---|:---|
|1|[利用工具/dedecms/getAdminBak.py](利用工具/dedecms/getAdminBak.py)|利用Win+Appache特性跑dedecms管理密码的小脚本|
|2|[利用工具/ThinkPHP/ThinkLogFinder.zip](利用工具/ThinkPHP/ThinkLogFinder.zip)|扫描ThinkPHP日志文件，支持多种版本。|
|3|[利用工具/Nexus Repository/CVE-2019-7238/NexusKiller.exe](利用工具/Nexus Repository/CVE-2019-7238/NexusKiller.exe)|Nexus Repository[CVE-2019-7238]RCE利用工具|

