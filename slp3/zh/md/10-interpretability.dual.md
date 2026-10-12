# 第 10 章 可解释性

### 章

> CHAPTER

# 10 可解释性

> 10 Interpretability

“我们所见的一切，都是我们所未见之物投下的影子”

> “Everything that we see is a shadow cast by that which we do not see”

> 马丁·路德·金（Martin Luther King, Jr.），在底特律教会协进会的布道，1961 年
>
> *Martin Luther King, Jr., Sermon at the Detroit Council of Churches, 1961*

在这一章（目前仍为梗概）中，我们转向 LLM 可解释性，它有时

> In this (currently stub) chapter we turn to LLM interpretability, sometimes

> 可解释性
>
> *interpretability*

被称为机制可解释性（mechanistic interpretability）。在这里，研究者寻找能帮助我们理解语言模型如何完成其工作的方法。大部分工作聚焦于揭示模型的内部表示——它们似乎在编码何种含义——以及模型的推理路径，即我们能否描述出具体的“回路”。

> called mechanistic interpretability. Here researchers search for methods that will help us understand how language models do what they do. Much of the work focuses on uncovering the model’s internal representations what kind of meanings they seem to encode, as well as the models paths for reasoning, whether we can describe specific “circuits”.

## 10.1 上下文嵌入

> 10.1 Contextual Embeddings

我们首先扩展第 5 章所介绍的嵌入的基本思想，来看一看 transformer 及其他 LLM 架构中对应的思想。第 5 章的方法（如 word2vec 或 GloVe）为词汇表中的每个唯一词 w 学习单个向量嵌入。相比之下，在上下文嵌入中，每个词 w 每次出现在不同上下文中时都会由不同的向量来表示。上下文嵌入既用于第 7 章的因果语言模型，也用于第 9 章的编码器模型，不过由掩码语言模型生成的嵌入作为表示似乎效果特别好，因此我们在示例中将使用这类嵌入。

> Let’s begin by extending the fundamental idea of embeddings that we introduce in Chapter 5 to see the corresponding idea in transformers and other LLM architectures. The methods of Chapter 5 like word2vec or GloVe learned a single vector embedding for each unique word w in the vocabulary. By contrast, with contextual embeddings, each word w will be represented by a different vector each time it appears in a different context. Contextual embeddings are used in both the causal language models of Chapter 7 and in the encoder models of Chapter 9, although the embeddings created by masked language models seem to function particularly well as representations, so we will use those in examples.

当把一段文本输入预训练语言模型时，模型各组件（注意力头、前馈网络）的输出都是被加入残差流的表示。这些表示中的每一个，它们出现在

> When a text is fed to a pretrained language model, the output of each component of the model (the attention heads, the feedforward network) is a representation that gets added into the residual stream. Each of these representations, which occur

> 上下文
>
> *contextual*

每一层、每个 token 上，都被称为上下文嵌入。正如我们提到的，一种理解上下文嵌入的方式是：把它们看作编码某个 token 在上下文中含义某一方面的向量，像是第 5 章静态嵌入的上下文化版本。因此，我们可以把这些嵌入用于涉及 token 或词义的任务。

> at every level and for every token, are called contextual embeddings. As we suggested, one way to think of contextual embeddings is as vectors that encode some aspect of the meaning of a token in context, like a contextualized version of the static embeddings of Chapter 5. As such, we can use these embeddings for tasks involving the meaning of tokens or words.

> 嵌入
>
> *embeddings*

例如，给定输入 token 序列 x1,...,xn，我们可以使用输出

> For example, given a sequence of input tokens x1,...,xn, we can use the output

向量 hLi 作为 token xi 在句子 x1,...,xn 上下文中含义的表示，其中该向量来自模型的最后一层 L，如图 10.1 所示。

> vector hLi from the final layer L of a model aes a representation of the meaning of token xi in the context of sentence x1,...,xn, as shown in Fig. 10.1.

对于 BERT 模型，并不只使用模型最后一层的向量 hLi，

> For BERT models, instead of just using the vector hLi from the final layer of

常见的做法是通过对模型最后四层的输出 token hi 做均值池化或最大池化来计算 xi 的表示，即 hLi、hL−1i、hL−2i 和 hL−3i。

> the model, it’s common to compute a representation for xi by mean pooling or max pooling the output tokens hi from each of the last four layers of the model, i.e., hLi, hL−1i, hL−2i, and hL−3i.

正如我们在第 5 章用 word2vec 这类静态嵌入来表示

> Just as we used static embeddings like word2vec in Chapter 5 to represent the

词的含义一样，我们也可以把上下文嵌入用作上下文中词义的表示，用于任何可能需要词义模型的任务。而

> meaning of words, we can use contextual embeddings as representations of word meanings in context for any task that might require a model of word meaning. Where

243 244 第 10 章 • 可解释性

> 243 244 CHAPTER 10 • INTERPRETABILITY

| hL CLS hL 1 hL 2 hL 3 hL 4 hL 5 hL 6<br>+ i + i + i + i + i + i + i<br>E E E E E E E<br>[CLS] 再见了，感谢所有<br>hL CLS hL 1 hL 2 hL 3 hL 4 hL 5 hL 6<br>+ i + i + i + i + i + i + i<br>E E E E E E E<br>[CLS] So long and thanks for all |  |
| --- | --- |
| 图 10.1<br>Figure 10.1 | BERT 风格模型的输出是上下文嵌入向量 hL，对应<br>i<br>The output of a BERT-style model is a contextual embedding vector hL for<br>i |

hL hL hL hL hL hL hL

> CLS 1 2 3 4 5 6

![](images/img_56.png)

![](images/img_58.png)

![](images/img_58.png)

![](images/img_58.png)

![](images/img_58.png)

![](images/img_58.png)

![](images/img_58.png)

![](images/img_58.png)

> + i + i + i + i + i + i + i

> E E E E E E E

[CLS] 再见了，感谢所有

> [CLS] So long and thanks for all

> 图 10.1 BERT 风格模型的输出是为每个输入 token xi 生成的上下文嵌入向量 hL i。
>
> *Figure 10.1 The output of a BERT-style model is a contextual embedding vector hL i for each input token xi.*

静态嵌入表示词类型（词汇表条目）的含义，而上下文嵌入表示词实例的含义：即某个特定词类型在特定上下文中的实例。因此，word2vec 对每个词类型只有一个向量，而上下文嵌入为该词类型在其句子上下文中的每个实例都提供一个向量。于是上下文嵌入可用于诸如度量上下文中两个词的语义相似度之类的任务，并有助于那些需要词义模型的语言学任务。

> static embeddings represent the meaning of word types (vocabulary entries), contextual embeddings represent the meaning of word instances: instances of a particular word type in a particular context. Thus where word2vec had a single vector for each word type, contextual embeddings provide a single vector for each instance of that word type in its sentential context. Contextual embeddings can thus be used for tasks like measuring the semantic similarity of two words in context, and are useful in linguistic tasks that require models of word meaning.

### 10.1.1 上下文嵌入与词义

> 10.1.1 Contextual Embeddings and Word Sense

词是有歧义的：同一个词可以用来表示不同的事物。在

> Words are ambiguous: the same word can be used to mean different things. In

> 歧义
>
> *ambiguous*

第 5 章中我们看到，单词“mouse”可以表示（1）一种小型啮齿动物，或（2）一种用于控制光标的手持设备。单词“bank”可以表示：（1）一家金融机构，或（2）一个倾斜的土堆。我们说“mouse”或“bank”这类词是多义词（polysemous，源自希腊语“多种意义”，poly- 表示“多”+ sema 表示“符号、标记”）。1

> Chapter 5 we saw that the word “mouse” can mean (1) a small rodent, or (2) a handoperated device to control a cursor. The word “bank” can mean: (1) a financial institution or (2) a sloping mound. We say that the words ‘mouse’ or ‘bank’ are polysemous (from Greek ‘many senses’, poly- ‘many’ + sema, ‘sign, mark’).1

一个义项（sense，或称词义）是对含义某一个方面的离散表示，而该含义属于

> A sense (or word sense) is a discrete representation of one aspect of the meaning

> 词义
>
> *word sense*

一个词。我们可以用上标来表示每个义项：bank1 和 bank2，mouse1 和 mouse2。这些义项可以在 WordNet（Fellbaum, 1998）这类在线同义词词典（thesauruses，或 thesauri）中查到，它拥有多种语言的数据集，

> of a word. We can represent each sense with a superscript: bank1 and bank2, mouse1 and mouse2. These senses can be found listed in online thesauruses (or thesauri) like WordNet (Fellbaum, 1998), which has datasets in many languages

> WordNet

其中列出了许多词的义项。在上下文中，很容易看出不同的含义：mouse1：……1968 年一只控制计算机系统的鼠标。mouse2：……一种像老鼠一样安静的动物 bank1：……银行可以在保管账户中持有投资…… bank2：……随着农业在东岸蓬勃发展，那条河……

> listing the senses of many words. In context, it’s easy to see the different meanings: mouse1 : .... a mouse controlling a computer system in 1968. mouse2 : .... a quiet animal like a mouse bank1 : ...a bank can hold the investments in a custodial account ... bank2 : ...as agriculture burgeons on the east bank, the river ...

上文所体现的上下文能够消解 mouse 和 bank 的义项歧义这一事实，也

> This fact that context disambiguates the senses of mouse and bank above can

可以用几何方式加以可视化。图 10.2 展示了英语和德语中单词 die 的 BERT 嵌入的许多实例的二维投影。

> also be visualized geometrically. Fig. 10.2 shows a two-dimensional projection of many instances of the BERT embeddings of the word die in English and German.

图中的每个点代表 die 在一个输入句子中的用法。我们可以

> Each point in the graph represents the use of die in one input sentence. We can

> 多义性（polysemy）这个词本身就有歧义；你可能会看到它以另一种方式被使用，仅用来指以下情况
>
> *The word polysemy itself is ambiguous; you may see it used in a different way, to refer only to cases*

> 1

> 即一个词的各个义项以某种结构化的方式相关联的情况，而把同形异义（homonymy）一词留作表示义项之间毫无关联的义项歧义（Haber and Poesio, 2020）。在本书中，我们用“多义性”表示任何类型的义项歧义，用“结构化多义性”表示具有义项关联的多义现象。
>
> *where a word’s senses are related in some structured way, reserving the word homonymy to mean sense ambiguities with no relation between the senses (Haber and Poesio, 2020). Here we will use ‘polysemy’to mean any kind of sense ambiguity, and ‘structured polysemy’ for polysemy with sense relations.*

10.1 • 上下文嵌入 245

> 10.1 • CONTEXTUAL EMBEDDINGS 245

在 BERT 嵌入空间中，可以清楚地看到 die 至少有两种不同的英语义项（dice 的单数形式和动词 to die），此外还有德语冠词。

> clearly see at least two different English senses of die (the singular of dice and the verb to die, as well as the German article, in the BERT embedding space.

![](images/img_74.png)

|  |  |
| --- | --- |
| 图 10.2<br>Figure 10.2 | 每个蓝点表示来自不同句子的单词 die 的一个 BERT 上下文嵌入<br>Each blue dot shows a BERT contextual embedding for the word die from different sentences |

> 英语和德语中的用法，使用 UMAP 算法投影到二维空间。德语和英语的含义以及不同的英语义项分别落入不同的簇中。部分样本点连同其来源的上下文句子一并展示。图引自 Coenen et al. (2019)。
>
> *in English and German, projected into two dimensions with the UMAP algorithm. The German and English meanings and the different English senses fall into different clusters. Some sample points are shown with the contextual sentence they came from. Figure from Coenen et al. (2019).*

因此，尽管像 WordNet 这样的同义词词典给出的是离散的义项列表，而嵌入

> Thus while thesauruses like WordNet give discrete lists of senses, embeddings

（无论是静态的还是上下文的）所提供的是一种连续的高维语义模型，它虽然可以被聚类，但并不能划分为完全离散的义项。

> (whether static or contextual) offer a continuous high-dimensional model of meaning that, although it can be clustered, doesn’t divide up into fully discrete senses.

词义消歧

> Word Sense Disambiguation

为某个词选择正确义项的任务称为词义消歧，或称 WSD。WSD 算法以语境中的一个词和一个固定的

> The task of selecting the correct sense for a word is called word sense disambiguation, or WSD. WSD algorithms take as input a word in context and a fixed inventory

> 词义
>
> *word sense*

> 消歧
>
> *disambiguation*

候选词义清单（如 WordNet 中的那些）作为输入，并输出正确的词

> of potential word senses (like the ones in WordNet) and outputs the correct word

> WSD

在语境中的义项。图 10.3 勾勒了该任务。

> sense in context. Fig. 10.3 sketches out the task.

| y y<br>5 6<br>y<br>3<br>stand1: side1:<br>y y<br>1 bass1: 4 竖直 相对<br>低音域 … 区域<br>electric1: … player1: stand5: …<br>使用 bass4: 在游戏中 熊 side3:<br>电 海 鱼 player2: … 身体的<br>electric2: y … 音乐家 stand10: …<br>紧张 2 bass7: player3: 放置 side11:<br>electric3: 乐器 演员 竖直 斜坡<br>令人兴奋的 guitar1 … … … …<br>x x x x x x<br>1 2 3 4 5 6<br>一把电吉他和一名贝斯手站在一旁<br>y y<br>5 6<br>y<br>3<br>stand1: side1:<br>y y<br>1 bass1: 4 upright relative<br>low range … region<br>electric1: … player1: stand5: …<br>using bass4: in game bear side3:<br>electricity sea fish player2: … of body<br>electric2: y … musician stand10: …<br>tense 2 bass7: player3: put side11:<br>electric3: instrument actor upright slope<br>thrilling guitar1 … … … …<br>x x x x x x<br>1 2 3 4 5 6<br>an electric guitar and bass player stand off to one side |  |
| --- | --- |
| 图 10.3<br>Figure 10.3 | 全词 WSD 任务，将输入词（x）映射到 WordNet 义项<br>The all-words WSD task, mapping from input words (x) to WordNet senses |

y5 y6

y3

> stand1: side1:

y1 y4

> bass1: 竖直 相对 低音域 … 区域
>
> *bass1: upright relative low range … region*

| electric1:<br>使用<br>电<br>electric2:<br>紧张<br>electric3:<br>令人兴奋的<br>electric1:<br>using<br>electricity<br>electric2:<br>tense<br>electric3:<br>thrilling |  |
| --- | --- |
|  | guitar1 |

> electric1: … player1: stand5: …使用 bass4: 在游戏中 熊 side3: 电 海 鱼 player2: … 身体的 electric2: … 音乐家 stand10: …
>
> *electric1: … player1: stand5: …using bass4: in game bear side3: electricity sea ﬁsh player2: … of body electric2: … musician stand10: …*

y2

> 紧张 bass7: player3: 放置 side11: electric3: 乐器 演员 竖直 斜坡 令人兴奋的 guitar1 … … … …
>
> *tense bass7: player3: put side11: electric3: instrument actor upright slope thrilling guitar1 … … … …*

x1 x2 x3 x4 x5 x6

> 一把电吉他和一名贝斯手站在一旁
>
> *an electric guitar and bass player stand oﬀ to one side*

> （y）。图受 Chaplot and Salakhutdinov (2018) 启发。
>
> *(y). Figure inspired by Chaplot and Salakhutdinov (2018).*

WSD 可以成为人文学科和社会科学中文本分析的有用分析工具，246 第 10 章 • 可解释性 词义也可以在词表示的模型可解释性中发挥作用。词义还具有有趣的分布性质。例如，一个词在一段语篇中往往大致以相同的义项使用，这一观察

> WSD can be a useful analytic tool for text analysis in the humanities and social 246 CHAPTER 10 • INTERPRETABILITY sciences, and word senses can play a role in model interpretability for word representations. Word senses also have interesting distributional properties. For example a word often is used in roughly the same sense through a discourse, an observation

> 一段语篇一个
>
> *one sense per*

被称为“一段语篇一个义项”规则（one sense per discourse）（Gale et al., 1992a）。

> called the one sense per discourse rule (Gale et al., 1992a).

> 义项
>
> *discourse*

性能最好的 WSD 算法是一个简单的 1-最近邻算法

> The best performing WSD algorithm is a simple 1-nearest-neighbor algorithm

该算法使用上下文词嵌入，由 Melamud et al. (2016) 和 Peters et al.(2018) 提出。训练时，我们把某个带义项标注的数据集（如各种语言的 SemCore 或 SenseEval 数据集）中的每个句子送入任意一种上下文嵌入模型（例如 BERT），从而为每个带标注的 token 得到一个上下文嵌入。（为一个 token i 计算这个上下文嵌入 vi 有多种方式；对于 BERT，常见做法是把 i 在最后四层 BERT 层中的向量表示相加，以池化多层信息）。然后，对于语料库中任意词的每个义项 s，对该义项的 n 个 token 中的每一个，我们把它们的 n 个上下文表示 vi 取平均，得到 s 的上下文义项嵌入 vs：

> using contextual word embeddings, due to Melamud et al. (2016) and Peters et al.(2018). At training time we pass each sentence in some sense-labeled dataset (like the SemCore or SenseEval datasets in various languages) through any contextual embedding (e.g., BERT) resulting in a contextual embedding for each labeled token.(There are various ways to compute this contextual embedding vi for a token i; for BERT it is common to pool multiple layers by summing the vector representations of i from the last four BERT layers). Then for each sense s of any word in the corpus, for each of the n tokens of that sense, we average their n contextual representations vi to produce a contextual sense embedding vs for s:

vs = 1 X

∀vi ∈tokens(s)

> (10.1)

n vi

> i

在测试时，给定上下文中目标词 t 的一个词元，我们计算它的上下文嵌入 t，并从训练集中选择其最近邻义项，即义项嵌入与 t 的余弦值最高的那个义项：

> At test time, given a token of a target word t in context, we compute its contextual embedding t and choose its nearest neighbor sense from the training set, i.e., the sense whose sense embedding has the highest cosine with t:

sense(t) = argmax cosine(t,vs)

> (10.2)

> s∈senses(t)

图 10.4 展示了该模型。

> Fig. 10.4 illustrates the model.

| 5<br>4 find v<br>find<br>v 1<br>find<br>v<br>9<br>find<br>v<br>c c c c c<br>我发现罐子是空的<br>编码器<br>我发现罐子是空的<br>5<br>4 find v<br>find<br>v 1<br>find<br>v<br>9<br>find<br>v<br>c c c c c<br>I found the jar empty<br>ENCODER<br>I found the jar empty |  |
| --- | --- |
| 图 10.4<br>Figure 10.4 | WSD 的最近邻算法。绿色部分为上下文嵌<br>The nearest-neighbor algorithm for WSD. In green are the contextual embed- |

> find5

> find4 v

> v find1

> v

> find9

> v

> cI cfound cthe cjar cempty

### 编码器

> ENCODER

> 我发现罐子是空的
>
> *I found the jar empty*

> ……嵌入为每个词的每个义项预先计算好；这里我们只展示 find 的少数几个义项。为目标词 found 计算上下文嵌入，然后选出最近邻义项（此处为 find9v）。图受 Loureiro 和 Jorge（2019）启发。
>
> *dings precomputed for each sense of each word; here we just show a few of the senses for find. A contextual embedding is computed for the target word found, and then the nearest neighbor sense (in this case find9v) is chosen. Figure inspired by Loureiro and Jorge (2019).*

### 10.1.2 上下文嵌入与词语相似度

> 10.1.2 Contextual Embeddings and Word Similarity

在第 5 章中我们提出了这样的想法：我们可以通过考察两个词在几何上有多接近来衡量它们的相似度，即以余弦作为相似度函数。语义相似这一想法在图 10.2 的语义聚类中同样在几何上清晰可见；一个词在某个上下文中具有特定义项时的表示，与该词同一义项的其他实例更为接近。因此，我们常常通过两个词的上下文嵌入之间的余弦，来衡量上下文中两个词的两个实例（或同一词在两个不同上下文中的两个 10.2 • 探测 247 实例）之间的相似度。

> In Chapter 5 we introduced the idea that we could measure the similarity of two words by considering how close they are geometrically, by using the cosine as a similarity function. The idea of meaning similarity is also clear geometrically in the meaning clusters in Fig. 10.2; the representation of a word which has a particular sense in a context is closer to other instances of the same sense of the word. Thus we often measure the similarity between two instances of two words in context (or two 10.2 • PROBING 247 instances of the same word in two different contexts) by using the cosine between their contextual embeddings.

通常，在计算之前需要对嵌入做一些变换

> Usually some transformations to the embeddings are required before computing

余弦。这是因为上下文嵌入（无论来自掩码语言模型还是自回归模型）都具有这样的性质：所有词的向量都极为相似。如果我们查看 BERT 或其他模型最后一层的嵌入，任意两个随机选取的词实例的嵌入都会具有极高的余弦值，甚至可能相当接近 1，这意味着所有词向量都倾向于指向同一个方向。系统中向量都倾向于指向同一方向的性质被称为各向异性。Ethayarajh（2019）将模型的各向异性定义为在

> cosine. This is because contextual embeddings (whether from masked language models or from autoregressive ones) have the property that the vectors for all words are extremely similar. If we look at the embeddings from the final layer of BERT or other models, embeddings for instances of any two randomly chosen words will have extremely high cosines that can be quite close to 1, meaning all word vectors tend to point in the same direction. The property of vectors in a system all tending to point in the same direction is known as anisotropy. Ethayarajh (2019) defines the anisotropy of a model as the expected cosine similarity of any pair of words in

> 各向异性
>
> *anisotropy*

语料库中任意一对词的期望余弦相似度。“isotropy”（各向同性）一词意为在所有方向上均匀，因此在各向同性的模型中，向量集合应当指向所有方向，一对随机嵌入之间的期望余弦值应当为零。Timkey 和 van Schijndel（2021）表明，各向异性的一个成因是余弦度量被上下文嵌入中少数几个维度所主导，这些维度的取值与其他维度非常不同：这些异常维度的量级非常大，方差也非常高。

> a corpus. The word ‘isotropy’ means uniformity in all directions, so in an isotropic model, the collection of vectors should point in all directions and the expected cosine between a pair of random embeddings would be zero. Timkey and van Schijndel(2021) show that one cause of anisotropy is that cosine measures are dominated by a small number of dimensions of the contextual embedding whose values are very different than the others: these rogue dimensions have very large magnitudes and very high variance.

Timkey 和 van Schijndel（2021）表明，我们可以使嵌入更具

> Timkey and van Schijndel (2021) shows that we can make the embeddings more

各向同性，方法是对向量进行标准化（z 分数化），即减去均值并除以方差。给定某个语料库中所有嵌入的集合 C，每个嵌入的维度为 d（即 x ∈Rd），则均值向量 µ ∈Rd 为：

> isotropic by standardizing (z-scoring) the vectors, i.e., subtracting the mean and dividing by the variance. Given a set C of all the embeddings in some corpus, each with dimensionality d (i.e., x ∈Rd), the mean vector µ ∈Rd is:

µ = 1 X

> (10.3)

|C| x

> x∈C

每个维度上的标准差 σ ∈Rd 为：

> The standard deviation in each dimension σ ∈Rd is:

s

1 X

(x−µ)2

> (10.4)

σ = |C|

> x∈C

然后每个词向量 x 被替换为标准化后的版本 z：

> Then each word vector x is replaced by a standardized version z:

z = x−µ

> (10.5)

σ

标准化无法解决的一个余弦问题是，余弦倾向于

> One problem with cosine that is not solved by standardization is that cosine tends

从而低估人类对高频词词义相似度的判断（Zhou 等，2022）。

> to underestimate human judgments on similarity of word meaning for very frequent words (Zhou et al., 2022).

## 10.2 探测

> 10.2 Probing

我们常常想知道网络中的某个特定表示是否编码了某些特定信息。例如，我们可能想知道网络如何处理关于语法或意义的语言学信息，比如在某一层中，网络对单词 ketchup 的表示是否编码了它是名词而非动词这一事实。又或者，单词 sublet（既可以是过去时也可以是现在时）的表示是否编码了特定句子中的时态，如果是的话，这又发生在网络的哪一层。

> Often we have want to know whether a particular representation in the network encodes some particular information. For example we might want to know how the network processing linguistic information about grammar or meaning, such as whether at a certain layer the network’s representation of the word ketchup encodes the fact that it is a noun and not a verb. Or whether the representation of the word sublet (which can be past or present tense) encodes the tense in a particular sentence, and if so at what layer of the network this happens.

最简单的技术称为探测（probing）。在探测中，我们构建一个分

> The simplest technique for this is called probing. In probing, we build a clas-

> 探测
>
> *probing*

248 第 10 章 • 可解释性

> 248 CHAPTER 10 • INTERPRETABILITY

类器，它可以是逻辑回归或线性回归，也可以是一个小型 MLP，它以嵌入向量作为输入，返回我们感兴趣的类别（比如「名词」或「动词」）。

> sifier, which can be logistic or linear regression or a small MLP which takes an embedding vector as input and returns the class of interest (say ‘noun’, or ‘verb’).

如果探测器给出该词是名词的高概率（与某些对照条件相比），那么我们就说该表示很可能编码了名词这一概念。图 10.5 展示了这一直觉，其中有 3 个潜在的探测器在考察 BERT 表示内部的两个不同嵌入向量。

> If the probe has a high probability, say, that the word is a noun, (as compared with some control conditions), then we say that the representation probably encodes the concept of noun. Fig. 10.5 shows the intuition, showing 3 potential probes looking at two different embedding vectors inside a BERT representation.

探测已被用于研究信息从较低层向

> Probing has been used to study the way information propagates up from lower to

变换器（transformer）中较高层传播的方式，例如表明关于词元的语法信息似乎在较低层编码，语义信息在中间层编码，而像共指这样的篇章信息则在更高层编码（Tenney 等，2019）。

> higher layers in the transformer, showing for example that grammatical information about tokens seems to be encoded at lower layers, semantic information at middle layers, and discourse information like coreference still higher (Tenney et al., 2019).

| Did t h inis S t pa ak ie n ?place hL CLS hL 1 hL 2 hL 3 hL 4 hL 5 hL 6<br>这是动词吗？<br>block 6<br>block 5 时态是<br>block 4 过去时吗？<br>h3 block 3<br>CLS h1<br>block 2 2<br>h1<br>block 1 2<br>[CLS] 他们去年在 Chamartín 转租了房子<br>Did t h inis S t pa ak ie n ?place hL CLS hL 1 hL 2 hL 3 hL 4 hL 5 hL 6<br>Is this a verb?<br>block 6<br>block 5 Is the tense<br>block 4 past?<br>h3 block 3<br>CLS h1<br>block 2 2<br>h1<br>block 1 2<br>[CLS] They sublet in Chamartín last year |  |
| --- | --- |
| 图 10<br>Figure 10 | .5 在探测中，我们探究模型中某个表示所编码的信息，通过<br>.5 In probing, we explore what information is encoded in some representation in the model by |

> 这件事是否发生
>
> *Did this take place*

> hL hL hL hL hL hL hL

> CLS 1 2 3 4 5 6

> 在西班牙？
>
> *in Spain?*

![](images/img_186.png)

> 这是动词吗？
>
> *Is this a verb?*

> block 6

![](images/img_192.png)

![](images/img_192.png)

> block 5

> 时态是过去时吗？
>
> *Is the tense past?*

> block 4

> block 3

> h3

![](images/img_192.png)

> CLS

> h1

> block 2 2

> h1

> block 1 2

> [CLS] 他们去年在 Chamartín 转租了房子
>
> *[CLS] They sublet in Chamartín last year*

> 图 10.5 在探测中，我们通过训练简单的分类器来提取词元（如是否为动词、是否为过去时）或句子（如是否发生在西班牙）的语言学属性或其他属性，从而探究模型中某个表示编码了哪些信息。这里我们看到 3 个不同的探测器在考察 2 个表示，即 h3 CLS 和 h1 2。
>
> *Figure 10.5 In probing, we explore what information is encoded in some representation in the model by training simple classifiers to extract linguistic or other properties of tokens (like being a verb or being in the past tense) or sentences (like taking place in Spain). Here we see 3 different probes examining 2 representations, h3 CLS and h1 2.*

探测分为两个阶段：训练和测试。训练一个探测器有 4 个步骤：

> Probing has two phases, training and testing. Training a probe has 4 steps:

- 选择我们想要考察的属性（比如词性、意义的某个方面，或者某个代词与哪个实体共指）
- 在我们感兴趣研究的位置和层级上创建嵌入的训练集和测试集（比如「变换器第 2 层到第 16 层前馈网络的输出」），并用正确答案（相关的词性、时态或其他属性）加以标注。
- 把训练集的句子输入 LLM，并提取激活值
- 然后冻结 LLM 的权重，只训练分类器的权重，使它把嵌入映射到某个属性。

> Choose a property we want to examine (like part of speech, or some aspect of meaning, or which entity a pronoun corefers with)
> Create a training and test set of embeddings at some position and level we are interested in studying (like “the output of the feedforward network at transformer layers 2 through 16”), labeled with the correct answer (the relevant part of speech, or tense, or whatever).
> Pass the training set sentences through the LLM, and extract activations
> Now freeze the weights of the LLM, and train only the weights of the classifier to map from an embedding to a property.

在推理时，我们把测试集文本输入模型，提取激活值，将它们送入分类器，并报告模型是否能够正确地提取该属性。

> At inference times we pass a test set text through the model, extract activations, and pass them through the classifier, and report on whether the model is able to correctly extract the property.

探测通常需要与对照条件进行比较，例如确保

> Probing generally requires comparing to control conditions, like making sure

其表现优于使用随机标签的探测（Belinkov 等，2017）。

> that performance is better than probing with random labels (Belinkov et al., 2017).

而且探测器不能过于强大，这一点很重要，以免它之所以成功是因为相关信息编码在探测器的权重本身，而不是编码在表示之中（Hewitt and Liang，2019）。

> And it’s important that the probe not be too powerful, to keep it from succeeding because the relevant information is encoded in the probe weights themselves rather than in the representation (Hewitt and Liang, 2019).

虽然探测成功表明信息编码在某个表示之中，

> While success at probing shows that information is encoded in a representation,

但这并不能证明模型使用了该信息。也就是说，被探测的信息可能与嵌入中的内容相关，但对模型的行为没有因果影响（Belinkov，2022）。

> it doesn’t prove that the model uses the information. That is, the information being probed could be correlated with what’s in the embedding, but not have a causal effect on the model’s behavior (Belinkov, 2022).

10.3 • LOGIT 透镜 249

> 10.3 • THE LOGIT LENS 249

## 10.3 logit 透镜

> 10.3 The Logit Lens

另一个有用的可解释性工具是 logit 透镜（Nostalgebraist，2020），它提供了

> Another useful interpretability tool, the logit lens (Nostalgebraist, 2020), offers a

> logit 透镜（logit lens）
>
> *logit lens*

一种可视化 transformer 内部各层可能表示什么的方法。

> way to visualize what the internal layers of the transformer might be representing.

其思路是：我们从 transformer 的任意一层取出任意一个向量，假装它就是最终嵌入（prefinal embedding），直接将它乘以反嵌入层（unembedding layer）得到 logits，再计算 softmax，以查看该向量可能表示的词分布。这可以成为观察模型内部表示的一扇有用窗口。由于网络在训练时并未让内部表示以这种方式发挥作用，logit 透镜并不总是完美奏效，但它仍然可以是一个有用的技巧，帮助我们可视化 transformer 的内部各层。

> The idea is that we take any vector from any layer of the transformer and, pretending that it is the prefinal embedding, simply multiply it by the unembedding layer to get logits, and compute a softmax to see the distribution over words that that vector might be representing. This can be a useful window into the internal representations of the model. Since the network wasn’t trained to make the internal representations function in this way, the logit lens doesn’t always work perfectly, but this can still be a useful trick to help us visualize the internal layers of a transformer.

雅可比透镜（Jacobian lens）或 J-lens（Gurnee et al., 2026）是 logit 透镜的一种变体，它

> The Jacobian lens or J-lens (Gurnee et al., 2026) is a variant of the logit lens that

> J-lens

似乎在揭示模型在较早层编码了什么方面表现更好。

> seems to perform better at uncovering what the model is encoding at earlier layers.

logit 透镜以相同的方式解释所有层，即把某一层的嵌入乘以同一个反编码矩阵。因此，它隐含地假设较早层的表示与最后一层处于同一个嵌入空间。而 J-lens 则考察最后一层相对于中间层的导数，追问层的微小变化会如何影响最后一层的输出表示。因此，它实际上是把较早层的嵌入通过对其余网络的一个近似来传递，并且还在许多上下文中取平均。

> The logit lens interprets all layers the same way, by multiplying an embedding at that layer by the same unencoding matrix. It thus implicitly makes the assumption that representations at earlier layers are in the same embedding space as the final layer. The J-lens instead looks at the derivatives of the final layer with respect to the intermediate layers, asking how a small change in layers would affect the final layer output representation. It thus effectively is passing embeddings at earlier layers through an approximation of the rest of the network, and also averages over many contexts.

logit 透镜把 transformer 的中间层当作它们已经

> The logit lens treats the intermediate layers of a transformer as if they already

在说最终输出的“语言”。雅可比透镜则充当翻译器，映射早期层中的微小推动如何实际改变最终输出的 token

> speak the ”language” of the final output. The Jacobian lens acts as a translator, mapping how a small push in an early layer physically alters the final output tokens

。

> .

| 这颗行星的颜色 “⼩” 的反义词是“<br>距太阳第四近的是<br>= “small” 的反义词是“<br>L100 red red L100 = big<br>L92 red rust L92<br>L83 red red L83 big больш = big<br>L75 red red L75 big large<br>L67 color Mars L67 bigger oppos<br>L58 Mars Mars L58 opposite opposite<br>L50 color general L50 Chinese anie<br>L42 color valea L42 " interc<br>The color of the planet “⼩” 的反义词是“<br>fourth from the sun is<br>= The opposite of “small” is “<br>L100 red red L100 = big<br>L92 red rust L92<br>L83 red red L83 big больш = big<br>L75 red red L75 big large<br>L67 color Mars L67 bigger oppos<br>L58 Mars Mars L58 opposite opposite<br>L50 color general L50 Chinese anie<br>L42 color valea L42 " interc |  |
| --- | --- |
| 图 10.6<br>Figure 10.6 | 模型在不同层对 2 个不同前缀给出的最可能的词。<br>The most likely words at different layers of the model for 2 different prefixes. |

| 这颗行星的颜色 “⼩” 的反义词是“<br>距太阳第四近的是<br>= “small” 的反义词是“<br>L100 red red L100 = big<br>L92 red rust L92<br>L83 red red L83 big больш = big<br>L75 red red L75 big large<br>L67 color Mars L67 bigger oppos<br>L58 Mars Mars L58 opposite opposite<br>L50 color general L50 Chinese anie<br>L42 color valea L42 " interc<br>The color of the planet “⼩” 的反义词是“<br>fourth from the sun is<br>= The opposite of “small” is “<br>L100 red red L100 = big<br>L92 red rust L92<br>L83 red red L83 big больш = big<br>L75 red red L75 big large<br>L67 color Mars L67 bigger oppos<br>L58 Mars Mars L58 opposite opposite<br>L50 color general L50 Chinese anie<br>L42 color valea L42 " interc |  |  |
| --- | --- | --- |
| L100<br>L92<br>L83<br>L75<br>L67<br>L58<br>L50<br>L42 | red | red |
|  | red | rust |
|  | red | red |
|  | red | red |
|  | color | Mars |
|  | Mars | Mars |
|  | color | general |
|  | color | valea |

> 这颗行星的颜色
>
> *The color of the planet*

“⼩” 的反义词是“

> 距太阳第四近的是
>
> *fourth from the sun is*

> = “small” 的反义词是“
>
> *= The opposite of “small” is “*

> L100 red red L100 = big L92 red rust L92 L83 red red L83 big больш = big L75 red red L75 big large L67 color Mars L67 bigger oppos L58 Mars Mars L58 opposite opposite L50 color general L50 Chinese anie L42 color valea L42 " interc

|  |  |
| --- | --- |
| big | больш = |
| big | large |
| bigger | oppos |
| opposite | opposite |
| Chinese | anie |
| " | interc |

> 左侧示例展示了模型进行多跳推理（multihop reasoning）的能力，这在 J-lens 中尤为成功：模型首先编码颜色的概念，随后较高的层似乎把“第四颗行星”这一指代解析为火星（Mars），直到更晚才开始编码红色。
>
> *The left example shows the ability of the model to do multihop reasoning, particularly successful in the J-lens, where the model first encodes the idea of color, then higher layers seem to resolve the “fourth planet” reference to refer to Mars, and only later starting encoding red.*

> 在右侧示例中，logit 透镜和 J-lens 似乎都编码了反义词的概念，而只在较高的层才表示出正确的反义词 large——先是英语，接着是俄语，最后是正确的汉语。图片来自（Gurnee et al., 2026）的图 51。
>
> *The right model both the logit lens and the J-lens seem to encode the concept of opposites, and only at higher layers represent the correct opposite large first in English, then in Russian, and finally in the correct Chinese. Image from Figure 51 of (Gurnee et al., 2026).*

J-lens 揭示出似乎是一种工作空间，模型在其中

> The J-lens uncovers what seems to be a kind of workspace where the model

逐层地对问题展开推理。图 10.6 以 Anthropic Claude Sonnet 4.5 模型的不同层为例，直观展示了 J-lens 与 logit 透镜的这一过程。

> reasons through problems, layer by layer. Fig. 10.6 shows an intuition of this for the J-lens and logit lens at different layers of the Anthropic Claude Sonnet 4.5 model.

左侧示例展示了模型如何利用各层逐步推理一个关于颜色的 250 第 10 章 • 可解释性 多步推理问题，该问题要求模型首先识别出第四颗行星。右侧示例则表明，模型似乎主要以英语表示这些含义，只在较晚的层才将它们翻译成相关语言用于输出

> The left example shows the model using layers to reason successively through a 250 CHAPTER 10 • INTERPRETABILITY multi-step reasoning question about color that requires the model to first identify the fourth planet. And the right example shows that the model seems to represent these meanings mostly in English, and then translate them into relevant languages for output only in later layers

## 10.4 稀疏自编码器

> 10.4 Sparse Auto-Encoders

## 10.5 因果可解释性技术

> 10.5 Causal Interpretability Techniques

## 10.6 上下文学习与归纳头

> 10.6 In-Context Learning and Induction Heads

作为一种让模型做我们想让它做的事的方式，我们可以认为提示（prompting）与预训练有着根本性的不同。通过预训练进行学习意味着依据某个损失函数，使用梯度下降来更新模型的参数。

> As a way of getting a model to do what we want, we can think of prompting as being fundamentally different than pretraining. Learning via pretraining means updating the model’s parameters by using gradient descent according to some loss function.

但用示例（demonstrations）进行提示可以教会模型完成一项新任务。模型在处理提示的过程中，会从这些示例中学到关于该任务的某些东西。

> But prompting with demonstrations can teach a model to do a new task. The model is learning something about the task from those demonstrations as it processes the prompt.

即使没有示例，我们也可以把提示的过程看作一种

> Even without demonstrations, we can think of the process of prompting as a kind

学习。例如，模型在提示中读得越靠后，它往往就越擅长预测接下来的 token。上下文中的信息帮助模型获得更强的预测能力。

> of learning. For example, the further a model gets in a prompt, the better it tends to get at predicting the upcoming tokens. The information in the context is helping give the model more predictive power.

> 上下文
>
> *in-context*

“上下文学习”（in-context learning）这一术语最早由 Brown et al.（2020）在

> The term in-context learning was first proposed by Brown et al. (2020) in their

> 学习
>
> *learning*

介绍 GPT3 系统时提出，用来指语言模型从提示中进行的上述任一种学习。上下文学习是指语言模型在推理时的前向传播过程中学会完成新任务、更好地预测 token，或者总体上降低其损失，而无需对模型参数做任何基于梯度的更新。

> introduction of the GPT3 system, to refer to either of these kinds of learning that language models do from their prompts. In-context learning means language models learning to do new tasks, better predict tokens, or generally reduce their loss during the forward-pass at inference-time, without any gradient-based updates to the model’s parameters.

上下文学习是如何运作的？虽然我们并不完全确定，但存在一些

> How does in-context learning work? While we don’t know for sure, there are

引人入胜的设想。其中一种假说基于归纳头（induction heads）的想法

> some intriguing ideas. One hypothesis is based on the idea of induction heads

> 归纳头
>
> *induction heads*

（Elhage et al., 2021；Olsson et al., 2022）。归纳头是一个电路（circuit）的名称，而电路是网络中一种抽象的组成部分。归纳头电路是 transformer 中注意力计算的一部分，是通过观察只有 1-2 个注意力头的小型语言模型发现的。

> (Elhage et al., 2021; Olsson et al., 2022). Induction heads are the name for a circuit, which is a kind of abstract component of a network. The induction head circuit is part of the attention computation in transformers, discovered by looking at mini language models with only 1-2 attention heads.

归纳头的功能是预测重复出现的序列。例如

> The function of the induction head is to predict repeated sequences. For example

如果它在输入序列中看到模式 AB...A，它就会预测接下来是 B，从而实例化模式补全规则 AB...A→B。它实现这一点的方式是：注意力计算中有一个前缀匹配组件，当看到当前 token A 时，它会回溯上下文以寻找先前出现过的 A。如果找到了，归纳头便有一个复制机制，通过提高 B 接下来出现的概率，来“复制”先前那个 A 之后的 token B。图 10.7 展示了一个示例。

> if it sees the pattern AB...A in an input sequence, it predicts that B will follow, instantiating the pattern completion rule AB...A→B. It does this by having a prefix matching component of the attention computation that, when looking at the current token A, searches back over the context to find a prior instance of A. If it finds one, the induction head has a copying mechanism that “copies” the token B that followed the earlier A, by increasing the probability the B will occur next. Fig. 10.7 shows an example.

Olsson 等人（2022）提出，这条模式补全规则的广义模糊版本——即实现形如 A*B*...A→B 的规则，其中 A* ≈A 且 B* ≈B（这里的 ≈ 指二者在某种意义上语义相似）——或许正是上下文学习（in-context learning）的成因。支持其假设的提示性证据来自 Cros- 10.6 • 上下文学习与归纳头 251

> Olsson et al. (2022) propose that a generalized fuzzy version of this pattern completion rule, implementing a rule like A*B*...A→B, where A* ≈A and B* ≈B(by ≈we mean they are semantically similar in some way), might be responsible for in-context learning. Suggestive evidence for their hypothesis comes from Cros- 10.6 • IN-CONTEXT LEARNING AND INDUCTION HEADS 251

![](images/img_294.png)

> 图 10.7 一个关注 vintage 的归纳头使用前缀匹配机制找到先前出现过的一个 vintage 实例，并使用复制机制预测 cars 会再次出现。图取自 Crosbie 和 Shutova（2022）。
>
> *Figure 10.7 An induction head looking at vintage uses the prefix matching mechanism to find a prior instance of vintage, and the copying mechanism to predict that cars will occur again. Figure from Crosbie and Shutova (2022).*

bie 和 Shutova（2022），他们表明消融归纳头会导致上下文

> bie and Shutova (2022), who show that ablating induction heads causes in-context

> 消融
>
> *ablating*

学习性能下降。消融（ablation）原本是一个医学术语，意为移除某物。我们在 NLP 可解释性研究中把它用作检验因果效应的工具；如果我们敲除一个假设的原因，就应当期望该效应随之消失。Crosbie 和 Shutova（2022）对归纳头进行消融的做法是：先找出在随机输入序列上表现为归纳头的注意力头，然后通过把输出矩阵 WO 的某些项置零来将这些头的输出清零。他们确实发现，被消融的模型在上下文学习上差得多：它们从提示中的示例进行学习时表现差得多。

> learning performance to decrease. Ablation is originally a medical term meaning the removal of something. We use it in NLP interpretability studies as a tool for testing causal effects; if we knock out a hypothesized cause, we would expect the effect to disappear. Crosbie and Shutova (2022) ablate induction heads by first finding attention heads that perform as induction heads on random input sequences, and then zeroing out the output of these heads by setting certain terms of the output matrix WO to zero. Indeed they find that ablated models are much worse at in-context learning: they have much worse performance at learning from demonstrations in the prompts.
