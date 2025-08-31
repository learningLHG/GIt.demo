import os
import shutil
import pandas as pd
import json
import numpy as np


#第一步：数据提取

#下载路径
download_path = r"C:\Users\LHG\Desktop\aiofiles-24.1.0\tmdb_5000_movies.csv"
#当前目录文件路径的上一级
project_dir = os.path.dirname(__file__)
#所需要创建的地址以及名字
target_path = os.path.join(project_dir, "data", "Movie_dataset.csv")

#确保当前路径下文件可以创建,并创建父级文件夹
os.makedirs(os.path.dirname(target_path), exist_ok=True)

#csv文档复制过来
shutil.copy(download_path, target_path)
print(f"文件已复制到目录{target_path}")

#读取数据
df = pd.read_csv(target_path)

#所有信息
#print(df.head(5))
# print(df.info())
#print(df["genres"][0])



#第二步，创建数组
#将Genre拿出来
'''
原本df内容
#"[{""id"": 12, ""name"": ""Adventure""}, {""id"": 14, ""name"": ""Fantasy""}, {""id"": 10751, ""name"": ""Family""}]"
'''
#解析字符串
df_genres_serialization= df["genres"].apply(lambda x: json.loads(x) if isinstance(x, str) else x) #非常关键的序列化
#print(df["genres"])

df_genres_list = df_genres_serialization.apply(lambda x: [item["name"] for item in x])#脱去外衣
Temp_list = [i for i in df_genres_list]


#去重操作
Genres_list = list(set([i for j in Temp_list for i in j]))

zeros_list = pd.DataFrame(np.zeros((df.shape[0], len(Genres_list))), columns=Genres_list)


#给每部电影进行分类标注
for i in range(df.shape[0]):
    zeros_list.loc[i, Temp_list[i]] = 1

#统计每个分类电影数量
genres_count = zeros_list.sum(axis=0)
genres_count =genres_count.sort_values(ascending=True)


#第三步，画图
_x = genres_count.index
_y = genres_count.values

plt.figure(figsize=(20, 8), dpi=80)
plt.bar(range(len(_x)), _y)
plt.xticks(range(len(_x)),_x)
plt.show()



