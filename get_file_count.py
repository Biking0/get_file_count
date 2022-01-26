#!/usr/bin/env python
# -*-coding:utf-8 -*-
# ***************************************************************************
# 文件名称：hadoop_monitor.py
# 功能描述：发送短信通用脚本
# 输 入 表：
# 输 出 表：
# 创 建 者：hyn
# 创建日期：20211129
# 修改日志：
# 修改日期：
# ***************************************************************************
# 程序调用格式：nohup python /home/dacp/shell/hadoop_monitor/hadoop_monitor.py >> /home/dacp/shell/hadoop_monitor/nohup.out &
# ***************************************************************************

import json
from flask import request, Flask  # flask模块
import send_sms
import os

# from dingtalkchatbot.chatbot import DingtalkChatbot  # 钉钉发送群消息模块

# Flask通用配置
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/webhook/test/', methods=['GET'])
def IssueCreate():

    result = os.popen("echo '123'").readlines()

    f=open('test.log','a+')
    f.write(str(result))

    request.get_data()

    # post_data = json.loads(request.get_data())

    print 123
    # alerts_list = post_data['alerts']
    #
    # for i in range(len(alerts_list)):
    #
    #     # 获取警告内容
    #     content = str(alerts_list[i]['annotations']['description'])
    #
    #     # 屏蔽内存告警，告警太频繁
    #     if 'memory' in content:
    #         f = open('/home/dacp/shell/hadoop_monitor/nohup.out', 'a+')
    #         print '屏蔽内存告警', content
    #         f.write(content)
    #         f.close()
    #         continue
    #
    #     send_sms.sendSms(content)
    #
    # result=os.popen('sh test.sh 123 34').readlines()


    return "OK", 200


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8060)


