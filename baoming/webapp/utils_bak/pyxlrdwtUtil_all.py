# coding:utf-8
import pandas as pd
from pandas import DataFrame

data = pd.read_excel("all_info.xlsx", sheet_name='Sheet1')

# 增加行数据，在第5行新增
for i in range(10):
    data.loc[i + 4] = [1, '韩小顺', '男', '152224199101105555', '初级', '否', 33.5, '17099887654', '1999-01-01', '青峰白羽软件技术工作室',
                       '韩小顺', '电（高）, 钳（中）']
    DataFrame(data).to_excel("all_info.xlsx", sheet_name='Sheet1', index=False, header=True)
# 增加列数据，给定默认值None
# data['profession'] = None

# 保存数据
DataFrame(data).to_excel("all_info_01.xlsx", sheet_name='Sheet1', index=False, header=True)
