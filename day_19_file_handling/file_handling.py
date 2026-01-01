import os
import re
from collections import Counter
import json
# 文件清洗
file_name = r'obama_speech.txt'
if os.path.exists(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        raw_content = f.read()
        print(f'读取成功，文件清洗前字符长度为{len(raw_content)}')
    #    正则化处理html格式
    pattern = r'<[^>]+>'
    content = re.sub(pattern, '', raw_content)
    content = re.sub('&rsquo;', '\'', content)
    content = content.strip()

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"保存成功！文件已更新。文件清洗后字符长度为{len(content)}")
else:
    print('请输入正确的文件地址')


# 任务 1：行数与单词数统计
# 编写一个函数 count_lines_and_words(filename)。
#
# 读取文件。
#
# 统计文件一共有多少行。
#
# 统计文件一共有多少个单词（以空格分隔）。
#
# 返回一个字典：{'lines': 10, 'words': 150}。
def count_lines_and_words(filename):
    if not os.path.exists(filename):
        print('error path')
        return False
    line_word = {'lines': 0,
                 'words': 0}
    with open(filename, 'r',encoding='utf-8') as f:
        lines = f.readlines()
        print('read over')
    line_word['lines'] = len(lines)
    total_word = sum(len(re.sub(r'[^\w\s]', '', line).split()) for line in lines)
    line_word['words'] = total_word
    return line_word
# print(count_lines_and_words(file_name))
# 任务 2：高频词汇提取 (综合题)
# 结合 Day 11 (Counter)、Day 18 (re) 和今天的知识。 编写一个函数 find_most_common_words(filename, n)。
#
# 读取文件内容。
#
# 清洗数据：使用正则 re.sub 去掉标点符号，统一转为小写。
#
# 使用 Counter 统计单词出现的频率。
#
# 返回出现频率最高的 n 个单词。
def find_most_common_words(filename, n):
    if not os.path.exists(filename):
        print('error path')
        return False
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    # 清洗
    pattern = '[^\w\s]'
    clean_text = re.sub(pattern,'',text)
    word = clean_text.lower().split()
    count_word = Counter(word)
    return count_word.most_common(n)

# print(find_most_common_words(file_name,3))


# 任务 3：保存结果
# 把任务 2 的结果（前 n 个单词）写入到一个新文件 results.txt 中。 格式要求：
# word1: 50次
# word2: 40次
# ...
def save(filename, n):
    count_word = find_most_common_words(filename, n)
    with open('results.txt', 'w') as f:
        # for line in count_word:
        #     f.write(f"{line[0]}:{line[1]}\n")
        for word, count in count_word:
            f.write(f"{word}:{count}\n")
# save(file_name,3)


# 编写一个函数，该函数需要一个参数（文件名）并统计文件中单词的数量
# def count_lines_and_words(filename):

# 阅读obama_speech.txt文件并计算单词数
file_name = r'D:\DESKTOP\MyPythonStudy\30-Days-Of-Python\data\obama_speech.txt'
with open(file_name,'r',encoding='utf-8') as f:
    speech = f.readlines()
    for line in speech:
        print(line,end='')
print(f'total_word:{count_lines_and_words(file_name)}')

# 阅读michelle_obama_speech.txt文件并计算单词数

# 阅读donald_speech.txt文件并计算单词数
# 阅读melina_trump_speech.txt文件并计算单词数

# 使用以下数据集创建一个JSON文件：
python_libraries = [
{
    "库名称": "Django",
    "创建者": "Adrian Holovaty",
    "首次发布年份": 2005,
    "版本": "4.0.2",
    "用途": "Web开发",
    "描述": "Django让您可以快速构建更好的Web应用程序。"
},
{
    "库名称": "Flask",
    "创建者": "Armin Ronacher",
    "首次发布年份": 2010,
    "版本": "2.0.2",
    "用途": "Web开发",
    "描述": "Flask是一个轻量级的WSGI Web应用程序框架。"
},
{
    "库名称": "NumPy",
    "创建者": "Travis Oliphant",
    "首次发布年份": 2005,
    "版本": "1.22.0",
    "用途": "科学计算",
    "描述": "NumPy是Python中用于科学计算的基础包。"
},
{
    "库名称": "Pandas",
    "创建者": "Wes McKinney",
    "首次发布年份": 2008,
    "版本": "1.4.0",
    "用途": "数据分析",
    "描述": "pandas是一个用于数据分析和数据操作的开源库。"
},
{
    "库名称": "Matplotlib",
    "创建者": "John D. Hunter",
    "首次发布年份": 2003,
    "版本": "3.5.1",
    "用途": "数据可视化",
    "描述": "Matplotlib是一个用于在Python中创建静态、动画和交互式可视化的库。"
}
]

with open('python_libraries.json', 'w', encoding='utf-8') as f:
    json.dump(python_libraries, f, ensure_ascii=False, indent=4)

