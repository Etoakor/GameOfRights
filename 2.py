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

# 排序
top15 = sorted(item.items(), key=lambda x: x[1], reverse=True)[:15]
for i in top15:
    print(i[1], i[0])