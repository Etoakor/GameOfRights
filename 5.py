# 统计每季人物出场时间
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
# print(names)

# 获取人物说话次数
item = {}
for name in names:
    num = 0
    for i in load_dict:
        for j in i['text']:
            if j['name'] == name:
                num += 1
    item[name] = num
# 读取数据

df = pd.read_csv('got_3.csv', header=None)

top15 = sorted(item.items(), key=lambda x: x[1], reverse=True)[:15]
for i in range(1, 9):
    name_1 = []
    nums_1 = []
    df1 = df[df[2] == i]
    for j in top15:
        num_1 = []
        for k in df1[df1[0] == j[0]][1]:
            num_1.append(k)
        name_1.append(j[0])
        nums_1.append(sum(num_1))
    print(i, name_1, nums_1)


def people_scenes():
    """
    每季人物出现时间
    """
    # 参数数据
    attr = ['提利昂', '雪诺', '龙妈', '三傻', '瑟曦', '二丫', '詹姆', '莫尔蒙', '戴佛斯', '山姆', '瓦里斯', '席恩', '布蕾妮', '布兰', '猎狗']
    v1 = [4903, 5323, 4900, 3608, 4252, 3655, 2523, 3650, 0, 1918, 2949, 3270, 0, 3115, 2442]
    v2 = [5257, 2658, 3037, 2455, 3021, 3373, 1363, 1694, 1879, 1225, 1594, 2908, 1869, 1387, 1445]
    v3 = [4146, 2620, 2760, 2369, 2429, 2612, 2674, 2561, 1636, 2074, 1533, 1605, 2009, 1768, 1283]
    v4 = [5480, 3818, 2490, 3130, 4694, 2510, 4269, 1634, 1021, 2273, 1332, 1190, 1536, 1427, 2328]
    v5 = [4469, 5066, 3767, 2919, 3927, 2770, 1889, 2998, 1452, 2742, 876, 1635, 1163, 0, 0]
    v6 = [2852, 5527, 2473, 3848, 2222, 2294, 2948, 827, 4101, 1268, 1424, 1626, 1749, 2107, 906]
    v7 = [5849, 7840, 5773, 3436, 3426, 2744, 4074, 4549, 4417, 1747, 3072, 2553, 2313, 1246, 3657]
    v8 = [8148, 7513, 6494, 3940, 1551, 4357, 3935, 1740, 3679, 2871, 3247, 888, 3817, 3296, 1827]
    # 创建条形图
    bar = Bar("权游人物出场时间分布", title_pos='center', title_top='18', width=800, height=400)
    bar.add("第一季", attr, v1, is_convert=True, xaxis_min=10, yaxis_label_textsize=12, is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=False, is_legend_show=True, label_pos='right', legend_orient='vertical', legend_pos='80%', legend_top='30%', is_yaxis_inverse=True, is_splitline_show=False, is_stack=True)
    bar.add("第二季", attr, v2, is_convert=True, xaxis_min=10, yaxis_label_textsize=12, is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=False, is_legend_show=True, label_pos='right', legend_orient='vertical', legend_pos='80%', legend_top='30%', is_yaxis_inverse=True, is_splitline_show=False, is_stack=True)
    bar.add("第三季", attr, v3, is_convert=True, xaxis_min=10, yaxis_label_textsize=12, is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=False, is_legend_show=True, label_pos='right', legend_orient='vertical', legend_pos='80%', legend_top='30%', is_yaxis_inverse=True, is_splitline_show=False, is_stack=True)
    bar.add("第四季", attr, v4, is_convert=True, xaxis_min=10, yaxis_label_textsize=12, is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=False, is_legend_show=True, label_pos='right', legend_orient='vertical', legend_pos='80%', legend_top='30%', is_yaxis_inverse=True, is_splitline_show=False, is_stack=True)
    bar.add("第五季", attr, v5, is_convert=True, xaxis_min=10, yaxis_label_textsize=12, is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=False, is_legend_show=True, label_pos='right', legend_orient='vertical', legend_pos='80%', legend_top='30%', is_yaxis_inverse=True, is_splitline_show=False, is_stack=True)
    bar.add("第六季", attr, v6, is_convert=True, xaxis_min=10, yaxis_label_textsize=12, is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=False, is_legend_show=True, label_pos='right', legend_orient='vertical', legend_pos='80%', legend_top='30%', is_yaxis_inverse=True, is_splitline_show=False, is_stack=True)
    bar.add("第七季", attr, v7, is_convert=True, xaxis_min=10, yaxis_label_textsize=12, is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=False, is_legend_show=True, label_pos='right', legend_orient='vertical', legend_pos='80%', legend_top='30%', is_yaxis_inverse=True, is_splitline_show=False, is_stack=True)
    bar.add("第八季", attr, v8, is_convert=True, xaxis_min=10, yaxis_label_textsize=12, is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=False, is_legend_show=True, label_pos='right', legend_orient='vertical', legend_pos='80%', legend_top='30%', is_yaxis_inverse=True, is_splitline_show=False, is_stack=True)
    # 生成图表
    bar.render("权游人物出场时间分布.html")


people_scenes()
