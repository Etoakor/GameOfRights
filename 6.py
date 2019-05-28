import pandas as pd
from pyecharts import Bar
import json

# 读取人物信息文件
with open("script-bag-of-words.json", 'r', errors='ignore') as load_f:
    load_dict = json.load(load_f)

# 对人物人名进行统计
names = []
for i in load_dict:
    for j in i['text']:
        name = j['name']
        if name not in names:
            names.append(name)
# 读取数据

df = pd.read_csv('got_3.csv', header=None)

def people_season(season, mes1, mes2):
    """
    每季统计
    """
    attr = mes1
    v1 = mes2
    bar = 'bar' + str(season)
    bar = Bar('第' + str(season) + '季人物出场时间分布', title_pos='center', title_top='18', width=800, height=400)
    bar.add("", attr, v1, is_convert=True, xaxis_min=10, yaxis_label_textsize=8, is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=True, is_legend_show=False, label_pos='right', is_yaxis_inverse=True, is_splitline_show=False)
    bar.render('第' + str(season) + '季人物出场时间分布.html')


# 遍历每一季
for season in range(1, 9):
    df2 = df[df[2] == season]
    for i in df2[0]:
        if i not in names:
            names.append(i)
    item = {}
    # 对人物出现时间进行统计
    for j in names:
        num_3 = []
        for k in df2[df2[0] == j][1]:
            num_3.append(k)
        item[j] = sum(num_3)
    # 排序
    top15 = sorted(item.items(), key=lambda x: x[1], reverse=True)[:15]
    print(top15)
    name_2 = []
    num_2 = []
    # 对前15位进行数据汇总
    for p in top15:
        name_2.append(p[0])
        num_2.append(p[1])
    print(season, name_2, num_2)
    people_season(season, name_2, num_2)