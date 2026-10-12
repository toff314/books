# 第 11 章 基于检索的模型

252　第 11 章 • 基于检索的模型

> 252 CHAPTER 11 • RETRIEVAL-BASED MODELS

### 章

> CHAPTER

# 11 信息检索与检索增强生成

> 11 Information Retrieval and Retrieval-Augmented Generation

有人曾两次问我——“请问，巴贝奇先生，如果你把错误的数字输入机器，正确的答案会出来吗？”……我实在无法理解，究竟是怎样一种观念混乱才会引出这样的问题。巴贝奇（1864）

> On two occasions I have been asked,—“Pray, Mr. Babbage, if you put into the machine wrong figures, will the right answers come out?” ... I am not able rightly to apprehend the kind of confusion of ideas that could provoke such a question. Babbage (1864)

人们需要了解各种事情。所以几乎在计算机刚出现时

> People need to know things. So pretty much as soon as there were computers

我们就在向它们提问了。到 1961 年，已经出现了一个系统，可以回答关于美国棒球统计数据的问题，比如“洋基队在 7 月打了多少场比赛？”（Green et al., 1961）。甚至 20 世纪 70 年代的虚构计算机也是如此，例如道格拉斯·亚当斯在《银河系漫游指南》中发明的“深思”（Deep Thought），它回答了“关于生命、宇宙以及一切的终极问题”。1 而由于大量知识都以文本形式编码，早在 LLM 出现之前，系统回答问题的表现就已达到人类水平：IBM 的 Watson 系统于 2011 年赢得了电视问答节目 Jeopardy!，在回答如下这类问题上超过了人类：

> we were asking them questions. By 1961 there was a system to answer questions about American baseball statistics like “How many games did the Yankees play in July?” (Green et al., 1961). Even fictional computers in the 1970s like Deep Thought, invented by Douglas Adams in The Hitchhiker’s Guide to the Galaxy, answered “the Ultimate Question Of Life, The Universe, and Everything”.1 And because so much knowledge is encoded in text, systems were answering questions at human-level performance even before LLMs: IBM’s Watson system won the TV game-show Jeopardy! in 2011, surpassing humans at answering questions like:

> 威廉·威尔金森的《瓦拉几亚和摩尔达维亚诸公国纪行》启发了该作者最著名的小说 2
>
> *WILLIAM WILKINSON’S “AN ACCOUNT OF THE PRINCIPALITIES OF WALLACHIA AND MOLDOVIA”INSPIRED THIS AUTHOR’S MOST FAMOUS NOVEL 2*

于是自然可以推出，大语言模型的一项重要功能就是

> It follows naturally, then, that an important function of large language models is

满足人类的信息需求。而由于大量信息都在网上，找到能满足我们需求的信息与网络信息检索（即搜索引擎所执行的任务）密切相关。事实上，随着现代搜索引擎与大语言模型相集成，两者的界限正变得越来越模糊。

> to fill human information needs. And since a lot of information is online, finding the information that fills our needs is closely related to web information retrieval, the task performed by search engines. Indeed, the distinction is becoming ever more fuzzy, as modern search engines are integrated with large language models.

> 事实型
>
> *factoid*

考虑一些简单的信息需求，例如事实型问题，这类

> Consider some simple information needs, for example factoid questions that

> 问题
>
> *questions*

可以用如下这类简短文本中表述的事实来满足：

> can be met with facts expressed in short texts like the following:

(11.1) 卢浮宫博物馆在哪里？(11.2) 核爆炸中的能量来自哪里？(11.3) 如何在 latex 中得到花体 l？

> (11.1) Where is the Louvre Museum located?(11.2) Where does the energy in a nuclear explosion come from?(11.3) How to get a script l in latex?

要让 LLM 回答这些问题，我们只需向它提示即可！例如，一个

> To get an LLM to answer these questions, we can just prompt it! For example a

在回答问题方面经过指令微调的预训练 LLM（指令微调见第 8 章）可以直接回答下面这个问题

> pretrained LLM that has been instruction-tuned on answering questions (instructiontuning is in Chapter 8) could directly answer the following question

卢浮宫博物馆在哪里？

> Where is the Louvre Museum located?

通过以该前缀为条件进行条件生成，并把响应作为答案。这之所以可行，是因为大语言模型在其预训练数据中处理过大量事实，包括卢浮宫的位置，并把这些信息编码进了它们的参数中。这类事实性知识似乎存储在 transformer 模型极其庞大的前馈层的连接之中（Geva et al., 2021; Meng et al., 2022）。

> by performing conditional generation given this prefix, and take the response as the answer. This works because large language models have processed a lot of facts in their pretraining data, including the location of the Louvre, and have encoded this information in their parameters. Factual knowledge of this type seems to be stored in the connections in the very large feedforward layers of transformer models (Geva et al., 2021; Meng et al., 2022).

> 1

> 答案是 42，但遗憾的是那个问题从未被揭示。
>
> *The answer was 42, but unfortunately the question was never revealed.*

> 2

> 答案当然是“谁是布拉姆·斯托克”，那部小说是《德古拉》。
>
> *The answer, of course, is ‘Who is Bram Stoker’, and the novel was Dracula.*

253

简单地提示 LLM 对许多生成任务都很有用，包括那些

> Simply prompting an LLM is useful for many generation tasks, including those

涉及事实的任务。但知识存储在 LLM 的前馈权重之中这一事实，使得把提示作为正确生成事实性文本或答案的方法会带来若干问题。

> involving facts. But the fact that knowledge is stored in the feedforward weights of the LLM leads to a number of problems with prompting as a method for correctly generating factual texts or answers.

第一个也是主要的问题是，LLM 在生成

> The first and main problem is that LLMs are often incorrect when generating

关于事实的答案或其他文本时常常出错！大语言模型会产生幻觉。幻觉是指不忠实于世界事实的响应。也就是说，当被提问时，大语言模型有时会编造听起来合理的答案。例如，Dahl et al. (2024) 发现，当被问及法律领域的问题（比如关于特定法律案件）时，大语言模型有 69% 到 88% 的情况下会产生幻觉！即使正确的事实就存储在参数中，LLM 有时也会给出错误的事实性回答；这似乎是由于前馈层未能回忆起存储在参数中的知识所致（Jiang et al., 2024）。

> answers or other texts about facts! Large language models hallucinate. A hallucination is a response that is not faithful to the facts of the world. That is, when asked questions, large language models sometimes make up answers that sound reasonable. For example, Dahl et al. (2024) found that when asked questions about the legal domain (like about particular legal cases), large language models hallucinated from 69% to 88% of the time! LLMs sometimes give incorrect factual responses even when the correct facts are stored in the parameters; this seems to be caused by the feedforward layers failing to recall the knowledge stored in their parameters(Jiang et al., 2024).

> 产生幻觉
>
> *hallucinate*

而且并不总能判断出语言模型何时在产生幻觉，

> And it’s not always possible to tell when language models are hallucinating,

部分原因是 LLM 并未得到良好的校准。在一个已校准的系统中，系统对自身答案正确性的

> partly because LLMs aren’t well-calibrated. In a calibrated system, the confidence

> 已校准
>
> *calibrated*

置信度与答案正确的概率高度相关。因此，如果一个已校准的系统出错了，至少它可能会对自己的答案有所保留，或者告诉我们去查另一个来源。但由于语言模型并未得到良好的校准，它们常常以十足的把握给出一个非常错误的答案（Zhou et al., 2024a）。

> of a system in the correctness of its answer is highly correlated with the probability of an answer being correct. So if a calibrated system is wrong, at least it might hedge its answer or tell us to go check another source. But since language models are not well-calibrated, they often give a very wrong answer with complete certainty (Zhou et al., 2024a).

用简单的提示方法来满足用户信息需求的第二个问题

> A second problem with meeting user information needs with simple prompting

是，提示大语言模型从其预训练参数中作答，无法让我们就专有数据提问。我们希望用语言模型来帮助满足涉及专有数据（如个人电子邮件）的用户信息需求。或者，对于医疗健康领域的应用，我们可能想将语言模型应用于病历。又或者，一家公司可能有包含客户服务或内部使用答案的内部文档。再或者，律师事务所需要就专有文档中的法律证据开示提出问题。这些数据（但愿）都不在用于预训练大语言模型的基于网络的大规模语料库中。

> methods is that prompting a large language model to answer from its pretrained parameters doesn’t allow us to ask questions about proprietary data. We would like to use language models to help with user information needs about proprietary data like personal email. Or for the healthcare application we might want to apply a language model to medical records. Or a company may have internal documents that contain answers for customer service or internal use. Or legal firms need to ask questions about legal discovery from proprietary documents. None of this data (hopefully) was in the large web-based corpora that large language models are pretrained on.

用大语言模型回答知识问题的最后一个问题是

> A final issue with using large language models to answer knowledge questions is

它们是静态的；它们只在某个特定时间被预训练过一次。这意味着 LLM 无法谈论快速变化的信息（比如上周发生的某件事），因为它们不会有其发布数据之后的最新信息。

> that they are static; they were pretrained once, at a particular time. This means that LLMs cannot talk about about rapidly changing information (like something that happened last week) since they won’t have up-to-date information from after their release data.

针对用简单提示生成事实性文本所遇到的这全部问题，一个解决方案是为语言模型提供外部知识来源，例如医疗或法律记录、个人电子邮件或公司文档等专有文本，并在回答问题时使用这些文档。这种方法被称为检索增强生成（retrieval-augmented generation），即 RAG，而这就是我们将要重点介绍的

> One solution to all these problems with simple prompting for generating factual text is to give a language model external sources of knowledge, for example proprietary texts like medical or legal records, personal emails, or corporate documents, and to use those documents in answering questions. This method is called retrieval-augmented generation or RAG, and that is the method we will focus on

> RAG

> 信息
>
> *information*

本章的方法。在 RAG 中，我们使用信息检索（information retrieval，IR）技术来检索

> in this chapter. In RAG we use information retrieval (IR) techniques to retrieve

> 检索
>
> *retrieval*

那些可能包含有助于回答该问题信息的文档。

> documents that are likely to have information that might help answer the question.

然后我们使用大语言模型，在这些文档的基础上生成答案。

> Then we use a large language model to generate an answer given these documents.

把答案建立在检索到的文档之上，可以解决

> Basing our answers on retrieved documents can solve some of the problems with

使用简单提示来回答问题所带来的一些问题。首先，它有助于确保答案立足于某个精选数据集中的事实。而且系统可以在给出答案的同时，附上答案所来源的段落或文档的上下文。这些信息可以帮助用户对答案的准确性建立信心（也可以帮助他们发现答案何时是错的！）。此外，这些检索技术可以用于我们想要的任何专有数据，例如面向这些应用的法律或医疗数据。

> using simple prompting to answer questions. First, it helps ensure that the answer is grounded in facts from some curated dataset. And the system can give the user the answer accompanied by the context of the passage or document it came from. This information can help users have confidence in the accuracy of the answer (or help them spot when it is wrong!). And these retrieval techniques can be used on any proprietary data we want, such as legal or medical data for those applications.

254 第 11 章 • 基于检索的模型

> 254 CHAPTER 11 • RETRIEVAL-BASED MODELS

我们将首先介绍信息检索，即在给定用户表达其信息需求的查询时，

> We’ll begin by introducing information retrieval, the task of choosing the most

从文档集中选出最相关文档的任务。我们将看到基于稀疏 tf-idf 向量余弦的经典方法，以及现代神经“稠密”检索器，后者改为用 BERT 或其他语言模型对查询和文档进行神经表示。接着我们介绍检索增强生成范式。

> relevant document from a document set given a user’s query expressing their information need. We’ll see the classic method based on cosines of sparse tf-idf vectors, modern neural ‘dense’ retrievers based on instead representing queries and documents neurally with BERT or other language models. We then introduce the retrieval-augmented generation paradigm.

最后，我们将讨论各种包含问题与答案的数据集，它们可以

> Finally, we’ll discuss various datasets with questions and answers that can be

用于在指令微调中微调 LLM，以及用作评估的基准。

> used for fine-tuning LLMs in instruction tuning and for use as benchmarks for evaluation.

## 11.1 信息检索

> 11.1 Information Retrieval

> 信息
>
> *information*

信息检索（information retrieval，IR）是涵盖基于用户信息需求检索

> Information retrieval or IR is the name of the field encompassing the retrieval of

> 检索
>
> *retrieval*

各种媒体的领域的名称。由此得到的 IR 系统

> all manner of media based on user information needs. The resulting IR system is

> IR

通常被称为搜索引擎。本节的目标是对 IR 给出充分的概述，以便看清它在满足用户信息需求的大语言模型中的应用。

> often called a search engine. Our goal in this section is to give a sufficient overview of IR to see its application to large language models meeting user information needs.

对信息检索本身有更多兴趣的读者，应参阅本章末尾的历史注记一节。

> Readers with more interest specifically in information retrieval should see the Historical Notes section at the end of the chapter.

我们考虑的 IR 任务称为即席检索（ad hoc retrieval），其中用户向

> The IR task we consider is called ad hoc retrieval, in which a user poses a

> 即席检索
>
> *ad hoc retrieval*

检索系统提出查询，系统随后从某个集合中返回一个有序的文档集合。文档（document）指系统所索引

> query to a retrieval system, which then returns an ordered set of documents from some collection. A document refers to whatever unit of text the system indexes

> 文档
>
> *document*

和检索的任何文本单位（网页、科学论文、新闻文章，甚至像段落这样更短的片段）。集合（collection）指用于满足

> and retrieves (web pages, scientific papers, news articles, or even shorter passages like paragraphs). A collection refers to a set of documents being used to satisfy

> 集合
>
> *collection*

用户请求的一组文档。集合可以指整个网络，此时我们做的是网络搜索。但集合也可以是一个较小的企业仓库，甚至是一组

> user requests. A collection can mean the entire web, in which case we are doing web search. But a collection can also be a smaller corporate repo, or even a set of

> 网络搜索
>
> *web search*

供一个人使用的文档。词项（term）指集合中的一个词，但它也可能

> documents used by one person. term refers to a word in a collection, but it may also

> 词项
>
> *term*

包括短语。最后，查询（query）表示用户以

> include phrases. Finally, a query represents a user’s information need expressed as

> 查询
>
> *query*

一组词项表达的信息需求。

> a set of terms.

| 文档<br>文档 文档<br>文档文档 处理 搜索<br>索引<br>文档文档 & 索引<br>文档 文档 文档<br>最大化：Do Dc ou cm ue mn et nt<br>文档集合 文档 Do Dc ou cm Rue man et nnkted<br>文档<br>相关性<br>得分<br>查询 查询<br>查询<br>处理 向量<br>Document<br>Document Document<br>DocumenDtocument Processing Search<br>Index<br>DocumeDntocument & Indexing<br>Document Document Document<br>Maximize: Do Dc ou cm ue mn et nt<br>document collection Document Do Dc ou cm Rue man et nnkted<br>Documents<br>Relevance<br>Score<br>Query Query<br>query<br>Processing Vector |  |
| --- | --- |
| 图 11.1<br>Figure 11.1 | 即席 IR 系统的架构。文档排序基于为以下对象计算得分<br>The architecture of an ad hoc IR system. Document ranking is based on computing a score for |

![](images/img_89.png)

|  |  |  | 文档<br>Document |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 文档<br>Docume |  |  |  |
|  | 文档<br>me | 文档<br>nDto | 文档<br>cu | 文档<br>me | 文档<br>nt |  |

![](images/img_81.png)

![](images/img_89.png)

![](images/img_91.png)

![](images/img_89.png)

> 处理 文档
>
> *Processing Document*

![](images/img_83.png)

![](images/img_89.png)

![](images/img_89.png)

搜索

> Search

> & 索引 索引
>
> *& Indexing Index*

![](images/img_89.png)

![](images/img_89.png)

![](images/img_85.png)

![](images/img_85.png)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |
| t |  |  |  |

![](images/img_85.png)

![](images/img_85.png)

最大化：

> Maximize:

![](images/img_85.png)

![](images/img_87.png)

> 文档集合
>
> *document collection*

> 已排序文档
>
> *Ranked Documents*

相关性得分

> Relevance Score

![](images/img_79.png)

![](images/img_93.png)

> 查询 查询
>
> *Query Query*

查询

> query

> 处理 向量
>
> *Processing Vector*

> 针对给定查询的每个候选文档，表达它可能有多相关，以满足用户的信息需求。信息检索（IR）系统有两类，它们基于用于表示查询和文档的两类向量：稀疏向量和稠密向量。这两类检索在索引与打分机制的细节上有所不同。
>
> *each candidate document given the query, expressing how relevant it is likely to be to meet the users information need. There are two classes of IR systems, based on the two classes of vectors that are used to represent queries and documents: sparse vectors and dense vectors. These two kinds of retrieval differ in the details of the indexing and scoring mechanisms.*

即席检索（ad hoc retrieval）引擎的高层架构如图 11.1 所示。

> The high-level architecture of an ad hoc retrieval engine is shown in Fig. 11.1.

该图对两类 IR 系统作了抽象，这两类系统基于用于表示查询和文档的两类向量：稀疏向量和稠密向量。在稀疏检索中，我们用计数向量表示文档和查询，并以 tf-idf 或 BM25 加权。在稠密检索中，我们用嵌入（embedding）表示 11.1 • 信息检索 255 文档和查询，嵌入由语言模型（编码器模型或解码器模型）计算得到。我们将在本节余下部分讨论稀疏检索，并在 11.3 节转向稠密检索。

> This figure abstracts over the two classes of IR systems, which are based on the two classes of vectors that are used to represent queries and documents: sparse vectors and dense vectors. In sparse retrieval, we represent documents and queries with count vectors, weighted by tf-idf or BM25. In dense retrieval, we represent 11.1 • INFORMATION RETRIEVAL 255 documents and queries with embeddings, computed from language models (either encoder or decoder models). We’ll discuss sparse retrieval in the rest of this section, and turn to dense retrieval in Section 11.3.

### 11.1.1 将文档表示为向量

> 11.1.1 Representing documents as vectors

> 向量空间
>
> *vector space*

在信息检索的向量空间模型（Salton, 1971）中，文档被

> In the vector space model of information retrieval (Salton, 1971) a document is

> 模型
>
> *model*

表示为一个对其所含词语进行计数的向量。

> represented as a vector of counts of the words it contains.

我们有时把这类模型称为词袋（bag-of-words）模型。图 11.2 展示了

> We sometimes call this kind of model a bag-of-words model. Fig. 11.2 shows

其直观含义：我们把一个文本文档表示为仿佛一袋词语，

> the intuition: we are representing a text document as if it were a bag of words,

> 词袋
>
> *bag of words*

也就是说，一个无序的词语集合，其位置被忽略，只保留它们在文档中的频次。在图中这个例子里，我们不去表示像“It manages to be whimsical and romantic”这类短语中的词序，而只记录单词 it 在整个摘录中出现了 5 次，love、recommend 和 movie 各出现 1 次，等等。

> that is, an unordered set of words with their position ignored, keeping only their frequency in the document. In the example in the figure, instead of representing the word order in all the phrases like “It manages to be whimsical and romantic”, we simply note that the word it occurred 5 times in the entire excerpt, the words love, recommend, and movie once, and so on.

|  |  |
| --- | --- |
| 冒险 1<br>和 3<br>仙子 1<br>我爱这部电影！它很甜美，<br>仙子 它 类型 1<br>但带有讽刺幽默。The always loveto<br>它 很棒 1<br>对白 很棒 和 the 奇妙 它 我<br>冒险 场景 很有趣... 和 看过 是 任何人 有 1<br>它 设法 变得 奇妙 frien hd appy 对白 幽默 1<br>推荐 我 5<br>和 浪漫 同时 欢笑 冒险<br>在 the 常规 of the whosweet of msa ot vir ieical it i st 6<br>atirical 1<br>f ra ei cry mta mle g ne dn ir e to. I uw so u ald sevi et raI butto yr eo tmantic I seen 2<br>o e t j t b out l<br>任何人。我 已经 看过 它 数次 再次 它 the 幽默 甜美 1<br>the 看过 会 the 4<br>次，而且 我 总是 乐于 场景 我 themanages 次 1<br>再次 看到 它 每当 我 the<br>有 一个 朋友 谁 还没有 有趣 我 和 次 和 to 3<br>看过 它 还！每当 关于 同时 奇妙 1<br>有 会 1<br>常规<br>与 还 1<br>… …<br>adventure 1<br>and 3<br>fairy 1<br>I love this movie! It's sweet,<br>fairy it genre 1<br>but with satirical humor. The always loveto<br>it great 1<br>dialogue is great and the whimsical it I<br>adventure scenes are fun... and seen are anyone have 1<br>It manages to be whimsical frien hd appy dialogue humor 1<br>recommend I 5<br>and romantic while laughing adventure<br>at the conventions of the whosweet of msa ot vir ieical it i st 6<br>atirical 1<br>f ra ei cry mta mle g ne dn ir e to. I uw so u ald sevi et raI butto yr eo tmantic I seen 2<br>o e t j t b out l<br>anyone. I've seen it several again it the humor sweet 1<br>the seen would the 4<br>times, and I'm always happy to scenes I themanages times 1<br>to see it again whenever I the<br>have a friend who hasn't fun I and times and to 3<br>seen it yet! whenever about while whimsical 1<br>have would 1<br>conventions<br>with yet 1<br>… … |  |
|  |  |
| 图 11.2<br>Figure 11.2 | 经典向量空间模型应用于单个文档的直观示意。词在文档中的位置<br>Intuition of the classic vector space model applied to a single document. The position of the |

> 冒险 1 和 3
>
> *adventure 1 and 3*

> 仙子 1
>
> *fairy 1*

> 我爱这部电影！它很甜美，
>
> *I love this movie! It's sweet,*

> 仙子 总是 爱 它 类型 1
>
> *fairy always love it genre 1*

> 但带有讽刺幽默。The to
>
> *but with satirical humor. The to*

> 它 奇妙 它 很棒 1
>
> *it whimsical it great 1*

> 对白 很棒 和 the 我
>
> *dialogue is great and the I*

> 和 看过 是任何人 有 1
>
> *and seen areanyone have 1*

> 冒险 场景 很有趣... 朋友
>
> *adventure scenes are fun... friend*

> 对白 幽默 1
>
> *dialogue humor 1*

> 它 设法 变得 奇妙 快乐
>
> *It manages to be whimsical happy*

> 推荐 我 5
>
> *recommend I 5*

> 和 浪漫 同时 欢笑 冒险
>
> *and romantic while laughing adventure*

> 甜美 of 讽刺 它 6
>
> *sweet of satirical it 6*

> 在 the 常规 of the who 它
>
> *at the conventions of the who it*

> 我 to 电影 讽刺 1
>
> *I to movie satirical 1*

> 仙子 故事 类型。我 会 它 但 浪漫 我
>
> *fairy tale genre. I would it but romantic I*

> 还 看过 2
>
> *yet seen 2*

> 推荐 它 to 几乎 大约 数个 幽默
>
> *recommend it to just about several humor*

> 再次 它 the 甜美 1
>
> *again it the sweet 1*

> 任何人。我 已经 看过 它 数次 the
>
> *anyone. I've seen it several the*

> 看过 会 the 4
>
> *seen would the 4*

> 次，而且 我 总是 乐于 场景 我
>
> *times, and I'm always happy to scenes I*

> 该 管理 次数 1
>
> *the manages times 1*

> 再次看到它 每当 我 该
>
> *to see it again whenever I the*

> 有趣 我 次数 和 到 3
>
> *fun I times and to 3*

> 有一个还没有的朋友 并且 关于
>
> *have a friend who hasn't and about*

> 而 异想天开的 1
>
> *while whimsical 1*

> 见过它了！每当 有
>
> *seen it yet! whenever have*

> 会 1
>
> *would 1*

> 惯例 与 还 1
>
> *conventions with yet 1*

> … …

> 单词被忽略（词袋假设），并且我们利用每个单词的频率。
>
> *words is ignored (the bag-of-words assumption) and we make use of the frequency of each word.*

因此我们可以设想把图 11.2 中的文档表示为向量 [1 3

> We could thus imagine representing the document in Fig. 11.2 as the vector [1 3

1 1 1 1 1 5 6 1 2 1 4 1 3 1 1 1]（如果我们把自己限制在这 18 个维度上，并忽略英语中所有其他的单词）。

> 1 1 1 1 1 5 6 1 2 1 4 1 3 1 1 1] (if we limited ourselves to these 18 dimensions and ignored all the other words in English).

更一般地，我们可以把一组文档表示为一个词项-文档矩阵（term-document matrix），其中每一行表示词汇表中的一个单词，而每一列表-

> More generally, we can represent a set of documents as a term-document matrix in which each row represents a word in the vocabulary and each column rep-

> 词项-文档
>
> *term-document*

> 矩阵
>
> *matrix*

示某个文档集合中的一个文档。图 11.3 展示了词项-文档矩阵中的一个小片段，其中显示四个单词在莎士比亚的四部戏剧中的出现情况。该矩阵中的每个单元格表示某个特定单词（由行定义）在某个特定文档（由列定义）中出现的次数。因此 fool 在《第十二夜》中出现了 58 次。

> resents a document from some collection of documents. Fig. 11.3 shows a small selection from a term-document matrix showing the occurrence of four words in four plays by Shakespeare. Each cell in this matrix represents the number of times a particular word (defined by the row) occurs in a particular document (defined by the column). Thus fool appeared 58 times in Twelfth Night.

一个文档被表示为一个计数向量，即图 11.4 中的一列。在

> A document is represented as a count vector, a column in Fig. 11.4. In the

图 11.4 的例子中，我们选择把文档向量的维度设为 4，只是为了它们能排在页面上；在真实的词项-文档矩阵中，文档向量的维度会是 |V|，即词汇表的大小。这两个向量的第一个维度都对应于单词 battle 出现的次数，而我们可以 256 第 11 章 • 基于检索的模型

> example in Fig. 11.4, we’ve chosen to make the document vectors of dimension 4, just so they fit on the page; in real term-document matrices, the document vectors would have dimensionality |V|, the vocabulary size. The first dimension for both these vectors corresponds to the number of times the word battle occurs, and we can 256 CHAPTER 11 • RETRIEVAL-BASED MODELS

> 《皆大欢喜》 《第十二夜》 《裘力斯·凯撒》 《亨利五世》
>
> *As You Like It Twelfth Night Julius Caesar Henry V*

| 《皆大欢喜》 《第十二夜》 《裘力斯·凯撒》 《亨利五世》<br>As You Like It Twelfth Night Julius Caesar Henry V |  |
| --- | --- |
| battle 1 0 7 13<br>good 114 80 62 89<br>fool 36 58 1 4<br>wit 20 15 2 3 |  |
| 图 11.3<br>Figure 11.3 | 四个单词在四部莎士比亚戏剧中的词项-文档矩阵。每个<br>The term-document matrix for four words in four Shakespeare plays. Each |

> battle 1 0 7 13 good 114 80 62 89 fool 36 58 1 4 wit 20 15 2 3

> 单元格包含（行）单词在（列）文档中出现的次数。
>
> *cell contains the number of times the (row) word occurs in the (column) document.*

比较每个维度，例如注意《皆大欢喜》和《第十二夜》的向量在第一个维度上具有相似的值（分别为 1 和 0）。

> compare each dimension, noting for example that the vectors for As You Like It and Twelfth Night have similar values (1 and 0, respectively) for the first dimension.

| 《皆大欢喜》 《第十二夜》 《裘力斯·凯撒》 《亨利五世》<br>battle 1 0 7 13<br>good 114 80 62 89<br>fool 36 58 1 4<br>wit 20 15 2 3<br>图 11.4 四个单词在四部莎士比亚戏剧中的词项-文档矩阵。红<br>框表明每个文档都被表示为一个长度为四的列向量。<br>由于四维空间难以可视化，图 11.5 展示了四个文档向量在二维空间中的可视<br>化；我们任意选取了<br>对应于单词 battle 和 fool 的维度。<br>40<br>《亨利五世》[4,13]<br>15<br>battle<br>10 《裘力斯·凯撒》[1,7]<br>5 《皆大欢喜》[36,1] 《第十二夜》[58,0]<br>5 10 15 20 25 30 35 40 45 50 55 60<br>fool<br>图 11.5 四部莎士比亚戏剧<br>文档的文档向量的空间可视化，仅展示其中两个维度，分别对应单词 battle 和<br>喜剧在 fool 维度上取值高，在 battle 维度上取值低<br>两个相似的文档往往具有相似的单词，而如果两个<br>文档具有相似的单词，它们的列向量也往往相似。向量<br>对于喜剧《皆大欢喜》[1,114,36,20] 和《第十二夜》[0,80,58,15] 看<br>彼此更像（傻子和机智多于战斗），而不太像《裘<br>力斯·凯撒》[7,62,1,2] 或《亨利五世》[13,89,4,3]。<br>11.1.2 词项加权：tf-idf 与 BM25<br>As You Like It Twelfth Night Julius Caesar Henry V<br>battle 1 0 7 13<br>good 114 80 62 89<br>fool 36 58 1 4<br>wit 20 15 2 3<br>Figure 11.4 The term-document matrix for four words in four Shakespeare plays. Th<br>boxes show that each document is represented as a column vector of length four.<br>Since 4-dimensional spaces are hard to visualize, Fig. 11.5 shows a visua<br>tion of the four document vectors in two dimensions; we’ve arbitrarily chosen<br>dimensions corresponding to the words battle and fool.<br>40<br>Henry V [4,13]<br>15<br>battle<br>10 Julius Caesar [1,7]<br>5 As You Like It [36,1] Twelfth Night [58,0]<br>5 10 15 20 25 30 35 40 45 50 55 60<br>fool<br>Figure 11.5 A spatial visualization of the document vectors for the four Shakespeare<br>documents, showing just two of the dimensions, corresponding to the words battle and<br>The comedies have high values for the fool dimension and low values for the battle dimen<br>Two documents that are similar will tend to have similar words, and if two<br>uments have similar words their column vectors will tend to be similar. The vec<br>for the comedies As You Like It [1,114,36,20] and Twelfth Night [0,80,58,15] lo<br>lot more like each other (more fools and wit than battles) than they look like Ju<br>Caesar [7,62,1,2] or Henry V [13,89,4,3].<br>11.1.2 Term weighting: tf-idf and BM25 |  |  |
| --- | --- | --- |
|  | 《皆大欢喜》 《第十二夜》 《裘力斯·凯撒》 《亨利五世》<br>As You Like It Twelfth Night Julius Caesar Henry V |  |
|  | battle 1 0 7 13<br>good 114 80 62 89<br>fool 36 58 1 4<br>wit 20 15 2 3 |  |
|  | 图 11.4<br>Figure 11.4 | e 红色<br>化-<br>该<br>e red<br>liza-<br>the |
|  | 40<br>《亨利五世》[4,13]<br>15<br>battle<br>10 《裘力斯·凯撒》[1,7]<br>5 《皆大欢喜》[36,1] 《第十二夜》[58,0]<br>5 10 15 20 25 30 35 40 45 50 55 60<br>fool<br>40<br>Henry V [4,13]<br>15<br>battle<br>10 Julius Caesar [1,7]<br>5 As You Like It [36,1] Twelfth Night [58,0]<br>5 10 15 20 25 30 35 40 45 50 55 60<br>fool |  |
|  | 图 11.5<br>Figure 11.5 | 剧<br>fool。<br>维。<br>档-<br>量<br>看 一<br>斯<br>play<br>fool.<br>sion.<br>doc-<br>tors<br>ok a<br>lius |

> 《皆大欢喜》 《第十二夜》 《裘力斯·凯撒》 《亨利五世》
>
> *As You Like It Twelfth Night Julius Caesar Henry V*

> battle 1 0 7 13 good 114 80 62 89 fool 36 58 1 4 wit 20 15 2 3 图 11.4 四个单词在四部莎士比亚戏剧中的词项-文档矩阵。红色方框表明每个文档都被表示为一个长度为四的列向量。
>
> *battle 1 0 7 13 good 114 80 62 89 fool 36 58 1 4 wit 20 15 2 3 Figure 11.4 The term-document matrix for four words in four Shakespeare plays. The red boxes show that each document is represented as a column vector of length four.*

由于四维空间难以可视化，图 11.5 展示了四个文档向量在二维空间中的可视化；我们任意选取了对应于单词 battle 和 fool 的维度。

> Since 4-dimensional spaces are hard to visualize, Fig. 11.5 shows a visualization of the four document vectors in two dimensions; we’ve arbitrarily chosen the dimensions corresponding to the words battle and fool.

> 40

> 《亨利五世》[4,13]
>
> *Henry V [4,13]*

> 15

battle

> 10 《裘力斯·凯撒》[1,7]
>
> *10 Julius Caesar [1,7]*

> 5 《皆大欢喜》[36,1] 《第十二夜》[58,0]
>
> *5 As You Like It [36,1] Twelfth Night [58,0]*

> 5 10 15 20 25 30 35 40 45 50 55 60

fool

> 图 11.5 四部莎士比亚戏剧文档的文档向量的空间可视化，仅展示其中两个维度，分别对应单词 battle 和 fool。
>
> *Figure 11.5 A spatial visualization of the document vectors for the four Shakespeare play documents, showing just two of the dimensions, corresponding to the words battle and fool.*

> 喜剧在 fool 维度上取值高，在 battle 维度上取值低。
>
> *The comedies have high values for the fool dimension and low values for the battle dimension.*

两个相似的文档往往具有相似的单词，而如果两个文档具有相似的单词，它们的列向量也往往相似。喜剧《皆大欢喜》[1,114,36,20] 和《第十二夜》[0,80,58,15] 的向量彼此之间的相似程度（傻子和机智多于战斗）远高于它们与《裘力斯·凯撒》[7,62,1,2] 或《亨利五世》[13,89,4,3] 的相似程度。

> Two documents that are similar will tend to have similar words, and if two documents have similar words their column vectors will tend to be similar. The vectors for the comedies As You Like It [1,114,36,20] and Twelfth Night [0,80,58,15] look a lot more like each other (more fools and wit than battles) than they look like Julius Caesar [7,62,1,2] or Henry V [13,89,4,3].

### 11.1.2 词项加权：tf-idf 与 BM25

> 11.1.2 Term weighting: tf-idf and BM25

事实上，在信息检索（IR）中，我们并不对《皆大欢喜》使用 [1 114 36 20] 这样的原始词频计数，也不对图 11.2 中的文档使用 [1 3 1 1 1 1 1 5 6 1 2 1 4 1 3 1 1 1]。相反，我们为文档中的每个单词计算一个词项权重。两种词项加权方案是

> In fact, in IR, we don’t use raw word counts like [1 114 36 20] for As You Like It, or [1 3 1 1 1 1 1 5 6 1 2 1 4 1 3 1 1 1] for the document in Fig. 11.2. Instead we compute a term weight for each document word. Two term weighting schemes are

> 词项权重
>
> *term weight*

常见的有：tf-idf 以及 tf-idf 的一种变体 BM25。

> common: tf-idf and a variant of tf-idf called BM25.

> BM25

Tf-idf（这里的“-”是连字符，不是减号）是两项的乘积：

> Tf-idf (the ‘-’ here is a hyphen, not a minus sign) is the product of two terms, the

词频 tf 与逆文档频率 idf。

> term frequency tf and the inverse document frequency idf.

11.1 • 信息检索 257

> 11.1 • INFORMATION RETRIEVAL 257

词频项告诉我们该词出现的频繁程度；出现

> The term frequency term tells us how frequent the word is; words that occur

得越频繁的词，往往越能反映文档的内容。

> more often in a document are likely to be informative about the document’s contents.

我们通常使用词频的 log10，而不是原始计数。其直觉是：一个词在文档中出现 100 次，并不意味着它与文档含义相关的可能性提高 100 倍。我们还需要对计数为 0 的情况做特殊处理，因为不能对 0 取对数。3 因此，如果我们把 count(t,d) 定义为词项 t 在文档 d 中的原始计数，那么 tft,d，即词项 t 在文档 d 中的 tf 为

> We usually use the log10 of the word frequency, rather than the raw count. The intuition is that a word appearing 100 times in a document doesn’t make that word 100 times more likely to be relevant to the meaning of the document. We also need to do something special with counts of 0, since we can’t take the log of 0.3 So if we define count(t,d) as the raw count of term t in document d, then tft,d, the tf of term t in document d is

(1+log10 count(t,d) if count(t,d) > 0

tft,d =

> (11.4)

否则为 0

> 0 otherwise

如果我们使用对数加权，则词项在文档中出现 0 次时 tf = 0，出现 1 次时 tf = 1 + log10(1) = 1 + 0 = 1，出现 10 次时 tf =1+log10(10) = 2，出现 100 次时 tf = 1+log10(100) = 3，出现 1000 次时 tf = 4，依此类推。

> If we use log weighting, terms which occur 0 times in a document would have tf = 0, 1 times in a document tf = 1 + log10(1) = 1 + 0 = 1, 10 times in a document tf =1+log10(10) = 2, 100 times tf = 1+log10(100) = 3, 1000 times tf = 4, and so on.

词项 t 的文档频率 dft 是它出现的文档数量。只在少数文档中出现的词项有助于把这些文档与集合中其余文档区分开；而在整个集合中都出现的词项则没有那么有用。逆文档频率（inverse document frequency，idf）词项权重（Sparck Jones, 1972）定义为：

> The document frequency dft of a term t is the number of documents it occurs in. Terms that occur in only a few documents are useful for discriminating those documents from the rest of the collection; terms that occur across the entire collection aren’t as helpful. The inverse document frequency or idf term weight(Sparck Jones, 1972) is defined as:

N

idft = log10

> (11.5)

dft

其中 N 是集合中的文档总数，dft 是词项 t 出现的文档数量。一个词项出现的文档越少，该权重就越高；在每个文档中都出现的词项被赋予最低权重 0。

> where N is the total number of documents in the collection, and dft is the number of documents in which term t occurs. The fewer documents in which a term occurs, the higher this weight; the lowest weight of 0 is assigned to terms that occur in every document.

下面给出莎士比亚戏剧语料库中一些词的 idf 值，

> Here are some idf values for some words in the corpus of Shakespeare plays,

从只在一部戏剧中出现的极具信息量的词，如 Romeo，到在少数几部戏剧中出现的词，如 salad 或 Falstaff，再到非常常见的词，如 fool，乃至因为出现在全部 37 部戏剧中而完全不具区分度的词，如 good 或 sweet。4

> ranging from extremely informative words that occur in only one play like Romeo, to those that occur in a few like salad or Falstaff, to those that are very common like fool or so common as to be completely non-discriminative since they occur in all 37 plays like good or sweet.4

| 词<br>Word | df | idf |
| --- | --- | --- |
| Romeo | 1 | 1.57 |
| salad | 2 | 1.27 |
| Falstaff | 4 | 0.967 |
| forest | 12 | 0.489 |
| battle | 21 | 0.246 |
| wit | 34 | 0.037 |
| fool | 36 | 0.012 |
| good | 37 | 0 |
| sweet | 37 | 0 |

于是，词 t 在文档 d 中的 tf-idf 值就是词频

> The tf-idf value for word t in document d is then the product of term frequency

tft,d 与 IDF 的乘积：

> tft,d and IDF:

tf-idf(t,d) = tft,d ·idft

> (11.6)

> 3

> 我们也可以使用下面这种替代形式，我们在较早的版本中使用过它：tft,d =log10(count(t,d)+1)
>
> *We can also use this alternative formulation, which we have used in earlier editions: tft,d =log10(count(t,d)+1)*

> 4

> Sweet 是莎士比亚最喜爱的形容词之一，这一事实可能与 16 世纪之交欧洲食谱中糖的使用增加有关（Jurafsky, 2014, p. 175）。
>
> *Sweet was one of Shakespeare’s favorite adjectives, a fact probably related to the increased use of sugar in European recipes around the turn of the 16th century (Jurafsky, 2014, p. 175).*

258 第 11 章 • 基于检索的模型

> 258 CHAPTER 11 • RETRIEVAL-BASED MODELS

### 11.1.3 文档打分

> 11.1.3 Document Scoring

一旦我们把每个文档和查询都表示为加权向量，就需要对每个文档打分。我们的目标是衡量文档与用户查询所表达的信息需求之间的相关性。在经典的 tf-idf 模型中，我们通过度量文档在向量空间中与查询的几何相似度来估计这种相关性。也就是说，我们做了一个简化假设：与查询含有相似词语的文档对用户更相关。

> Once we have represented each document and query as a weighted vector, we need to score each document. Our goal is to measure the relevance of the document to the user’s information need, as expressed in their query. In the classic tf-idf model we estimate this relevance of a document by measuring its geometric similarity in vector space to the query. That is, we make the simplifying assumption that documents that have similar words to the query are more relevant to the user.

我们使用第 5 章介绍的余弦相似度函数，用文档

> We use the cosine similarity function introduced in Chapter 5, scoring document

向量 d 与查询向量 q 的余弦值来给文档 d 打分：

> d by the cosine of its vector d with the query vector q:

score(q,d) = cos(q,d) = q·d

> (11.7)

|q||d|

理解余弦计算的另一种方式是把它看作单位向量的点积；我们可以先把查询向量和文档向量都除以各自的长度归一化为单位向量，然后再取点积：

> Another way to think of the cosine computation is as the dot product of unit vectors; we can first normalize both the query and document vector to unit vectors, by dividing by their lengths, and then take the dot product:

score(q,d) = cos(q,d) = q |q| · d

> （11.8）
>
> *(11.8)*

|d|

我们可以展开式 11.8，使用 tf-idf 值并把点积展开

> We can spell out Eq. 11.8, using the tf-idf values and spelling out the dot product

为乘积之和：

> as a sum of products:

X tf-idf(t,q) tf-idf(t,d)

score(q,d) =

> （11.9）
>
> *(11.9)*

qP · qP

qi∈q tf-idf 2(qi,q) di∈d tf-idf 2(di,d)

> t∈q

现在让我们用式 11.9 走一遍一个针对

> Now let’s use Eq. 11.9 to walk through an example of a tiny query against a

由 4 篇微型文档组成的集合的小查询示例，计算 tf-idf 值并查看文档的排名。我们假设下面查询和文档中的所有单词都已转为小写并去除了标点：

> collection of 4 nano documents, computing tf-idf values and seeing the rank of the documents. We’ll assume all words in the following query and documents are downcased and punctuation is removed:

查询：sweet love

> Query: sweet love

| 查询：<br>Query: | sweet love |
| --- | --- |
| 文档 1：<br>Doc 1: | Sweet sweet nurse! Love? |
| 文档 2：<br>Doc 2: | Sweet sorrow |
| 文档 3：<br>Doc 3: | How sweet is love? |
| 文档 4：<br>Doc 4: | Nurse! |

图 11.6 展示了查询与文档 1 之间、以及查询与文档 2 之间 tf-idf 余弦的计算。余弦是 tf-idf 值的归一化点积，因此为了归一化，我们必须使用式 11.4、式 11.5、式 11.6 和式 11.9 计算查询与前两篇文档的文档向量长度 |q|、|d1| 和 |d2|（文档 3 和文档 4 的计算也是需要的，但留作读者练习）。向量之间的点积是各维度上两个 tf-idf 向量在该维度上的值的乘积之和。只有当查询和文档在该维度上都有非零值时，该乘积才非零，因此在本例中，查询里只有 sweet 和 love 有非零值，点积将是各向量中这些元素乘积之和。

> Fig. 11.6 shows the computation of the tf-idf cosine between the query and Document 1, and the query and Document 2. The cosine is the normalized dot product of tf-idf values, so for the normalization we must need to compute the document vector lengths |q|, |d1|, and |d2| for the query and the first two documents using Eq. 11.4, Eq. 11.5, Eq. 11.6, and Eq. 11.9 (computations for Documents 3 and 4 are also needed but are left as an exercise for the reader). The dot product between the vectors is the sum over dimensions of the product, for each dimension, of the values of the two tf-idf vectors for that dimension. This product is only non-zero where both the query and document have non-zero values, so for this example, in which only sweet and love have non-zero values in the query, the dot product will be the sum of the products of those elements of each vector.

文档 1 与查询的余弦（0.747）高于文档 2

> Document 1 has a higher cosine with the query (0.747) than Document 2 has

与查询的余弦（0.0779），因此 tf-idf 余弦模型会把文档 1 排在文档 2 之前。考虑到向量空间模型，这一排名是符合直觉的，因为文档 1 包含两个词项，其中 sweet 出现了两次，而文档 2 是 11.1 • 信息检索 259 查询

> with the query (0.0779), and so the tf-idf cosine model would rank Document 1 above Document 2. This ranking is intuitive given the vector space model, since Document 1 has both terms including two instances of sweet, while Document 2 is 11.1 • INFORMATION RETRIEVAL 259 Query

| 查询<br>单词 计数 tf df idf tf-idf 归一化 = tf-idf/ \|q \|<br>sweet 1 1 3 0.125 0.125 0.383<br>nurse 0 0 2 0.301 0 0<br>love 1 1 2 0.301 0.301 0.924<br>how 0 0 1 0.602 0 0<br>sorrow 0 0 1 0.602 0 0<br>is 0 0 1 0.602 0 0<br>=√<br>q .1252 +.3012 = .326<br>\| \|<br>文档 1 文档 2<br>单词 计数 tf tf-idf 归一化 × q 计数 tf tf-idf 归一化 ×q<br>sweet 2 1.301 0.163 0.357 0.137 1 1.000 0.125 0.203 0.0779<br>nurse 1 1.000 0.301 0.661 0 0 0 0 0 0<br>love 1 1.000 0.301 0.661 0.610 0 0 0 0 0<br>how 0 0 0 0 0 0 0 0 0 0<br>sorrow 0 0 0 0 0 1 1.000 0.602 0.979 0<br>is 0 0 0 0 0 0 0 0 0 0<br>=√ =√<br>d .1632 +.3012 +.3012 = .456 d .1252 +.6022 = .615<br>\| 1\| \| 2\|<br>余弦：列求和：0.747 余弦：列求和：0.0779<br>Query<br>word cnt tf df idf tf-idf n’lized = tf-idf/ \|q \|<br>sweet 1 1 3 0.125 0.125 0.383<br>nurse 0 0 2 0.301 0 0<br>love 1 1 2 0.301 0.301 0.924<br>how 0 0 1 0.602 0 0<br>sorrow 0 0 1 0.602 0 0<br>is 0 0 1 0.602 0 0<br>=√<br>q .1252 +.3012 = .326<br>\| \|<br>Document 1 Document 2<br>word cnt tf tf-idf n’lized × q cnt tf tf-idf n’lized ×q<br>sweet 2 1.301 0.163 0.357 0.137 1 1.000 0.125 0.203 0.0779<br>nurse 1 1.000 0.301 0.661 0 0 0 0 0 0<br>love 1 1.000 0.301 0.661 0.610 0 0 0 0 0<br>how 0 0 0 0 0 0 0 0 0 0<br>sorrow 0 0 0 0 0 1 1.000 0.602 0.979 0<br>is 0 0 0 0 0 0 0 0 0 0<br>=√ =√<br>d .1632 +.3012 +.3012 = .456 d .1252 +.6022 = .615<br>\| 1\| \| 2\|<br>Cosine: Pof column: 0.747 Cosine: Pof column: 0.0779 |  |
| --- | --- |
| 图 11.6<br>Figure 11.6 | 查询与微型文档 1（0.747）和 2 之间 tf-idf 余弦得分的计算<br>Computation of tf-idf cosine score between the query and nano-documents 1 (0.747) and 2 |

单词 计数 tf df idf tf-idf 归一化 = tf-idf/|q|sweet 1 1 3 0.125 0.125 0.383 nurse 0 0 2 0.301 0 0 love 1 1 2 0.301 0.301 0.924 how 0 0 1 0.602 0 0 sorrow 0 0 1 0.602 0 0 is 0 0 1 0.602 0 0

> word cnt tf df idf tf-idf n’lized = tf-idf/|q|sweet 1 1 3 0.125 0.125 0.383 nurse 0 0 2 0.301 0 0 love 1 1 2 0.301 0.301 0.924 how 0 0 1 0.602 0 0 sorrow 0 0 1 0.602 0 0 is 0 0 1 0.602 0 0

√ .1252 +.3012 = .326

|q| =

文档 1 文档 2

> Document 1 Document 2

单词 计数 tf tf-idf 归一化 × q 计数 tf tf-idf 归一化 ×q sweet 2 1.301 0.163 0.357 0.137 1 1.000 0.125 0.203 0.0779 nurse 1 1.000 0.301 0.661 0 0 0 0 0 0 love 1 1.000 0.301 0.661 0.610 0 0 0 0 0 how 0 0 0 0 0 0 0 0 0 0 sorrow 0 0 0 0 0 1 1.000 0.602 0.979 0 is 0 0 0 0 0 0 0 0 0 0

> word cnt tf tf-idf n’lized × q cnt tf tf-idf n’lized ×q sweet 2 1.301 0.163 0.357 0.137 1 1.000 0.125 0.203 0.0779 nurse 1 1.000 0.301 0.661 0 0 0 0 0 0 love 1 1.000 0.301 0.661 0.610 0 0 0 0 0 how 0 0 0 0 0 0 0 0 0 0 sorrow 0 0 0 0 0 1 1.000 0.602 0.979 0 is 0 0 0 0 0 0 0 0 0 0

√ .1632 +.3012 +.3012 = .456 √ .1252 +.6022 = .615

|d1| = |d2| =

余弦：列求和：0.747 余弦：列求和：0.0779

> Cosine: P of column: 0.747 Cosine: P of column: 0.0779

> （0.0779），使用式 11.4、式 11.5、式 11.6 和式 11.9。
>
> *(0.0779), using Eq. 11.4, Eq. 11.5, Eq. 11.6 and Eq. 11.9.*

缺少其中一个词项。文档 3 和文档 4 的计算我们留作读者练习。

> missing one of the terms. We leave the computation for Documents 3 and 4 as an exercise for the reader.

在实践中，式 11.9 有许多变体和近似。例如，我们可能选择通过去除某些词项来简化处理。为此，我们先展开式 11.9 中 tf-idf 的公式，明确写出式 11.6 中的 tf 和 idf 项：

> In practice, there are many variants and approximations to Eq. 11.9. For example, we might choose to simplify processing by removing some terms. To see this, let’s start by expanding the formula for tf-idf in Eq. 11.9 to explicitly mention the tf and idf terms from Eq. 11.6:

X tft,q ·idft tft,d ·idft

score(q,d) =

> （11.10）
>
> *(11.10)*

qP · qP

qi∈q tf-idf 2(qi,q) di∈d tf-idf 2(di,d)

> t∈q

例如，在 tf-idf 余弦的一种常见变体中，我们去掉了

> In one common variant of tf-idf cosine, for example, we drop the idf term for the

文档的 idf 项。消除 idf 项的第二份副本（因为查询中已经计算了完全相同的项）有时会带来更好的性能：

> document. Eliminating the second copy of the idf term (since the identical term is already computed for the query) turns out to sometimes result in better performance:

X tft,q·idft tft,d ·idft

score(q,d) =

> (11.11)

qP · qP

qi∈q tf-idf 2(qi,q) di∈d tf-idf 2(di,d)

> t∈q

tf-idf 的其他变体则去掉了各种其他项。

> Other variants of tf-idf eliminate various other terms.

tf-idf 家族中稍复杂一些的变体是 BM25 权重

> A slightly more complex variant in the tf-idf family is the BM25 weighting

> BM25

方案（有时称为 Okapi BM25，得名于它最初被引入的 Okapi 信息检索系统（Robertson et al., 1995））。BM25 增加了两个参数：k，一个用于调整词频与 IDF 之间平衡的旋钮；b，用于控制文档长度归一化的重要程度。给定 260 第 11 章 • 基于检索的模型 查询 q 时，文档 d 的 BM25 得分为：

> scheme (sometimes called Okapi BM25 after the Okapi IR system in which it was introduced (Robertson et al., 1995)). BM25 adds two parameters: k, a knob that adjusts the balance between term frequency and IDF, and b, which controls the importance of document length normalization. The BM25 score of a document d given 260 CHAPTER 11 • RETRIEVAL-BASED MODELS a query q is:

> IDF 加权的 tf
>
> *IDF weighted tf*

z  N }|  { z }| {

X tft,d

log   

> (11.12)

dft

> |d|

k 1−b+b +tft,d

> t∈q |davg|

其中 |davg| 是平均文档长度。当 k 为 0 时，BM25 退化为不使用词频，仅对查询中的词项做二值选择（再加上 idf）。

> where |davg| is the length of the average document. When k is 0, BM25 reverts to no use of term frequency, just a binary selection of terms in the query (plus idf).

较大的 k 会使结果趋近于原始词频（再加上 idf）。b 的取值范围从 1（按文档长度缩放）到 0（不做长度缩放）。Manning et al. (2008) 指出合理的取值是 k = [1.2,2] 和 b = 0.75。Kamphuis et al. (2020) 对 BM25 的众多细微变体做了有用的总结。

> A large k results in raw term frequency (plus idf). b ranges from 1 (scaling by document length) to 0 (no length scaling). Manning et al. (2008) suggest reasonable values are k = [1.2,2] and b = 0.75. Kamphuis et al. (2020) is a useful summary of the many minor variants of BM25.

停用词 过去，常见的做法是在表示查询和文档之前，把其中的高频词去掉。这类要被移除的高频词的列表称为停用词表（stop list）。其背后的直觉是，高频词

> Stop words In the past it was common to remove high-frequency words from both the query and document before representing them. The list of such high-frequency words to be removed is called a stop list. The intuition is that high-frequency terms

> 停用词表
>
> *stop list*

（通常是像 the、a、to 这样的功能词）语义权重很低，对检索帮助不大，而且去掉它们还有助于缩小我们下面将要描述的倒排索引文件。

> (often function words like the, a, to) carry little semantic weight and may not help with retrieval, and can also help shrink the inverted index files we describe below.

使用停用词表的缺点是，它使得搜索包含停用词表中词语的短语变得困难。例如，常见的停用词表会把短语 to be or not to be 缩减为短语 not。在现代信息检索系统中，停用词表的使用已远不那么普遍，部分原因是效率的提升，部分原因是其大部分功能已由 IDF 加权承担——IDF 会降低在每个文档中都出现的功能词的权重。尽管如此，停用词移除在各种 NLP 任务中偶尔仍有用处，因此值得留意。

> The downside of using a stop list is that it makes it difficult to search for phrases that contain words in the stop list. For example, common stop lists would reduce the phrase to be or not to be to the phrase not. In modern IR systems, the use of stop lists is much less common, partly due to improved efficiency and partly because much of their function is already handled by IDF weighting, which downweights function words that occur in every document. Nonetheless, stop word removal is occasionally useful in various NLP tasks so is worth keeping in mind.

### 11.1.4 高效地查找文档：倒排索引

> 11.1.4 Efficiently finding documents: the Inverted Index

为了计算得分，我们需要高效地找出包含查询中词语的文档。（任何不包含查询词项的文档得分都为 0，可以忽略。）因此，信息检索中的基本搜索问题就是找出所有包含某个词项 q ∈Q 的文档 d ∈C。

> In order to compute scores, we need to efficiently find documents that contain words in the query. (Any document that contains none of the query terms will have a score of 0 and can be ignored.) The basic search problem in IR is thus to find all documents d ∈C that contain a term q ∈Q.

用于完成这一任务的数据结构是倒排索引，我们用它使这种搜索变得高效，同时它还能方便地存储一些有用信息，比如文档频率以及每个词项在每个文档中的出现次数。

> The data structure for this task is the inverted index, which we use for making this search efficient, and also conveniently storing useful information like the document frequency and the count of each term in each document.

> 倒排索引
>
> *inverted index*

给定一个查询词项，倒排索引会给出一个包含该

> An inverted index, given a query term, gives a list of documents that contain the

词项的文档列表。它由两部分组成：词典和倒排记录表。词典是一个列表

> term. It consists of two parts, a dictionary and the postings. The dictionary is a list

> 倒排记录表
>
> *postings*

由词项构成（其设计目标是能被高效访问），每个词项都指向该词项的倒排记录表。倒排记录表是与每个词项相关联的文档 ID 的列表，其中还可以包含诸如词频、甚至词项在文档中的精确位置等信息。词典还可以为每个词项存储文档频率。例如，针对上面 4 篇示例文档的一个简单倒排索引，其中每个词带有放在 {} 中的文档频率，并指向一个包含文档 ID 和放在 [] 中的词项计数的倒排记录表，可能如下所示：

> of terms (designed to be efficiently accessed), each pointing to a postings list for the term. A postings list is the list of document IDs associated with each term, which can also contain information like the term frequency or even the exact positions of terms in the document. The dictionary can also store the document frequency for each term. For example, a simple inverted index for our 4 sample documents above, with each word containing its document frequency in {}, and a pointer to a postings list that contains document IDs and term counts in [], might look like the following:

how {1} →3 [1] is {1} →3 [1] love {2} →1 [1] →3 [1] nurse {2} →1 [1] →4 [1] sorrow {1} →2 [1] sweet {3} →1 [2] →2 [1] →3 [1]

| how 1<br>{ } | → | 3 [1] |
| --- | --- | --- |
| is 1<br>{ } | → | 3 [1] |
| love 2<br>{ } | → | 1 [1] 3 [1]<br>→ |
| nurse 2<br>{ } | → | 1 [1] 4 [1]<br>→ |
| sorrow 1<br>{ } | → | 2 [1] |
| sweet 3<br>{ } | → | 1 [2] 2 [1] 3 [1]<br>→ → |

11.2 • 信息检索系统的评价 261

> 11.2 • EVALUATION OF INFORMATION-RETRIEVAL SYSTEMS 261

给定查询中的词项列表，我们可以非常高效地得到所有候选

> Given a list of terms in query, we can very efficiently get lists of all candidate

文档的列表，连同计算我们所需的 tf-idf 得分所必需的信息。

> documents, together with the information necessary to compute the tf-idf scores we need.

### 11.1.5 小结：排序式检索

> 11.1.5 Summary: Ranked Retrieval

我们所描述的各个部分被整合在一起，构成一个完整的排序式检索系统。在初始化阶段，系统会接收一个文档集合

> All the pieces we’ve describe are integrated together to create a single ranked retrieval system. In the initialization phase, the system is given a document collection

> 排序式
>
> *ranked*

> 检索
>
> *retrieval*

并为其创建倒排索引。

> and creates the inverted index for it.

然后在检索阶段，给定一个用户查询，检索系统使用倒排

> Then during retrieval, given a user query, the retrieval system uses the inverted

索引找出所有包含查询中关键词的候选文档。对于每篇候选文档，系统通过计算 tf-idf（或 BM25）与用户查询向量的余弦值来为其打分，从而估计它与用户的相关性。文档按相关性得分从高到低排序，并将该列表（或列表中的前 N 篇文档）返回给用户。

> index to find all candidate documents with keywords in the query. For each candidate document, the system estimates its relevance to the user by assigning it a score based on computing the tf-idf (or BM25) cosine with the user’s query vector. The documents are sorted according to relevance scores, from most to least relevant, and the list (or the first N documents on it) are returned to the user.

## 11.2 信息检索系统的评估

> 11.2 Evaluation of Information-Retrieval Systems

我们使用一直沿用的精确率与召回率指标来衡量排序式检索系统的性能。我们假设 IR 系统返回的每篇文档要么与我们的目的相关，要么不相关。

> We measure the performance of ranked retrieval systems using the same precision and recall metrics we have been using. We make the assumption that each document returned by the IR system is either relevant to our purposes or not relevant.

精确率是返回文档中相关文档所占的比例，召回率是全部相关文档中被返回的比例。更形式化地说，假设某系统响应一个信息请求返回 T 篇排序文档，其中子集 R 是相关的，与之不相交的子集 N 是其余不相关的文档，而整个集合中有 U 篇文档与该请求相关。精确率与召回率则定义为：

> Precision is the fraction of the returned documents that are relevant, and recall is the fraction of all relevant documents that are returned. More formally, let’s assume a system returns T ranked documents in response to an information request, a subset R of these are relevant, a disjoint subset, N, are the remaining irrelevant documents, and U documents in the collection as a whole are relevant to this request. Precision and recall are then defined as:

精确率 = |R| 召回率 = |R|

> Precision = |R| Recall = |R|

> (11.13)

|T| |U|

遗憾的是，这些指标并不能充分衡量一个对其返回文档进行排序的系统的性能。如果我们要比较两个排序式检索系统的性能，就需要一个偏爱把相关文档排得更靠前的系统的指标。我们需要改造精确率与召回率，以刻画系统把相关文档放在排名更靠前位置的能力有多好。

> Unfortunately, these metrics don’t adequately measure the performance of a system that ranks the documents it returns. If we are comparing the performance of two ranked retrieval systems, we need a metric that prefers the one that ranks the relevant documents higher. We need to adapt precision and recall to capture how well a system does at putting relevant documents higher in the ranking.

让我们看一个例子。假设我们有一个用户查询，并从一个由 25 篇文档组成的集合中检索出

> Let’s turn to an example. Assume we have a user query and have retrieved a

一组文档，其中 9 篇与该查询相关。图 11.7 中的表格展示了这 25 篇排序文档，判断列表明该文档是否相关。

> set of documents from a collection of 25 documents, 9 of which are relevant to the query in this collection. The table in Fig. 11.7 shows the 25 ranked documents with the judgment column indicating if the document was relevant or not.

接下来的两列给出了针对某一特定查询、随着我们沿排序文档集合向下推进而计算出的各排名位置的精确率与召回率值。

> The next two columns give the rank-specific precision and recall values calculated as we proceed down through a set of ranked documents for a particular query.

精确率是在给定排名位置所看到的相关文档的比例，召回率是在同一排名位置找到的相关文档的比例。更形式化地说，在排名 k 处，我们可以将 precisionk 与 recallk 定义为：

> The precisions are the fraction of relevant documents seen at a given rank, and recalls the fraction of relevant documents found at the same rank. More formally, at rank k, we can define precisionk and recallk as:

Precisionk = |前 k 篇中的相关文档|

> Precisionk = |relevant documents in top k|

k

Recallk = |前 k 篇中的相关文档|

> Recallk = |relevant documents in top k|

> (11.14)

9 262 第 11 章 • 基于检索的模型

> 9 262 CHAPTER 11 • RETRIEVAL-BASED MODELS

> 排名 判断 PrecisionRank RecallRank 1 R 1.0 .11 2 N .50 .11 3 R .66 .22 4 N .50 .22 5 R .60 .33 6 R .66 .44 7 N .57 .44 8 R .63 .55 9 N .55 .55 10 N .50 .55 11 R .55 .66 12 N .50 .66 13 N .46 .66 14 N .43 .66 15 R .47 .77 16 N .44 .77 17 N .41 .77 18 R .44 .88 19 N .42 .88 20 N .40 .88 21 N .38 .88 22 N .36 .88 23 N .35 .88 24 N .33 .88 25 R .36 1.0
>
> *Rank Judgment PrecisionRank RecallRank 1 R 1.0 .11 2 N .50 .11 3 R .66 .22 4 N .50 .22 5 R .60 .33 6 R .66 .44 7 N .57 .44 8 R .63 .55 9 N .55 .55 10 N .50 .55 11 R .55 .66 12 N .50 .66 13 N .46 .66 14 N .43 .66 15 R .47 .77 16 N .44 .77 17 N .41 .77 18 R .44 .88 19 N .42 .88 20 N .40 .88 21 N .38 .88 22 N .36 .88 23 N .35 .88 24 N .33 .88 25 R .36 1.0*

| 排名 判断 PrecisionRank RecallRank<br>Rank Judgment PrecisionRank RecallRank |  |
| --- | --- |
| 1 R 1.0 .11<br>2 N .50 .11<br>3 R .66 .22<br>4 N .50 .22<br>5 R .60 .33<br>6 R .66 .44<br>7 N .57 .44<br>8 R .63 .55<br>9 N .55 .55<br>10 N .50 .55<br>11 R .55 .66<br>12 N .50 .66<br>13 N .46 .66<br>14 N .43 .66<br>15 R .47 .77<br>16 N .44 .77<br>17 N .41 .77<br>18 R .44 .88<br>19 N .42 .88<br>20 N .40 .88<br>21 N .38 .88<br>22 N .36 .88<br>23 N .35 .88<br>24 N .33 .88<br>25 R .36 1.0 |  |
| 图 11.7<br>Figure 11.7 | 沿排序文档集合向下推进时计算出的各排名位置的精确率与召回率值<br>Rank-specific precision and recall values calculated as we proceed down |

> （假设该集合中有 9 篇相关文档）。
>
> *through a set of ranked documents (assuming the collection has 9 relevant documents).*

| 1.0<br>0.8<br>0.6 精确率<br>0.4<br>0.2<br>0.0<br>0.0 0.2 0.4 0.6 0.8 1.0<br>召回率<br>1.0<br>0.8<br>0.6 Precision<br>0.4<br>0.2<br>0.0<br>0.0 0.2 0.4 0.6 0.8 1.0<br>Recall |  |
| --- | --- |
| 图 11.8<br>Figure 11.8 | 表 11.7 中数据的精确率-召回率曲线。<br>The precision recall curve for the data in table 11.7. |

> 1.0

> 0.8

> 精确率
>
> *Precision*

> 0.6

> 0.4

> 0.2

> 0.0 0.0 0.2 0.4 0.6 0.8 1.0

> 召回率
>
> *Recall*

注意召回率是非递减的；当遇到一篇相关文档时，

> Note that recall is non-decreasing; when a relevant document is encountered,

召回率会增加，而当找到一篇不相关文档时，它保持不变。

> recall increases, and when a non-relevant document is found it remains unchanged.

另一方面，精确率则上下跳动，遇到相关文档时升高，否则降低。最常见的可视化

> Precision, on the other hand, jumps up and down, increasing when relevant documents are found, and decreasing otherwise. The most common way to visualize

> 精确率-召回率
>
> *precision-recall*

精确率与召回率的方式，是在精确率-召回率曲线中绘制精确率对召回率的关系，

> precision and recall is to plot precision against recall in a precision-recall curve,

> 曲线
>
> *curve*

就像图 11.8 针对表 11.7 中数据所展示的那条曲线一样。

> like the one shown in Fig. 11.8 for the data in table 11.7.

图 11.8 展示的是单个查询的取值。但我们需要把 11.2 • 信息检索系统的评估 263 所有查询的取值合并起来，并且要以一种能让我们将一个系统与另一个系统进行比较的方式来做。做到这一点的一种方法是，在 11 个固定的召回率水平（从 0 到 100，步长为 10）上绘制平均精确率值。由于我们不太可能在这些确切的水平上有数据点，我们

> Fig. 11.8 shows the values for a single query. But we’ll need to combine values 11.2 • EVALUATION OF INFORMATION-RETRIEVAL SYSTEMS 263 for all the queries, and in a way that lets us compare one system to another. One way of doing this is to plot averaged precision values at 11 fixed levels of recall (0 to 100, in steps of 10). Since we’re not likely to have datapoints at these exact levels, we

> 插值
>
> *interpolated*

对 11 个召回率取值使用插值精确率值，这些值取自我们所

> use interpolated precision values for the 11 recall values from the data points we do

> 精确率
>
> *precision*

拥有的数据点。我们可以通过选取在等于或高于当前所计算召回率的任一召回率水平上所达到的最大精确率值来实现这一点。换言之，

> have. We can accomplish this by choosing the maximum precision value achieved at any level of recall at or above the one we’re calculating. In other words,

IntPrecision(r) = max i>=r Precision(i)

> (11.15)

这种插值方案不仅让我们能对一组查询上的性能取平均，还有助于平滑原始数据中不规则的精确率取值。它的设计意图是给予系统有利的推定，即把在高于当前所测召回率的更高召回率水平上所达到的最大精确率值赋予该系统。图 11.9 和图 11.10 给出了我们示例中所得到的插值数据点。

> This interpolation scheme not only lets us average performance over a set of queries, but also helps smooth over the irregular precision values in the original data. It is designed to give systems the benefit of the doubt by assigning the maximum precision value achieved at higher levels of recall from the one being measured. Fig. 11.9 and Fig. 11.10 show the resulting interpolated data points from our example.

> 插值精确率 召回率
>
> *Interpolated Precision Recall*

| 插值精确率 召回率<br>Interpolated Precision Recall |  |
| --- | --- |
| 1.0 0.0<br>1.0 .10<br>.66 .20<br>.66 .30<br>.66 .40<br>.63 .50<br>.55 .60<br>.47 .70<br>.44 .80<br>.36 .90<br>.36 1.0 |  |
| 图 11.9<br>Figure 11.9 | 来自图 11.7 的插值数据点。<br>Interpolated data points from Fig. 11.7. |

> 1.0 0.0 1.0 .10.66 .20.66 .30.66 .40.63 .50.55 .60.47 .70.44 .80.36 .90.36 1.0

给定诸如 图 11.10 中那样的曲线，我们可以通过比较曲线来比较两个系统或方法。显然，在所有召回率取值上精确率都更高的曲线更受青睐。不过，这些曲线也能提供对系统整体行为的洞见。在靠左端精确率更高的系统可能更偏好精确率而非召回率，而更偏向召回率的系统则会在更高的召回率水平上（靠右端）更高。

> Given curves such as that in Fig. 11.10 we can compare two systems or approaches by comparing their curves. Clearly, curves that are higher in precision across all recall values are preferred. However, these curves can also provide insight into the overall behavior of a system. Systems that are higher in precision toward the left may favor precision over recall, while systems that are more geared towards recall will be higher at higher levels of recall (to the right).

> 均值平均
>
> *mean average*

评估排序式检索的第二种方法是平均平均精确率（mean average precision，MAP），

> A second way to evaluate ranked retrieval is mean average precision (MAP),

> 精确率
>
> *precision*

它提供了一个可用于比较相互竞争的系统或方法的单一度量。在这种方法中，我们同样沿排好序的条目列表向下遍历，但此时只在遇到相关条目的那些位置记录精确率（例如图 11.7 中的排名 1、3、5、6，而不包括 2 或 4）。对于单个查询，我们在返回集上对这些单独的精确率测量值取平均（截至某个固定截断点）。更形式化地说，若假定 Rr 是排名在 r 或 r 之前的相关文档集合，则单个查询的平均精确率（average precision，AP）为

> which provides a single metric that can be used to compare competing systems or approaches. In this approach, we again descend through the ranked list of items, but now we note the precision only at those points where a relevant item has been encountered (for example at ranks 1, 3, 5, 6 but not 2 or 4 in Fig. 11.7). For a single query, we average these individual precision measurements over the return set (up to some fixed cutoff). More formally, if we assume that Rr is the set of relevant documents at or above r, then the average precision (AP) for a single query is

1 X

AP = Precisionr(d)

> (11.16)

|Rr|

> d∈Rr

其中 Precisionr(d) 是在发现文档 d 的排名处所测得的精确率。对于一组查询 Q，我们再对这些平均值取平均，从而得到最终的 MAP 度量：

> where Precisionr(d) is the precision measured at the rank at which document d was found. For an ensemble of queries Q, we then average over these averages, to get our final MAP measure:

MAP = 1 X

AP(q)

> (11.17)

|Q|

> q∈Q

图 11.7 中该单个查询的 MAP（因而等于 AP）为 0.6。

> The MAP for the single query (hence = AP) in Fig. 11.7 is 0.6.

264 第 11 章 • 基于检索的模型

> 264 CHAPTER 11 • RETRIEVAL-BASED MODELS

| 插值精确率-召回率曲线<br>1<br>0.9<br>0.8<br>0.7<br>0.6<br>精确率<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br>召回率<br>Interpolated Precision Recall Curve<br>1<br>0.9<br>0.8<br>0.7<br>0.6<br>Precision<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br>Recall |  |
| --- | --- |
| 图 11.10<br>Figure 11.10 | 一条 11 点插值精确率-召回率曲线。11 个点中每个点处的精确率<br>An 11 point interpolated precision-recall curve. Precision at each of the 11 |

> 插值精确率-召回率曲线
>
> *Interpolated Precision Recall Curve*

> 1

![](images/img_220.png)

> 0.9

> 0.8

![](images/img_219.png)

> 0.7

![](images/img_218.png)

> 0.6 精确率 0.5
>
> *0.6 Precision 0.5*

![](images/img_217.png)

![](images/img_216.png)

> 0.4

> 0.3

> 0.2

![](images/img_215.png)

> 0.1

![](images/img_214.png)

> 0

> 0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1

> 召回率
>
> *Recall*

> 标准召回率水平是就每个查询、从任意更高召回率水平上的最大值插值得到的。原始测得的精确率—召回率点也一并显示。
>
> *standard recall levels is interpolated for each query from the maximum at any higher level of recall. The original measured precision recall points are also shown.*

## 11.3 使用稠密向量的信息检索

> 11.3 Information Retrieval with Dense Vectors

经典的信息检索算法 tf-idf 或 BM25 长期以来被认为存在一个概念性缺陷：只有当查询与文档之间存在完全相同的词重叠时，它们才能奏效。换言之，提出查询（或提出问题）的用户必须准确猜出答案撰写者可能使用了哪些词，这一问题被称为词汇不匹配问题（vocabulary mismatch problem）（Furnas et al., 1987）。

> The classic tf-idf or BM25 algorithms for IR have long been known to have a conceptual flaw: they work only if there is exact overlap of words between the query and document. In other words, the user posing a query (or asking a question) needs to guess exactly what words the writer of the answer might have used, an issue called the vocabulary mismatch problem (Furnas et al., 1987).

解决这一问题的方法是采用一种能够处理同义关系的方法：

> The solution to this problem is to use an approach that can handle synonymy:

即不使用（稀疏的）词频向量，而使用（稠密的）嵌入。这一思想最早在上个世纪以潜在语义索引（Latent Semantic Indexing）方法的名义被提出用于检索（Deerwester et al., 1990），而在当代则通过 BERT 之类的编码器来实现。

> instead of (sparse) word-count vectors, using (dense) embeddings. This idea was first proposed for retrieval in the last century under the name of Latent Semantic Indexing approach (Deerwester et al., 1990), but is implemented in modern times via encoders like BERT.

最强大的方法是将查询和文档同时输入一个

> The most powerful approach is to present both the query and the document to a

单一的编码器，使 transformer 自注意力能够看到查询和文档的所有 token，从而构建出对查询和文档双方含义都敏感的表示。然后可以在 [CLS] token 之上加一个线性层，为查询/文档元组预测一个相似度分数：

> single encoder, allowing the transformer self-attention to see all the tokens of both the query and the document, and thus building a representation that is sensitive to the meanings of both query and document. Then a linear layer can be put on top of the [CLS] token to predict a similarity score for the query/document tuple:

z = BERT(q;[SEP];d)[CLS]

score(q,d) = softmax(U(z))

> (11.18)

该架构如图 11.11a 所示。通常检索步骤并不是在整个文档上进行的。而是把文档切分成更小的段，例如互不重叠的定长块，比如 100 个 token，检索器对这些段而非整个文档进行编码和检索。查询和文档必须被调整为适应 BERT 的 512 个 token 的窗口，例如把查询截断到 64 个 token，并在必要时截断文档，使文档、查询、[CLS] 和 [SEP] 能放进 512 个 token 之内。然后，可以通过收集由 11.3 • 使用稠密向量的信息检索 265 相关段与不相关段构成的调优数据集，把 BERT 系统连同线性层 U 一起针对相关性任务进行微调。

> This architecture is shown in Fig. 11.11a. Usually the retrieval step is not done on an entire document. Instead documents are broken up into smaller passages, such as non-overlapping fixed-length chunks of say 100 tokens, and the retriever encodes and retrieves these passages rather than entire documents. The query and document have to be made to fit in the BERT 512-token window, for example by truncating the query to 64 tokens and truncating the document if necessary so that it, the query,[CLS], and [SEP] fit in 512 tokens. The BERT system together with the linear layer U can then be fine-tuned for the relevance task by gathering a tuning dataset of 11.3 • INFORMATION RETRIEVAL WITH DENSE VECTORS 265 relevant and non-relevant passages.

| s(q,d)<br>s(q,d)<br>•<br>U<br>z CLS z CLS _Q z CLS _D<br>… …<br>… …<br>… …<br>… …<br>… …<br>… …<br>查询 [sep] 文档 查询 文档<br>(a) (b)<br>s(q,d)<br>s(q,d)<br>•<br>U<br>z CLS z CLS _Q z CLS _D<br>… …<br>… …<br>… …<br>… …<br>… …<br>… …<br>Query [sep] Document Query Document<br>(a) (b) |  |
| --- | --- |
| 图 11.11<br>Figure 11.11 | 稠密检索的两种方式，图中用层间连线示意性地表-<br>Two ways to do dense retrieval, illustrated by using lines between layers to schematically rep- |

> s(q,d)

> s(q,d)

### •

> U

> zCLS zCLS_Q zCLS_D

![](images/img_268.png)

![](images/img_266.png)

![](images/img_246.png)

> … …

> … …

> … …

> … …

> … …

> … …

> 查询 [sep] 文档 查询 文档
>
> *Query [sep] Document Query Document*

(a) (b)

> 示自注意力：（a）使用单个编码器联合编码查询和文档，并针对在 CLS token 之上的线性层所产生的相关性分数进行微调。这种方式计算开销过大，除用于重排序外无法使用。（b）对查询和文档使用彼此独立的编码器，并以查询和文档的 CLS token 输出之间的点积作为分数。这种方式计算开销较小，但准确度不如前者。
>
> *resent self-attention: (a) Use a single encoder to jointly encode query and document and fine-tune to produce a relevance score with a linear layer over the CLS token. This is too compute-expensive to use except in rescoring(b) Use separate encoders for query and document, and use the dot product between CLS token outputs for the query and document as the score. This is less compute-expensive, but not as accurate.*

图 11.11a 中完整的 BERT 架构的问题在于开销，体现在

> The problem with the full BERT architecture in Fig. 11.11a is the expense in

计算和时间上。采用这种架构，每当我们收到一个查询，都必须把整个集合中的每一个文档与新查询一起送入 BERT 编码器！这种巨大的资源消耗在实际场景中是不可行的。

> computation and time. With this architecture, every time we get a query, we have to pass every single document in our entire collection through a BERT encoder jointly with the new query! This enormous use of resources is impractical for real cases.

在计算量谱系的另一端是一种高效得多的架构，即双编码器（bi-encoder）。在这种架构中，我们可以使用两个彼此独立的编码器模型，一个用于编码查询、一个用于编码文档，从而只对集合中的文档编码一次。我们预先对每个文档进行编码，并把所有编码后的文档向量存储起来。当有查询到来时，我们只对这个查询进行编码，然后以查询向量与预先计算好的文档向量之间的点积作为每个候选文档的分数（图 11.11b）。例如，如果我们使用 BERT，就会有两个编码器 BERTQ 和 BERTD，可以把查询和文档表示为各自编码器的 [CLS] token（Karpukhin et al., 2020）：

> At the other end of the computational spectrum is a much more efficient architecture, the bi-encoder. In this architecture we can encode the documents in the collection only one time by using two separate encoder models, one to encode the query and one to encode the document. We encode each document, and store all the encoded document vectors in advance. When a query comes in, we encode just this query and then use the dot product between the query vector and the precomputed document vectors as the score for each candidate document (Fig. 11.11b). For example, if we used BERT, we would have two encoders BERTQ and BERTD and we could represent the query and document as the [CLS] token of the respective encoders (Karpukhin et al., 2020):

zq = BERTQ(q)[CLS] zd = BERTD(d)[CLS] score(q,d) = zq ·zd

> (11.19)

双编码器比完整的查询/文档编码器便宜得多，但准确度也较低，因为它的相关性判定无法充分利用查询中的所有 token 与文档中的所有 token 之间所有可能的语义交互。

> The bi-encoder is much cheaper than a full query/document encoder, but is also less accurate, since its relevance decision can’t take full advantage of all the possible meaning interactions between all the tokens in the query and the tokens in the document.

介于完整编码器与双编码器之间的方法有很多。一种中间方案是先用较廉价的方法（如 BM25）对每个文档做第一轮相关性排序，取出排名前 N 的文档，再用昂贵的方法（如完整的 BERT 打分）只对这前 N 个文档而非整个集合进行重排序。

> There are numerous approaches that lie in between the full encoder and the biencoder. One intermediate alternative is to use cheaper methods (like BM25) as the first pass relevance ranking for each document, take the top N ranked documents, and use expensive methods like the full BERT scoring to rerank only the top N documents rather than the whole set.

266 第 11 章 • 基于检索的模型

> 266 CHAPTER 11 • RETRIEVAL-BASED MODELS

另一种中间方案是 Khattab and Zaharia (2020) 与 Khattab et al. (2021) 提出的 ColBERT 方法，如图 11.12 所示。该方法分别对查询和文档进行编码，但不是把整个查询或文档编码为一个向量，而是把它们各自分别编码为每个 token 的上下文表示。为了提高效率，这些对每个文档词得到的 BERT 表示可以预先存储。查询 q 与文档 d 之间的相关性分数是 q 中的 token 与 d 中的 token 之间最大相似度（MaxSim）算子之和。本质上，对于 q 中的每个 token，ColBERT 都会在 d 中找到上下文最相似的 token，然后把这些相似度相加。相关文档会包含与查询在上下文上非常相似的 token。

> Another intermediate approach is the ColBERT approach of Khattab and Zaharia (2020) and Khattab et al. (2021), shown in Fig. 11.12. This method separately encodes the query and document, but rather than encoding the entire query or document into one vector, it separately encodes each of them into contextual representations for each token. These BERT representations of each document word can be pre-stored for efficiency. The relevance score between a query q and a document d is a sum of maximum similarity (MaxSim) operators between tokens in q and tokens in d. Essentially, for each token in q, ColBERT finds the most contextually similar token in d, and then sums up these similarities. A relevant document will have tokens that are contextually very similar to the query.

> ColBERT

| s(q,d)<br>∑<br>MaxSim MaxSim MaxSim<br>norm norm norm norm norm norm<br>…<br>…<br>…<br>…<br>…<br>…<br>查询 文档<br>s(q,d)<br>∑<br>MaxSim MaxSim MaxSim<br>norm norm norm norm norm norm<br>…<br>…<br>…<br>…<br>…<br>…<br>Query Document |  |
| --- | --- |
| 图 11.12<br>Figure 11.12 | ColBERT 算法在推理时的示意图。查询和文-<br>A sketch of the ColBERT algorithm at inference time. The query and doc- |

> s(q,d)

∑

> MaxSim MaxSim MaxSim

> norm norm norm norm norm norm

![](images/img_291.png)

![](images/img_293.png)

> …

> …

> …

> …

> …

> …

> 查询 文档
>
> *Query Document*

> …文档首先分别通过独立的 BERT 编码器。查询与文档之间的相似度通过将查询与文档中词元的上下文表示之间的软对齐求和来计算。训练是端到端的。（图中未描绘各种细节；例如查询前会加上 [CLS] 和 [Q:] 词元，文档前会加上 [CLS] 和 [D:] 词元）。图改编自 Khattab and Zaharia (2020)。
>
> *ument are first passed through separate BERT encoders. Similarity between query and document is computed by summing a soft alignment between the contextual representations of tokens in the query and the document. Training is end-to-end. (Various details aren’t depicted; for example the query is prepended by a [CLS] and [Q:] tokens, and the document by [CLS] and [D:] tokens). Figure adapted from Khattab and Zaharia (2020).*

更正式地说，问题 q 被分词为 [q1,...,qn]，并在前面加上一个 [CLS]

> More formally, a question q is tokenized as [q1,...,qn], prepended with a [CLS]

以及一个特殊的 [Q] 词元，截断为 N=32 个词元（若更短则用 [MASK] 词元填充），然后通过 BERT 得到输出向量 q = [q1,...,qN]。包含词元 [d1,...,dm] 的段落 d 也以类似方式处理，其中包括一个 [CLS] 和特殊的 [D] 词元。在 d 和 q 之上应用一个线性层以控制输出维度，从而保持向量较小以提高存储效率，并将向量重新缩放为单位长度，得到最终的向量序列 Eq（长度 N）和 Ed（长度 m）。ColBERT 的打分机制为：

> and a special [Q] token, truncated to N=32 tokens (or padded with [MASK] tokens if it is shorter), and passed through BERT to get output vectors q = [q1,...,qN]. The passage d with tokens [d1,...,dm], is processed similarly, including a [CLS] and special [D] token. A linear layer is applied on top of d and q to control the output dimension, so as to keep the vectors small for storage efficiency, and vectors are rescaled to unit length, producing the final vector sequences Eq (length N) and Ed(length m). The ColBERT scoring mechanism is:

> N

X

> m

score(q,d) = max

> (11.20)

j=1 Eqi ·Edj

> i=1

尽管这种交互机制没有可调参数，ColBERT 架构仍需要端到端训练，以微调 BERT 编码器并从头训练线性层（以及特殊的 [Q] 和 [D] 嵌入）。它在由查询 q、正样本文档 d+ 与负样本文档 d− 构成的三元组 ⟨q,d+,d−⟩ 上 11.4 • 检索增强生成（RAG）267 进行训练，使用式 11.20 为每个文档生成分数，并用交叉熵损失优化模型参数。

> While the interaction mechanism has no tunable parameters, the ColBERT architecture still needs to be trained end-to-end to fine-tune the BERT encoders and train the linear layers (and the special [Q] and [D] embeddings) from scratch. It is 11.4 • RETRIEVAL-AUGMENTED GENERATION (RAG) 267 trained on triples ⟨q,d+,d−⟩of query q, positive document d+ and negative document d−to produce a score for each document using Eq. 11.20, optimizing model parameters using a cross-entropy loss.

所有监督式算法（如 ColBERT 或完全交互版本的

> All the supervised algorithms (like ColBERT or the full-interaction version of

用于重排序的 BERT 算法）都需要以查询连同相关与不相关段落或文档（正例与负例）的形式给出的训练数据。获取标签有各种半监督方法；一些数据集（如 MS MARCO Ranking，见 11.5 节）包含人工标注的正例。负例可以从某个现有 IR 系统的前 1000 条结果中随机采样。如果数据集没有已标注的正例，可以使用诸如相关性引导监督（relevance-guided supervision）这样的迭代方法（Khattab et al., 2021），这类方法依赖于许多数据集都包含简短答案字符串这一事实。在该方法中，使用现有 IR 系统来收集确实包含简短答案字符串的样本（取前几个作为正例）或不包含简短答案字符串的样本（取前几个作为负例），用它们训练一个新的检索器，然后迭代该过程。

> the BERT algorithm applied for reranking) need training data in the form of queries together with relevant and irrelevant passages or documents (positive and negative examples). There are various semi-supervised ways to get labels; some datasets(like MS MARCO Ranking, Section 11.5) contain gold positive examples. Negative examples can be sampled randomly from the top-1000 results from some existing IR system. If datasets don’t have labeled positive examples, iterative methods like relevance-guided supervision can be used (Khattab et al., 2021) which rely on the fact that many datasets contain short answer strings. In this method, an existing IR system is used to harvest examples that do contain short answer strings (the top few are taken as positives) or don’t contain short answer strings (the top few are taken as negatives), these are used to train a new retriever, and then the process is iterated.

效率是一个重要问题，因为必须对每一个可能的文档进行排序

> Efficiency is an important issue, since every possible document must be ranked

以确定其与查询的相似度。对于稀疏的词计数向量，倒排索引可以非常高效地做到这一点。对于稠密向量算法，找出与稠密查询向量点积最高的稠密文档向量集合，是最近邻搜索问题的一个实例。因此，现代系统会利用诸如 Faiss 这样的近似最近邻向量搜索算法

> for its similarity to the query. For sparse word-count vectors, the inverted index allows this very efficiently. For dense vector algorithms finding the set of dense document vectors that have the highest dot product with a dense query vector is an instance of the problem of nearest neighbor search. Modern systems therefore make use of approximate nearest neighbor vector search algorithms like Faiss

> Faiss

（Johnson et al., 2017）。

> (Johnson et al., 2017).

11.4 检索增强生成（RAG）

> 11.4 Retrieval-Augmented Generation (RAG)

我们在上一节介绍的信息检索技术，可以通过一种称为检索增强生成（retrieval-augmented generation，RAG）的方法集成到语言模型中。在本节将要描述的基本 RAG 场景中，我们使用 IR 技术从某个指定的文档库中检索可能含有有用信息的文档。然后我们使用大语言模型，在原始查询之外还以这些文档为条件来生成答案。

> The information retrieval techniques we introduced in the prior section can be integrated into language models via a method called retrieval-augmented generation or RAG. In the basic RAG scenario that we will describe in this section, we use IR techniques to retrieve documents from some specified store of documents that are likely to have useful information. Then we use a large language model to generate an answer conditioned on these documents in addition to the original query.

正如我们在本章引言中所总结的，检索增强生成有许多目标。

> As we summarized in the introduction to the chapter, there are many goals of

RAG 可以通过为模型提供一组可信文档来帮助缓解幻觉。RAG 还可以帮助语言模型生成关于专有数据的事实性文本，例如个人电子邮件、健康记录、公司内部文档或其他法律文件。RAG 还能帮助解决知识是动态的且具有时效性这一问题，例如当我们知道用户的信息需求涉及语言模型训练之后某个时间的数据时。

> retrieval-augmented generation. RAG can help mitigate hallucination, by giving the model a set of trusted documents. RAG can also help language models generate factual text about proprietary data, like personal email, or health records, or company-internal documents, or other legal documents. RAG can also help with the problem that knowledge is dynamic and time-sensitive, for example if we know the user’s information need references data from a time after a language model was trained.

一个 RAG 系统基于两个主要组件：检索器（retriever）和生成器（generator）（出于历史原因，后者有时被称为阅读器（reader）（Chen et al., 2017a））。图 11.13 勾勒出这一用于回答问题的标准模型。

> A RAG system is based on two major components: the retriever and the generator, (the latter is sometimes called, for historical reasons, the reader (Chen et al., 2017a)). Fig. 11.13 sketches out this standard model for answering questions.

> 检索-
>
> *retrieval-*

在检索增强生成（RAG）模型的第一阶段，如

> In the first stage of the retrieval-augmented generation, or RAG model shown

> 增强生成
>
> *augmented generation*

图 11.13 所示，我们从某个预先指定的文本集合中检索相关段落，

> in Fig. 11.13 we retrieve relevant passages from some prespecified text collection,

> RAG

例如使用上一节的稠密检索器。在第二阶段的生成中，我们取出检索到的段落集合，将其与用户提示整合，并把它们的某种形式传给大语言模型，以这两者为条件生成答案。

> for example using the dense retrievers of the previous section. In the second generate stage, we take the set of retrieved passages, integrate it with the user prompt, and pass some version of these to a large language model to generate an answer conditioned on these two things.

例如，设想用户提出了这样的问题：首演是哪一年 268 第 11 章 • 基于检索的模型

> For example imagine the user asks the question What year was the premiere 268 CHAPTER 11 • RETRIEVAL-BASED MODELS

| 用户提示：<br>检索器 生成器<br>何时是<br>的首演<br>《魔笛》？ 提示 LLM 1791 年，根据<br>构建<br>这一页面<br>已索引文档<br>相关知识<br>文档语料库 引用<br>文档<br>User prompt:<br>Retriever Generator<br>When was<br>the premiere of<br>The Magic Flute? Prompt LLM 1791, according<br>formulation<br>to this page<br>Indexed Docs<br>Relevant Knowledge<br>Corpus of Docs Citation<br>Documents |  |
| --- | --- |
| 图 11.13<br>Figure 11.13 | 检索增强生成以用户提示为输入（该提示可能表达一个信息<br>Retrieval-augmented generation takes as input a user prompt (which may express an informa- |

> 用户提示： 检索器
>
> *User prompt: Retriever*

![](images/img_335.png)

![](images/img_337.png)

> 生成器
>
> *Generator*

> 《魔笛》何时首演？
>
> *When was the premiere of The Magic Flute?*

![](images/img_339.png)

![](images/img_341.png)

![](images/img_341.png)

![](images/img_341.png)

![](images/img_341.png)

![](images/img_341.png)

![](images/img_341.png)

![](images/img_341.png)

![](images/img_341.png)

![](images/img_341.png)

![](images/img_341.png)

![](images/img_341.png)

![](images/img_341.png)

![](images/img_341.png)

![](images/img_341.png)

![](images/img_341.png)

![](images/img_341.png)

> 提示
>
> *Prompt*

> LLM 1791，根据
>
> *LLM 1791, according*

![](images/img_341.png)

![](images/img_341.png)

![](images/img_341.png)

> 表述
>
> *formulation*

> 这一页
>
> *to this page*

![](images/img_341.png)

![](images/img_341.png)

> 已索引文档
>
> *Indexed Docs*

> 知识
>
> *Knowledge*

> 相关
>
> *Relevant*

> 引文
>
> *Citation*

> 文档语料库 文档
>
> *Corpus of Docs Documents*

> 信息需求（如本例中的问题），以及一个可能有助于满足该信息需求的文档语料库。该方法分为两个阶段：检索，即从集合中返回相关文档；生成，即 LLM 以这些文档作为提示生成文本。有些生成结果包含知识引文，可帮助用户判断是否信任该生成结果，或在感兴趣时进一步跟进。
>
> *tion need like this question example), and a corpus of documents that may be useful in meeting the information need. The method has two stages: retrieval, which returns relevant documents from the collection, and generation, in which an LLM generates text given the documents as a prompt. Some generations include a knowledge citation that can help the user decide whether to trust the generation, or follow up if they are interested.*

《魔笛》的？我们把这个问题传给稠密检索器（dense retriever），返回一系列关于《魔笛》的段落。

> of The Magic Flute?. We pass this question to a dense retriever and return a series of passages about The Magic Flute.

检索增强生成（retrieval-augmented generation）的思想是，以检索到的段落为条件，并联合一些提示文本，例如“基于这些文本，回答这个问题：”。因此，给定文档集合 D 和用户查询 q，最基本的 RAG 算法是：

> The idea of retrieval-augmented generation is to condition on the retrieved passages, jointly with some prompt text, for example like “Based on these texts, answer this question:”. Thus given a document collection D and a user query q, the most basic RAG algorithm is:

- 调用检索器返回 R(q) = d1 ···dk，即来自 D 的前 k 个相关段落
- 构造一个包含 q 和检索到的段落的提示
- 用该提示调用 LLM

> Call a retriever to return R(q) = d1 ···dk, the top-k relevant passages from D
> Create a prompt that includes q and the retrieved passages
> Call an LLM with the prompt

得到的提示大致如下所示：

> The resulting prompts might look something like:

RAG 提示示意图

> Schematic of a RAG Prompt

检索到的段落 1

> retrieved passage 1

检索到的段落 2

> retrieved passage 2

...

检索到的段落 k

> retrieved passage k

基于这些文本，回答这个问题：《魔笛》是哪一年首演的？

> Based on these texts, answer this question: What year was the premiere of The Magic Flute?

语言模型的任务则是根据以下概率模型生成文本：

> The task for the language model is then to generate text according to this probability model:

> n

Y

p(x1,...,xn) = p(xi|R(q) ; Answer the following question... ; q ;x<i)

> i=1

这种基本 RAG 范式有许多增强方式。其中一项补充是

> There are many augmentations of this basic RAG paradigm. One addition is

使用基于智能体的 RAG（agent-based RAG）。在目前所描述的 RAG 范式中，总是先执行检索，再把检索到的段落与用户的问题组合成一个提示。但在实际应用中，我们可能不希望为用户的每一 11.5 • 数据集 269 轮都执行检索。或者我们可能希望针对不同的用户需求从不同的集合中检索（有时是网络，有时是私有集合）。在基于智能体的 RAG 中，由系统决定何时调用检索智能体以及检索哪个集合。

> the use of agent-based RAG. In the RAG paradigm described so far, a search is always run and then retrieved passages are combined with the user’s question in a prompt. But in actual applications, we may not want to run retrieval for every user 11.5 • DATASETS 269 turn. Or we may want to retrieve from different collections for different user needs(sometimes the web, other times a private collection). In agent-based RAG, the system decides when to call a retrieval agent and for which collection.

另一个研究领域涉及检索器与

> Another research area has to do with the relationship between the retriever and

生成器之间的关系。例如，检索到的段落中可能存在噪声；其中一些可能不相关或错误，或者顺序无益。我们如何促使 LLM 关注那些好段落？一些 RAG 架构加入了重排器（reranker），在段落被检索之后对其重排或重新排序。或者，一些复杂问题可能需要多跳（multi-hop）架构，即用查询检索文档，再把这些文档追加到原始查询中，进行第二阶段的检索。

> the generator. For example there may be noise in the retrieved passages; some of them may be irrelevant or wrong, or in an unhelpful order. How can we encourage the LLM to focus on the good passages? Some RAG architectures add a reranker that reranks or reorders passages after they are retrieved. Or some complex questions may require multi-hop architectures, in which a query is used to retrieve documents, which are then appended to the original query for a second stage of retrieval.

另一类解决方案是为 RAG 训练 LLM。上述

> Another class of solutions is to train the LLM for RAG. The basic version of

基本版本的 RAG 不涉及训练；我们取一个现成的 LLM，把段落和提示交给它，并希望它能正确判断哪些段落在生成答案时是有用或相关的。一种学习变体是对 LLM 进行指令微调：先构建一个数据集，其中问题标注了检索到的段落和正确答案，然后对 LLM 进行指令微调，使其能根据这些段落正确回答问题。另一种方法是通过测试时计算（test-time compute）来实现，提示 LLM 在回答问题的同时生成关于哪些段落有用的反思。生成这些反思的过程可能提升 LLM 识别好段落的能力。得到的反思文本也可用于上下文学习（in-context learning），例如把该文本用作后续问题提示的一部分。

> RAG described above involves no training; we take an off-the-shelf LLM, and give it the passages and a prompt and hope that it will correctly figure out which passages are useful or relevant in generating the answer. One learning variant involves instruction-tuning an LLM, by first creating a dataset of questions annotated with retrieved passages and correct answers, and then instruction-tuning the LLM to correctly answer the questions from the passages. An alternative method is to do this via test-time compute, prompting the LLM to answer the question and simultaneously to generate reflections on which passages were useful. The process of generating these reflections may lead the LLM to improve at identifying good passages. The resulting reflection text can also be used for in-context learning, for example by using the text as part of a prompt for further questions.

除了训练 LLM，我们还可以训练 IR 引擎。毕竟，IR

> In addition to training the LLM, we could train the IR engine. After all, the IR

引擎本身并未针对 RAG 场景进行优化。它可能从未被训练过，或者即使训练过，也很可能是针对简单 IR 或事实型问答任务训练的，而不是针对检索到的段落专门供另一个 LLM 生成文本之用的 RAG 场景。对于可训练的 IR 算法，我们可以通过在某一组问题和答案上对整个架构进行端到端训练，同时训练 IR 模型和 LLM 的参数，来解决这种不匹配。

> engine itself has not been optimized for the RAG scenario. It might not have been trained, or if it was, it was likely trained for simple IR or factoid question-answering tasks, not for the RAG scenario where the retrieved passages are specifically to be used by another LLM for generating texts. We can address this mismatch for trainable IR algorithms by doing end-to-end training of the entire architecture on some set of questions and answers, training the parameters of the IR model as well as the LLM.

最后，LLM 为任何事实性

> Finally, it is generally useful for LLMs to give the user evidence for any factual

> 知识
>
> *knowledge*

陈述向用户提供证据通常都是有用的。这可以采取知识引文的形式，例如某个

> statement. This can be in the form of knowledge citations, such as URLs of a

> 引文
>
> *citations*

可信来源的 URL，或对特定文献的引用。例如，问答系统可能会生成指向 URL 的带编号指针，如下所示：

> trusted source or citation references to particular literature. For example a question answering system might generate numbered pointers to URLs as follows:

问：哪些电影的演员阵容中有巩俐（Gong Li）？答：《秋菊打官司》（The Story of Qiu Ju）[1]、《霸王别姬》（Farewell My Concubine）[2]、《西游记之孙悟空三打白骨精》（The Monkey King 2）[3]、《花木兰》（Mulan）[3]、《兰心大剧院》（Saturday Fiction）[3] ...

> Q: Which films have Gong Li as a member of their cast? A: The Story of Qiu Ju [1], Farewell My Concubine [2], The Monkey King 2 [3], Mulan [3], Saturday Fiction [3] ...

生成知识引用最简单的方法，是把它作为

> The simplest way for generating knowledge citations is to specify it as part of

提示的一部分来指定。例如 Gao et al.（2023）使用了这样的提示文本：

> the prompt. For example Gao et al. (2023) employ a prompt with text like:

“仅使用

> ‘‘Write an answer for the given question using only the

所提供的搜索结果（其中一些可能无关）为给定问题写出答案，并正确地引用它们……对任何事实性主张都要给出引用”。

> provided search results (some of which might be irrelevant) and cite them properly... Always cite for any factual claim".

## 11.5 数据集

> 11.5 Datasets

有大量数据集以问题的形式承载信息需求，并标注了答案。它们既可用于指令微调，也可用于评估语言模型的问答能力。

> There are scores of datasets that contain information needs in the form of questions, annotated with the answer. These can be used both for instruction tuning and for evaluation of the question answering abilities of language models.

270 第 11 章 • 基于检索的模型

> 270 CHAPTER 11 • RETRIEVAL-BASED MODELS

我们可以从许多维度来区分这些数据集，

> We can distinguish the datasets along many dimensions, summarized nicely in

Rogers et al.（2023）对此做了很好的总结。其中一个维度是数据中问题的最初目的：它们是自然的信息寻求型问题，还是为探测而设计的问题——用于评估或测试系统或人类。

> Rogers et al. (2023). One is the original purpose of the questions in the data, whether they were natural information-seeking questions, or whether they were questions designed for probing: evaluating or testing systems or humans.

> 自然
>
> *Natural*

在自然类这一侧，有诸如 Natural Questions（Kwiatkowski

> On the natural side there are datasets like Natural Questions (Kwiatkowski

> 问题
>
> *Questions*

et al., 2019）这样的数据集，它是一组提交给 Google 搜索引擎的匿名化英文查询及其答案。答案由标注者依据维基百科的信息创建，包括一段段落长度的长答案和一个短片段答案。例如，问题“啤酒花在酿造过程中何时加入？”的短答案是“煮沸过程”，长答案则是维基百科 Brewing 页面中的整整一个段落。

> et al., 2019), a set of anonymized English queries to the Google search engine and their answers. The answers are created by annotators based on Wikipedia information, and include a paragraph-length long answer and a short span answer. For example the question “When are hops added to the brewing process?” has the short answer the boiling process and a long answer which is an entire paragraph from the Wikipedia page on Brewing.

一个类似的自然问题集是 MS MARCO（Microsoft Machine Reading

> A similar natural question set is the MS MARCO (Microsoft Machine Reading

> MS MARCO

Comprehension，微软机器阅读理解）数据集集合，其中包含来自 Microsoft Bing 查询日志的 100 万条真实的匿名化英文问题及人工生成的答案，以及 900 万个段落（Bajaj et al., 2016），既可用于测试检索排序，也可用于问答。

> Comprehension) collection of datasets, including 1 million real anonymized English questions from Microsoft Bing query logs together with a human generated answer and 9 million passages (Bajaj et al., 2016), that can be used both to test retrieval ranking and question answering.

尽管许多数据集以英文为主，其他语言也存在自然信息寻求型问题数据集。DuReader 数据集是一个基于搜索引擎查询和社区问答的中文问答资源（He et al., 2018）。

> Although many datasets focus on English, natural information-seeking question datasets exist in other languages. The DuReader dataset is a Chinese QA resource based on search engine queries and community QA (He et al., 2018).

TyDi QA 数据集包含来自 11 种类型学上差异很大的语言的 20.4 万对问答，其中包括阿拉伯语、孟加拉语、斯瓦希里语、俄语和泰语（Clark et al., 2020a）。在 TYDI QA 任务中，系统会收到一个问题以及来自某篇维基百科文章的若干段落，它必须 (a) 选出包含答案的段落（若没有段落包含答案则给出 NULL），以及 (b) 标出最小的答案片段（或给出 NULL）。

> TyDi QA dataset contains 204K question-answer pairs from 11 typologically diverse languages, including Arabic, Bengali, Kiswahili, Russian, and Thai (Clark et al., 2020a). In the TYDI QA task, a system is given a question and the passages from a Wikipedia article and must (a) select the passage containing the answer (or NULL if no passage contains the answer), and (b) mark the minimal answer span (or NULL).

> TyDi QA

在探测类这一侧，有 MMLU（Massive Multitask Language Understanding，大规模多任务语言理解）这样的数据集，它是一个常用的数据集，包含 57 个领域（包括医学、数学、计算机科学、法律等）的 15908 道知识与推理题。MMLU 的问题取自面向人类的各种考试，例如美国研究生入学考试（GRE）、医师资格考试和大学先修课程（AP）考试。因此，这些问题并不代表人们的信息需求，而是为学术或执业许可目的而设计、用于测试人类知识的题目。图 11.14 给出了一些示例，正确答案用粗体表示。

> On the probing side are datasets like MMLU (Massive Multitask Language Understanding), a commonly-used dataset of 15908 knowledge and reasoning questions in 57 areas including medicine, mathematics, computer science, law, and others. MMLU questions are sourced from various exams for humans, such as the US Graduate Record Exam, Medical Licensing Examination, and Advanced Placement exams. So the questions don’t represent people’s information needs, but rather are designed to test human knowledge for academic or licensing purposes. Fig. 11.14 shows some examples, with the correct answers in bold.

> MMLU

上面描述的一些问题数据集为每个问题附加了可从中抽取答案的段落。这些数据集主要是为

> Some of the question datasets described above augment each question with passage(s) from which the answer can be extracted. These datasets were mainly created

> 阅读
>
> *reading*

一种更早的、称为阅读理解的问答任务而创建的，在该任务中模型会得到

> for an earlier QA task called reading comprehension in which a model is given

> 理解
>
> *comprehension*

一个问题和一个文档，并被要求从给定文档中抽取答案。我们有时把给定一个或多个文档（例如通过 RAG）进行问答的任务称为开卷问答任务，而完全不带检索组件、直接由语言模型作答的任务则称为闭卷

> a question and a document and is required to extract the answer from the given document. We sometimes call the task of question answering given one or more documents (for example via RAG), the open book QA task, while the task of answering directly from the LM with no retrieval component at all is the closed book

> 开卷
>
> *open book*

> 闭卷
>
> *closed book*

问答任务。5 因此，如果求解器使用每个问题附带的文档，像 Natural Questions 这样的数据集就可以视为开卷；如果不使用这些文档，则视为闭卷；而像 MMLU 这样的数据集则完全是闭卷的。

> QA task.5 Thus datasets like Natural Questions can be treated as open book if the solver uses each question’s attached document, or closed book if the documents are not used, while datasets like MMLU are solely closed book.

另一个变化维度是答案的格式：选择题

> Another dimension of variation is the format of the answer: multiple-choice

还是自由形式。当然，提示方式也有种种变化，例如模型只收到问题（零样本），还是同时收到对类似问题的答案示范（少样本）。MMLU 同时提供零样本和少样本提示选项。

> versus freeform. And of course there are variations in prompting, like whether the model is just the question (zero-shot) or also given demonstrations of answers to similar questions (few-shot). MMLU offers both zero-shot and few-shot prompt options.

> 5

> 这里挪用了该词原本指代的一类考试，即允许学生“打开书本”或不允许的考试。
>
> *This repurposes the word for types of exams in which students are allowed to ‘open their books’ or not.*

11.6 • 问答评估 271

> 11.6 • EVALUATING QUESTION ANSWERING 271

MMLU 示例

> MMLU examples

大学计算机科学 任何足以表示所有布尔表达式的布尔运算符集合都称为完备的。下列哪一项不是完备的？(A) AND, NOT(B) NOT, OR(C) AND, OR(D) NAND

> College Computer Science Any set of Boolean operators that is sufficient to represent all Boolean expressions is said to be complete. Which of the following is NOT complete?(A) AND, NOT(B) NOT, OR(C) AND, OR(D) NAND

大学物理 太阳能量的主要来源是一系列热核反应，其中产生的能量等于质量差的 c2 倍，该质量差为(A) 两个氢原子与一个氦原子之间(B) 四个氢原子与一个氦原子之间(C) 六个氢原子与两个氦原子之间(D) 三个氦原子与一个碳原子之间

> College Physics The primary source of the Sun’s energy is a series of thermonuclear reactions in which the energy produced is c2 times the mass difference between(A) two hydrogen atoms and one helium atom(B) four hydrogen atoms and one helium atom(C) six hydrogen atoms and two helium atoms(D) three helium atoms and one carbon atom

国际法 下列哪一项是基于条约的人权机制？(A) 联合国人权事务委员会(B) 联合国人权理事会(C) 联合国普遍定期审议(D) 联合国特别任务

> International Law Which of the following is a treaty-based human rights mechanism?(A) The UN Human Rights Committee(B) The UN Human Rights Council(C) The UN Universal Periodic Review(D) The UN special mandates

史前史 与大多数其他早期文明不同，米诺斯文化几乎没有显示出以下方面的证据：(A) 贸易。(B) 战争。(C) 共同宗教的发展。(D) 精英的炫耀性消费。

> Prehistory Unlike most other early civilizations, Minoan culture shows little evidence of(A) trade.(B) warfare.(C) the development of a common religion.(D) conspicuous consumption by elites.

> 图 11.14 MMLU 中的示例问题
>
> *Figure 11.14 Example problems from MMLU*

## 11.6 评估问答

> 11.6 Evaluating Question Answering

评估问答系统通常采用两种技术，具体选择取决于问题的类型和问答场景。对于像 MMLU 中那样的多项选择题，我们报告精确匹配：

> Two techniques are commonly employed to evaluate question-answering systems, with the choice depending on the type of question and QA situation. For multiple choice questions like in MMLU, we report exact match:

精确匹配：与标准答案完全一致的预测答案所占的百分比。

> Exact match: The % of predicted answers that match the gold answer exactly.

对于答案形式为自由文本的问题，例如 Natural Questions，我们通常用词元 F1 分数来评估，以粗略衡量答案与参考答案之间的字符串部分重叠：

> For questions with free text answers, like Natural Questions, we commonly evaluated with token F1 score to roughly measure the partial string overlap between the answer and the reference answer:

F1 分数：预测答案与标准答案之间词元重叠的平均值。将预测答案和标准答案视为词元袋，对每个问题计算 F1，然后返回所有问题 F1 的平均值。

> F1 score: The average token overlap between predicted and gold answers. Treat the prediction and gold as a bag of tokens, and compute F1 for each question, then return the average F1 over all questions.

272 第 11 章 • 基于检索的模型

> 272 CHAPTER 11 • RETRIEVAL-BASED MODELS

## 11.7 小结

> 11.7 Summary

本章介绍了信息检索的任务，以及如何使用检索增强生成（RAG）来利用检索到的段落改进问答和大语言模型的其他事实性生成。

> This chapter introduced the tasks of information retrieval and the use of retrieval augmented generation (RAG) to use retrieved passages to improve question answering and other factual generations from LLMs.

- 本章重点关注信息检索在问答以及相关基于事实的任务中的应用。其思路是利用某一文档集合（可能是网络）中的材料来满足用户的信息需求。
- 信息检索（IR）的任务是根据用户在查询中表达的信息需求，向用户返回文档。在排序检索中，文档按排序后的顺序返回。
- 信息检索的两大范式是稀疏检索和稠密检索。两种范式都用文档与查询的相似度来估计其与用户信息需求的相关性。
- 在稀疏检索技术中，我们把查询和文档都表示为其所含词的一元计数的稀疏向量，每个计数由 tf-idf 或 BM25 加权。于是查询与文档的相似度可以用这些稀疏向量之间的余弦来度量。
- 倒排索引是稀疏检索的一种存储机制，它使查找含有特定词的文档变得非常高效。
- 在稠密检索技术中，文档或查询则被表示为由语言模型（无论是 BERT 系列这类仅编码器模型，还是仅解码器模型）计算得到的嵌入（稠密向量）。文档与查询的相似度在嵌入空间中按点积或余弦计算。
- 对于稠密检索，FAISS 是一种近似最近邻向量搜索算法，它能非常高效地找到与查询嵌入最相似的 k 个文档嵌入，从而快速完成排序。
- 排序检索通常用平均精度均值或插值精度来评估。
- 检索可以通过检索增强生成被纳入语言建模。在检索步骤中，用户查询被传给搜索引擎，以检索出一组相关的文档或段落。在生成阶段，用查询以及从集合中检索出的一组文档来提示大语言模型，然后有条件地生成答案。
- 像问答这样的事实性任务，如果只给出单一答案，可以用与已知答案的精确匹配来评估；对于自由文本答案，则用词元 F1 分数。

> We focus in this chapter on the use of information retrieval for question answering and related factually-based tasks. The idea is to meet the user’s information needs by drawing on the material in some set of documents (which might be the web).
> Information Retrieval (IR) is the task of returning documents to a user based on their information need as expressed in a query. In ranked retrieval, the documents are returned in ranked order.
> Two paradigms for IR are sparse retrieval and dense retrieval. Both paradigms use a document’s similarity to the query as an estimate of its relevance to the user’s information need.
> In sparse retrieval techniques, we represent both the query and the document as sparse vectors of the unigram counts of the words they contain, each count weighted by tf-idf or BM25. Then the query-document similarity can be measured by the cosine between these sparse vectors.
> The inverted index is a storage mechanism for sparse retrieval that makes it very efficient to find documents that have a particular word.
> In dense retrieval techniques, documents or queries are instead represented as embeddings (dense vectors) computed by a language model (whether encoderonly models like the BERT family, or decoder-only). Document-query similarity is computed as dot product or cosine in they embedding space.
> For dense retrieval, FAISS is an approximate nearest neighbor vector search algorithm that makes it very efficient to find the k most similar document embeddings to a query embedding, making it quick to do ranking.
> Ranked retrieval is generally evaluated by mean average precision or interpolated precision.
> Retrieval can be incorporated into language modeling via retrieval-augmented generation. In the retrieval step, the user query is passed to the search engine to retrieve a set of relevant documents or passages. In the generation stage, a large language model is prompted with the query and a set of documents retrieved from the collection, and then conditionally generates an answer.
> Factual tasks like question answering can be evaluated by exact match with a known answer if only a single answer is given, with token F1 score for free text answers.

## 历史注记

> Historical Notes

问答是最早的自然语言处理任务之一。到 1961 年，BASEBALL 系统（Green et al., 1961）通过查询一个结构化的比赛信息数据库，回答了诸如“Where did the Red Sox play on July 7”这类关于棒球比赛的问题。该数据库以一种属性—值矩阵的形式存储，其中给出每场比赛各属性的取值：

> Question answering was one of the earliest NLP tasks. By 1961 the BASEBALL system (Green et al., 1961) answered questions about baseball games like “Where did the Red Sox play on July 7” by querying a structured database of game information. The database was stored as a kind of attribute-value matrix with values for attributes of each game:

历史注记 273

> HISTORICAL NOTES 273

Month = July

Place = Boston

Day = 7 Game Serial No. = 96(Team = Red Sox, Score = 5)(Team = Yankees, Score = 3)

每个问题都使用 Zellig Harris 的算法进行成分句法分析

> Each question was constituency-parsed using the algorithm of Zellig Harris’s

即宾夕法尼亚大学的 TDAP 项目，它本质上是一系列有限状态转换器的级联（参见 Joshi and Hopely 1999 和 Karttunen 1999 中的历史讨论）。随后在内容分析阶段，每个词或短语都与一个计算其部分含义的程序相关联。因此，短语“Where”配有赋予语义 Place = ? 的代码，结果是问题“Where did the Red Sox play on July 7”被赋予含义

> TDAP project at the University of Pennsylvania, essentially a cascade of finite-state transducers (see the historical discussion in Joshi and Hopely 1999 and Karttunen 1999). Then in a content analysis phase each word or phrase was associated with a program that computed parts of its meaning. Thus the phrase ‘Where’ had code to assign the semantics Place = ?, with the result that the question “Where did the Red Sox play on July 7” was assigned the meaning

Place = ? Team = Red Sox Month = July Day = 7

然后将该问题与数据库进行匹配，从而返回答案。

> The question is then matched against the database to return the answer.

Simmons 等人（1964）的 Protosynthex 系统在给定一个问题时，会构造一个

> The Protosynthex system of Simmons et al. (1964), given a question, formed a

查询，其内容词取自问题中的实词，然后在文档中检索候选答案句，并按它们与问题的频率加权词项重叠度排序。之后用依存句法分析器对查询和每个检索到的句子进行句法分析，并选出结构最匹配问题结构的句子。因此，问题 What do worms eat? 会匹配 worms eat grass：在当时使用的依存语法版本中，两者都以主语 worms 作为 eat 的依存项；而 birds eat worms 的主语是 birds：

> query from the content words in the question, and then retrieved candidate answer sentences in the document, ranked by their frequency-weighted term overlap with the question. The query and each retrieved sentence were then parsed with dependency parsers, and the sentence whose structure best matches the question structure selected. Thus the question What do worms eat? would match worms eat grass: both have the subject worms as a dependent of eat, in the version of dependency grammar used at the time, while birds eat worms has birds as the subject:

What do worms eat Worms eat grass Birds eat worms

Simmons（1965）总结了其他早期的问答系统。到 20 世纪 70 年代，系统使用谓词演算作为意义表示

> Simmons (1965) summarizes other early QA systems. By the 1970s, systems used predicate calculus as the meaning representation

语言。LUNAR 系统（Woods et al. 1972, Woods 1978）的设计目标是

> language. The LUNAR system (Woods et al. 1972, Woods 1978) was designed to

> LUNAR

成为关于月球地质的化学事实数据库的自然语言接口。它能够回答诸如 Do any samples have greater than 13 percent aluminum 这样的问题，方法是将它们解析为逻辑形式

> be a natural language interface to a database of chemical facts about lunar geology. It could answer questions like Do any samples have greater than 13 percent aluminum by parsing them into a logical form

(TEST (FOR SOME X16 / (SEQ SAMPLES) : T ; (CONTAIN’ X16(NPR* X17 / (QUOTE AL203)) (GREATERTHAN 13 PCT))))

到 20 世纪 90 年代，问答转向了机器学习。Zelle 和 Mooney

> By the 1990s question answering shifted to machine learning. Zelle and Mooney

（1996）提出把问答视为一项语义分析任务，并为此创建了基于 Prolog 的 GEOQUERY 数据集，其中包含关于美国地理的问题。该模型由 Zettlemoyer 和 Collins（2005）以及 2007 年的工作加以扩展。又过了十年，神经模型被应用于语义分析（Dong and Lapata 2016, Jia and Liang 2016），随后又通过把文本映射为 SQL 应用于基于知识的问答（Iyer et al., 2017）。

> (1996) proposed to treat question answering as a semantic parsing task, by creating the Prolog-based GEOQUERY dataset of questions about US geography. This model was extended by Zettlemoyer and Collins (2005) and 2007. By a decade later, neural models were applied to semantic parsing (Dong and Lapata 2016, Jia and Liang 2016), and then to knowledge-based question answering by mapping text to SQL (Iyer et al., 2017).

［待补：信息检索的历史。］与此同时，一种更多借助信息检索的问答范式受到了 20 世纪 90 年代网络兴起的影响。美国政府——274 第 11 章 • 基于检索的模型——资助的 TREC（Text REtrieval Conference，文本检索会议）评测自 1992 年起每年举办，为评估信息检索任务与技术提供了试验平台（Voorhees and Harman, 2005）。TREC 在 1999 年增设了一个颇具影响力的问答赛道，由此催生了各种各样的事实型与非事实型问答系统在年度评测中同台竞技。

> [TBD: History of IR.] Meanwhile, a paradigm for answering questions that drew more on informationretrieval was influenced by the rise of the web in the 1990s. The U.S. government- 274 CHAPTER 11 • RETRIEVAL-BASED MODELS sponsored TREC (Text REtrieval Conference) evaluations, run annually since 1992, provide a testbed for evaluating information-retrieval tasks and techniques (Voorhees and Harman, 2005). TREC added an influential QA track in 1999, which led to a wide variety of factoid and non-factoid question answering systems competing in annual evaluations.

在同一时期，Hirschman 等人（1999）提出了利用儿童阅读理解测试来评估机器文本理解算法的想法。他们获取了一个由 120 篇短文组成的语料库，每篇配有 5 个为 3—6 年级儿童设计的问题，构建了一个答案抽取系统，并衡量其系统给出的答案与测试出版方提供的参考答案之间的吻合程度。他们的算法以词重叠作为特征；后来的算法则加入了命名实体特征以及问题与答案片段之间更复杂的相似度（Riloff and Thelen 2000, Ng et al. 2000）。

> At that same time, Hirschman et al. (1999) introduced the idea of using children’s reading comprehension tests to evaluate machine text comprehension algorithms. They acquired a corpus of 120 passages with 5 questions each designed for 3rd-6th grade children, built an answer extraction system, and measured how well the answers given by their system corresponded to the answer key from the test’s publisher. Their algorithm focused on word overlap as a feature; later algorithms added named entity features and more complex similarity between the question and the answer span (Riloff and Thelen 2000, Ng et al. 2000).

Watson Jeopardy! 系统的 DeepQA 组件是一个大型而精密的基于特征的系统，开发于神经系统普及之前不久。它在《IBM Journal of Research and Development》第 56 卷的一系列论文中有介绍，例如 Ferrucci (2012)。

> The DeepQA component of the Watson Jeopardy! system was a large and sophisticated feature-based system developed just before neural systems became common. It is described in a series of papers in volume 56 of the IBM Journal of Research and Development, e.g., Ferrucci (2012).

早期的神经阅读理解系统借鉴了一个共同的洞见

> Early neural reading comprehension systems drew on the insight common to

早期系统认为答案查找应聚焦于问题与段落的相似度。这些神经系统的许多架构概要由 Hermann et al.(2015)、Chen et al. (2017a) 和 Seo et al. (2017) 提出。这些系统关注 Rajpurkar et al. (2016)、Rajpurkar et al. (2018) 等数据集及其后续版本，通常使用独立的 IR 算法作为神经阅读理解系统的输入。将稠密检索与基于片段的阅读器相结合（常常采用单一端到端架构）这一范式，以 Lee et al. (2019) 或 Karpukhin et al. (2020) 等系统为代表。面向开放域问答的稠密检索的一个重要研究领域是训练数据：使用自监督方法以避免标注正、负段落（Sachan et al., 2023）。

> early systems that answer finding should focus on question-passage similarity. Many of the architectural outlines of these neural systems were laid out in Hermann et al.(2015), Chen et al. (2017a), and Seo et al. (2017). These systems focused on datasets like Rajpurkar et al. (2016) and Rajpurkar et al. (2018) and their successors, usually using separate IR algorithms as input to neural reading comprehension systems. The paradigm of using dense retrieval with a span-based reader, often with a single endto-end architecture, is exemplified by systems like Lee et al. (2019) or Karpukhin et al. (2020). An important research area with dense retrieval for open-domain QA is training data: using self-supervised methods to avoid having to label positive and negative passages (Sachan et al., 2023).

关于大语言模型的早期工作表明，它们在预训练过程中存储了足够的知识来回答问题（Petroni et al., 2019；Raffel et al., 2020；Radford et al., 2019；Roberts et al., 2020），起初无法与专用问答系统竞争，但很快便超越了它们。检索增强生成算法最初是作为改进语言建模词预测的一种方式被提出的（Khandelwal et al., 2019），但很快就被应用于问答（Izacard et al., 2022；Ram et al., 2023；Shi et al., 2023）。

> Early work on large language models showed that they stored sufficient knowledge in the pretraining process to answer questions (Petroni et al., 2019; Raffel et al., 2020; Radford et al., 2019; Roberts et al., 2020), at first not competitively with special-purpose question answerers, but quickly surpassing them. Retrievalaugmented generation algorithms were first introduced as a way to improve language modeling word prediction (Khandelwal et al., 2019), but were quickly applied to question answering (Izacard et al., 2022; Ram et al., 2023; Shi et al., 2023).

## 练习

> Exercises
