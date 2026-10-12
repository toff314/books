# 第 20 章 依存句法分析

### 章

> CHAPTER

# 20 依存句法分析

> 20 Dependency Parsing

凡是构成句子一部分的每一个词……在它与它的邻词之间，心智察觉到种种联系，这些联系共同构成句子的骨架。

> Tout mot qui fait partie d’une phrase... Entre lui et ses voisins, l’esprit aperc¸oit des connexions, dont l’ensemble forme la charpente de la phrase.

[在句子中每个词与其邻词之间，心智察觉到种种联系。这些联系共同构成句子的骨架。]

> [Between each word in a sentence and its neighbors, the mind perceives connections. These connections together form the scaffolding of the sentence.]
上一章的重点是上下文无关文法和基于成分的表示。这里我们介绍另一个重要的语法形式体系族，称为依存语法。在依存形式体系中，短语成

> The focus of the last chapter was on context-free grammars and constituentbased representations. Here we present another important family of grammar formalisms called dependency grammars. In dependency formalisms, phrasal con-

> Lucien Tesnière. 1959. Éléments de syntaxe structurale, A.1.§3
>
> *Lucien Tesni`ere. 1959. ´El´ements de syntaxe structurale, A.1.§3*

> `dependency grammars`（依存语法）
>
> 释义：只用词与词之间的有向二元语法关系来描述句子句法结构的一类形式语法，短语成分和短语结构规则在其中不起直接作用。

分和短语结构规则并不起直接作用。相反，句子的句法结构仅用词与词之间的有向二元语法关系来描述，如下面的依存句法分析所示：

> stituents and phrase-structure rules do not play a direct role. Instead, the syntactic structure of a sentence is described solely in terms of directed binary grammatical relations between the words, as in the following dependency parse:

> root

> obj

> det nmod

(20.1)

> nsubj compound case

I prefer the morning flight through Denver
词与词之间的关系在句子上方用有向、带标签的

> Relations among the words are illustrated above the sentence with directed, labeled

> `typed`（带类型的（typed））
>
> 释义：指依存弧上带有语法关系标签，标签取自一份固定的语法关系清单，如 nsubj、obj 等。

弧从中心词指向依存词来标示。我们称之为带类型的依存结构，因为

> arcs from heads to dependents. We call this a typed dependency structure because

> `dependency`（依存（dependency））
>
> 释义：指词与词之间一个词支配另一个词的单向句法联系，句子的结构全靠这类有向关系来描写。

这些标签取自一份固定的语法关系清单。根节点明确标出树的根，也就是整个结构的中心词。

> the labels are drawn from a fixed inventory of grammatical relations. A root node explicitly marks the root of the tree, the head of the entire structure.

下一页的图 20.1 展示了式 20.1 的依存分析，但

> Figure 20.1 on the next page shows the dependency analysis from Eq. 20.1 but
以树的形式可视化，并与上一章所给出的那种相应的短语结构分析并列。注意，依存分析中不存在与短语成分或词汇类别相对应的节点；依存分析的内部结构仅由词与词之间的有向关系构成。这些中心词-依存词关系直接编码了往往被埋没在更复杂的短语结构分析中的重要信息。例如，动词 prefer 的论元在依存结构中直接与它相连，而在短语结构树中，它们与主要动词的联系则要疏远得多。同样，作为 flight 的修饰语的 morning 和 Denver，在依存结构中直接与之相连。

> visualized as a tree, alongside its corresponding phrase-structure analysis of the kind given in the prior chapter. Note the absence of nodes corresponding to phrasal constituents or lexical categories in the dependency parse; the internal structure of the dependency parse consists solely of directed relations between words. These headdependent relationships directly encode important information that is often buried in the more complex phrase-structure parses. For example, the arguments to the verb prefer are directly linked to it in the dependency structure, while their connection to the main verb is more distant in the phrase-structure tree. Similarly, morning and Denver, modifiers of flight, are linked to it directly in the dependency structure.

中心词-依存词关系能够很好地代表谓语与其论元之间的语义关系，这一事实是依存语法目前在自然语言处理中比成分结构语法更为常见的一个重要原因。

> This fact that the head-dependent relations are a good proxy for the semantic relationship between predicates and their arguments is an important reason why dependency grammars are currently more common than constituency grammars in natural language processing.

依存语法的另一个主要优势在于它们能够处理

> Another major advantage of dependency grammars is their ability to deal with
语序相对自由的语言。例如，捷克语中的语序

> languages that have a relatively free word order. For example, word order in Czech

> `free word order`（自由语序）
>
> 释义：指词语在句中的次序比较灵活，语法功能主要由形态而非位置决定，同一成分可以出现在不同位置。

可能比英语灵活得多；一个语法宾语可能出现在地点状语之前或之后。而短语结构语法则需要为分析树中

> can be much more flexible than in English; a grammatical object might occur before or after a location adverbial. A phrase-structure grammar would need a separate rule

![](images/20-dependency-parsing/fig_p2_0.png)

*图 20.1 I prefer the morning flight through Denver 的依存分析与成分分析。*
*Figure 20.1 Dependency and constituent analyses for I prefer the morning flight through Denver.*

这类状语短语可能出现的每一个位置，单独设一条规则。

> for each possible place in the parse tree where such an adverbial phrase could occur.

基于依存的方法只需一种链接类型来表示这一特定的状语关系；因此依存语法方法能够更多地摆脱语序信息。

> A dependency-based approach can have just one link type representing this particular adverbial relation; dependency grammar approaches can thus abstract away a bit more from word order information.

在接下来的几节中，我们将给出依存句法分析中所用关系的清单，

> In the following sections, we’ll give an inventory of relations used in dependency
讨论两族句法分析算法（基于转移的和基于图的），并讨论评价。

> parsing, discuss two families of parsing algorithms (transition-based, and graphbased), and discuss evaluation.

## 20.1 依存关系

> 20.1 Dependency Relations

> `grammatical relation`（语法关系）
>
> 释义：指中心词与其依存词之间带类型标注的句法联系，如主语、宾语、修饰语等，标签来自固定的清单。

语言学中传统的语法关系概念，为构成这些依存结构的

> The traditional linguistic notion of grammatical relation provides the basis for the
二元关系提供了基础。这些关系的论元由一个中心词和一个依存词构成。中心词扮演核心的

> binary relations that comprise these dependency structures. The arguments to these relations consist of a head and a dependent. The head plays the role of the central

> `head`（中心词）
>
> 释义：依存关系中起支配作用的词，是所辖结构的组织核心，其余的词都直接或间接依存于它。

组织性词项的角色，而依存词则是一种修饰语。中心词-依存词关系通过把中心词直接链接到紧依存于它的词而得到显式表达。

> organizing word, and the dependent as a kind of modifier. The head-dependent relationship is made explicit by directly linking heads to the words that are immediately dependent on them.

> `dependent`（依存词）
>
> 释义：依存关系中受中心词支配的词，在句中充当修饰语一类的角色，直接挂在中心词之下。

除了指明中心词-依存词对之外，依存语法还允许

> In addition to specifying the head-dependent pairs, dependency grammars allow

> `grammatical function`（语法功能）
>
> 释义：对中心词-依存词关系所做的类别划分，也就是主语、宾语、修饰语等句法角色的名称。

我们对语法关系的种类，或者说这些关系所承担的语法功能，进行分类，即

> us to classify the kinds of grammatical relations, or grammatical function that the
依存词相对于其中心词所扮演的角色。这些关系包括主语、直接宾语和间接宾语等人们熟悉的概念。在英语中，这些概念与句子中的位置以及成分类型密切相关，但绝不决定它们，因此与短语结构树中所能找到的那类信息在一定程度上有所重复。然而，在语序更为灵活的语言中，这些语法关系直接编码的信息至关重要，因为基于短语的成分句法几乎提供不了什么帮助。

> dependent plays with respect to its head. These include familiar notions such as subject, direct object and indirect object. In English these notions strongly correlate with, but by no means determine, both position in a sentence and constituent type and are therefore somewhat redundant with the kind of information found in phrase-structure trees. However, in languages with more flexible word order, the information encoded directly in these grammatical relations is critical since phrasebased constituent syntax provides little help.

语言学家们已经发展出各种关系的分类体系，远远超出人们熟悉的主语和宾语概念。尽管不同理论之间存在相当大的差异，

> Linguists have developed taxonomies of relations that go well beyond the familiar notions of subject and object. While there is considerable variation from theory

> 从句论元关系 描述
>
> *Clausal Argument Relations Description*

*图 20.2 部分通用依存关系（de Marneffe 等，2021）。*
*Figure 20.2 Some of the Universal Dependency relations (de Marneffe et al., 2021).*

> 名词性主语
>
> *Nominal subject*

> NSUBJ

> 直接宾语
>
> *Direct object*

> OBJ

> 间接宾语
>
> *Indirect object*

> IOBJ

> 从句补语
>
> *Clausal complement*

> CCOMP

> 名词性修饰语关系 描述
>
> *Nominal Modifier Relations Description*

> 名词性修饰语
>
> *Nominal modifier*

> NMOD

> 形容词性修饰语
>
> *Adjectival modifier*

> AMOD

> 同位语修饰语
>
> *Appositional modifier*

> APPOS

> 限定词
>
> *Determiner*

> DET

> 前置词、后置词及其他格标记
>
> *Prepositions, postpositions and other case markers*

> CASE

> 其他值得注意的关系 描述
>
> *Other Notable Relations Description*

> 并列项
>
> *Conjunct*

> CONJ

> 并列连词
>
> *Coordinating conjunction*

> CC

从一种理论到另一种理论，都存在足够的共性，因此跨语言的标准已经

> to theory, there is enough commonality that cross-linguistic standards have been

> `Universal`（通用（Universal））
>
> 释义：此处为通用依存（UD）标注体系名称的一部分，指该体系力图跨语言通用，覆盖 100 多种语言。

被制定出来。通用依存（Universal Dependencies，UD）项目（de Marneffe 等，2021），

> developed. The Universal Dependencies (UD) project (de Marneffe et al., 2021),

> `Dependencies`（依存（Dependencies））
>
> 释义：指词与词之间中心词和依存词的语法关系，是通用依存体系用来刻画句子结构的核心内容。

是一个开放的社区项目，致力于为 100 多种语言标注依存关系及其他语法信息，它提供了包含 37 种依存关系的清单。

> an open community effort to annotate dependencies and other aspects of grammar across more than 100 languages, provides an inventory of 37 dependency relations.

图 20.2 展示了 UD 关系的一个子集，图 20.3 给出了一些示例。

> Fig. 20.2 shows a subset of the UD relations and Fig. 20.3 provides some examples.

通用依存方案中所有这些关系背后的动机

> The motivation for all of the relations in the Universal Dependency scheme is
超出了本章的讨论范围，但常用的核心关系可以分为两类：一类是从句关系，描述相对于谓语（通常是动词）的句法角色；另一类是修饰语关系，对词修饰其中心词的方式加以归类。

> beyond the scope of this chapter, but the core set of frequently used relations can be broken into two sets: clausal relations that describe syntactic roles with respect to a predicate (often a verb), and modifier relations that categorize the ways that words can modify their heads.

例如，考虑下面这个句子：

> Consider, for example, the following sentence:

> `root`（根（root））
>
> 释义：依存树中最顶层的节点，即整个句子的中心词，通常由谓语动词充当，图中标注为 root。

> obj

> det nmod

(20.2)

> nsubj compound case

United canceled the morning flights to Houston
这里，从句关系 NSUBJ 和 OBJ 标出了谓语 cancel 的主语和直接宾语，而 NMOD、DET 和 CASE 关系则表示名词 flights 和 Houston 的修饰语。

> Here the clausal relations NSUBJ and OBJ identify the subject and direct object of the predicate cancel, while the NMOD, DET, and CASE relations denote modifiers of the nouns flights and Houston.

### 20.1.1 依存形式体系

> 20.1.1 Dependency Formalisms

依存结构可以表示为一个有向图 G = (V,A)，它由一个顶点集合 V 和一个顶点有序对集合 A 组成，我们把 A 中的元素称为弧。

> A dependency structure can be represented as a directed graph G = (V,A), consisting of a set of vertices V, and a set of ordered pairs of vertices A, which we’ll call arcs.

在大多数情况下，我们将假定顶点集合 V 恰好对应

> For the most part we will assume that the set of vertices, V, corresponds exactly
给定句子中的词集合。不过，它们也可能对应于标点符号；而在处理形态复杂的语言时，顶点集合还可能由词干和词缀构成。弧集合 A 刻画了 V 中各元素之间的中心词-依存词关系与语法功能关系。

> to the set of words in a given sentence. However, they might also correspond to punctuation, or when dealing with morphologically complex languages the set of vertices might consist of stems and affixes. The set of arcs, A, captures the headdependent and grammatical function relationships between the elements in V.

不同的语法理论或形式体系可能还会对

> Different grammatical theories or formalisms may place further constraints on
这些依存结构施加更多限制。较为常见的限制包括：结构必须连通、具有一个指定的根节点，并且是无环的或平面的。与本章所讨论的句法分析方法关系最大的，是那种常见的、

> these dependency structures. Among the more frequent restrictions are that the structures must be connected, have a designated root node, and be acyclic or planar. Of most relevance to the parsing approaches discussed in this chapter is the common,

> 关系　带有中心词与依存词的示例
>
> *Relation Examples with head and dependent*

*图 20.3 一些通用依存关系的示例。*
*Figure 20.3 Examples of some Universal Dependency relations.*

> United canceled the flight.

> NSUBJ

> United diverted the flight to Reno.

> OBJ

> We booked her the first flight to Miami. We booked her the flight to Miami.

> IOBJ

> We took the morning flight.

> COMPOUND

> flight to Houston.

> NMOD

> Book the cheapest flight.

> AMOD

> United, a unit of UAL, matched the fares.

> APPOS

> The flight was canceled.

> DET

> Which flight was delayed? We flew to Denver and drove to Steamboat.

> CONJ

> We flew to Denver and drove to Steamboat.

> CC

> Book the flight through Houston.

> CASE

> `dependency`（依存关系）
>
> 释义：指词与词之间由中心词支配依存词而形成的非对称二元关系，是依存句法分析中语法关系的载体。

出于计算动机的限制，即限定为有根树。也就是说，一棵依存树

> computationally-motivated, restriction to rooted trees. That is, a dependency tree

> `tree`（树）
>
> 释义：指满足连通、无环、只有一个根节点且除根外每个顶点恰有一条入弧等约束的有向图，用来表示依存结构。

是一个满足下列约束的有向图：

> is a directed graph that satisfies the following constraints:

- 有且仅有一个指定的根节点，它没有入弧。
- 除根节点之外，每个顶点恰好有一条入弧。
- 从根节点到 V 中的每个顶点都存在唯一一条路径。

> There is a single designated root node that has no incoming arcs.
> With the exception of the root node, each vertex has exactly one incoming arc.
> There is a unique path from the root node to each vertex in V.

综合起来，这些约束保证了每个词都只有一个中心词，保证了

> Taken together, these constraints ensure that each word has a single head, that the
依存结构是连通的，并且存在一个唯一的根节点，从该节点出发可以沿唯一的有向路径到达句子中的每一个词。

> dependency structure is connected, and that there is a single root node from which one can follow a unique directed path to each of the words in the sentence.

### 20.1.2 投射性

> 20.1.2 Projectivity

投射性这一概念施加了一条额外的约束，它源自输入中词的顺序。如果存在一条从中心词出发、通向位于中心词

> The notion of projectivity imposes an additional constraint that is derived from the order of the words in the input. An arc from a head to a dependent is said to be projective if there is a path from the head to every word that lies between the head

> `projective`（投射的）
>
> 释义：指依存弧满足投射性约束，即从中心词到依存词的路径不跨越句子中位于两者之间的词。

与依存词之间的每个词的路径，则称从中心词到依存词的弧是投射的。如果构成一棵依存树的所有弧都是投射的，则称这棵依存树是投射的。到目前为止我们看到的所有依存树都是投射的。然而，有许多合法的结构会导致非投射的树，特别是在语序相对灵活的语言中。

> and the dependent in the sentence. A dependency tree is then said to be projective if all the arcs that make it up are projective. All the dependency trees we’ve seen thus far have been projective. There are, however, many valid constructions which lead to non-projective trees, particularly in languages with relatively flexible word order.

考虑下面的例子。

> Consider the following example.

> acl:relcl

> root obl

> obj cop

(20.3)

> nsubj det det nsubj adv

JetBlue canceled our flight this morning which was already late
在这个例子中，从 flight 到其修饰语 late 的弧是非投射的，因为不存在从 flight 通向中间词 this 和 morning 的路径。从这个图可以看出，投射性（以及非投射性）可以通过我们绘制树的方式来检测。如果一棵依存树能在边不交叉的情况下绘出，那么它就是投射的。在这里，无法在不穿过连接 morning 与其中心词的弧的情况下，把 flight 连接到它的依存词 late。

> In this example, the arc from flight to its modifier late is non-projective since there is no path from flight to the intervening words this and morning. As we can see from this diagram, projectivity (and non-projectivity) can be detected in the way we’ve been drawing our trees. A dependency tree is projective if it can be drawn with no crossing edges. Here there is no way to link flight to its dependent late without crossing the arc that links morning to its head.

我们对投射性的关注源自两个相关的问题。第一，最

> Our concern with projectivity arises from two related issues. First, the most
广泛使用的英语依存树库，是通过中心词查找规则从短语结构树库自动转换而来的。以这种方式生成的树总是投射的，因此当遇到像这个例子这样的非投射实例时就会出错。

> widely used English dependency treebanks were automatically derived from phrasestructure treebanks through the use of head-finding rules. The trees generated in such a fashion will always be projective, and hence will be incorrect when non-projective examples like this one are encountered.

第二，最广泛使用的几类

> Second, there are computational limitations to the most widely used families of
句法分析算法存在计算上的局限。第 20.2 节讨论的基于转移的方法只能生成投射树，因此任何带有非投射结构的句子都必然包含一些错误。这一局限正是第 20.3 节所述更为灵活的基于图的句法分析方法的动机之一。

> parsing algorithms. The transition-based approaches discussed in Section 20.2 can only produce projective trees, hence any sentences with non-projective structures will necessarily contain some errors. This limitation is one of the motivations for the more flexible graph-based parsing approach described in Section 20.3.

### 20.1.3 依存树库

> 20.1.3 Dependency Treebanks

树库在依存句法分析器的开发与评价中起着关键作用。它们被用于训练分析器，充当评价分析器的黄金标准标签，同时也为语料库语言学研究提供有用的信息。

> Treebanks play a critical role in the development and evaluation of dependency parsers. They are used for training parsers, they act as the gold labels for evaluating parsers, and they also provide useful information for corpus linguistics studies.

依存树库的创建方式是，让人类标注者直接为

> Dependency treebanks are created by having human annotators directly generate
给定语料生成依存结构，或者人工修正自动分析器的输出。少数早期的树库还基于使用一个确定性过程，把已有的基于成分的树库转换为依存树。

> dependency structures for a given corpus, or by hand-correcting the output of an automatic parser. A few early treebanks were also based on using a deterministic process to translate existing constituent-based treebanks into dependency trees.

构建依存树的最大开放社区项目是上文介绍的 Universal Dependencies 项目，其网址为 https://universaldependencies.org/，它目前拥有 100 多种语言的近 200 个依存树库（de Marneffe et al., 2021）。下面给出几个 UD 示例，展示西班牙语、巴斯克语和汉语普通话句子的依存树：

> The largest open community project for building dependency trees is the Universal Dependencies project at https://universaldependencies.org/ introduced above, which currently has almost 200 dependency treebanks in more than 100 languages (de Marneffe et al., 2021). Here are a few UD examples showing dependency trees for sentences in Spanish, Basque, and Mandarin Chinese:

> punct

> obl obl:tmod

> case case

> det det

VERB ADP DET NOUN ADP DET NUM PUNCT Subiremos a el tren a las cinco . we-will-board on the train at the five .

[Spanish] Subiremos al tren a las cinco. “We will be boarding the train at five.”(20.4)
NOUN NOUN VERB AUX PUNCT Ekaitzak itsasontzia hondoratu du . storm (Erg.) ship (Abs.) sunk has .

> nsubj punct

> obj aux

[Basque] Ekaitzak itsasontzia hondoratu du. “The storm has sunk the ship.”(20.5)
ADV PRON NOUN ADV VERB VERB NOUN但 我 昨天 才 收 到 信but I yesterday only-then receive arrive letter .

> adv

> nsubj

> obj:tmod obj

> advmod compound:vv

[Chinese] 但我昨天才收到信“But I didn’t receive the letter until yesterday”(20.6)

## 20.2 基于转移的依存句法分析

> 20.2 Transition-Based Dependency Parsing

我们要介绍的第一种依存句法分析方法称为基于转移的句法分析。这种

> Our first approach to dependency parsing is called transition-based parsing. This

> `transition-based`（基于转移的）
>
> 释义：指通过逐步执行转移操作符（如 SHIFT、LEFTARC）来增量地构建依存树的一类分析方法。

架构借鉴了移进-归约分析，这是一种最初为分析编程语言而开发的范式（Aho and Ullman, 1972）。在基于转移的句法分析中，我们会有一个用来构建分析结果的栈、一个存放待分析词元的缓冲区，以及一个分析器，它经由称为神谕的预测器对分析过程采取动作，如图 20.4 所示。

> architecture draws on shift-reduce parsing, a paradigm originally developed for analyzing programming languages (Aho and Ullman, 1972). In transition-based parsing we’ll have a stack on which we build the parse, a buffer of tokens to be parsed, and a parser which takes actions on the parse via a predictor called an oracle, as illustrated in Fig. 20.4.

![](images/20-dependency-parsing/fig_p6_0.png)

*图 20.4 基本的基于转移的分析器。分析器检查栈顶的两个元素，并通过查询一个考察当前格局的神谕来选择动作。*
*Figure 20.4 Basic transition-based parser. The parser examines the top two elements of the stack and selects an action by consulting an oracle that examines the current configuration.*

分析器从左到右遍历句子，依次将元素转移

> The parser walks through the sentence left-to-right, successively shifting items
从缓冲区到栈上。在每个时刻，我们检查栈顶的两个元素，神谕决定应用哪个转移来构建句法分析结果。可能的转移对应着人们在从左到右单次遍历输入、通过考察词语来创建依存树时可能采取的直观动作（Covington，2001）：

> from the buffer onto the stack. At each time point we examine the top two elements on the stack, and the oracle makes a decision about what transition to apply to build the parse. The possible transitions correspond to the intuitive actions one might take in creating a dependency tree by examining the words in a single pass over the input from left to right (Covington, 2001):

- 将当前词指定为某个先前见过的词的中心词，
- 将某个先前见过的词指定为当前词的中心词，
- 推迟处理当前词，将其存储起来以供后续处理。

> Assign the current word as the head of some previously seen word,
> Assign some previously seen word as the head of the current word,
> Postpone dealing with the current word, storing it for later processing.

我们将用以下三个转移操作符把这一直观想法形式化，它们

> We’ll formalize this intuition with the following three transition operators that
将作用于栈顶的两个元素：

> will operate on the top two elements of the stack:

- LEFTARC：在栈顶的词与第二个词之间建立中心词-依存词关系；将第二个词从栈中移除。
- RIGHTARC：在栈上的第二个词与栈顶的词之间建立中心词-依存词关系；将栈顶的词从栈中移除；

> LEFTARC: Assert a head-dependent relation between the word at the top of the stack and the second word; remove the second word from the stack.
> RIGHTARC: Assert a head-dependent relation between the second word on the stack and the word at the top; remove the top word from the stack;

- SHIFT：将词从输入缓冲区的前端移除，并将其压入栈中。

> SHIFT: Remove the word from the front of the input buffer and push it onto the stack.

我们有时会把 LEFTARC 和 RIGHTARC 这类操作称为归约操作，这源自移位-归约句法分析的一个比喻，其中归约意味着合并栈上的元素。使用这些操作符有一些前提条件。当 ROOT 是栈的第二个元素时，不能应用 LEFTARC 操作符（因为根据定义，ROOT 节点不能有任何入弧）。并且，LEFTARC 和 RIGHTARC 操作符都要求栈上有两个元素才能应用。

> We’ll sometimes call operations like LEFTARC and RIGHTARC reduce operations, based on a metaphor from shift-reduce parsing, in which reducing means combining elements on the stack. There are some preconditions for using operators. The LEFTARC operator cannot be applied when ROOT is the second element of the stack(since by definition the ROOT node cannot have any incoming arcs). And both the LEFTARC and RIGHTARC operators require two elements to be on the stack to be applied.

这组特定的操作符实现了所谓的标准弧

> This particular set of operators implements what is known as the arc standard

> `arc standard`（标准弧（arc-standard））
>
> 释义：本书所述基于转移的依存句法分析方式，只在栈顶两元素间建立依存关系，元素一旦确定中心词即出栈。

方法（Covington 2001，Nivre 2003，Yamada 和 Matsumoto 2003）。在标准弧句法分析中，转移操作符只在栈顶元素之间建立关系，一旦某个元素被指定了中心词，它就会从栈中移除，不再可用于后续处理。正如我们将看到的，还有其他转移系统表现出不同的句法分析行为，但标准弧方法相当有效，且易于实现。

> approach to transition-based parsing (Covington 2001, Nivre 2003, Yamada and Matsumoto 2003). In arc standard parsing the transition operators only assert relations between elements at the top of the stack, and once an element has been assigned its head it is removed from the stack and is not available for further processing. As we’ll see, there are alternative transition systems which demonstrate different parsing behaviors, but the arc standard approach is quite effective and is simple to implement.

基于转移的分析器的规范相当简单，其基础是把句法分析的当前状态表示为一个格局：栈、一个输入缓冲区

> The specification of a transition-based parser is quite simple, based on representing the current state of the parse as a configuration: the stack, an input buffer

> `configuration`（格局）
>
> 释义：在基于转移的句法分析中描述分析器当前状态的三元组：栈、输入缓冲区以及已建立的依存关系集合。

（由词或词元组成），以及一个表示依存树的关系集合。句法分析意味着在可能的格局空间中做出一系列转移。我们从一个初始格局开始：其中栈包含 ROOT 节点，缓冲区含有句子中的词元，而空的关系集合表示句法分析结果。在最终的目标状态下，栈和词表都应为空，关系集合将表示最终的句法分析结果。图 20.5 给出了该算法。

> of words or tokens, and a set of relations representing a dependency tree. Parsing means making a sequence of transitions through the space of possible configurations. We start with an initial configuration in which the stack contains the ROOT node, the buffer has the tokens in the sentence, and an empty set of relations represents the parse. In the final goal state, the stack and the word list should be empty, and the set of relations will represent the final parse. Fig. 20.5 gives the algorithm.

![](images/20-dependency-parsing/fig_p7_0.png)

*图 20.5 一个通用的基于转移的依存句法分析器*
*Figure 20.5 A generic transition-based dependency parser*

在每一步，分析器查询一个神谕（我们稍后会回到这一点），它

> At each step, the parser consults an oracle (we’ll come back to this shortly) that
在给定当前格局的情况下提供正确的转移操作符。然后它将该操作符应用于当前格局，产生一个新的格局。

> provides the correct transition operator to use given the current configuration. It then applies that operator to the current configuration, producing a new configuration.

当句子中的所有词都被消耗完，且 ROOT 节点是栈上唯一剩下的元素时，该过程结束。

> The process ends when all the words in the sentence have been consumed and the ROOT node is the only element remaining on the stack.

基于转移的分析器的效率从该算法中应当显而易见。

> The efficiency of transition-based parsers should be apparent from the algorithm.

其复杂度与句子长度成线性关系，因为它基于对句子中词语的一次从左到右遍历。（每个词必须首先被转移到栈上，之后再进行归约。）

> The complexity is linear in the length of the sentence since it is based on a single left to right pass through the words in the sentence. (Each word must first be shifted onto the stack and then later reduced.)
注意，与第 19 章讨论的动态规划和基于搜索的方法不同，这种方法是一种直接的贪心算法——神谕在每一步提供一个选择，分析器就按该选择继续推进，不探索其他选项，不采用回溯，最终返回一个句法分析结果。

> Note that unlike the dynamic programming and search-based approaches discussed in Chapter 19, this approach is a straightforward greedy algorithm—the oracle provides a single choice at each step and the parser proceeds with that choice, no other options are explored, no backtracking is employed, and a single parse is returned in the end.

图 20.6 用一系列转移说明了分析器的运行过程

> Figure 20.6 illustrates the operation of the parser with the sequence of transitions
这些转移得到以下例子的句法分析结果。

> leading to a parse for the following example.

> root

> obj

> det

(20.7)

> iobj compound

Book me the morning flight
让我们考虑第 2 步的格局状态，此时词 me 已经被

> Let’s consider the state of the configuration at Step 2, after the word me has been
压入栈中。

> pushed onto the stack.

| 栈<br>Stack | 词表<br>Word List | 关系<br>Relations |
| --- | --- | --- |
| [root, book, me] | [the, morning, flight] |  |

[root, book, me] [the, morning, flight]
这里要应用的正确操作符是 RIGHTARC，它将 book 指定为 me 的中心词，并把 me 从栈中弹出，得到以下格局。

> The correct operator to apply here is RIGHTARC which assigns book as the head of me and pops me from the stack resulting in the following configuration.

> 栈 词表 关系[root, book] [the, morning, flight] (book →me)
>
> *Stack Word List Relations[root, book] [the, morning, flight] (book →me)*

在随后几次应用 SHIFT 操作符之后，第 6 步的格局如下所示：

> After several subsequent applications of the SHIFT operator, the configuration in Step 6 looks like the following:

> 栈 词表 关系
>
> *Stack Word List Relations*

> [root, book, the, morning, flight] [] (book →me)

这里，所有剩余的词语都已被传递到栈上，剩下要做的就是应用适当的归约操作符。在当前格局中，我们采用 LEFTARC 操作符，得到以下状态。

> Here, all the remaining words have been passed onto the stack and all that is left to do is to apply the appropriate reduce operators. In the current configuration, we employ the LEFTARC operator resulting in the following state.

> 栈 词表 关系
>
> *Stack Word List Relations*

> [root, book, the, flight] [] (book →me)

> (morning ←flight)

此时，该句子的句法分析结果由以下结构构成。

> At this point, the parse for this sentence consists of the following structure.

> iobj compound

Book me the morning flight (20.8)
在考察如下这类序列时，有几点重要之处需要注意

> There are several important things to note when examining sequences such as
图 20.6 中的那一个。首先，所给出的序列并不是唯一可能导出合理解析的序列。一般来说，可能存在不止一条通向相同结果的路径；并且由于歧义的存在，还可能有其他转移序列，导出不同的、但同样有效的解析。

> the one in Figure 20.6. First, the sequence given is not the only one that might lead to a reasonable parse. In general, there may be more than one path that leads to the same result, and due to ambiguity, there may be other transition sequences that lead to different equally valid parses.

其次，我们假设神谕在解析的每个时刻总是给出正确的操作符

> Second, we are assuming that the oracle always provides the correct operator
——这一假设在实践中不太可能成立。

> at each point in the parse—an assumption that is unlikely to be true in practice.

因此，鉴于该算法的贪心性质，错误的选择将导致错误的解析，因为分析器没有机会回退并尝试其他选择。20.2.4 节将介绍若干技术，使基于转移的方法能够更充分地探索搜索空间。

> As a result, given the greedy nature of this algorithm, incorrect choices will lead to incorrect parses since the parser has no opportunity to go back and pursue alternative choices. Section 20.2.4 will introduce several techniques that allow transition-based approaches to explore the search space more fully.

> 步 栈 词表 动作 添加的关系 0 [root] [book, me, the, morning, flight]
>
> *Step Stack Word List Action Relation Added 0 [root] [book, me, the, morning, flight]*

*图 20.6 基于转移的句法分析轨迹。*
*Figure 20.6 Trace of a transition-based parse.*

> SHIFT

> 1 [root, book] [me, the, morning, flight]

> SHIFT

> 2 [root, book, me] [the, morning, flight] RIGHTARC (book →me) 3 [root, book] [the, morning, flight]

> SHIFT

> 4 [root, book, the] [morning, flight]

> SHIFT

> 5 [root, book, the, morning] [flight]

> SHIFT

> 6 [root, book, the, morning, flight] [] LEFTARC (morning ←flight) 7 [root, book, the, flight] [] LEFTARC (the ←flight) 8 [root, book, flight] [] RIGHTARC (book →flight) 9 [root, book] [] RIGHTARC (root →book) 10 [root] [] Done

最后，为简单起见，我们在说明该示例时没有标注依存关系上的标签

> Finally, for simplicity, we have illustrated this example without the labels on
依存关系。为了生成带标签的依存树，我们可以用依存标签对 LEFTARC 和 RIGHTARC 操作符进行参数化，例如 LEFTARC(NSUBJ) 或 RIGHTARC(OBJ)。这相当于把转移操作符集合从最初的三个扩展为一个集合，其中对所使用的依存关系集合中的每个关系都包含相应的 LEFTARC 和 RIGHTARC 操作符，另外再加上一个用于 SHIFT 操作符。当然，这使神谕的工作变得更加困难，因为它现在可选的操作符集合大得多。

> the dependency relations. To produce labeled trees, we can parameterize the LEFT-ARC and RIGHTARC operators with dependency labels, as in LEFTARC(NSUBJ) or RIGHTARC(OBJ). This is equivalent to expanding the set of transition operators from our original set of three to a set that includes LEFTARC and RIGHTARC operators for each relation in the set of dependency relations being used, plus an additional one for the SHIFT operator. This, of course, makes the job of the oracle more difficult since it now has a much larger set of operators from which to choose.

### 20.2.1 构建神谕

> 20.2.1 Creating an Oracle

用于贪心地选择合适转移的神谕通过有监督机器学习来训练。与所有有监督机器学习方法一样，我们需要训练数据：标注了应采取的正确转移的格局。我们可以从依存树中获取这些数据。此外，我们还需要提取格局的特征。我们将介绍通过嵌入来表示格局的神经分类器，以及使用人工设计特征的经典系统。

> The oracle for greedily selecting the appropriate transition is trained by supervised machine learning. As with all supervised machine learning methods, we will need training data: configurations annotated with the correct transition to take. We can draw these from dependency trees. And we need to extract features of the configuration. We’ll introduce neural classifiers that represent the configuration via embeddings, as well as classic systems that use hand-designed features.

生成训练数据

> Generating Training Data
图 20.5 中算法所用的神谕以格局为输入，返回一个转移操作符。因此，要训练分类器，我们需要与转移操作符（即 LEFTARC、RIGHTARC 或 SHIFT）配对的格局。遗憾的是，树库提供的是整句与其对应依存树的配对，而不是格局与转移的配对。

> The oracle from the algorithm in Fig. 20.5 takes as input a configuration and returns a transition operator. Therefore, to train a classifier, we will need configurations paired with transition operators (i.e., LEFTARC, RIGHTARC, or SHIFT). Unfortunately, treebanks pair entire sentences with their corresponding trees, not configurations with transitions.

为了生成所需的训练数据，我们以一种巧妙的方式使用基于神谕的句法分析算法。我们把待分析的训练句子及其在树库中对应的参考解析一并提供给神谕。为了产生训练样本，我们随后通过运行该算法来模拟分析器的运作，并依靠一个新的训练神谕为每个

> To generate the required training data, we employ the oracle-based parsing algorithm in a clever way. We supply our oracle with the training sentences to be parsed along with their corresponding reference parses from the treebank. To produce training instances, we then simulate the operation of the parser by running the algorithm and relying on a new training oracle to give us correct transition operators for each

> `training oracle`（训练神谕）
>
> 释义：在生成训练数据时用来模拟分析器运作、为每个格局给出正确转移操作符的神谕。

后续格局给出正确的转移操作符。

> successive configuration.

要理解其运作方式，我们先回顾一下分析器的工作过程。它从

> To see how this works, let’s first review the operation of our parser. It begins with
一个默认的初始格局开始，其中栈包含 ROOT，输入列表就是词的列表，关系集合为空。LEFTARC 和 RIGHTARC 操作符各自把栈顶词之间的关系加入为给定句子累积的关系集合中。由于我们对每个训练句子都有一个黄金标准参考解析，我们知道哪些依存关系对给定句子是有效的。因此，我们可以利用参考解析来引导

> a default initial configuration where the stack contains the ROOT, the input list is just the list of words, and the set of relations is empty. The LEFTARC and RIGHTARC operators each add relations between the words at the top of the stack to the set of relations being accumulated for a given sentence. Since we have a gold-standard reference parse for each training sentence, we know which dependency relations are valid for a given sentence. Therefore, we can use the reference parse to guide the

> 步 栈 词表 预测动作 0 [root] [book, the, flight, through, houston]
>
> *Step Stack Word List Predicted Action 0 [root] [book, the, flight, through, houston]*

> SHIFT

> 1 [root, book] [the, flight, through, houston]

> SHIFT

> 2 [root, book, the] [flight, through, houston]

> SHIFT

> 3 [root, book, the, flight] [through, houston] LEFTARC 4 [root, book, flight] [through, houston]

> SHIFT

> 5 [root, book, flight, through] [houston]

> SHIFT

> 6 [root, book, flight, through, houston] [] LEFTARC 7 [root, book, flight, houston ] [] RIGHTARC 8 [root, book, flight] [] RIGHTARC 9 [root, book] [] RIGHTARC 10 [root] [] Done

*图 20.7 用给定的参考依存树模拟一次句法分析，生成由“格局／预测动作”对构成的训练样本。*
*Figure 20.7 Generating training items consisting of configuration/predicted action pairs by simulating a parse with a given reference parse.*

也就是分析器逐步走过一系列格局时对操作符的选择。

> selection of operators as the parser steps through a sequence of configurations.

更确切地说，给定一棵参考依存树和一个格局，训练

> To be more precise, given a reference parse and a configuration, the training
神谕按如下方式进行：

> oracle proceeds as follows:

- 如果 LEFTARC 在给定参考依存树和当前格局下能产生正确的中心词-依存词关系，就选择 LEFTARC；
- 否则，如果 RIGHTARC 满足以下两个条件，就选择 RIGHTARC：（1）它在给定参考依存树和当前格局下能产生正确的中心词-依存词关系，（2）栈顶词的所有依存词都已分配完毕；
- 否则，选择 SHIFT。

> Choose LEFTARC if it produces a correct head-dependent relation given the reference parse and the current configuration,
> Otherwise, choose RIGHTARC if (1) it produces a correct head-dependent relation given the reference parse and (2) all of the dependents of the word at the top of the stack have already been assigned,
> Otherwise, choose SHIFT.

之所以要对选择 RIGHTARC 操作符加以限制，是为了确保一个

> The restriction on selecting the RIGHTARC operator is needed to ensure that a
词不会在它的所有依存词都分配给它之前就被弹出栈，从而不再参与后续处理。

> word is not popped from the stack, and thus lost to further processing, before all its dependents have been assigned to it.

更形式化地说，训练期间神谕可以获取以下信息：

> More formally, during training the oracle has access to the following:

- 一个当前格局，包含栈 S 和一组依存关系 Rc
- 一棵参考依存树，由一组顶点 V 和一组依存关系 Rp 构成

> A current configuration with a stack S and a set of dependency relations Rc
> A reference parse consisting of a set of vertices V and a set of dependency relations Rp

根据这些信息，神谕按如下方式选择转移：

> Given this information, the oracle chooses transitions as follows:

LEFTARC(r): if (S1 r S2) ∈Rp RIGHTARC(r): if (S2 r S1) ∈Rp and ∀r′,w s.t.(S1 r′ w) ∈Rp then (S1 r′ w) ∈Rc SHIFT: otherwise
下面以图 20.7 所示的例子走一遍处理过程。

> Let’s walk through the processing of the following example as shown in Fig. 20.7.

> root

> obj nmod

(20.9)

> det case

Book the flight through Houston
在第 1 步的初始格局中 LEFTARC 不适用，因为它断言了一个不在参考答案中的关系 (root ←book)；RIGHTARC 确实断言了最终答案中包含的一个关系 (root →book)，但 book 尚未连接上它的任何依存词，所以只能推迟，于是 SHIFT 成为唯一可能的动作。接下来的两步条件相同。在第 3 步，选择 LEFTARC 把 the 连接到它的中心词上。

> At Step 1, LEFTARC is not applicable in the initial configuration since it asserts a relation, (root ←book), not in the reference answer; RIGHTARC does assert a relation contained in the final answer (root →book), however book has not been attached to any of its dependents yet, so we have to defer, leaving SHIFT as the only possible action. The same conditions hold in the next two steps. In step 3, LEFTARC is selected to link the to its head.

现在考察第 4 步的情形。

> Now consider the situation in Step 4.

栈 词 缓冲区 关系[root, book, flight] [through, Houston] (the ←flight)

> Stack Word buffer Relations[root, book, flight] [through, Houston] (the ←flight)
这里我们可能会忍不住在 book 与 flight 之间添加一条依存关系，因为它在参考依存树中确实存在。但此时这样做会使 Houston 之后无法连接，因为 flight 会被从栈中移除。所幸，选择 RIGHTARC 的前置条件阻止了这一选择，我们再次只剩下 SHIFT 这一可行选项。其余的选择则补全了本例所需的那组操作符。

> Here, we might be tempted to add a dependency relation between book and flight, which is present in the reference parse. But doing so now would prevent the later attachment of Houston since flight would have been removed from the stack. Fortunately, the precondition on choosing RIGHTARC prevents this choice and we’re again left with SHIFT as the only viable option. The remaining choices complete the set of operators needed for this example.

回顾一下，我们通过在参考依存树的背景下模拟分析器的运行，从树库中导出由“格局—转移”对构成的合适训练实例。在处理每个训练样本的过程中，我们可以确定性地记录每一步正确的分析器动作，从而构造出所需的训练集。

> To recap, we derive appropriate training instances consisting of configurationtransition pairs from a treebank by simulating the operation of a parser in the context of a reference dependency tree. We can deterministically record correct parser actions at each step as we progress through each training example, thereby creating the training set we require.

### 20.2.2 基于特征的分类器

> 20.2.2 A feature-based classifier

下面我们介绍两种用于选择转移的分类器：这里先讲一种经典的基于特征的算法，下一节再讲使用嵌入特征的神经分类器。

> We’ll now introduce two classifiers for choosing transitions, here a classic featurebased algorithm and in the next section a neural classifier using embedding features.

基于特征的分类器一般使用我们在词性标注和部分句法分析中见过的那些特征：词形、词元、词性、中心词，以及到中心词的依存关系。对某些语言而言，其他特征也可能有用，例如主语或宾语的格标记这类形态句法特征。这些特征从训练格局中抽取，而格局由栈、缓冲区和当前的关系集合构成。最有用的是那些引用栈顶若干层、缓冲区靠前若干词，以及与这些元素中任一元素已关联的依存关系的特征。

> Featured-based classifiers generally use the same features we’ve seen with partof-speech tagging and partial parsing: Word forms, lemmas, parts of speech, the head, and the dependency relation to the head. Other features may be relevant for some languages, for example morphosyntactic features like case marking on subjects or objects. The features are extracted from the training configurations, which consist of the stack, the buffer and the current set of relations. Most useful are features referencing the top levels of the stack, the words near the front of the buffer, and the dependency relations already associated with any of those elements.

> `feature template`（特征模板）
>
> 释义：预先定义的位置与属性组合模式，可从训练格局中自动展开为大量具体特征，供分类器判定转移时使用。

我们会像在情感分析和词性

> We’ll use a feature template as we did for sentiment analysis and part-of-speech
标注中那样使用特征模板。特征模板使我们能够从训练集中自动生成大量具体特征。例如，考察下列基于格局中单个位置的特征模板。

> tagging. Feature templates allow us to automatically generate large numbers of specific features from a training set. For example, consider the following feature templates that are based on single positions in a configuration.

⟨s1.w,op⟩,⟨s2.w,op⟩⟨s1.t,op⟩,⟨s2.t,op⟩
⟨b1.w,op⟩,⟨b1.t,op⟩⟨s1.wt,op⟩ (20.10)
这里特征记作 location.property，其中 s = 栈，b = 词

> Here features are denoted as location.property, where s = stack, b = the word
缓冲区，w = 词形，t = 词性，op = 操作符。因此，栈顶词形的特征就是 s1.w，缓冲区首词的词性标注就是 b1.t，而拼接特征 s1.wt 表示栈顶词的词形与其词性拼接在一起。下面考虑把这些模板应用于由 (20.2) 的训练神谕导出的下列中间格局。

> buffer, w = word forms, t = part-of-speech, and op = operator. Thus the feature for the word form at the top of the stack would be s1.w, the part of speech tag at the front of the buffer b1.t, and the concatenated feature s1.wt represents the word form concatenated with the part of speech of the word at the top of the stack. Consider applying these templates to the following intermediate configuration derived from a training oracle for (20.2).

栈 词 缓冲区 关系[root, canceled, flights] [to Houston] (canceled →United)

> Stack Word buffer Relations[root, canceled, flights] [to Houston] (canceled →United)
(flights →morning)(flights →the) 这里正确的转移是 SHIFT（继续往下之前你应当先说服自己确信这一点）。把我们的那组特征模板应用于该格局，会得到下列这组实例化特征。

> (flights →morning)(flights →the) The correct transition here is SHIFT (you should convince yourself of this before proceeding). The application of our set of feature templates to this configuration would result in the following set of instantiated features.

⟨s1.w = flights,op = shift⟩ (20.11)
⟨s2.w = canceled,op = shift⟩
⟨s1.t = NNS,op = shift⟩⟨s2.t = VBD,op = shift⟩⟨b1.w = to,op = shift⟩⟨b1.t = TO,op = shift⟩
⟨s1.wt = flightsNNS,op = shift⟩
鉴于左弧和右弧转移都作用于栈顶的两个元素，结合这两个位置属性的特征就更为有用。

> Given that the left and right arc transitions operate on the top two elements of the stack, features that combine properties from these positions are even more useful.

例如，诸如 s1.t ◦s2.t 这样的特征会把栈顶词的词性标注与其下方词的词性标注拼接起来。

> For example, a feature like s1.t ◦s2.t concatenates the part of speech tag of the word at the top of the stack with the tag of the word beneath it.

⟨s1.t ◦s2.t = NNSVBD,op = shift⟩ (20.12)
给定训练数据和特征，可以使用任何分类器，例如多项逻辑回归或支持向量机。

> Given the training data and features, any classifier, like multinomial logistic regression or support vector machines, can be used.

### 20.2.3 神经分类器

> 20.2.3 A neural classifier

神谕也可以由一个神经分类器来实现。一种标准架构是：将句子送入编码器，然后取栈顶 2 个词和缓冲区首个词的表示，将它们拼接后送入一个前馈网络，由该网络预测应采取的转移（Kiperwasser and Goldberg, 2016; Kulmizev et al., 2019）。图 20.8 勾勒了该模型。可以使用交叉熵损失进行学习。

> The oracle can also be implemented by a neural classifier. A standard architecture is simply to pass the sentence through an encoder, then take the presentation of the top 2 words on the stack and the first word of the buffer, concatenate them, and present to a feedforward network that predicts the transition to take (Kiperwasser and Goldberg, 2016; Kulmizev et al., 2019). Fig. 20.8 sketches this model. Learning can be done with cross-entropy loss.

![](images/20-dependency-parsing/fig_p12_0.png)

*图 20.8 用于基于转移的分析器之神谕的神经分类器。分析器取栈顶 2 个词和缓冲区首个词，用它们的编码（来自将整句送入编码器）来表示它们，拼接这些嵌入，并*
*Figure 20.8 Neural classifier for the oracle for the transition-based parser. The parser takes the top 2 words on the stack and the first word of the buffer, represents them by their encodings(from running the whole sentence through the encoder), concatenates the embeddings and*

### 20.2.4 基于转移的句法分析中的进阶方法

> 20.2.4 Advanced Methods in Transition-Based Parsing

通过解决该方法中一些最明显的缺陷，可以以多种方式对基本的基于转移的方法加以改进，从而提升性能。

> The basic transition-based approach can be elaborated in a number of ways to improve performance by addressing some of the most obvious flaws in the approach.

其他转移系统

> Alternative Transition Systems
上文描述的标准弧（arc-standard）转移系统只是众多可能的系统之一。一种常用的替代方案是弧急切（arc-eager）转移系统。弧急切

> The arc-standard transition system described above is only one of many possible systems. A frequently used alternative is the arc eager transition system. The arc eager

> `arc eager`（弧急切（arc-eager））
>
> 释义：一种基于转移的转移系统，允许词尽早挂到其中心词上，不必等到其后的依存词全部出现，以减少等待带来的错误累积。

方法之所以得名，是因为它能够比标准弧（arc-standard）方法更早地确立向右的关系。为看清这一点，让我们重新查看例 20.9 的标准弧（arc-standard）轨迹，此处重复给出。

> approach gets its name from its ability to assert rightward relations much sooner than in the arc standard approach. To see this, let’s revisit the arc standard trace of Example 20.9, repeated here.

> root

> obj nmod

> det case

Book the flight through Houston 考虑该分析中 book 与 flight 之间的依存关系。如

> Book the flight through Houston Consider the dependency relation between book and flight in this analysis. As
图 20.7 所示，标准弧（arc-standard）方法会在步骤 8 才确立这一关系，尽管 book 与 flight 早在步骤 4 就已在栈上汇合。此时无法捕获这一关系的原因在于后置名词修饰语 through Houston 的存在。在标准弧（arc-standard）方法中，依存词一旦被指派了中心词，就立即从栈中移除。如果 flight 在步骤 4 就被指派 book 为其中心词，它便不再能充当 Houston 的中心词。

> is shown in Fig. 20.7, an arc-standard approach would assert this relation at Step 8, despite the fact that book and flight first come together on the stack much earlier at Step 4. The reason this relation can’t be captured at this point is due to the presence of the postnominal modifier through Houston. In an arc-standard approach, dependents are removed from the stack as soon as they are assigned their heads. If flight had been assigned book as its head in Step 4, it would no longer be available to serve as the head of Houston.

尽管这种延迟在此例中并未造成任何问题，但一般而言，

> While this delay doesn’t cause any issues in this example, in general the longer
一个词等待被指派其中心词的时间越长，出现差错的机会就越多。弧急切（arc-eager）系统通过允许词尽早挂接到其中心词上来解决这一问题，甚至可以在依赖它们的后续词全部出现之前就完成挂接。这是通过对 LEFTARC 和 RIGHTARC 操作符做细微修改，并新增一个 REDUCE 操作符来实现的。

> a word has to wait to get assigned its head the more opportunities there are for something to go awry. The arc-eager system addresses this issue by allowing words to be attached to their heads as early as possible, before all the subsequent words dependent on them have been seen. This is accomplished through minor changes to the LEFTARC and RIGHTARC operators and the addition of a new REDUCE operator.

- LEFTARC：在输入缓冲区前端的词与栈顶的词之间确立中心词-依存词关系；弹出栈顶。
- RIGHTARC：在栈顶的词与输入缓冲区前端的词之间确立中心词-依存词关系；将输入缓冲区前端的词移到栈上。
- SHIFT：从输入缓冲区前端移除该词，并将其压入栈。
- REDUCE：弹出栈顶。

> LEFTARC: Assert a head-dependent relation between the word at the front of the input buffer and the word at the top of the stack; pop the stack.
> RIGHTARC: Assert a head-dependent relation between the word on the top of the stack and the word at the front of the input buffer; shift the word at the front of the input buffer to the stack.
> SHIFT: Remove the word from the front of the input buffer and push it onto the stack.
> REDUCE: Pop the stack.

LEFTARC 和 RIGHTARC 操作符作用于栈顶以及

> The LEFTARC and RIGHTARC operators are applied to the top of the stack and
输入缓冲区前端，而不是像标准弧（arc-standard）方法那样作用于栈顶的两个元素。RIGHTARC 操作符现在把依存词从缓冲区移到栈上，而不是将其移除，从而使其可以充当后续词的中心词。新的 REDUCE 操作符则移除栈顶元素。这些改动共同使得一个词可以被尽早指派中心词，同时仍能充当后续依存词的中心词。图 20.9 所示的轨迹说明了此例的新决策序列。

> the front of the input buffer, instead of the top two elements of the stack as in the arc-standard approach. The RIGHTARC operator now moves the dependent to the stack from the buffer rather than removing it, thus making it available to serve as the head of following words. The new REDUCE operator removes the top element from the stack. Together these changes permit a word to be eagerly assigned its head and still allow it to serve as the head for later dependents. The trace shown in Fig. 20.9 illustrates the new decision sequence for this example.

除了展示弧急切（arc-eager）转移系统之外，此例还展示了整个基于转移的方法的强大与灵活。我们能够换入一个新的转移系统，而无需对

> In addition to demonstrating the arc-eager transition system, this example demonstrates the power and flexibility of the overall transition-based approach. We were able to swap in a new transition system without having to make any changes to the

> 步骤 栈 词表 动作 新增关系 0 [root] [book, the, flight, through, houston] RIGHTARC (root →book) 1 [root, book] [the, flight, through, houston]
>
> *Step Stack Word List Action Relation Added 0 [root] [book, the, flight, through, houston] RIGHTARC (root →book) 1 [root, book] [the, flight, through, houston]*

*图 20.9 使用弧急切（arc-eager）转移操作符对 Book the flight through Houston 的处理轨迹。*
*Figure 20.9 A processing trace of Book the flight through Houston using the arc-eager transition operators.*

> SHIFT

> 2 [root, book, the] [flight, through, houston] LEFTARC (the ←flight) 3 [root, book] [flight, through, houston] RIGHTARC (book →flight) 4 [root, book, flight] [through, houston]

> SHIFT

> 5 [root, book, flight, through] [houston] LEFTARC (through ←houston) 6 [root, book, flight] [houston] RIGHTARC (flight →houston) 7 [root, book, flight, houston] []

> REDUCE

> 8 [root, book, flight] []

> REDUCE

> 9 [root, book] []

> REDUCE

> 10 [root] [] Done

底层的句法分析算法做任何改动。这种灵活性促成了多样化的转移系统的发展，它们处理句法和语义的不同方面，包括：指派词性标注（Choi and Palmer, 2011a）、允许生成非投射依存结构（Nivre, 2009）、指派语义角色（Choi and Palmer, 2011b），以及分析包含多种语言的文本（Bhat et al., 2017）。

> underlying parsing algorithm. This flexibility has led to the development of a diverse set of transition systems that address different aspects of syntax and semantics including: assigning part of speech tags (Choi and Palmer, 2011a), allowing the generation of non-projective dependency structures (Nivre, 2009), assigning semantic roles (Choi and Palmer, 2011b), and parsing texts containing multiple languages(Bhat et al., 2017).

束搜索

> Beam Search
前面讨论的基于转移的方法的计算效率源于这样一个事实：它只对句子做一遍处理，贪心地作出决策而不考虑其他备选方案。当然，这也是一个弱点——一旦作出决策就无法撤销，即使句子后面出现压倒性的证据也无济于事。我们可以使用束搜索来探索其他

> The computational efficiency of the transition-based approach discussed earlier derives from the fact that it makes a single pass through the sentence, greedily making decisions without considering alternatives. Of course, this is also a weakness – once a decision has been made it can not be undone, even in the face of overwhelming evidence arriving later in a sentence. We can use beam search to explore alternative

> `beam search`（束搜索）
>
> 释义：一种带启发式剪枝的广度优先搜索，在固定的束宽内保留若干最优候选格局。

决策序列。回想第 13 章，束搜索采用广度优先搜索策略，并用一个启发式过滤器对搜索前沿进行剪枝，使其保持在固定大小的束宽之内。

> decision sequences. Recall from Chapter 13 that beam search uses a breadth-first search strategy with a heuristic filter that prunes the search frontier to stay within a fixed-size beam width.

> `beam width`（束宽）
>
> 释义：束搜索中每一层允许保留的候选格局数量上限，用于约束搜索前沿的规模。

在把束搜索应用于基于转移的句法分析时，我们将对图 20.5 给出的算法加以扩展。我们不再在每一轮迭代中选择唯一最优的转移操作符，而是对议程上每个状态应用所有适用的操作符，然后为得到的格局打分。接着，我们把这些新格局加入前沿，前提是束内还有空间。只要议程的规模未超出指定的束宽，我们就可以向议程中加入新格局。一旦议程达到上限，我们只加入比议程上最差格局更好的新格局（同时移除最差元素，以保持在限额之内）。最后，为确保取到议程上尽可能最好的状态，只要议程上还存在非终结状态，while 循环就继续执行。

> In applying beam search to transition-based parsing, we’ll elaborate on the algorithm given in Fig. 20.5. Instead of choosing the single best transition operator at each iteration, we’ll apply all applicable operators to each state on an agenda and then score the resulting configurations. We then add each of these new configurations to the frontier, subject to the constraint that there has to be room within the beam. As long as the size of the agenda is within the specified beam width, we can add new configurations to the agenda. Once the agenda reaches the limit, we only add new configurations that are better than the worst configuration on the agenda(removing the worst element so that we stay within the limit). Finally, to insure that we retrieve the best possible state on the agenda, the while loop continues as long as there are non-final states on the agenda.

束搜索方法需要一种比我们

> The beam search approach requires a more elaborate notion of scoring than we
在贪心算法中所用的更为精细的打分概念。在贪心算法中，我们假定神谕会是一个有监督分类器，它根据当前格局的特征选择最佳的转移操作符。这一选择可以看作是为所有可能的转移赋予分数，并挑选出最好的一个。

> used with the greedy algorithm. There, we assumed that the oracle would be a supervised classifier that chose the best transition operator based on features of the current configuration. This choice can be viewed as assigning a score to all the possible transitions and picking the best one.

ˆT(c) = argmaxScore(t,c)
使用束搜索时，我们是在决策序列的空间中进行搜索，因此把格局的分数建立在其完整历史之上是合理的。于是我们可以把新格局的分数定义为其前驱格局的分数，加上产生该格局所用操作符的分数。

> With beam search we are now searching through the space of decision sequences, so it makes sense to base the score for a configuration on its entire history. So we can define the score for a new configuration as the score of its predecessor plus the score of the operator used to produce it.

ConfigScore(c0) = 0.0 ConfigScore(ci) = ConfigScore(ci−1)+Score(ti,ci−1)
该分数既用于过滤议程，也用于选择最终答案。基于转移的句法分析的束搜索新版本见图 20.10。

> This score is used both in filtering the agenda and in selecting the final answer. The new beam search version of transition-based parsing is given in Fig. 20.10.

![](images/20-dependency-parsing/fig_p15_0.png)

*图 20.10 应用于基于转移的依存句法分析的束搜索。*
*Figure 20.10 Beam search applied to transition-based dependency parsing.*

## 20.3 基于图的依存句法分析

> 20.3 Graph-Based Dependency Parsing

基于图的方法是第二类重要的依存句法分析算法。基于图的分析器比基于转移的分析器更准确，在长句上尤其如此；当中心词与依存词相距很远时，基于转移的方法会遇到困难（McDonald and Nivre, 2011）。基于图的方法通过对整棵树打分来避免这一困难，而不是依赖贪心的局部决策。此外，与基于转移的方法不同，基于图的分析器能够生成非投射的树。尽管投射性对英语而言不是重要问题，但对世界上许多语言而言确实是个问题。

> Graph-based methods are the second important family of dependency parsing algorithms. Graph-based parsers are more accurate than transition-based parsers, especially on long sentences; transition-based methods have trouble when the heads are very far from the dependents (McDonald and Nivre, 2011). Graph-based methods avoid this difficulty by scoring entire trees, rather than relying on greedy local decisions. Furthermore, unlike transition-based approaches, graph-based parsers can produce non-projective trees. Although projectivity is not a significant issue for English, it is definitely a problem for many of the world’s languages.

基于图的依存句法分析器会在所有可能的树构成的空间中搜索，为

> Graph-based dependency parsers search through the space of possible trees for a
给定句子寻找使某个分数最大化的树（或若干棵树）。这些方法把搜索空间编码为有向图，并采用图论中的方法来在该空间中搜索最优解。更形式化地说，给定一个句子 S，我们要在 Gs（该句子所有可能的树构成的空间）中寻找使某个分数最大化的最优依存树。

> given sentence for a tree (or trees) that maximize some score. These methods encode the search space as directed graphs and employ methods drawn from graph theory to search the space for optimal solutions. More formally, given a sentence S we’re looking for the best dependency tree in Gs, the space of all possible trees for that sentence, that maximizes some score.

ˆT(S) = argmax Score(t,S) 我们将做一个简化假设，即该分数可以是边因子化的，

> ˆT(S) = argmax Score(t,S) We’ll make the simplifying assumption that this score can be edge-factored,

> `edge-factored`（边因子化的）
>
> 释义：指一棵树的总体分数可以分解为构成该树的各条边的分数之和这一性质。

也就是说，一棵树的总体分数是构成该树的各条边的分数之和。

> meaning that the overall score for a tree is the sum of the scores of each of the scores of the edges that comprise the tree.

X
Score(t,S) = Score(e)
基于图的算法必须解决两个问题：（1）为

> Graph-based algorithms have to solve two problems: (1) assigning a score to
每条边赋予分数；（2）在给定所有可能边的分数的情况下找出最佳分析树。

> each edge, and (2) finding the best parse tree given the scores of all potential edges.

> e∈t

在接下来的几节中，我们将介绍这两个问题的解决方案，先从第二个问题（寻找树）开始，然后给出一种基于特征的算法和一种神经算法，用于解决第一个问题（赋予分数）。

> In the next few sections we’ll introduce solutions to these two problems, beginning with the second problem of finding trees, and then giving a feature-based and a neural algorithm for solving the first problem of assigning scores.

### 20.3.1 通过寻找最大生成树进行句法分析

> 20.3.1 Parsing via finding the maximum spanning tree

在基于图的句法分析中，给定一个句子 S，我们首先创建一个图 G，它是一个全连通、带权、有向的图，其中顶点是输入词，有向边表示所有可能的中心词-依存词指派。我们会额外加入一个 ROOT 节点，其出边指向所有其他顶点。

> In graph-based parsing, given a sentence S we start by creating a graph G which is a fully-connected, weighted, directed graph where the vertices are the input words and the directed edges represent all possible head-dependent assignments. We’ll include an additional ROOT node with outgoing edges directed at all of the other vertices.

G 中每条边的权重反映了由某种打分算法为每个可能的中心词-依存词关系赋予的分数。

> The weights of each edge in G reflect the score for each possible head-dependent relation assigned by some scoring algorithm.

事实证明，为 S 寻找最佳依存分析等价于寻找

> It turns out that finding the best dependency parse for S is equivalent to finding

> `maximum spanning tree`（最大生成树）
>
> 释义：图中分数最高的生成树；从 ROOT 出发的最大生成树即该句子的最优依存分析。

G 上的最大生成树。图 G 上的生成树是 G 的一个子集，

> the maximum spanning tree over G. A spanning tree over a graph G is a subset
它是一棵树并且覆盖 G 中的所有顶点；G 上从 ROOT 出发的生成树就是 S 的一个合法分析。最大生成树是分数最高的生成树。因此，G 上从 ROOT 出发的最大生成树就是该句子的最优依存分析。

> of G that is a tree and covers all the vertices in G; a spanning tree over G that starts from the ROOT is a valid parse of S. A maximum spanning tree is the spanning tree with the highest score. Thus a maximum spanning tree of G emanating from the ROOT is the optimal dependency parse for the sentence.

例句 Book that flight 的有向图如图 20.11 所示，其中

> A directed graph for the example Book that flight is shown in Fig. 20.11, with the
对应期望分析的最大生成树以蓝色显示。为便于阐述，这里我们描述的是无标签依存句法分析的算法。

> maximum spanning tree corresponding to the desired parse shown in blue. For ease of exposition, we’ll describe here the algorithm for unlabeled dependency parsing.

![](images/20-dependency-parsing/fig_p16_0.png)

*图 20.11 Book that flight 的初始带根有向图。*
*Figure 20.11 Initial rooted, directed graph for Book that flight.*

在描述该算法之前，先考虑关于有向图及其生成树的两个直觉是有益的。第一个直觉始于这样一个事实：生成树中的每个顶点都恰好有一条入边。由此可以推出，生成树的每个连通分量（即每一组通过边上的路径相互连接的顶点）也会有恰好一条入边。

> Before describing the algorithm it’s useful to consider two intuitions about directed graphs and their spanning trees. The first intuition begins with the fact that every vertex in a spanning tree has exactly one incoming edge. It follows from this that every connected component of a spanning tree (i.e., every set of vertices that are linked to each other by paths over edges) will also have one incoming edge.

第二个直觉是，边分数的绝对值对于确定最大生成树并不关键。起决定作用的是进入每个顶点的各条边之间的相对权重。如果我们从进入某个给定顶点的每条边中减去一个常数，那么对最大生成树的选择没有任何影响，因为每个可能的生成树都会以完全相同的量减少。

> The second intuition is that the absolute values of the edge scores are not critical to determining its maximum spanning tree. Instead, it is the relative weights of the edges entering each vertex that matters. If we were to subtract a constant amount from each edge entering a given vertex it would have no impact on the choice of the maximum spanning tree since every possible spanning tree would decrease by exactly the same amount.

算法本身的第一步相当直接。对于图中的每个顶点，

> The first step of the algorithm itself is quite straightforward. For each vertex
选择一条分数最高的入边（表示一种可能的中心词指派）。如果由此得到的边集构成一棵生成树，那么我们就完成了。更形式化地说，给定原始的完全连通图 G = (V,E)，若子图 T = (V,F) 不含环且每个顶点（根除外）都恰好有一条边进入，则它是一棵生成树。如果贪心选择过程产生了这样的树，那么它就是最优的。

> in the graph, an incoming edge (representing a possible head assignment) with the highest score is chosen. If the resulting set of edges produces a spanning tree then we’re done. More formally, given the original fully-connected graph G = (V,E), a subgraph T = (V,F) is a spanning tree if it has no cycles and each vertex (other than the root) has exactly one edge entering it. If the greedy selection process produces such a tree then it is the best possible one.

遗憾的是，这种方法并不总能得到一棵树，因为所选出的边集

> Unfortunately, this approach doesn’t always lead to a tree since the set of edges
可能包含环。幸运的是，在又一次多重发现的情形中，存在一种直接的办法来消除贪心选择阶段产生的环。Chu 和 Liu（1965）以及 Edmonds（1967）各自独立地提出了一种方法，它先进行贪心选择，随后用一个优雅的递归清理阶段来消除环。

> selected may contain cycles. Fortunately, in yet another case of multiple discovery, there is a straightforward way to eliminate cycles generated during the greedy selection phase. Chu and Liu (1965) and Edmonds (1967) independently developed an approach that begins with greedy selection and follows with an elegant recursive cleanup phase that eliminates cycles.

清理阶段首先调整图中的所有权重，做法是减去

> The cleanup phase begins by adjusting all the weights in the graph by subtracting
进入每个顶点的最大边的分数，即从所有进入该顶点的边的分数中减去该值。前面提到的直觉正是在这里发挥作用。

> the score of the maximum edge entering each vertex from the score of all the edges entering that vertex. This is where the intuitions mentioned earlier come into play.

我们对边的取值做了缩放，使得环中各边的权重不再影响任何可能生成树的权重。从进入某个顶点的每条边中减去权重最大的那条边的值，会使贪心选择阶段选中的所有边的权重变为零，其中包括环中涉及的所有边。

> We have scaled the values of the edges so that the weights of the edges in the cycle have no bearing on the weight of any of the possible spanning trees. Subtracting the value of the edge with maximum weight from each edge entering a vertex results in a weight of zero for all of the edges selected during the greedy selection phase, including all of the edges involved in the cycle.

调整权重之后，算法通过选择一条

> Having adjusted the weights, the algorithm creates a new graph by selecting a
环并将其收缩为一个新节点来创建新图。进入或离开该环的边会被修改，使它们现在进入或离开新收缩出的节点。不接触该环的边被保留，而环内部的边被丢弃。

> cycle and collapsing it into a single new node. Edges that enter or leave the cycle are altered so that they now enter or leave the newly collapsed node. Edges that do not touch the cycle are included and edges within the cycle are dropped.

现在，如果我们知道这个新图的最大生成树，我们就拥有了

> Now, if we knew the maximum spanning tree of this new graph, we would have
消除该环所需要的东西。最大生成树中指向代表被收缩环的那个顶点的边，告诉我们要消除该环应当删除哪条边。那么我们如何找到这个新图的最大生成树呢？我们对新图递归地应用该算法。其结果要么是一棵生成树，要么是一个含环的图。只要遇到环，递归就可以继续下去。当每次递归完成时，我们展开被收缩的顶点，恢复该环中的所有顶点和边，但要删除的那一条边除外。

> what we need to eliminate the cycle. The edge of the maximum spanning tree directed towards the vertex representing the collapsed cycle tells us which edge to delete in order to eliminate the cycle. How do we find the maximum spanning tree of this new graph? We recursively apply the algorithm to the new graph. This will either result in a spanning tree or a graph with a cycle. The recursions can continue as long as cycles are encountered. When each recursion completes we expand the collapsed vertex, restoring all the vertices and edges from the cycle with the exception of the single edge to be deleted.

把所有内容合在一起，最大生成树算法由以下部分组成：贪心的

> Putting all this together, the maximum spanning tree algorithm consists of greedy
边选择、边代价的重新打分，以及在需要时进行的递归清理阶段。

> edge selection, re-scoring of edge costs and a recursive cleanup phase when needed.

完整算法如图 20.12 所示。

> The full algorithm is shown in Fig. 20.12.

图 20.13 用我们的 Book that flight 例子逐步演示了该算法。

> Fig. 20.13 steps through the algorithm with our Book that flight example. The

图中第一行展示了贪心的边选择，被选中的边用蓝色表示（对应算法中的集合 F）。这导致 that 与 flight 之间出现一个环。使用进入每个节点的最大值缩放后的权重显示在右侧的图中。

> first row of the figure illustrates greedy edge selection with the edges chosen shown in blue (corresponding to the set F in the algorithm). This results in a cycle between that and flight. The scaled weights using the maximum value entering each node are shown in the graph to the right.

第二行展示了将 that 与 flight 之间的环收缩为一个节点（标记为 tf），并用新缩放后的代价进行递归。这次递归中的贪心选择步骤得到一棵把 root 连到 book 的生成树，以及一条把 book 连到被收缩节点的边。展开被收缩的节点后，我们可以看到这条边对应原图中从 book 到 flight 的边。这反过来告诉我们要消除该环应当丢弃哪条边。

> Collapsing the cycle between that and flight to a single node (labeled tf) and recursing with the newly scaled costs is shown in the second row. The greedy selection step in this recursion yields a spanning tree that links root to book, as well as an edge that links book to the contracted node. Expanding the contracted node, we can see that this edge corresponds to the edge from book to flight in the original graph. This in turn tells us which edge to drop to eliminate the cycle.

![](images/20-dependency-parsing/fig_p18_0.png)

*图 20.12　在有向加权图中寻找最大生成树的 Chu-Liu Edmonds 算法。*
*Figure 20.12 The Chu-Liu Edmonds algorithm for finding a maximum spanning tree in a weighted directed graph.*

在任意有向图上，这个版本的 CLE 算法的运行时间为 O(mn)

> On arbitrary directed graphs, this version of the CLE algorithm runs in O(mn)
，其中 m 是边的数量，n 是节点的数量。由于该算法在此处的这一特定应用首先构造一个完全连通的图 m = n2，因此运行时间为 O(n3)。Gabow 等人（1986）给出了一个更高效的实现，其运行时间为 O(m+nlogn)。

> time, where m is the number of edges and n is the number of nodes. Since this particular application of the algorithm begins by constructing a fully connected graph m = n2 yielding a running time of O(n3). Gabow et al. (1986) present a more efficient implementation with a running time of O(m+nlogn).

### 20.3.2 一种为边打分的基于特征的算法

> 20.3.2 A feature-based algorithm for assigning scores

回想一下，给定一个句子 S 和一个候选树 T，边因子化的句法分析模型做了这样的简化：树的分数等于构成该树的各条边的分数之和：

> Recall that given a sentence, S, and a candidate tree, T, edge-factored parsing models make the simplification that the score for the tree is the sum of the scores of the edges that comprise the tree:

X
score(S,T) = score(S,e)
在基于特征的算法中，我们把边的分数计算为从该边提取出的特征的加权和：

> In a feature-based algorithm we compute the edge score as a weighted sum of features extracted from it:

> e∈T

> N

X
score(S,e) = wi fi(S,e)
或者写得更简洁一些。

> Or more succinctly.

> i=1

score(S,e) = w· f
在这种表述下，我们需要确定相关的特征并训练权重。

> Given this formulation, we need to identify relevant features and train the weights.

用于训练边因子化模型的特征（以及特征组合）与训练基于转移的分析器时所用的那些特征类似，例如

> The features (and feature combinations) used to train edge-factored models mirror those used in training transition-based parsers, such as

![](images/20-dependency-parsing/fig_p19_0.png)

*图 20.13　针对 Book that flight 的 Chu-Liu-Edmonds 基于图示例*
*Figure 20.13 Chu-Liu-Edmonds graph-based example for Book that flight*

- 中心词及其依存词的词形、词元和词性。
- 这些词之前、之后以及之间的上下文所对应的特征。
- 词嵌入。
- 依存关系本身。
- 关系的方向（向右或向左）。
- 从中心词到依存词的距离。

> Wordforms, lemmas, and parts of speech of the headword and its dependent.
> Corresponding features from the contexts before, after and between the words.
> Word embeddings.
> The dependency relation itself.
> The direction of the relation (to the right or left).
> The distance from the head to the dependent.

给定一组特征之后，我们的下一个问题是学习与每个特征相对应的一组权重。与前面章节讨论的许多学习问题不同，这里我们并不是在训练模型把训练样本与类别标签或分析器动作关联起来。相反，我们要训练一个模型，使它给正确的树打出比错误的树更高的分数。对于这类问题，一个有效的框架是

> Given a set of features, our next problem is to learn a set of weights corresponding to each. Unlike many of the learning problems discussed in earlier chapters, here we are not training a model to associate training items with class labels, or parser actions. Instead, we seek to train a model that assigns higher scores to correct trees than to incorrect ones. An effective framework for problems like this is to

> `inference-based learning`（基于推理的学习）
>
> 释义：一种训练思路：先对句子做推理式分析，再按结果与参考答案的差异调整权重，而非直接学习类别标签。

采用基于推理的学习并结合感知机学习规则。在这个

> use inference-based learning combined with the perceptron learning rule. In this
框架中，我们用一组最初随机设定的初始权重对训练集中的一个句子进行分析（即执行推理）。如果得到的分析结果与训练数据中对应的树一致，我们就不改动权重。否则，我们找出错误分析结果中那些在参考分析结果里不存在的特征，并根据学习率把它们的权重略微调低。我们对训练数据中的每个句子依次增量地这样做，直到权重收敛。

> framework, we parse a sentence (i.e, perform inference) from the training set using some initially random set of initial weights. If the resulting parse matches the corresponding tree in the training data, we do nothing to the weights. Otherwise, we find those features in the incorrect parse that are not present in the reference parse and we lower their weights by a small amount based on the learning rate. We do this incrementally for each sentence in our training data until the weights converge.

### 20.3.3 一种为边打分的神经网络算法

> 20.3.3 A neural algorithm for assigning scores

最先进的基于图的多语言分析器建立在神经网络之上。这类分析器不再抽取人工设计的特征来表示词 wi 与 wj 之间的每条边，而是把句子送入一个编码器，再把 wi 和 wj 这两个词的编码表示送入一个网络，由该网络估计边 i →j 的分数。

> State-of-the-art graph-based multilingual parsers are based on neural networks. Instead of extracting hand-designed features to represent each edge between words wi and wj, these parsers run the sentence through an encoder, and then pass the encoded representation of the two words wi and wj through a network that estimates a score for the edge i →j.

![](images/20-dependency-parsing/fig_p20_0.png)

*图 20.14　Dozat 和 Manning（2017）、Dozat 等人（2017）的双仿射分析器中计算单条边（book→flight）分数的过程。该分析器使用各不相同的前馈网络，把每个词的编码器输出分别转换成该词的中心词表示和依存词表示。双仿射函数把中心词的中心嵌入与依存词的依存嵌入转换为该依存边的分数。*
*Figure 20.14 Computing scores for a single edge (book→flight) in the biaffine parser of Dozat and Manning (2017); Dozat et al. (2017). The parser uses distinct feedforward networks to turn the encoder output for each word into a head and dependent representation for the word. The biaffine function turns the head embedding of the head and the dependent embedding of the dependent into a score for the dependency edge.*

这里我们将概述 Dozat 和 Manning（2017）以及 Dozat

> Here we’ll sketch the biaffine algorithm of Dozat and Manning (2017) and Dozat
等人（2017）的算法，如图 20.14 所示，它借鉴了 Gr¨unewald 等人（2021）的工作，后者通过其 STEPS 系统测试了该算法的许多版本。该算法首先将句子 X = x1,...,xn 送入编码器，为每个词元生成上下文嵌入表示 R = r1,...,rn。每个词元的嵌入随后分别通过两个独立的前馈网络，一个用于生成该词元作为中心词的表示，另一个用于生成该词元作为依存词的表示：

> et al. (2017) shown in Fig. 20.14, drawing on the work of Gr¨unewald et al. (2021) who tested many versions of the algorithm via their STEPS system. The algorithm first runs the sentence X = x1,...,xn through an encoder to produce a contextual embedding representation for each token R = r1,...,rn. The embedding for each token is now passed through two separate feedforward networks, one to produce a representation of this token as a head, and one to produce a representation of this token as a dependent:

hhead = FFNhead(ri) (20.13)
hdep = FFNdep(ri) (20.14)
现在，为了给有向边 i →j 赋分（其中 wi 是中心词，w j 是依存词），我们将 i 的中心词表示 hhead 以及依存词的表示

> Now to assign a score to the directed edge i →j, (wi is the head and w j is the dependent), we feed the head representation of i, hhead , and the dependent representation
即 j 的 hdep，送入一个双仿射打分函数：

> of j, hdep , into a biaffine scoring function:

> i

> i

> i

> j

Score(i →j) = Biaff(hhead ,hdep
)
Biaff(x,y) = x⊺Uy +W(x⊕y)+b，其中 U、W 和 b 是模型学习到的权重。使用双仿射函数的目的，是让系统能够学习向量 x 与 y 之间的乘性交互。

> Biaff(x,y) = x⊺Uy +W(x⊕y)+b where U, W, and b are weights learned by the model. The idea of using a biaffine function is to allow the system to learn multiplicative interactions between the vectors x and y.

若将 Score(i →j) 通过 softmax，我们便得到对于每个词元 j、在其所有可能的中心词 i（句子中所有其他词元）上的一个概率分布：

> If we pass Score(i →j) through a softmax, we end up with a probability distribution, for each token j, over potential heads i (all other tokens in the sentence):

p(i →j) = softmax([Score(k →j);∀k̸ = j,1 ≤k ≤n]) (20.17)
随后可以把该概率交给第 20.3.1 节的最大生成树算法，以找出最优的树。

> This probability can then be passed to the maximum spanning tree algorithm of Section 20.3.1 to find the best tree.

该 p(i →j) 分类器通过优化交叉熵损失来训练。

> This p(i →j) classifier is trained by optimizing the cross-entropy loss.

注意，我们此前描述的该算法是无标签的。要把它变成

> Note that the algorithm as we’ve described it is unlabeled. To make this into
一个带标签的算法，Dozat 和 Manning（2017）的算法实际上训练了两个分类器。第一个分类器是边打分器，也就是我们上文描述的那个，它为每一对词 wi 和 wj 赋予概率 p(i →j)。然后运行最大生成树算法，为第二个分类器得到一棵唯一的最佳依存分析树。接着我们使用第二个分类器，即标签打分器，它的任务是为该分析树中的每条边找出概率最大的标签。第二个分类器的形式与式（20.15–20.17）相同，但它不是用二元 softmax 来预测两个词之间是否存在边的概率，而是用对依存标签的 softmax 来预测两个词之间的依存标签。

> a labeled algorithm, the Dozat and Manning (2017) algorithm actually trains two classifiers. The first classifier, the edge-scorer, the one we described above, assigns a probability p(i →j) to each word wi and wj. Then the Maximum Spanning Tree algorithm is run to get a single best dependency parse tree for the second. We then apply a second classifier, the label-scorer, whose job is to find the maximum probability label for each edge in this parse. This second classifier has the same form as (20.15-20.17), but instead of being trained to predict with binary softmax the probability of an edge existing between two words, it is trained with a softmax over dependency labels to predict the dependency label between the words.

## 20.4 评价

> 20.4 Evaluation

与基于短语结构的句法分析一样，依存句法分析器的评价是通过测量它们在测试集上的表现来进行的。一个显而易见的指标是完全匹配（exact match，EM）——即有多少句子被正确分析。该指标相当悲观，大多数句子都会被判为错误。这类度量不够细粒度，无法指导开发过程。我们的指标需要足够灵敏，以便判断是否真的取得了改进。

> As with phrase structure-based parsing, the evaluation of dependency parsers proceeds by measuring how well they work on a test set. An obvious metric would be exact match (EM)—how many sentences are parsed correctly. This metric is quite pessimistic, with most sentences being marked wrong. Such measures are not finegrained enough to guide the development process. Our metrics need to be sensitive enough to tell if actual improvements are being made.

出于这些原因，评价依存句法分析器最常用的方法

> For these reasons, the most common method for evaluating dependency parsers
是带标签和无标签的依存附着准确率。带标签附着指把一个词正确地指派到其中心词，并给出正确的依存关系。

> are labeled and unlabeled attachment accuracy. Labeled attachment refers to the proper assignment of a word to its head along with the correct dependency relation.

无标签附着只考察所指派的中心词是否正确，而忽略依存关系。给定系统输出和相应的参考分析树，准确率就是输入中被指派了正确中心词并具有正确关系的词的百分比。这些指标通常称为带标签附着分数（labeled attachment score，LAS）和无标签附着分数（unlabeled attachment score，UAS）。最后，我们还可以使用标签准确率分数（label accuracy score，LS），即标签正确的词元的百分比，不考虑这些关系来自何处。

> Unlabeled attachment simply looks at the correctness of the assigned head, ignoring the dependency relation. Given a system output and a corresponding reference parse, accuracy is simply the percentage of words in an input that are assigned the correct head with the correct relation. These metrics are usually referred to as the labeled attachment score (LAS) and unlabeled attachment score (UAS). Finally, we can make use of a label accuracy score (LS), the percentage of tokens with correct labels, ignoring where the relations are coming from.

作为一个例子，考虑下面

> As an example, consider the reference parse and system parse for the following
图 20.15 所示例子的参考分析树和系统分析树。

> example shown in Fig. 20.15.

(20.18) Book me the flight through Houston.

该系统正确找出了参考分析树中 6 个依存关系里的 4 个，得到 2/3 的 LAS。不过，系统找到的 2 个错误关系之一存在于 book 与 flight 之间，而在参考分析树中这两者处于中心词-依存词关系；因此该系统取得了 5/6 的 UAS。

> The system correctly finds 4 of the 6 dependency relations present in the reference parse and receives an LAS of 2/3. However, one of the 2 incorrect relations found by the system holds between book and flight, which are in a head-dependent relation in the reference parse; the system therefore achieves a UAS of 5/6.

除附着分数之外，我们可能还想了解一个系统在

> Beyond attachment scores, we may also be interested in how well a system is
某一类特定依存关系（例如 NSUBJ）上的表现如何，这需要在整个

> performing on a particular kind of dependency relation, for example NSUBJ, across

![](images/20-dependency-parsing/fig_p22_0.png)

*图 20.15 Book me the flight through Houston 的参考分析树与系统分析树，其 LAS 为 2/3、UAS 为 5/6。*
*Figure 20.15 Reference and system parses for Book me the flight through Houston, resulting in an LAS of 2/3 and an UAS of 5/6.*

开发语料库上进行考察。这里我们可以利用第 18 章介绍的精确率和召回率概念，测量系统标注为 NSUBJ 的关系中正确的百分比（精确率），以及开发集中实际存在的 NSUBJ 关系被系统发现的百分比（召回率）。

> a development corpus. Here we can make use of the notions of precision and recall introduced in Chapter 18, measuring the percentage of relations labeled NSUBJ by the system that were correct (precision), and the percentage of the NSUBJ relations present in the development set that were in fact discovered by the system (recall).

我们可以使用混淆矩阵来记录每种依存类型被误判为另一种类型的频次。

> We can employ a confusion matrix to keep track of how often each dependency type was confused for another.

## 20.5 小结

> 20.5 Summary

本章介绍了依存语法和依存句法分析的概念。以下是我们所涉及要点的总结：

> This chapter has introduced the concept of dependency grammars and dependency parsing. Here’s a summary of the main points that we covered:

- 在基于依存句法的句法研究方法中，句子的结构被描述为句子中词与词之间存在的一组二元关系。更大的成分概念不会直接编码在依存分析中。
- 依存结构中的关系刻画了句子中词与词之间的中心词-依存词关系。
- 基于依存的分析所提供的信息可直接用于后续的语言处理任务，包括信息抽取、语义分析和问答。
- 基于转移的分析系统采用贪心的、基于栈的算法来构建依存结构。
- 构建依存结构的基于图的方法，基于图论中的最大生成树方法。
- 基于转移和基于图的两种方法都使用有监督机器学习技术来开发。
- 树库提供了训练这些系统所需的数据。依存树库可以直接由人工标注者创建，也可以通过从短语结构树库自动转换得到。
- 依存句法分析器的评价基于在留出的开发集和测试集上测得的带标签与无标签准确率分数。

> In dependency-based approaches to syntax, the structure of a sentence is described in terms of a set of binary relations that hold between the words in a sentence. Larger notions of constituency are not directly encoded in dependency analyses.
> The relations in a dependency structure capture the head-dependent relationship among the words in a sentence.
> Dependency-based analysis provides information directly useful in further language processing tasks including information extraction, semantic parsing and question answering.
> Transition-based parsing systems employ a greedy stack-based algorithm to create dependency structures.
> Graph-based methods for creating dependency structures are based on the use of maximum spanning tree methods from graph theory.
> Both transition-based and graph-based approaches are developed using supervised machine learning techniques.
> Treebanks provide the data needed to train these systems. Dependency treebanks can be created directly by human annotators or via automatic transformation from phrase-structure treebanks.
> Evaluation of dependency parsers is based on labeled and unlabeled accuracy scores as measured against withheld development and test corpora.

## 历史注记

> Historical Notes

基于依存的语法方法远比相对晚近的短语结构或成分语法古老，后者只能追溯到 20 世纪。依存语法的历史可追溯到公元前 7 世纪至前 4 世纪之间的印度语法学家 P¯an.ini，以及古希腊的语言学传统。

> The dependency-based approach to grammar is much older than the relatively recent phrase-structure or constituency grammars, which date only to the 20th century. Dependency grammar dates back to the Indian grammarian P¯an.ini sometime between the 7th and 4th centuries BCE, as well as the ancient Greek linguistic traditions.

当代的依存语法理论都大量借鉴了 Tesnière（1959）在 20 世纪的工作。

> Contemporary theories of dependency grammar all draw heavily on the 20th century work of Tesni`ere (1959).

使用依存语法的自动句法分析，最早由 David Hays 领导的兰德公司（RAND Corporation）机器翻译早期工作引入计算语言学。这项依存句法分析工作与成分句法分析工作密切并行，并明确使用语法来指导句法分析过程。

> Automatic parsing using dependency grammars was first introduced into computational linguistics by early work on machine translation at the RAND Corporation led by David Hays. This work on dependency parsing closely paralleled work on constituent parsing and made explicit use of grammars to guide the parsing process.

在早期阶段之后，接下来几十年里依存句法分析的计算工作一直时断时续。这一时期值得注意的英语依存句法分析器实现包括 Link Grammar（Sleator 和 Temperley，1993）、Constraint Grammar（Karlsson 等人，1995）以及 MINIPAR（Lin，2003）。

> After this early period, computational work on dependency parsing remained intermittent over the following decades. Notable implementations of dependency parsers for English during this period include Link Grammar (Sleator and Temperley, 1993), Constraint Grammar (Karlsson et al., 1995), and MINIPAR (Lin, 2003).

依存句法分析在 20 世纪 90 年代末迎来了重大复兴，其标志是大型依存树库的出现，以及本章所述数据驱动方法的随之兴起。Eisner（1996）基于从宾州树库（Penn Treebank）导出的双词汇文法，开发了一种高效的依存句法分析动态规划方法。Covington（2001）提出了确定性的逐词（word by word）方法，它是当前基于转移的方法的基础。Yamada and Matsumoto（2003）以及 Kudo and Matsumoto（2002）将移进-归约（shift-reduce）范式，以及以支持向量机形式使用的有监督机器学习，一并引入了依存句法分析。

> Dependency parsing saw a major resurgence in the late 1990’s with the appearance of large dependency-based treebanks and the associated advent of data driven approaches described in this chapter. Eisner (1996) developed an efficient dynamic programming approach to dependency parsing based on bilexical grammars derived from the Penn Treebank. Covington (2001) introduced the deterministic word by word approach underlying current transition-based approaches. Yamada and Matsumoto (2003) and Kudo and Matsumoto (2002) introduced both the shift-reduce paradigm and the use of supervised machine learning in the form of support vector machines to dependency parsing.

基于转移的句法分析以移进-归约（shift-reduce）分析算法为基础，该算法最初是为分析编程语言而开发的（Aho and Ullman, 1972）。

> Transition-based parsing is based on the shift-reduce parsing algorithm originally developed for analyzing programming languages (Aho and Ullman, 1972).

移进-归约分析同样使用上下文无关文法。输入词元被依次移进栈中，栈顶的两个元素与文法规则的右部进行匹配；一旦匹配成功，被匹配的元素就在栈中被所匹配规则左部的非终结符所替换（归约）。在基于转移的依存句法分析中，我们跳过文法，并修改归约操作，以在词与其中心词之间加入一条依存关系。

> Shift-reduce parsing also makes use of a context-free grammar. Input tokens are successively shifted onto the stack and the top two elements of the stack are matched against the right-hand side of the rules in the grammar; when a match is found the matched elements are replaced on the stack (reduced) by the non-terminal from the left-hand side of the rule being matched. In transition-based dependency parsing we skip the grammar, and alter the reduce operation to add a dependency relation between a word and its head.

Nivre（2003）定义了现代、确定性、基于转移的依存句法分析方法。

> Nivre (2003) defined the modern, deterministic, transition-based approach to

Nivre 及其同事的后续工作对众多转移系统、训练方法以及处理非投射语言的方法进行了形式化与性能分析（Nivre and Scholz 2004, Nivre 2006, Nivre and Nilsson 2005, Nivre et al. 2007b, Nivre 2007）。神经方法由 Chen and Manning（2014）开创，并由 Kiperwasser and Goldberg（2016）和 Kulmizev et al.（2019）加以拓展。

> dependency parsing. Subsequent work by Nivre and his colleagues formalized and analyzed the performance of numerous transition systems, training methods, and methods for dealing with non-projective language (Nivre and Scholz 2004, Nivre 2006, Nivre and Nilsson 2005, Nivre et al. 2007b, Nivre 2007). The neural approach was pioneered by Chen and Manning (2014) and extended by Kiperwasser and Goldberg (2016); Kulmizev et al. (2019).

基于图的最大生成树依存句法分析方法由 McDonald et al. 2005a、McDonald et al. 2005b 提出。

> The graph-based maximum spanning tree approach to dependency parsing was

神经分类器由（Kiperwasser and Goldberg, 2016）提出。

> introduced by McDonald et al. 2005a, McDonald et al. 2005b. The neural classifier was introduced by (Kiperwasser and Goldberg, 2016).

长期运行的布拉格依存树库项目（Hajiˇc, 1998）是规模最大的、

> The long-running Prague Dependency Treebank project (Hajiˇc, 1998) is the most
旨在直接为语料标注多层形态、句法和语义信息的努力。PDT 3.0 包含超过 150 万个词元（Bejˇcek et al., 2013）。

> significant effort to directly annotate a corpus with multiple layers of morphological, syntactic and semantic information. PDT 3.0 contains over 1.5 M tokens (Bejˇcek et al., 2013).

通用依存（Universal Dependencies，UD）（de Marneffe et al., 2021）是一个开放的社区项目，旨在为依存树库标注建立一套框架，涵盖 100 多种语言中近 200 个树库。UD 标注方案由若干各自独立的努力演化而来，包括斯坦福依存（Stanford dependencies）（de Marneffe et al. 2006, de Marneffe and Manning 2008, de Marneffe et al. 2014）、Google 的通用词性标注（Petrov et al., 2012）以及面向形态句法标签集的 Interset 中间语言（interlingua）（Zeman, 2008）。

> Universal Dependencies (UD) (de Marneffe et al., 2021) is an open community project to create a framework for dependency treebank annotation, with nearly 200 treebanks in over 100 languages. The UD annotation scheme evolved out of several distinct efforts including Stanford dependencies (de Marneffe et al. 2006, de Marneffe and Manning 2008, de Marneffe et al. 2014), Google’s universal part-of-speech tags (Petrov et al., 2012), and the Interset interlingua for morphosyntactic tagsets(Zeman, 2008).

自然语言学习会议（Conference on Natural Language Learning，CoNLL）多年来开展了一系列与依存句法分析相关的、颇具影响力的共享任务（Buchholz and Marsi 2006, Nivre et al. 2007a, Surdeanu et al. 2008, Hajiˇc et al. 2009）。

> The Conference on Natural Language Learning (CoNLL) has conducted an influential series of shared tasks related to dependency parsing over the years (Buchholz and Marsi 2006, Nivre et al. 2007a, Surdeanu et al. 2008, Hajiˇc et al. 2009).

较晚近的评价则关注分析器的鲁棒性，一方面针对形态丰富的语言（Seddah et al., 2013），另一方面针对社交媒体、文本和口语等非规范的语言形式（Petrov and McDonald, 2012）。

> More recent evaluations have focused on parser robustness with respect to morphologically rich languages (Seddah et al., 2013), and non-canonical language forms such as social media, texts, and spoken language (Petrov and McDonald, 2012).

Choi et al.（2015）给出了一项针对 10 个依存句法分析器、覆盖多项指标的性能分析，以及一个稳健的分析器评价工具 DEPENDABLE。

> Choi et al. (2015) presents a performance analysis of 10 dependency parsers across a range of metrics, as well as DEPENDABLE, a robust parser evaluation tool.

## 练习

> Exercises
