# 中文《诗歌总集》

  互联网发达的时代，我们依然很难找到一个非常系统、完善、高质量的诗词数据集合。
  
  思考了很长时间，决定创建《诗歌总集》这个github repo。借助收集的数据，以及LLM（大语言模型）的能力从下面几个维度去不断完善这个项目。
  
- [ ] 收录：收录所有中文诗词
- [ ] 校正：内容来源于网络，矫正诗词内容*
- [ ] 鉴赏：鉴赏、翻译、考究诗词的创作背景
- [ ] 评分：从不同角度对诗词进行评分评级*


*诗词中存在很多字已经不在使用、甚至在电脑上没有可用的编码表示，这一类问题的处理是比较费时的

*文学的好坏既是客观的也是主观的，量化的评分是困难的，但是为了让好的诗词在数十万首诗词中更容易地进入到大家的视线，数值化是一个最高效的方式之一


# 数据格式

每一首诗词统一建模，标准化为如下的json格式，所有内容使用将简体中文
```json
{
    "id": "全局唯一标识，title+author+content的hash id",
    "title": "标题/词牌",
    "content": "内容",
    "author": "作者",
    "form": "文学体裁，诗、词、曲- optional",
    "dynasty": "创作朝代、时期 - optional",
    "year": "创作年代 - optional",
    "volume": "收录诗集或者著作名称 - optional",
    "introduction": "作品说明 - optional",
    "traditional": {
        "title": "繁体标题- optional",
        "author": "繁体作者- optional",
        "content": "繁体内容- optional"
    },
    "translation": "现在简体中文翻译 - optional",
    "metadata": {
        "ai_score": "AI视角的分数- optional",
        "human_score": "人的视角分数- optional",
        "popularity": "流行度- optional",
        "words_count": "作品字数- optional",
        "sentence_count": "作品句子数- optional",
        "vector": "向量化"
    }
}
```



