================================================================================
              《年轮》版权之争 - 跨平台舆情数据说明文档
                        2026-05-29 爬取
================================================================================

【项目背景】
  汪苏泷 vs 张碧晨关于歌曲《年轮》的"原唱"与"版权"之争（2025年7月爆发）。
  本数据集覆盖5个平台，用于分析不同平台舆论态度差异。

================================================================================
                         一、文件清单
================================================================================

文件名                      行数      平台      数据类型
---------------------------------------------------------------------------
bilibili_cases.csv           36      B站       视频 + 热评（15列）
douyin_cases.csv             27      抖音       视频 + 热评（11列）
douban_all_comments.csv     867      豆瓣       帖子评论（13列）
zhihu_cases.csv              30      知乎       回答摘要（8列）
zhihu_all_comments.csv     1891      知乎       回答评论（8列）
qqmusic_comments.csv        492      QQ音乐     歌曲评论（7列）
platform_cases.csv          104      跨平台汇总  精选案例（17列）

================================================================================
                      二、各文件字段说明
================================================================================

1. bilibili_cases.csv（B站视频）
   platform        - 平台标识，固定"B站"
   video_title     - 视频标题
   up_author       - UP主名称
   play_count      - 播放量
   danmu_count     - 弹幕数
   reply_count     - 评论数
   publish_time    - 发布时间
   hot_comment_1~5 - 热门评论（格式：用户名: 评论内容 (点赞数赞)）
   crawl_time      - 爬取时间

2. douyin_cases.csv（抖音视频）
   platform        - 平台标识，固定"抖音"
   video_title     - 视频标题/文案
   author          - 作者昵称
   estimated_like  - 点赞数
   publish_date    - 发布日期
   hot_comment_1~5 - 热门评论
   crawl_time      - 爬取时间

3. douban_all_comments.csv（豆瓣评论）
   platform          - 平台标识，固定"豆瓣"
   source_post_id    - 来源帖子ID
   source_post_url   - 帖子链接
   post_title        - 帖子标题
   post_author       - 发帖人
   post_time         - 发帖时间
   post_content_summary - 帖子摘要
   post_like_count   - 帖子点赞
   post_collect_count- 帖子收藏
   comment_user      - 评论用户
   comment_time      - 评论时间
   comment_text      - 评论内容
   crawl_time        - 爬取时间

4. zhihu_cases.csv（知乎回答摘要）
   platform        - 平台标识，固定"知乎"
   question_title  - 问题标题
   answer_author   - 回答者
   upvote_count    - 赞同数
   comment_count   - 评论数
   publish_date    - 回答日期
   answer_summary  - 回答内容摘要（核心观点）
   stance          - 立场标注（待填充）
   crawl_time      - 爬取时间

5. zhihu_all_comments.csv（知乎评论）
   platform        - 平台标识
   answer_id       - 所属回答ID（可关联zhihu_cases）
   question_title  - 问题标题（部分为空）
   comment_user    - 评论用户
   comment_text    - 评论内容
   comment_likes   - 评论点赞
   comment_time    - 评论时间
   crawl_time      - 爬取时间

6. qqmusic_comments.csv（QQ音乐评论区）
   platform        - 平台标识，固定"QQ音乐"
   song_version    - 歌曲版本："张碧晨版" 或 "汪苏泷版"
   comment_user    - 评论用户
   comment_text    - 评论内容
   comment_likes   - 点赞数（API限制，多为0）
   comment_time    - 评论时间
   crawl_time      - 爬取时间

7. platform_cases.csv（跨平台汇总）
   platform        - 平台（B站/抖音/豆瓣/知乎/QQ音乐）
   video_title     - 标题
   author          - 作者/UP主
   play_count      - 播放量（B站）
   like_count      - 点赞数（抖音/知乎）
   reply_count     - 评论数
   danmu_count     - 弹幕数（B站）
   publish_date    - 发布日期
   video_type      - 内容类型（待标注）
   stance          - 立场（待标注：偏汪/偏张/中立）
   main_viewpoint  - 主要观点（待标注）
   hot_comment_1~5 - 热门评论
   crawl_time      - 爬取时间

================================================================================
                      三、数据特点与注意事项
================================================================================

1. 时间范围：2025-07-25（事件爆发）至 2026-05-29（爬取日）
2. 立场分布（粗略）：
   - B站：偏汪为主，法律/科普类视频占优
   - 抖音：偏汪略多，但分裂明显
   - 豆瓣：偏张为主（鹅组等女性用户多）
   - 知乎：双方均有高赞回答，法律分析较多
   - QQ音乐：两版评论区均有粉丝互撕，立场分明
3. 热评来源：
   - B站：通过官方API抓取
   - 抖音：通过页面滚动提取
   - 豆瓣/知乎：通过API批量抓取
   - QQ音乐：通过JSONP接口抓取
4. 部分字段（video_type、stance、main_viewpoint）留空，需后续标注
5. 豆瓣11个帖子的URL见 douban_all_comments.csv 的 source_post_url 列

================================================================================
                      四、关键发现摘要
================================================================================

- 舆论共识：汪苏泷拥有著作权无争议，争议核心是"唯一原唱 vs 双原唱"
- B站深度分析多，知乎法律讨论多，豆瓣/QQ音乐情绪化争论多
- 高频热词：杜鹃、偷原唱、永久演唱权、花千骨、房子住久了忘了房东是谁
- 事件时间线：旺仔小乔2021年言论 → 2025年7月引爆 → 汪收回版权 → 张告别

================================================================================
                      五、数据使用建议
================================================================================

1. 情感分析：douban_all_comments + zhihu_all_comments + qqmusic_comments
2. 立场对比：platform_cases.csv（标注stance后使用）
3. 时间趋势：按publish_date/publish_time排序分析舆论演变
4. 平台差异：对比各平台热评关键词和观点倾向
5. 如需原始HTML/JSON数据，联系数据爬取者
================================================================================
