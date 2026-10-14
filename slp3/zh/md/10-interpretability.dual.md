# 第 10 章 可解释性

### 章

> CHAPTER

# 10 可解释性

> 10 Interpretability

“我们所看到的一切，都是由我们看不到之物投下的影子。”

> “Everything that we see is a shadow cast by that which we do not see”

> 马丁·路德·金，《在底特律教会理事会上的布道》，1961 年
>
> *Martin Luther King, Jr., Sermon at the Detroit Council of Churches, 1961*

在本章（目前尚为草稿）中，我们转向大语言模型可解释性，它有时

> In this (currently stub) chapter we turn to LLM interpretability, sometimes

> `interpretability`（可解释性）
>
> 释义：研究模型内部表示、推理路径与具体计算回路，以弄清语言模型如何完成其任务的领域。

被称为机制可解释性。在这里，研究者寻找各种方法，以帮助我们理解语言模型是如何完成它们所做之事的。大部分工作聚焦于揭示模型的内部表示——它们似乎编码了何种含义，以及模型的推理路径，即我们能否描述出具体的“回路”。

> called mechanistic interpretability. Here researchers search for methods that will help us understand how language models do what they do. Much of the work focuses on uncovering the model’s internal representations what kind of meanings they seem to encode, as well as the models paths for reasoning, whether we can describe specific “circuits”.

## 10.1 上下文嵌入

> 10.1 Contextual Embeddings

让我们从扩展第 5 章引入的嵌入这一基本思想入手，来看看在 Transformer 及其他大语言模型架构中与之对应的思想。第 5 章的方法（如 word2vec 或 GloVe）为词表中每个独一无二的词 w 学得单个向量嵌入。相比之下，借助上下文嵌入，每个词 w 每次出现在不同上下文中时都由不同的向量来表示。上下文嵌入在第 7 章的因果语言模型和第 9 章的编码器模型中都有使用，不过掩码语言模型所生成的嵌入似乎作为表示格外有效，因此我们将在示例中使用这类嵌入。

> Let’s begin by extending the fundamental idea of embeddings that we introduce in Chapter 5 to see the corresponding idea in transformers and other LLM architectures. The methods of Chapter 5 like word2vec or GloVe learned a single vector embedding for each unique word w in the vocabulary. By contrast, with contextual embeddings, each word w will be represented by a different vector each time it appears in a different context. Contextual embeddings are used in both the causal language models of Chapter 7 and in the encoder models of Chapter 9, although the embeddings created by masked language models seem to function particularly well as representations, so we will use those in examples.

当一段文本被送入预训练语言模型时，模型每个组件（注意力头、前馈网络）的输出都是一种表示，会被加进残差流中。这些表示中的每一个都出现在

> When a text is fed to a pretrained language model, the output of each component of the model (the attention heads, the feedforward network) is a representation that gets added into the residual stream. Each of these representations, which occur

> `contextual`（上下文的）
>
> 释义：指表示或含义依赖于词元所处的具体语境，而非固定不变。

每一层、每个词元上，都被称为上下文嵌入。正如我们所提到的，思考上下文嵌入的一种方式，是把它看作编码了词元在语境中某一含义侧面的向量，好比第 5 章静态嵌入的语境化版本。因此，我们可以把这些嵌入用于涉及词元或词的含义的任务。

> at every level and for every token, are called contextual embeddings. As we suggested, one way to think of contextual embeddings is as vectors that encode some aspect of the meaning of a token in context, like a contextualized version of the static embeddings of Chapter 5. As such, we can use these embeddings for tasks involving the meaning of tokens or words.

> `embeddings`（嵌入）
>
> 释义：把词或其他对象映射为稠密向量的表示形式，使语义关系可以被计算。

例如，给定一个输入词元序列 x1,...,xn，我们可以使用输出

> For example, given a sequence of input tokens x1,...,xn, we can use the output
向量 hLi（来自模型最后一层 L）作为词元 xi 在句子 x1,...,xn 语境中含义的表示，如图 10.1 所示。

> vector hLi from the final layer L of a model aes a representation of the meaning of token xi in the context of sentence x1,...,xn, as shown in Fig. 10.1.

对于 BERT 模型，与其只使用来自模型最后一层的向量 hLi，

> For BERT models, instead of just using the vector hLi from the final layer of
更常见的做法是对模型最后四层各自的输出词元 hi（即 hLi、hL−1i、hL−2i 和 hL−3i）做平均池化或最大池化，从而为 xi 计算出一个表示。

> the model, it’s common to compute a representation for xi by mean pooling or max pooling the output tokens hi from each of the last four layers of the model, i.e., hLi, hL−1i, hL−2i, and hL−3i.

正如我们在第 5 章使用 word2vec 这类静态嵌入来表示

> Just as we used static embeddings like word2vec in Chapter 5 to represent the
词的含义那样，对于任何可能需要词义模型的任务，我们都可以用上下文嵌入作为词在语境中含义的表示。而

> meaning of words, we can use contextual embeddings as representations of word meanings in context for any task that might require a model of word meaning. Where
243

![](images/10-interpretability/fig_p2_0.png)

*图 10.1 BERT 风格模型的输出是为每个输入词元 xi 给出的上下文嵌入向量 hL i。*
*Figure 10.1 The output of a BERT-style model is a contextual embedding vector hL i for each input token xi.*

静态嵌入表示的是词型（词表条目）的含义，而上下文嵌入表示的是词例的含义：某个特定词型在特定上下文中的实例。因此，word2vec 为每个词型只有一个向量，而上下文嵌入则为该词型在其句子语境中的每个实例各提供一个向量。于是，上下文嵌入可用于衡量两个词在语境中语义相似度之类的任务，并且在需要词义模型的语言学任务中很有用。

> static embeddings represent the meaning of word types (vocabulary entries), contextual embeddings represent the meaning of word instances: instances of a particular word type in a particular context. Thus where word2vec had a single vector for each word type, contextual embeddings provide a single vector for each instance of that word type in its sentential context. Contextual embeddings can thus be used for tasks like measuring the semantic similarity of two words in context, and are useful in linguistic tasks that require models of word meaning.

### 10.1.1 上下文嵌入与词义

> 10.1.1 Contextual Embeddings and Word Sense

词是有歧义的：同一个词可以用来表示不同的事物。在

> Words are ambiguous: the same word can be used to mean different things. In

> `ambiguous`（有歧义的）
>
> 释义：指同一形式可以承载多种不同含义，需依据语境才能确定其具体所指。

第 5 章我们看到，“mouse”一词可以指（1）一种小型啮齿动物，或（2）一种用于控制光标的手持设备。“bank”一词可以指：（1）一家金融机构，或（2）一个斜坡状土丘。我们说“mouse”或“bank”这些词是多义的（源自希腊语“许多义项”，poly-“多”+ sema“符号、标记”）。1

> Chapter 5 we saw that the word “mouse” can mean (1) a small rodent, or (2) a handoperated device to control a cursor. The word “bank” can mean: (1) a financial institution or (2) a sloping mound. We say that the words ‘mouse’ or ‘bank’ are polysemous (from Greek ‘many senses’, poly- ‘many’ + sema, ‘sign, mark’).1
一个义项（或称词义）是对词义某一方面的离散表示，

> A sense (or word sense) is a discrete representation of one aspect of the meaning

> `word sense`（词义）
>
> 释义：一个词所承载的某一具体含义，与同一形式的其他含义相区分并列。

是对一个词含义某一方面的表示。我们可以用上标来表示每个义项：bank1 和 bank2，mouse1 和 mouse2。这些义项可以在 WordNet（Fellbaum, 1998）之类的在线同义词典中查到，WordNet 拥有多种语言的数据集，

> of a word. We can represent each sense with a superscript: bank1 and bank2, mouse1 and mouse2. These senses can be found listed in online thesauruses (or thesauri) like WordNet (Fellbaum, 1998), which has datasets in many languages

> `WordNet`
>
> 释义：按义项组织、覆盖多种语言的在线词汇数据库，广泛用于与词义相关的任务。

其中列出了许多词的义项。在语境中，很容易看出不同的含义：mouse1：…… 1968 年一台控制计算机系统的鼠标。mouse2：…… 一只像老鼠一样安静的动物。bank1：……一家银行可以在托管账户中持有这些投资…… bank2：……随着农业在东岸蓬勃发展，这条河……

> listing the senses of many words. In context, it’s easy to see the different meanings: mouse1 : .... a mouse controlling a computer system in 1968. mouse2 : .... a quiet animal like a mouse bank1 : ...a bank can hold the investments in a custodial account ... bank2 : ...as agriculture burgeons on the east bank, the river ...

上文语境能够消解 mouse 和 bank 的义项这一事实，

> This fact that context disambiguates the senses of mouse and bank above can
也可以通过几何方式可视化。图 10.2 展示了英文和德文中 die 一词的许多 BERT 嵌入实例的二维投影。

> also be visualized geometrically. Fig. 10.2 shows a two-dimensional projection of many instances of the BERT embeddings of the word die in English and German.

图中的每个点都表示 die 在某一个输入句子中的使用。我们

> E_1ach point in the graph represents the use of die in one input sentence. We can
清楚地看到 die 在 BERT 嵌入空间中至少有三种不同的用法（英文中 dice 的单数形式和动词“to die”，以及德语的冠词）。

> clearly see at least two different English senses of die (the singular of dice and the verb to die, as well as the German article, in the BERT embedding space.

> 多义性这个词本身就有歧义；你可能会看到它以另一种方式被使用，即只指那些
>
> *The word polysemy itself is ambiguous; you may see it used in a different way, to refer only to cases*

> 义项之间毫无关联的歧义（Haber and Poesio, 2020）。这里我们将用“多义性”
>
> *ambiguities with no relation between the senses (Haber and Poesio, 2020). Here we will use ‘polysemy’*

![](images/10-interpretability/fig_p3_0.png)

*图 10.2 每个蓝点表示 die 一词在英文和德文不同句子中的一个 BERT 上下文嵌入，它们用 UMAP 算法投影到二维空间。德语和英语的含义以及英语的不同义项落入不同的簇中。部分样本点标注了它们所在的语境句子。图出自 Coenen 等（2019）。*
*Figure 10.2 Each blue dot shows a BERT contextual embedding for the word die from different sentences in English and German, projected into two dimensions with the UMAP algorithm. The German and English meanings and the different English senses fall into different clusters. Some sample points are shown with the contextual sentence they came from. Figure from Coenen et al. (2019).*

因此，尽管 WordNet 这类同义词典给出的是离散的义项列表，嵌入

> Thus while thesauruses like WordNet give discrete lists of senses, embeddings
（无论是静态的还是上下文的）提供的则是一种连续的高维含义模型，它虽然可以被聚类，却不会划分成完全离散的义项。

> (whether static or contextual) offer a continuous high-dimensional model of meaning that, although it can be clustered, doesn’t divide up into fully discrete senses.

词义消歧

> Word Sense Disambiguation
为一个词选择正确义项的任务称为词义消歧，即 WSD。WSD 算法以语境中的一个词和一份固定的清单作为输入

> The task of selecting the correct sense for a word is called word sense disambiguation, or WSD. WSD algorithms take as input a word in context and a fixed inventory

> `word sense disambiguation WSD`（词义消歧（WSD））
>
> 释义：指依据语境从固定的义项清单中为词选定正确义项的任务，常借助上下文嵌入实现。

即潜在词义（如 WordNet 中的那些义项）的清单，并输出语境中正确的词

> of potential word senses (like the ones in WordNet) and outputs the correct word
义项。图 10.3 勾勒了这一任务。

> sense in context. Fig. 10.3 sketches out the task.

![](images/10-interpretability/fig_p3_1.png)

*图 10.3 全词 WSD 任务：从输入词（x）映射到 WordNet 义项（y）。图改编自 Chaplot 和 Salakhutdinov（2018）。*
*Figure 10.3 The all-words WSD task, mapping from input words (x) to WordNet senses(y). Figure inspired by Chaplot and Salakhutdinov (2018).*

WSD 可以成为人文与社会科学领域文本分析的一种有用工具，而词义也能在词表示的模型可解释性中发挥作用。词义还具有有趣的分布特性。例如，一个词在一篇话语中往往以大致相同的义项使用，这一观察

> WSD can be a useful analytic tool for text analysis in the humanities and social sciences, and word senses can play a role in model interpretability for word representations. Word senses also have interesting distributional properties. For example a word often is used in roughly the same sense through a discourse, an observation

> `one sense per discourse`（一篇话语一个义项）
>
> 释义：指一个词在一篇话语的范围内通常始终使用大致相同的意义，是可资利用的分布规律。

被称为一篇话语一个义项规则（Gale 等，1992a）。

> called the one sense per discourse rule (Gale et al., 1992a).

表现最好的 WSD 算法是一个简单的 1-最近邻算法

> The best performing WSD algorithm is a simple 1-nearest-neighbor algorithm
它使用上下文词嵌入，由 Melamud 等（2016）与 Peters 等（2018）提出。在训练时，我们把某个带义项标注的数据集（如多种语言中的 SemCor 或 SenseEval 数据集）中的每个句子输入任意一种上下文嵌入模型（例如 BERT），从而为每个带标注的词元得到一个上下文嵌入。（计算词元 i 的上下文嵌入 vi 有多种方式；对 BERT 而言，常见做法是把 i 在最后四个 BERT 层中的向量表示相加，以汇聚多个层。）随后，对语料中任何词的每个义项 s，针对该义项的 n 个词元，我们对它们的 n 个上下文表示 vi 取平均，得到 s 的上下文义项嵌入 vs：

> using contextual word embeddings, due to Melamud et al. (2016) and Peters et al.(2018). At training time we pass each sentence in some sense-labeled dataset (like the SemCore or SenseEval datasets in various languages) through any contextual embedding (e.g., BERT) resulting in a contextual embedding for each labeled token.(There are various ways to compute this contextual embedding vi for a token i; for BERT it is common to pool multiple layers by summing the vector representations of i from the last four BERT layers). Then for each sense s of any word in the corpus, for each of the n tokens of that sense, we average their n contextual representations vi to produce a contextual sense embedding vs for s:

vs = 1 X

$$∀v_{i}\in\text{tokens}(s)$$

n vi (10.1)
在测试时，给定语境中目标词 t 的一个词元，我们计算它的上下文嵌入 t，并从训练集中选择其最近邻义项，即其义项嵌入与 t 的余弦最高的义项：

> At test time, given a token of a target word t in context, we compute its contextual embedding t and choose its nearest neighbor sense from the training set, i.e., the sense whose sense embedding has the highest cosine with t:

> i

$$\text{sense}(t) =\text{argmax}\text{cosine}(t,v_{s})$$

> s∈senses(t)

图 10.4 展示了该模型。

> Fig. 10.4 illustrates the model.

![](images/10-interpretability/fig_p4_0.png)

*图 10.4 WSD 的最近邻算法。绿色部分是为每个词的每个义项预先计算好的上下文嵌入；这里只展示 find 的少数几个义项。为目标词 found 计算上下文嵌入，然后选择最近邻义项（本例中为 find9v）。图改编自 Loureiro 和 Jorge（2019）。*
*Figure 10.4 The nearest-neighbor algorithm for WSD. In green are the contextual embeddings precomputed for each sense of each word; here we just show a few of the senses for find. A contextual embedding is computed for the target word found, and then the nearest neighbor sense (in this case find9v) is chosen. Figure inspired by Loureiro and Jorge (2019).*

### 10.1.2 上下文嵌入与词的相似度

> 10.1.2 Contextual Embeddings and Word Similarity

在第 5 章，我们提出了这样一个想法：可以把余弦用作相似度函数，通过考察两个词在几何上的接近程度来度量它们的相似性。意义相似性这一想法在图 10.2 的意义聚类中同样清晰地体现为几何上的接近；一个在语境中具有特定义项的词，其表示与该词相同义项的其他实例更为接近。因此，我们常常用两个上下文嵌入之间的余弦来度量语境中两个词的两个实例（或同一个词在两个不同语境中的两个实例）之间的相似度。

> In Chapter 5 we introduced the idea that we could measure the similarity of two words by considering how close they are geometrically, by using the cosine as a similarity function. The idea of meaning similarity is also clear geometrically in the meaning clusters in Fig. 10.2; the representation of a word which has a particular sense in a context is closer to other instances of the same sense of the word. Thus we often measure the similarity between two instances of two words in context (or two instances of the same word in two different contexts) by using the cosine between their contextual embeddings.

通常，在计算

> Usually some transformations to the embeddings are required before computing
余弦之前，需要对嵌入做一些变换。这是因为上下文嵌入（无论来自掩码语言模型还是自回归模型）都具有这样的性质：所有词的向量都极其相似。如果我们观察 BERT 或其他模型最后一层的嵌入，任意两个随机选取的词的实例的嵌入都会有极高的余弦，甚至可能相当接近 1，这意味着所有词向量倾向于指向同一方向。系统中所有向量都倾向于指向同一方向的性质称为各向异性。Ethayarajh（2019）把模型的各向异性定义为任意一对词在

> cosine. This is because contextual embeddings (whether from masked language models or from autoregressive ones) have the property that the vectors for all words are extremely similar. If we look at the embeddings from the final layer of BERT or other models, embeddings for instances of any two randomly chosen words will have extremely high cosines that can be quite close to 1, meaning all word vectors tend to point in the same direction. The property of vectors in a system all tending to point in the same direction is known as anisotropy. Ethayarajh (2019) defines the anisotropy of a model as the expected cosine similarity of any pair of words in

> `anisotropy`（各向异性）
>
> 释义：指系统中所有向量倾向于指向同一方向，使任意两词的余弦相似度异常偏高。

一个语料中的期望余弦相似度。‘各向同性’（isotropy）一词意为在所有方向上均匀，因此在各向同性的模型中，向量的集合应当指向各个方向，任意一对随机嵌入的期望余弦将为零。Timkey 和 van Schijndel（2021）指出，造成各向异性的一个原因是余弦度量被上下文嵌入中少数几个取值与其他维度差异很大的维度所主导：这些异常维度具有非常大的量级和极高的方差。

> a corpus. The word ‘isotropy’ means uniformity in all directions, so in an isotropic model, the collection of vectors should point in all directions and the expected cosine between a pair of random embeddings would be zero. Timkey and van Schijndel(2021) show that one cause of anisotropy is that cosine measures are dominated by a small number of dimensions of the contextual embedding whose values are very different than the others: these rogue dimensions have very large magnitudes and very high variance.

Timkey 和 van Schijndel（2021）表明，我们可以让嵌入更加

> Timkey and van Schijndel (2021) shows that we can make the embeddings more
各向同性，办法是对向量进行标准化（z 分数标准化），即减去均值并除以方差。给定某个语料中所有嵌入的集合 C，每个嵌入的维数为 d（即 x ∈Rd），均值向量 µ ∈Rd 为：

> isotropic by standardizing (z-scoring) the vectors, i.e., subtracting the mean and dividing by the variance. Given a set C of all the embeddings in some corpus, each with dimensionality d (i.e., x ∈Rd), the mean vector µ ∈Rd is:

µ = 1 X (10.3)
|C| x
每个维度上的标准差 σ ∈Rd 为：

> The standard deviation in each dimension σ ∈Rd is:

> x∈C

s (10.4)
1 X

$$(x-µ)^{2}$$

σ = |C|
然后，每个词向量 x 都被替换为其标准化版本 z：

> Then each word vector x is replaced by a standardized version z:

> x∈C

z = x−µ (10.5)
σ
余弦相似度有一个标准化无法解决的问题，即余弦往往

> One problem with cosine that is not solved by standardization is that cosine tends
会低估人类对非常高频的词在词义相似度上的判断（Zhou 等，2022）。

> to underestimate human judgments on similarity of word meaning for very frequent words (Zhou et al., 2022).

## 10.2 探针分析

> 10.2 Probing

我们常常想要知道，网络中的某个特定表示是否编码了某些特定信息。例如，我们可能想知道网络如何处理关于语法或意义的语言信息，比如在某一层，网络对单词 ketchup 的表示是否编码了它是名词而非动词这一事实。又或者，单词 sublet（既可为过去时也可为现在时）的表示是否编码了某个特定句子中的时态，如果是，这发生在网络的哪一层。

> Often we have want to know whether a particular representation in the network encodes some particular information. For example we might want to know how the network processing linguistic information about grammar or meaning, such as whether at a certain layer the network’s representation of the word ketchup encodes the fact that it is a noun and not a verb. Or whether the representation of the word sublet (which can be past or present tense) encodes the tense in a particular sentence, and if so at what layer of the network this happens.

用于此目的的最简单技术称为探针分析。在探针分析中，我们构建一个分类器，它可以是逻辑回归或线性回归，也可以是一个小型 MLP，它以嵌入向量为输入，返回我们关注的类别（比如“名词”或“动词”）。

> The simplest technique for this is called probing. In probing, we build a clas- sifier, which can be logistic or linear regression or a small MLP which takes an embedding vector as input and returns the class of interest (say ‘noun’, or ‘verb’).

如果探针给出该词是名词的高概率（与某些对照条件相比），那么我们就说该表示很可能编码了名词这一概念。图 10.5 展示了这一直觉，其中 3 个可能的探针分别考察 BERT 表示内部的两个不同嵌入向量。

> If the probe has a high probability, say, that the word is a noun, (as compared with some control conditions), then we say that the representation probably encodes the concept of noun. Fig. 10.5 shows the intuition, showing 3 potential probes looking at two different embedding vectors inside a BERT representation.

探针分析已被用于研究信息在 Transformer 中从较低层向

> Probing has been used to study the way information propagates up from lower to
较高层传播的方式，例如表明关于词元的语法信息似乎编码在较低层，语义信息编码在中间层，而像共指这样的话语信息则位于更高的层（Tenney 等，2019）。

> higher layers in the transformer, showing for example that grammatical information about tokens seems to be encoded at lower layers, semantic information at middle layers, and discourse information like coreference still higher (Tenney et al., 2019).

![](images/10-interpretability/fig_p6_0.png)

*图 10.5 在探针分析中，我们通过训练简单分类器来提取词元（如是否为动词、是否为过去时）或句子（如是否发生在西班牙）的语言学属性或其他属性，从而探究模型中的某个表示编码了哪些信息。这里我们看到 3 个不同的探针考察 2 个表示，h3 CLS 与 h1 2。*
*Figure 10.5 In probing, we explore what information is encoded in some representation in the model by training simple classifiers to extract linguistic or other properties of tokens (like being a verb or being in the past tense) or sentences (like taking place in Spain). Here we see 3 different probes examining 2 representations, h3 CLS and h1 2.*

探针分析有两个阶段：训练与测试。训练一个探针有 4 个步骤：

> Probing has two phases, training and testing. Training a probe has 4 steps:

- 选择我们想要考察的属性（如词性、意义的某个方面，或代词与哪个实体共指）
- 在我们有兴趣研究的某个位置和层上（如“Transformer 第 2 层到第 16 层前馈网络的输出”）构建训练集与测试集的嵌入，并标注出正确答案（相关的词性、时态或其他）。
- 把训练集的句子输入大语言模型，并提取激活值
- 现在冻结大语言模型的权重，只训练分类器的权重，使其把嵌入映射到某个属性。

> Choose a property we want to examine (like part of speech, or some aspect of meaning, or which entity a pronoun corefers with)
> Create a training and test set of embeddings at some position and level we are interested in studying (like “the output of the feedforward network at transformer layers 2 through 16”), labeled with the correct answer (the relevant part of speech, or tense, or whatever).
> Pass the training set sentences through the LLM, and extract activations
> Now freeze the weights of the LLM, and train only the weights of the classifier to map from an embedding to a property.

在推理时，我们把测试集的文本输入模型，提取激活值，让它们通过分类器，并报告模型能否正确提取该属性。

> At inference times we pass a test set text through the model, extract activations, and pass them through the classifier, and report on whether the model is able to correctly extract the property.

探针分析通常需要与对照条件进行比较，比如确保

> Probing generally requires comparing to control conditions, like making sure
其表现优于使用随机标签进行探针分析的结果（Belinkov 等，2017）。

> that performance is better than probing with random labels (Belinkov et al., 2017).

而且探针不能过于强大，这一点很重要，以免它之所以成功是因为相关信息编码在探针权重本身，而非编码在表示之中（Hewitt 和 Liang，2019）。

> And it’s important that the probe not be too powerful, to keep it from succeeding because the relevant information is encoded in the probe weights themselves rather than in the representation (Hewitt and Liang, 2019).

虽然探针分析的成功表明信息编码在表示之中，

> While success at probing shows that information is encoded in a representation,
但这并不证明模型使用了这些信息。也就是说，被探查的信息可能与嵌入中的内容相关，却对模型的行为没有因果影响（Belinkov，2022）。

> it doesn’t prove that the model uses the information. That is, the information being probed could be correlated with what’s in the embedding, but not have a causal effect on the model’s behavior (Belinkov, 2022).

## 10.3 logit lens

> 10.3 The Logit Lens

另一个有用的可解释性工具是 logit lens（Nostalgebraist，2020），它提供了一种

> Another useful interpretability tool, the logit lens (Nostalgebraist, 2020), offers a

> `logit lens`
>
> 释义：把 Transformer 任意一层的向量直接乘以解嵌入矩阵并做 softmax，以查看该层可能表示哪些词。

可视化 Transformer 内部各层可能表示什么的方法。

> way to visualize what the internal layers of the transformer might be representing.

其思路是：我们从 Transformer 的任意一层取出任意向量，假装它就是最终层之前的嵌入，直接把它乘以解嵌入层得到 logit，再计算 softmax，以查看该向量可能表示的词上的分布。这可以成为观察模型内部表示的一个有用窗口。由于网络在训练时并未让内部表示以这种方式起作用，logit lens 并不总能完美工作，但这仍然是一个有用的技巧，能帮助我们可视化 Transformer 的内部各层。

> The idea is that we take any vector from any layer of the transformer and, pretending that it is the prefinal embedding, simply multiply it by the unembedding layer to get logits, and compute a softmax to see the distribution over words that that vector might be representing. This can be a useful window into the internal representations of the model. Since the network wasn’t trained to make the internal representations function in this way, the logit lens doesn’t always work perfectly, but this can still be a useful trick to help us visualize the internal layers of a transformer.

Jacobian lens 或称 J-lens（Gurnee 等，2026）是 logit lens 的一个变体，它

> The Jacobian lens or J-lens (Gurnee et al., 2026) is a variant of the logit lens that

> `J-lens`
>
> 释义：一种变体方法，通过计算最终层对中间层的导数，把早期层的嵌入映射到输出空间，以解读浅层编码了什么。

在揭示模型于较早层编码了什么方面似乎表现更好。

> seems to perform better at uncovering what the model is encoding at earlier layers.

logit lens 以同样的方式解释所有层，即把某一层的嵌入乘以同一个解编码矩阵。因此，它隐含地假设较早层的表示与最终层处于同一个嵌入空间。而 J-lens 则考察最终层关于中间层的导数，追问层的微小变化会如何影响最终层的输出表示。因此，它实际上是把较早层的嵌入通过对其余网络的一个近似，并且还在许多上下文上取平均。

> The logit lens interprets all layers the same way, by multiplying an embedding at that layer by the same unencoding matrix. It thus implicitly makes the assumption that representations at earlier layers are in the same embedding space as the final layer. The J-lens instead looks at the derivatives of the final layer with respect to the intermediate layers, asking how a small change in layers would affect the final layer output representation. It thus effectively is passing embeddings at earlier layers through an approximation of the rest of the network, and also averages over many contexts.

logit lens 把 Transformer 的中间层当作它们已经

> The logit lens treats the intermediate layers of a transformer as if they already
能说最终输出的“语言”。而 Jacobian lens 则充当翻译器，映射早期层中的一个微小推动如何实际改变最终输出的词元

> speak the ”language” of the final output. The Jacobian lens acts as a translator, mapping how a small push in an early layer physically alters the final output tokens
。

> .

![](images/10-interpretability/fig_p7_0.png)

*图 10.6 对于 2 个不同的前缀，模型在不同层上最可能的词。*
*Figure 10.6 The most likely words at different layers of the model for 2 different prefixes.*

> 左侧示例展示了模型进行多跳推理的能力，这在 J-lens 中尤为成功：模型首先编码颜色的概念，接着更高的层似乎把“第四颗行星”这一指称解析为火星，直到更晚才开始编码红色。
>
> *The left example shows the ability of the model to do multihop reasoning, particularly successful in the J-lens, where the model first encodes the idea of color, then higher layers seem to resolve the “fourth planet” reference to refer to Mars, and only later starting encoding red.*

> 右侧示例中，logit lens 与 J-lens 似乎都编码了反义的概念，而只有在更高的层才表示出正确的反义词 large，先以英语、之后以俄语、最后以正确的中文。图片来自（Gurnee 等，2026）的图 51。
>
> *The right model both the logit lens and the J-lens seem to encode the concept of opposites, and only at higher layers represent the correct opposite large first in English, then in Russian, and finally in the correct Chinese. Image from Figure 51 of (Gurnee et al., 2026).*

J-lens 揭示出似乎存在一种工作空间，模型在其中

> The J-lens uncovers what seems to be a kind of workspace where the model
逐层地推理问题。图 10.6 给出了在 Anthropic Claude Sonnet 4.5 模型的不同层上，J-lens 与 logit lens 对此的直观展示。

> reasons through problems, layer by layer. Fig. 10.6 shows an intuition of this for the J-lens and logit lens at different layers of the Anthropic Claude Sonnet 4.5 model.

左侧示例展示了模型利用各层依次推理一个关于颜色的多步推理问题，该问题要求模型首先识别出第四颗行星。右侧示例则表明，模型似乎主要以英语来表示这些含义，并只在较后的层才把它们翻译成相应的语言用于输出

> The left example shows the model using layers to reason successively through a multi-step reasoning question about color that requires the model to first identify the fourth planet. And the right example shows that the model seems to represent these meanings mostly in English, and then translate them into relevant languages for output only in later layers

## 10.4 稀疏自编码器

> 10.4 Sparse Auto-Encoders

## 10.5 因果可解释性技术

> 10.5 Causal Interpretability Techniques

## 10.6 上下文学习与归纳头

> 10.6 In-Context Learning and Induction Heads

作为一种让模型做我们想做的事的方式，我们可以把提示视为与预训练有本质区别。通过预训练进行学习意味着依据某个损失函数，使用梯度下降更新模型的参数。

> As a way of getting a model to do what we want, we can think of prompting as being fundamentally different than pretraining. Learning via pretraining means updating the model’s parameters by using gradient descent according to some loss function.

但用示例进行提示可以教会模型完成一项新任务。模型在处理提示词的过程中，从这些示例里学到了关于该任务的某些东西。

> But prompting with demonstrations can teach a model to do a new task. The model is learning something about the task from those demonstrations as it processes the prompt.

即使没有示例，我们也可以把提示的过程看作一种

> Even without demonstrations, we can think of the process of prompting as a kind
学习。例如，模型在提示词中推进得越远，它预测后续词元的表现往往就越好。上下文中的信息帮助模型获得更强的预测能力。

> of learning. For example, the further a model gets in a prompt, the better it tends to get at predicting the upcoming tokens. The information in the context is helping give the model more predictive power.

> `in-context`（上下文内）
>
> 释义：指信息位于模型当前接收的提示词上下文之中，模型据此即时调整预测，而不改变自身参数。

上下文学习（in-context learning）这一术语最早由 Brown 等人（2020）在其

> The term in-context learning was first proposed by Brown et al. (2020) in their

> `learning`（学习）
>
> 释义：此处指模型从提示词上下文中获取信息，从而在推理时无需更新参数即可改善预测的过程。

介绍 GPT3 系统的论文中提出，用来指代语言模型从提示词中进行的这两类学习中的任意一种。上下文学习指语言模型在推理阶段的前向传播过程中学会完成新任务、更好地预测词元，或者总体降低其损失，而无需对模型参数进行任何基于梯度的更新。

> introduction of the GPT3 system, to refer to either of these kinds of learning that language models do from their prompts. In-context learning means language models learning to do new tasks, better predict tokens, or generally reduce their loss during the forward-pass at inference-time, without any gradient-based updates to the model’s parameters.

上下文学习是如何工作的？虽然我们并不完全确定，但已有

> How does in-context learning work? While we don’t know for sure, there are
一些引人入胜的想法。其中一种假设建立在归纳头这一概念之上

> some intriguing ideas. One hypothesis is based on the idea of induction heads

> `induction heads`（归纳头）
>
> 释义：注意力计算中的一类电路，能识别重复出现的模式并预测其后续词元，被认为与上下文学习相关。

（Elhage 等，2021；Olsson 等，2022）。归纳头是对一种电路（circuit）的称呼，电路是网络中一类抽象的组件。归纳头电路是 Transformer 中注意力计算的一部分，研究者通过观察仅有 1-2 个注意力头的微型语言模型发现了它。

> (Elhage et al., 2021; Olsson et al., 2022). Induction heads are the name for a circuit, which is a kind of abstract component of a network. The induction head circuit is part of the attention computation in transformers, discovered by looking at mini language models with only 1-2 attention heads.

归纳头的功能是预测重复出现的序列。例如

> The function of the induction head is to predict repeated sequences. For example
如果它在输入序列中看到模式 AB...A，就会预测后面跟着 B，从而实例化模式补全规则 AB...A→B。它通过注意力计算中的一个前缀匹配组件来实现这一点：当看到当前词元 A 时，该组件会在上下文中向前搜索，找出此前出现过的 A。若找到，归纳头便通过一个复制机制“复制”先前 A 之后所跟的词元 B，方法是提高 B 接下来出现的概率。图 10.7 给出了一个例子。

> if it sees the pattern AB...A in an input sequence, it predicts that B will follow, instantiating the pattern completion rule AB...A→B. It does this by having a prefix matching component of the attention computation that, when looking at the current token A, searches back over the context to find a prior instance of A. If it finds one, the induction head has a copying mechanism that “copies” the token B that followed the earlier A, by increasing the probability the B will occur next. Fig. 10.7 shows an example.

Olsson 等人（2022）提出，这一模式补全规则的一种广义模糊版本——即实现形如 A*B*...A→B 的规则，其中 A* ≈ A 且 B* ≈ B（这里的 ≈ 指它们在某种意义下语义相似）——可能正是上下文学习的原因所在。支持他们假设的提示性证据来自 Cros-

> Olsson et al. (2022) propose that a generalized fuzzy version of this pattern completion rule, implementing a rule like A*B*...A→B, where A* ≈A and B* ≈B(by ≈we mean they are semantically similar in some way), might be responsible for in-context learning. Suggestive evidence for their hypothesis comes from Cros-

![](images/10-interpretability/fig_p9_0.png)

*图 10.7 一个归纳头在处理 vintage 时，使用前缀匹配机制找到此前出现过的 vintage，并用复制机制预测 cars 会再次出现。图来自 Crosbie 与 Shutova（2022）。*
*Figure 10.7 An induction head looking at vintage uses the prefix matching mechanism to find a prior instance of vintage, and the copying mechanism to predict that cars will occur again. Figure from Crosbie and Shutova (2022).*

bie 与 Shutova（2022），他们表明消融归纳头会导致上下文

> bie and Shutova (2022), who show that ablating induction heads causes in-context

> `ablating`（消融）
>
> 释义：通过使某个组件失效（例如将其输出置零）来观察其因果作用，是检验可解释性假设的实验手段。

学习性能下降。消融原本是一个医学术语，意为切除某物。在 NLP 可解释性研究中，我们把它用作检验因果效应的工具：如果剔除一个假设的原因，我们预期相应的效应也会消失。Crosbie 与 Shutova（2022）消融归纳头的做法是，先找出在随机输入序列上表现得像归纳头的注意力头，然后通过把输出矩阵 WO 的某些元素置零来将这些头的输出归零。他们确实发现，消融后的模型在上下文学习上差得多：它们从提示词中的示例学习的效果要差很多。

> learning performance to decrease. Ablation is originally a medical term meaning the removal of something. We use it in NLP interpretability studies as a tool for testing causal effects; if we knock out a hypothesized cause, we would expect the effect to disappear. Crosbie and Shutova (2022) ablate induction heads by first finding attention heads that perform as induction heads on random input sequences, and then zeroing out the output of these heads by setting certain terms of the output matrix WO to zero. Indeed they find that ablated models are much worse at in-context learning: they have much worse performance at learning from demonstrations in the prompts.
