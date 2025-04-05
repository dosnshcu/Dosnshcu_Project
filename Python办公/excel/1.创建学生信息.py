import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 生成示例数据
np.random.seed(42)
names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Hannah", "Ian", "Jack", "Kate", "Leo", "Mia", "Noah", "Olivia", "Paul", "Quinn", "Rachel", "Steve", "Tom", "Uma", "Victor", "Wendy", "Xander", "Yvonne", "Zack", "Amy", "Brian", "Catherine", "Daniel", "Ella", "Felix", "Gina", "Henry", "Isla", "James", "Karen", "Liam", "Monica", "Nathan", "Olga", "Peter", "Quincy", "Rebecca", "Samuel", "Tina", "Ulysses", "Vera"]
subjects = ["数学", "物理", "化学", "英语", "历史"]

# 生成学生基本信息 DataFrame
data = {
    "学号": [f"S{1000 + i}" for i in range(50)],
    "姓名": np.random.choice(names, size=50, replace=True),
    "年龄": np.random.randint(18, 25, size=50),
    "性别": np.random.choice(["男", "女"], size=50),
    "入学日期": [(datetime(2020, 1, 1) + timedelta(days=np.random.randint(0, 365 * 4))).strftime('%Y-%m-%d') for _ in range(50)],
    "是否毕业": np.random.choice([True, False], size=50),
    "平均绩点": np.round(np.random.uniform(2.0, 4.0, size=50), 2),
    "成绩": [[
        {"语文": np.random.randint(60, 100)},
        {"数学": np.random.randint(60, 100)},
        {"英语": np.random.randint(60, 100)}
    ]for _ in range(50)]
}

# 创建学生基本信息 DataFrame
df = pd.DataFrame(data)
print(df.dtypes)
# 保存到 Excel 文件
df.to_excel("学生信息.xlsx", index=False)
print("Excel 文件 '学生信息.xlsx' 已创建！")
