#!/usr/bin/python3
from email import header
from email.utils import formataddr
import smtplib
import email
from email.mime.text import MIMEText                  #负责构造文本
from email.mime.image import MIMEImage                #负责构造图片
from email.mime.multipart import MIMEMultipart        #负责将多个对象集合起来
from email.header import Header
from socket import timeout
import time
#
mail_host="smtp.163.com" 
mail_user="17621702488@163.com" 
mail_pass="GKKVSSFETWULFRXE" 
#
class mail2(object):
        def __init__(self,mail_host,mail_user,mail_pass,mail_port):
             self.mail1_host = mail_host
             self.mail1_user = mail_user
             self.mail1_pass = mail_pass
             self.mail1_port = mail_port
             try:
                #self.server1 = smtplib.SMTP()
                #self.server1.connect(self.mail1_host,self.mail1_port)
                self.server1 = smtplib.SMTP_SSL(self.mail1_host,self.mail1_port)
                self.server1.set_debuglevel(2)
                self.server1.login(self.mail1_user,self.mail1_pass)
             except smtplib.SMTPException:
                print ("Error: 连接邮箱失败")
        def run_cls(self):
            self.server1.close()
        def run_txt1(self,receivers):
            sender = self.mail1_user
            message = MIMEText('花开花落总有时，总赖东君主', 'plain', 'utf-8')
            message['From'] = formataddr(["马常万骁",self.mail1_user],'utf-8')
            subject = '月儿弯弯照九照'
            message['Subject'] = Header(subject, 'utf-8')
            for rec in receivers:
                message['To'] = formataddr(["马方卓然",rec],'utf-8')
                try:
                    self.server1.sendmail(sender,rec,message.as_string())
                    print ("邮件发送成功")
                except:
                    print ("error:邮件发送失败")
            #
        def run_html1(self,receivers):
            receivers1 = receivers
            sender = self.mail1_user
            #
            mail_msg = """
            <p>花开花落总有时，总赖东君主</p>
            <p><a href="http://www.runoob.com">这是一个链接</a></p>
            """
            message = MIMEText(mail_msg, 'html', 'utf-8')
            message['From'] = Header("马常万骁", 'utf-8')
            message['To'] =  Header("马方卓然", 'utf-8')
            subject = '月儿弯弯照九照'
            message['Subject'] = Header(subject, 'utf-8')
            try:
                self.server1.sendmail(sender,receivers1,message.as_string())
                print ("邮件发送成功")
            except:
                print ("error:邮件发送失败")
        def run_annex1(self,receivers):
            sender = self.mail1_user
            mail_msg = """
            <p>花开花落总有时，总赖东君主</p>
            <p><a href="https://cn.bing.com">这是一个链接</a></p>
            """
            message = MIMEMultipart()
            message['From'] = Header("马常万骁 <%s>" % self.mail1_user,'utf-8')
            message['To'] =  Header("马方卓然 <%s>" % receivers, 'utf-8')
            subject = '月儿弯弯照九州'
            message['Subject'] = Header(subject, 'utf-8')
            message.attach(MIMEText(mail_msg, 'html', 'utf-8'))
            # 构造附件1，传送当前目录下的 test.txt 文件
            file1 = "D:\\Tool\\vscode\\微编程\\py\\mail\\alimail.py"
            att1 = MIMEText(open(file1, 'rb').read(),'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            att1["Content-Disposition"] = 'attachment; filename="alimail.py"'
            message.attach(att1)
            try:
                self.server1.sendmail(sender,receivers,message.as_string())
                print ("邮件发送成功")
            except:
                print ("error:邮件发送失败")
        def run_imge1(self,receivers):
            sender = self.mail1_user
            #
            message = MIMEMultipart('related')
            message['From'] = formataddr(["马常万骁",self.mail1_user],'utf-8')
            message['To'] =  Header("马方卓然", 'utf-8')
            subject = '月儿弯弯照九照'
            message['Subject'] = Header(subject, 'utf-8') 
            msgAlternative = MIMEMultipart('alternative')
            message.attach(msgAlternative)
            #
            mail_msg = """
            <p>花开花落总有时，总赖东君主</p>
            <p><a href="http://www.runoob.com">这是一个链接</a></p>
            <p>秀图演示：</p>
            <p><img src="cid:image1"></p>
            """
            msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
            # 指定图片为当前目录
            fp = open('D:\\IT\\Hello World\\python\\爬虫\\20220101.jpg', 'rb')
            msgImage = MIMEImage(fp.read())
            fp.close()
            # 定义图片 ID，在 HTML 文本中引用
            msgImage.add_header('Content-ID', '<image1>')
            message.attach(msgImage)
            try:
                self.server1.sendmail(sender,receivers,message.as_string())
                print ("邮件发送成功")
            except:
                print ("error:邮件发送失败")
#
if __name__ == '__main__':
    a=mail2("smtp.163.com","17621702488@163.com","GKKVSSFETWULFRXE",994)
    #a.run_txt1(['15738843050@139.com','corporate-slave@outlook.com','pinwuli@2980.com'])
    #a.run_html1(['15738843050@139.com','corporate-slave@outlook.com'])
    a.run_annex1('pinwuli@2980.com')
    #a.run_imge1(['15738843050@139.com','corporate-slave@outlook.com'])
    a.run_cls()
#
