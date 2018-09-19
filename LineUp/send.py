# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
import email
_user = "2970311382@qq.com"
_pwd  = "zlipbfbavherdfcj"
sent=smtplib.SMTP_SSL('smtp.qq.com',465)
#设置了SMTP服务器为stmp.qq.com 其端口号为465
file = open('file.txt','r')
text = str(file.read())
sent.login(_user, _pwd)#登陆
try:
    to=['469977511@qq.com']
    content=MIMEText(text)#MIMEText表示邮件发送具体内容
    content['Subject']='freebuf最新资讯'
    content['From']='2970311382@qq.com'
    content['To']=','.join(to)
    sent.sendmail('2970311382@qq.com',to,content.as_string())#三个参数
    sent.close()#关闭邮箱
    print "success"
except smtplib.SMTPException.e:
    print "Falied"
