# coding:utf-8
import pandas as pd
from pandas import DataFrame

data = pd.read_excel("huagonginfo.xlsx", sheet_name='Sheet1')

# 增加行数据，在第5行新增
data.loc[7] = [1, '初级', '电工', '152224199101105555', '韩小顺', '男', '青峰白羽', '1991-01-10', '1999-01-01', 2, '3333333333',
               '本科', '18811663456', '备注的内容']

# 增加列数据，给定默认值None
# data['profession'] = None

# 保存数据
DataFrame(data).to_excel("huagonginfo.xlsx", sheet_name='Sheet1', index=False, header=True)
