#!/usr/bin/env python
# -*-coding:utf-8 -*-
# ***************************************************************************
# 文件名称：send_sms.py
# 功能描述：发送短信通用脚本
# 输 入 表：
# 输 出 表：
# 创 建 者：hyn
# 创建日期：20211117
# 修改日志：
# 修改日期：
# ***************************************************************************
# 程序调用格式：python send_sms.py
# ***************************************************************************

import requests
import json
import random
from xml.dom.minidom import parse

import datetime as date_time

url = "http://10.85.130.210:8080/APL-SMSService/SMSService?wsdl"
phone_list = ['17796653422', '15239629674', '18119748221']
# phone_list = ['17796653422']
app_key = 'A7EC6FFBC13A2E8E'


def sendSms(content):
    now_time = str(date_time.datetime.now())[0:19]

    content = content + ' 当前时间：' + now_time

    id = str(random.randrange(1, 1000000000000, 13))

    phone_str = ''
    for i in range(len(phone_list)):
        phone_str = phone_str + ' ' + phone_list[i]

    payload = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<SOAP-ENV:Envelope xmlns:ns0=\"http://ws.sms.zjapl.com\" xmlns:ns1=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:xsi=\"http\r\n    ://www.w3.org/2001/XMLSchema-instance\" xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\">\r\n<SOAP-ENV:Header/>\r\n<ns1:Body>\r\n    <ns0:sendSmsXzqh>\r\n        " \
              "<id>%s</id>\r\n        <appKey>%s</appKey>\r\n        <phoneNums>%s</phoneNums>\r\n        <content>%s</content>\r\n        <time>1517367751</time>\r\n        <flag>1</flag>        \r\n        </ns0:sendSmsXzqh>\r\n        </ns1:Body>\r\n        " \
              "</SOAP-ENV:Envelope>" % (id, app_key, phone_str, content)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_data = response.text

    if '0' in response_data:
        print '短信发送成功'
    else:
        print '短信发送失败'

# sendSms('测试1')
