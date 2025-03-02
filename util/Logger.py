#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Create: 2024/8/10 23:32
# @Author: liuzejin
"""
import logging
import os
import time


"""
1、定义log文件名和存放目录
2、创建记录器
3、设置日志等级
4、设置日志格式
5、创建控制台处理器，设置cmd输出日志和log文件日志
6、添加处理器到记录器里
"""


def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
SCR_DIR = os.path.join(CONFIG_DIR, '..')
OUTPUT_DIR = os.path.join(CONFIG_DIR, SCR_DIR, 'output')
LOG_DIR = os.path.join(OUTPUT_DIR, 'log')
create_dir(LOG_DIR)

# 定义log文件名
log_name = f"LOG-{time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))}.log"
# 定义log存放目录
log_file = os.path.join(LOG_DIR, log_name)

# 创建记录器
logger = logging.getLogger(log_file)
logger.handlers.clear()

# 设置日志等级
logger.setLevel(logging.DEBUG)
# 创建并设置格式器
LOGFORMAT = "[%(levelname)s][%(asctime)s.%(msecs)03d][%(filename)s:%(lineno)d][%(funcName)s]: %(message)s"
formatter = logging.Formatter(LOGFORMAT, '%Y-%m-%d %H:%M:%S')

# 创建控制台处理器，设置cmd日志
sh = logging.StreamHandler()
sh.setFormatter(formatter)
sh.setLevel(logging.DEBUG)

# 创建文件日志处理器，设置文件日志
fh = logging.FileHandler(log_file, encoding='utf-8')
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)

# 添加处理器到记录器
logger.addHandler(sh)
logger.addHandler(fh)

