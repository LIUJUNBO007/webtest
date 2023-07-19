import unittest
import os

# 收集测试用例
# 确定测试用例存放路径--->找Case文件夹路径
base_path = os.path.dirname(__file__)
case_path = os.path.join(base_path, 'Case')
print(base_path)
# 收集测试用例
suit = unittest.defaultTestLoader.discover(case_path)  # 默认执行所有以test开头的文件
# 执行测试用例
runner = unittest.TextTestRunner()
runner.run(suit)
