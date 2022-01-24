#!/usr/bin/env python
# -*-coding:utf-8 -*-
# ***************************************************************************
# 文件名称：run.py
# 功能描述：hive表数据稽核
# 输 入 表：
# 输 出 表：
# 创 建 者：hyn
# 创建日期：20210106
# 修改日志：
# 修改日期：
# ***************************************************************************
# 源端程序调用格式：nohup python /home/dacp/shell/hadoop_monitor/run.py >> /home/dacp/shell/hadoop_monitor/nohup.out &

# ***************************************************************************

import os
import sys
import time
import hadoop_health

# 启动
if __name__ == '__main__':

    while True:
        # 休息10分钟，600
        hadoop_health.hadoop_health()
        hadoop_health.nn_status()
        print 'sleep 600'

        time.sleep(600)
