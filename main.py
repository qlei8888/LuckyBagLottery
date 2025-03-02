#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Create: 2024/8/10 23:41
# @Author: liuzejin
"""
import os
import subprocess
import sys
import yaml
from util.DevicesController import DevicesController
from util.Logger import logger

# 读取配置文件
yamlPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.yml")
# 添加项目路径到系统变量
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
logger.debug(sys.path)


def get_yml(yamlPath):
    """读取配置文件"""
    print(os.getcwd())
    with open(yamlPath, encoding='utf-8') as f:
        data = yaml.safe_load(f)

    return data

def get_connected_devices():
    """获取已连接的设备列表"""
    devices = []
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
    output = result.stdout.split('\n')
    for line in output[1:]:
        if line and not line.startswith('offline'):
            device_id = line.split('\t')[0]
            devices.append(device_id)
    return devices


if __name__ == '__main__':
    """读取配置文件"""
    yml = get_yml(yamlPath)
    """构造设备控制对象，并调用实例方法"""
    main = DevicesController(get_connected_devices(), interest=yml['interest'])  # interest=True 通过关注直播间抽奖，False为商城抽奖
    main.main()
