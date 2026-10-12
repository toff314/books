# 第 23 章 情感、态度与内涵词表

### 章

> CHAPTER

# 23 情感、态度与内涵词表

> 23 Lexicons for Sentiment, Affect, and Connotation

总有一天，我们将能够度量词语的力量

> Some day we’ll be able to measure the power of words
本章转向用于解读情感含义的工具，延续我们

> In this chapter we turn to tools for interpreting affective meaning, extending our

> Maya Angelou

> `affective`（情感的）
>
> 释义：本书沿用情感计算的传统，用它统称情绪、情感、人格、心境与态度等与感受相关的意义。

在附录 B 中对情感分析的研究。我们沿用情感计算（Picard, 1995）的传统使用“情感的”一词，用以表示情绪、情感、人格、心境和态度。情感含义与主观性密切相关，

> study of sentiment analysis in Appendix B. We use the word ‘affective’, following the tradition in affective computing (Picard, 1995) to mean emotion, sentiment, personality, mood, and attitudes. Affective meaning is closely related to subjectivity,

> `subjectivity`（主观性）
>
> 释义：指对说话人或作者所表达的评价、意见、情绪和推测等内容的研究。

即对说话人或作者的评价、意见、情绪和推测的研究（Wiebe 等，1999）。

> the study of a speaker or writer’s evaluations, opinions, emotions, and speculations(Wiebe et al., 1999).

情感含义应当如何定义？一种颇具影响力的情感状态类型学来自 Scherer（2000），他依据认知实现方式和时间进程等因素来定义每一类情感状态（图 23.1）。

> How should affective meaning be defined? One influential typology of affective states comes from Scherer (2000), who defines each class of affective states by factors like its cognitive realization and time course (Fig. 23.1).

![](images/23-lexicons-sentiment/fig_p1_0.png)

*图 23.1 Scherer 的情感状态类型学（Scherer, 2000）。*
*Figure 23.1 The Scherer typology of affective states (Scherer, 2000).*

我们可以为这些类型的情感状态分别设计抽取器。附录 B

> We can design extractors for each of these kinds of affective states. Appendix B
已经介绍了情感分析，即抽取作者在文本中所表达的正面或负面倾向的任务。在 Scherer 的类型学中，这对应于态度的抽取：从充满情感的文本（如书籍或电影的消费者评论、报纸社论，或博客与推文中的公众情绪）中判断人们喜欢或不喜欢什么。

> already introduced sentiment analysis, the task of extracting the positive or negative orientation that a writer expresses in a text. This corresponds in Scherer’s typology to the extraction of attitudes: figuring out what people like or dislike, from affectrich texts like consumer reviews of books or movies, newspaper editorials, or public sentiment in blogs or tweets.

检测情绪与心境有助于判断：学生在与辅导系统交互时是困惑、投入还是确信，求助热线的来电者是否感到挫败，某人的博客文章或推文是否显示出抑郁。例如，检测小说中恐惧之类的情绪，可以帮助我们追踪哪些群体或情境令人恐惧，以及这种恐惧如何随时间变化。

> Detecting emotion and moods is useful for detecting whether a student is confused, engaged, or certain when interacting with a tutorial system, whether a caller to a help line is frustrated, whether someone’s blog posts or tweets indicated depression. Detecting emotions like fear in novels, for example, could help us trace what groups or situations are feared and how that changes over time.

在从人与人之间的对话中抽取信息时，检测不同的人际立场会很有用。这里的目标是检测访谈或友好交谈中的友好、尴尬之类的立场，例如用于会议摘要，或找出对话中人们特别兴奋或投入的部分——即有助于会议摘要的对话热点。检测用户的个性——例如用户是否外向，或者他们在多大程度上乐于接受新经验——有助于改进会话代理，若会话代理与用户对个性的预期相匹配，其表现似乎更好（Mairesse 与 Walker, 2008）。而态度不仅对识别重要，对生成也很重要；合成态度对多个领域的会话代理都很重要，包括儿童故事书之类的读写辅导系统，以及电脑游戏。

> Detecting different interpersonal stances can be useful when extracting information from human-human conversations. The goal here is to detect stances like friendliness or awkwardness in interviews or friendly conversations, for example for summarizing meetings or finding parts of a conversation where people are especially excited or engaged, conversational hot spots that can help in meeting summarization. Detecting the personality of a user—such as whether the user is an extrovert or the extent to which they are open to experience— can help improve conversational agents, which seem to work better if they match users’ personality expectations (Mairesse and Walker, 2008). And affect is important for generation as well as recognition; synthesizing affect is important for conversational agents in various domains, including literacy tutors such as children’s storybooks, or computer games.

在附录 B 中，我们介绍了使用朴素贝叶斯分类来对

> In Appendix B we introduced the use of naive Bayes classification to classify a
文档的情感进行分类。多种分类器已成功应用于其中许多任务，它们把训练集中的所有词作为分类器的输入，再由分类器判定文本的态度状态。

> document’s sentiment. Various classifiers have been successfully applied to many of these tasks, using all the words in the training set as input to a classifier which then determines the affect status of the text.

本章关注另一种模型，其中并不把每个

> In this chapter we focus on an alternative model, in which instead of using every
词都用作特征，而是只关注某些词，即那些携带特别强烈的态度或情感线索的词。我们把这类词表称为态度词表（affective lexicons）或情感词表（sentiment lexicons）。这些词表预设了语义学上的一个事实：词具有情感含义或内涵。“内涵”一词在不同领域有不同含义

> word as a feature, we focus only on certain words, ones that carry particularly strong cues to affect or sentiment. We call these lists of words affective lexicons or sentiment lexicons. These lexicons presuppose a fact about semantics: that words have affective meanings or connotations. The word connotation has different meanings

> `connotations`（内涵）
>
> 释义：指词义中与作者或读者的情绪、情感、意见或评价相关的那些方面。

但在本书中，我们用它指词义中与作者或读者的情绪、情感、意见或评价相关的那些方面。除了有助于判定文本的态度状态外，内涵词表还可以作为其他类型情感任务以及计算社会科学分析的有用特征。

> in different fields, but here we use it to mean the aspects of a word’s meaning that are related to a writer or reader’s emotions, sentiment, opinions, or evaluations. In addition to their ability to help determine the affective status of a text, connotation lexicons can be useful features for other kinds of affective tasks, and for computational social science analysis.

在接下来的一节中，我们介绍情绪的基本理论，说明情感

> In the next sections we introduce basic theories of emotion, show how sentiment
词表如何是情绪词表的一个特例，并提及一些有用的词表。

> lexicons are a special case of emotion lexicons, and mention some useful lexicons.

随后我们综述构建词表的三种方式：人工标注、半监督和有监督。最后，我们讨论如何检测针对某一特定实体的态度，并介绍内涵框架。

> We then survey three ways for building lexicons: human labeling, semi-supervised, and supervised. Finally, we talk about how to detect affect toward a particular entity, and introduce connotation frames.

## 23.1 定义情绪

> 23.1 Defining Emotion

最重要的态度类别之一是情绪，Scherer（2000）将

> One of the most important affective classes is emotion, which Scherer (2000) defines

> `emotion`（情绪）
>
> 释义：指对被视为具有重大意义的内外事件作出评价后产生的相对短暂的应答。

其定义为“对内外事件被评价为具有重大意义时相对短暂的应答片段”。

> as a “relatively brief episode of response to the evaluation of an external or internal event as being of major significance”.

情绪检测有可能改进许多语言处理

> Detecting emotion has the potential to improve a number of language processing
任务。情绪识别可以帮助辅导系统之类的对话系统检测出学生不高兴、无聊、犹豫、自信等状态。自动检测评论或客户回复中的情绪（愤怒、不满、信任），可以帮助企业识别出具体的问题环节或表现良好的环节。

> tasks. Emotion recognition could help dialogue systems like tutoring systems detect that a student was unhappy, bored, hesitant, confident, and so on. Automatically detecting emotions in reviews or customer responses (anger, dissatisfaction, trust) could help businesses recognize specific problem areas or ones that are going well.

情绪在医学自然语言处理任务中也能发挥作用，例如辅助诊断抑郁或自杀意图。检测小说中针对人物表达的情绪，或许有助于理解不同社会群体在不同时期如何被社会看待。

> Emotion can play a role in medical NLP tasks like helping diagnose depression or suicidal intent. Detecting emotions expressed toward characters in novels might play a role in understanding how different social groups were viewed by society at different times.

自然语言处理中的情绪计算模型主要基于两族情绪理论（这只是情感科学领域中研究的众多理论中的两族）。

> Computational models of emotion in NLP have mainly been based on two families of theories of emotion (out of the many studied in the field of affective science).

在其中一族中，情绪被视为固定的原子单元，数量有限，其他情绪由它们生成，通常称为基本情绪（Tomkins 1962；Plutchik 1962），这一模型可追溯到 Darwin。这一族理论中最著名的或许是 Ekman 提出的 6 种在所有文化中普遍存在的情绪（例如 Ekman 1999）：惊讶、快乐、愤怒、恐惧、厌恶、悲伤。另一种原子论是 Plutchik（1980）的情绪轮，由四对相对的基本情绪共 8 种构成：喜悦—悲伤、愤怒—恐惧、信任—厌恶、期待—惊讶，再加上由它们派生的情绪，如图 23.2 所示。

> In one of these families, emotions are viewed as fixed atomic units, limited in number, and from which others are generated, often called basic emotions (Tomkins 1962, Plutchik 1962), a model dating back to Darwin. Perhaps the most well-known of this family of theories are the 6 emotions proposed by Ekman (e.g., Ekman 1999) to be universally present in all cultures: surprise, happiness, anger, fear, disgust, sadness. Another atomic theory is the Plutchik (1980) wheel of emotion, consisting of 8 basic emotions in four opposing pairs: joy–sadness, anger–fear, trust–disgust, and anticipation–surprise, together with the emotions derived from them, shown in Fig. 23.2.

![](images/23-lexicons-sentiment/fig_p3_0.png)

*图 23.2 Plutchik 情绪轮。*
*Figure 23.2 Plutchik wheel of emotion.*

自然语言处理中广泛使用的第二类情绪理论把情绪视为一个

> The second class of emotion theories widely used in NLP views emotion as a
2 维或 3 维空间（Russell, 1980）。大多数模型包含效价和唤醒度这两个维度，许多模型还加上第三个维度——支配度。它们的定义如下：

> space in 2 or 3 dimensions (Russell, 1980). Most models include the two dimensions valence and arousal, and many add a third, dominance. These can be defined as:

效价：刺激的愉悦程度；唤醒度：刺激所引发的警觉、活跃或精力水平；支配度：刺激或

> valence: the pleasantness of the stimulus arousal: the level of alertness, activeness, or energy provoked by the stimulus dominance: the degree of control or dominance exerted by the stimulus or the
情绪所施加的控制或支配程度

> emotion
可以把情感视为第二种观点（把情绪看作空间中的点）的一个特例。特别是，衡量一个词有多愉悦或不愉悦的效价维度，常被直接用作情感的度量。

> Sentiment can be viewed as a special case of this second view of emotions as points in space. In particular, the valence dimension, measuring how pleasant or unpleasant a word is, is often used directly as a measure of sentiment.

在这类基于词表的态度模型中，一个词的情感含义通常是固定的，与使用该词的语言语境、说话者的方言或文化无关。相比之下，情感科学中的其他模型把情绪表示为涉及认知的丰富得多的过程（Barrett 等，2007）。例如在评价理论中，情绪是复杂的过程，其中人会考虑事件与其目标的一致程度，并顾及与该事件相关的能动性、确定性、紧迫性、新颖性和控制力等变量（Moors 等，2013）。考虑这些更丰富情绪理论的自然语言处理计算模型，很可能在未来工作中发挥重要作用。

> In these lexicon-based models of affect, the affective meaning of a word is generally fixed, irrespective of the linguistic context in which a word is used, or the dialect or culture of the speaker. By contrast, other models in affective science represent emotions as much richer processes involving cognition (Barrett et al., 2007). In appraisal theory, for example, emotions are complex processes, in which a person considers how an event is congruent with their goals, taking into account variables like the agency, certainty, urgency, novelty and control associated with the event(Moors et al., 2013). Computational models in NLP taking into account these richer theories of emotion will likely play an important role in future work.

## 23.2 可用的情感与态度词表

> 23.2 Available Sentiment and Affect Lexicons

已经创建并发布了各种各样的态度词表。最基本的词表沿着一个语义变异性维度为词进行标注，该维度通常称为「情感」（sentiment）或「效价」（valence）。

> A wide variety of affect lexicons have been created and released. The most basic lexicons label words along one dimension of semantic variability, generally called“sentiment” or “valence”.

在最简单的词表中，这一维度以二元方式表示，即

> In the simplest lexicons this dimension is represented in a binary fashion, with
一个正面词词表和一个负面词词表。最古老的是

> a wordlist for positive words and a wordlist for negative words. The oldest is the

> `General Inquirer`
>
> 释义：最早的态度词表之一（1966 年），含正面词 1915 个、负面词 2291 个，源自内容分析与认知心理学词义研究。

General Inquirer（Stone 等，1966），它借鉴了内容分析以及词语意义的认知心理学的早期

> General Inquirer (Stone et al., 1966), which drew on content analysis and on early
研究（Osgood 等，1957）。General Inquirer 有一个包含 1915 个正面词的词表和一个包含 2291 个负面词的词表（以及下文讨论的其他词表）。MPQA 主观性词表（Wilson 等，2005）含有 2718 个正面词和 4912 个负面词，取自先前的词表，另加一份通过自举（bootstrapping）得到的主观词与短语列表（Riloff 与 Wiebe，2003）。该词表中的每个条目都经过人工标注情感，同时也标注了信度（强主观或弱主观）。Hu 和 Liu（2004）的极性词表给出 2006 个正面词和 4783 个负面词，取自产品评论，并使用基于 WordNet 的自举（bootstrapping）方法进行标注。

> work in the cognitive psychology of word meaning (Osgood et al., 1957). The General Inquirer has a lexicon of 1915 positive words and a lexicon of 2291 negative words (as well as other lexicons discussed below). The MPQA Subjectivity lexicon(Wilson et al., 2005) has 2718 positive and 4912 negative words drawn from prior lexicons plus a bootstrapped list of subjective words and phrases (Riloff and Wiebe, 2003). Each entry in the lexicon is hand-labeled for sentiment and also labeled for reliability (strongly subjective or weakly subjective). The polarity lexicon of Hu and Liu (2004) gives 2006 positive and 4783 negative words, drawn from product reviews, labeled using a bootstrapping method from WordNet.

> 正面 钦佩、令人惊叹、保证、庆祝、魅力、渴望、热忱、卓越、精致、绝妙、嬉戏、优雅、快乐、喜悦、好运、威严、仁慈、美好、耐心、完美、自豪、欢欣、宽慰、尊重、令人满意、轰动、超棒、了不起、感谢、生动、明智、美妙、兴致
>
> *Positive admire, amazing, assure, celebration, charm, eager, enthusiastic, excellent, fancy, fantastic, frolic, graceful, happy, joy, luck, majesty, mercy, nice, patience, perfect, proud, rejoice, relief, respect, satisfactorily, sensational, super, terrific, thank, vivid, wise, wonderful, zest*

> 负面 可恶、愤怒、焦虑、糟糕、灾难、廉价、抱怨、居高临下、欺骗、
>
> *Negative abominable, anger, anxious, bad, catastrophe, cheap, complaint, condescending, deceit,*

> 有缺陷、失望、使尴尬、虚假、恐惧、肮脏、傻瓜、罪疚、憎恨、白痴、施加、懒惰、悲惨、哀悼、紧张、反对、害虫、阴谋、拒绝、尖叫、愚蠢、可怕、不友好、卑劣、邪恶
>
> *defective, disappointment, embarrass, fake, fear, filthy, fool, guilt, hate, idiot, inflict, lazy, miserable, mourn, nervous, objection, pest, plot, reject, scream, silly, terrible, unfriendly, vile, wicked*

*图 23.3 在 General Inquirer（Stone 等，1966）、MPQA 主观性词表（Wilson 等，2005）以及 Hu 和 Liu（2004）的极性词表中情感一致的若干词。*
*Figure 23.3 Some words with consistent sentiment across the General Inquirer (Stone et al., 1966), the MPQA Subjectivity lexicon (Wilson et al., 2005), and the polarity lexicon of Hu and Liu (2004).*

比这些情感词表稍微更一般化的，是这样一类词表：它们为每个

> Slightly more general than these sentiment lexicons are lexicons that assign each
词在全部三个情感维度上都赋予一个值。NRC 效价-唤醒度-支配度（VAD）词表（Mohammad, 2018a）为 20,000 个词赋予效价、唤醒度和支配度得分。图 23.4 给出了一些示例。

> word a value on all three affective dimensions. The NRC Valence, Arousal, and Dominance (VAD) lexicon (Mohammad, 2018a) assigns valence, arousal, and dominance scores to 20,000 words. Some examples are shown in Fig. 23.4.

> 效价 唤醒度 支配度
>
> *Valence Arousal Dominance*

> 度假 .840 暴怒 .962 强大 .991 令人愉快 .918 聚会 .840 权威 .935 哨声 .653 有条理 .337 萨克斯管 .482 安慰 .408 毫不费力 .120 气馁 .0090 折磨 .115 打盹 .046 软弱 .045
>
> *vacation .840 enraged .962 powerful .991 delightful .918 party .840 authority .935 whistle .653 organized .337 saxophone .482 consolation .408 effortless .120 discouraged .0090 torture .115 napping .046 weak .045*

*图 23.4 若干示例词在 Mohammad（2018a）的情感维度上的取值。*
*Figure 23.4 Values of sample words on the emotional dimensions of Mohammad (2018a).*

NRC 词-情绪关联词表，也称为 EmoLex（Mohammad and Turney, 2013），使用上文定义的 Plutchik（1980）8 种基本情绪。

> The NRC Word-Emotion Association Lexicon, also called EmoLex (Mohammad and Turney, 2013), uses the Plutchik (1980) 8 basic emotions defined above.

> `EmoLex`
>
> 释义：一种把词与 Plutchik 八种基本情绪及正负极性关联起来的词表，含约 14,000 个词，常用于情绪识别与情感分析。

该词表包含约 14,000 个词，既有来自先前词表的词，也包括高频名词、动词、副词和形容词。以下是一些示例词在该词表中的取值：

> The lexicon includes around 14,000 words including words from prior lexicons as well as frequent nouns, verbs, adverbs and adjectives. Values from the lexicon for some sample words:

| 词<br>Word | 愤怒<br>anger | 期待<br>anticipation | 厌恶<br>disgust | 恐惧<br>fear | 喜悦<br>joy | 悲伤<br>sadness | 惊讶<br>surprise | 信任<br>trust | 正面<br>positive | 负面<br>negative |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 奖励<br>reward | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 0 |
| 担忧<br>worry | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 温柔<br>tenderness | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 |
| 心上人<br>sweetheart | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 1 | 0 |
| 突然<br>suddenly | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| 口渴<br>thirst | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 |
| 垃圾<br>garbage | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |

奖励 0 1 0 0 1 0 1 1 1 0 担忧 0 1 0 1 0 1 0 0 0 1 温柔 0 0 0 0 1 0 0 0 1 0 心上人 0 1 0 0 1 1 0 1 1 0 突然 0 0 0 0 0 0 1 0 0 0 口渴 0 1 0 0 0 1 1 0 0 0 垃圾 0 0 1 0 0 0 0 0 0 1

> reward 0 1 0 0 1 0 1 1 1 0 worry 0 1 0 1 0 1 0 0 0 1 tenderness 0 0 0 0 1 0 0 0 1 0 sweetheart 0 1 0 0 1 1 0 1 1 0 suddenly 0 0 0 0 0 0 1 0 0 0 thirst 0 1 0 0 0 1 1 0 0 0 garbage 0 0 1 0 0 0 0 0 0 1
对于一组较小的 5,814 个词，NRC 情绪/态度强度词表

> For a smaller set of 5,814 words, the NRC Emotion/Affect Intensity Lexicon
（Mohammad, 2018b）包含针对愤怒、恐惧、喜悦和悲伤的实值关联得分；图 23.5 给出了一些示例。

> (Mohammad, 2018b) contains real-valued scores of association for anger, fear, joy, and sadness; Fig. 23.5 shows examples.

> 愤怒 恐惧 喜悦 悲伤
>
> *Anger Fear Joy Sadness*

> 暴怒 0.964 恐怖 0.923 极好 0.864 悲伤 0.844 暴力 0.742 痛苦 0.703 欢呼 0.773 罪疚 0.750 政变 0.578 瘟疫 0.625 彩虹 0.531 刻薄 0.547 驱逐 0.484 紧张 0.531 手势 0.387 困难 0.421 可疑 0.484 失败 0.531 温暖 0.391 乞丐 0.422 培育 0.059 自信 0.094 艰难 .031 歌唱 0.017
>
> *outraged 0.964 horror 0.923 superb 0.864 sad 0.844 violence 0.742 anguish 0.703 cheered 0.773 guilt 0.750 coup 0.578 pestilence 0.625 rainbow 0.531 unkind 0.547 oust 0.484 stressed 0.531 gesture 0.387 difficulties 0.421 suspicious 0.484 failing 0.531 warms 0.391 beggar 0.422 nurture 0.059 confident 0.094 hardship .031 sing 0.017*

*图 23.5 取自 Mohammad（2018b）的若干词在愤怒、恐惧、喜悦和悲伤上的情感强度示例。*
*Figure 23.5 Sample emotional intensities for words for anger, fear, joy, and sadness from Mohammad (2018b).*

LIWC，即语言探究与词计数（Linguistic Inquiry and Word Count），是一套被广泛使用的、包含 73 个词表、2300 多个词的词表集合（Pennebaker 等，2007），旨在捕捉与社会心理学任务相关的词汇意义方面。除了诸如负面情绪（bad、weird、hate、problem、tough）和正面情绪（love、nice、sweet）这类与情感相关的词表之外，LIWC 还包含愤怒、悲伤、认知机制、感知、尝试和抑制等类别的词表，如图 23.6 所示。

> LIWC, Linguistic Inquiry and Word Count, is a widely used set of 73 lexicons containing over 2300 words (Pennebaker et al., 2007), designed to capture aspects of lexical meaning relevant for social psychological tasks. In addition to sentiment-related lexicons like ones for negative emotion (bad, weird, hate, problem, tough) and positive emotion (love, nice, sweet), LIWC includes lexicons for categories like anger, sadness, cognitive mechanisms, perception, tentative, and inhibition, shown in Fig. 23.6.

> `LIWC`
>
> 释义：一套含 73 个类别、2300 多个词的文本分析词表，用于捕捉情感、认知、社会心理等方面的词汇意义特征。

还有各种其他手工构建的态度词表。General Inquirer 还包含针对强与弱、主动与被动、夸大与含蓄等维度的附加词表，以及诸如愉快、痛苦、美德、恶行、动机和认知取向等类别的词表。

> There are various other hand-built affective lexicons. The General Inquirer includes additional lexicons for dimensions like strong vs. weak, active vs. passive, overstated vs. understated, as well as lexicons for categories like pleasure, pain, virtue, vice, motivation, and cognitive orientation.

对各类任务而言另一个有用的特征是，区分具体

> Another useful feature for various tasks is the distinction between concrete

> `concrete abstract`（具体与抽象）
>
> 释义：按词义能否被感官感知而区分的词类特征，一端如香蕉、浴袍，另一端如信念、尽管，可用 1 至 5 分评定。

词（如香蕉或浴袍）与抽象词（如信念和尽管）之间的区别。

> words like banana or bathrobe and abstract words like belief and although. The

Brysbaert 等（2014）的词表使用众包为 40,000 个词的具体性赋予 1 到 5 的评分，从而给香蕉、浴袍和百吉饼评 5 分，给信念评 1.19 分，给尽管评 1.07 分，而介于其间的词如明快则评 2.5 分。

> lexicon in Brysbaert et al. (2014) used crowdsourcing to assign a rating from 1 to 5 of the concreteness of 40,000 words, thus assigning banana, bathrobe, and bagel 5, belief 1.19, although 1.07, and in between words like brisk a 2.5.

## 23.3 通过人工标注创建态度词表

> 23.3 Creating Affect Lexicons by Human Labeling

构建态度词表最早使用、至今仍普遍使用的方法是让人类为每个词标注。如今这通常通过众包完成：把任务拆成小块，分发给大量标注者。

> The earliest method used to build affect lexicons, and still in common use, is to have humans label each word. This is now most commonly done via crowdsourcing: breaking the task into small pieces and distributing them to a large number of anno-

> 正面情绪：欣赏*、安慰*、很好、快乐、兴趣、喜悦*、完美*、请*、安全*、极好、价值、哇*；负面情绪：愤怒*、无聊*、哭泣、绝望*、失败*、恐惧、悲伤*、憎恨*、恐慌*、受苦、使恐惧、暴力*；洞察力：意识到*、相信、决定*、感觉、弄清*、知道、懂得、意味着、注意*、认识*、感知、思考；抑制：避免*、小心*、犹豫*、限制*、反对*、阻止*、不情愿*、安全*、停止、固执*、等待、警惕；家庭：兄弟*、表亲*、女儿*、家庭、父亲*、祖父*、祖母*、丈夫、妈妈、母亲、侄女*、妻子；否定：不是、不能、没有、既不、从不、不、没有人*、一个也没有、也不、没有什么、无处、无
>
> *Positive Negative Emotion Emotion Insight Inhibition Family Negate appreciat* anger* aware* avoid* brother* aren’t comfort* bore* believe careful* cousin* cannot great cry decid* hesitat* daughter* didn’t happy despair* feel limit* family neither interest fail* figur* oppos* father* never joy* fear know prevent* grandf* no perfect* griev* knew reluctan* grandm* nobod*please* hate* means safe* husband none safe* panic* notice* stop mom nor terrific suffers recogni* stubborn* mother nothing value terrify sense wait niece* nowhere wow* violent* think wary wife without*

*图 23.6 LIWC 中 73 个词汇类别里 5 个类别的示例（Pennebaker 等，2007）。*
*Figure 23.6 Samples from 5 of the 73 lexical categories in LIWC (Pennebaker et al., 2007).*

> * 表示其前面的字母是一个词前缀，所有以该前缀开头的词都包含在该类别中。
>
> *The * means the previous letters are a word prefix and all words with that prefix are included in the category.*

让我们来看看两个众包情绪词表在方法上的一些选择。

> tators. Let’s take a look at some of the methodological choices for two crowdsourced emotion lexicons.

NRC 情绪词表（EmoLex）（Mohammad and Turney, 2013），其标注

> The NRC Emotion Lexicon (EmoLex) (Mohammad and Turney, 2013), labeled
情绪分两个步骤进行。为确保标注者评判的是该词的正确义项，他们先回答一道多项选择式的近义词题，以引导出该词的正确义项（无需标注者去阅读可能令人困惑的义项定义）。这些题目是自动生成的，使用的是 Macquarie 词典中与所考察义项的同义词库类别相关联的中心词，以及 3 个随机干扰类别的中心词。示例如下：

> emotions in two steps. To ensure that the annotators were judging the correct sense of the word, they first answered a multiple-choice synonym question that primed the correct sense of the word (without requiring the annotator to read a potentially confusing sense definition). These were created automatically using the headwords associated with the thesaurus category of the sense in question in the Macquarie dictionary and the headwords of 3 random distractor categories. An example:

哪个词在意义上与 startle 最接近（关联最强）？

> Which word is closest in meaning (most related) to startle?

- 汽车
- 摇晃
- 诚实
- 使娱乐

> automobile
> shake
> honesty
> entertain

对于每个词（例如 startle），随后要求标注者评定其关联程度

> For each word (e.g. startle), the annotator was then asked to rate how associated
该词与 8 种情绪（喜悦、恐惧、愤怒等）各自的关联程度。关联程度按无关联、弱关联、中等关联和强关联的等级评定。离群评分被剔除，随后每个词被赋予多数标注者所选的类别，票数相同时选择强度更高的那一类，最后把 4 个等级映射为每个词的一个二元标签（无关联和弱关联映射为 0，中等关联和强关联映射为 1）。

> that word is with each of the 8 emotions (joy, fear, anger, etc.). The associations were rated on a scale of not, weakly, moderately, and strongly associated. Outlier ratings were removed, and then each term was assigned the class chosen by the majority of the annotators, with ties broken by choosing the stronger intensity, and then the 4 levels were mapped into a binary label for each word (no and weak mapped to 0, moderate and strong mapped to 1).

NRC VAD 词表（Mohammad，2018a）的构建方式是，挑选来自既有词表的词语和

> The NRC VAD Lexicon (Mohammad, 2018a) was built by selecting words and
表情符号，并用众包方式通过最好-最差标度法对它们进行标注（Louviere 等，2015；Kiritchenko 与 Mohammad，2017）。在最好-

> emoticons from prior lexicons and annotating them with crowd-sourcing using bestworst scaling (Louviere et al. 2015, Kiritchenko and Mohammad 2017). In best-

> `best-worst scaling`（最好-最差标度法）
>
> 释义：让标注者在若干条目中挑出两端最极端的条目，再依据条目被选中的比例推算各自相对强度的众包标注方法。

最差标度法中，标注者会拿到 N 个条目（通常为 4 个），并被要求指出就某一属性而言哪个条目最好（最高）、哪个条目最差（最低）。用于描述标度两端的那组词取自既有文献。

> worst scaling, annotators are given N items (usually 4) and are asked which item is the best (highest) and which is the worst (lowest) in terms of some property. The set of words used to describe the ends of the scales are taken from prior literature.

以效价为例，评分者被问到：

> For valence, for example, the raters were asked:

问题 1. 下列四个词中，哪一个与幸福／快乐／积极／满意／知足／满怀希望关联最多，或者与不幸福／恼怒／消极／不满意／忧郁／绝望关联最少？（列出四个词作为选项。）问题 2. 下列四个词中，哪一个与幸福／快乐／积极／满意／知足／满怀希望关联最少，或者与不幸福／恼怒／消极／不满意／忧郁／绝望关联最多？（列出四个词作为选项。）词表中每个词的得分，是该条目被选为最好（V/A/D 最高）的次数占比减去它被选为最差（V/A/D 最低）的次数占比。标注之间的一致性用分半信度来评估：把语料分成两半，并计算

> Q1. Which of the four words below is associated with the MOST happiness / pleasure / positiveness / satisfaction / contentedness / hopefulness OR LEAST unhappiness / annoyance / negativeness / dissatisfaction / melancholy / despair? (Four words listed as options.) Q2. Which of the four words below is associated with the LEAST happiness / pleasure / positiveness / satisfaction / contentedness / hopefulness OR MOST unhappiness / annoyance / negativeness / dissatisfaction/ melancholy / despair? (Four words listed as options.) The score for each word in the lexicon is the proportion of times the item was chosen as the best (highest V/A/D) minus the proportion of times the item was chosen as the worst (lowest V/A/D). The agreement between annotations are evaluated by splithalf reliability: split the corpus in half and compute the correlations between the

> `split-half reliability`（分半信度）
>
> 释义：把同一批标注结果分成两半，用两半之间的相关程度来衡量标注一致性的评估方法。

两半中的标注之间的相关性。

> annotations in the two halves.

## 23.4 态度词表的半监督归纳

> 23.4 Semi-supervised Induction of Affect Lexicons

另一种学习情感词表的常见做法是，从一组定义语义轴两极的种子词（如 good 或 bad 这类词）出发，然后设法依据每个词 w 与这两个种子集的相似度为其打上标签。这里我们总结两类基于种子的半监督词表归纳算法：基于轴的（axis-based）与基于图的（graph-based）。

> Another common way to learn sentiment lexicons is to start from a set of seed words that define two poles of a semantic axis (words like good or bad), and then find ways to label each word w by its similarity to the two seed sets. Here we summarize two families of seed-based semi-supervised lexicon induction algorithms, axis-based and graph-based.

### 23.4.1 语义轴方法

> 23.4.1 Semantic Axis Methods

最著名的词表归纳方法之一，即 Turney 与 Littman（2003）的算法，先给定 good 或 bad 之类的种子词，然后对每个待标注的词 w，同时度量它与 good 的相似程度以及它与 bad 的差异程度。

> One of the most well-known lexicon induction methods, the Turney and Littman(2003) algorithm, is given seed words like good or bad, and then for each word w to be labeled, measures both how similar it is to good and how different it is from bad.

这里我们介绍 An 等（2018）对该算法所做的一个小幅扩展，它基于对语义轴的计算。

> Here we describe a slight extension of the algorithm due to An et al. (2018), which is based on computing a semantic axis.

第一步，我们手工挑选种子词。有两种方法

> In the first step, we choose seed words by hand. There are two methods for
处理同一个词在不同语境中态度不同这一事实：（1）从一个单一的大型种子词表出发，依靠归纳算法把它微调到目标领域；或者（2）为不同体裁挑选不同的种子词。Hellrich 等（2019）指出，在为不同历史时期建模态度时，从一部大型现代态度词典出发，要优于使用为跨时间稳定而调校过的小种子集。作为第二种做法的一个例子，Hamilton 等（2016a）为一般情感分析定义了一组种子词，为 Twitter 定义了另一组，又为金融文本中的情感定义了第三组：

> dealing with the fact that the affect of a word is different in different contexts: (1) start with a single large seed lexicon and rely on the induction algorithm to fine-tune it to the domain, or (2) choose different seed words for different genres. Hellrich et al. (2019) suggests that for modeling affect across different historical time periods, starting with a large modern affect dictionary is better than small seedsets tuned to be stable across time. As an example of the second approach, Hamilton et al. (2016a) define one set of seed words for general sentiment analysis, a different set for Twitter, and yet another set for sentiment in financial text:

> 领域 正向种子词 负向种子词
>
> *Domain Positive seeds Negative seeds*

> 通用 好、可爱、优秀、幸运、pleas-、坏、可怕、糟糕、不幸、unant、令人愉悦、完美、被爱、爱、愉快、令人厌恶、邪恶、被憎恨、憎恨、快乐、不快乐
>
> *General good, lovely, excellent, fortunate, pleas- bad, horrible, poor, unfortunate, unant, delightful, perfect, loved, love, pleasant, disgusting, evil, hated, hate, happy unhappy*

> Twitter 爱、被爱、爱着、极好、不错、恨、被恨、憎恨着、糟糕、讨厌、可怕、
>
> *Twitter love, loved, loves, awesome, nice, hate, hated, hates, terrible, nasty, awful,*

> 令人惊叹、最好、了不起、正确、快乐 最差、可怕、错误、悲伤
>
> *amazing, best, fantastic, correct, happy worst, horrible, wrong, sad*

> 金融 成功的、优秀的、利润、有益的、疏忽的、损失、波动、错误的、亏损、
>
> *Finance successful, excellent, profit, beneficial, negligent, loss, volatile, wrong, losses,*

> 改善、好转、成功、收益、损害、糟糕、诉讼、失败、下跌、正面 负面
>
> *improving, improved, success, gains, damages, bad, litigation, failure, down, positive negative*

第二步，我们为每个极点词计算嵌入。这些

> In the second step, we compute embeddings for each of the pole words. These
嵌入可以是现成的 word2vec 嵌入，也可以直接在一个特定语料上计算（例如，如果目标是一部金融词表，就使用金融语料），或者我们可以把现成的嵌入微调到某个语料上。如果我们面对的是一种非常特定的文本体裁，却又没有足够的数据训练出好的嵌入，那么微调就尤为重要。在微调时，我们从 word2vec 之类的现成嵌入出发，在小型目标语料上继续训练它们。

> embeddings can be off-the-shelf word2vec embeddings, or can be computed directly on a specific corpus (for example using a financial corpus if a finance lexicon is the goal), or we can fine-tune off-the-shelf embeddings to a corpus. Fine-tuning is especially important if we have a very specific genre of text but don’t have enough data to train good embeddings. In fine-tuning, we begin with off-the-shelf embeddings like word2vec, and continue training them on the small target corpus.

一旦我们有了每个极点词的嵌入，我们就构造一个嵌入，它

> Once we have embeddings for each pole word, we create an embedding that
通过取各个种子词嵌入的质心来表示每个极点；回忆一下，质心是均值在多维情形下的推广。给定正向种子词的一组嵌入 S+ = {E(w+ 1 ),E(w+ 2 ),...,E(w+ n )}，以及负向种子词的嵌入 S−= {E(w− 1 ),E(w− 2 ),...,E(w− m)}，两个极点的质心为：

> represents each pole by taking the centroid of the embeddings of each of the seed words; recall that the centroid is the multidimensional version of the mean. Given a set of embeddings for the positive seed words S+ = {E(w+ 1 ),E(w+ 2 ),...,E(w+ n )}, and embeddings for the negative seed words S−= {E(w− 1 ),E(w− 2 ),...,E(w− m)}, the pole centroids are:

> n

V+ = 1 X
E(w+ i )
n

> 1 m

V−= 1 X_1

E(w− (23.1)
m i )
由这两个极点定义的语义轴，只需把这两个向量相减即可算出：

> The semantic axis defined by the poles is computed just by subtracting the two vectors:

Vaxis = V+ −V− (23.2)
Vaxis 即语义轴，是指向正向情感方向的向量。最后，我们（通过余弦相似度）计算正向情感方向向量与 w 的嵌入方向之间的夹角。余弦值越高，意味着 w 与 S+ 的一致性比与 S− 的一致性更强。

> Vaxis, the semantic axis, is a vector in the direction of positive sentiment. Finally, we compute (via cosine similarity) the angle between the vector in the direction of positive sentiment and the direction of w’s embedding. A higher cosine means that w is more aligned with S+ than S−.

  
score(w) = cos E(w),Vaxis
E(w)·Vaxis (23.3)
= ∥E(w)∥∥Vaxis∥
如果一部带有情感得分的词表词典就够了，那我们就大功告成了！或者，如果我们

> If a dictionary of words with sentiment scores is sufficient, we’re done! Or if we
需要把词划分到一个正向词表和一个负向词表中，我们可以使用一个阈值或其他方法来得到离散的词表。

> need to group words into a positive and a negative lexicon, we can use a threshold or other method to give us discrete lexicons.

### 23.4.2 标签传播

> 23.4.2 Label Propagation

另一类方法通过在图上传播情感标签来定义词表，这一思想由 Hatzivassiloglou 与 McKeown（1997）的早期工作提出。我们将介绍 Hamilton 等人（2016a）提出的简单 SentProp（情感传播，Sentiment Propagation）算法，它包含四个步骤：

> An alternative family of methods defines lexicons by propagating sentiment labels on graphs, an idea suggested in early work by Hatzivassiloglou and McKeown(1997). We’ll describe the simple SentProp (Sentiment Propagation) algorithm of Hamilton et al. (2016a), which has four steps:

- 定义图：给定词嵌入，通过把每个词与其 k 个最近邻（依据余弦相似度）相连，构建一张带权的词汇图。词 wi 与 wj 之间边的权重设定为：

> Define a graph: Given word embeddings, build a weighted lexical graph by connecting each word with its k nearest neighbors (according to cosine similarity). The weights of the edge between words wi and wj are set as:

 wi⊤wj  (23.4)
Ei,j = arccos
− .∥wi∥∥wj∥

- 定义种子集：选取正向种子词和负向种子词。
- 从种子集传播极性：现在我们在该图上从种子集出发进行随机游走。在随机游走中，我们从一个节点出发，

> Define a seed set: Choose positive and negative seed words.
> Propagate polarities from the seed set: Now we perform a random walk on this graph, starting at the seed set. In a random walk, we start at a node and

然后按照与边概率成正比的概率选择要转移到的节点。一个词相对于某个种子集的极性得分，与从该种子集出发的随机游走落在该词上的概率成正比（图 23.7）。

> then choose a node to move to with probability proportional to the edge probability. A word’s polarity score for a seed set is proportional to the probability of a random walk from the seed set landing on that word (Fig. 23.7).

- 生成词得分：我们分别从正向和负向种子集出发进行游走，得到正向（rawscore+(wi)）和负向（rawscore−(wi)）的原始标签得分。然后我们将这些值合并为一个正向极性得分：

> Create word scores: We walk from both positive and negative seed sets, resulting in positive (rawscore+(wi)) and negative (rawscore−(wi)) raw label scores. We then combine these values into a positive-polarity score as:

rawscore+(wi)
score+(wi) = (23.5)
rawscore+(wi)+rawscore−(wi)
通常有帮助的做法是对得分进行标准化，使其在某个语料库内具有零均值和单位方差。

> It’s often helpful to standardize the scores to have zero mean and unit variance within a corpus.

- 为每个得分赋予置信度：由于情感得分受种子集影响，我们想知道如果换用不同的种子集，一个词的得分会变化多少。我们可以使用自举（bootstrapping）抽样来得到置信区域，方法是在正向和负向种子集的随机子集上计算传播 B 次（例如取 B = 50，每次从 10 个种子词中选择 7 个）。自举抽样的极性得分的标准差给出了一个置信度量。

> Assign confidence to each score: Because sentiment scores are influenced by the seed set, we’d like to know how much the score of a word would change if a different seed set is used. We can use bootstrap sampling to get confidence regions, by computing the propagation B times over random subsets of the positive and negative seed sets (for example using B = 50 and choosing 7 of the 10 seed words each time). The standard deviation of the bootstrap sampled polarity scores gives a confidence measure.

![](images/23-lexicons-sentiment/fig_p9_0.png)

*图 23.7 SENTPROP 算法的直观示意。(a) 从种子词出发进行随机游走。(b) 依据随机游走访问的频率赋予极性得分（此处以绿色或红色表示）。*
*Figure 23.7 Intuition of the SENTPROP algorithm. (a) Run random walks from the seed words. (b) Assign polarity scores (shown here as colors green or red) based on the frequency of random walk visits.*

### 23.4.3 其他方法

> 23.4.3 Other Methods

半监督算法的核心是衡量与种子词相似度的度量。上述 Turney 与 Littman（2003）以及 Hamilton 等人（2016a）的方法使用嵌入余弦作为距离度量：基本上，如果一个词的嵌入与正向种子词的余弦较高、与负向种子词的余弦较低，它就被标注为正向。除了嵌入余弦之外，其他方法还选择了其他类型的距离度量。

> The core of semisupervised algorithms is the metric for measuring similarity with the seed words. The Turney and Littman (2003) and Hamilton et al. (2016a) approaches above used embedding cosine as the distance metric: words were labeled as positive basically if their embeddings had high cosines with positive seeds and low cosines with negative seeds. Other methods have chosen other kinds of distance metrics besides embedding cosine.

例如，Hatzivassiloglou 与 McKeown（1997）的算法使用句法

> For example the Hatzivassiloglou and McKeown (1997) algorithm uses syntactic
线索；如果两个形容词经常由 and 连接、而很少由 but 连接，就认为它们相似。这基于一个直觉：由 and 连接的形容词往往具有相同的极性；正向形容词通常与正向形容词并列，负向形容词与负向形容词并列：

> cues; two adjectives are considered similar if they were frequently conjoined by and and rarely conjoined by but. This is based on the intuition that adjectives conjoined by the words and tend to have the same polarity; positive adjectives are generally coordinated with positive, negative with negative:

fair and legitimate、corrupt and brutal

> fair and legitimate, corrupt and brutal
但正向形容词与负向形容词并列的情况较少见：

> but less often positive adjectives coordinated with negative:

*fair and brutal、*corrupt and legitimate

> *fair and brutal, *corrupt and legitimate
相比之下，由 but 连接的形容词很可能具有相反的极性：

> By contrast, adjectives conjoined by but are likely to be of opposite polarity:

fair but brutal
相反极性的另一个线索来自形态否定（un-、im-、

> Another cue to opposite polarity comes from morphological negation (un-, im-,
-less）。词根相同但在形态否定上不同的形容词（adequate/inadequate、thoughtful/thoughtless）往往具有相反的极性。

> -less). Adjectives with the same root but differing in a morphological negative (adequate/inadequate, thoughtful/thoughtless) tend to be of opposite polarity.

还有一种寻找与种子词极性相似的词的方法

> Yet another method for finding words that have a similar polarity to seed words
是利用像 WordNet 这样的同义词词典（Kim 与 Hovy 2004，Hu 与 Liu 2004）。

> is to make use of a thesaurus like WordNet (Kim and Hovy 2004, Hu and Liu 2004).

一个词的同义词大概共享它的极性，而一个词的反义词很可能具有相反的极性。在种子词表构建完成后，每个词表按如下方式更新，并可能迭代进行。

> A word’s synonyms presumably share its polarity while a word’s antonyms probably have the opposite polarity. After a seed lexicon is built, each lexicon is updated as follows, possibly iterated.

Lex+：加入正向词的同义词（well）以及负向词的反义词（如 fine）

> Lex+: Add synonyms of positive words (well) and antonyms (like fine) of negative
词

> words
Lex−：加入负向词的同义词（awful）以及正向词的反义词（如 evil）

> Lex−: Add synonyms of negative words (awful) and antonyms (like evil) of positive
词

> words
该算法的一个扩展为 WordNet 的词义赋予极性，称为 SentiWordNet（Baccianella 等人，2010）。图 23.8 给出了一些例子。

> An extension of this algorithm assigns polarity to WordNet senses, called Senti-WordNet (Baccianella et al., 2010). Fig. 23.8 shows some examples.

> `SentiWordNet`
>
> 释义：一种情感词表：为 WordNet 的每个同义词集分别赋予正面、负面与客观三类情感得分。

| 同义词集<br>Synset |  | 正面<br>Pos | 负面<br>Neg | 客观<br>Obj |
| --- | --- | --- | --- | --- |
| good#6“令人愉快的或讨人喜欢的”<br>good#6 ‘agreeable or pleasing’ |  | 1 | 0 | 0 |
| respectable#2 honorable#4 good#4 estimable#2“值得尊敬的”<br>respectable#2 honorable#4 good#4 estimable#2 ‘deserving of esteem’ |  | 0.75 | 0 | 0.25 |
| estimable#3 computable#1“可以计算或估计的”<br>estimable#3 computable#1 ‘may be computed or estimated’ |  | 0 | 0 | 1 |
| sting#1 burn#4 bite#2“引起尖锐或刺痛般的疼痛”<br>sting#1 burn#4 bite#2 ‘cause a sharp or stinging pain’ |  | 0 | 0.875 | .125 |
| acute#6“具有关键的重要性和后果”<br>acute#6 ‘of critical importance and consequence’ |  | 0.625 | 0.125 | .250 |
| acute#4“角的；小于 90 度”<br>acute#4 ‘of an angle; less than 90 degrees’ |  | 0 | 0 | 1 |
| acute#1“发作迅速、病程短暂但严重的”<br>acute#1 ‘having or experiencing a rapid onset and short but severe course’ |  | 0 | 0.5 | 0.5 |
| 图 23.8<br>Figure 23.8 | 取自 SentiWordNet 3.0 的示例（Baccianella 等，2010）。注意不同义项之间的差异<br>Examples from SentiWordNet 3.0 (Baccianella et al., 2010). Note the differences between sense |  |  |  |

good#6“令人愉快的或讨人喜欢的” 1 0 0 respectable#2 honorable#4 good#4 estimable#2“值得尊敬的” 0.75 0 0.25 estimable#3 computable#1“可以计算或估计的” 0 0 1 sting#1 burn#4 bite#2“引起尖锐或刺痛般的疼痛” 0 0.875 .125 acute#6“具有关键的重要性和后果” 0.625 0.125 .250 acute#4“角的；小于 90 度” 0 0 1 acute#1“发作迅速、病程短暂但严重的” 0 0.5 0.5

> good#6 ‘agreeable or pleasing’ 1 0 0 respectable#2 honorable#4 good#4 estimable#2 ‘deserving of esteem’ 0.75 0 0.25 estimable#3 computable#1 ‘may be computed or estimated’ 0 0 1 sting#1 burn#4 bite#2 ‘cause a sharp or stinging pain’ 0 0.875 .125 acute#6 ‘of critical importance and consequence’ 0.625 0.125 .250 acute#4 ‘of an angle; less than 90 degrees’ 0 0 1 acute#1 ‘having or experiencing a rapid onset and short but severe course’ 0 0.5 0.5

*图 23.8 SentiWordNet 3.0 中的示例（Baccianella 等，2010）。注意同形异义词不同义项之间的差异：estimable#3 纯粹是客观的，而 estimable#2 是正面的；acute 可以是正面的（acute#6）、负面的（acute#1），也可以是中性的（acute #4）。*
*Figure 23.8 Examples from SentiWordNet 3.0 (Baccianella et al., 2010). Note the differences between senses of homonymous words: estimable#3 is purely objective, while estimable#2 is positive; acute can be positive(acute#6), negative (acute#1), or neutral (acute #4).*

在该算法中，极性赋予的是整个同义词集，而不是单个词。

> In this algorithm, polarity is assigned to entire synsets rather than words. A

正面词表由与 7 个正面词相关联的所有同义词集构成，负面词表则由与 7 个负面词相关联的同义词集构成。随后用这些数据训练一个分类器，使其接收一个 WordNet 释义，并判断正在被定义的义项是正面的、负面的还是中性的。还有一个步骤（涉及随机游走算法）会为每个 WordNet 同义词集赋予一个得分，表示其正面、负面和中性的程度。

> positive lexicon is built from all the synsets associated with 7 positive words, and a negative lexicon from synsets associated with 7 negative words. A classifier is then trained from this data to take a WordNet gloss and decide if the sense being defined is positive, negative or neutral. A further step (involving a random-walk algorithm) assigns a score to each WordNet synset for its degree of positivity, negativity, and neutrality.

总之，半监督算法使用一组由人工定义的种子词

> In summary, semisupervised algorithms use a human-defined set of seed words
来表示某一维度的两个端点，并使用嵌入余弦、并列结构、形态学或同义词词典结构等相似度指标，根据词与正面种子词的相似程度以及与负面种子词的不相似程度来为词打分。

> for the two poles of a dimension, and use similarity metrics like embedding cosine, coordination, morphology, or thesaurus structure to score words by how similar they are to the positive seeds and how dissimilar to the negative seeds.

## 23.5 词情感的有监督学习

> 23.5 Supervised Learning of Word Sentiment

半监督方法只需要极少的人工监督（以种子集的形式）。但有时现实世界中存在某种监督信号，并且可以利用它。其中一种信号就是与在线评论相关联的评分。

> Semi-supervised methods require only minimal human supervision (in the form of seed sets). But sometimes a supervision signal exists in the world and can be made use of. One such signal is the scores associated with online reviews.

网络上包含数量极为庞大的餐馆评论、电影评论、

> The web contains an enormous number of online reviews for restaurants, movies,
图书或其他产品的在线评论，每一条评论都带有评论正文以及一个

> books, or other products, each of which have the text of the review along with an

> 电影评论摘录（IMDb）
>
> *Movie review excerpts (IMDb)*

> 10 一部很棒的电影。这部影片就是一次绝妙的体验。它超现实、怪诞、机智，又充满闹剧色彩，
>
> *10 A great movie. This film is just a wonderful experience. It’s surreal, zany, witty and slapstick*

> 而且这些同时具备。表演也非常出色。
>
> *all at the same time. And terrific performances too.*

> 1 这大概是我看过的最糟糕的电影。故事情节毫无进展，尽管他们
>
> *1 This was probably the worst movie I have ever seen. The story went nowhere even though they*

> 本可以从中做出一些有意思的东西。
>
> *could have done some interesting stuff with it.*

> 餐馆评论摘录（Yelp）
>
> *Restaurant review excerpts (Yelp)*

> 5 服务无可挑剔。食物烹制与调味都恰到好处……那块西瓜
>
> *5 The service was impeccable. The food was cooked and seasoned perfectly... The watermelon*

> 切得方方正正……烤章鱼……令人垂涎……
>
> *was perfectly square ... The grilled octopus was ... mouthwatering...*

> 2 ……我们等了好一会儿才喝上水，主菜先于前菜上桌，而且我们一直没有拿到
>
> *2 ...it took a while to get our waters, we got our entree before our starter, and we never received*

> 餐具或餐巾，直到我们主动索要……
>
> *silverware or napkins until we requested them...*

> 图书评论摘录（GoodReads）
>
> *Book review excerpts (GoodReads)*

> 1 我要设法不再被那些抓眼球的标题所蒙骗。我原本非常想喜欢这本书，
>
> *1 I am going to try and stop being deceived by eye-catching titles. I so wanted to like this book*

> 结果却对它非常失望。
>
> *and was so disappointed by it.*

> 5 这本书非常搞笑。我会把它推荐给任何想找一本带有
>
> *5 This book is hilarious. I would recommend it to anyone looking for a satirical read with a*

> 浪漫转折、且叙述者不断插话的讽刺读物的读者
>
> *romantic twist and a narrator that keeps butting in*

> 产品评论摘录（Amazon）
>
> *Product review excerpts (Amazon)*

> 5 不过这台搅拌机的盖子大概是我最喜欢的地方……它能让你在不
>
> *5 The lid on this blender though is probably what I like the best about it... enables you to pour*

> 取下盖子的情况下就倒进别的容器！……完美的壶身！……运行得棒极了。
>
> *into something without even taking the lid off! ... the perfect pitcher! ... works fantastic.*

> 1 我讨厌这台搅拌机……几乎不可能把冷冻水果和冰块打成冰沙……
>
> *1 I hate this blender... It is nearly impossible to get frozen fruit and ice to turn into a smoothie...*

> 你得加超多的液体。我还希望它有个壶嘴……
>
> *You have to add a TON of liquid. I also wish it had a spout ...*

*图 23.9 取自各类评论网站的一些评论摘录，除 IMDb 采用 1 到 10 星标度外，其余均采用 1 到 5 星标度。*
*Figure 23.9 Excerpts from some reviews from various review websites, all on a scale of 1 to 5 stars except IMDb, which is on a scale of 1 to 10 stars.*

相关联的评论评分：其取值可能从 1 星到 5 星，或者按 1 到 10 打分。图 23.9 展示了从餐馆、图书和电影评论中摘取的样例。

> associated review score: a value that may range from 1 star to 5 stars, or scoring 1 to 10. Fig. 23.9 shows samples extracted from restaurant, book, and movie reviews.

我们可以把这种评论评分用作监督信号：正面词更可能

> We can use this review score as supervision: positive words are more likely to
出现在 5 星评论中；负面词则更可能出现在 1 星评论中。而且，这种监督不只是给出二值极性，它还使我们能够为词赋予一种更复杂的极性表示：它在各星级（或其他评分）上的分布。

> appear in 5-star reviews; negative words in 1-star reviews. And instead of just a binary polarity, this kind of supervision allows us to assign a word a more complex representation of its polarity: its distribution over stars (or other scores).

因此在十分制中，我们可以把每个词的情感表示为

> Thus in a ten-star system we could represent the sentiment of each word as a
一个 10 元组，其中每个数字都是一个得分，表示该词与对应极性水平的关联程度。对从 1 到 10 的每个类别 c，这种关联可以是原始计数，也可以是似然 P(w|c)，或者是计数的其他某种函数。

> 10-tuple, each number a score representing the word’s association with that polarity level. This association can be a raw count, or a likelihood P(w|c), or some other function of the count, for each class c from 1 to 10.

例如，我们可以这样计算 disappoint(ed/ing) 这类词出现在 1 星评论中的 IMDb 似然：用该词在 IMDb 数据集的 1 星评论中出现的次数（8,557）除以 1 星评论中出现的词总数（25,395,214），于是 P(disappointing|1) 的 IMDb 估计值为 .0003。

> For example, we could compute the IMDb likelihood of a word like disappoint(ed/ing) occurring in a 1 star review by dividing the number of times disappoint(ed/ing) occurs in 1-star reviews in the IMDb dataset (8,557) by the total number of words occurring in 1-star reviews (25,395,214), so the IMDb estimate of P(disappointing|1) is .0003.

对这种加权方式稍作修改，即归一化似然，可用于

> A slight modification of this weighting, the normalized likelihood, can be used
作为一种富有启发性的可视化（Potts, 2011）1

> as an illuminating visualization (Potts, 2011)1
count(w,c)
P(w|c) = P
w∈C count(w,c) P(w|c)
PottsScore(w) = P
c P(w|c) (23.6)
将 IMDb 估计值 P(disappointing|1)=.0003 除以所有类别上似然 P(w|c) 之和，得到 Potts 分数 0.10。于是词 disappointing 与向量 [.10, .12, .14, .14, .13, .11, .08, .06, .06, .05] 相关联。Potts 图（Potts, 2011）是这些词分数的可视化，它表示

> Dividing the IMDb estimate P(disappointing|1) of .0003 by the sum of the likelihood P(w|c) over all categories gives a Potts score of 0.10. The word disappointing thus is associated with the vector [.10, .12, .14, .14, .13, .11, .08, .06, .06, .05]. The Potts diagram (Potts, 2011) is a visualization of these word scores, representing the

> `Potts diagram`（Potts 图）
>
> 释义：把单词的先验情感表示为各评分类别上的概率分布曲线，并依据曲线形状刻画其情感类型的一种可视化图。

单词的先验情感在各评分类别上的分布。

> prior sentiment of a word as a distribution over the rating categories.

图 23.10 给出了 3 个正面和 3 个负面程度形容词的 Potts 图。请注意，强正面程度词的曲线呈字母 J 形，而强负面程度词看起来像倒 J 形。相比之下，弱正面和弱负面程度词呈驼峰形，其峰值要么低于均值（如 disappointing 这类弱负面词），要么高于均值（如 good 这类弱正面词）。这些形状提供了一种富有启发性的情感含义类型学。

> Fig. 23.10 shows the Potts diagrams for 3 positive and 3 negative scalar adjectives. Note that the curve for strongly positive scalars have the shape of the letter J, while strongly negative scalars look like a reverse J. By contrast, weakly positive and negative scalars have a hump-shape, with the maximum either below the mean (weakly negative words like disappointing) or above the mean (weakly positive words like good). These shapes offer an illuminating typology of affective meaning.

![](images/23-lexicons-sentiment/fig_p12_0.png)

![](images/23-lexicons-sentiment/img_1145.jpeg)

![](images/23-lexicons-sentiment/img_1120.jpeg)

![](images/23-lexicons-sentiment/img_1125.jpeg)

*图 23.10 正面和负面程度形容词的 Potts 图（Potts, 2011），展示了强正面和强负面形容词的 J 形与倒 J 形，以及极性较弱的形容词的驼峰形。*
*Figure 23.10 Potts diagrams (Potts, 2011) for positive and negative scalar adjectives, showing the J-shape and reverse J-shape for strongly positive and negative adjectives, and the hump-shape for more weakly polarized adjectives.*

图 23.11 给出了强调副词和弱化副词的 Potts 图。

> Fig. 23.11 shows the Potts diagrams for emphasizing and attenuating adverbs.

请注意，强调词往往呈 J 形（最可能出现在最正面的评论中）或 U 形（最可能出现在强正面和强负面评论中）。弱化词则都呈驼峰形，强调量表的中间部分而淡化两端。这些图既可用作词汇情感的类型学，也在情感组合性建模中发挥作用。

> Note that emphatics tend to have a J-shape (most likely to occur in the most positive reviews) or a U-shape (most likely to occur in the strongly positive and negative). Attenuators all have the hump-shape, emphasizing the middle of the scale and downplaying both extremes. The diagrams can be used both as a typology of lexical sentiment, and also play a role in modeling sentiment compositionality.

除了后验 P(c|w)、似然 P(w|c) 或归一化

> In addition to functions like posterior P(c|w), likelihood P(w|c), or normalized
似然（式 23.6）这类函数之外，单词与情感标签共现次数的许多其他函数也已被使用。我们将在第 534 页介绍其中一些，包括式 23.14 中按作者对计数做归一化等思路。

> likelihood (Eq. 23.6) many other functions of the count of a word occurring with a sentiment label have been used. We’ll introduce some of these on page 534, including ideas like normalizing the counts per writer in Eq. 23.14.

### 23.5.1 对数几率比信息狄利克雷先验

> 23.5.1 Log Odds Ratio Informative Dirichlet Prior

对于单词极性，我们经常想做的一件事是区分更可能用于某一类文本而非另一类文本的词。例如，我们可能想知道与 1 星评论最相关的词，以及与 5 星评论最相关的词。这些差异未必只与情感有关。我们可能想找出美国国会中民主党人比共和党人使用得更频繁的词，或者昂贵餐厅菜单中比廉价餐厅

> One thing we often want to do with word polarity is to distinguish between words that are more likely to be used in one category of texts than in another. We may, for example, want to know the words most associated with 1 star reviews versus those associated with 5 star reviews. These differences may not be just related to sentiment. We might want to find words used more often by Democratic than Republican members of Congress, or words used more often in menus of expensive restaurants

![](images/23-lexicons-sentiment/fig_p13_0.png)

![](images/23-lexicons-sentiment/img_1837.jpeg)

![](images/23-lexicons-sentiment/img_1862.jpeg)

![](images/23-lexicons-sentiment/img_1832.jpeg)

![](images/23-lexicons-sentiment/img_1842.jpeg)

![](images/23-lexicons-sentiment/img_1822.jpeg)

![](images/23-lexicons-sentiment/img_1827.jpeg)

*图 23.11 强调副词与弱化副词的 Potts 图（Potts, 2011）。*
*Figure 23.11 Potts diagrams (Potts, 2011) for emphatic and attenuating adverbs.*

更常出现的词。

> than cheap restaurants.

给定两类文档，要找出与某一类别关联更强的词，我们可以度量频率之差（词 w 在类别 A 中更频繁，还是在类别 B 中更频繁？）。或者，不做频率之差，而是计算频率之比，或计算对数几率比（两个词的几率之比的对数）。随后，我们可以按所选的关联度量对词排序，从在类别 A 中过度代表的词排到在类别 B 中过度代表的词。

> Given two classes of documents, to find words more associated with one category than another, we could measure the difference in frequencies (is a word w more frequent in class A or class B?). Or instead of the difference in frequencies we could compute the ratio of frequencies, or compute the log odds ratio (the log of the ratio between the odds of the two words). We could then sort words by whichever association measure we pick, ranging from words overrepresented in category A to words overrepresented in category B.

简单的对数似然或对数几率方法的问题在于，它们会过分强调极罕见词的差异，而且往往还会过分强调极高频词的差异。极罕见词在两个语料库中看起来出现情况差别很大，因为计数极小时可能存在统计波动，甚至出现在一个语料库中为零次而另一个语料库中为非零次的情况。极高频词也会显得不同，因为所有计数都很大。

> The problem with simple log-likelihood or log odds methods is that they overemphasize differences in very rare words, and often also in very frequent words. Very rare words will seem to occur very differently in the two corpora since with tiny counts there may be statistical fluctuations, or even zero occurrences in one corpus compared to non-zero occurrences in the other. Very frequent words will also seem different since all counts are large.

在本节中，我们逐一讲解该问题的一种解决方案的细节：

> In this section we walk through the details of one solution to this problem: the

Monroe 等人（2008）提出的“对数几率比信息狄利克雷先验”方法，它是找出相对于另一类文本在某一特定类别文本中统计上过度代表的词的一种特别有用的方法。其思想是利用另一个大型语料库，得到对每个词频率的先验估计。

> “log odds ratio informative Dirichlet prior” method of Monroe et al. (2008) that is a particularly useful method for finding words that are statistically overrepresented in one particular category of texts compared to another. It’s based on the idea of using another large corpus to get a prior estimate of what we expect the frequency of each word to be.

我们先从目标说起：假设我们想知道单词 horrible

> Let’s start with the goal: assume we want to know whether the word horrible

> `log likelihood ratio`（对数似然比）
>
> 释义：用对数形式的比值比较某个词在两个语料库中出现的相对频率差异，但会对极罕见词和极高频词过度敏感。

在语料库 i 中还是在语料库 j 中出现得更多。我们可以计算对数似然比，

> occurs more in corpus i or corpus j. We could compute the log likelihood ratio,
其中用 f i(w) 表示词 w 在语料库 i 中的频率，用 ni 表示语料库 i 中的总词数：

> using f i(w) to mean the frequency of word w in corpus i, and ni to mean the total number of words in corpus i:

llr(horrible) = log Pi(horrible)
Pj(horrible)
= logPi(horrible)−logPj(horrible)= log fi(horrible) −log fj(horrible)
ni nj (23.7)
取而代之，我们来计算对数几率比：horrible 在 i 中还是在 j 中的几率更高：

> Instead, let’s compute the log odds ratio: does horrible have higher odds in i or in j:

 Pi(horrible)   Pj(horrible) 
lor(horrible) = log 1−Pi(horrible) −log 1−Pj(horrible)
 fi(horrible)   f j(horrible) 

>  fi(horrible)   f j(horrible) 
= log  ni  −log  n j 

> = log  ni  −log  n j 
 1−fi(horrible)  1−fj(horrible) 

>  1−fi(horrible)  1−fj(horrible) 
ni nj
 fi(horrible)   f j(horrible)  (23.8)
= log −log
ni −fi(horrible) nj −fj(horrible)
狄利克雷先验的直觉是：利用一个大规模背景语料库，来获得我们对每个词 w 的频率应当是多少的先验估计。做法非常简单：把该语料库中的计数加到分子和分母上，从而在实质上把计数朝该先验收缩。这就好比在问：相较于一个估计良好的大规模背景语料库所预期的频率，i 与 j 之间的差异究竟有多大。

> The Dirichlet intuition is to use a large background corpus to get a prior estimate of what we expect the frequency of each word w to be. We’ll do this very simply by adding the counts from that corpus to the numerator and denominator, so that we’re essentially shrinking the counts toward that prior. It’s like asking how large are the differences between i and j given what we would expect given their frequencies in a well-estimated large background corpus.

该方法估计的是词 w 在两个

> The method estimates the difference between the frequency of word w in two
语料库 i 与 j 中频率的差异，所用的是 w 的经先验修正的对数几率比 δ (i−j) ，其估计式为

> corpora i and j via the prior-modified log odds ratio for w, δ (i−j) , which is estimated
如下：

> as:

> w

  f j ! (23.9)
δ (i−j) f i w +αw w +αw
= log −log
ni +α0 −(f iw +αw) nj +α0 −(f j w +αw)
（其中 ni 是语料库 i 的规模，n j 是语料库 j 的规模，f i w 是词 w 在语料库 i 中的计数，f j w 是词 w 在语料库 j 中的计数，α0 是背景语料库的缩放规模，αw 是词 w 在背景语料库中的缩放计数。）

> (where ni is the size of corpus i, n j is the size of corpus j, f i w is the count of word w in corpus i, f j w is the count of word w in corpus j, α0 is the scaled size of the background corpus, and αw is the scaled count of word w in the background corpus.)
此外，Monroe 等人（2008）还利用了对方差的一个估计，该方差属于

> In addition, Monroe et al. (2008) make use of an estimate for the variance of the
对数几率比：

> log–odds–ratio:

> w

σ2   1 1
ˆδ (i−j) (23.10)
≈ +
f iw +αw f j w +αw
一个词最终的统计量就是其对数几率比的 z 分数：

> The final statistic for a word is then the z–score of its log–odds–ratio:

> w

ˆδ (i−j) (23.11)
r  σ2 ˆδ (i−j)
因此，Monroe 等人（2008）的方法从两个方面改造了常用的对数几率比：它使用对数几率比的 z 分数，从而控制了词频中方差的大小；它还使用背景语料库中的计数，为各个词提供一个先验计数。

> The Monroe et al. (2008) method thus modifies the commonly used log odds ratio in two ways: it uses the z-scores of the log odds ratio, which controls for the amount of variance in a word’s frequency, and it uses counts from a background corpus to provide a prior count for words.

> w

> w

图 23.12 展示了把该方法应用于一个餐厅评论数据集的结果，这些评论来自

> Fig. 23.12 shows the method applied to a dataset of restaurant reviews from
Yelp，把一星评论中使用的词与五星评论中使用的词加以比较（Jurafsky 等，2014）。差异最大的是那些显而易见的情感词：一星评论使用 worse、bad、awful 这类负面情感词，五星评论则使用 great、best、amazing 这类正面情感词。但还有一些同样很有启发的差异。一星评论使用逻辑否定（no、not），而五星评论使用强调词并强调普遍性（very、highly、every、always）。一星评论使用第一人称复数（we、us、our），而五星评论使用第二人称。一星评论谈论人（manager、waiter、customer），而五星评论谈论甜点以及昂贵餐厅的属性，如菜品和氛围。更多细节参见 Jurafsky 等（2014）。

> Yelp, comparing the words used in 1-star reviews to the words used in 5-star reviews(Jurafsky et al., 2014). The largest difference is in obvious sentiment words, with the 1-star reviews using negative sentiment words like worse, bad, awful and the 5-star reviews using positive sentiment words like great, best, amazing. But there are other illuminating differences. 1-star reviews use logical negation (no, not), while 5-star reviews use emphatics and emphasize universality (very, highly, every, always). 1star reviews use first person plurals (we, us, our) while 5 star reviews use the second person. 1-star reviews talk about people (manager, waiter, customer) while 5-star reviews talk about dessert and properties of expensive restaurants like courses and atmosphere. See Jurafsky et al. (2014) for more details.

> 类别 一星评论中的词 类别 五星评论中的词 负面 worst（最差）、rude（粗鲁）、terrible（糟透了）、horrible（可怕）、bad（差）、 正面 great（很棒）、best（最好）、love(d)（喜爱）、delicious（美味）、amazing（令人惊叹）、
>
> *Class Words in 1-star reviews Class Words in 5-star reviews Negative worst, rude, terrible, horrible, bad, Positive great, best, love(d), delicious, amazing,*

> awful（糟糕）、disgusting（令人作呕）、bland（平淡无味）、tasteless（没有味道）、favorite（最爱）、perfect（完美）、excellent（优秀）、awesome（极好）、gross（恶心）、mediocre（平庸）、overpriced（定价过高）、worse（更差）、friendly（友好）、fantastic（极妙）、fresh（新鲜）、wonderful（绝妙）、inpoor credible、sweet（甜）、yum(my)（好吃）
>
> *awful, disgusting, bland, tasteless, favorite, perfect, excellent, awesome, gross, mediocre, overpriced, worse, friendly, fantastic, fresh, wonderful, inpoor credible, sweet, yum(my)*

> 否定 no（不）、not（不是） 强调词／ 全称词 very（非常）、highly（高度地）、perfectly（完全地）、definitely（确切地）、abso- lutely（绝对地）、everything（一切）、every（每个）、always（总是）
>
> *Negation no, not Emphatics/ very, highly, perfectly, definitely, absouniversals lutely, everything, every, always*

> 第一人称复数代词 we（我们）、us（我们）、our（我们的） 第二人称代词 you（你） 第三人称代词 she（她）、he（他）、her（她）、him（他） 冠词 a、the 过去式动词 was、were、asked、told、said、did、 建议 try、recommend
>
> *1Pl pro we, us, our 2 pro you 3 pro she, he, her, him Articles a, the Past verb was, were, asked, told, said, did, Advice try, recommend*

> charged（收费）、waited（等待）、left（离开）、took（取走）
>
> *charged, waited, left, took*

> 顺序词 after（之后）、then（然后） 连词 also（也）、as（以及）、well（也）、with（和）、and（和） 名词 manager（经理）、waitress（女服务员）、waiter（服务员）、customer（顾客）、 名词 atmosphere（氛围）、dessert（甜点）、chocolate（巧克力）、wine（葡萄酒）、
>
> *Sequencers after, then Conjunct also, as, well, with, and Nouns manager, waitress, waiter, customer, Nouns atmosphere, dessert, chocolate, wine,*

> customers（顾客）、attitude（态度）、waste（浪费）、poisoning（中毒）、course（菜品）、menu（菜单） money（钱）、bill（账单）、minutes（分钟）
>
> *customers, attitude, waste, poisoning, course, menu money, bill, minutes*

> 非现实语气 would（会）、should（应该） 助动词／情态动词 is／’s、can、’ve、are 补语标记词 to、that 介词、其他 in（在……里）、of（……的）、die（死）、city（城市）、mouth（嘴）
>
> *Irrealis would, should Auxiliaries is/’s, can, ’ve, are modals Comp to, that Prep, other in, of, die, city, mouth*

*图 23.12 在一个包含 900,000 条评论的 Yelp 数据集中，使用 Monroe 等人（2008）的方法找出的与一星和五星餐厅评论最相关的前 50 个词（Jurafsky 等，2014）。*
*Figure 23.12 The top 50 words associated with one–star and five-star restaurant reviews in a Yelp dataset of 900,000 reviews, using the Monroe et al. (2008) method (Jurafsky et al., 2014).*

## 23.6 使用词表进行情感识别

> 23.6 Using Lexicons for Sentiment Recognition

在附录 B 中，我们介绍了用于情感分析的朴素贝叶斯算法。本章至此一直关注的这些词表可以有多种用法，用来改进情感识别。

> In Appendix B we introduced the naive Bayes algorithm for sentiment analysis. The lexicons we have focused on throughout the chapter so far can be used in a number of ways to improve sentiment detection.

最简单的情形是：当我们没有足够的训练

> In the simplest case, lexicons can be used when we don’t have sufficient training
数据来构建一个有监督的情感分析器时，可以使用词表；为了训练有监督分类器而让人为每个文档标注情感，往往代价高昂。

> data to build a supervised sentiment analyzer; it can often be expensive to have a human assign sentiment to each document to train the supervised classifier.

在这类情况下，词表可以用于基于规则的分类算法。最简单的版本就是使用正面词与负面词的比例：如果一篇文档中的正面词多于负面词（用词表来判定文档中每个词的极性），就把它分类为正面。通常会使用一个阈值 λ，只有当该比例大于 λ 时，才把文档分类为正面。如果情感词表为每个词都给出了正面权重和负面权重 θ + w 与 θ − w ，这些权重也可以使用。下面是一个这样的简单情感算法：

> In such situations, lexicons can be used in a rule-based algorithm for classification. The simplest version is just to use the ratio of positive to negative words: if a document has more positive than negative words (using the lexicon to decide the polarity of each word in the document), it is classified as positive. Often a threshold λis used, in which a document is classified as positive only if the ratio is greater thanλ. If the sentiment lexicon includes positive and negative weights for each word,θ + w and θ − w , these can be used as well. Here’s a simple such sentiment algorithm:

f + = X
θ + w count(w)
X
f −= θ − w count(w)
if f + + f −> λ

>  if f +  + f −> λ 
sentiment = if f − (23.12)
− f + > λ 0 otherwise.

> − f + > λ   0 otherwise.

> w 满足 w∈positivelexicon
>
> *w s.t. w∈positivelexicon*

> w 满足 w∈negativelexicon
>
> *w s.t. w∈negativelexicon*

如果有有监督训练数据，那么从情感词表计算出的这些计数（有时会以各种方式加权或归一化），也可以与其他词汇特征或非词汇特征一起用作分类器中的特征。我们将在第 23.7 节回到这类算法。

> If supervised training data is available, these counts computed from sentiment lexicons, sometimes weighted or normalized in various ways, can also be used as features in a classifier along with other lexical or non-lexical features. We return to such algorithms in Section 23.7.

## 23.7 使用词表进行态度识别

> 23.7 Using Lexicons for Affect Recognition

情绪检测（以及 Scherer（2000）所描述的其他各类情感含义）可以通过推广上文用于检测情感的算法来实现。

> Detection of emotion (and the other kinds of affective meaning described by Scherer(2000)) can be done by generalizing the algorithms described above for detecting sentiment.

最常见的算法涉及有监督分类：一个训练集被

> The most common algorithms involve supervised classification: a training set is
标注出待检测的情感含义，并使用从训练集中抽取的特征来构建分类器。与情感分析一样，如果训练集足够大，并且测试集与训练集足够相似，那么简单地使用所有词或所有二元组作为特征、放入逻辑回归或 SVM 这类强大的分类器，就是一种性能很难被超越的优秀算法。因此，我们可以把文本样本的情感含义分类当作简单的文档分类来处理。

> labeled for the affective meaning to be detected, and a classifier is built using features extracted from the training set. As with sentiment analysis, if the training set is large enough, and the test set is sufficiently similar to the training set, simply using all the words or all the bigrams as features in a powerful classifier like logistic regression or SVM is an excellent algorithm whose performance is hard to beat. Thus we can treat affective meaning classification of a text sample as simple document classification.

不过，对于非常大的数据集，往往还是需要做一些调整。例如，

> Some modifications are nonetheless often necessary for very large datasets. For
Schwartz 等人（2013）利用 7 亿词的 Facebook 帖子研究人格、性别和年龄时，只使用了长度为 1- 的 n-gram 的一个子集

> example, the Schwartz et al. (2013) study of personality, gender, and age using 700 million words of Facebook posts used only a subset of the n-grams of lengths 1-

- 只有至少被 1% 的被试使用的词和短语才被纳入特征，并且 2-gram 和 3-gram 只有在 PMI 足够高时才保留（PMI 大于 2∗length，其中 length 是词数）：

> Only words and phrases used by at least 1% of the subjects were included as features, and 2-grams and 3-grams were only kept if they had sufficiently high PMI(PMI greater than 2∗length, where length is the number of words):

p(phrase)
pmi(phrase) = log Y (23.13)
p(w)
这些特征可以使用各种权重，包括训练集中的原始计数，或某种归一化概率或对数概率。例如，Schwartz 等人（2013）用每个被试的总用词量对特征计数做归一化，从而把它们转换为短语似然度。

> Various weights can be used for the features, including the raw count in the training set, or some normalized probability or log probability. Schwartz et al. (2013), for example, turn feature counts into phrase likelihoods by normalizing them by each subject’s total word use.

> w∈phrase

freq(phrase,subject)
p(phrase|subject) = X (23.14)
freq(phrase′,subject)
phrase′∈vocab(subject)
如果训练数据更稀疏，或者与测试集不那么相似，那么我们已经讨论过的任何词表都能发挥有益的作用，既可以单独使用，也可以与所有词和 n-gram 结合使用。

> If the training data is sparser, or not as similar to the test set, any of the lexicons we’ve discussed can play a helpful role, either alone or in combination with all the words and n-grams.

词表特征可以采用许多可能的值。最简单的就是一个

> Many possible values can be used for lexicon features. The simplest is just an
指示函数，其中如果某个特定文本含有来自相关词表 L 的任意一个词，特征 fL 的取值就是 1。这里使用附录 B 的记法，即特征值针对特定的输出类别 c 和文档 x 来定义。

> indicator function, in which the value of a feature fL takes the value 1 if a particular text has any word from the relevant lexicon L. Using the notation of Appendix B, in which a feature value is defined for a particular output class c and document x.

1 if ∃w : w ∈L & w ∈x & class = c
fL(c,x) = 0 otherwise
另一种做法是，针对特定词表 L 的特征 fL 的取值，可以是文档中出现在 L 中的词例总数：

> Alternatively the value of a feature fL for a particular lexicon L can be the total number of word tokens in the document that occur in L:

X
fL = count(w)
对于每个词都关联一个得分或权重的词表，该计数可以乘以权重 θ L w：

> For lexica in which each word is associated with a score or weight, the count can be multiplied by a weight θ L w:

> w∈L

X
fL = θ L wcount(w) 计数也可以取对数，或像式 23.14 那样按作者做归一化。

> fL = θ L wcount(w) Counts can alternatively be logged or normalized per writer as in Eq. 23.14.

无论怎样定义，这些词表特征随后都会被用于一个有监督

> However they are defined, these lexicon features are then used in a supervised
分类器，来预测文本或文档所需的情感类别。分类器训练完成后，我们就可以考察哪些词表特征与哪些类别相关联。对于逻辑回归这类分类器，特征权重可以指示该特征与类别的关联程度。

> classifier to predict the desired affective category for the text or document. Once a classifier is trained, we can examine which lexicon features are associated with which classes. For a classifier like logistic regression the feature weight gives an indication of how associated the feature is with the class.

## 23.8 面向以实体为中心的态度词表方法

> 23.8 Lexicon-based methods for Entity-Centric Affect

如果我们想要的不是整篇文档的态度得分，而是文本中某个特定实体的态度得分，该怎么办？Field 与 Tsvetkov（2019）的以实体为中心的方法把态度词表与上下文嵌入结合起来，为文本中的实体赋予态度得分。在针对人的态度这一语境下，他们把效价/唤醒度/支配度这一维度重新命名为情感/能动性/权力。该算法首先训练分类器，把嵌入映射为得分：

> What if we want to get an affect score not for an entire document, but for a particular entity in the text? The entity-centric method of Field and Tsvetkov (2019) combines affect lexicons with contextual embeddings to assign an affect score to an entity in text. In the context of affect about people, they relabel the Valence/Arousal/Dominance dimension as Sentiment/Agency/Power. The algorithm first trains classifiers to map embeddings to scores:

- 对训练语料中的每个词 w：

> For each word w in the training corpus:

（a）使用现成的预训练编码器（如 BERT）提取一个上下文

> (a) Use off-the-shelf pretrained encoders (like BERT) to extract a contextual
嵌入 e，针对该词出现的每个实例分别提取。不进行额外的微调。

> embedding e for each instance of the word. No additional fine-tuning is done.

（b）对 w 的每个实例的 e 嵌入取平均，得到一个单一的

> (b) Average over the e embeddings of each instance of w to obtain a single
嵌入向量，作为一个训练点 w。

> embedding vector for one training point w.

（c）使用 NRC VAD 词表获取 w 的 S、A、P 得分。

> (c) Use the NRC VAD Lexicon to get S, A, and P scores for w.

- 对所有词 w 训练（三个）回归模型，由词的平均嵌入预测 V、A、D 得分。

> Train (three) regression models on all words w to predict V, A, D scores from a word’s average embedding.

现在，给定文本中的一个实体提及 m，我们按如下方式赋予态度得分：

> Now given an entity mention m in a text, we assign affect scores as follows:

- 使用同一个预训练语言模型获取 m 在上下文中的上下文嵌入。
- 把该嵌入输入这 3 个回归模型，得到该实体的 S、A、P 得分。

> Use the same pretrained LM to get contextual embeddings for m in context.
> Feed this embedding through the 3 regression models to get S, A, P scores for the entity.

这样就为给定的实体提及得到一个 (S,A,P) 元组；要得到某个实体在整篇文档中的表示所对应的得分，我们可以进行共指消解，并对所有提及的 (S,A,P) 得分取平均。图 23.13 展示了他们的算法在维基百科剧情摘要文本上、使用金标准共指时为电影《黑暗骑士》（The Dark Knight）中的人物算出的得分。

> This results in a (S,A,P) tuple for a given entity mention; To get scores for the representation of an entity in a complete document, we can run coreference resolution and average the (S,A,P) scores for all the mentions. Fig. 23.13 shows the scores from their algorithm for characters from the movie The Dark Knight when run on Wikipedia plot summary texts with gold coreference.

## 23.9 内涵框架

> 23.9 Connotation Frames

我们迄今描述的词表都把词定义为情感空间中的一个点。而一个

> The lexicons we’ve described so far define a word as a point in affective space. A

> `connotation frame`（内涵框架）
>
> 释义：一种把情感词表与框架语义词表结合构建的词表，用来刻画谓词对其各个论元在情感、价值、权势等方面的表达。

内涵框架则相反，它是一种纳入了更丰富语法结构的词表，做法是把情感词表与第 22 章的框架语义词表结合起来。内涵框架词表的基本洞见是：像动词这样的谓词会表达有关该动词各论元的内涵（Rashkin et al. 2016, Rashkin et al. 2017）。

> connotation frame, by contrast, is a lexicon that incorporates a richer kind of grammatical structure, by combining affective lexicons with the frame semantic lexicons of Chapter 22. The basic insight of connotation frame lexicons is that a predicate like a verb expresses connotations about the verb’s arguments (Rashkin et al. 2016, Rashkin et al. 2017).

请看下面这样的句子：

> Consider sentences like:

（23.15）A 国侵犯了 B 国的主权

> (23.15) Country A violated the sovereignty of Country B

![](images/23-lexicons-sentiment/fig_p18_1.png)

*图 23.13 由在 NRC VAD 词表上训练的嵌入计算出的电影《黑暗骑士》（The Dark Knight）中各人物的权力（支配度）、情感（效价）与能动性（唤醒度）。*
*Figure 23.13 Power (dominance), sentiment (valence) and agency (arousal) for characters in the movie The Dark Knight computed from embeddings trained on the NRC VAD Lexicon.*

> 注意，主角（蝙蝠侠）与反派（小丑）的权力和能动性得分都很高，但情感得分不同；而恋人 Rachel 的权力和能动性得分低，情感得分却很高。
>
> *Note the protagonist (Batman) and the antagonist (the Joker) have high power and agency scores but differ in sentiment, while the love interest Rachel has low power and agency but high sentiment.*

（23.16）那名少年……从波士顿马拉松爆炸案中幸存下来”

> (23.16) the teenager ... survived the Boston Marathon bombing”

通过使用（23.15）中的动词 violate，作者表达了对 B 国的同情，把 B 国描绘成受害者，并表达了对施事方 A 国的敌意。相比之下，（23.16）的作者使用动词 survive，表达的是这次爆炸是一次负面经历，而句子的主语——那名少年——是一个令人同情的角色。这些内涵方面的特征内在于动词 violate 与 survive 的意义之中，如图 23.14 所示。

> By using the verb violate in (23.15), the author is expressing their sympathies with Country B, portraying Country B as a victim, and expressing antagonism toward the agent Country A. By contrast, in using the verb survive, the author of (23.16) is expressing that the bombing is a negative experience, and the subject of the sentence, the teenager, is a sympathetic character. These aspects of connotation are inherent in the meaning of the verbs violate and survive, as shown in Fig. 23.14.

![](images/23-lexicons-sentiment/fig_p18_0.png)

*图 23.14 survive 与 violate 的内涵框架。(a) 对于 survive，作者和读者对 Role1（主语）持正面情感，对 Role2（直接宾语）持负面情感。(b) 对于 violate，作者和读者则对 Role2（直接宾语）持正面情感。*
*Figure 23.14 Connotation frames for survive and violate. (a) For survive, the writer and reader have positive sentiment toward Role1, the subject, and negative sentiment toward Role2, the direct object. (b) For violate, the writer and reader have positive sentiment instead toward Role2, the direct object.*

Rashkin 等人（2016）和 Rashkin 等人的内涵框架词表

> The connotation frame lexicons of Rashkin et al. (2016) and Rashkin et al.
（2017）还表达了谓词对每个论元的其他内涵方面，包括效应（某事坏的事情发生在 x 身上）、价值（x 是有价值的）和心智状态（x 因该事件而痛苦）。内涵框架还可以标注论元之间的权力差异（使用动词 implore 意味着主题论元比施事论元拥有更大的权力），以及每个论元的能动性（waited 的能动性较低）。图 23.15 给出了 Sap 等人（2017）的一个可视化结果。

> (2017) also express other connotative aspects of the predicate toward each argument, including the effect (something bad happened to x) value: (x is valuable), and mental state: (x is distressed by the event). Connotation frames can also mark the power differential between the arguments (using the verb implore means that the theme argument has greater power than the agent), and the agency of each argument(waited is low agency). Fig. 23.15 shows a visualization from Sap et al. (2017).

内涵框架可以手工构建（Sap et al., 2017），也可以通过有监督学习

> Connotation frames can be built by hand (Sap et al., 2017), or they can be learned
得到（Rashkin et al., 2016），例如使用人工标注的训练

> by supervised learning (Rashkin et al., 2016), for example using hand-labeled train-

![](images/23-lexicons-sentiment/fig_p19_0.png)

*图 23.15 Sap 等人（2017）的内涵框架，显示动词 implore 意味着施事的权力低于主题（与之相对，例如动词 demanded 那样的词），并显示 waited 的主语具有较低的能动性水平。图取自 Sap 等人（2017）。*
*Figure 23.15 The connotation frames of Sap et al. (2017), showing that the verb implore implies the agent has lower power than the theme (in contrast, say, with a verb like demanded), and showing the low level of agency of the subject of waited. Figure from Sap et al. (2017).*

数据，为每一条单独的关系训练分类器，例如判断 S(writer →Role1) 是 + 还是 -，然后通过跨所有关系的全局约束来提高准确率。

> ing data to supervise classifiers for each of the individual relations, e.g., whether S(writer →Role1) is + or -, and then improving accuracy via global constraints across all relations.

## 23.10 小结

> 23.10 Summary

- 可以区分出许多种情感状态，包括情绪、心境、态度（其中包含情感）、人际立场和人格。
- 情绪可以用通常称为基本情绪的固定原子单元来表示，也可以表示为由效价、唤醒度等维度所定义的空间中的点。
- 词具有与这些情感状态相关的内涵方面，而词义的这一内涵方面可以用词表来表示。
- 情感词表可以手工构建，即借助众包来标注每个词的情感内容。
- 词表也可以用半监督方式构建，即借助嵌入余弦这类相似度度量，从种子词出发进行自举。
- 当能在现实世界中找到便利的训练信号时，例如评论网站上用户给出的评分，词表可以以完全有监督的方式学习得到。
- 利用训练文本中词频的各种函数，以及诸如对数几率比信息狄利克雷先验这样的比值度量，可以为词在词表中赋予权重。
- 与情感一样，态度也可以使用标准的有监督文本分类技术来检测，即以文本中的所有词或二元组作为特征。

> Many kinds of affective states can be distinguished, including emotions, moods, attitudes (which include sentiment), interpersonal stance, and personality.
> Emotion can be represented by fixed atomic units often called basic emotions, or as points in space defined by dimensions like valence and arousal.
> Words have connotational aspects related to these affective states, and this connotational aspect of word meaning can be represented in lexicons.
> Affective lexicons can be built by hand, using crowd sourcing to label the affective content of each word.
> Lexicons can be built with semi-supervised, bootstrapping from seed words using similarity metrics like embedding cosine.
> Lexicons can be learned in a fully supervised manner, when a convenient training signal can be found in the world, such as ratings assigned by users on a review site.
> Words can be assigned weights in a lexicon by using various functions of word counts in training texts, and ratio metrics like log odds ratio informative Dirichlet prior.
> Affect can be detected, just like sentiment, by using standard supervised text classification techniques, using all the words or bigrams in a text as features.

还可以从词表中词的出现次数抽取额外的特征。

> Additional features can be drawn from counts of words in lexicons.

- 词表也可以用于基于规则的分类器来检测态度，方法是根据各个词表中词的出现次数选取简单多数情感。
- 内涵框架表达了谓词就其论元所编码的更丰富的情感含义关系。

> Lexicons can also be used to detect affect in a rule-based classifier by picking the simple majority sentiment based on counts of words in each lexicon.
> Connotation frames express richer relations of affective meaning that a predicate encodes about its arguments.

## 历史注记

> Historical Notes

形式化地表示词的主观含义这一想法始于 Osgood 等人（1957），这项开创性研究也首次提出了第 5 章所述的词义向量空间模型。Osgood 等人（1957）让参与者按各种量表对词评分，并对评分结果做因子分析。他们发现的最重要的因子是评价性维度，它把 good/bad、valuable/worthless、pleasant/unpleasant 这样的词对区分开来。这项工作影响了内容分析领域早期情感与情感含义词典的发展（Stone et al., 1966）。

> The idea of formally representing the subjective meaning of words began with Osgood et al. (1957), the same pioneering study that first proposed the vector space model of meaning described in Chapter 5. Osgood et al. (1957) had participants rate words on various scales, and ran factor analysis on the ratings. The most significant factor they uncovered was the evaluative dimension, which distinguished between pairs like good/bad, valuable/worthless, pleasant/unpleasant. This work influenced the development of early dictionaries of sentiment and affective meaning in the field of content analysis (Stone et al., 1966).

Wiebe（1994）开启了一条颇具影响力的研究路线，即检测文本中的主观性，

> Wiebe (1994) began an influential line of work on detecting subjectivity in text,

> `subjectivity`（主观性）
>
> 释义：文本表达作者私人状态（如看法、信念、态度）而非仅陈述客观事实的属性，是主观性检测任务要识别的目标。

其起点是识别主观句，以及文本中被描述为持有私人状态、信念或态度的主观人物。

> beginning with the task of identifying subjective sentences and the subjective characters who are described in the text as holding private states, beliefs or attitudes.

像 Hatzivassiloglou 与 McKeown（1997）的极性词表这样学习得到的情感词表，被证明是主观性检测中的一个有用特征（Hatzivassiloglou and Wiebe 2000, Wiebe 2000）。

> Learned sentiment lexicons such as the polarity lexicons of Hatzivassiloglou and McKeown (1997) were shown to be a useful feature in subjectivity detection (Hatzivassiloglou and Wiebe 2000, Wiebe 2000).

「情感」这一术语似乎是由 Das 与 Chen 于 2001 年引入的

> The term sentiment seems to have been introduced in 2001 by Das and Chen
（2001），用以描述通过考察股票交易留言板中的词语来度量市场情感这一任务。在同一篇论文中，Das 与 Chen（2001）还提出了使用情感词表。该词表中的词语清单是手工编制的，但每个词都被赋予权重，权重取决于它区分某一特定类别（比如买入与卖出）的程度，其做法是最大化类间差异并最小化类内差异。情感这一术语以及对词表的使用很快流行开来（例如，除其他外，Turney 2002）。Pang 等人（2002）首次展示了不使用情感词表而直接使用全部词语的力量；另见 Wang 与 Manning（2012）。

> (2001), to describe the task of measuring market sentiment by looking at the words in stock trading message boards. In the same paper Das and Chen (2001) also proposed the use of a sentiment lexicon. The list of words in the lexicon was created by hand, but each word was assigned weights according to how much it discriminated a particular class (say buy versus sell) by maximizing across-class variation and minimizing within-class variation. The term sentiment, and the use of lexicons, caught on quite quickly (e.g., inter alia, Turney 2002). Pang et al. (2002) first showed the power of using all the words without a sentiment lexicon; see also Wang and Manning (2012).

我们在扩展情感词典时所描述的大多数半监督方法，都源自一个早期想法：同义词与反义词倾向于在同一句子中共现（Miller 与 Charles 1991，Justeson 与 Katz 1991，Riloff 与 Shepherd 1997）。其他用于学习情感含义线索的半监督方法则依赖信息抽取技术，例如 AutoSlog 模式抽取器（Riloff 与 Wiebe，2003）。面向情感的基于图的算法最早由 Hatzivassiloglou 与 McKeown（1997）提出，此后图传播成为一种标准方法（Zhu 与 Ghahramani 2002，Zhu 等人 2003，Zhou 等人 2004a，Velikovich 等人 2010）。众包也可用于提高精确率，办法是对半监督词表学习的结果进行过滤（Riloff 与 Shepherd 1997，Fast 等人 2016）。

> Most of the semi-supervised methods we describe for extending sentiment dictionaries drew on the early idea that synonyms and antonyms tend to co-occur in the same sentence (Miller and Charles 1991, Justeson and Katz 1991, Riloff and Shepherd 1997). Other semi-supervised methods for learning cues to affective meaning rely on information extraction techniques, like the AutoSlog pattern extractors(Riloff and Wiebe, 2003). Graph based algorithms for sentiment were first suggested by Hatzivassiloglou and McKeown (1997), and graph propagation became a standard method (Zhu and Ghahramani 2002, Zhu et al. 2003, Zhou et al. 2004a, Velikovich et al. 2010). Crowdsourcing can also be used to improve precision by filtering the result of semi-supervised lexicon learning (Riloff and Shepherd 1997, Fast et al. 2016).

近期许多工作关注学习能够直接编码情感或其他属性的嵌入的方法，例如 Rothe 等人（2016）的 DENSIFIER 算法，该算法学习对嵌入空间进行变换，使其聚焦于情感（或其他）信息。

> Much recent work focuses on ways to learn embeddings that directly encode sentiment or other properties, such as the DENSIFIER algorithm of Rothe et al. (2016) that learns to transform the embedding space to focus on sentiment (or other) information.

## 习题

> Exercises

23.1 证明 Potts 图中词 w 与类别 c 之间的关系

> 23.1 Show that the relationship between a word w and a category c in the Potts
得分（式 23.6）是不含对数项的点互信息 pmi(w,c) 的一种变体。

> Score in Eq. 23.6 is a variant of the pointwise mutual information pmi(w,c) without the log term.
