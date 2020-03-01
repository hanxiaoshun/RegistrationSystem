# coding:utf-8
import pandas as pd
from pandas import DataFrame

data = pd.read_excel("fujian04_excel_2.xlsx", sheet_name='培训人员花名册')

# 增加行数据，在第5行新增
data.loc[7] = [1, '初级', '电工', '152224199101105555', '韩小顺', '男', '青峰白羽', '1991-01-10', '1999-01-01', 2, '3333333333',
               '本科', '18811663456','4444']

# 增加列数据，给定默认值None
# data['profession'] = None

# 保存数据
DataFrame(data).to_excel("fujian04_excel_4.xlsx", sheet_name='培训人员花名册', index=False, header=0)
