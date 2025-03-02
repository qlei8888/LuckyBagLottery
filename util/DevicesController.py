#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Create: 2024/8/11 0:12
# @Author: liuzejin
"""

import threading
from util import UIChecker
from util.PageController import PageController
from util.Logger import logger


class DevicesController:
    def __init__(self, devices_list, interest=True):
        self.devices_list = devices_list
        self.interest = interest
        self.d_object = []
        self.threads = []

    def create_object(self, device_id):
        """
        创建一个PageController对象，并处理单个设备的逻辑
        :param device_id:
        :return:
        """
        objects = PageController(device_id)
        self.d_object.append(objects)
        while True:
            objects.start_app()
            try:
                if self.interest:
                    if not objects.interest_live():
                        objects.stop_app()
                        continue
                else:
                    objects.square_live()
            except Exception as e:
                objects.stop_app()
                logger.error(f"出现异常{e}, 重启app")
                continue
            count = 0
            while True:
                try:
                    if objects.lucky_bag_if_exists():
                        if objects.clickByText('一键发表评论'):
                            objects.waiting()
                        else:
                            objects.watcher_run()

                        if UIChecker.checkByTextWait(objects.d, '我知道了', timeout=5):
                            logger.info(f"本次福袋未中奖")
                            objects.back_designation_button('说点什么...')
                            count = 0
                            continue
                        elif UIChecker.checkByTextWait(objects.d, '立即领取奖品', timeout=5):
                            logger.info(f"本次福袋已中奖")
                            objects.back_designation_button('说点什么...')
                            count = 0
                            continue
                    else:
                        objects.swipe_on()
                        count += 1
                        if count > 5:
                            raise Exception("连续5次未参与福袋")
                        continue
                except Exception as e:
                    objects.stop_app()
                    logger.error(f"出现异常{e}, 重启app")
                    break

    def main(self):
        if self.devices_list:
            for device_id in self.devices_list:
                # 创建线程，并将设备 ID 作为参数传递给线程的 target 方法
                thread = threading.Thread(target=self.create_object, args=(device_id,))
                self.threads.append(thread)
                thread.start()

                # 等待所有线程执行完成
            for thread in self.threads:
                thread.join()
        else:
            logger.error("设备列表为空")


if __name__ == '__main__':
    dlist = ['192.168.31.153:5555']
    test = DevicesController(dlist)
    test.main()
