#coding:utf-8
import smtplib  
from email.mime.text import MIMEText  
mailto_list=["lvchunhui7@126.com"] 
mail_host="smtp.163.com"  #设置服务器
mail_user="18500581509@163.com"    #用户名
mail_pass="95123120290"   #口令 
mail_postfix="163.com"  #发件箱的后缀
  
def send_mail(to_list):  #to_list：收件人；sub：主题；content：邮件内容
    content = u'您好，请点击以下链接激活邮箱：' + '<a href="http://www.wafuli.cn">http://www.wafuli.cn</a>'
    msg = MIMEText(content,_subtype='html',_charset='gb2312')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = u'挖福利邮箱激活'    #设置主题
    msg['From'] = mail_user
    msg['To'] = ";".join(to_list)  
    try:  
        s = smtplib.SMTP()  
        s.connect(mail_host)  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(mail_user, to_list, msg.as_string())  #发送邮件
        s.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False  
if __name__ == '__main__':  
    if send_mail(mailto_list,):  
        print "发送成功"  
    else:  
        print "发送失败"  