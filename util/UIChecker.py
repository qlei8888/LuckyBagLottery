#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Create: 2024/8/10 23:47
# @Author: liuzejin
"""
wait_time = 12


def checkByTextWait(d, text, timeout=wait_time):
    """检查匹配的文本是否存在"""
    if d(text=text).exists(timeout=wait_time):
        return True
    else:
        return False


def check_ctrls_wait_exists_by_text(d, controls_text, timeout_millisecond=wait_time, click=False):
    """通过文本检查控件是否存在，并等待wait_time时间
    Args:
        d: uiautomatior device
        controls_text: Android control text
    Returns:
        Int: 0 or 1
    """
    # if d(text=controls_text).wait.exists(timeout=wait_time):
    if d(text=controls_text).wait(timeout=timeout_millisecond):
        if click:
            d(text=controls_text).click(timeout=True)
        return True
    else:
        return False


def check_by_xpath(d, xpath, timeout=wait_time, click=False):
    """检查匹配的xpath是否存在"""
    if d.xpath(xpath).wait(timeout=timeout):
        if click:
            d.xpath(xpath).click(timeout=True)
        return True
    else:
        return False


def check_ctrls_wait_exists_by_resource_id(d, resource_id, timeout=wait_time, click=False):
    """通过resource id检查控件是否存在，并等待wait_time时间
    Args:
        d: uiautomatior device
        resource_id: Android control text
        timeout_millisecond: 超时时间，有默认值
    Returns:
        Int: 0 or 1
    """
    # if d(resourceId=resource_id).wait.exists(timeout=timeout_millisecond):
    # if d.wait(Until.findObject(By.res(resource_id)), timeout_millisecond):
    if d(resourceId=resource_id).wait(timeout=timeout):
        if click:
            d(resourceId=resource_id).click(timeout=True)
        return True
    else:
        return False


def check_ctrls_wait_exists_by_id_and_index(d, resource_id, i):
    """通过resource_id和index检查控件是否存在，并等待wait_time时间
    Args:
        d: uiautomatior device
        resource_id: Android control id
        i: index
    Returns:
        Int: 0 or 1
    """
    if d(resourceId=resource_id, index=i).wait(timeout=wait_time):
        return 1
    else:
        return 0


def check_ctrls_wait_exists_by_className_and_index(d, className, i, click=False):
    """通过className和index检查控件是否存在，并等待wait_time时间
    Args:
        d: uiautomatior device
        className: Android control id
        i: index
    Returns:
        Int: 0 or 1
    """
    if d(className=className, index=i).wait(timeout=wait_time):
        if click:
            d(className=className, index=i).click()
        return True
    else:
        return False


def check_ctrls_exists_by_text(d, controls_text, click=False):
    """通过文本检查控件是否存在
    Args:
        d: uiautomatior device
        controls_text: Android control text
    Returns:
        Int: 0 or 1
    """
    if d(text=controls_text).exists:
        if click:
            d(text=controls_text).click(timeout=True)
        return 1
    else:
        return 0


def check_ctrls_exists_by_resource_id(d, resource_id, click=False):
    """通过resource id检查控件是否存在
    Args:
        d: uiautomatior device
        resource_id: Android control text
    Returns:
        Int: 0 or 1
    """
    if d(resourceId=resource_id).exists:
        if (click):
            d(resourceId=resource_id).click(timeout=True)
        return 1
    else:
        return 0


def check_ctrls_exists_by_id_and_index(d, resource_id, i):
    """通过resource_id和index检查控件是否存在
    Args:
        d: uiautomatior device
        resource_id: Android control id
        i: index
    Returns:
        Int: 0 or 1
    """
    if d(resourceId=resource_id, index=i).exists:
        return 1
    else:
        return 0


def check_ctrls_exists_by_child_id(d, resource_id, child_id, click=False):
    if check_ctrls_exists_by_resource_id(d, resource_id=resource_id, click=False) == 0:
        return 0

    if d(resourceId=resource_id).child(resourceId=child_id).exists:
        if click:
            d(resourceId=resource_id).child(resourceId=child_id).click()
        return 1
    else:
        return 0


def check_controls_checked_by_resource_id(d, resource_id, flag, set_flag=False):
    """通过resource_id，判断checked选项为true or false
    Args:
        d: uiautomatior device
        resource_id: Android control id
        flag: true or false
    Returns:
        Int: 0 or 1
    """
    if d(resourceId=resource_id).info['checked'] == flag:
        return 1
    else:
        if set_flag:
            d(resourceId=resource_id).click()
        return 0


def check_controls_checked_by_text(d, content, flag):
    """通过text，判断checked选项为true or false
    Args:
        d: uiautomatior device
        text: text
        flag: true or false
    Returns:
        Int: 0 or 1
    """
    if d(text=content).info['checked'] == flag:
        return 1
    else:
        return 0


def get_text_by_resource_id(d, resource_id):
    """
        通过资源ID获取文本信息，如果不存在则返回空字符串

        Args:
    d (obj): uiautomator对象，用于查找元素
        eg. d = uiautomator.Device("127.0.0.1:6200")

    resource_id (str): 需要查找的元素的资源ID，格式为"package:id/name"
        eg. "com.tencent.mobileqq:id/title"

        Returns:
    str: 如果元素存在，返回该元素的文本信息；否则返回空字符串"""
    if not d(resourceId=resource_id).exists:
        return ''

    return d(resourceId=resource_id).info['text']


def check_text(d, resource_id, text):
    """判断id为resourceid的控件 text是否符合预期
    Args:
        d: uiautomatior device
        resource_id: Android control resource_id
        text: expected text
    Returns:
        Int: 0 or 1
    """
    if not d(resourceId=resource_id).exists:
        return 0

    if d(resourceId=resource_id).info['text'] == text:
        return 1
    else:
        return 0


def checkBychild(d, resource_id, resource_id_child, text):
    """判断id为resourceid的控件子text是否符合预期
    Args:
        d: uiautomatior device
        resource_id: Android control resource_id
        resource_id_child: child text
    Returns:
        Int: 0 or 1"""
    if d(resourceId=resource_id).child(resourceId=resource_id_child).info['text'] == text:
        return 1
    else:
        return 0


def check_controls_click_text(d, controls_text):
    """判断按钮是否置灰 & text & clickable
    Args:
        d: uiautomatior device
        controls_text: Android control text
    Returns:
        Int: 0 or 1
    """
    if d(text=controls_text).info['clickable'] is True:
        return 1
    else:
        return 0


# assertIn(a, b)     a in b
def check_ainb(d, resource_id, b):
    """判断控件文本是否包含在b中
    Args:
        d: uiautomatior device
        resource_id: Android control resource id
    Returns:
        Int: 0 or 1
    """
    if d(resourceId=resource_id).info['text'] in b:
        return 1
    else:
        return 0


def check_controls_click_enabled_by_resource_id(d, resource_id):
    """判断控件是否可点击
    Args:
        d: uiautomatior device
        resource_id: Android control resource id
    Returns:
        Int: 0 or 1
    """
    if d(resourceId=resource_id).info['enabled']:
        return 1
    else:
        return 0


def scroll_to_text(d, text, click=False):
    """滑动到指定TEXT"""
    if d(scrollable=True).exists:
        d(scrollable=True).scroll.to(text=text)
    if d(text=text).exists:
        if click:
            d(text=text).click()
        return 1
    else:
        return 0


def scroll_to_resource_id(d, point, click=False):
    """滑动到指定位置"""
    if d(scrollable=True).exists:
        d(scrollable=True).scroll.to(resourceId=point)

    if d(resourceId=point).exists:
        if click:
            d(resourceId=point).click()
        return 1
    else:
        return 0


'''
def check_controls_exists_by_resource_id_appium(driver, resource_id):
    """通过resource id检查控件是否存在 - for appium
    Args:
        driver: appium webdriver
        resource_id: Android control resource id
    Returns:
        Int: 0 or 1
    Raises:
        NoSuchElementException: An error occurred when element doesn't exist
    """
    try:
        if driver.find_element_by_id(resource_id).is_displayed():
            return 1
        else:
            return 0
    except NoSuchElementException as e:
        raise e
        return 0
'''


def lucky_bag_if_exists(d):
    times = None
    # 超级福袋
    super_bag = d(className='com.lynx.tasm.behavior.ui.LynxFlattenUI', descriptionContains='超级福袋')
    # 普通福袋
    general_bag = d(className='android.widget.TextView', descriptionContains='秒')
    if super_bag.exists(timeout=30):
        times = super_bag.get_text().split(' ')[1]
        super_bag.click()
        return times, True
    elif general_bag.exists(timeout=15):
        inf = general_bag.info
        times = inf.get('contentDescription')
        # 判断 times 是否以 "秒" 结尾
        if not times.endswith('秒'):
            return None, False
        general_bag.click()
        return times, True
    else:
        return times, False


def check_ctrls_exists_by_class_and_index(d, classname, i):
    """通过resource_id和index检查控件是否存在
    Args:
        d: uiautomatior device
        resource_id: Android control id
        i: index
    Returns:
        Int: 0 or 1
    """
    if d(className=classname, index=i).exists:
        return True
    else:
        return False
