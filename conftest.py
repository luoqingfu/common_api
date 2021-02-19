#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   conftest.py    
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/14 9:16 下午   luoqingfu   1.0         None
'''

# import lib
import logging
import os
from datetime import time

import pytest
import requests
from _pytest.runner import runtestprotocol
from py._xmlgen import html

# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR + "/report/"

# 配置运行的 URL
baseurl = "https://api.ruguoapp.com/1.0"
serverurl = 'http://134.175.157.xx:8000//api'

# 用户名
phone = 13600000000

# 密码
password = '123456'  # 123456

# 失败重跑次数
rerun = "0"

# 运行测试用例的目录或文件
cases_path = "./test_dir/"


# 设置用例描述表头
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.pop()


# 设置用例描述表格
@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    用于向测试用例中添加用例的开始时间、内部注释
    :param item:
    """

    outcome = yield
    report = outcome.get_result()
    report.description = description_html(item.function.__doc__)
    extra = getattr(report, 'extra', [])
    report.extra = extra


def pytest_terminal_summary(terminalreporter):
    """
    获取所有接口测试用例执行的情况
    :param terminalreporter:
    :return:
    """
    passed = len(terminalreporter.stats.get('passed', []))
    failed = len(terminalreporter.stats.get('failed', []))
    skipped = len(terminalreporter.stats.get('skipped', []))
    try:
        url = serverurl + '/statusnumber'
        request = requests.post(
            url=url,
            data=({
                'pass_number': passed,
                'skipped_number': skipped,
                'failed_number': failed
            }),
        )
    except Exception as e:
        logging.exception(e)


def description_html(desc):
    """
    将用例中的描述转成HTML对象
    :param desc: 描述
    :return:
    """
    if desc is None:
        return "No case description"
    desc_ = ""
    for i in range(len(desc)):
        if i == 0:
            pass
        elif desc[i] == '\n':
            desc_ = desc_ + ";"
        else:
            desc_ = desc_ + desc[i]

    desc_lines = desc_.split(";")
    desc_html = html.html(
        html.head(
            html.meta(name="Content-Type", value="text/html; charset=latin1")),
        html.body(
            [html.p(line) for line in desc_lines]))
    return desc_html


def new_report_time():
    """
    获取最新报告的目录名（即运行时间，例如：2018_11_21_17_40_44）
    """
    files = os.listdir(REPORT_DIR)
    files.sort()
    try:
        return files[-1]
    except IndexError:
        return None


if __name__ == "__main__":
    pytest.main(['-s', '-q'])
