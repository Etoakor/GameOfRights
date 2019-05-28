import json
from datetime import datetime

# 读取每集的出场信息
with open("episodes.json", 'r') as load_f:
    load_dict = json.load(load_f)
    episodes = load_dict["episodes"]

for episode in episodes:
    # 获取每集的片段信息
    for scene in episode["scenes"]:
        # 处理时间数据
        start = datetime.strptime(scene['sceneStart'], "%H:%M:%S")
        end = datetime.strptime(scene['sceneEnd'], "%H:%M:%S")
        # 国家
        with open('got_1.csv', 'a+') as f:
            f.write(scene['location'] + ',' + str((end - start).seconds) + ',' + str(episode["seasonNum"]) + ',' + str(episode["episodeNum"]) + '\n')
        # 城市
        if 'subLocation' in scene.keys():
            with open('got_2.csv', 'a+') as f:
                f.write(scene['subLocation'] + ',' + str((end - start).seconds) + ',' + str(episode["seasonNum"]) + ',' + str(episode["episodeNum"]) + '\n')
        # 人物
        for people in scene['characters']:
            with open('got_3.csv', 'a+') as f:
                f.write(people['name'] + ',' + str((end - start).seconds) + ',' + str(episode["seasonNum"]) + ',' + str(episode["episodeNum"]) + '\n')
