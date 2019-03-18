# _*_ encoding: utf-8 _*_
__author__ = 'SemiLavender'
__date__ = '2019/3/5 23:02'

from random import Random

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MXueTest.settings import EMAIL_FROM


def send_register_email(eamil, send_type="register"):
    email_record = EmailVerifyRecord()
    code = generate_random_str(16)
    email_record.code = code
    email_record.email = eamil
    email_record.send_type = send_type
    email_record.save()

    email_tilte = ""
    email_body = ""

    if send_type == "register":
        email_tilte = u"bupt 激活链接"
        email_body = u"请点击下面的连接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_tilte, email_body, EMAIL_FROM, [eamil, ])
        if send_status:
            pass
    elif send_type == "forget":
        email_tilte = u"bupt 密码重置"
        email_body = u"请点击下面的连接重置你的密码：http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_tilte, email_body, EMAIL_FROM, [eamil, ])
        if send_status:
            pass


def generate_random_str(random_length=8):
    random_str = ''
    chars = 'qwertyuiopasdfghjklzxcvbnm1234567890-=QWERTYUIOPASDFGHJKLZXCVBNM'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        random_str += chars[random.randint(0, length)]
    return random_str
