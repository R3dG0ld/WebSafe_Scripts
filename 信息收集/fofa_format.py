import urllib
import base64
import json


Rdata="""
fofa的api响应base64编码，前提是fofa调用api时fields参数要为host
"""
Rdata=Rdata.encode("utf-8")
Ndata = base64.b64decode(Rdata)
Ndata=urllib.unquote(Ndata)
JsData=json.loads(Ndata)
iplist=JsData["results"]
iplistS = '\n'.join(iplist)
print iplistS
