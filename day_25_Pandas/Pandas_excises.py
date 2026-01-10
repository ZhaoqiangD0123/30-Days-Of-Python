import pandas as pd

# 阅读hacker_news.csv文件并获取前五行
df = pd.read_csv(r"D:\DESKTOP\MyPythonStudy\30-Days-Of-Python\data\hacker_news.csv", encoding='utf-8')
# 获取标题列
print(df.columns)
# 获取行数、列数
print(df.shape)
# 获取前十行和最后十行
print(df.head(10))
print(df.tail(10))
# 获取第二行和第四行从第二列到第四列的数据
print(df.iloc[1:3,1:3])
# 获取主题为Python的行
df_python = df[df['title'].apply(lambda x:'python' in str(x).lower())]
print("--- Python相关的主题 ---")
print(df_python.head())
# # print(df_python.head())
# # 获取投票数超过200的所有行
df_200num_comment = df[df['num_comments']>200]
print(df_200num_comment)
# # 按投票数排序数据框
sorted_df = df.sort_values(by='num_points')
print("\n--- 按票数升序 ---")
print(sorted_df['num_points'])
# # 按投票数进行降序排序
N_sorted_df = df.sort_values(by='num_points',ascending=False)
print("\n--- 按票数降序 ---")
print(N_sorted_df['num_points'])
# # 过滤掉Python主题并按票数排序
df_no_python = df[df['title'].apply(lambda x:'python' not in str(x).lower())]
print(df_no_python.shape)
df_no_python_sort = df_no_python.sort_values(by='num_points')
print(df_no_python_sort['num_points'])

python_sorted = df_python.sort_values(by='num_points', ascending=False)
print("\n--- Python主题按热度排序 ---")
print(python_sorted)
