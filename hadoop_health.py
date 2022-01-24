#!/usr/bin/env python
# -*-coding:utf-8 -*-
# ***************************************************************************
# 文件名称：hadoop_health.py
# 功能描述：发送短信通用脚本
# 输 入 表：
# 输 出 表：
# 创 建 者：hyn
# 创建日期：20211129
# 修改日志：
# 修改日期：
# ***************************************************************************
# 程序调用格式：nohup python /home/dacp/shell/hadoop_monitor/hadoop_health.py >> /home/dacp/shell/hadoop_monitor/nohup.out &
# ***************************************************************************

import os
import json
import send_sms
import requests


def hadoop_health():
    url = "https://10.85.85.2:8380/api/v2/health?Accept=application/json"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    print(response.text)

    result_json = json.loads(response.text)

    if result_json['status'] != 'UP' or result_json['details']['Database'] != 'UP' or result_json['details'][
        'ApacheDs'] != 'UP':
        content = '重要，星环集群状态异常！！！'
        print content
        send_sms.sendSms(content)
    else:
        content = '星环集群状态正常'
        print content


# 监控namenode状态
def nn_status():
    nn1_sh = 'source /home/hive/TDH-Client/init.sh;export HADOOP_USER_NAME=hdfs;hdfs haadmin -getServiceState nn1'
    nn2_sh = 'source /home/hive/TDH-Client/init.sh;export HADOOP_USER_NAME=hdfs;hdfs haadmin -getServiceState nn2'
    result1 = os.popen(nn1_sh).readlines()
    result2 = os.popen(nn2_sh).readlines()
    print result1
    print result1[-1]

    nn_status = str(result1[-1].replace('\n', '')) + str(result2[-1].replace('\n', ''))
    print nn_status
    if 'standby' in nn_status and 'active' in nn_status:
        content = '星环集群nn状态正常'
        print content
    else:
        content = '重要，星环集群nn状态异常！！！'
        print content
        send_sms.sendSms(content)
