import pandas as pd
from pyecharts import Bar

# 读取数据
df = pd.read_csv('got_1.csv', header=None)
# df = pd.read_csv('got_2.csv', header=None)
# df = pd.read_csv('got_3.csv', header=None)

# 汇总名称
names = []
for name in df[0]:
    if name not in names:
        names.append(name)

item = {}
for name in names:
    nums = []
    for num in df[df[0] == name][1]:
        nums.append(num)
    # 列表求和
    s = sum(nums)
    # 时间转换
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    item[name] = "%02d:%02d:%02d" % (h, m, s)

# 出场时间前15位角色
top15 = sorted(item.items(), key=lambda x: x[1], reverse=True)[:15]
for i in top15:
    print(i[1], i[0])
