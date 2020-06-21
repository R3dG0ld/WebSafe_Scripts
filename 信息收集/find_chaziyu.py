import requests
import sys
import urllib3
import socket
import threading
from bs4 import BeautifulSoup

def banner():
    print(
"""
  _____ _           _ ____                        _       
 |  ___(_)_ __   __| |  _ \  ___  _ __ ___   __ _(_)_ __  
 | |_  | | '_ \ / _` | | | |/ _ \| '_ ` _ \ / _` | | '_ \ 
 |  _| | | | | | (_| | |_| | (_) | | | | | | (_| | | | | |
 |_|   |_|_| |_|\__,_|____/ \___/|_| |_| |_|\__,_|_|_| |_|
\n\t\tAuthor:RG Date:2020/6/5\n"""
    )

api = "https://chaziyu.com/{domain}/"
header = {'Connection':'close','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
ports = [80,81,82,88,8080,8081,8088,8090]
openPorts = []
urllib3.disable_warnings()
def useage():
    banner()
    print("Useage:python3 {0} [domain] --check".format(sys.argv[0]))
def tcpPortScan(ip, port, openPort):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建套接字
    sock.settimeout(0.1) #设置延时
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            openPort.append(port) #如果端口开放，就赋给openPort
    except:
        pass
    sock.close() #关闭套接字
    
def threadingPortScan(host, portList):
    nloops = range(len(portList))
    threads = []
    openPorts=[]
    for i in nloops:
        t = threading.Thread(target=tcpPortScan, args=(host, portList[i], openPorts))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    return openPorts #返回该域名下开放的端口列表
def checkAlive(domain):
    try:
        host = socket.gethostbyname(f'{domain}') #获取域名IP
        openedPorts = threadingPortScan(host, ports)
        if len(openedPorts) > 0:
            print(f'[+] {domain}\t[{host}]\t{openedPorts} Open')
    except:
        pass
def getSubDomain(domain):
    print(f"[*] Start Geting [{domain}]...")
    target = api.format(domain=domain)
    res = requests.get(target,headers=header,verify=False,timeout=3).text
    soup = BeautifulSoup(res,'html.parser')
    links = soup.find_all(name='tr',attrs={'class':'J_link'})
    for line in links:
        for link in line.find_all('a'):
            if len(sys.argv) == 3:
                if sys.argv[2] == '--check':
                    checkAlive(link.text)
                else:
                    exit('[-] Error Parmar !!!')
            else:
                print(link.text)
if __name__=="__main__":
    if len(sys.argv) == 1:
        useage()
    else:
        if '.' not in sys.argv[1]:
            print("[-] Error Domain !!!")
        else:
            banner()
            getSubDomain(sys.argv[1])
