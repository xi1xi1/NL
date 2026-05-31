# 微博传播链采集摘要

- 生成时间：2026-05-31 15:45:37
- 数据模式：自动浏览器采集模式
- 读取微博主帖：905 条
- 筛选核心传播源微博：20 条
- 成功获得转发数据的微博：20 条
- 总共获得转发记录：2503 条
- 传播节点数量：2093
- 传播边数量：2503

## 采集失败微博
- 无记录。

## 高频转发节点
- 吃烤肠的泡泡-ov-：18 次，类型 ordinary_user
- Silencewli：14 次，类型 ordinary_user
- 比喻体：6 次，类型 ordinary_user
- 随便泷：5 次，类型 ordinary_user
- 请快乐一直重播：5 次，类型 ordinary_user
- 是阿包喽-：5 次，类型 ordinary_user
- 三里屯大笨狗：5 次，类型 ordinary_user
- 小豆芝士卷koi：5 次，类型 legal_account
- wm_engya：5 次，类型 ordinary_user
- 蛋黄果味的大西瓜：5 次，类型 ordinary_user

## 账号类型参与数量
- ordinary_user：1563
- legal_account：229
- music_account：194
- marketing：54
- media：37
- fan_account：16

## 输出文件说明
- output/top_source_posts.csv：按传播得分筛出的核心微博主帖。
- output/weibo_reposts_raw.csv：自动采集或手动导入后的原始转发记录。
- output/weibo_reposts_clean.csv：清洗后的转发记录，包含 parent_user 和 user_type。
- output/repost_edges.csv：传播边表，可导入 Gephi、Cytoscape、ECharts、D3。
- output/repost_nodes.csv：传播节点表，可与边表一起构建传播网络图。
- output/repost_chain_summary.md：本摘要。

## 后续可视化建议
- 传播网络图：使用 repost_edges.csv 的 source_user -> target_user 画有向图，用 repost_nodes.csv 给节点着色。
- 账号类型堆叠图：按 user_type 统计参与传播的账号类型。
- 高频节点排行：按 repost_count 展示关键扩散者。
- 传播链层级图：将 direct_repost 与 chain_repost 分开，观察原微博扩散和二次扩散。
- 时间序列图：用 repost_time 展示转发热度随时间变化。