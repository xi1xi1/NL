"""
微博爬虫 - 快速启动指南

步骤 1: 获取有效的 Cookie
  a) 打开浏览器（Chrome/Edge/Firefox）访问 https://weibo.com
  b) 登录你的微博账号
  c) 按 F12 打开开发者工具
  d) 进入 Application/Storage -> Cookies
  e) 找到 weibo.com 的 Cookie 列表
  f) 复制 "SUB" 的 value 值
  
步骤 2: 更新脚本中的 SUB 值
  打开 weibo_crawler.py，找到 COOKIES 配置，替换 SUB 值为你复制的值
  
步骤 3: 运行爬虫
  运行: D:/cv/python.exe weibo_crawler.py
"""

import re
import json

def extract_cookies_from_devtools():
    """
    从 Chrome DevTools 导出的 cookies.json 文件中解析
    """
    print(__doc__)
    
    # 提示用户导出cookies的方式
    print("\n如果已经用浏览器导出了 cookies.json，可以这样导入：")
    print("  1. 在 Chrome DevTools -> Storage -> Cookies -> weibo.com")
    print("  2. 右键 -> Copy all as cURL")
    print("  3. 粘贴到下方提取 SUB 值\n")

def manual_cookie_input():
    """手动输入SUB值"""
    print("=" * 60)
    print("微博爬虫 - Cookie 配置")
    print("=" * 60)
    print("\n请按照以下步骤获取 Cookie：")
    print("\n1️⃣  打开浏览器访问 https://weibo.com 并登录")
    print("2️⃣  按 F12 打开开发者工具")
    print("3️⃣  切换到 Application 标签")
    print("4️⃣  左侧选择 Cookies -> weibo.com")
    print("5️⃣  找到名为 'SUB' 的条目，复制其 Value 值")
    print("\n然后将下方的 SUB 值替换为你复制的值")
    print("=" * 60)

if __name__ == '__main__':
    manual_cookie_input()
