import os
import shutil
import pandas as pd
import json

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



#解析字符串
df["genres"] = df["genres"].apply(lambda x: json.loads(x) if isinstance(x, str) else x)
Temp_list = [item["name"] for j in df["genres"] for item in j]
print(Temp_list)
