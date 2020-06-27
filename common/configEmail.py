
"""
功能描述：配置邮件，实现发送邮件的功能
解析：
    1-读取配置，调用readconfig
    2-创建邮件连接配置（host，username……）
    3-创建邮件内容（添加附件report）
    4-调用发送邮件的方法
"""
from email.mime.text import MIMEText
import smtplib, os, time
from email.mime.multipart import MIMEMultipart
from email.header import Header


report=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ '/' + 'testReport' + '/' + 'report1.html'
print(report)
class configEmail(object):
    # 属性
    def __init__(self):
        # 1-读取config配置
        rc=readConfig()
        conf_list=rc.get_email_all()
        self.mail_host=conf_list[0][1]
        self.sender=conf_list[4][1]
        self.receiver=conf_list[5][1]
        self.mail_user=conf_list[1][1]
        self.mail_pwd=conf_list[2][1]
        self.subject=conf_list[6][1]
        self.content=conf_list[7][1]
        self.title=time.strftime("%b %d %Y %H:%M:%S",time.localtime())

        # 2-定义邮件内容（）
        with open(report,'rb') as file:
            mail_body=file.read()
            # 代表邮件内容分多个部分
            self.msg=MIMEMultipart()
            # 基本信息(key大小写均可)
            self.msg['From']=self.sender
            self.msg['To']=self.receiver
            self.msg['Subject']=Header(self.subject,'utf-8')

            # 邮件的文字内容部分
            content=MIMEText(self.content)
            self.msg.attach(content)

            # 邮件的附件内容部分
            att=MIMEText(mail_body,'plain','utf-8')
            att['Content-Type']='application/octet-stream'
            att["Content-Disposition"]='attachment;filename={}.html'.format(self.title)
            self.msg.attach(att)

    # 发送邮件（1-实例化；2-连接服务器；3-登录；4-发送邮件）
    def send_mail(self):
        s=smtplib.SMTP()
        s.connect(self.mail_host)
        s.login(self.mail_user, self.mail_pwd)
        s.sendmail(self.sender, self.receiver, self.msg.as_string())

    # 查找最新的测试报告，添加附件
    def find_latest_report(self):
        pass


if __name__ == '__main__':
    re=configEmail()
    re.send_mail()

