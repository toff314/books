# 第 5 章 嵌入

### 章

> CHAPTER

# 5 嵌入

> 5 Embeddings

荃者所以在鱼，得鱼而忘荃 网是为了捕鱼；

> 荃者所以在鱼，得鱼而忘荃Nets are for fish;

捕到鱼之后，就可以忘掉网。

> Once you get the fish, you can forget the net.

言者所以在意，得意而忘言 言语是为了表达意义；

> 言者所以在意，得意而忘言Words are for meaning;

领会了意义之后，就可以忘掉言语

> Once you get the meaning, you can forget the words

> 庄子（Zhuangzi），第 26 章
>
> *庄子(Zhuangzi), Chapter 26*

洛杉矶闻名于世的沥青主要出现在它的高速公路上。但

> The asphalt that Los Angeles is famous for occurs mainly on its freeways. But

在市中心还有另一片沥青地，即拉布雷亚沥青坑（La Brea tar pits），这片沥青保存了来自更新世（Pleistocene Epoch）最后一个冰期的数百万块化石骨骼。这些化石中有一件是斯剑虎（Smilodon），即剑齿虎，凭其长长的犬齿一眼即可辨认。大约五百万年前，一种完全不同的剑齿虎——袋剑虎（Thylacosmilus）——生活在阿根廷以及南美洲的其他地区。Thylacosmilus 是有袋类动物，而 Smilodon 是胎盘哺乳动物，但 Thylacosmilus 拥有同样长长的上犬齿，并且和 Smilodon 一样，下颌上有一块起保护作用的骨质凸缘。这两种哺乳动物的相似性是平行演化或趋同演化的众多例证之一，在这类演化中，特定的语境或环境导致不同物种演化出极为相似的结构（Gould, 1980）。

> in the middle of the city is another patch of asphalt, the La Brea tar pits, and this asphalt preserves millions of fossil bones from the last of the Ice Ages of the Pleistocene Epoch. One of these fossils is the Smilodon, or saber-toothed tiger, instantly recognizable by its long canines. Five million years ago or so, a completely different saber-tooth tiger called Thylacosmilus lived in Argentina and other parts of South America. Thylacosmilus was a marsupial whereas Smilodon was a placental mammal, but Thylacosmilus had the same long upper canines and, like Smilodon, had a protective bone flange on the lower jaw. The similarity of these two mammals is one of many examples of parallel or convergent evolution, in which particular contexts or environments lead to the evolution of very similar structures in different species (Gould, 1980).

![](images/img_84.jpeg)

语境的作用在一种不那么具有生物学色彩的

> The role of context is also important in the similarity of a less biological kind

生物体——词——的相似性中同样重要。出现在相似语境中的词往往具有相似的意义。词在分布方式上的相似性与

> of organism: the word. Words that occur in similar contexts tend to have similar meanings. This link between similarity in how words are distributed and similarity

> 分布的
>
> *distributional*

它们在意义上所具有的相似性之间的联系，被称为分布假说（distributional hypothesis）。该假说

> in what they mean is called the distributional hypothesis. The hypothesis was

> 假说
>
> *hypothesis*

最早由 Joos（1950）、Harris（1954）和 Firth（1957）等语言学家在 20 世纪 50 年代提出，他们注意到，互为同义词的词（如 oculist 与 eye-doctor）往往出现在相同的环境之中（例如出现在 eye 或 examined 这类词附近），而两个词之间意义差异的大小“大致对应于它们环境差异的大小”（Harris, 1954, p. 157）。

> first formulated in the 1950s by linguists like Joos (1950), Harris (1954), and Firth(1957), who noticed that words which are synonyms (like oculist and eye-doctor) tended to occur in the same environment (e.g., near words like eye or examined) with the amount of meaning difference between two words “corresponding roughly to the amount of difference in their environments” (Harris, 1954, p. 157).

本章介绍嵌入，即词的意义的向量表示，

> In this chapter we introduce embeddings, vector representations of the meaning

> 嵌入
>
> *embeddings*

这种表示直接从文本中的词分布学习得到。嵌入位于大语言模型以及其他现代应用的核心。我们在此介绍的静态嵌入，是第 7 章和第 9 章将看到的 BERT 之类更强大的动态嵌入（或称语境化嵌入）的基础。

> of words that are learned directly from word distributions in texts. Embeddings lie at the heart of large language models and other modern applications. The static embeddings we introduce here underlie the more powerful dynamic or contextualized embeddings like BERT that we will see in Chapter 7 and Chapter 9.

研究嵌入及其意义的语言学领域被称为向量

> The linguistic field that studies embeddings and their meanings is called vector

> 向量
>
> *vector*

语义学。嵌入也是本书中表示学习的第一个例子，

> semantics. Embeddings are also the first example in this book of representation

> 表示语义
>
> *representation semantics*

即自动学习输入文本的有用表示。寻找

> learning, automatically learning useful representations of the input text. Finding

> 学习
>
> *learning*

这种以自监督方式学习语言表示、而不是通过特征工程手工构造表示的做法，是现代自然语言处理（NLP）的一条重要原则（Bengio et al., 2013）。

> such self-supervised ways to learn representations of language, instead of creating representations by hand via feature engineering, is an important principle of modern NLP (Bengio et al., 2013).

128 第 5 章 • 嵌入

> 128 CHAPTER 5 • EMBEDDINGS

## 5.1 词汇语义

> 5.1 Lexical Semantics

我们先从词义的一些基本原理讲起。我们应当如何表示一个词的意义？在第 3 章的 n-gram 模型以及经典的自然语言处理应用中，我们对一个词唯一的表示就是一串字母，或者词表中的一个索引。这种表示与哲学中的一种传统并没有多大差别——也许你在逻辑学入门课上见过它——那种传统仅仅用小型大写字母拼写出词来表示词的意义：把“dog”的意义表示为 DOG，把“cat”的表示为 CAT，或者使用一个撇号（DOG’）。

> Let’s begin by introducing some basic principles of word meaning. How should we represent the meaning of a word? In the n-gram models of Chapter 3, and in classical NLP applications, our only representation of a word is as a string of letters, or an index in a vocabulary list. This representation is not that different from a tradition in philosophy, perhaps you’ve seen it in introductory logic classes, in which the meaning of words is represented by just spelling the word with small capital letters; representing the meaning of “dog” as DOG, and “cat” as CAT, or by using an apostrophe (DOG’).

通过把词大写的办法来表示一个词的意义，是一种相当不令人满意的

> Representing the meaning of a word by capitalizing it is a pretty unsatisfactory

模型。你可能见过一个最初出自语义学家 Barbara Partee 的笑话的某个版本（Carlson, 1977）：

> model. You might have seen a version of a joke due originally to semanticist Barbara Partee (Carlson, 1977):

问：生命的意义是什么？答：LIFE’

> Q: What’s the meaning of life? A: LIFE’

我们肯定能做得比这更好！毕竟，我们希望一个词义模型

> Surely we can do better than this! After all, we’ll want a model of word meaning

能为我们做各种各样的事情。它应当告诉我们，有些词意义相近（cat 与 dog 相近），有些词互为反义词（cold 是 hot 的反面），有些词带有正面内涵（happy），而另一些词带有负面内涵（sad）。它应当表示出这一事实：buy、sell 和 pay 的意义为同一个底层的购买事件提供了不同的视角。（如果我从你那里买了某样东西，你很可能把它卖给了我，而我很可能付了钱给你。）更一般地说，词义模型应当让我们能够进行推理，以处理问答或对话之类与意义相关的任务。

> to do all sorts of things for us. It should tell us that some words have similar meanings (cat is similar to dog), others are antonyms (cold is the opposite of hot), some have positive connotations (happy) while others have negative connotations (sad). It should represent the fact that the meanings of buy, sell, and pay offer differing perspectives on the same underlying purchasing event. (If I buy something from you, you’ve probably sold it to me, and I likely paid you.) More generally, a model of word meaning should allow us to draw inferences to address meaning-related tasks like question-answering or dialogue.

本节我们总结其中一些需求，所依据的是

> In this section we summarize some of these desiderata, drawing on results in the

> 词汇
>
> *lexical*

语言学对词义的研究成果，这项研究被称为词汇语义学；我们将回到

> linguistic study of word meaning, which is called lexical semantics; we’ll return to

> 语义
>
> *semantics*

并在附录 I 和第 22 章中扩充这一列表。

> and expand on this list in Appendix I and Chapter 22.

词元与义项 我们先来看一个词（我们选 mouse）在词典中可能如何被定义（简化自在线词典 WordNet）：

> Lemmas and Senses Let’s start by looking at how one word (we’ll choose mouse) might be defined in a dictionary (simplified from the online dictionary WordNet):

> mouse（名词）
>
> *mouse (N)*

> 1. 众多小型啮齿动物中的任意一种……
>
> *1. any of numerous small rodents...*

> 2. 一种控制光标的手持设备……
>
> *2. a hand-operated device that controls a cursor...*

这里，形式 mouse 就是词元（lemma），也称为引用形式（citation form）。形式

> Here the form mouse is the lemma, also called the citation form. The form

> 词元
>
> *lemma*

mouse 也同样是单词 mice 的词元；词典不会为

> mouse would also be the lemma for the word mice; dictionaries don’t have separate

> 引用形式
>
> *citation form*

mice 这类屈折形式单独列出释义。同样，sing 是 sing、sang、sung 的词元。在许多语言中，动词的不定式形式被用作该动词的词元，因此西班牙语 dormir“睡觉”是 duermes“你睡觉”的词元。sung、carpets、sing 或 duermes 这些具体形式称为词形（wordform）。

> definitions for inflected forms like mice. Similarly sing is the lemma for sing, sang, sung. In many languages the infinitive form is used as the lemma for the verb, so Spanish dormir “to sleep” is the lemma for duermes “you sleep”. The specific forms sung or carpets or sing or duermes are called wordforms.

> 词形
>
> *wordform*

如上例所示，每个词元都可能有多个含义；

> As the example above shows, each lemma can have multiple meanings; the

词元 mouse 既可以指这种啮齿动物，也可以指光标控制设备。我们把 mouse 含义的每一个方面称为一个词义（word sense）。词元可能是一词多义的（具有多个词义），这一事实会使理解变得困难（搜索“mouse info”的人是想找宠物还是想找控件？）。第 9 章和附录 I 将讨论多义性问题，并介绍词义消歧（word sense disambiguation），即判定某个词在特定上下文中使用的是哪个词义的任务。

> lemma mouse can refer to the rodent or the cursor control device. We call each of these aspects of the meaning of mouse a word sense. The fact that lemmas can be polysemous (have multiple senses) can make interpretation difficult (is someone who searches for “mouse info” looking for a pet or a widget?). Chapter 9 and Appendix I will discuss the problem of polysemy, and introduce word sense disambiguation, the task of determining which sense of a word is being used in a particular context.

同义关系（Synonymy） 词义的一个重要组成部分是词义之间的关系。例如，当一个词的某个词义与另一个词的某个词义 5.1 • 词汇语义学 129 相同或几乎相同时，我们就说这两个词的这两个词义是同义词。同义词包括这样一些词对：

> Synonymy One important component of word meaning is the relationship between word senses. For example when one word has a sense whose meaning is 5.1 • LEXICAL SEMANTICS 129 identical to a sense of another word, or nearly identical, we say the two senses of those two words are synonyms. Synonyms include such pairs as

> 同义词
>
> *synonym*

couch/sofa（长沙发/沙发） vomit/throw up（呕吐/吐） filbert/hazelnut（榛子/榛子） car/automobile（汽车/汽车）

> couch/sofa vomit/throw up filbert/hazelnut car/automobile

同义关系（指词与词之间而非词义之间）更形式化的定义是，

> A more formal definition of synonymy (between words rather than senses) is that

如果两个词在任何句子中都能相互替换而不改变该句的真值条件，即使该句为真的那些情境，那么这两个词就是同义的。

> two words are synonymous if they are substitutable for one another in any sentence without changing the truth conditions of the sentence, the situations in which the sentence would be true.

虽然 car / automobile 或 water / H2O 这类词对之间的替换是保真的，但这些词在含义上仍然并不相同。事实上，恐怕没有任何两个词在含义上是绝对相同的。……其中一条基本

> While substitutions between some pairs of words like car / automobile or water / H2O are truth preserving, the words are still not identical in meaning. Indeed, probably no two words are absolutely identical in meaning. One of the fundamental

> 的原则
>
> *principle of*

语义学信条，称为对比原则（Girard 1718，Br´eal 1897，Clark

> tenets of semantics, called the principle of contrast (Girard 1718, Br´eal 1897, Clark

> 对比
>
> *contrast*

1987），它指出：语言形式上的差异总是与某种含义上的差异相关联。例如，H2O 一词用于科学语境，用在徒步指南中就不合适——water 会更恰当——而这种体裁上的差异也是该词含义的一部分。因此在实际使用中，synonym（同义词）一词描述的是近似或粗略的同义关系。

> 1987), states that a difference in linguistic form is always associated with some difference in meaning. For example, the word H2O is used in scientific contexts and would be inappropriate in a hiking guide—water would be more appropriate— and this genre difference is part of the meaning of the word. In practice, the word synonym is therefore used to describe a relationship of approximate or rough synonymy.

词的相似性（Word Similarity） 虽然拥有很多同义词的词并不多，但大多数词确实都有许多相似的词。Cat 不是 dog 的同义词，但 cats 和 dogs 无疑是相似的词。从同义关系转向相似性时，把话题从词义之间的关系（如同义关系）转向词与词之间的关系（如相似性）会很有用。以词为处理对象，就不必确定某种特定的词义表示方式，而这最终会简化我们的任务。

> Word Similarity While words don’t have many synonyms, most words do have lots of similar words. Cat is not a synonym of dog, but cats and dogs are certainly similar words. In moving from synonymy to similarity, it will be useful to shift from talking about relations between word senses (like synonymy) to relations between words (like similarity). Dealing with words avoids having to commit to a particular representation of word senses, which will turn out to simplify our task.

词的相似性这一概念在更大的语义任务中非常有用。了解

> The notion of word similarity is very useful in larger semantic tasks. Knowing

> 相似性
>
> *similarity*

两个词有多相似，有助于计算两个短语或句子的含义有多相似，而这在问答、复述和摘要等任务中是非常重要的组成部分。获取词的相似性数值的一种方法是请人来判断一个词与另一个词有多相似。这类实验已经产生了一些数据集。例如，SimLex-999 数据集（Hill 等，2015）给出 0 到 10 的评分，如下面的例子所示，其范围从近义词（vanish、disappear）到似乎几乎没有共同之处的词对（hole、agreement）：

> how similar two words are can help in computing how similar the meaning of two phrases or sentences are, a very important component of tasks like question answering, paraphrasing, and summarization. One way of getting values for word similarity is to ask humans to judge how similar one word is to another. A number of datasets have resulted from such experiments. For example the SimLex-999 dataset (Hill et al., 2015) gives values on a scale from 0 to 10, like the examples below, which range from near-synonyms (vanish, disappear) to pairs that scarcely seem to have anything in common (hole, agreement):

| vanish（消失）<br>vanish | disappear（消失）<br>disappear | 9.8 |
| --- | --- | --- |
| belief（信念）<br>belief | impression（印象）<br>impression | 5.95 |
| muscle（肌肉）<br>muscle | bone（骨头）<br>bone | 3.65 |
| modest（谦虚的）<br>modest | flexible（灵活的）<br>flexible | 0.98 |
| hole（洞）<br>hole | agreement（一致）<br>agreement | 0.3 |

belief（信念） impression（印象） 5.95 muscle（肌肉） bone（骨头） 3.65 modest（谦虚的） flexible（灵活的） 0.98

> belief impression 5.95 muscle bone 3.65 modest flexible 0.98

词的相关性（Word Relatedness） 两个词的含义可以以相似之外的其他方式相关联。其中一类联系称为词的相关性（word relatedness）（Budanitsky

> Word Relatedness The meaning of two words can be related in ways other than similarity. One such class of connections is called word relatedness (Budanitsky

> 相关性
>
> *relatedness*

与 Hirst，2006），在心理学中也历来称为词联想（word association）。

> and Hirst, 2006), also traditionally called word association in psychology.

> 联想
>
> *association*

考察 coffee 和 cup 这两个词的含义。coffee 与 cup 并不相似；

> Consider the meanings of the words coffee and cup. Coffee is not similar to cup;

它们几乎不共享任何特征（coffee 是一种植物或一种饮料，而 cup 是一件具有特定形状的人造物品）。但 coffee 和 cup 显然相关；它们通过共同参与一个日常事件（用杯子喝咖啡这一事件）而相互关联。同样，scalpel 和 surgeon 并不相似，但通过事件相关联（外科医生往往会使用手术刀）。

> they share practically no features (coffee is a plant or a beverage, while a cup is a manufactured object with a particular shape). But coffee and cup are clearly related; they are associated by co-participating in an everyday event (the event of drinking coffee out of a cup). Similarly scalpel and surgeon are not similar but are related eventively (a surgeon tends to make use of a scalpel).

词与词之间一种常见的相关性是它们属于同一

> One common kind of relatedness between words is if they belong to the same

语义场。语义场是一组覆盖某一特定语义

> semantic field. A semantic field is a set of words which cover a particular semantic

> 语义场
>
> *semantic field*

领域并彼此具有结构化关系的词的集合。例如，有些词可能 130 第 5 章 • 嵌入 因为同属医院（surgeon、scalpel、nurse、anesthetic、hospital）、餐馆（waiter、menu、plate、food、chef）或住宅（door、roof、kitchen、family、bed）的语义场而相互关联。语义场还与一种称为主题模型（topic models）的形式化方法相关，例如潜在狄利克雷分配（Latent Dirichlet Allocation，LDA），它在大规模文本集合上应用无监督学习，从文本中归纳出相关联的词集。语义场和主题模型是发现文档中主题结构的非常有用的工具。

> domain and bear structured relations with each other. For example, words might be 130 CHAPTER 5 • EMBEDDINGS related by being in the semantic field of hospitals (surgeon, scalpel, nurse, anesthetic, hospital), restaurants (waiter, menu, plate, food, chef), or houses (door, roof, kitchen, family, bed). Semantic fields are also related to a formalism called topic models, like Latent Dirichlet Allocation, LDA, which apply unsupervised learning on large sets of texts to induce sets of associated words from text. Semantic fields and topic models are very useful tools for discovering topical structure in documents.

> 主题模型
>
> *topic models*

在附录 I 中，我们将介绍更多词义之间的关系，例如上位关系（hypernymy）或

> In Appendix I we’ll introduce more relations between senses like hypernymy or

IS-A、反义关系（即对立）以及部分—整体关系（meronymy）。

> IS-A, antonymy (opposites) and meronymy (part-whole relations).

内涵意义（Connotation） 最后，词还具有情感意义或内涵意义。这个词

> Connotation Finally, words have affective meanings or connotations. The word

> 内涵义
>
> *connotations*

内涵义在不同领域有不同的含义，但在这里我们用它来指词义中与作者或读者的情绪、情感、观点或评价相关的那些方面。例如，有些词带有正面内涵义（wonderful），而另一些词带有负面内涵义（dreary）。即使在其它方面意义相近的词，内涵义也可能不同；试比较 fake、knockoff、forgery 与 copy、replica、reproduction 之间内涵义的差异，或者 innocent（正面内涵义）与 naive（负面内涵义）的差异。有些词表达正面评价（great、love），另一些则表达负面评价（terrible、hate）。表达正面或负面评价的语言称为情感，而词的情感在诸如情感

> connotation has different meanings in different fields, but here we use it to mean the aspects of a word’s meaning that are related to a writer or reader’s emotions, sentiment, opinions, or evaluations. For example some words have positive connotations (wonderful) while others have negative connotations (dreary). Even words whose meanings are similar in other ways can vary in connotation; consider the difference in connotations between fake, knockoff, forgery, on the one hand, and copy, replica, reproduction on the other, or innocent (positive connotation) and naive (negative connotation). Some words describe positive evaluation (great, love) and others negative evaluation (terrible, hate). Positive or negative evaluation language is called sentiment, and word sentiment plays a role in important tasks like sentiment

> 情感
>
> *sentiment*

分析、立场检测，以及 NLP 在政治语言和消费者评论中的应用等任务中发挥着作用。

> analysis, stance detection, and applications of NLP to the language of politics and consumer reviews.

关于情感意义（affective meaning）的早期研究（Osgood 等，1957）发现，词之间存在差异

> Early work on affective meaning (Osgood et al., 1957) found that words varied

这种差异体现在情感意义的三个重要维度上：

> along three important dimensions of affective meaning:

效价（valence）：刺激的愉悦程度

> valence: the pleasantness of the stimulus

唤醒度（arousal）：刺激所引发情绪的强度

> arousal: the intensity of emotion provoked by the stimulus

支配度（dominance）：刺激所施加的控制程度

> dominance: the degree of control exerted by the stimulus

因此，像 happy 或 satisfied 这样的词效价高，而 unhappy 或 annoyed 效价低。Excited 唤醒度高，而 calm 唤醒度低。

> Thus words like happy or satisfied are high on valence, while unhappy or annoyed are low on valence. Excited is high on arousal, while calm is low on arousal.

Controlling 支配度高，而 awed 或 influenced 支配度低。

> Controlling is high on dominance, while awed or influenced are low on dominance.

因此，每个词都由三个数字表示，分别对应它在三个维度上的取值：

> Each word is thus represented by three numbers, corresponding to its value on each of the three dimensions:

效价 唤醒度 支配度

> Valence Arousal Dominance

|  | 效价<br>Valence | 唤醒度<br>Arousal | 支配度<br>Dominance |
| --- | --- | --- | --- |
| 勇敢的<br>courageous | 8.0 | 5.5 | 7.4 |
| 音乐<br>music | 7.7 | 5.6 | 6.5 |
| 心碎<br>heartbreak | 2.5 | 5.7 | 3.6 |
| 幼兽<br>cub | 6.7 | 4.0 | 4.2 |

勇敢的 8.0 5.5 7.4

> courageous 8.0 5.5 7.4

Osgood 等（1957）注意到，在用这 3 个数字表示一个词的

> Osgood et al. (1957) noticed that in using these 3 numbers to represent the

意义时，该模型把每个词表示为三维空间中的一个点，即一个向量，其三个维度分别对应该词在三个量表上的评分。词义可以被表示为空间中的一个点，这一革命性思想（例如，heartbreak 的部分意义可以表示为点 [2.5,5.7,3.6]）首次体现了我们接下来要介绍的向量语义模型。

> meaning of a word, the model was representing each word as a point in a threedimensional space, a vector whose three dimensions corresponded to the word’s rating on the three scales. This revolutionary idea that word meaning could be represented as a point in space (e.g., that part of the meaning of heartbreak can be represented as the point [2.5,5.7,3.6]) was the first expression of the vector semantics models that we introduce next.

5.2 • 向量语义：直观理解 131

> 5.2 • VECTOR SEMANTICS: THE INTUITION 131

## 5.2 向量语义：直观理解

> 5.2 Vector Semantics: The Intuition

> 向量
>
> *vector*

向量语义是 NLP 中表示词义的标准方式，它帮助我们

> Vector semantics is the standard way to represent word meaning in NLP, helping

> 语义
>
> *semantics*

对上一节中所看到的词义的许多方面进行建模。该模型的根源可追溯到 20 世纪 50 年代，当时两个重要构想汇合在一起：上文提到的 Osgood 1957 年的构想，即用一个三维空间中的点来表示词的内涵义；以及 Joos（1950）、Harris（1954）和 Firth（1957）等语言学家的主张，即通过词在语言使用中的分布来定义词义，也就是通过它的邻近词或语法环境来定义。他们的观点是：分布非常相似（邻近词相似）的两个词具有相似的意义。

> us model many of the aspects of word meaning we saw in the previous section. The roots of the model lie in the 1950s when two big ideas converged: Osgood’s 1957 idea mentioned above to use a point in three-dimensional space to represent the connotation of a word, and the proposal by linguists like Joos (1950), Harris (1954), and Firth (1957) to define the meaning of a word by its distribution in language use, meaning its neighboring words or grammatical environments. Their idea was that two words that occur in very similar distributions (whose neighboring words are similar) have similar meanings.

例如，假设你不知道 ongchoi 这个词的意思（它是近期从粤语借入的词），但你在以下语境中见到了它：

> For example, suppose you didn’t know the meaning of the word ongchoi (a recent borrowing from Cantonese) but you see it in the following contexts:

（5.1）Ongchoi 用大蒜爆炒很美味。

> (5.1) Ongchoi is delicious sauteed with garlic.

（5.2）Ongchoi 配米饭极佳。

> (5.2) Ongchoi is superb over rice.

（5.3）……ongchoi 叶配咸味酱汁……

> (5.3) ...ongchoi leaves with salty sauces...

再假设你曾在其它语境中见过其中许多上下文词：

> And suppose that you had seen many of these context words in other contexts:

（5.4）……菠菜用大蒜爆炒，配米饭……

> (5.4) ...spinach sauteed with garlic over rice...

![](images/img_114.png)

（5.5）……莙荙菜的茎和叶很美味……

> (5.5) ...chard stems and leaves are delicious...

（5.6）……羽衣甘蓝和其它带咸味的绿叶蔬菜

> (5.6) ...collard greens and other salty leafy greens

ongchoi 与米饭、大蒜、美味和

> The fact that ongchoi occurs with words like rice and garlic and delicious and

咸味这类词共现，菠菜、莙荙菜和羽衣甘蓝等词也是如此，这一事实可能提示 ongchoi 是一种与这些其它绿叶蔬菜相似的绿叶蔬菜。1 我们可以通过在 ongchoi 的上下文中统计词，用计算的方式实现同样的直觉。

> salty, as do words like spinach, chard, and collard greens might suggest that ongchoi is a leafy green similar to these other leafy greens.1 We can implement the same intuition computationally by just counting words in the context of ongchoi.

|  |  |
| --- | --- |
| 图 5.1<br>Figure 5.1 | 200 维 word2vec 嵌<br>A two-dimensional (t-SNE) visualization of 200-dimensional word2vec em- |

> 入，涉及若干与单词 sweet 相近的词，表明意义相似的词在空间中彼此邻近。该可视化使用 TensorBoard Embedding Projector https://projector.tensorflow.org/ 生成。
>
> *beddings for some words close to the word sweet, showing that words with similar meanings are nearby in space. Visualization created using the TensorBoard Embedding Projector https://projector.tensorflow.org/.*

向量语义的思想是把词表示为多维语义空间中的一个点，该空间由词的邻近词的分布导出（导出的方式各有不同，我们随后会看到）。用于表示词的向量称为嵌入。

> The idea of vector semantics is to represent a word as a point in a multidimensional semantic space that is derived (in different ways we’ll see) from the distributions of word neighbors. Vectors for representing words are called embeddings.

> 嵌入
>
> *embeddings*

> 1

> 它实际上是 Ipomoea aquatica（蕹菜），一种牵牛花的近亲，在英语中有时被称为 water spinach。
>
> *It’s in fact Ipomoea aquatica, a relative of morning glory sometimes called water spinach in English.*

132 第 5 章 • 嵌入

> 132 CHAPTER 5 • EMBEDDINGS

“嵌入”（embedding）一词在历史上源自其数学含义，即从一个空间或结构到另一个空间或结构的映射，尽管其含义已经发生变化；参见本章末尾。

> The word “embedding” derives historically from its mathematical sense as a mapping from one space or structure to another, although the meaning has shifted; see the end of the chapter.

图 5.1 展示了由 word2vec 算法学习得到的嵌入的可视化，

> Fig. 5.1 shows a visualization of embeddings learned by the word2vec algorithm,

其中显示了若干选定词（“sweet”的近邻）从 200 维空间投影到二维空间后的位置。注意 sweet 的最近邻是 honey、candy、juice、chocolate 等语义相关的词。相似词在高维空间中互为近邻这一思想，为语言模型和其他 NLP 应用提供了巨大的能力。例如，第 4 章的情感分类器依赖于相同的词同时出现在训练集和测试集中。但通过把词表示为嵌入，分类器只要见到一些含义相似的词就能判定情感。而且正如我们将看到的，像图 5.1 所示的这类向量语义模型可以无需监督地从文本中自动学习得到。

> showing the location of selected words (neighbors of “sweet”) projected down from 200-dimensional space into a 2-dimensional space. Note that the nearest neighbors of sweet are semantically related words like honey, candy, juice, chocolate. This idea that similar words are neighbors in high-dimensional space offers enormous power to language models and other NLP applications. For example the sentiment classifiers of Chapter 4 depend on the same words appearing in the training and test sets. But by representing words as embeddings, a classifier can assign sentiment as long as it sees some words with similar meanings. And as we’ll see, vector semantic models like the ones showed in Fig. 5.1 can be learned automatically from text without supervision.

本章我们将从一个简单的教学用嵌入模型开始，

> In this chapter we’ll begin with a simple pedagogical model of embeddings in

该模型用一个包含附近词计数的向量来定义词的含义。

> which the meaning of a word is defined by a vector with the counts of nearby words.

我们引入这个模型，是为了帮助理解向量的概念，以及向量作为词义表示意味着什么；但更精细的变体，比如我们将在第 11 章介绍的 tf-idf 模型，也是你应当掌握的重要方法。我们会看到，这种方法会产生非常长且稀疏的向量，即大部分元素为零（因为大多数词根本不会出现在其他词的上下文中）。随后我们将介绍 word2vec 模型族，用于构造更短、更稠密且具有更有用语义性质的向量。

> We introduce this model as a helpful way to understand the concept of vectors and what it means for a vector to be a representation of word meaning, but more sophisticated variants like the tf-idf model we will introduce in Chapter 11 are important methods you should understand. We will see that this method results in very long vectors that are sparse, i.e. mostly zeros (since most words simply never occur in the context of others). We’ll then introduce the word2vec model family for constructing short, dense vectors that have even more useful semantic properties.

我们还会介绍余弦（cosine），这是用嵌入来计算两个词、两个句子或两个文档之间语义相似度的标准方法，也是实际应用中的重要工具。

> We’ll also introduce the cosine, the standard way to use embeddings to compute semantic similarity, between two words, two sentences, or two documents, an important tool in practical applications.

## 5.3 简单的基于计数的嵌入

> 5.3 Simple count-based embeddings

“三维空间中向量最重要的属性是 {位置，位置，位置}”

> “The most important attributes of a vector in 3-space are {Location, Location, Location}”

> Randall Munroe，来自 https://xkcd.com/2358/ 的悬停文本
>
> *Randall Munroe, the hover from https://xkcd.com/2358/*

现在我们介绍计算词向量嵌入的第一种方法。这种最简单的词义向量模型基于共现矩阵（co-occurrence matrix），即一种表示词与词共现频率的方式。我们将定义一种特殊的共现

> Let’s now introduce the first way to compute word vector embeddings. This simplest vector model of meaning is based on the co-occurrence matrix, a way of representing how often words co-occur. We’ll define a particular kind of co-occurrence

> 词-上下文
>
> *word-context*

矩阵，即词-上下文矩阵（word-context matrix），其中矩阵的每一行代表词汇表中的一个词

> matrix, the word-context matrix, in which each row in the matrix represents a word

> 矩阵
>
> *matrix*

而每一列代表词汇表中其他每个词在其附近出现的频率。因此该矩阵的维度为 |V| × |V|，每个单元格记录行（目标）词与列（上下文）词在某个训练语料中于近旁共现的次数。

> in the vocabulary and each column represents how often each other word in the vocabulary appears nearby. This matrix is thus of dimensionality |V| × |V| and each cell records the number of times the row (target) word and the column (context) word co-occur nearby in some training corpus.

我们所说的“近旁”是什么意思？我们可以采用多种方法，但让我们

> What do we mean by ‘nearby’? We could implement various methods, but let’s

先从一种非常简单的方法开始：以该词为中心的上下文窗口，比如说左侧 4 个词、右侧 4 个词。如果这样做，每个单元格就表示（在某个训练语料中）列词出现在行词周围这样的 ±4 词窗口中的次数。

> start with a very simple one: a context window around the word, let’s say of 4 words to the left and 4 words to the right. If we do that, each cell will represent the number of times (in some training corpus) the column word occurs in such a±4-word window around the row word.

让我们看看这对 4 个词是如何运作的：cherry、strawberry、digital 和 information。对每个词，我们从语料中取出一个实例，并展示该实例的 ±4 词窗口：

> Let’s see how this works for 4 words: cherry, strawberry, digital, and information. For each word we took a single instance from a corpus, and we show the ±4 word window from that instance:

5.3 • 简单的基于计数的嵌入 133

> 5.3 • SIMPLE COUNT-BASED EMBEDDINGS 133

传统上后接 cherry pie（樱桃派），一种传统甜点

> is traditionally followed by cherry pie, a traditional dessert

常与其他水果混合，例如 strawberry rhubarb pie（草莓大黄派）。Apple pie

> often mixed, such as strawberry rhubarb pie. Apple pie

计算机外围设备和个人数字助理。这些设备通常

> computer peripherals and personal digital assistants. These devices usually

一台计算机。这包括互联网上可获得的信息

> a computer. This includes information available on the internet

如果我们随后取大语料中每个词的每一次出现，并统计

> If we then take every occurrence of each word in a large corpus and count the

它周围的上下文词，就得到一个词-上下文共现矩阵。完整的词-上下文共现矩阵非常庞大，因为对词汇表中的每个词（规模为 |V|），我们都必须统计它与词汇表中其他每个词共现的频率，因此维度为 |V|×|V|。所以我们改为在更小的尺度上勾勒这一过程。假设我们只看这 4 个词，并且只考虑以下 3 个上下文词：a、computer 和 pie。此外再假设我们只统计上面这个小语料中的出现次数。

> context words around it, we get a word-context co-occurrence matrix. The full wordcontext co-occurrence matrix is very large, because for each word in the vocabulary(of size |V|) we have to count how often it occurs with every other word in the vocabulary, hence dimensionality |V|×|V|. Let’s therefore instead sketch the process on a smaller scale. Imagine that we are going to look at only the 4 words, and only consider the following 3 context words: a, computer, and pie. Furthermore let’s assume we only count occurrences in the mini-corpus above.

所以在看图 5.2 之前，请手工计算这 3 个上下文

> So before looking at Fig. 5.2, compute by hand the counts for these 3 context

词对于 cherry、strawberry、digital 和 information 这 4 个词的计数。

> words for the four words cherry, strawberry, digital, and information.

> a computer pie

| a computer pie |  |
| --- | --- |
| cherry 1 0 1<br>strawberry 0 0 2<br>digital 0 1 0<br>information 1 1 0 |  |
| 图 5.2<br>Figure 5.2 | 四个词的共现向量，计数来自上面 4 个窗口，<br>Co-occurrence vectors for four words with counts from the 4 windows above, |

> cherry 1 0 1 strawberry 0 0 2 digital 0 1 0 information 1 1 0

> 仅显示潜在的上下文词维度中的 3 个。cherry 的向量用红色标出。注意真实的向量维度要多得多，因而更加稀疏。
>
> *showing just 3 of the potential context word dimensions. The vector for cherry is outlined in red. Note that a real vector would have vastly more dimensions and thus be even sparser.*

希望你的计数与图 5.2 所示一致，即每个单元格表示某个特定词（由行定义）出现在某个特定上下文（由词列定义）中的次数。

> Hopefully your count matches what is shown in Fig. 5.2, so that each cell represents the number of times a particular word (defined by the row) occurs in a particular context (defined by the word column).

这样，每一行就是代表一个词的向量。回顾一些基本的线性

> Each row, then, is a vector representing a word. To review some basic linear

代数知识：向量本质上就是一个数字列表或数组。因此 cherry 被表示为

> algebra, a vector is, at heart, just a list or array of numbers. So cherry is represented

> 向量
>
> *vector*

列表 [1,0,1]（图 5.2 中的第一行向量），而 information 被表示为列表 [1,1,0]（第四行向量）。

> as the list [1,0,1] (the first row vector in Fig. 5.2) and information is represented as the list [1,1,0] (the fourth row vector).

向量空间是一组向量的集合，其特征由维数决定。

> A vector space is a collection of vectors, and is characterized by its dimension.

> 向量空间
>
> *vector space*

三维向量空间中的向量对于该空间的每一个维度都有一个元素，

> Vectors in a 3-dimensional vector space have an element for each dimension of the

> 维度
>
> *dimension*

空间。我们粗略地把 3 维空间中的向量称为 3 维向量，每个维度上各有一个元素。在图 5.2 的例子中，我们选择把词向量设为 3 维，只是为了能放进页面；在真实的词–词矩阵中，向量的维度会是 |V|，即词汇表大小。

> space. We will loosely refer to a vector in a 3-dimensional space as a 3-dimensional vector, with one element along each dimension. In the example in Fig. 5.2, we’ve chosen to make the word vectors of dimension 3, just so they fit on the page; in real word-word matrices, the vectors would have dimensionality |V|, the vocabulary size.

向量空间中数字的排列顺序指示了各不相同的维度

> The ordering of the numbers in a vector space indicates the different dimensions

词语正是在这些维度上发生变化。所有这些向量的第三个维度对应于 pie 在上下文中出现的次数。它们全部的第二维度对应于单词 computer 出现的次数。注意，information 和 digital 的向量在这个“computer”维度上具有相同的值（1）。

> on which words vary. The third dimension for all these vectors corresponds to the number of times pie occurs in the context. The second dimension for all of them corresponds to the number of times the word computer occurs. Notice that the vectors for information and digital have the same value (1) for this “computer” dimension.

在现实中，我们并不是在单个上下文窗口上计算词向量，而是

> In reality, we don’t compute word vectors on a single context window. Instead,

在整个语料库上计算它们。让我们看看一些真实计数是什么样子。

> we compute them over an entire corpus. Let’s see what some real counts look like.

让我们看看按这种方式计算得到的一些向量。图 5.3 展示了这四个词的词–词共现矩阵的一个子集；同样，由于无法在本教科书的页面上可视化全部 |V| 个可能的上下文词，我们只展示其中 6 个维度的子集，计数由 Wikipedia 语料库计算得到（Davies, 2015）。

> Let’s look at some vectors computed in this way. Fig. 5.3 shows a subset of the word-word co-occurrence matrix for these four words, where, again because it’s impossible to visualize all |V| possible context words on the page of this textbook, we show a subset of 6 of the dimensions, with counts computed from the Wikipedia corpus (Davies, 2015).

注意在图 5.3 中，cherry 和 strawberry 这两个词彼此之间更为相似，而不是 134 第 5 章 • 嵌入

> Note in Fig. 5.3 that the two words cherry and strawberry are more similar to 134 CHAPTER 5 • EMBEDDINGS

> aardvark ... computer data result pie sugar ...

> cherry 0 ... 2 8 9 442 25 ... strawberry 0 ... 0 0 1 60 19 ... digital 0 ... 1670 1683 85 5 4 ... information 0 ... 3325 3982 378 5 13 ...

> 图 5.3 Wikipedia 语料库中四个词的共现向量，展示了其中六个维度（为教学目的手工挑选）。digital 的向量用红色勾勒。注意，真实的向量会有多得多的维度，因而稀疏得多，即在大多数维度上取值为零。
>
> *Figure 5.3 Co-occurrence vectors for four words in the Wikipedia corpus, showing six of the dimensions (hand-picked for pedagogical purposes). The vector for digital is outlined in red. Note that a real vector would have vastly more dimensions and thus be much sparser, i.e. would have zero values in most dimensions.*

彼此之间更相似（pie 和 sugar 都倾向于出现在它们的窗口中），而不是与像 digital 这样的其他词更相似；反过来，digital 和 information 彼此之间也比它们与 strawberry 之类更相似。

> each other (both pie and sugar tend to occur in their window) than they are to other words like digital; conversely, digital and information are more similar to each other than, say, to strawberry.

我们可以把某个词的向量看作 |V| 维空间中的一个点；因此

> We can think of the vector for a word as a point in |V|-dimensional space; thus

图 5.3 中的词是 6 维空间中的点。图 5.4 展示了 2 维的空间可视化。

> the words in Fig. 5.3 are points in 6-dimensional space. Fig. 5.4 shows a spatial visualization in 2 dimensions.

|  | 4000<br>information computer<br>3000 [3982,3325]<br>digital<br>2000 [1683,1670]<br>1000<br>1000 2000 3000 4000<br>data |
| --- | --- |
| 图 5.4<br>Figure 5.4 |  |

> 4000

> information

computer

> 3000 [3982,3325]

> digital

> 2000 [1683,1670]

> 1000

> 1000 2000 3000 4000

data

> 图 5.4 digital 和 information 的词向量空间可视化，只展示了其中两个维度，分别对应于单词 data 和 computer。
>
> *Figure 5.4 A spatial visualization of word vectors for digital and information, showing just two of the dimensions, corresponding to the words data and computer.*

注意，|V|（即向量的维度）通常是词汇表的大小，往往在 10,000 到 50,000 个词之间（使用训练语料库中最频繁出现的词；保留大约最频繁的 50,000 个之后的词通常没有帮助）。由于这些数字大多是零，因此它们是稀疏向量表示；存在高效的算法来存储稀疏矩阵并用其进行计算。

> Note that |V|, the dimensionality of the vector, is generally the size of the vocabulary, often between 10,000 and 50,000 words (using the most frequent words in the training corpus; keeping words after about the most frequent 50,000 or so is generally not helpful). Since most of these numbers are zero these are sparse vector representations; there are efficient algorithms for storing and computing with sparse matrices.

也可以对这些计数应用各种类型的加权函数

> It’s also possible to apply various kinds of weighting functions to the counts

施加在这些单元格上。最流行的此类加权是 tf-idf，我们将在第 11 章介绍它，但历史上曾出现过各种各样的其他加权方式。

> in these cells. The most popular such weighting is tf-idf, which we’ll introduce in Chapter 11, but there have historically been a wide variety of other weightings.

既然我们已经有了一些直观认识，接下来就详细考察词相似度的计算。

> Now that we have some intuitions, let’s move on to examine the details of computing word similarity.

## 5.4 用余弦度量相似度

> 5.4 Cosine for Measuring Similarity

要度量两个目标词 v 和 w 之间的相似度，我们需要一个度量：它接收两个向量（维度相同，要么都以词为维度，因而长度为 |V|，要么都以文档为维度，长度为 |D|），并给出它们相似程度的一个度量。迄今为止最常见的相似度度量是向量之间夹角的余弦。

> To measure similarity between two target words v and w, we need a metric that takes two vectors (of the same dimensionality, either both with words as dimensions, hence of length |V|, or both with documents as dimensions, of length |D|) and gives a measure of their similarity. By far the most common similarity metric is the cosine of the angle between the vectors.

5.4 • 用余弦度量相似度 135

> 5.4 • COSINE FOR MEASURING SIMILARITY 135

余弦——如同 NLP 中使用的大多数向量相似度度量一样——基于

> The cosine—like most measures for vector similarity used in NLP—is based on

线性代数中的点积算子，也称为内积：

> the dot product operator from linear algebra, also called the inner product:

> 点积
>
> *dot product*

> 内积
>
> *inner product*

> N

X

dot product(v,w) = v ·w = viwi = v1w1 +v2w2 +...+vNwN

> (5.7)

> i=1

点积之所以能充当相似度度量，是因为当两个向量在相同维度上取值都很大时，点积往往也很大。反之，若两个向量在不同维度上取零——即正交向量——其点积为 0，表示它们高度不相似。

> The dot product acts as a similarity metric because it will tend to be high just when the two vectors have large values in the same dimensions. Alternatively, vectors that have zeros in different dimensions—orthogonal vectors—will have a dot product of 0, representing their strong dissimilarity.

然而，这种原始点积作为相似度度量存在一个问题：它偏爱

> This raw dot product, however, has a problem as a similarity metric: it favors

长向量。向量长度的定义为

> long vectors. The vector length is defined as

> 向量长度
>
> *vector length*

v u

> N

u t X

v2

> (5.8)

|v| =

> i

> i=1

向量越长，各维度上的取值越大，点积就越高。

> The dot product is higher if a vector is longer, with higher values in each dimension.

更频繁出现的词具有更长的向量，因为它们倾向于与更多词共现，且与其中每个词的共现值都更高。因此，原始点积对高频词而言会更大。但这是一个问题；我们希望相似度度量能告诉我们两个词有多相似，而不受其词频影响。

> More frequent words have longer vectors, since they tend to co-occur with more words and have higher co-occurrence values with each of them. The raw dot product thus will be higher for frequent words. But this is a problem; we’d like a similarity metric that tells us how similar two words are regardless of their frequency.

我们修改点积，通过将

> We modify the dot product to normalize for the vector length by dividing the

点积除以两个向量各自的长度，从而对向量长度做归一化。根据向量 a 与 b 之间点积的定义可知，这个归一化后的点积恰好等于两个向量夹角的余弦：

> dot product by the lengths of each of the two vectors. This normalized dot product turns out to be the same as the cosine of the angle between the two vectors, following from the definition of the dot product between two vectors a and b:

a·b = |a||b|cosθ|a||b| = cosθ a·b

> (5.9)

于是，两个向量 v 与 w 之间的余弦相似度度量可以计算为：

> The cosine similarity metric between two vectors v and w thus can be computed as:

> 余弦
>
> *cosine*

> N

X

viwi

cosine(v,w) = v ·w

> i=1

> (5.10)

|v||w| = v u v u

> N N

u t X u t X

v2 w2

> i i

> i=1 i=1

对于某些应用，我们会预先对每个向量做归一化，即将其除以自身长度，得到一个长度为 1 的单位向量。于是我们可以由 a 通过

> For some applications we pre-normalize each vector, by dividing it by its length, creating a unit vector of length 1. Thus we could compute a unit vector from a by

> 单位向量
>
> *unit vector*

将其除以 |a| 来计算单位向量。对于单位向量，点积与余弦相同。

> dividing it by |a|. For unit vectors, the dot product is the same as the cosine.

余弦值的范围从 1（向量指向同一方向），经过

> The cosine value ranges from 1 for vectors pointing in the same direction, through

0（正交向量），到 -1（向量指向相反方向）。但由于原始频数取值非负，这些向量的余弦范围为 0–1。

> 0 for orthogonal vectors, to -1 for vectors pointing in opposite directions. But since raw frequency values are non-negative, the cosine for these vectors ranges from 0–1.

下面我们看看，余弦如何计算出 cherry 与 digital 这两个词中哪一个

> Let’s see how the cosine computes which of the words cherry or digital is closer

在含义上更接近 information，仅使用下面这张简化表中的原始计数：

> in meaning to information, just using raw counts from the following shortened table:

> pie data computer

> cherry 442 8 2 digital 5 1683 1670 information 5 3982 3325

136 第 5 章 • 嵌入

> 136 CHAPTER 5 • EMBEDDINGS

442∗5+8∗3982+2∗3325

cos(cherry,information) = √ 4422 +82 +22√ 52 +39822 +33252 = .018

5∗5+1683∗3982+1670∗3325

cos(digital,information) = √ 52 +16832 +16702√ 52 +39822 +33252 = .996

模型判定 information 与 digital 的距离远比它与 cherry 的距离更近，这

> The model decides that information is way closer to digital than it is to cherry, a

一结果看来是合理的。图 5.5 给出了可视化。

> result that seems sensible. Fig. 5.5 shows a visualization.

> 维度 1：“pie”
>
> *Dimension 1: ‘pie’*

> 500 cherry

> digital information

> 500 1000 1500 2000 2500 3000

> 维度 2：“computer”
>
> *Dimension 2: ‘computer’*

> 图 5.5 余弦相似度的一个（粗略）图形演示，展示了三个词（cherry、digital 和 information）在以邻近词 computer 与 pie 的计数所定义的二维空间中的向量。图中并未显示余弦值，而是突出了夹角；注意 digital 与 information 之间的夹角小于 cherry 与 information 之间的夹角。两个向量越相似，余弦值越大而夹角越小；当两个向量之间的夹角最小（0◦）时，余弦值达到最大（1）；其他所有角度的余弦值都小于 1。
>
> *Figure 5.5 A (rough) graphical demonstration of cosine similarity, showing vectors for three words (cherry, digital, and information) in the two dimensional space defined by counts of the words computer and pie nearby. The figure doesn’t show the cosine, but it highlights the angles; note that the angle between digital and information is smaller than the angle between cherry and information. When two vectors are more similar, the cosine is larger but the angle is smaller; the cosine has its maximum (1) when the angle between two vectors is smallest(0◦); the cosine of all other angles is less than 1.*

余弦相似度可用于估计词相似度，以完成诸如查找

> Cosine similarity can be used to estimate word similarity, for tasks like finding

词的释义、追踪词义变化，或在不同语料库中自动发现词语含义之类的任务。例如，我们可以计算 w 与其余 |V|−1 个词各自之间的余弦值，排序后取前 10 名，从而找出与任意目标词 w 最相似的 10 个词。

> word paraphrases, tracking changes in word meaning, or automatically discovering meanings of words in different corpora. For example, we can find the 10 most similar words to any target word w by computing the cosines between w and each of the |V|−1 other words, sorting, and looking at the top 10.

## 5.5 Word2vec

在前几节中，我们看到了如何把一个词表示为稀疏的长向量，其维度对应于词表中的词。现在我们引入一种更强大的词表示：嵌入（embedding），即短而稠密的向量。与目前所见过的向量不同，嵌入很短，其维度数 d 在 50 到 1000 之间，而不是大得多的词表大小 |V|。这 d 个维度并没有明确的解释。而且这些向量是稠密的：向量元素不再是稀疏的、大多为零的计数或计数的函数，取而代之的可以是取负值的实数值。

> In the previous sections we saw how to represent a word as a sparse, long vector with dimensions corresponding to words in the vocabulary. We now introduce a more powerful word representation: embeddings, short dense vectors. Unlike the vectors we’ve seen so far, embeddings are short, with number of dimensions d ranging from 50-1000, rather than the much larger vocabulary size |V|. These d dimensions don’t have a clear interpretation. And the vectors are dense: instead of vector entries being sparse, mostly-zero counts or functions of counts, the values will be realvalued numbers that can be negative.

事实证明，在每一项 NLP 任务中，稠密向量都比稀疏向量表现更好。

> It turns out that dense vectors work better in every NLP task than sparse vectors.

尽管我们并不完全理解其中的所有原因，但对此有一些直觉。把词表示为 300 维稠密向量时，分类器需要学习的权重数量远少于把词表示为 50,000 维向量时的情形，而更小的参数空间可能有助于泛化和避免过拟合。稠密向量在捕捉同义关系方面也可能做得更好。例如，在稀疏向量表示中，car 和 5.5 • WORD2VEC 137 automobile 这类同义词的维度各不相同且互不相关；因此稀疏向量可能无法捕捉到以 car 为邻近词的词与以 automobile 为邻近词的词之间的相似性。

> While we don’t completely understand all the reasons for this, we have some intuitions. Representing words as 300-dimensional dense vectors requires our classifiers to learn far fewer weights than if we represented words as 50,000-dimensional vectors, and the smaller parameter space possibly helps with generalization and avoiding overfitting. Dense vectors may also do a better job of capturing synonymy. For example, in a sparse vector representation, dimensions for synonyms like car and 5.5 • WORD2VEC 137 automobile are distinct and unrelated; sparse vectors may thus fail to capture the similarity between a word with car as a neighbor and a word with automobile as a neighbor.

本节介绍一种计算嵌入的方法：skip-gram

> In this section we introduce one method for computing embeddings: skip-gram

> skip-gram

带负采样，有时称为 SGNS。skip-gram 算法是

> with negative sampling, sometimes called SGNS. The skip-gram algorithm is one

> SGNS

名为 word2vec 的软件包中两种算法之一，因此有时该

> of two algorithms in a software package called word2vec, and so sometimes the

> word2vec

算法被宽泛地称作 word2vec（Mikolov et al. 2013a，Mikolov et al. 2013b）。word2vec 方法速度快、训练效率高，并且可以在网上方便地获取代码和预训练嵌入。Word2vec 嵌入是静态嵌入，即该方法为

> algorithm is loosely referred to as word2vec (Mikolov et al. 2013a, Mikolov et al. 2013b). The word2vec methods are fast, efficient to train, and easily available online with code and pretrained embeddings. Word2vec embeddings are static embeddings, meaning that the method learns one fixed embedding for each word in the

> 静态
>
> *static*

> 嵌入
>
> *embeddings*

词表中的每个词学习一个固定的嵌入。第 9 章将介绍学习动态上下文嵌入的方法，例如广受欢迎的 BERT 表示系列，其中每个词的向量在不同上下文中各不相同。

> vocabulary. In Chapter 9 we’ll introduce methods for learning dynamic contextual embeddings like the popular family of BERT representations, in which the vector for each word is different in different contexts.

word2vec 的基本思路是：我们不去统计每个上下文

> The intuition of word2vec is that instead of counting how often each context

词 c 在比如 apricot 附近的出现频率，而是改为在一个二分类预测任务上训练分类器：“词 c 是否可能出现在 apricot 附近？”我们其实并不关心这个预测任务本身，而是把学到的分类器权重作为词嵌入。

> word c occurs near, say, apricot, we’ll instead train a classifier on a binary prediction task: “Is word c likely to show up near apricot?” We don’t actually care about this prediction task; instead we’ll take the learned classifier weights as the word embeddings.

这里具有革命性的洞见在于，我们可以直接把连续文本用作隐含的

> The revolutionary intuition here is that we can just use running text as implicitly

监督训练数据来训练这样的分类器；出现在目标词 apricot 附近的词 c 就充当问题“词 c 是否可能出现在 apricot 附近？”的黄金“正确答案”。这种方法通常称为自监督，它避免了

> supervised training data for such a classifier; a word c that occurs near the target word apricot acts as gold ‘correct answer’ to the question “Is word c likely to show up near apricot?” This method, often called self-supervision, avoids the need for

> 自监督
>
> *self-supervision*

任何形式的人工标注监督信号。这一思想最初是在神经语言建模任务中提出的，当时 Bengio 等人（2003）和 Collobert 等人（2011）表明，神经语言模型（一种从前面若干个词学习预测下一个词的神经网络）可以直接把连续文本中的下一个词作为其监督信号，并且可以在完成这一预测任务的过程中为每个词学习一种嵌入表示。

> any sort of hand-labeled supervision signal. This idea was first proposed in the task of neural language modeling, when Bengio et al. (2003) and Collobert et al. (2011) showed that a neural language model (a neural network that learned to predict the next word from prior words) could just use the next word in running text as its supervision signal, and could be used to learn an embedding representation for each word as part of doing this prediction task.

我们将在下一章看到如何实现神经网络，但 word2vec 是一个

> We’ll see how to do neural networks in the next chapter, but word2vec is a

比神经网络语言模型简单得多的模型，体现在两个方面。第一，word2vec 简化了任务（把它变成二分类而不是词预测）。第二，word2vec 简化了架构（训练一个逻辑回归分类器，而不是带隐藏层、需要更复杂训练算法的多层神经网络）。skip-gram 的思路是：

> much simpler model than the neural network language model, in two ways. First, word2vec simplifies the task (making it binary classification instead of word prediction). Second, word2vec simplifies the architecture (training a logistic regression classifier instead of a multi-layer neural network with hidden layers that demand more sophisticated training algorithms). The intuition of skip-gram is:

- 把目标词及其邻近的上下文词当作正例。
- 从词库中随机抽取其他词作为负例样本。
- 用逻辑回归训练一个分类器来区分这两种情况。
- 把学到的权重用作嵌入。

> Treat the target word and a neighboring context word as positive examples.
> Randomly sample other words in the lexicon to get negative samples.
> Use logistic regression to train a classifier to distinguish those two cases.
> Use the learned weights as the embeddings.

### 5.5.1 分类器

> 5.5.1 The classifier

我们先从分类任务谈起，然后再讨论如何训练。

> Let’s start by thinking about the classification task, and then turn to how to train.

设想下面这样一个句子，目标词为 apricot，并假设我们使用 ±2 个上下文词的窗口：

> Imagine a sentence like the following, with a target word apricot, and assume we’re using a window of ±2 context words:

> ……柠檬、一[汤匙杏子酱、一]撮……
>
> *... lemon, a [tablespoon of apricot jam, a] pinch ...*

> c1 c2 w c3 c4

我们的目标是训练一个分类器，使其在给定由目标词

> Our goal is to train a classifier such that, given a tuple (w,c) of a target word

w 与候选上下文词 c 组成的元组（例如 (apricot, jam)，或者也可能是 138 第 5 章 • 嵌入 (apricot, aardvark)）时，返回 c 是真实上下文词的概率（对 jam 为真，对 aardvark 为假）：

> w paired with a candidate context word c (for example (apricot, jam), or perhaps 138 CHAPTER 5 • EMBEDDINGS (apricot, aardvark)) it will return the probability that c is a real context word (true for jam, false for aardvark):

P(+|w,c) (5.11)

词 c 不是 w 的真实上下文词的概率，就是 1 减去

> The probability that word c is not a real context word for w is just 1 minus

式 5.11：

> Eq. 5.11:

P(−|w,c) = 1−P(+|w,c) (5.12)

分类器如何计算概率 P？skip-gram 模型的直觉是让这一概率建立在嵌入相似度之上：如果某个词的嵌入向量与目标词的嵌入向量相似，它就更有可能出现在目标词附近。为了计算这些稠密嵌入之间的相似度，我们依据这样一个直觉：两个向量的点积大，就说明它们相似（毕竟余弦只是归一化的点积）。换句话说：

> How does the classifier compute the probability P? The intuition of the skipgram model is to base this probability on embedding similarity: a word is likely to occur near the target if its embedding vector is similar to the target embedding. To compute similarity between these dense embeddings, we rely on the intuition that two vectors are similar if they have a high dot product (after all, cosine is just a normalized dot product). In other words:

Similarity(w,c) ≈c·w

> (5.13)

点积 c · w 不是概率，它只是一个取值范围从 −∞ 到 ∞ 的数（由于 word2vec 嵌入中的元素可以为负，点积也可以为负）。要把点积转化为概率，我们使用 logistic 函数或称 sigmoid 函数 σ(x)，它是逻辑回归最根本的核心：

> The dot product c · w is not a probability, it’s just a number ranging from −∞to ∞(since the elements in word2vec embeddings can be negative, the dot product can be negative). To turn the dot product into a probability, we’ll use the logistic or sigmoid function σ(x), the fundamental core of logistic regression:

1

σ(x) =

> (5.14)

1+exp(−x)

我们把词 c 是目标词 w 的真实上下文词的概率建模为：

> We model the probability that word c is a real context word for target word w as:

1

P(+|w,c) = σ(c·w) =

> (5.15)

1+exp(−c·w)

sigmoid 函数返回一个 0 到 1 之间的数，但要让它成为一个概率，我们还需要两个可能事件（c 是上下文词，以及 c 不是上下文词）的概率之和为 1。因此，我们把词 c 不是 w 的真实上下文词的概率估计为：

> The sigmoid function returns a number between 0 and 1, but to make it a probability we’ll also need the total probability of the two possible events (c is a context word, and c isn’t a context word) to sum to 1. We thus estimate the probability that word c is not a real context word for w as:

P(−|w,c) = 1−P(+|w,c)

1

> (5.16)

= σ(−c·w) = 1+exp(c·w)

式 5.15 给出了一个词的概率，但窗口中还有很多上下文词。Skip-gram 做出了一个简化假设：所有上下文词都是相互独立的，这使我们能够直接把它们的概率相乘：

> Equation 5.15 gives us the probability for one word, but there are many context words in the window. Skip-gram makes the simplifying assumption that all context words are independent, allowing us to just multiply their probabilities:

> L

Y

P(+|w,c1:L) =

> (5.17)

σ(ci ·w)

> i=1

> L

X

logP(+|w,c1:L) = logσ(ci ·w)

> (5.18)

> i=1

总之，skip-gram 训练一个概率分类器：给定测试目标词 w 及其包含 L 个词的上下文窗口 c1:L，该分类器根据这个上下文窗口与目标词的相似程度赋予一个概率。该概率基于将 5.5 • WORD2VEC 139

> In summary, skip-gram trains a probabilistic classifier that, given a test target word w and its context window of L words c1:L, assigns a probability based on how similar this context window is to the target word. The probability is based on applying the 5.5 • WORD2VEC 139

| 1..d<br>aardvark 1<br>apricot<br>W 目标词<br>… …<br>𝜽 = zebra \|V\|<br>aardvark \|V\|+1<br>apricot<br>C 上下文与噪声<br>… … 词<br>zebra 2\|V\|<br>1..d<br>aardvark 1<br>apricot<br>W target words<br>… …<br>𝜽 = zebra \|V\|<br>aardvark \|V\|+1<br>apricot<br>C context & noise<br>… … words<br>zebra 2\|V\| |  |
| --- | --- |
| 图 5.6<br>Figure 5.6 | 由 skip-gram 模型学习得到的嵌入。该算法存储两个嵌—<br>The embeddings learned by the skipgram model. The algorithm stores two em- |

> 1..d

> aardvark 1

> apricot

### 𝜽 =

W 目标词

> W target words

> … …

> zebra |V|

> aardvark |V|+1

> apricot

C 上下文与噪声

> C context & noise

> … …

词

> words

> zebra 2|V|

> 每个词的两个嵌入：目标嵌入（有时称为输入嵌入）和上下文嵌入（有时称为输出嵌入）。因此，算法学习到的参数 θ 是一个由 2|V| 个向量构成的矩阵，每个向量的维度为 d，由两个矩阵拼接而成，即目标嵌入 W 和上下文+噪声嵌入 C。
>
> *beddings for each word, the target embedding (sometimes called the input embedding) and the context embedding (sometimes called the output embedding). The parameter θ that the algorithm learns is thus a matrix of 2|V| vectors, each of dimension d, formed by concatenating two matrices, the target embeddings W and the context+noise embeddings C.*

logistic（sigmoid）函数应用于目标词嵌入与每个上下文词嵌入的点积。要计算该概率，我们只需要词汇表中每个目标词和上下文词的嵌入。

> logistic (sigmoid) function to the dot product of the embeddings of the target word with each context word. To compute this probability, we just need embeddings for each target word and context word in the vocabulary.

图 5.6 展示了我们所需参数的直观含义。skip-gram 实际上

> Fig. 5.6 shows the intuition of the parameters we’ll need. Skip-gram actually

为每个词存储两个嵌入：一个用于该词作为目标词的情形，另一个用于该词被视作上下文的情形。因此，我们需要学习的参数是两个矩阵 W 和 C，每个矩阵都包含词汇表 V 中 |V| 个词各自的嵌入。2 现在让我们转向学习这些嵌入（这本来就是训练该分类器的真正目标）。

> stores two embeddings for each word, one for the word as a target, and one for the word considered as context. Thus the parameters we need to learn are two matrices W and C, each containing an embedding for every one of the |V| words in the vocabulary V.2 Let’s now turn to learning these embeddings (which is the real goal of training this classifier in the first place).

### 5.5.2 学习 skip-gram 嵌入

> 5.5.2 Learning skip-gram embeddings

skip-gram 嵌入的学习算法以文本语料库和选定的词汇表规模 N 作为输入。它首先为 N 个词汇表中的每个词随机分配一个嵌入向量，然后迭代地调整每个词 w 的嵌入，使其更接近文本中出现在附近的词的嵌入，而不那么接近未出现在附近的词的嵌入。让我们先来看一条训练数据：

> The learning algorithm for skip-gram embeddings takes as input a corpus of text, and a chosen vocabulary size N. It begins by assigning a random embedding vector for each of the N vocabulary words, and then proceeds to iteratively shift the embedding of each word w to be more like the embeddings of words that occur nearby in texts, and less like the embeddings of words that don’t occur nearby. Let’s start by considering a single piece of training data:

> ... lemon, a [tablespoon of apricot jam, a] pinch ...

> c1 c2 w c3 c4

该示例有一个目标词 w（apricot），以及 L = ±2

> This example has a target word w (apricot), and 4 context words in the L = ±2

窗口中的 4 个上下文词，由此得到 4 个正训练实例（见下左）：

> window, resulting in 4 positive training instances (on the left below):

正例 + 负例 w cpos w cneg w cneg apricot tablespoon apricot aardvark apricot seven apricot of apricot my apricot forever apricot jam apricot where apricot dear apricot a apricot coaxial apricot if

> positive examples + negative examples w cpos w cneg w cneg apricot tablespoon apricot aardvark apricot seven apricot of apricot my apricot forever apricot jam apricot where apricot dear apricot a apricot coaxial apricot if

> 2

> 原则上，目标矩阵和上下文矩阵可以使用不同的词汇表，但我们简化处理，假设共用一个词汇表 V。
>
> *In principle the target matrix and the context matrix could use different vocabularies, but we’ll simplify by assuming one shared vocabulary V.*

140 第 5 章 • 嵌入

> 140 CHAPTER 5 • EMBEDDINGS

训练二分类器还需要负例。事实上，带负采样的 skip-gram（skipgram with negative sampling，SGNS）使用的负例多于正例（两者之间的比例由参数 k 设定）。因此，对于每个 (w,cpos) 训练实例，我们会创建 k 个负样本，每个负样本由目标 w 加上一个“噪声词”cneg 组成。噪声词是从词表中随机抽取的词，并被约束为不能是目标词 w。正上方的表格展示了 k = 2 的设置，因此对于每个正例 w,cpos，我们在负训练集中会有 2 个负例。

> For training a binary classifier we also need negative examples. In fact skipgram with negative sampling (SGNS) uses more negative examples than positive examples (with the ratio between them set by a parameter k). So for each of these(w,cpos) training instances we’ll create k negative samples, each consisting of the target w plus a ‘noise word’ cneg. A noise word is a random word from the lexicon, constrained not to be the target word w. The table right above shows the setting where k = 2, so we’ll have 2 negative examples in the negative training set −for each positive example w,cpos.

噪声词根据其加权一元概率来选取

> The noise words are chosen according to their weighted unigram probability

pα(w)，其中 α 是权重。如果我们按照未加权的概率 P(w) 采样，那就意味着会以一元概率 P(“the”) 选取词 the 作为噪声词，以一元概率 P(“aardvark”) 选取 aardvark，依此类推。但在实践中通常设定 α = 0.75，即使用加权 P3 4 (w)：

> pα(w), where α is a weight. If we were sampling according to unweighted probability P(w), it would mean that with unigram probability P(“the”) we would choose the word the as a noise word, with unigram probability P(“aardvark”) we would choose aardvark, and so on. But in practice it is common to set α = 0.75, i.e. use the weighting P3 4 (w):

count(w)α

Pα(w) = P

> (5.19)

w′ count(w′)α

设定 α = .75 能获得更好的性能，因为它给稀有的噪声词略高的概率：对于稀有词，Pα(w) > P(w)。为说明这一直观理解，不妨计算一个例子中的概率，其中 α = .75 且有两个事件，P(a) = 0.99，P(b) = 0.01：

> Setting α = .75 gives better performance because it gives rare noise words slightly higher probability: for rare words, Pα(w) > P(w). To illustrate this intuition, it might help to work out the probabilities for an example with α = .75 and two events, P(a) = 0.99 and P(b) = 0.01:

.99.75

Pα(a) = .99.75 +.01.75 = 0.97

.01.75

Pα(b) = .99.75 +.01.75 = 0.03

> (5.20)

因此，使用 α = .75 会把稀有事件 b 的概率从 0.01 提高到 0.03。

> Thus using α = .75 increases the probability of the rare event b from 0.01 to 0.03.

给定正、负训练实例的集合，以及一组初始的

> Given the set of positive and negative training instances, and an initial set of

嵌入向量，学习算法的目标是调整这些嵌入向量，以

> embeddings, the goal of the learning algorithm is to adjust those embeddings to

- 最大化取自正例的目标词、上下文词对 (w,cpos) 的相似度
- 最小化取自负例的 (w,cneg) 词对的相似度。

> Maximize the similarity of the target word, context word pairs (w,cpos) drawn from the positive examples
> Minimize the similarity of the (w,cneg) pairs from the negative examples.

若考虑一个词/上下文词对 (w,cpos) 及其 k 个噪声词 cneg1...cnegk，

> If we consider one word/context pair (w,cpos) with its k noise words cneg1...cnegk,

我们可以把这两个目标表示为如下待最小化的损失函数 L（故带有 − 号）；其中第一项表示我们希望分类器给真实上下文词 cpos 赋予较高的成为邻居的概率，第二项表示我们希望给每个噪声词 cnegi 赋予较高的不成为邻居的概率，二者相乘是因为我们假定它们相互独立：

> we can express these two goals as the following loss function L to be minimized(hence the −); here the first term expresses that we want the classifier to assign the real context word cpos a high probability of being a neighbor, and the second term expresses that we want to assign each of the noise words cnegi a high probability of being a non-neighbor, all multiplied because we assume independence:

" kY #

L(w,cpos,cneg*) = −log P(+|w,cpos) P(−|w,cnegi)

> i=1

" #

> k

X

= − logP(+|w,cpos)+ logP(−|w,cnegi)

> i=1

" #

> k

X   

= − logP(+|w,cpos)+ log 1−P(+|w,cnegi)

> i=1

" #

> k

X

logσ(cpos ·w)+ logσ(−cnegi ·w)

> (5.21)

= −

> i=1

5.5 • WORD2VEC 141

也就是说，我们希望最大化该词与真实上下文词的点积，并最小化该词与 k 个负采样的非邻居词的点积。

> That is, we want to maximize the dot product of the word with the actual context words, and minimize the dot products of the word with the k negative sampled nonneighbor words.

我们使用随机梯度下降来最小化该损失函数。图 5.7 展示了

> We minimize this loss function using stochastic gradient descent. Fig. 5.7 shows

一步学习的直观含义。

> the intuition of one step of learning.

| aardvark<br>使 apricot 与 jam 靠近，<br>apricot w 增大 c pos z w<br>W<br>“…apricot jam…”<br>zebra<br>!<br>aardvark<br>使 apricot 与 matrix 远离<br>减小 c z w<br>jam c neg1<br>pos<br>C<br>matrix c neg1<br>k=2<br>Tolstoy c neg2 使 apricot 与 Tolstoy 远离<br>减小 c z w<br>neg2<br>zebra<br>aardvark<br>move apricot and jam closer,<br>apricot w increasing c pos z w<br>W<br>“…apricot jam…”<br>zebra<br>!<br>aardvark<br>move apricot and matrix apart<br>decreasing c z w<br>jam c neg1<br>pos<br>C<br>matrix c neg1<br>k=2<br>Tolstoy c neg2 move apricot and Tolstoy apart<br>decreasing c z w<br>neg2<br>zebra |  |
| --- | --- |
| 图 5.7<br>Figure 5.7 | 梯度下降一步的直观含义。skip-gram 模型试图移动嵌-<br>Intuition of one step of gradient descent. The skip-gram model tries to shift em- |

> aardvark

| aardvark<br>apricot<br>W<br>zebra<br>!<br>aardvark<br>jam<br>C<br>matrix<br>k=2<br>Tolstoy<br>zebra |  |  |  | 使 apricot 与 jam 靠近，<br>w 增大 c pos z w<br>“…apricot jam…”<br>使 apricot 与 matrix 远离<br>减小 c z w<br>c neg1<br>pos<br>c<br>neg1<br>c 使 apricot 与 Tolstoy 远离<br>neg2<br>减小 c z w<br>neg2<br>move apricot and jam closer,<br>w increasing c pos z w<br>“…apricot jam…”<br>move apricot and matrix apart<br>decreasing c z w<br>c neg1<br>pos<br>c<br>neg1<br>c move apricot and Tolstoy apart<br>neg2<br>decreasing c z w<br>neg2 |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  | apricot |  |  | w |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  | jam |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  | c<br>neg1 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  | Tolstoy |  |  | c<br>neg2 |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

> 使 apricot 与 jam 靠近，
>
> *move apricot and jam closer,*

> apricot w 增大 cpos z w
>
> *apricot w increasing cpos z w*

### W

“…apricot jam…”

> zebra

!

> aardvark 使 apricot 与 matrix 相互远离
>
> *aardvark move apricot and matrix apart*

> jam cpos 递减 cneg1 z w
>
> *jam cpos decreasing cneg1 z w*

### C

> matrix cneg1

> k=2

> Tolstoy cneg2 使 apricot 与 Tolstoy 相互远离
>
> *Tolstoy cneg2 move apricot and Tolstoy apart*

> 递减 cneg2 z w
>
> *decreasing cneg2 z w*

> zebra

> 嵌入，因此目标嵌入（此处为 apricot）与附近单词（此处为 jam）的上下文嵌入更接近（点积更大），而与不在附近出现的噪声词（此处为 Tolstoy 和 matrix）的上下文嵌入更远（点积更小）。
>
> *beddings so the target embeddings (here for apricot) are closer to (have a higher dot product with) context embeddings for nearby words (here jam) and further from (lower dot product with) context embeddings for noise words that don’t occur nearby (here Tolstoy and matrix).*

为了求梯度，我们需要对式 5.21 求关于

> To get the gradient, we need to take the derivative of Eq. 5.21 with respect to

不同嵌入的导数。结果表明导数如下（我们将证明留作本章末尾的练习）：

> the different embeddings. It turns out the derivatives are the following (we leave the proof as an exercise at the end of the chapter):

∂L

= [σ(cpos ·w)−1]w

> (5.22)

∂cpos∂L

> (5.23)

∂cnegi = [σ(cnegi ·w)]w

> k

∂L X∂w = [σ(cpos ·w)−1]cpos +

> (5.24)

[σ(cnegi ·w)]cnegi

> i=1

因此，随机梯度下降中从时间步 t 到 t + 1 的更新方程为：

> The update equations going from time step t to t + 1 in stochastic gradient descent are thus:

ct+1 = ct pos −η[σ(ct pos ·wt)−1]wt

> (5.25)

> pos

ct+1 negi = ct negi −η[σ(ct negi ·wt)]wt

> (5.26)

" #

> k

wt+1 = wt −η X

[σ(ct pos ·wt)−1]ct [σ(ct negi ·wt)]ct

> (5.27)

pos +

> negi

> i=1

因此，与逻辑回归一样，学习算法从随机初始化的 W 和 C 矩阵开始，然后遍历训练语料，利用梯度下降移动 W 和 C，通过执行（式 5.25）—（式 5.27）中的更新来最小化式 5.21 中的损失。

> Just as in logistic regression, then, the learning algorithm starts with randomly initialized W and C matrices, and then walks through the training corpus using gradient descent to move W and C so as to minimize the loss in Eq. 5.21 by making the updates in (Eq. 5.25)-(Eq. 5.27).

142 第 5 章 • 嵌入

> 142 CHAPTER 5 • EMBEDDINGS

回想一下，skip-gram 模型为每个单词 i 学习两个独立的嵌入：

> Recall that the skip-gram model learns two separate embeddings for each word i:

> 目标
>
> *target*

目标嵌入 wi 与上下文嵌入 ci，它们存储在两个矩阵中，即

> the target embedding wi and the context embedding ci, stored in two matrices, the

> 上下文嵌入
>
> *embedding context*

目标矩阵 W 和上下文矩阵 C。通常的做法是把它们直接相加，

> target matrix W and the context matrix C. It’s common to just add them together,

> 嵌入
>
> *embedding*

用向量 wi + ci 表示词 i。另一种做法是丢弃 C 矩阵，只用一个向量 wi 来表示每个词 i。

> representing word i with the vector wi +ci. Alternatively we can throw away the C matrix and just represent each word i by the vector wi.

与 tf-idf 这类简单的基于计数的方法一样，上下文窗口大小

> As with the simple count-based methods like tf-idf, the context window size

会影响 skip-gram 嵌入的性能，实验中常常在开发集上调整上下文窗口大小这个参数。

> affects the performance of skip-gram embeddings, and experiments often tune the context window size parameter on a devset.

### 5.5.3 其他类型的静态嵌入

> 5.5.3 Other kinds of static embeddings

静态嵌入有很多种。作为 word2vec 的一种扩展，fasttext

> There are many kinds of static embeddings. An extension of word2vec, fasttext

> fasttext

（Bojanowski 等，2017）解决了我们目前所介绍的 word2vec 存在的一个问题：它没有好的办法处理未知词——即出现在测试语料中、却在训练语料中未见过的词。与之相关的一个问题是词稀疏，例如在形态丰富的语言中，每个名词和动词的众多形式中有些可能只是偶尔出现。fasttext 通过使用子词模型来处理这些问题，它把每个词表示为该词自身再加上一组构成它的 n-gram，并为每个词添加特殊的边界符号 < 和 >。例如，当 n = 3 时，单词 where 会被表示为序列 <where> 再加上字符 n-gram：

> (Bojanowski et al., 2017), addresses a problem with word2vec as we have presented it so far: it has no good way to deal with unknown words—words that appear in a test corpus but were unseen in the training corpus. A related problem is word sparsity, such as in languages with rich morphology, where some of the many forms for each noun and verb may only occur rarely. Fasttext deals with these problems by using subword models, representing each word as itself plus a bag of constituent n-grams, with special boundary symbols < and > added to each word. For example, with n = 3 the word where would be represented by the sequence <where> plus the character n-grams:

<wh, whe, her, ere, re>

然后为每个构成它的 n-gram 学习一个 skipgram 嵌入，单词 where 就由它的各个构成 n-gram 的嵌入之和来表示。

> Then a skipgram embedding is learned for each constituent n-gram, and the word where is represented by the sum of all of the embeddings of its constituent n-grams.

这样，未知词就只能由其构成 n-gram 的嵌入之和来表示。

> Unknown words can then be represented only by the sum of the constituent n-grams.

fasttext 开源库（其中包含 157 种语言的预训练嵌入）可在 https://fasttext.cc 获取。

> A fasttext open-source library, including pretrained embeddings for 157 languages, is available at https://fasttext.cc.

另一个应用非常广泛的静态嵌入模型是 GloVe（Pennington 等，

> Another very widely used static embedding model is GloVe (Pennington et al.,

2014），它是 Global Vectors 的缩写，因为该模型基于对全局语料统计量的捕捉。GloVe 基于词—词共现矩阵中概率的比值。

> 2014), short for Global Vectors, because the model is based on capturing global corpus statistics. GloVe is based on ratios of probabilities from the word-word cooccurrence matrix.

事实证明，像 word2vec 这样的稠密嵌入与基于计数的嵌入之间实际上存在一种优雅的数学关系，其中 word2vec 可以被看作是隐式地优化一个带有特定（PPMI）加权的计数矩阵函数（Levy and Goldberg, 2014c）。

> It turns out that dense embeddings like word2vec actually have an elegant mathematical relationship with count-based embeddings, in which word2vec can be seen as implicitly optimizing a function of a count matrix with a particular (PPMI) weighting (Levy and Goldberg, 2014c).

## 5.6 嵌入的可视化

> 5.6 Visualizing Embeddings

“只要维度在二维左右，我在很多个维度上都看得很清楚。”

> “I see well in many dimensions as long as the dimensions are around two.”

> 已故经济学家马丁·舒比克（Martin Shubik）
>
> *The late economist Martin Shubik*

可视化嵌入是帮助理解、应用和

> Visualizing embeddings is an important goal in helping understand, apply, and

改进这些词义模型的一个重要目标。但我们怎样可视化一个（例如）100 维的向量呢？

> improve these models of word meaning. But how can we visualize a (for example) 100-dimensional vector?

可视化一个词的含义最简单的方法，

> The simplest way to visualize the meaning of a word

> 手腕 脚踝
>
> *WRIST ANKLE*

就是列出与嵌入在空间中的 w 最相似的词，

> w embedded in a space is to list the most similar words to

> 手臂 肩膀
>
> *ARM SHOULDER*

做法是把词汇表中所有词的向量，按它们与 w 的向量

> w by sorting the vectors for all words in the vocabulary by

> 腿 手 脚
>
> *LEG HAND FOOT*

的余弦值排序。例如，与 frog 最接近的 7 个

> their cosine with the vector for w. For example the 7 closest

> 头 鼻子
>
> *HEAD NOSE*

词（使用某一组特定的嵌入计算得到）

> words to frog using a particular set of embeddings computed

> 手指 脚趾 脸 耳朵 眼睛 牙齿 狗 猫
>
> *FINGER TOE FACE EAR EYE TOOTH DOG CAT*

> 幼犬 小猫 老鼠 奶牛
>
> *PUPPY KITTEN MOUSE COW*

> 乌龟 牡蛎 公牛 狮子 芝加哥 亚特兰大
>
> *TURTLE OYSTER BULL LION CHICAGO ATLANTA*

5.7 • 嵌入的语义特性 143

> 5.7 • SEMANTIC PROPERTIES OF EMBEDDINGS 143

使用 GloVe 算法计算时，最接近的词是：frogs、toad、litoria、leptodactylidae、rana、lizard 和 eleutherodactylus（Pennington 等，2014）。

> with the GloVe algorithm are: frogs, toad, litoria, leptodactylidae, rana, lizard, and eleutherodactylus (Pennington et al., 2014).

还有一种可视化方法是使用聚类

> Yet another visualization method is to use a clustering

算法，以分层的方式展示嵌入空间中哪些词与哪些词相似。左图把一些名词的嵌入向量的层次聚类作为一种可视化方法（Rohde 等，2006）。

> algorithm to show a hierarchical representation of which words are similar to others in the embedding space. The figure on the left uses hierarchical clustering of some embedding vectors for nouns as a visualization method (Rohde et al., 2006).

不过，最常见的可视化方法大概是把单词的 100 个维度投影到 2 维空间。图 5.1 展示了这样一种可视化，图 5.10 也是如此，它使用的投影方法叫作 t-SNE（van der

> Probably the most common visualization method, however, is to project the 100 dimensions of a word down into 2 dimensions. Fig. 5.1 showed one such visualization, as does Fig. 5.10, using a projection method called t-SNE (van der

Maaten and Hinton, 2008）。

> Maaten and Hinton, 2008).

## 5.7 嵌入的语义性质

> 5.7 Semantic properties of embeddings

本节简要概括已有研究考察过的嵌入的一些语义性质。

> In this section we briefly summarize some of the semantic properties of embeddings that have been studied.

不同类型相似性或关联：向量语义模型的一个参数是用于收集计数的上下文窗口大小。它通常是目标词每一侧 1 到 10 个词（总计 2-20 个词的上下文）。

> Different types of similarity or association: One parameter of vector semantic models is the size of the context window used to collect counts. This is generally between 1 and 10 words on each side of the target word (for a total context of 2-20 words).

这一选择取决于表示的目标。较短的上下文窗口

> The choice depends on the goals of the representation. Shorter context windows

往往会产生语法性稍强的表示，因为信息来自紧邻的词。当向量由短上下文窗口计算得到时，与目标词 w 最相似的词往往是词性相同的语义相似词。当向量由长上下文窗口计算得到时，与目标词 w 余弦相似度最高的词往往是主题相关但并不相似的词。

> tend to lead to representations that are a bit more syntactic, since the information is coming from immediately nearby words. When the vectors are computed from short context windows, the most similar words to a target word w tend to be semantically similar words with the same parts of speech. When vectors are computed from long context windows, the highest cosine words to a target word w tend to be words that are topically related but not similar.

例如，Levy and Goldberg（2014a）表明，使用窗口为

> For example Levy and Goldberg (2014a) showed that using skip-gram with a

±2 的 skip-gram 时，与单词 Hogwarts（来自《哈利·波特》系列）最相似的词是其他虚构学校的名称：Sunnydale（来自《吸血鬼猎人巴菲》）或 Evernight（来自一部吸血鬼系列）。窗口为 ±5 时，与 Hogwarts 最相似的词是与《哈利·波特》系列主题相关的其他词：Dumbledore、Malfoy 和 half-blood。

> window of ±2, the most similar words to the word Hogwarts (from the Harry Potter series) were names of other fictional schools: Sunnydale (from Buffy the Vampire Slayer) or Evernight (from a vampire series). With a window of ±5, the most similar words to Hogwarts were other words topically related to the Harry Potter series: Dumbledore, Malfoy, and half-blood.

区分以下两种相似性或关联往往也很有用

> It’s also often useful to distinguish two kinds of similarity or association between

> 一阶
>
> *first-order*

词（Sch¨utze and Pedersen, 1993）。两个词具有一阶共现

> words (Sch¨utze and Pedersen, 1993). Two words have first-order co-occurrence

> 共现
>
> *co-occurrence*

（有时称为组合关系关联），如果它们通常彼此邻近出现。

> (sometimes called syntagmatic association) if they are typically nearby each other.

因此，wrote 是 book 或 poem 的一阶关联词。两个词具有二阶

> Thus wrote is a first-order associate of book or poem. Two words have second-order

> 二阶
>
> *second-order*

共现（有时称为聚合关系关联），如果它们具有相似的

> co-occurrence (sometimes called paradigmatic association) if they have similar

> 共现
>
> *co-occurrence*

邻居。因此，wrote 是 said 或 remarked 这类词的二阶关联词。

> neighbors. Thus wrote is a second-order associate of words like said or remarked.

类比／关系相似性：嵌入的另一项语义性质是它们捕捉关系含义的能力。在一个重要的早期向量空间

> Analogy/Relational Similarity: Another semantic property of embeddings is their ability to capture relational meanings. In an important early vector space model of

> 平行四边形
>
> *parallelogram*

认知模型中，Rumelhart and Abrahamson（1973）提出了平行四边形模型

> cognition, Rumelhart and Abrahamson (1973) proposed the parallelogram model

> 模型
>
> *model*

用于求解形如「a 之于 b 如同 a* 之于什么？」的简单类比问题。在此类问题中，系统会拿到像 apple:tree::grape:? 这样的问题，即 apple 之于 tree 如同 grape 之于 ____，并且必须填入单词 vine。在平行四边形模型中，如第 144 页第 5 章 • 嵌入 图 5.8 所示，从单词 apple 到单词 tree 的向量（= # » tree−# » apple）被加到 grape 的向量（# » grape）上；返回离该点最近的单词。

> for solving simple analogy problems of the form a is to b as a* is to what?. In such problems, a system is given a problem like apple:tree::grape:?, i.e., apple is to tree as grape is to , and must fill in the word vine. In the parallelogram model, il- 144 CHAPTER 5 • EMBEDDINGS lustrated in Fig. 5.8, the vector from the word apple to the word tree (= # » tree−# » apple) is added to the vector for grape (# » grape); the nearest word to that point is returned.

| tree<br>apple<br>vine<br>grape |  |
| --- | --- |
| 图 5.8<br>Figure 5.8 | 类比问题的平行四边形模型（Rumelhart and Abrahamson,<br>The parallelogram model for analogy problems (Rumelhart and Abrahamson, |

tree

apple

vine

grape

> 1973）：从 # » tree 中减去 # » apple 再加上 # » grape，即可得到 # » vine 的位置。
>
> *1973): the location of # » vine can be found by subtracting # » apple from # » tree and adding # » grape.*

在稀疏嵌入的早期研究中，学者们表明稀疏的语义向量模型也能求解这类类比问题（Turney and Littman, 2005），但平行四边形方法因在 word2vec 或 GloVe 向量上取得成功而获得了更现代的关注（Mikolov et al. 2013c, Levy and Goldberg 2014b, Pennington et al. 2014）。例如，表达式 # » king −man + # » # » woman 的结果是一个接近 # » queen 的向量。类似地，# » Paris −# » France + # » Italy 得到的向量接近 # » Rome。因此，嵌入模型似乎提取出了诸如 男性-女性、首都-所属国家，甚至 比较级／最高级 之类关系的表示，如图 5.9 中来自 GloVe 的结果所示。

> In early work with sparse embeddings, scholars showed that sparse vector models of meaning could solve such analogy problems (Turney and Littman, 2005), but the parallelogram method received more modern attention because of its success with word2vec or GloVe vectors (Mikolov et al. 2013c, Levy and Goldberg 2014b, Pennington et al. 2014). For example, the result of the expression # » king −man + # » # » woman is a vector close to # » queen. Similarly, # » Paris −# » France + # » Italy results in a vector that is close to # » Rome. The embedding model thus seems to be extracting representations of relations like MALE-FEMALE, or CAPITAL-CITY-OF, or even COMPARATIVE/SUPERLATIVE, as shown in Fig. 5.9 from GloVe.

| (a) (b) |  |
| --- | --- |
| 图 5.9<br>Figure 5.9 | GloVe 向量空间的关系性质，通过把向量投影到两个维度上展示。<br>Relational properties of the GloVe vector space, shown by projecting vectors onto two dimensions. |

![](images/img_358.png)

![](images/img_347.png)

(a) (b)

> （a）# » king−# » man+ # » woman 接近 # » queen。（b）偏移量似乎捕捉到了比较级和最高级的形态信息（Pennington et al., 2014）。
>
> *(a) # » king−# » man+ # » woman is close to # » queen. (b) offsets seem to capture comparative and superlative morphology(Pennington et al., 2014).*

对于 a : b :: a∗: b∗ 问题，即算法给定向量 a、b 与

> For an a : b :: a∗: b∗problem, meaning the algorithm is given vectors a, b, and

a∗，并且必须找出 b∗，平行四边形方法如下：

> a∗and must find b∗, the parallelogram method is thus:

ˆb∗= argmin distance(x,b−a+a∗)

> (5.28)

> x

其中 distance 是某种距离函数，例如欧氏距离。

> with some distance function, such as Euclidean distance.

这里有一些需要注意的地方。例如，word2vec 或 GloVe 嵌入空间中的平行四边形算法返回的最接近值，通常实际上并不是 5.8 • 偏见与嵌入 145 b*，而是 3 个输入词之一或它们的形态变体（即 cherry:red :: potato:x 返回的是 potato 或 potatoes，而不是 brown），因此必须显式地将它们排除。此外，如果任务涉及高频词、较小的距离以及某些特定关系（如把国家与其首都联系起来，或把动词/名词与它们的屈折形式联系起来），嵌入空间的表现很好，但对其他关系而言，基于嵌入的平行四边形方法效果就不那么好了（Linzen 2016, Gladkova et al. 2016, Schluter 2018, Ethayarajh et al. 2019a）；事实上 Peterson et al.（2020）认为，平行四边形方法总体上过于简单，无法建模人类形成这类类比时的认知过程。

> There are some caveats. For example, the closest value returned by the parallelogram algorithm in word2vec or GloVe embedding spaces is usually not in fact 5.8 • BIAS AND EMBEDDINGS 145 b* but one of the 3 input words or their morphological variants (i.e., cherry:red :: potato:x returns potato or potatoes instead of brown), so these must be explicitly excluded. Furthermore while embedding spaces perform well if the task involves frequent words, small distances, and certain relations (like relating countries with their capitals or verbs/nouns with their inflected forms), the parallelogram method with embeddings doesn’t work as well for other relations (Linzen 2016, Gladkova et al. 2016, Schluter 2018, Ethayarajh et al. 2019a), and indeed Peterson et al. (2020) argue that the parallelogram method is in general too simple to model the human cognitive process of forming analogies of this kind.

### 5.7.1 嵌入与历史语义学

> 5.7.1 Embeddings and Historical Semantics

嵌入也可以成为研究意义如何随时间变化的有用工具，方法是计算多个嵌入空间，每个嵌入空间都来自某一特定时期写成的文本。例如，图 5.10 展示了英语词汇在过去两个世纪中的意义变化可视化，它是通过为每一个十年分别构建嵌入空间计算得到的，所用的历史语料包括 Google n-grams（Lin et al., 2012b）和美国历史英语语料库（Corpus of Historical American English，Davies, 2012）。

> Embeddings can also be a useful tool for studying how meaning changes over time, by computing multiple embedding spaces, each from texts written in a particular time period. For example Fig. 5.10 shows a visualization of changes in meaning in English words over the last two centuries, computed by building separate embedding spaces for each decade from historical corpora like Google n-grams (Lin et al., 2012b) and the Corpus of Historical American English (Davies, 2012).

|  |  |
| --- | --- |
| 图 5.10<br>Figure 5.10 | 对英语中 3 个词的语义变化进行的 t-SNE 可视化，使用的是<br>A t-SNE visualization of the semantic change of 3 words in English using |

![](images/img_392.png)

> word2vec 向量。每个词的现代含义以及灰色的上下文词，都是从最近（现代）时间点的嵌入空间计算得到的；更早的点则由更早的历史嵌入空间计算得到。这些可视化展示了 gay 一词从与“cheerful（快活）”或“frolicsome（嬉闹）”相关的含义转变为指代同性恋，broadcast 现代的“播送”义从其原本“播种”义发展而来，以及 awful 一词的语义贬降——它从意为“full of awe（充满敬畏）”转变为意为“terrible or appalling（可怕或骇人）”（Hamilton et al., 2016b）。
>
> *word2vec vectors. The modern sense of each word, and the grey context words, are computed from the most recent (modern) time-point embedding space. Earlier points are computed from earlier historical embedding spaces. The visualizations show the changes in the word gay from meanings related to “cheerful” or “frolicsome” to referring to homosexuality, the development of the modern “transmission” sense of broadcast from its original sense of sowing seeds, and the pejoration of the word awful as it shifted from meaning “full of awe”to meaning “terrible or appalling” (Hamilton et al., 2016b).*

## 5.8 偏见与嵌入

> 5.8 Bias and Embeddings

除了能够从文本中学习词义之外，遗憾的是，嵌入还会重现文本中潜藏的隐性偏见与刻板印象。正如上一节所示，嵌入可以粗略地建模关系相似性：与‘king’ - ‘man’ + ‘woman’ 最接近的词是‘queen’，这蕴含着类比 man:woman::king:queen。但同样的嵌入类比也表现出性别刻板印象。例如，Bolukbasi et al.（2016）发现，在基于新闻文本训练的 word2vec 嵌入中，与‘computer programmer’ - ‘man’ + ‘woman’ 最接近的职业是‘homemaker’，并且嵌入同样暗示了“‘father’之于‘doctor’相当于‘mother’之于‘nurse’”这一类比。这可能造成 Crawford

> In addition to their ability to learn word meaning from text, embeddings, alas, also reproduce the implicit biases and stereotypes that were latent in the text. As the prior section just showed, embeddings can roughly model relational similarity: ‘queen’ as the closest word to ‘king’ - ‘man’ + ‘woman’ implies the analogy man:woman::king:queen. But these same embedding analogies also exhibit gender stereotypes. For example Bolukbasi et al. (2016) find that the closest occupation to ‘computer programmer’ - ‘man’ + ‘woman’ in word2vec embeddings trained on news text is ‘homemaker’, and that the embeddings similarly suggest the analogy‘father’ is to ‘doctor’ as ‘mother’ is to ‘nurse’. This could result in what Crawford

> 分配性
>
> *allocational*

（2017）和 Blodgett et al.（2020）所称的分配性伤害，即当一个系统分

> (2017) and Blodgett et al. (2020) call an allocational harm, when a system allo-

> 伤害
>
> *harm*

146 第 5 章 • 词嵌入

> 146 CHAPTER 5 • EMBEDDINGS

配资源（工作或信贷）时不公平地分给不同群体。例如，那些把嵌入作为筛选潜在程序员或医生招聘手段的一部分的算法，就可能因此错误地降低含有女性姓名的文档的权重。

> cates resources (jobs or credit) unfairly to different groups. For example algorithms that use embeddings as part of a search for hiring potential programmers or doctors might thus incorrectly downweight documents with women’s names.

事实证明，嵌入不仅反映其输入的统计特性，还会

> It turns out that embeddings don’t just reflect the statistics of their input, but also

> 偏见
>
> *bias*

放大偏见；带有性别色彩的词在嵌入空间中变得比它们

> amplify bias; gendered terms become more gendered in embedding space than they

> 放大
>
> *amplification*

在输入文本的统计中更具性别色彩（Zhao et al. 2017, Ethayarajh et al. 2019b, Jia et al. 2020），并且这些偏见比实际劳动力就业统计中的情况更为夸张（Garg et al., 2018）。

> were in the input text statistics (Zhao et al. 2017, Ethayarajh et al. 2019b, Jia et al. 2020), and biases are more exaggerated than in actual labor employment statistics(Garg et al., 2018).

嵌入还编码了隐含联想，而这是人类

> Embeddings also encode the implicit associations that are a property of human

推理的一种特性。内隐联想测验（Implicit Association Test，Greenwald et al., 1998）通过测量人们对各类别词汇进行标注时的反应延迟差异，来衡量人们对概念（如‘flowers’或‘insects’）与属性（如‘pleasantness’和‘unpleasantness’）之间的联想。3 使用这类方法，美国境内的人被证明会把非裔美国人的名字与不愉悦的词联系起来（强于对欧裔美国人名字的联想），把男性名字更多地与数学联系起来、把女性名字与艺术联系起来，并把老年人的名字与不愉悦的词联系起来（Greenwald et al. 1998, Nosek et al. 2002a, Nosek et al. 2002b）。Caliskan et al.（2017）用 GloVe 向量和余弦相似度代替人类的反应延迟，复现了所有这些内隐联想的发现。例如，像‘Leroy’和‘Shaniqua’这样的非裔美国人名字与不愉悦词的 GloVe 余弦相似度更高，而欧裔美国人名字（‘Brad’、‘Greg’、‘Courtney’）与愉悦词的余弦相似度更高。这些与嵌入有关的问题正是代表性伤害的一个例子（Crawford 2017, Blodgett et al. 2020），它是由

> reasoning. The Implicit Association Test (Greenwald et al., 1998) measures people’s associations between concepts (like ‘flowers’ or ‘insects’) and attributes (like‘pleasantness’ and ‘unpleasantness’) by measuring differences in the latency with which they label words in the various categories.3 Using such methods, people in the United States have been shown to associate African American names with unpleasant words (more than European-American names), male names more with mathematics and female names with the arts, and old people’s names with unpleasant words (Greenwald et al. 1998, Nosek et al. 2002a, Nosek et al. 2002b). Caliskan et al. (2017) replicated all these findings of implicit associations using GloVe vectors and cosine similarity instead of human latencies. For example African American names like ‘Leroy’ and ‘Shaniqua’ had a higher GloVe cosine with unpleasant words while European-American names (‘Brad’, ‘Greg’, ‘Courtney’) had a higher cosine with pleasant words. These problems with embeddings are an example of a representational harm (Crawford 2017, Blodgett et al. 2020), which is a harm caused by

> 代表性
>
> *representational*

> 伤害
>
> *harm*

系统贬低甚至忽视某些社会群体而造成的伤害。因此，任何使用了词语情感倾向、能够感知嵌入的算法，都可能加剧对非裔美国人的偏见。

> a system demeaning or even ignoring some social groups. Any embedding-aware algorithm that made use of word sentiment could thus exacerbate bias against African Americans.

近期研究聚焦于设法去除这类偏见的方法，例如

> Recent research focuses on ways to try to remove these kinds of biases, for

通过设计一种对嵌入空间的变换，去除性别刻板印象但保留与定义相关的性别信息（Bolukbasi et al. 2016, Zhao et al. 2017），或者改变训练过程（Zhao et al., 2018b）。然而，尽管这类去偏可能减少嵌入中的偏见，但并不能消除它

> example by developing a transformation of the embedding space that removes gender stereotypes but preserves definitional gender (Bolukbasi et al. 2016, Zhao et al. 2017) or changing the training procedure (Zhao et al., 2018b). However, although these sorts of debiasing may reduce bias in embeddings, they do not eliminate it

> 去偏
>
> *debiasing*

（Gonen and Goldberg, 2019），这仍是一个未解决的问题。

> (Gonen and Goldberg, 2019), and this remains an open problem.

历史嵌入也被用来衡量过去的偏见。Garg

> Historical embeddings are also being used to measure biases in the past. Garg

et al.（2018）使用来自历史文本的嵌入，衡量整个 20 世纪中职业的嵌入与各种族裔或性别的名字的嵌入之间的关联（例如女性名字相对于男性名字与‘librarian’或‘carpenter’这类职业词之间的余弦相似度）。

> et al. (2018) used embeddings from historical texts to measure the association between embeddings for occupations and embeddings for names of various ethnicities or genders (for example the relative cosine similarity of women’s names versus men’s to occupation words like ‘librarian’ or ‘carpenter’) across the 20th century.

他们发现，这些余弦相似度与那些职业中女性或族裔群体在历史上的实际百分比相关。历史嵌入还复现了早期关于族裔刻板印象的调查：1933 年的实验参与者倾向于把‘industrious（勤勉）’或‘superstitious（迷信）’这类形容词与例如华裔联系起来，这种倾向与使用 1930 年代文本训练的嵌入中中文姓氏与这些形容词之间的余弦相似度相关。他们还能够记录历史上的性别偏见，例如与能力相关的形容词（‘smart’、‘wise’、‘thoughtful’、‘resourceful’）的嵌入与男性词的余弦相似度高于与女性词的余弦相似度，并表明这种偏见自 1960 年以来一直在缓慢减弱。我们

> They found that the cosines correlate with the empirical historical percentages of women or ethnic groups in those occupations. Historical embeddings also replicated old surveys of ethnic stereotypes; the tendency of experimental participants in 1933 to associate adjectives like ‘industrious’ or ‘superstitious’ with, e.g., Chinese ethnicity, correlates with the cosine between Chinese last names and those adjectives using embeddings trained on 1930s text. They also were able to document historical gender biases, such as the fact that embeddings for adjectives related to competence(‘smart’, ‘wise’, ‘thoughtful’, ‘resourceful’) had a higher cosine with male than female words, and showed that this bias has been slowly decreasing since 1960. We

> 3

> 粗略地说，如果人类把‘flowers’与‘pleasantness’联系起来、把‘insects’与‘unpleasantness’联系起来，那么当他们被要求为‘flowers’（daisy、iris、lilac）和‘pleasant words’（love、laughter、pleasure）按绿色按钮、为‘insects’（flea、spider、mosquito）和‘unpleasant words’（abuse、hatred、ugly）按红色按钮时，他们的反应要比在不一致条件下更快——在不一致条件下，他们要分别为‘flowers’和‘unpleasant words’按红色按钮、为‘insects’和‘pleasant words’按绿色按钮。
>
> *Roughly speaking, if humans associate ‘flowers’ with ‘pleasantness’ and ‘insects’ with ‘unpleasantness’, when they are instructed to push a green button for ‘flowers’ (daisy, iris, lilac) and ‘pleasant words’(love, laughter, pleasure) and a red button for ‘insects’ (flea, spider, mosquito) and ‘unpleasant words’(abuse, hatred, ugly) they are faster than in an incongruous condition where they push a red button for‘flowers’ and ‘unpleasant words’ and a green button for ‘insects’ and ‘pleasant words’.*

5.9 • 向量模型的评估 147

> 5.9 • EVALUATING VECTOR MODELS 147

将在后续章节回到这个关于偏见在自然语言处理中所起作用的问题。

> return in later chapters to this question about the role of bias in natural language processing.

## 5.9 向量模型的评估

> 5.9 Evaluating Vector Models

对向量模型来说，最重要的评价指标是在任务上的外部评价，即在某个自然语言处理任务中使用向量，看它是否比其他某些模型能带来更好的性能。

> The most important evaluation metric for vector models is extrinsic evaluation on tasks, i.e., using vectors in an NLP task and seeing whether this improves performance over some other model.

尽管如此，进行内部评价仍是有用的。最常见的指标

> Nonetheless it is useful to have intrinsic evaluations. The most common metric

是测试它们在相似度上的表现，即计算算法给出的词语相似度分数与人工给出的词语相似度评分之间的相关性。

> is to test their performance on similarity, computing the correlation between an algorithm’s word similarity scores and word similarity ratings assigned by humans.

WordSim-353（Finkelstein et al., 2002）是一组常用的评分数据，包含 353 个名词对的 0 到 10 分评分；例如（plane, car）的平均分为 5.77。

> WordSim-353 (Finkelstein et al., 2002) is a commonly used set of ratings from 0 to 10 for 353 noun pairs; for example (plane, car) had an average score of 5.77.

SimLex-999（Hill 等，2015）是一个更复杂的数据集，它量化的是相似性 similarity(cup, mug)，而非相关性 relatedness(cup, coffee)，并包含具体与抽象的形容词、名词和动词对。TOEFL 数据集是一组 80 道题，每道题由一个目标词和 4 个额外词选项组成；任务是选出其中正确的同义词，如示例所示：Levied 在意义上最接近的是：imposed、believed、requested、correlated（Landauer and Dumais, 1997）。所有这些数据集给出的词都不带上下文。

> SimLex-999 (Hill et al., 2015) is a more complex dataset that quantifies similarity(cup, mug) rather than relatedness (cup, coffee), and includes concrete and abstract adjective, noun and verb pairs. The TOEFL dataset is a set of 80 questions, each consisting of a target word with 4 additional word choices; the task is to choose which is the correct synonym, as in the example: Levied is closest in meaning to: imposed, believed, requested, correlated (Landauer and Dumais, 1997). All of these datasets present words without context.

略微更贴近实际的是包含上下文的内部相似性任务。

> Slightly more realistic are intrinsic similarity tasks that include context. The

Stanford Contextual Word Similarity（SCWS）数据集（Huang 等，2012）和 Word-in-Context（WiC）数据集（Pilehvar and Camacho-Collados, 2019）提供了更丰富的评测场景。SCWS 给出对 2,003 对词在其句子上下文中的相似性的人工判断，而 WiC 给出处于两个句子上下文中的目标词，这两个上下文要么属于同一义项，要么属于不同义项；参见附录 I。语义文本相似性任务（Agirre 等 2012，Agirre 等 2015）评估句子级相似度算法的性能，该任务由一组句子对构成，每对句子都带有人工标注的相似度分数。

> Stanford Contextual Word Similarity (SCWS) dataset (Huang et al., 2012) and the Word-in-Context (WiC) dataset (Pilehvar and Camacho-Collados, 2019) offer richer evaluation scenarios. SCWS gives human judgments on 2,003 pairs of words in their sentential context, while WiC gives target words in two sentential contexts that are either in the same or different senses; see Appendix I. The semantic textual similarity task (Agirre et al. 2012, Agirre et al. 2015) evaluates the performance of sentencelevel similarity algorithms, consisting of a set of pairs of sentences, each pair with human-labeled similarity scores.

另一种用于评估的任务是类比任务，已在第 143 页讨论，

> Another task used for evaluation is the analogy task, discussed on page 143,

在这类任务中，系统必须求解形如「a 之于 b 相当于 a* 之于 b*」的问题，给定 a、b 和 a*，要求找出 b*（Turney and Littman, 2005）。人们已为该任务创建了若干元组集合（Mikolov 等 2013a，Mikolov 等 2013c，Gladkova 等 2016），涵盖形态关系（city:cities::child:children）、词汇关系（leg:table::spout:teapot）和百科关系（Beijing:China::Dublin:Ireland），其中一些取自 SemEval-2012 任务 2 中 79 种不同关系的数据集（Jurgens 等，2012）。

> where the system has to solve problems of the form a is to b as a* is to b*, given a, b, and a* and having to find b* (Turney and Littman, 2005). A number of sets of tuples have been created for this task (Mikolov et al. 2013a, Mikolov et al. 2013c, Gladkova et al. 2016), covering morphology (city:cities::child:children), lexicographic relations (leg:table::spout:teapot) and encyclopedia relations (Beijing:China::Dublin:Ireland), some drawing from the SemEval-2012 Task 2 dataset of 79 different relations (Jurgens et al., 2012).

所有嵌入算法都存在固有的变异性。例如，由于

> All embedding algorithms suffer from inherent variability. For example because

初始化中的随机性和随机负采样，像 word2vec 这样的算法即使在同一个数据集上也可能产生不同的结果，而且集合中个别文档可能对所得的嵌入产生很大影响（Tian 等 2016，Hellrich and Hahn 2016，Antoniak and Mimno 2018）。因此，当使用嵌入来研究特定语料库中的词语关联时，最佳做法是对文档进行自助采样（bootstrap sampling）来训练多个嵌入，并对结果取平均（Antoniak and Mimno, 2018）。

> of randomness in the initialization and the random negative sampling, algorithms like word2vec may produce different results even from the same dataset, and individual documents in a collection may strongly impact the resulting embeddings(Tian et al. 2016, Hellrich and Hahn 2016, Antoniak and Mimno 2018). When embeddings are used to study word associations in particular corpora, therefore, it is best practice to train multiple embeddings with bootstrap sampling over documents and average the results (Antoniak and Mimno, 2018).

148 第 5 章 • 嵌入

> 148 CHAPTER 5 • EMBEDDINGS

## 5.10 小结

> 5.10 Summary

- 在向量语义学中，一个词被建模为一个向量——高维空间中的一个点，也称为嵌入。本章我们关注静态嵌入，即每个词都被映射到一个固定的嵌入。
- 向量语义模型分为两类：稀疏模型和稠密模型。在稀疏模型中，每个维度对应词汇表 V 中的一个词，单元格是共现计数的某种函数。词—上下文矩阵（或称词项—词项矩阵）为词汇表中的每个（目标）词设一行，为词汇表中的每个上下文词项设一列。
- 稠密向量模型的维度通常为 50–1000。像 skip-gram 这样的 word2vec 算法是计算稠密嵌入的常用方法。

> In vector semantics, a word is modeled as a vector—a point in high-dimensional space, also called an embedding. In this chapter we focus on static embeddings, where each word is mapped to a fixed embedding.
> Vector semantic models fall into two classes: sparse and dense. In sparse models each dimension corresponds to a word in the vocabulary V and cells are functions of co-occurrence counts. The word-context or term-term matrix has a row for each (target) word in the vocabulary and a column for each context term in the vocabulary.
> Dense vector models typically have dimensionality 50–1000. Word2vec algorithms like skip-gram are a popular way to compute dense embeddings.

skip-gram 训练一个逻辑回归分类器，以计算两个词「可能在文本中邻近出现」的概率。该概率由这两个词的嵌入之间的点积计算得到。

> Skip-gram trains a logistic regression classifier to compute the probability that two words are ‘likely to occur nearby in text’. This probability is computed from the dot product between the embeddings for the two words.

- skip-gram 使用随机梯度下降来训练该分类器，其学习目标是使嵌入与邻近出现的词的嵌入具有高点积，而与噪声词具有低点积。
- 其他重要的嵌入算法包括 GloVe，这是一种基于词共现概率之比的方法。
- 无论使用稀疏向量还是稠密向量，词与文档的相似度都由向量之间点积的某种函数计算得到。两个向量的余弦——一种归一化的点积——是这类度量中最常用的一种。

> Skip-gram uses stochastic gradient descent to train the classifier, by learning embeddings that have a high dot product with embeddings of words that occur nearby and a low dot product with noise words.
> Other important embedding algorithms include GloVe, a method based on ratios of word co-occurrence probabilities.
> Whether using sparse or dense vectors, word and document similarities are computed by some function of the dot product between vectors. The cosine of two vectors—a normalized dot product—is the most popular of such metrics.

## 历史注记

> Historical Notes

向量语义学的思想源于 20 世纪 50 年代三个不同领域的研究：语言学、心理学和计算机科学，每个领域都贡献了该模型的一个基本方面。

> The idea of vector semantics arose out of research in the 1950s in three distinct fields: linguistics, psychology, and computer science, each of which contributed a fundamental aspect of the model.

意义与词在上下文中的分布有关这一观点，

> The idea that meaning is related to the distribution of words in context was

在 20 世纪 50 年代的语言学理论中广为流传，持此观点的有 Zellig Harris、Martin Joos 和 J. R. Firth 等分布主义者，以及 Thomas Sebeok 等符号学家。正如 Joos（1950）所说，

> widespread in linguistic theory of the 1950s, among distributionalists like Zellig Harris, Martin Joos, and J. R. Firth, and semioticians like Thomas Sebeok. As Joos(1950) put it,

> 语言学家所说的语素「意义」……按定义就是该语素在与所有其他语素共现的上下文中的条件概率集合。
>
> *the linguist’s “meaning” of a morpheme. . . is by definition the set of conditional probabilities of its occurrence in context with all other morphemes.*

词的意义可以被建模为多维语义空间中的一个点，这一想法来自 Charles E. Osgood 等心理学家，他此前一直在研究人们如何通过在快乐/悲伤或硬/软等量表上赋分来回应词的意义。Osgood 等（1957）提出，一般而言，词的意义可以建模为多维欧几里得空间中的一个点，而两个词之间意义的相似性可以建模为该空间中这些点之间的距离。

> The idea that the meaning of a word might be modeled as a point in a multidimensional semantic space came from psychologists like Charles E. Osgood, who had been studying how people responded to the meaning of words by assigning values along scales like happy/sad or hard/soft. Osgood et al. (1957) proposed that the meaning of a word in general could be modeled as a point in a multidimensional Euclidean space, and that the similarity of meaning between two words could be modeled as the distance between these points in the space.

20 世纪 50 年代和 60 年代初的最后一个思想来源，是当时被称为

> A final intellectual source in the 1950s and early 1960s was the field then called

> 机械
>
> *mechanical*

机械索引的领域，现在称为信息检索。在后来被称为

> mechanical indexing, now known as information retrieval. In what became known

> 索引
>
> *indexing*

信息检索的向量空间模型（Salton 1971，Sparck Jones 历史注记 149 1986）的那项工作中，研究者展示了用向量来定义词义的新方法（Switzer, 1965），并改进了基于词间统计关联度量（如互信息（Giuliano, 1965）和 idf（Sparck Jones, 1972））的词相似度方法，还表明文档的意义可以在与词相同的向量空间中表示。大约在同一时期，Cordier（1965）表明，对词关联概率做因子分析可以用来形成词的稠密向量表示。

> as the vector space model for information retrieval (Salton 1971, Sparck Jones HISTORICAL NOTES 149 1986), researchers demonstrated new ways to define the meaning of words in terms of vectors (Switzer, 1965), and refined methods for word similarity based on measures of statistical association between words like mutual information (Giuliano, 1965) and idf (Sparck Jones, 1972), and showed that the meaning of documents could be represented in the same vector spaces used for words. Around the same time, Cordier (1965) showed that factor analysis of word association probabilities could be used to form dense vector representations of words.

分布式思维方式的一些哲学基础，

> Some of the philosophical underpinning of the distributional way of thinking

来自哲学家维特根斯坦（Wittgenstein）晚期的著作，他对为每个词建立完全形式化的意义定义理论的可能性持怀疑态度。维特根斯坦转而提出，「一个词的意义就是它在语言中的用法」（Wittgenstein, 1953, PI 43）。也就是说，维特根斯坦的想法是不用某种逻辑语言来定义每个词，也不诉诸外延或真值，而是应当根据人们在日常交往中说话和理解时如何使用一个词来定义它，从而预示了语言学和自然语言处理中走向具身与体验式模型的运动（Glenberg and Robertson 2000, Lake and Murphy 2021, Bisk et al. 2020, Bender and Koller 2020）。

> came from the late writings of the philosopher Wittgenstein, who was skeptical of the possibility of building a completely formal theory of meaning definitions for each word. Wittgenstein suggested instead that “the meaning of a word is its use in the language” (Wittgenstein, 1953, PI 43). That is, instead of using some logical language to define each word, or drawing on denotations or truth values, Wittgenstein’s idea is that we should define a word by how it is used by people in speaking and understanding in their day-to-day interactions, thus prefiguring the movement toward embodied and experiential models in linguistics and NLP (Glenberg and Robertson 2000, Lake and Murphy 2021, Bisk et al. 2020, Bender and Koller 2020).

关系更远一些的是用离散特征向量来定义词的想法，其根源至少可以追溯到笛卡尔（Descartes）和莱布尼茨（Leibniz）（Wierzbicka 1992, Wierzbicka 1996）。到 20 世纪中叶，从 Hjelmslev 的工作（Hjelmslev, 1969）（原版为 1943）开始，并在生成语法的早期模型（Katz and Fodor, 1963）中得到充实，出现了用「意

> More distantly related is the idea of defining words by a vector of discrete features, which has roots at least as far back as Descartes and Leibniz (Wierzbicka 1992, Wierzbicka 1996). By the middle of the 20th century, beginning with the work of Hjelmslev (Hjelmslev, 1969) (originally 1943) and fleshed out in early models of generative grammar (Katz and Fodor, 1963), the idea arose of representing mean-

> 语义
>
> *semantic*

义」用语义特征来表示的想法，这类特征符号代表某种原始意义。

> ing with semantic features, symbols that represent some sort of primitive meaning.

> 特征
>
> *feature*

例如 hen、rooster 或 chick 这类词有共同之处（它们都描述鸡），也有不同之处（它们的年龄和性别），可以表示为：

> For example words like hen, rooster, or chick, have something in common (they all describe chickens) and something different (their age and sex), representable as:

hen +female, +chicken, +adult rooster -female, +chicken, +adult chick +chicken, -adult

然而，意义的向量模型用来定义词的那些维度，

> The dimensions used by vector models of meaning to define words, however, are

只是抽象地与这种由少量固定的手工构建维度构成的想法相关。

> only abstractly related to this idea of a small fixed number of hand-built dimensions.

尽管如此，已有一些尝试表明，嵌入模型的某些维度确实像这些早期的语义特征一样，贡献了意义的某个特定的组合方面。

> Nonetheless, there has been some attempt to show that certain dimensions of embedding models do contribute some specific compositional aspect of meaning like these early semantic features.

用稠密向量来建模词义的做法，乃至 embedding（嵌入）这一术语本身，都源于潜在语义索引（latent semantic indexing，LSI）模型（Deerwester et al., 1988），该模型后来被重新表述为 LSA（latent semantic analysis，潜在语义分析）（Deerwester et al., 1990）。在 LSA 中，奇异值分解——SVD——被应用于一个词项-文档矩阵（每个

> The use of dense vectors to model word meaning, and indeed the term embedding, grew out of the latent semantic indexing (LSI) model (Deerwester et al., 1988) recast as LSA (latent semantic analysis) (Deerwester et al., 1990). In LSA singular value decomposition—SVD— is applied to a term-document matrix (each

> SVD

单元格按对数频率加权并按熵归一化），然后取前 300 个维度作为 LSA 嵌入。奇异值分解（Singular Value Decomposition，SVD）是一种找出数据集最重要维度的方法，即数据变化最大的那些维度。LSA 随后迅速得到广泛应用：作为认知模型（Landauer and Dumais, 1997），以及用于拼写检查（Jones and Martin, 1997）、语言建模（Bellegarda 1997，Coccaro and Jurafsky 1998，Bellegarda 2000）、形态归纳（Schone and Jurafsky 2000，Schone and Jurafsky 2001b）、多词表达（multiword expressions，MWE）（Schone and Jurafsky, 2001a）和作文评分（Rehder et al., 1998）等任务。与此同时，Sch¨utze（1992b）也独立开发了相关模型并将其应用于词义消歧。

> cell weighted by log frequency and normalized by entropy), and then the first 300 dimensions are used as the LSA embedding. Singular Value Decomposition (SVD) is a method for finding the most important dimensions of a dataset, those dimensions along which the data varies the most. LSA was then quickly widely applied: as a cognitive model (Landauer and Dumais, 1997), and for tasks like spell checking(Jones and Martin, 1997), language modeling (Bellegarda 1997, Coccaro and Jurafsky 1998, Bellegarda 2000), morphology induction (Schone and Jurafsky 2000, Schone and Jurafsky 2001b), multiword expressions (MWEs) (Schone and Jurafsky, 2001a), and essay grading (Rehder et al., 1998). Related models were simultaneously developed and applied to word sense disambiguation by Sch¨utze (1992b).

LSA 还促成了最早在概率分类器中使用嵌入表示词的做法，即 Sch¨utze et al.（1995）的逻辑回归文档路由器。

> LSA also led to the earliest use of embeddings to represent words in a probabilistic classifier, in the logistic regression document router of Sch¨utze et al. (1995).

在词项-词项矩阵（而非词项-文档矩阵）上做 SVD，以此作为 NLP 的意义模型，150 第 5 章 • 嵌入 这一想法在 LSA 之后不久由 Sch¨utze（1992b）提出。

> The idea of SVD on the term-term matrix (rather than the term-document matrix) 150 CHAPTER 5 • EMBEDDINGS as a model of meaning for NLP was proposed soon after LSA by Sch¨utze (1992b).

Sch¨utze 将 SVD 产生的低秩（97 维）嵌入应用于词义消歧任务，分析了由此得到的语义空间，还提出了可能的技术，如丢弃高阶维度。参见 Sch¨utze（1997）。

> Sch¨utze applied the low-rank (97-dimensional) embeddings produced by SVD to the task of word sense disambiguation, analyzed the resulting semantic space, and also suggested possible techniques like dropping high-order dimensions. See Sch¨utze(1997).

在早期的 SVD 工作之后，又出现了一系列替代的矩阵模型，

> A number of alternative matrix models followed on from the early SVD work,

包括概率潜在语义索引（Probabilistic Latent Semantic Indexing，PLSI）（Hofmann, 1999）、潜在狄利克雷分配（Latent Dirichlet Allocation，LDA）（Blei et al., 2003）和非负矩阵分解（Non-negative Matrix Factorization，NMF）（Lee and Seung, 1999）。

> including Probabilistic Latent Semantic Indexing (PLSI) (Hofmann, 1999), Latent Dirichlet Allocation (LDA) (Blei et al., 2003), and Non-negative Matrix Factorization (NMF) (Lee and Seung, 1999).

LSA 学界似乎最早是在 Landauer

> The LSA community seems to have first used the word “embedding” in Landauer

et al.（1997）中使用了“embedding”一词，用的是其数学含义的一个变体，即从一个空间或数学结构到另一个空间的映射。在 LSA 中，embedding 一词似乎指的是从稀疏计数向量空间到 SVD 稠密向量的潜在空间的映射。因此，尽管该词最初意指从一个空间到另一个空间的映射，但它已通过转喻转变为指潜在空间中由此得到的稠密向量，而我们当前正是在这个意义上使用该词。

> et al. (1997), in a variant of its mathematical meaning as a mapping from one space or mathematical structure to another. In LSA, the word embedding seems to have described the mapping from the space of sparse count vectors to the latent space of SVD dense vectors. Although the word thus originally meant the mapping from one space to another, it has metonymically shifted to mean the resulting dense vector in the latent space, and it is in this sense that we currently use the word.

到下一个十年，Bengio et al.（2003）和 Bengio et al.（2006）表明，

> By the next decade, Bengio et al. (2003) and Bengio et al. (2006) showed that

神经语言模型也可以用来发展嵌入，并将其作为词预测任务的一部分。随后 Collobert and Weston（2007）、Collobert and Weston（2008）和 Collobert et al.（2011）证明，嵌入可用于表示多种 NLP 任务中的词义。Turian et al.（2010）比较了不同种类的嵌入在不同 NLP 任务中的价值。Mikolov et al.（2011）表明循环神经网络可以用作语言模型。将这些神经网络语言模型的隐藏层简化以构造 skipgram（以及 CBOW）算法的想法由 Mikolov et al.（2013a）提出。负采样训练算法在 Mikolov et al.（2013b）中提出。关于静态嵌入及其参数化有大量综述（Bullinaria and Levy 2007，Bullinaria and Levy 2012，Lapesa and Evert 2014，Kiela and Clark 2014，Levy et al. 2015）。

> neural language models could also be used to develop embeddings as part of the task of word prediction. Collobert and Weston (2007), Collobert and Weston (2008), and Collobert et al. (2011) then demonstrated that embeddings could be used to represent word meanings for a number of NLP tasks. Turian et al. (2010) compared the value of different kinds of embeddings for different NLP tasks. Mikolov et al. (2011) showed that recurrent neural nets could be used as language models. The idea of simplifying the hidden layer of these neural net language models to create the skipgram (and also CBOW) algorithms was proposed by Mikolov et al. (2013a). The negative sampling training algorithm was proposed in Mikolov et al. (2013b). There are numerous surveys of static embeddings and their parameterizations (Bullinaria and Levy 2007, Bullinaria and Levy 2012, Lapesa and Evert 2014, Kiela and Clark 2014, Levy et al. 2015).

要更深入地理解其作用，参见 Manning et al.（2008）和第 11 章

> See Manning et al. (2008) and Chapter 11 for a deeper understanding of the role

即向量在信息检索中的作用，包括如何比较查询与文档、关于 tf-idf 的更多细节，以及扩展到超大规模数据集的问题。关于 word2vec 的清晰而全面的教程，参见 Kim（2019）。Cruse（2004）是一本关于词汇语义学的有用语言学入门教材。

> of vectors in information retrieval, including how to compare queries with documents, more details on tf-idf, and issues of scaling to very large datasets. See Kim(2019) for a clear and comprehensive tutorial on word2vec. Cruse (2004) is a useful introductory linguistic text on lexical semantics.

## 练习

> Exercises

5.1 使用图 5.2 中的共现计数，计算 cos(cherry, strawberry)

> 5.1 Using the co-occurrence counts in Fig. 5.2, compute cos(cherry, strawberry)

以及仅使用 pie 和 result 两个维度的 cos(cherry, digital)。哪一对更相似，结果是否符合你关于这些词含义的直觉？

> and cos(cherry, digital) using only the pie and result dimensions. Which pair is more similar, and does the result match your intuition about the words’meanings?

5.2 证明余弦相似度对缩放不变：对任意正常数 c，

> 5.2 Show that cosine similarity is invariant to scaling: for any positive constant c,

cos(cv,w) = cos(v,w)。鉴于第 5.4 节对频率和向量长度的讨论，为什么这是词相似度度量所期望的一个性质？

> cos(cv,w) = cos(v,w). Why is this a desirable property for a word-similarity metric, given the discussion of frequency and vector length in Section 5.4?

5.3 通过对损失函数求导，推导式 5.22-式 5.24 中的 SGNS 梯度，该损失函数为

> 5.3 Derive the SGNS gradients in Eq. 5.22-Eq. 5.24 by differentiating the loss in

式 5.21，分别对 cpos、cneg 和 w 求导。你可以利用 dσ(z) =

> Eq. 5.21 with respect to cpos, cneg, and w. You may use the fact that dσ(z) =

> dz

σ(z)(1−σ(z))，以及 d(cw) = c。

> σ(z)(1−σ(z)) and that d(cw) = c.

> dw
