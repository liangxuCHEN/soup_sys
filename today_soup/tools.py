import smtplib
from email.mime.text import MIMEText

MAIL_FROM = "chenliangxu68@163.com"

SMTP_SERVER = "smtp.163.com"

MAIL_PW = ""


def send_mail(mail_to, subject, msg_txt):
    # Record the MIME types of both parts - text/plain and text/html.
    msg = MIMEText(msg_txt, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = MAIL_FROM
    msg['To'] = mail_to
    server = smtplib.SMTP(SMTP_SERVER, 25)
    try:
        server.login(MAIL_FROM, MAIL_PW)
        mailto_list = mail_to.strip().split(",")
        if len(mailto_list) > 1:
            for mailtoi in mailto_list:
                server.sendmail(MAIL_FROM, mailtoi.strip(), msg.as_string())
        else:
            server.sendmail(MAIL_FROM, mail_to, msg.as_string())
    except Exception as e:
        print(e)
        server.quit()
        return False

    server.quit()
    return True


if __name__ == '__main__':
    send_mail('chenliangxu68@163.com', '测试', '<P>测试邮件</P><p>不要回复</p>')
