# 数据清洗最简运行说明

本 README 仅保留数据汇总、整理、清洗主流程，不包含 stance/frame/emotion 的后续修复脚本。

## 目标产物
运行完成后，得到以下结果文件：

- all_weibo_texts_clean.csv
- weibo_posts_clean.csv
- weibo_reposts_clean.csv
- weibo_comments_clean.csv
- platform_cases_clean.csv
- qqmusic_comments_clean.csv
- label_rules.xlsx
- data_cleaning_log.txt

## 运行环境

- Python 3.10+
- 建议依赖：pandas、openpyxl

可安装：

```powershell
pip install pandas openpyxl
```

## 数据路径说明

当前脚本内使用固定根路径：

- e:/大学/大二/大二下/数据可视化/大作业_传播学

请确保原始数据目录存在并与脚本一致，否则先修改各脚本顶部的 BASE 路径。

## 最简运行顺序（仅 6 个脚本）

按以下顺序执行：

1. run_data_cleaning_stage1.py  
   作用：初始化主表与子表，生成基础清洗结果和初始规则文件。

2. run_labeling_stage2.py  
   作用：执行文本清洗与第一轮规则标注，并同步到主表/子表。

3. run_labeling_stage3.py  
   作用：补充 event_stage、keyword_hit、QQ 评论标注，并更新规则统计。

4. run_stage3_timefix.py  
   作用：统一时间解析逻辑，修正 event_stage 并回写各表。

5. run_stage4_comments.py  
   作用：汇入微博评论数据，生成 weibo_comments_clean.csv，并追加到总表。

6. run_text_clean_reply_fix.py  
   作用：修复 回复@ 场景下的 text_clean，同步回主表和子表。

## 执行命令示例

在项目目录运行：

```powershell
python run_data_cleaning_stage1.py
python run_labeling_stage2.py
python run_labeling_stage3.py
python run_stage3_timefix.py
python run_stage4_comments.py
python run_text_clean_reply_fix.py
```

## 结果检查

重点检查：

- 8 个目标文件是否都已生成
- data_cleaning_log.txt 是否有对应阶段日志
- all_weibo_texts_clean.csv 与三张微博子表行数、关键字段是否一致

## 说明

本流程用于复现数据汇总、整理、清洗主线结果。
如需进一步优化 stance/frame/emotion，请在此基础上再运行单独的修复脚本。