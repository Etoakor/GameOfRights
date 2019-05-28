import json

# 读取人物信息文件
with open("characters.json", 'r') as load_f:
    load_dict = json.load(load_f)
    characters = load_dict["characters"]

# 计算人物的杀人数
item = {}
for character in characters:
    if 'killed' in character.keys():
        item[character['characterName']] = len(character['killed'])

# 排序
top15 = sorted(item.items(), key=lambda x: x[1], reverse=True)[:15]
print(top15, '\n\n')

# 获取杀手榜前15位,以及是哪位被领盒饭
for i in top15:
    for character in characters:
        if character['characterName'] == i[0]:
            print(i[1], i[0], character['killed'], '\n\n')