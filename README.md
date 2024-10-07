# 中文诗歌总集

  互联网发达的时代，我们依然很难找到一个非常系统、完善、高质量的诗词数据集合。
  
  思考了很长时间，决定创建《诗歌总集》这个github repo。借助收集的数据，以及LLM（大语言模型）的能力从下面几个维度去不断完善这个项目。
  
- [ ] 收录：收录所有中文诗词
- [ ] 校正：内容来源于网络，矫正诗词内容
- [ ] 鉴赏：鉴赏、翻译、考究诗词的创作背景
- [ ] 评分：从不同角度对诗词进行评分评级（文学的好坏既是客观的也是主观的，量化的评分是困难的，但是为了让好的诗词再数十万首诗词中进入到大家的视线，数值化是一个最高效的方式之一）


# 数据格式

每一首诗词标准化为如下的json格式
```json
{
    "id": "全局唯一标识，title+author+content的hash id",
    "title": "标题/词牌",
    "content": "内容",
    "author": "作者",
    "form": "文学体裁，诗、词、曲",
    "dynasty": "创作朝代、时期 - optional",
    "year": "创作年代 - optional",
    "volume": "收录诗集或者著作名称 - optional",
    "introduction": "作品说明 - optional",
    "translation": "现在简体中文翻译 - optional",
    "metadata": {
        "ai_score": "AI视角的分数",
        "human_score": "人的视角分数",
        "popularity": "流行度",
        "words_count": "作品字数",
        "sentence_count": "作品句子数",
        "vector": "向量化"
    }
}
```



