#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Create: 2024/8/10 23:50
# @Author: liuzejin
"""

import uiautomator2 as u2
from util import UIChecker
import time
from util.Logger import logger


class PageController:
    def __init__(self, device_id):
        self.device_id = device_id
        self.package = 'com.ss.android.ugc.aweme'
        self.activity = '.splash.SplashActivity'
        self.sleep = 0
        self.d = u2.connect(device_id)

    def start_app(self):
        self.d.app_start(self.package, self.activity, wait=True)
        logger.info(f"启动了{self.package}")

    def stop_app(self):
        self.d.app_stop(self.package)
        logger.info(f"关闭了{self.package}")

    def clickByText(self, text):
        result = UIChecker.check_ctrls_wait_exists_by_text(self.d, text, click=True)
        if result:
            logger.info(f"点击{text}成功")
            return True
        else:
            logger.debug(f"未找到{text}")
            return False

    def clickById(self, id):
        result = UIChecker.check_ctrls_wait_exists_by_resource_id(self.d, id, click=True)
        if result:
            logger.info(f"点击{id}成功")
        else:
            logger.debug(f"未找到{id}")

    def click_point(self, x, y):
        self.d.click(x, y)
        logger.info(f"点击了{x},{y}")

    def swipe_up_click(self, target_text):
        """
        下滑并点击直播间
        :param target_text: 点击进入直播间
        :return:
        """
        while True:
            self.d.swipe(0.5, 0.8, 0.5, 0.2)
            element = self.d(text=target_text)
            if element.exists:
                element.click(timeout=True)
                # 再次确认是否进入直播间
                if UIChecker.checkByTextWait(self.d, '说点什么...'):
                    logger.info(f"已在直播间中")
                    break
                else:
                    continue
            logger.info(f"上滑找直播间中。。")

    def square_live(self):
        if UIChecker.check_by_xpath(self.d, '//*[@content-desc="侧边栏"]/android.widget.FrameLayout[1]', click=True):
            self.clickByText('直播广场')

    def interest_live(self):
        """
        通过个人中心关注列表进入直播间，这里比较稳定
        :return:
        """
        self.clickByText("我")
        self.clickByText("关注")
        count = 0
        while True:
            if UIChecker.check_ctrls_wait_exists_by_resource_id(
                    self.d, "com.ss.android.ugc.aweme:id/avatar_live_tag", click=True):
                return True
            elif count >= 10:
                return False
            else:
                self.swipe_on()
                count += 1

    def swipe_on(self):
        self.d.swipe(0.5, 0.8, 0.5, 0.2)
        logger.info(f"上滑屏幕一次。。")

    def lucky_bag_if_exists(self):
        """
        查找福袋，并设置实例属性开奖时间。没有福袋return False
        :return:
        """
        times, flag = UIChecker.lucky_bag_if_exists(self.d)
        if flag:
            m, s = int(times.split('分')[0]), int(times.split('分')[1].split('秒')[0])
            logger.info(f"找到福袋，开奖时间为{m}分{s}秒，正在准备尝试参与中")
            time.sleep(2)
            self.sleep = m * 60 + s - 2
            return True
        else:
            return False

    def back_designation_button(self, button):
        """
        返回指定元素下
        :return:
        """
        while True:
            if UIChecker.check_ctrls_wait_exists_by_resource_id(self.d, button, timeout=5) or \
                    UIChecker.checkByTextWait(self.d, button, timeout=5):
                logger.info(f"关闭抽奖结果弹窗，回到直播间内")
                break
            else:
                self.d.press("back")

    def close_button(self):
        while True:
            result = UIChecker.check_ctrls_exists_by_class_and_index(self.d,
                                                                     'com.lynx.tasm.ui.image.FlattenUIImage', 17)
            if result:
                self.d(className='com.lynx.tasm.ui.image.FlattenUIImage', index=17).click()
                logger.info(f"关闭了中奖结果弹窗")
            else:
                break

    def join_comment_task(self):
        """
        发送评论 参与抽奖任务
        """
        if UIChecker.check_ctrls_wait_exists_by_text(self.d, '发送评论 参与抽奖', click=True):
            self.watcher_stop()
            self.waiting()

    def comment_task_back(self):
        """
        去发表评论任务，不参与，跳过这一次的福袋
        """
        if UIChecker.check_ctrls_wait_exists_by_text(self.d, '去发表评论'):
            self.back_designation_button('说点什么...')

    def shop_member_back(self):
        """
        开通店铺会员任务，不参与，跳过这一次的福袋
        """
        if UIChecker.check_ctrls_wait_exists_by_text(self.d, '去发表评论'):
            self.back_designation_button('说点什么...')

    def join_prize_draw_task(self):
        """
        参与抽奖任务
        """
        if UIChecker.check_ctrls_wait_exists_by_text(self.d, '参与抽奖', click=True):
            self.watcher_stop()
            self.waiting()

    def join_fans_comment(self):
        """加入粉丝团，并参与（一键发表评论）任务"""
        self.clickByText("加入粉丝团")
        self.clickByText("加入粉丝团")
        time.sleep(1)
        self.back_designation_button('说点什么...')
        self.watcher_stop()
        if self.lucky_bag_if_exists():
            if self.clickByText("一键发表评论"):
                self.waiting()
            else:
                self.clickByText("参与抽奖")
                self.waiting()

    def start_watch_live(self):
        """开始观看直播任务"""
        if UIChecker.check_ctrls_wait_exists_by_text(self.d, '开始观看直播任务', click=True):
            self.back_designation_button('说点什么...')
            self.watcher_stop()
            self.waiting()

    def waiting(self):
        logger.info(f"参与成功，等待开奖中")
        time.sleep(self.sleep)

    def watcher_run(self):
        # 应对措施
        self.d.watcher("活动已结束弹窗").when("活动已结束").call(self.back_designation_button("说点什么..."))
        self.d.watcher("更新应用弹窗").when("以后再说").click()
        self.d.watcher("开通店铺会员任务").when("去开通店铺会员").call(self.shop_member_back)
        self.d.watcher("去发表评论任务，不进行参与").when("去发表评论").call(self.comment_task_back)
        self.d.watcher("即将开奖 无法参与任务").when("即将开奖 无法参与").call(self.back_designation_button("说点什么..."))
        self.d.watcher("直播结束页面").when("直播已结束").call(self.swipe_on)

        # 参与福袋任务
        self.d.watcher("发送评论任务").when("发送评论 参与抽奖").call(self.join_comment_task)
        self.d.watcher("加入粉丝团，并参与一键评论").when("加入粉丝团").call(self.join_fans_comment)
        self.d.watcher("参与抽奖任务").when("参与抽奖").call(self.join_prize_draw_task)
        self.d.watcher("观看直播任务").when("开始观看直播任务").call(self.start_watch_live)
        self.d.watcher.run()
        logger.info("watcher启动")

        if not self.d.watcher.triggering:
            logger.debug("watcher未触发")
            self.back_designation_button("说点什么...")


    def watcher_stop(self):
        self.d.watcher.stop()
        logger.info("watcher停止")


if __name__ == '__main__':
    test = PageController('192.168.31.53:37749')
    test.watcher_run()
