# OA阅读爬虫

## 起因
  公司要求每天阅读OA信息，并不定期检查，唉。。。做正事有这样的态度和坚持就好了，为了避免被点名，还是想点办法糊弄一下吧

## 解决
  老早就看过python爬虫的教程，但是没有实践，正好这个机会可以学习一下，顺便解决问题。
  我的思路是这样的，通过命令行启动，带入登录OA的用户名和密码，然后打开OA页面列表中每个具体信息的链接，完成所谓的查阅
  1. 登录系统
    post方式，带入username和password，很奇怪的是，在URL中又已path方式传入了三个参数。总之加上这三个参数后，才能成功登陆。
  2. 打开OA主界面
    登陆后首页中，在OA功能页有一个进入系统的链接，此处使用这个链接，直接进入OA系统首页，通过SSO直接登陆OA系统
  3. 收集待阅列表中的链接
    待阅、待办项目为动态添加到页面，通过一个链接可以返回待阅、待办的列表html页面
  4. 打开链接，完成查阅
    遍历之前返回的列表页面，将具体每一项待阅、待办的链接获取，并进行访问，完成读取。

## 结束
  1. cookie的应用
  2. 未涉及session
  3. 初步使用正则来处理页面。
  4. 用DOM对象树来处理是否更好？
  5. 未来使用多线程，同时处理多个用户，多个文档
