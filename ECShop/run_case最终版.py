import time
import unittest
import os
import HTMLTestRunnerPlugins

# 1.确定文件夹路径
base_path = os.path.dirname(__file__)
case_path = os.path.join(base_path, 'Case')
report_path = os.path.join(base_path, 'Report')
# 2.确定测试报告名称 时间命名
now = time.strftime('%Y-%m-%d %H_%m_%S')  # 格式化时间
print(now)
report_name = now + 'HTMLReport.html'  # 报告名称
report_file_path = os.path.join(report_path, report_name)  # html报告路径
print(report_file_path)
# 3.收集测试用例
suite = unittest.defaultTestLoader.discover(case_path)
# 4.执行用例并生成报告
with open(report_file_path, 'wb') as fp:
    runner = HTMLTestRunnerPlugins.HTMLTestRunner(
        stream=fp,
        title='ECshop页面自动化测试',
        description='兼容性测试',
        tester='0605')

    runner.run(suite)
