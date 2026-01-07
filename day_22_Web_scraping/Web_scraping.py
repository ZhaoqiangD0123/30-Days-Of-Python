import requests
from bs4 import BeautifulSoup

# 1. 伪装成浏览器 (维基百科必做！)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("❌ 无法访问页面")
    exit()

soup = BeautifulSoup(response.content, 'html.parser')

# 2. 锁定那个特定的表格
# 虽然它有很多 class ('wikitable sortable...'), 我们只要匹配最独特的 'wikitable' 就能找到它
table = soup.find('table', class_='wikitable')

# 3. 获取所有行 (tr)
rows = table.find_all('tr')

print(f"{'总统姓名':<25} | {'生卒年份'}")
print("-" * 50)

# 4. 遍历每一行
# 使用 [1:] 跳过第一行表头
for row in rows[1:]:
    # --- 提取名字 (利用你发现的 class="fn") ---
    # 逻辑：在这一行里，找 class 为 "fn" 的 span
    name_tag = row.find('span', class_='fn')

    # --- 提取日期 (利用你发现的 style) ---
    # 逻辑：在这一行里，找 style 为 "font-size: 85%;" 的 span
    # 注意：使用 attrs 参数来匹配 style
    date_tag = row.find('span', attrs={'style': 'font-size: 85%;'})

    # --- 防御性编程 (防止报错) ---
    # 只有当名字存在时，才说明这一行是有效数据
    if name_tag:
        name_text = name_tag.get_text()

        # 如果找到了日期标签，就取文字；没找到就留空
        if date_tag:
            date_text = date_tag.get_text()
        else:
            date_text = "未知/在世"

        print(f"{name_text:<25} | {date_text}")