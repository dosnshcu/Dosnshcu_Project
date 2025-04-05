import pandas as pd

pd.set_option('display.max_rows', None)  # 1. 显示所有行
pd.set_option('display.max_columns', None)  # 2. 显示所有列
pd.set_option('display.expand_frame_repr', False)  # 3. 防止换行（每行占用一行，不自动换行）
pd.set_option('display.width', 0)  # 4. 适应终端宽度，避免数据被截断
pd.set_option('display.max_colwidth', None)  # 5. 显示完整文本内容（防止长文本被截断）


df = pd.read_excel('学生信息.xlsx',
                   engine='openpyxl',
                   # parse_dates=['入学日期'],  # 将“入学日期”解析为日期格式
                   # dtype={
                   #     '是否毕业': bool,
                   #     '平均绩点': float
                   # }
                   )
print(df.dtypes)
print('-'*100)
print(df.head())
