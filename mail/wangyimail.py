#!/usr/bin/python3
from email import header
from email.utils import formataddr
import smtplib
import email
from email.mime.text import MIMEText                  #负责构造文本
from email.mime.image import MIMEImage                #负责构造图片
from email.mime.multipart import MIMEMultipart        #负责将多个对象集合起来
from email.mime.application import MIMEApplication    #不管什么类型的附件，都用MIMEApplication，MIMEApplication默认子类型是application/octet-stream。
from email.header import Header
from socket import timeout
import time
#
class mail2(object):
        def __init__(self,mail_host,mail_user,mail_pass,mail_port):
             self.mail1_host = mail_host
             self.mail1_user = mail_user
             self.mail1_pass = mail_pass
             self.mail1_port = mail_port
             try:
                self.server1 = smtplib.SMTP_SSL(self.mail1_host,self.mail1_port,timeout=30)
                self.server1.set_debuglevel(2)
                self.server1.login(self.mail1_user,self.mail1_pass)
             except smtplib.SMTPException:
                print ("Error: 连接邮箱失败")
        def run_cls(self):
            self.server1.close()
        def run_annex1(self,receivers,dirname,file1):
            """导入抄送邮箱地址"""
            userlis = []
            maillis = []
            with open(dirname,"r",encoding="utf-8") as f:
                lines = f.readlines()
            for line in lines:
                user1,mail1 = line.strip().split(':')
                user1 = user1.strip('\n')
                userlis.append(user1)
                maillis.append(mail1)
            """导入抄送邮箱地址"""
            """提取接入邮箱地址"""
            dict1_user1 = list(receivers.keys());receivers_user1 = dict1_user1[0]
            dict1_mail1 = list(receivers.values());receivers_mail1 = dict1_mail1[0]
            """提取接入邮箱地址"""
            #
            mail_msg = """
            <p>花开花落总有时，总赖东君主</p>
            <p><a href="https://cn.bing.com/?mkt=zh-CN">这是一个链接</a></p>
            """
            """构造正文"""
            message = MIMEMultipart()
            message['From'] = Header(receivers_user1 + "<%s>" %self.mail1_user)
            message['To'] =  Header("<%s>" %receivers_mail1)
            message['Cc'] = Header('<%s> <%s> <%s>' % (maillis[0],maillis[1],maillis[2]))
            message['Subject'] = Header(file1, 'utf-8')
            message.attach(MIMEText(mail_msg, 'html', 'utf-8'))
            """构造正文"""
            """构造附件""" 
            dir1 =("D:\AK云\浙江信创云周报日报\\%s" % file1)
            att1 = MIMEApplication(open(dir1,'rb').read())
            att1.add_header('Content-Disposition','attachment',filename=file1)
            message.attach(att1)
            """构造附件""" 
            rec = [receivers_mail1]
            try:
                self.server1.sendmail(self.mail1_user,rec+maillis,message.as_string())
                print ("邮件发送成功")
            except:
                print ("error:邮件发送失败")
if __name__ == '__main__':
    a=mail2("smtp.163.com","17621702488@163.com","GKKVSSFETWULFRXE",994)
    #a=mail2("smtp.alibaba-inc.com","wb-mhz929995@alibaba-inc.com","Service#414414",465)
    a.run_annex1({"mahaizhuang":"corporate-slave@outlook.com"},"D:\\IT\\Hello World\\python\\爬虫\\mail\\name.txt","20220120.png")
    a.run_cls()
#
["17621702488@163.com","15738843050@139.com","wb-mhz929995@alibaba-inc.com"]
