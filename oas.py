#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, getopt, urllib, urllib2, cookielib

# 登录系统的URL
loginUrl = 'http://intranet.airchina.com.cn/PortalProject/appmanager/intraCA/indexCA?_nfpb=true&_windowLabel=T6201139491307581705078&_pageLabel=P400365441304674042407'

# 利用cookie请求访问另一个网址，此网址是OA首页
OAHomeUrl = 'http://intranet.airchina.com.cn/SSOAgent/appAction!getAppLink.action?appId=1'

# 进入OA桌面，包含待办、待阅、等其他内容
OAdetailUrl = 'http://oa.airchina.com.cn/HQ/myportal/HQ/__cm100/__frframe?stay_period=7'

# 登陆后首页上关于OA的待阅列表
needReadUrl = 'http://intranet.airchina.com.cn/TaskNew2/oataskToRead.action'

def main():
    opts, args = getopt.getopt(sys.argv[1:], "hu:p:")
    username=""
    password=""
    for op, value in opts:
        if op == "-u":
            username = value
        elif op == "-p":
            password = value
        elif op == "-h":
            help()
            sys.exit()
    spider(username, password)

def spider(username, password):
    if username=="":
        help()
        sys.exit()
    if password=="":
        help()
        sys.exit()
# 声明一个CookieJar对象实例来保存cookie
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    postdata = urllib.urlencode({'username':username,'password':password})
# 模拟登录，并把cookie保存到变量
    result = opener.open(loginUrl,postdata)

# 利用cookie请求访问网址：OA首页
    # result = opener.open(OAHomeUrl)

# 进入OA桌面，包含待办、待阅、等其他内容
    # result = opener.open(OAdetailUrl)

    # html = result.read()

    # print html

# 登陆后首页上关于OA的待阅列表
    result = opener.open(needReadUrl)

    html = result.read()

    print html
  


def help():
    help_text = """Usage: oas [options]
       Options:
        -u     OA User Name
        -p     OA Password for this User
        -h     This Help
    """
    print help_text

if __name__ == '__main__':
    main();