# update_texts.py 使用说明

## 文件准备
1. 确保已安装 Python 和 pandas 库（未安装可执行 `pip install pandas`）。
2. 将以下三个文件放入**同一个文件夹**内：
   - `update_texts.py`（脚本文件）
   - `weibo_comments_clean.csv`（更新来源）
   - `all_weibo_texts_clean.csv`（待更新目标）

## 运行方法
在存放上述三个文件的文件夹中打开终端（命令提示符/PowerShell），执行：
```bash
python update_texts.py