import requests
from bs4 import BeautifulSoup
import csv  # 或者 import json


def scrape_website():
    # ==============================
    # 1. 配置区域 (Config)
    # ==============================
    target_url = 'https://example.com/data-page'

    # 必须加的伪装头 (假装自己是 Chrome 浏览器)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # ==============================
    # 2. 发送请求 (Request)
    # ==============================
    try:
        print(f"📡 正在请求: {target_url} ...")
        response = requests.get(target_url, headers=headers, timeout=10)  # timeout 防止卡死

        # 检查 HTTP 状态码 (200 表示成功)
        response.raise_for_status()
        print("✅ 网页下载成功！")

    except requests.exceptions.RequestException as e:
        print(f"❌ 请求失败: {e}")
        return  # 如果下载失败，直接结束程序

    # ==============================
    # 3. 解析数据 (Parse)
    # ==============================
    soup = BeautifulSoup(response.content, 'html.parser')

    # --- 核心提取逻辑 (根据目标网页修改这里) ---
    # 假设我们要抓取一个列表，它们都在 <div class="item"> 里
    items = soup.find_all('div', class_='item')

    data_list = []  # 用于从循环里收集数据

    print(f"🔍 找到 {len(items)} 个目标元素，开始解析...")

    for item in items:
        # A. 提取标题 (防御性编程)
        title_tag = item.find('h2', class_='title')
        if title_tag:
            title = title_tag.get_text(strip=True)
        else:
            title = "未知标题"

        # B. 提取链接
        link_tag = item.find('a')
        if link_tag and 'href' in link_tag.attrs:
            # 自动拼接完整 URL (如果是相对路径 /wiki/...)
            link = "https://example.com" + link_tag['href']
        else:
            link = "无链接"

        # C. 存入字典
        entry = {
            'title': title,
            'link': link
        }
        data_list.append(entry)
        # 打印一下看看进度
        # print(f"抓取到: {title}")

    # ==============================
    # 4. 保存数据 (Save)
    # ==============================
    if data_list:
        filename = 'scraped_data.csv'
        try:
            # newline='' 是为了防止 CSV 多出空行
            with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.DictWriter(f, fieldnames=['title', 'link'])
                writer.writeheader()  # 写入表头
                writer.writerows(data_list)  # 写入数据
            print(f"💾 数据已成功保存至: {filename}")
        except Exception as e:
            print(f"❌ 保存文件失败: {e}")
    else:
        print("⚠️ 未找到任何数据，未保存文件。")


if __name__ == '__main__':
    scrape_website()