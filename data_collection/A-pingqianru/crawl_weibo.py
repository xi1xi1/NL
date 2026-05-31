import random
import re
import time
from datetime import datetime
from urllib.parse import quote, unquote

import pandas as pd
import requests
from bs4 import BeautifulSoup

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0",
    "Cookie": "XSRF-TOKEN=LHBcu6DFa4a3usakVcB2gasb; PC_TOKEN=85eb7df640; SCF=ApM6m8JVnRPBk4HBak7OWVuVpEqb-dPzz9qn07ObTv0wISny_uUKr5rKxHokbdtUKd8NTZ40KJ1GqEN_-W2gHwA.; SUB=_2A25HHU-pDeRhGeFG71QT-SfEyj6IHXVkU81hrDV8PUNbmtAYLXPskW9NeWWrr2RWPe1iI7lQ44-nLIFPEJQBpGv8; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWuceBxZYDKXA_16lD_TAJ15JpX5KzhUgL.FoMRShqE1K.ReKz2dJLoIXWki--ciKL8iKLhi--RiKyhi-zci--fi-z7iK.pi--fiKnci-z7i--Xi-iWiK.Xi--fiKnRiKnci--Ni-z0iK.c; ALF=02_1782631673; WBPSESS=5YbI5mYNhPWsX1nuUxy76hsJqLD9PURNlEHhLkeXZFjFRcg99V6w6pyCLEKVwTEPfgTzGq6kvu7VkthD0yWalT67jH8RzHN9wpwgFxwgOOzO1dfxFy2_zFwsVi78NRVVFOskc32EX-t62b7CyZTXFA=="
}

# 关键词及爬取页数
# 核心争议：8~12 页（强化张碧晨/汪苏泷/原唱之争舆论）
# 旺仔小乔相关：仅 3 页（控制占比）
KEYWORD_PAGES = {
    "张碧晨 年轮": 12,
    "汪苏泷 年轮": 12,
    "年轮 原唱": 12,
    "年轮原唱之争": 12,
    "年轮 版权": 10,
    "唯一原唱": 10,
    "双原唱": 10,
    "张碧晨告别年轮": 10,
    "汪苏泷收回年轮授权": 10,
    "旺仔小乔 年轮": 3,
    "旺仔小乔 张碧晨": 3,
    "旺仔小乔 汪苏泷": 3,
    "旺仔小乔 原唱": 3,
}

MEDIA_KEYWORDS = (
    "娱乐", "新闻", "日报", "晚报", "视频", "热点", "传媒",
    "周刊", "观察", "资讯", "电视", "广播", "门户", "财经",
)
OFFICIAL_KEYWORDS = ("studio", "工作室", "官微", "官方")
MAX_RETRIES = 2

OUTPUT_COLUMNS = [
    "post_id", "url", "keyword", "publish_time", "author_name",
    "author_type", "text", "repost_count", "comment_count",
    "like_count", "topic_tag", "crawl_time",
]


def parse_count(node):
    if not node:
        return 0
    text = node.get_text(" ", strip=True).replace(",", "")
    match = re.search(r"(\d+)", text)
    return int(match.group(1)) if match else 0


def guess_author_type(author_name):
    name_lower = author_name.lower()
    if any(keyword in name_lower for keyword in OFFICIAL_KEYWORDS):
        return "官方/工作室"
    if any(keyword in author_name for keyword in MEDIA_KEYWORDS):
        return "媒体"
    return "普通用户"


def extract_topic_tags(content):
    tags = []
    if not content:
        return tags

    for link in content.find_all("a", href=True):
        href = link["href"]
        if href.startswith("/weibo?q=%23") or "q=%23" in href:
            tag = unquote(href.split("q=")[-1]).strip("#")
            if tag and tag not in tags:
                tags.append(tag)
    return tags


def parse_card(card, keyword, crawl_time):
    if card.get("action-type") != "feed_list_item":
        return None

    post_id = card.get("mid")
    if not post_id:
        return None

    name_link = card.find("a", class_="name")
    author_name = ""
    if name_link:
        author_name = name_link.get("nick-name") or name_link.get_text(strip=True)

    from_div = card.find("div", class_="from")
    time_link = from_div.find("a", target="_blank") if from_div else None
    publish_time = time_link.get_text(strip=True) if time_link else ""

    url = time_link.get("href", "") if time_link else ""
    if url.startswith("//"):
        url = "https:" + url

    content = (
        card.find("p", attrs={"node-type": "feed_list_content_full"})
        or card.find("p", attrs={"node-type": "feed_list_content"})
    )
    text = content.get_text(" ", strip=True) if content else ""
    if len(text) < 10:
        return None

    return {
        "post_id": post_id,
        "url": url,
        "keyword": keyword,
        "publish_time": publish_time,
        "author_name": author_name,
        "author_type": guess_author_type(author_name),
        "text": text,
        "repost_count": parse_count(
            card.find("a", attrs={"action-type": "feed_list_forward"})
        ),
        "comment_count": parse_count(
            card.find("a", attrs={"action-type": "feed_list_comment"})
        ),
        "like_count": parse_count(card.find("span", class_="woo-like-count")),
        "topic_tag": ";".join(extract_topic_tags(content)),
        "crawl_time": crawl_time,
    }


def fetch_page(url):
    last_error = None
    for attempt in range(MAX_RETRIES + 1):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response
        except Exception as e:
            last_error = e
            if attempt < MAX_RETRIES:
                wait = random.uniform(1, 3)
                print(f"  请求失败，{wait:.1f} 秒后重试（{attempt + 1}/{MAX_RETRIES}）：{e}")
                time.sleep(wait)
    raise last_error


def crawl_keyword(keyword, max_pages, seen_post_ids, data):
    keyword_new_count = 0
    print(f"\n正在搜索：{keyword}（共 {max_pages} 页）")

    for page in range(1, max_pages + 1):
        url = f"https://s.weibo.com/weibo?q={quote(keyword)}&page={page}"
        crawl_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            response = fetch_page(url)
            soup = BeautifulSoup(response.text, "lxml")
            cards = soup.find_all("div", class_="card-wrap")
            page_count = 0

            print(f"  第 {page} 页找到 {len(cards)} 个卡片")

            for card in cards:
                post = parse_card(card, keyword, crawl_time)
                if not post:
                    continue
                if post["post_id"] in seen_post_ids:
                    continue

                seen_post_ids.add(post["post_id"])
                data.append(post)
                page_count += 1
                keyword_new_count += 1

            print(f"  第 {page} 页新增 {page_count} 条主帖，累计 {len(data)} 条")
            time.sleep(random.uniform(1, 3))

        except Exception as e:
            print(f"  第 {page} 页最终失败：{e}")

    print(f"关键词「{keyword}」完成：新增 {keyword_new_count} 条，当前累计 {len(data)} 条")
    return keyword_new_count


def main():
    data = []
    seen_post_ids = set()

    for keyword, max_pages in KEYWORD_PAGES.items():
        crawl_keyword(keyword, max_pages, seen_post_ids, data)

    df = pd.DataFrame(data, columns=OUTPUT_COLUMNS)
    df.to_csv("weibo_posts.csv", index=False, encoding="utf-8-sig")

    print("\n完成！")
    print(f"共获取 {len(df)} 条微博主帖，已保存至 weibo_posts.csv")


if __name__ == "__main__":
    main()
