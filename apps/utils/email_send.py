#!/usr/bin/env python
# -*- coding:utf-8 -*-
from users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail

from MxOnline.settings import EMAIL_FROM

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type='register'):
    email_recode = EmailVerifyRecord()
    code_str = random_str(16)
    email_recode.code = code_str
    email_recode.email = email
    email_recode.send_type = send_type
    email_recode.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = "慕学在线网注册激活链接"
        email_body = "请点击下面的链接激活你的账号:http://127.0.0.1:8000/action/{0}".format(code_str)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass