# 第 19 章 上下文无关文法与成分句法分析

### 章

> CHAPTER

# 19 上下文无关文法与成分句法分析

> 19 Context-Free Grammars and Constituency Parsing

Bruce Springsteen 与 Patti Smith 的《Because the Night》，James Baldwin 的《The Fire Next Time》，Italo Calvino 的《If on a winter’s night a traveler》，Richard Curtis 的《Love Actually》，Tennessee Williams 的《Suddenly Last Summer》，Philip K. Dick 的《A Scanner Darkly》

> Because the Night by Bruce Springsteen and Patti Smith The Fire Next Time by James Baldwin If on a winter’s night a traveler by Italo Calvino Love Actually by Richard Curtis Suddenly Last Summer by Tennessee Williams A Scanner Darkly by Philip K. Dick
一天早上我穿着睡衣射中了一头大象。它是怎么钻进我的睡衣里的，我可不知道。

> One morning I shot an elephant in my pajamas. How he got into my pajamas I don’t know.

> 六个不是成分的标题，出自 Geoffrey K. Pullum 在 Language Log 上的文章（他指出这类标题极为罕见）。
>
> *Six titles that are not constituents, from Geoffrey K. Pullum on Language Log (who was pointing out their incredible rarity).*

> Groucho Marx，《Animal Crackers》，1930
>
> *Groucho Marx, Animal Crackers, 1930*

对语法的研究有着古老的渊源。梵语的语法是

> The study of grammar has an ancient pedigree. The grammar of Sanskrit was
由印度语法学家 P¯an.ini 在公元前 7 世纪至前 4 世纪之间的某个时候，在其著名论著 As.t.¯adhy¯ay¯ı（「8 卷」）中加以描述。而我们的单词 syntax

> described by the Indian grammarian P¯an.ini sometime between the 7th and 4th centuries BCE, in his famous treatise the As.t.¯adhy¯ay¯ı (‘8 books’). And our word syntax

> `syntax`（句法）
>
> 释义：指词在句子中组合排列的方式，即研究词语如何组成短语与句子的结构规律。

源自希腊语 sýntaxis，意为「摆放在一起或排列」，指词组合在一起的方式。我们在前面几章已经见过句法概念，例如词性类别的使用（第 18 章）。本章与下一章将介绍用于刻画更精细的语法结构概念的形式化模型，以及分析这些结构的算法。

> comes from the Greek s´yntaxis, meaning “setting out together or arrangement”, and refers to the way words are arranged together. We have seen syntactic notions in previous chapters like the use of part-of-speech categories (Chapter 18). In this chapter and the next one we introduce formal models for capturing more sophisticated notions of grammatical structure and algorithms for parsing these structures.

本章的重点是上下文无关文法与 CKY 算法

> Our focus in this chapter is context-free grammars and the CKY algorithm
用于分析它们。上下文无关文法是自然语言句法（以及就此而言，计算机语言句法）的许多形式化模型的主干。

> for parsing them. Context-free grammars are the backbone of many formal models of the syntax of natural language (and, for that matter, of computer languages).

句法分析的任务是为句子赋予句法结构。解析树（无论是上下文无关文法的解析树，还是后面几章介绍的依存或 CCG 形式体系的解析树）可用于语法检查之类的应用：无法被分析的句子可能存在语法错误（或者至少难以阅读）。解析树可以作为形式语义分析的中间表示阶段。而分析器及其为句子赋予的语法结构，对于那些需要刻画句子中各元素之间关系的文本数据科学应用来说，是一种有用的文本分析工具。

> Syntactic parsing is the task of assigning a syntactic structure to a sentence. Parse trees (whether for context-free grammars or for the dependency or CCG formalisms we introduce in following chapters) can be used in applications such as grammar checking: sentence that cannot be parsed may have grammatical errors (or at least be hard to read). Parse trees can be an intermediate stage of representation for formal semantic analysis. And parsers and the grammatical structure they assign a sentence are a useful text analysis tool for text data science applications that require modeling the relationship of elements in sentences.

本章介绍上下文无关文法，给出一个英语的小型示例文法，介绍上下文无关文法与文法范式的更正式定义，并讨论树库：即用句法结构标注过的语料库。接着我们讨论分析歧义及其带来的问题，然后转入分析本身，给出著名的 Cocke-Kasami-Younger（CKY）算法（Kasami 1965，Younger 1967），这是句法分析的标准动态规划方法。CKY 算法返回一个句子全部解析树集合的高效表示，但并不会告诉我们哪一棵解析树才是正确的。为此，我们需要为每个可能的成分给 CKY 附加得分。我们将看到如何用基于跨度的神经分析器做到这一点。最后，我们将介绍评估分析器准确率的标准指标集。

> In this chapter we introduce context-free grammars, give a small sample grammar of English, introduce more formal definitions of context-free grammars and grammar normal form, and talk about treebanks: corpora that have been annotated with syntactic structure. We then discuss parse ambiguity and the problems it presents, and turn to parsing itself, giving the famous Cocke-Kasami-Younger(CKY) algorithm (Kasami 1965, Younger 1967), the standard dynamic programming approach to syntactic parsing. The CKY algorithm returns an efficient representation of the set of parse trees for a sentence, but doesn’t tell us which parse tree is the right one. For that, we need to augment CKY with scores for each possible constituent. We’ll see how to do this with neural span-based parsers. Finally, we’ll introduce the standard set of metrics for evaluating parser accuracy.

## 19.1 成分

> 19.1 Constituency

句法成分这一观念指的是：若干词的组合可以像单个单位一样起作用，这样的单位称为成分。构建文法的一部分工作，就是建立该语言中成分的清单。英语中词是如何组合在一起的？请看名词短语，即围绕至少一个名词的一串词。下面是

> Syntactic constituency is the idea that groups of words can behave as single units, or constituents. Part of developing a grammar involves building an inventory of the constituents in the language. How do words group together in English? Consider the noun phrase, a sequence of words surrounding at least one noun. Here are some

> `noun phrase`（名词短语）
>
> 释义：围绕至少一个名词组成、在句子中像一个单位那样充当成分的一串词。

一些名词短语的例子（感谢 Damon Runyon）：

> examples of noun phrases (thanks to Damon Runyon):

| Harry the Horse | a high-class spot such as Mindy’s |
| --- | --- |
| the Broadway coppers | the reason he comes into the Hot Box |
| they | three parties from Brooklyn |

我们有什么证据表明这些词组合在一起（或者说「构成成分」）？

> What evidence do we have that these words group together (or “form constituents”)?

一个证据是：它们都能出现在相似的句法环境中，例如出现在动词之前。

> One piece of evidence is that they can all appear in similar syntactic environments, for example, before a verb.

three parties from Brooklyn arrive... a high-class spot such as Mindy’s attracts... the Broadway coppers love... they sit
但是，虽然整个名词短语可以出现在动词之前，对其中

> But while the whole noun phrase can occur before a verb, this is not true of each
组成名词短语的每一个词来说却并非如此。下面这些都不是合乎语法的英语句子（回想一下，我们用星号（*）标记不合乎语法的英语片段）：

> of the individual words that make up a noun phrase. The following are not grammatical sentences of English (recall that we use an asterisk (*) to mark fragments that are not grammatical English sentences):

*from arrive... *as attracts...

| *from arrive... | *as attracts... |
| --- | --- |
| *the is... | *spot sat... |

因此，要正确描述英语中这些词排列顺序的事实，我们必须能够说出诸如「名词短语可以出现在动词之前」这样的话。现在我们来看看如何以更形式化的方式做到这一点！

> Thus, to correctly describe facts about the ordering of these words in English, we must be able to say things like “Noun Phrases can occur before verbs”. Let’s now see how to do this in a more formal way!

## 19.2 上下文无关文法

> 19.2 Context-Free Grammars

用于对自然语言中的成分结构建模的一种广泛使用的形式系统是上下文无关文法，即 CFG。上下文无关文法也称为

> A widely used formal system for modeling constituent structure in natural language is the context-free grammar, or CFG. Context-free grammars are also called

> `CFG`（上下文无关文法）
>
> 释义：由一组规则与一个词库构成的形式文法，每条规则的左部都是单个非终结符。

短语结构文法，这一形式体系等价于巴科斯范式（BNF）。把文法建立在成分结构之上的思想可追溯到心理学家 Wilhelm Wundt（1900），但直到 Chomsky（1956）以及独立地由 Backus（1959）提出时才被形式化。

> phrase-structure grammars, and the formalism is equivalent to Backus-Naur form, or BNF. The idea of basing a grammar on constituent structure dates back to the psychologist Wilhelm Wundt (1900) but was not formalized until Chomsky (1956) and, independently, Backus (1959).

一个上下文无关文法由一组规则或产生式构成，其中每一条

> A context-free grammar consists of a set of rules or productions, each of which

> `rules`（规则）
>
> 释义：形如 A → β 的重写式，表示左侧的单个非终结符可以展开为右侧的符号序列。

表达了该语言的符号可以被组合和排序的方式，此外还包含一个由词与符号构成的词库。例如，下面的产生式

> expresses the ways that symbols of the language can be grouped and ordered together, and a lexicon of words and symbols. For example, the following productions

> `lexicon`（词库）
>
> 释义：文法中与句法规则分开列出的词表，给出每个词所属的词性标记。

表达了 NP（即名词短语）既可以由一个 ProperNoun（专有名词）构成，也可以由

> express that an NP (or noun phrase) can be composed of either a ProperNoun or

> `NP`（名词短语）
>
> 释义：NP 即 noun phrase（名词短语），是以名词为中心词构成的短语，既可充当句子主语、宾语等成分，也可以由专有名词或“限定词 + Nominal”构成。

一个限定词（Det）后接一个 Nominal 构成；而 Nominal 又可以由一个或多个 Noun 构成。1 NP →Det Nominal NP →ProperNoun Nominal →Noun | Nominal Noun

> a determiner (Det) followed by a Nominal; a Nominal in turn can consist of one or more Nouns.1 NP →Det Nominal NP →ProperNoun Nominal →Noun | Nominal Noun
上下文无关规则可以分层嵌套，因此我们可以把前面的规则与其他规则组合起来，例如下面这些表达词库事实的规则：

> Context-free rules can be hierarchically embedded, so we can combine the previous rules with others, like the following, that express facts about the lexicon:

Det →a Det →the Noun →flight
CFG 中使用的符号分为两类。与语言中的词（「the」「nightclub」）相对应的符号称为终结符

> The symbols that are used in a CFG are divided into two classes. The symbols that correspond to words in the language (“the”, “nightclub”) are called terminal

> `terminal`（终结符）
>
> 释义：直接对应词库中某个词、不再由规则进一步展开的符号，如 the、flight。

符号；词库就是引入这些终结符的规则集合。对这些终结符作抽象表达所用的符号称为非终结符。在

> symbols; the lexicon is the set of rules that introduce these terminal symbols. The symbols that express abstractions over these terminals are called non-terminals. In

> `non-terminal`（非终结符）
>
> 释义：文法中可被一组终结符或非终结符展开的符号，如 S、NP、VP，用于表达语言中的抽象范畴。

在每条上下文无关规则中，箭头（→）右侧的项是一个或多个终结符与非终结符构成的有序列表；箭头左侧则是一个单一的非终结符符号，表达某种聚类或概括。词库中与每个词相关联的非终结符，就是该词的词汇范畴，即词性。

> each context-free rule, the item to the right of the arrow (→) is an ordered list of one or more terminals and non-terminals; to the left of the arrow is a single non-terminal symbol expressing some cluster or generalization. The non-terminal associated with each word in the lexicon is its lexical category, or part of speech.

CFG 可以从两个角度来理解：一是作为生成句子的装置，

> A CFG can be thought of in two ways: as a device for generating sentences
二是作为为给定句子指派结构的装置。把 CFG 看作生成器时，我们可以把箭头 → 读作“用右侧的符号串改写左侧的符号”。

> and as a device for assigning a structure to a given sentence. Viewing a CFG as a generator, we can read the →arrow as “rewrite the symbol on the left with the string of symbols on the right”.

因此，从符号 NP 出发，我们可以用第一条规则把 NP 改写为 Det Nominal，然后把 Nominal 改写为 Noun，最后把这些词性改写为：a flight

> So starting from the symbol: NP we can use our first rule to rewrite NP as: Det Nominal and then rewrite Nominal as: Noun and finally rewrite these parts-of-speech as: a flight
我们说符号串 a flight 可以由非终结符 NP 推导出。因此，一个 CFG

> We say the string a flight can be derived from the non-terminal NP. Thus, a CFG
可以用来生成一个符号串集合。这一系列规则展开称为该词串的推导。人们通常用解析树来表示推导，

> can be used to generate a set of strings. This sequence of rule expansions is called a derivation of the string of words. It is common to represent a derivation by a parse

> `derivation parse tree`（推导解析树）
>
> 释义：记录从起始符号出发、逐步应用规则展开为词串这一过程的树形表示，叶结点为终结符，内部结点为非终结符。

树（通常倒置绘制，根位于顶部）。图 19.1 给出了这一推导的树

> tree (commonly shown inverted with the root at the top). Figure 19.1 shows the tree
表示。

> representation of this derivation.

![](images/19-cfg-and-parsing/fig_p3_0.png)

*图 19.1 “a flight”的解析树。*
*Figure 19.1 A parse tree for “a flight”.*

在图 19.1 所示的解析树中，我们可以说结点 NP 支配

> In the parse tree shown in Fig. 19.1, we can say that the node NP dominates

> `dominates`（支配）
>
> 释义：解析树中一个结点位于另一个结点之上、且两者之间由路径相连的层级关系。

树中的所有结点（Det、Nom、Noun、a、flight）。我们还可以说，它直接支配结点 Det 和 Nom。

> all the nodes in the tree (Det, Nom, Noun, a, flight). We can say further that it immediately dominates the nodes Det and Nom.

由 CFG 定义的形式语言，是那些可推导出的符号串的集合，

> The formal language defined by a CFG is the set of strings that are derivable
它们由指定的起始符号推导而来。每个文法都必须有一个指定的起始符号，它通常被称为 S。由于上下文无关文法常用来定义句子，S 通常被解释为“句子”结点，而由 S 推导出的符号串集合，就是某种简化版英语中的句子集合。

> from the designated start symbol. Each grammar must have one designated start symbol, which is often called S. Since context-free grammars are often used to define sentences, S is usually interpreted as the “sentence” node, and the set of strings that are derivable from S is the set of sentences in some simplified version of English.

> `start symbol`（起始符号）
>
> 释义：文法中作为推导起点的那个非终结符，通常记为 S，语言即由它推导出的全部串构成。

让我们再往规则清单中添加几条规则。下面这条规则表达了

> Let’s add a few additional rules to our inventory. The following rule expresses
这样一个事实：句子可以由一个名词短语后接一个动词短语构成：

> the fact that a sentence can consist of a noun phrase followed by a verb phrase:

> `verb phrase`（动词短语）
>
> 释义：以动词为中心、可后接名词短语或介词短语等成分的短语，如 prefer a morning flight。

S →NP VP I prefer a morning flight
英语中的动词短语由一个动词后接各式其他成分构成；

> A verb phrase in English consists of a verb followed by assorted other things;

例如，有一类动词短语由一个动词后接一个名词短语构成：

> for example, one kind of verb phrase consists of a verb followed by a noun phrase:

VP →Verb NP prefer a morning flight
或者动词后面可以接一个名词短语和一个介词短语：

> Or the verb may be followed by a noun phrase and a prepositional phrase:

VP →Verb NP PP leave Boston in the morning
或者动词短语也可以只由一个动词后接一个介词短语构成：

> Or the verb phrase may have a verb followed by a prepositional phrase alone:

VP →Verb PP leaving on Thursday
介词短语通常由一个介词后接一个名词短语构成。

> A prepositional phrase generally has a preposition followed by a noun phrase.

例如，ATIS 语料库中常见的一类介词短语用来表示地点或方向：

> For example, a common type of prepositional phrase in the ATIS corpus is used to indicate location or direction:

PP →Preposition NP from Los Angeles
介词短语内部的 NP 不一定表示地点；介词短语也常与时间和

> The NP inside a PP need not be a location; PPs are often used with times and
日期连用，也可以与其他名词连用；它们可以任意复杂。下面是 ATIS 语料库中的十个例子：

> dates, and with other nouns as well; they can be arbitrarily complex. Here are ten examples from the ATIS corpus:

| to Seattle | on these flights |
| --- | --- |
| in Minneapolis | about the ground transportation in Chicago |
| on Wednesday | of the round trip flight on United Airlines |
| in the evening | of the AP fifty seven flight |
| on the ninth of July | with a stopover in Nashville |

图 19.2 给出了一个示例词库，图 19.3 汇总了文法规则

> Figure 19.2 gives a sample lexicon, and Fig. 19.3 summarizes the grammar rules
即我们目前所见的这些规则，我们称之为 L0。注意，我们可以用或符号 | 来表示一个非终结符有多种可能的展开。

> we’ve seen so far, which we’ll call L0. Note that we can use the or-symbol | to indicate that a non-terminal has alternate possible expansions.

<!--figbox-->
> Noun →flights | flight | breeze | trip | morning Verb →is | prefer | like | need | want | fly | do

> Adjective →cheapest | non-stop | first | latest

> | other | direct

> Pronoun →me | I | you | it

> Proper-Noun →Alaska | Baltimore | Los Angeles

> | Chicago | United | American

> Determiner →the | a | an | this | these | that Preposition →from | to | on | near | in Conjunction →and | or | but
<!--/figbox-->

*图 19.2 L0 的词库。*
*Figure 19.2 The lexicon for L0.*

我们可以用这个文法生成这种“ATIS 语言”的句子。我们

> We can use this grammar to generate sentences of this “ATIS-language”. We
从 S 开始，把它展开为 NP VP，然后随机选择 NP 的一个展开（比如展开为

> start with S, expand it to NP VP, then choose a random expansion of NP (let’s say, to

<!--figbox-->
> 文法  规则  示例
>
> *Grammar Rules Examples*

> S →NP VP I + want a morning flight

> NP →Pronoun I

> | Proper-Noun Los Angeles| Det Nominal a + flight

> Nominal →Nominal Noun morning + flight

> | Noun flights

> VP →Verb do

> | Verb NP want + a flight| Verb NP PP leave + Boston + in the morning| Verb PP leaving + on Thursday

> PP →Preposition NP from + Los Angeles
<!--/figbox-->

*图 19.3 L0 的文法，每条规则都附有示例短语。*
*Figure 19.3 The grammar for L0, with example phrases for each rule.*

![](images/19-cfg-and-parsing/fig_p5_0.png)

*图 19.4 依据文法 L0 得到的 “I prefer a morning flight” 的解析树。*
*Figure 19.4 The parse tree for “I prefer a morning flight” according to grammar L0.*

I），再随机展开 VP（比如展开为 Verb NP），如此继续，直到生成字符串 I prefer a morning flight。图 19.4 给出一棵解析树，它表示 I prefer a morning flight 的一次完整推导。

> I), and a random expansion of VP (let’s say, to Verb NP), and so on until we generate the string I prefer a morning flight. Figure 19.4 shows a parse tree that represents a complete derivation of I prefer a morning flight.

我们还可以用一种更紧凑的格式来表示解析树，这种格式称为括号标注的

> We can also represent a parse tree in a more compact format called bracketed

> `bracketed`（括号标注的）
>
> 释义：指用成对的中括号标出句中每个句法成分及其覆盖范围的书写方式。

记法；下面是图 19.4 中解析树的括号标注表示：

> notation; here is the bracketed representation of the parse tree of Fig. 19.4:

> `notation`（记法）
>
> 释义：把句子的成分结构用嵌套中括号写成一串符号的书写方式，如 [S [NP ...] [VP ...]]。

> (19.1) [S [NP [Pro I]] [VP [V prefer] [NP [Det a] [Nom [Nom [N morning]] [N flight]]]]]]

像 L0 这样的 CFG 定义了一种形式语言。句子（词的串）

> A CFG like that of L0 defines a formal language. Sentences (strings of words)
凡能由某个文法推导出来的句子（词的串），都属于该文法所定义的形式语言，称为合乎语法的句子。凡是不能由

> that can be derived by a grammar are in the formal language defined by that grammar, and are called grammatical sentences. Sentences that cannot be derived by

> `grammatical`（合乎语法的）
>
> 释义：指能由给定文法推导出来、因而属于该文法所定义形式语言的句子。

给定形式文法推导出来的句子，则不属于该文法所定义的语言，称为不合语法的。这种“在内”与“在外”之间泾渭分明的界线，是

> a given formal grammar are not in the language defined by that grammar and are referred to as ungrammatical. This hard line between “in” and “out” characterizes

> `ungrammatical`（不合语法的）
>
> 释义：指无法由给定形式文法推导出来、因而不属于该文法所定义语言的句子。

所有形式语言共有的特点，但它只是对自然语言实际运作方式的一种极为简化的模型。这是因为要判定某个句子是否属于某种自然语言（比如英语），往往取决于语境。在语言学中，用

> all formal languages but is only a very simplified model of how natural languages really work. This is because determining whether a given sentence is part of a given natural language (say, English) often depends on the context. In linguistics, the use

> `generative`（生成的）
>
> 释义：指用形式文法来定义语言、把语言看作由文法生成的全部句子之集合的研究取向。

形式语言来为自然语言建模的做法称为生成文法，因为

> of formal languages to model natural languages is called generative grammar since

> `grammar`（文法）
>
> 释义：这里指一套定义形式语言的规则，用以规定哪些词串属于该语言。

语言是由该文法等“生成”的全部可能句子所构成的集合来定义的。（注意，这里的“生成”与我们说语言模型生成文本时的“生成”含义不同。）

> the language is defined by the set of possible sentences “generated” by the grammar.(Note that this is a different sense of the word ‘generate’ than when we talk about language models generating text.)

### 19.2.1 上下文无关文法的形式定义

> 19.2.1 Formal Definition of Context-Free Grammar

本节最后，我们简要给出上下文无关文法及其所生成语言的形式描述。一个上下文无关文法 G 由四个参数定义：N、Σ、R、S（严格说，它是一个“四元组”）。

> We conclude this section with a quick, formal description of a context-free grammar and the language it generates. A context-free grammar G is defined by four parameters: N, Σ, R, S (technically it is a “4-tuple”).

N 非终结符（或称变量）的集合 Σ 终结符的集合（与 N 不相交） R 规则或产生式的集合，每条形如 A →β ，

> N a set of non-terminal symbols (or variables)Σ a set of terminal symbols (disjoint from N) R a set of rules or productions, each of the form A →β ,

| N | 非终结符（或称变量）的集合<br>a set of non-terminal symbols (or variables) |
| --- | --- |
| Σ | 终结符的集合（与 N 不相交）<br>a set of terminal symbols (disjoint from N) |
| R | 规则或产生式的集合，每条形如 A →β ，<br>a set of rules or productions, each of the form A →β , |
|  | 其中 A 是非终结符，<br>where A is a non-terminal, |
|  | β 是取自无限字符串集合 (Σ∪N)∗ 的一个符号串<br>β is a string of symbols from the infinite set of strings (Σ∪N)∗ |
| S | 指定的起始符号，且是 N 的一个成员<br>a designated start symbol and a member of N |

在本书余下的部分中，当我们讨论上下文无关文法的形式性质时（而不是在解释关于英语或其他语言的特定事实时），都遵循以下约定。

> For the remainder of the book we adhere to the following conventions when discussing the formal properties of context-free grammars (as opposed to explaining particular facts about English or other languages).

<!--figbox-->
> 大写字母如 A、B、S 表示非终结符
>
> *Capital letters like A, B, and S Non-terminals*

> S 起始符号 小写希腊字母如 α、β、γ 取自 (Σ∪N)∗ 的串 小写罗马字母如 u、v、w 终结符组成的串
>
> *S The start symbol Lower-case Greek letters like α, β, and γ Strings drawn from (Σ∪N)∗Lower-case Roman letters like u, v, and w Strings of terminals*
<!--/figbox-->

语言是通过推导这一概念来定义的。若一个串能经由若干次规则应用被改写为另一个串，则称前者推导出后者。

> A language is defined through the concept of derivation. One string derives another one if it can be rewritten as the second one by some series of rule applications.

更形式化地说，依据 Hopcroft 和 Ullman（1979），

> More formally, following Hopcroft and Ullman (1979),
若 A →β 是 R 的一条产生式，且 α 与 γ 是集合 (Σ∪N)∗ 中的任意串，则我们说 αAγ 直接推导出 αβγ，或记作 αAγ ⇒αβγ。

> if A →β is a production of R and α and γ are any strings in the set(Σ∪N)∗, then we say that αAγ directly derives αβγ, or αAγ ⇒αβγ.

> `directly derives`（直接推导出）
>
> 释义：单次应用一条产生式，把一个符号串改写为另一符号串的推导关系。

推导则是直接推导的推广：

> Derivation is then a generalization of direct derivation:

设 α1, α2, ..., αm 是 (Σ∪N)∗ 中的串，m ≥1，使得

> Let α1, α2, ..., αm be strings in (Σ∪N)∗,m ≥1, such that

$$α_{1}⇒α_{2},α_{2}⇒α_{3},...,α_{m-1}⇒α_{m}$$

我们说 α1 推导出 αm，或记作 α1 ∗⇒αm。

> We say that α1 derives αm, or α1 ∗⇒αm.

> `derives`（推导出）
>
> 释义：经一步或多步直接推导，由一个符号串得到另一个符号串的关系。

于是我们可以形式化地定义由文法 G 生成的语言 LG 为

> We can then formally define the language LG generated by a grammar G as the
由终结符组成、且可由指定的起始符号 S 推导出的串的集合。

> set of strings composed of terminal symbols that can be derived from the designated start symbol S.

$$L_{G}=\{w|w\text{is in}Σ^{\ast}\text{and}S⇒^{\ast}w\}$$

从词串映射到其解析树的问题称为句法分析，我们将在 19.6 节中看到。

> The problem of mapping from a string of words to its parse tree is called syntactic parsing, as we’ll see in Section 19.6.

> `syntactic`（句法的）
>
> 释义：与句子成分结构有关的；此处指用来在多个分析中做出选择的句法信息。

> `parsing`（句法分析）
>
> 释义：为输入词串指派句法结构（如解析树）的过程。

## 19.3 树库

> 19.3 Treebanks

其中每个句子都标注了解析树的语料库称为树库。

> A corpus in which every sentence is annotated with a parse tree is called a treebank.

> `treebank`（树库）
>
> 释义：用句法结构（解析树）标注过的语料库，其中的句子隐含地构成该语言的一部文法，为句法分析提供带结构标注的数据。

树库在句法分析中，以及在句法现象的语言学研究中，都起着重要作用。

> Treebanks play an important role in parsing as well as in linguistic investigations of syntactic phenomena.

树库通常是这样制作的：先用分析器处理每个句子，然后

> Treebanks are generally made by running a parser over each sentence and then
由人类语言学家对得到的分析结果进行人工校正。图 19.5 展示了来自宾州树库项目的句子，该项目包含多种语言的树库，涉及

> having the resulting parse hand-corrected by human linguists. Figure 19.5 shows sentences from the Penn Treebank project, which includes various treebanks in

> `Penn Treebank`（宾州树库（Penn Treebank））
>
> 释义：涵盖英语、阿拉伯语、汉语等的句法标注语料库，为句法分析与评测提供带解析树的数据。

英语、阿拉伯语和汉语。宾州树库的词性标注集已在第 18 章定义，但我们会看到各树库之间存在细微的格式差异。用 LISP 风格的括号记法表示树极为常见，它类似于我们先前在（19.1）中见到的括号记法。对于不熟悉这种记法的读者，我们在图 19.6 中给出标准的节点—连线树表示。

> English, Arabic, and Chinese. The Penn Treebank part-of-speech tagset was defined in Chapter 18, but we’ll see minor formatting differences across treebanks. The use of LISP-style parenthesized notation for trees is extremely common and resembles the bracketed notation we saw earlier in (19.1). For those who are not familiar with it we show a standard node-and-line tree representation in Fig. 19.6.

<!--figbox-->
> ((S

> (NP-SBJ (DT That) ((S(JJ cold) (, ,) (NP-SBJ The/DT flight/NN )(JJ empty) (NN sky) ) (VP should/MD(VP (VBD was) (VP arrive/VB(ADJP-PRD (JJ full) (PP-TMP at/IN(PP (IN of) (NP eleven/CD a.m/RB ))(NP (NN fire) (NP-TMP tomorrow/NN )))))(CC and)

> (NN light) ))))
<!--/figbox-->

(. .) ))

<!--figbox-->
> (a) (b)
<!--/figbox-->

*图 19.5 LDC 树库 3 中（a）Brown 与（b）ATIS 句子的分析。*
*Figure 19.5 Parses from the LDC Treebank3 for (a) Brown and (b) ATIS sentences.*

![](images/19-cfg-and-parsing/fig_p7_0.png)

*图 19.6 上一图中 Brown 语料库句子所对应的树。*
*Figure 19.6 The tree corresponding to the Brown corpus sentence in the previous figure.*

树库中的句子隐含地构成了该语言的一部文法。例如，

> The sentences in a treebank implicitly constitute a grammar of the language. For
例如，从图 19.5 中已分析的句子可以提取出图 19.7 所示的 CFG 规则（为简单起见去掉了规则后缀 (-SBJ)）。用于分析宾州树库的文法非常扁平，导致规则数量极多。例如，

> example, from the parsed sentences in Fig. 19.5 we can extract the CFG rules shown in Fig. 19.7 (with rule suffixes (-SBJ) stripped for simplicity). The grammar used to parse the Penn Treebank is very flat, resulting in very many rules. For example,

<!--figbox-->
> 文法 词库 S →NP VP . DT →the | that S →NP VP JJ →cold | empty | full NP →CD RB NN →sky | fire | light | flight | tomorrow NP →DT NN CC →and NP →NN CC NN IN →of | at NP →DT JJ , JJ NN CD →eleven NP →NN RB →a.m. VP →MD VP VB →arrive VP →VBD ADJP VBD →was | said VP →MD VP MD →should | would VP →VB PP NP ADJP →JJ PP PP →IN NP
>
> *Grammar Lexicon S →NP VP . DT →the | that S →NP VP JJ →cold | empty | full NP →CD RB NN →sky | fire | light | flight | tomorrow NP →DT NN CC →and NP →NN CC NN IN →of | at NP →DT JJ , JJ NN CD →eleven NP →NN RB →a.m. VP →MD VP VB →arrive VP →VBD ADJP VBD →was | said VP →MD VP MD →should | would VP →VB PP NP ADJP →JJ PP PP →IN NP*
<!--/figbox-->

*图 19.7 由图 19.5 中树库句子得到的 CFG 文法规则与词库。*
*Figure 19.7 CFG grammar rules and lexicon from the treebank sentences in Fig. 19.5.*

在约 4,500 条用于展开 VP 的不同规则中，有分别针对任意长度的 PP 序列以及动词论元各种可能排列方式的规则：

> among the approximately 4,500 different rules for expanding VPs are separate rules for PP sequences of any length and every possible arrangement of verb arguments:

> VP →VBD PP VP →VBD PP PP VP →VBD PP PP PP VP →VBD PP PP PP PP VP →VB ADVP PP VP →VB PP ADVP VP →ADVP VB PP

## 19.4 文法等价与范式

> 19.4 Grammar Equivalence and Normal Form

形式语言被定义为词串的（可能是无限的）集合。这提示我们，可以通过考察两部文法是否生成相同的串集合来询问它们是否等价。事实上，可以存在两部不同的上下文无关文法

> A formal language is defined as a (possibly infinite) set of strings of words. This suggests that we could ask if two grammars are equivalent by asking if they generate the same set of strings. In fact, it is possible to have two distinct context-free grammars

> `strongly`（强等价）
>
> 释义：指两部文法不仅生成相同的语言，还为每句话指派相同的短语结构树。

生成相同的语言。我们说两部文法是强等价的，如果

> generate the same language. We say that two grammars are strongly equivalent if

> `equivalent`（等价）
>
> 释义：文法之间的一种关系，分强等价与弱等价，区别在于是否指派相同的短语结构。

它们生成相同的字符串集合，并且为每个句子赋予相同的短语结构（仅允许对非终结符符号重新命名）。两个

> they generate the same set of strings and if they assign the same phrase structure to each sentence (allowing merely for renaming of the non-terminal symbols). Two

> `weakly`（弱）
>
> 释义：构成弱等价关系时的限定语，指两文法生成相同字符串集合但结构指派并不相同。

文法若生成相同的字符串集合，但并不

> grammars are weakly equivalent if they generate the same set of strings but do not

> `equivalent`（等价）
>
> 释义：文法之间的一种关系，分强等价与弱等价，区别在于是否指派相同的短语结构。

为每个句子赋予相同的短语结构，则它们是弱等价的。

> assign the same phrase structure to each sentence.

为文法设定一种范式有时是有用的，其中每条

> It is sometimes useful to have a normal form for grammars, in which each of

> `normal form`（范式）
>
> 释义：对产生式形式施加统一限制后的文法书写规范，如乔姆斯基范式要求每条产生式形如 A →B C 或 A →a。

产生式都取某种特定形式。例如，一个上下文无关文法处于

> the productions takes a particular form. For example, a context-free grammar is in

> `Chomsky normal form`（乔姆斯基范式（CNF））
>
> 释义：不含 ϵ 产生式、且每条产生式形如 A →B C 或 A →a 的上下文无关文法范式。

乔姆斯基范式（CNF）（Chomsky, 1963），如果它不含 ϵ 产生式，并且此外

> Chomsky normal form (CNF) (Chomsky, 1963) if it is ϵ-free and if in addition
每条产生式要么形如 A →B C，要么形如 A →a。也就是说，每条规则的右部要么有两个非终结符符号，要么有一个终结符符号。乔姆斯基

> each production is either of the form A →B C or A →a. That is, the right-hand side of each rule either has two non-terminal symbols or one terminal symbol. Chomsky

> `binary`（二叉的）
>
> 释义：指树上每个节点只分出两个子节点，乔姆斯基范式的文法树都具备这一性质。

范式文法是二叉分支的，也就是说它们具有二叉树（向下

> normal form grammars are binary branching, that is they have binary trees (down

> `branching`（分支）
>
> 释义：文法规则把父节点划分为子节点的数量特征，二叉分支即每次只分出两个。

直到词前节点）。我们在 19.6 节的 CKY 分析算法中利用了这一二叉分支性质。

> to the prelexical nodes). We make use of this binary branching property in the CKY parsing algorithm in Section 19.6.

任何上下文无关文法都可以转换为一个弱等价的乔姆斯基

> Any context-free grammar can be converted into a weakly equivalent Chomsky
范式文法。例如，形如

> normal form grammar. For example, a rule of the form
A →B C D
的规则可以转换为下面两条 CNF 规则（练习 19.1 要求读者

> can be converted into the following two CNF rules (Exercise 19.1 asks the reader to

<!--figbox-->
> 文法 词库
>
> *Grammar Lexicon*

> S →NP VP Det →that | this | the | a S →Aux NP VP Noun →book | flight | meal | money S →VP Verb →book | include | prefer NP →Pronoun Pronoun →I | she | me NP →Proper-Noun Proper-Noun →Houston | United NP →Det Nominal Aux →does Nominal →Noun Preposition →from | to | on | near | through Nominal →Nominal Noun Nominal →Nominal PP VP →Verb VP →Verb NP VP →Verb NP PP VP →Verb PP VP →VP PP PP →Preposition NP
<!--/figbox-->

*图 19.8 L1 微型英语文法与词库。*
*Figure 19.8 The L1 miniature English grammar and lexicon.*

构造完整的算法）：

> formulate the complete algorithm):

A →B X X →C D
有时使用二叉分支实际上能产生更小的文法。举例

> Sometimes using binary branching can actually produce smaller grammars. For
来说，那些可以刻画为下式的句子

> example, the sentences that might be characterized as
在宾州树库（Penn Treebank）中由下面这一系列规则表示：

> are represented in the Penn Treebank by this series of rules:

> VP -> VBD NP PP*

> VP →VBD NP PP VP →VBD NP PP PP VP →VBD NP PP PP PP VP →VBD NP PP PP PP PP...

但也可以由下面这个含两条规则的文法生成：

> but could also be generated by the following two-rule grammar:

> VP →VBD NP PP VP →VP PP

用一个符号 A 生成潜在的无限符号序列 B，配合

> The generation of a symbol A with a potentially infinite sequence of symbols B with

> `Chomsky- adjunction`（乔姆斯基附加）
>
> 释义：形如 A →A B 的规则，使同一符号可反复向下附加，从而生成任意长的序列。

形如 A →A B 的规则称为乔姆斯基附加（Chomsky-adjunction）。

> a rule of the form A →A B is known as Chomsky-adjunction.

## 19.5 歧义

> 19.5 Ambiguity

歧义是句法分析器面临的最严重的问题。第 18 章介绍了词性歧义与词性消歧的概念。这里我们介绍一种新的歧义，称为结构歧义，

> Ambiguity is the most serious problem faced by syntactic parsers. Chapter 18 introduced the notions of part-of-speech ambiguity and part-of-speech disambiguation. Here, we introduce a new kind of ambiguity, called structural ambiguity,

> `structural ambiguity`（结构歧义）
>
> 释义：同一句子被文法赋予多于一个解析树，因而具有多种句法结构的情形。

并用图 19.8 所示的新玩具文法 L1 加以说明，它在 L0 文法的基础上增加了几条规则。

> illustrated with a new toy grammar L1, shown in Figure 19.8, which adds a few rules to the L0 grammar.

当文法可以为句子指定多于一个解析

> Structural ambiguity occurs when the grammar can assign more than one parse
到一个句子上。Groucho Marx 在《Animal Crackers》中扮演 Captain Spaulding 时的那句著名台词

> to a sentence. Groucho Marx’s well-known line as Captain Spaulding in Animal

![](images/19-cfg-and-parsing/fig_p10_0.png)

*图 19.9 一个有歧义句子的两棵解析树。左侧的分析对应的是幽默的解读，即大象穿着睡衣；右侧的分析对应的是 Captain Spaulding 穿着自己的睡衣开枪的解读。*
*Figure 19.9 Two parse trees for an ambiguous sentence. The parse on the left corresponds to the humorous reading in which the elephant is in the pajamas, the parse on the right corresponds to the reading in which Captain Spaulding did the shooting in his pajamas.*

Crackers 之所以有歧义，是因为短语 in my pajamas 既可以是以 elephant 为中心词的 NP 的一部分，也可以是以 shot 为中心词的动词短语的一部分。图 19.9 使用 L1 中的规则说明了 Marx 这句台词的这两种分析。

> Crackers is ambiguous because the phrase in my pajamas can be part of the NP headed by elephant or a part of the verb phrase headed by shot. Figure 19.9 illustrates these two analyses of Marx’s line using rules from L1.

结构歧义的形式多种多样，这倒也在情理之中。两种常见的

> Structural ambiguity, appropriately enough, comes in many forms. Two common
歧义类型是附着歧义和并列歧义。

> kinds of ambiguity are attachment ambiguity and coordination ambiguity. A

> `attachment ambiguity`（附着歧义）
>
> 释义：同一个成分在解析树中可以附着到多个位置，从而产生多种解读的歧义。

如果某个特定的成分可以附着到

> sentence has an attachment ambiguity if a particular constituent can be attached to
解析树上的一处以上的位置，那么句子就存在附着歧义。Groucho Marx 的那句话就是一个例子

> the parse tree at more than one place. The Groucho Marx sentence is an example

> `PP-attachment ambiguity`（PP 附着歧义）
>
> 释义：介词短语既可以附着在 NP 内、也可以附着在 VP 内等不同归属所造成的歧义。

属于 PP 附着歧义：介词短语既可以附着为

> of PP-attachment ambiguity: the preposition phrase can be attached either as part
NP 的一部分，也可以附着为 VP 的一部分。各类副词短语也容易出现这类歧义。例如，在下面的例子中，动名词性 VP flying to Paris 既可以是以 the Eiffel Tower 为主语的动名词句的一部分，也可以是修饰以 saw 为中心词的 VP 的附加语：

> of the NP or as part of the VP. Various kinds of adverbial phrases are also subject to this kind of ambiguity. For instance, in the following example the gerundive-VP flying to Paris can be part of a gerundive sentence whose subject is the Eiffel Tower or it can be an adjunct modifying the VP headed by saw:

（19.2）我们看到埃菲尔铁塔正飞往巴黎。

> (19.2) We saw the Eiffel Tower flying to Paris.

> `coordination ambiguity`（并列歧义）
>
> 释义：由 and 等连词连接的短语可以有多种并列组合方式，由此产生多种解读的现象。

在并列歧义中，短语可以由 and 这样的连词连接在一起。

> In coordination ambiguity phrases can be conjoined by a conjunction like and.

例如，短语 old men and women 可以加括号为 [old [men and women]]，指的是年长的男人和年长的女人；也可以加括号为 [old men] and [women]，这时只有男人是年长的。这些歧义在真实句子中以复杂的方式交织在一起，比如下面这个来自 Brown 语料库的新闻句子：

> For example, the phrase old men and women can be bracketed as [old [men and women]], referring to old men and old women, or as [old men] and [women], in which case it is only the men who are old. These ambiguities combine in complex ways in real sentences, like the following news sentence from the Brown corpus:

（19.3）Kennedy 总统今天把白宫的其它事务搁置一旁，

> (19.3) President Kennedy today pushed aside other White House business to
以便把全部时间和精力都投入到那篇将于明晚通过全国电视和广播向美国人民发表的柏林危机演说上。

> devote all his time and attention to working on the Berlin crisis address he will deliver tomorrow night to the American people over nationwide television and radio.

这句话有多处歧义，不过由于它们在语义上

> This sentence has a number of ambiguities, although since they are semantically
并不合理，需要仔细阅读才能看出来。最后一个名词短语可以分析为 [nationwide [television and radio]] 或 [[nationwide television] and radio]。

> unreasonable, it requires a careful reading to see them. The last noun phrase could be parsed [nationwide [television and radio]] or [[nationwide television] and radio].

pushed aside 的直接宾语本应是 other White House business，但也可以是那个古怪的短语 [other White House business to devote all his time and attention to working]（即一种类似 Kennedy affirmed [his intention to propose a new budget to address the deficit] 的结构）。其次，短语 on the Berlin crisis address he will deliver tomorrow night to the American people 可以是修饰动词 pushed 的附加语。像 over nationwide television and radio 这样的 PP 可以附着到任何更高的 VP 或 NP 上（例如它可以修饰 people 或 night）。

> The direct object of pushed aside should be other White House business but could also be the bizarre phrase [other White House business to devote all his time and attention to working] (i.e., a structure like Kennedy affirmed [his intention to propose a new budget to address the deficit]). Then the phrase on the Berlin crisis address he will deliver tomorrow night to the American people could be an adjunct modifying the verb pushed. A PP like over nationwide television and radio could be attached to any of the higher VPs or NPs (e.g., it could modify people or night).

对于自然出现的句子存在许多语法正确但语义不合理的分析，这是一个困扰所有分析器的烦人问题。所幸，下面介绍的 CKY 算法正是为了高效处理结构歧义而设计的。而且正如我们在下一节将会看到的，我们可以用神经方法来增强 CKY，通过句法消歧选出一个正确的分析。

> The fact that there are many grammatically correct but semantically unreasonable parses for naturally occurring sentences is an irksome problem that affects all parsers. Fortunately, the CKY algorithm below is designed to efficiently handle structural ambiguities. And as we’ll see in the following section, we can augment CKY with neural methods to choose a single correct parse by syntactic disambiguation.

> `syntactic`（句法的）
>
> 释义：与句子成分结构有关的；此处指用来在多个分析中做出选择的句法信息。

> `disambiguation`（消歧）
>
> 释义：在多个符合文法的分析中选出唯一正确分析的过程，常借助句法或神经方法完成。

## 19.6 CKY 分析：一种动态规划方法

> 19.6 CKY Parsing: A Dynamic Programming Approach

动态规划为解决文法中的歧义所带来的问题提供了一个强大的框架。回想一下，动态规划方法会系统地填写一张存放子问题解的表。这张完整的表包含了解决整个问题所需的所有子问题的解。

> Dynamic programming provides a powerful framework for addressing the problems caused by ambiguity in grammars. Recall that a dynamic programming approach systematically fills in a table of solutions to subproblems. The complete table has the solution to all the subproblems needed to solve the problem as a whole.

在句法分析中，这些子问题表示输入中检测到的所有成分的解析树。

> In the case of syntactic parsing, these subproblems represent parse trees for all the constituents detected in the input.

动态规划的优势来自于我们

> The dynamic programming advantage arises from the context-free nature of our
文法规则的上下文无关性质——一旦在输入的某个片段中发现了一个成分，我们就可以记录它的存在，并让它可供任何后续可能需要它的推导使用。这在时间和存储两方面都带来了效率，因为子树可以在表中查找，而不必重新分析。本节介绍 Cocke-Kasami-Younger（CKY）算法，这是使用最广泛的基于动态规划的句法分析方法。图表分析（chart parsing，Kaplan 1973; Kay 1982）是一种相关的方法，而动态规划方法也常被称为图表分析方法。

> grammar rules—once a constituent has been discovered in a segment of the input we can record its presence and make it available for use in any subsequent derivation that might require it. This provides both time and storage efficiencies since subtrees can be looked up in a table, not reanalyzed. This section presents the Cocke-Kasami-Younger (CKY) algorithm, the most widely used dynamic-programming based approach to parsing. Chart parsing (Kaplan 1973, Kay 1982) is a related approach, and dynamic programming methods are often referred to as chart parsing methods.

> `chart parsing`（图表分析（chart parsing））
>
> 释义：在表中记录输入各片段中已识别成分的分析方法，动态规划方法因此也被称为图表分析方法。

### 19.6.1 转换为乔姆斯基范式（CNF）

> 19.6.1 Conversion to Chomsky Normal Form

CKY 算法要求文法首先处于乔姆斯基范式（CNF）。

> The CKY algorithm requires grammars to first be in Chomsky Normal Form (CNF).

回想节 19.4，处于 CNF 的文法只限于形如 A →B C 或 A →w 的规则。也就是说，每条规则的右侧必须或者展开为两个非终结符，或者展开为一个终结符。把文法限制为 CNF 不会造成任何表达能力的损失，因为任何上下文无关文法都可以转换为一个对应的 CNF 文法，它接受的字符串集合与原文法完全相同。

> Recall from Section 19.4 that grammars in CNF are restricted to rules of the form A →B C or A →w. That is, the right-hand side of each rule must expand either to two non-terminals or to a single terminal. Restricting a grammar to CNF does not lead to any loss in expressiveness, since any context-free grammar can be converted into a corresponding CNF grammar that accepts exactly the same set of strings as the original grammar.

我们先从把一般 CFG 转换为

> Let’s start with the process of converting a generic CFG into one represented in
CNF 表示的过程开始。假设我们处理的是不含 ϵ 的文法，那么在任何一般文法中都有三种情况需要处理：右侧混合了终结符与非终结符的规则、右侧只有一个非终结符的规则，以及右侧长度大于 2 的规则。

> CNF. Assuming we’re dealing with an ϵ-free grammar, there are three situations we need to address in any generic grammar: rules that mix terminals with non-terminals on the right-hand side, rules that have a single non-terminal on the right-hand side, and rules in which the length of the right-hand side is greater than 2.

对于混合了终结符和非终结符的规则，补救办法就是简单地引入

> The remedy for rules that mix terminals and non-terminals is to simply introduce
一个新的哑非终结符，它只覆盖原来的那个终结符。例如，像 INF-VP →to VP 这样的不定式动词短语规则，会被替换为两条规则：INF-VP →TO VP 和 TO →to。

> a new dummy non-terminal that covers only the original terminal. For example, a rule for an infinitive verb phrase such as INF-VP →to VP would be replaced by the two rules INF-VP →TO VP and TO →to.

> `Unit`（单元）
>
> 释义：指右侧只有一个非终结符的产生式，即单元产生式，如 A →B，可被消除而不改变语言。

右侧只有一个非终结符的规则称为单元产生式。我们

> Rules with a single non-terminal on the right are called unit productions. We

> `productions`（产生式）
>
> 释义：文法中规定某个非终结符如何重写为符号串的规则。

可以消除单元产生式：把原规则的右侧改写为它们最终导出的所有非单元产生式的右侧。更形式化地说，如果 A ∗⇒B 是经由一条或多条单元产生式构成的一条链，而 B →γ 是我们文法中的一条非单元产生式，那么我们就为文法中每一条这样的规则添加 A →γ，并丢弃中间所有的单元产生式。正如我们用玩具文法所演示的，这可能使文法大幅扁平化，并使终结符在最终得到的树中被提升到相当高的层次。

> can eliminate unit productions by rewriting the right-hand side of the original rules with the right-hand side of all the non-unit production rules that they ultimately lead to. More formally, if A ∗⇒B by a chain of one or more unit productions and B →γ is a non-unit production in our grammar, then we add A →γ for each such rule in the grammar and discard all the intervening unit productions. As we demonstrate with our toy grammar, this can lead to a substantial flattening of the grammar and a consequent promotion of terminals to fairly high levels in the resulting trees.

右部长度超过 2 的规则，通过引入新的非终结符来规范化，这些新非终结符把较长的序列分散到若干条新规则上。

> Rules with right-hand sides longer than 2 are normalized through the introduction of new non-terminals that spread the longer sequences over several new rules.

形式化地说，如果有一条形如

> Formally, if we have a rule like
A →B C γ
的规则，我们把最左边的一对非终结符替换为一个新的非终结符，并引入一条新的产生式，从而得到如下新规则：

> we replace the leftmost pair of non-terminals with a new non-terminal and introduce a new production, resulting in the following new rules:

A →X1 γX1 →B C
对于右部更长的情况，我们只需迭代这一过程，直到不合规的规则被替换为长度为 2 的规则。选择替换最左边的一对非终结符纯粹是任意的；任何能得到二元规则的系统性方案都可以。

> In the case of longer right-hand sides, we simply iterate this process until the offending rule has been replaced by rules of length 2. The choice of replacing the leftmost pair of non-terminals is purely arbitrary; any systematic scheme that results in binary rules would suffice.

在我们当前的文法中，规则 S →Aux NP VP 将被替换为下面两条

> In our current grammar, the rule S →Aux NP VP would be replaced by the two
规则 S →X1 VP 和 X1 →Aux NP。

> rules S →X1 VP and X1 →Aux NP.

整个转换过程可以总结如下：

> The entire conversion process can be summarized as follows:

- 把所有符合要求的规则原样复制到新文法中。
- 把规则中的终结符转换为哑非终结符。
- 转换单元产生式。
- 把所有规则变为二元规则并加入新文法。

> Copy all conforming rules to the new grammar unchanged.
> Convert terminals within rules to dummy non-terminals.
> Convert unit productions.
> Make all rules binary and add them to new grammar.

图 19.10 展示了把整个转换过程应用于

> Figure 19.10 shows the results of applying this entire conversion procedure to
前面第 433 页介绍的 L1 文法所得的结果。注意，该图没有显示原始的词汇规则；由于这些原始词汇规则已经处于 CNF 中，它们都原样保留到新文法中。不过，图 19.10 确实显示出了消除单元产生式的过程实际上在若干处创建了新的词汇规则。例如，在转换后的文法中，所有原来的动词都被提升为 VP，也被提升为 S。

> the L1 grammar introduced earlier on page 433. Note that this figure doesn’t show the original lexical rules; since these original lexical rules are already in CNF, they all carry over unchanged to the new grammar. Figure 19.10 does, however, show the various places where the process of eliminating unit productions has, in effect, created new lexical rules. For example, all the original verbs have been promoted to both VPs and to Ss in the converted grammar.

### 19.6.2 CKY 识别

> 19.6.2 CKY Recognition

现在我们的文法已处于 CNF，解析树中位于词性层之上的每个非终结符节点都恰好有两个女儿。可以用一个二维矩阵来编码整棵树的结构。对于长度为 n 的句子，我们处理的是一个 (n+1)×(n+1) 矩阵的上三角部分。该矩阵中的每个单元格 [i, j] 都包含一组非终结符，它们表示所有跨越输入中位置 i 到 j 的成分。由于我们的索引方案从 0 开始，自然可以把这些索引看作指向输入词之间的空隙（如 0 Book 1 that 2 flight 3）。这些空隙通常被称为 fenceposts，取自

> With our grammar now in CNF, each non-terminal node above the part-of-speech level in a parse tree will have exactly two daughters. A two-dimensional matrix can be used to encode the structure of an entire tree. For a sentence of length n, we will work with the upper-triangular portion of an (n+1)×(n+1) matrix. Each cell [i, j] in this matrix contains the set of non-terminals that represent all the constituents that span positions i through j of the input. Since our indexing scheme begins with 0, it’s natural to think of the indexes as pointing at the gaps between the input words (as in 0 Book 1 that 2 flight 3). These gaps are often called fenceposts, on the metaphor of

> `fenceposts`（栅栏桩）
>
> 释义：指句中相邻词之间（含首尾）的位置，用作图表分析中各成分起止位置的索引。

栅栏各段之间的桩子这一比喻。由此可知，表示整个输入的单元格位于矩阵中的位置 [0,n]。

> the posts between segments of fencing. It follows then that the cell that represents the entire input resides in position [0,n] in the matrix.

由于我们表中的每个非终结符条目在分析中都有两个女儿，因此对于由条目 [i, j] 表示的每个成分，输入中必定存在一个位置 k，使得它可以在该处被切分为两部分，且 i < k < j。给定这样

> Since each non-terminal entry in our table has two daughters in the parse, it follows that for each constituent represented by an entry [i, j], there must be a position in the input, k, where it can be split into two parts such that i < k < j. Given such

<!--figbox-->
> L1 文法　　L1 的 CNF 形式
>
> *L1 Grammar L1 in CNF*

> S →NP VP S →NP VP S →Aux NP VP S →X1 VP

> X1 →Aux NP

> S →VP S →book | include | prefer

> S →Verb NP S →X2 PP S →Verb PP S →VP PP

> NP →Pronoun NP →I | she | me NP →Proper-Noun NP →United | Houston NP →Det Nominal NP →Det Nominal Nominal →Noun Nominal →book | flight | meal | money Nominal →Nominal Noun Nominal →Nominal Noun Nominal →Nominal PP Nominal →Nominal PP VP →Verb VP →book | include | prefer VP →Verb NP VP →Verb NP VP →Verb NP PP VP →X2 PP

> X2 →Verb NP

> VP →Verb PP VP →Verb PP VP →VP PP VP →VP PP PP →Preposition NP PP →Preposition NP
<!--/figbox-->

*图 19.10 L1 文法及其到 CNF 的转换。注意，虽然这里没有显示，L1 中所有原始的词汇条目也同样原样保留。*
*Figure 19.10 L1 Grammar and its conversion to CNF. Note that although they aren’t shown here, all the original lexical entries from L1 carry over unchanged as well.*

的某个位置 k，第一个成分 [i,k] 必定位于第 i 行中条目 [i, j] 左侧的某处，而第二个条目 [k, j] 必定位于它的下方、沿第 j 列。

> a position k, the first constituent [i,k] must lie to the left of entry [i, j] somewhere along row i, and the second entry [k, j] must lie beneath it, along column j.

为使这一点更具体，考虑下面这个例子及其已填好的

> To make this more concrete, consider the following example with its completed
分析矩阵，如图 19.11 所示。

> parse matrix, shown in Fig. 19.11.

(19.4) Book the flight through Houston.

矩阵中的超对角线一行包含输入中每个词的词性。该超对角线之上的各条对角线包含覆盖输入中所有长度递增跨度的成分。

> The superdiagonal row in the matrix contains the parts of speech for each word in the input. The subsequent diagonals above that superdiagonal contain constituents that cover all the spans of increasing length in the input.

在这一设置下，CKY 识别就是按正确的顺序填充分析表。

> Given this setup, CKY recognition consists of filling the parse table in the right

顺序。为此，我们采用自底向上的方式，使得在填充任意单元格 [i, j] 时，那些包含可能对该条目有所贡献的部分的单元格（即左边的单元格和下方的单元格）都已经被填好。图 19.12 给出的算法一次填充一列地填写这个上三角矩阵，从左到右推进，每一列都自底向上填充，如图 19.11 右侧所示。这一方案保证我们在每个时刻都拥有所需的全部信息（左边的信息，因为左边各列都已填好；下方的信息，因为我们自底向上填充）。它也对应在线处理，因为从左到右填列相当于一次处理一个词。

> way. To do this, we’ll proceed in a bottom-up fashion so that at the point where we are filling any cell [i, j], the cells containing the parts that could contribute to this entry (i.e., the cells to the left and the cells below) have already been filled. The algorithm given in Fig. 19.12 fills the upper-triangular matrix a column at a time working from left to right, with each column filled from bottom to top, as the right side of Fig. 19.11 illustrates. This scheme guarantees that at each point in time we have all the information we need (to the left, since all the columns to the left have already been filled, and below since we’re filling bottom to top). It also mirrors online processing, since filling the columns from left to right corresponds to processing each word one at a time.

图 19.12 所给算法的最外层循环遍历各列，

> The outermost loop of the algorithm given in Fig. 19.12 iterates over the columns,
第二个循环遍历各行，自底向上。最内层循环的目的是遍历输入中从 i 跨到 j 的子串所有可能被一分为二的位置。当 k 遍历该串可以被切分的位置时，我们考虑的各对单元格同步地沿第 i 行向右、沿第 j 列向下移动。图 19.13 说明了填充单元格 [i, j] 的一般情形。

> and the second loop iterates over the rows, from the bottom up. The purpose of the innermost loop is to range over all the places where a substring spanning i to j in the input might be split in two. As k ranges over the places where the string can be split, the pairs of cells we consider move, in lockstep, to the right along row i and down along column j. Figure 19.13 illustrates the general case of filling cell [i, j].

![](images/19-cfg-and-parsing/fig_p14_0.png)

*图 19.11 Book the flight through Houston 的完整分析表。*
*Figure 19.11 Completed parse table for Book the flight through Houston.*

![](images/19-cfg-and-parsing/fig_p14_1.png)

*图 19.12 CKY 算法。*
*Figure 19.12 The CKY algorithm.*

在每一次这样的切分处，算法考虑这两个单元格的内容能否以文法中某条规则所允许的方式组合起来。如果存在这样的规则，就把其左部的非终结符填入表中。

> At each such split, the algorithm considers whether the contents of the two cells can be combined in a way that is sanctioned by a rule in the grammar. If such a rule exists, the non-terminal on its left-hand side is entered into the table.

图 19.14 展示了在读到

> Figure 19.14 shows how the five cells of column 5 of the table are filled after the
词 Houston 之后，表中第 5 列这五个单元格是如何填充的。箭头指出了用于向表中添加条目所用的两个跨度。注意，单元格 [0,5] 中的动作表明该输入存在三种不同的分析：一种 PP 修饰 the flight，一种 PP 修饰 the booking，还有一种对应原始规则 VP →Verb NP PP 中的第二个论元，现在由规则 VP →X2 PP 间接表示。

> word Houston is read. The arrows point out the two spans that are being used to add an entry to the table. Note that the action in cell [0,5] indicates the presence of three alternative parses for this input, one where the PP modifies the flight, one where it modifies the booking, and one that captures the second argument in the original VP →Verb NP PP rule, now captured indirectly with the VP →X2 PP rule.

### 19.6.3 CKY 分析

> 19.6.3 CKY Parsing

图 19.12 给出的算法是一个识别器，而不是一个分析器。也就是说，它只能根据在单元格 [0,n] 中是否找到 S 来告诉我们一个给定句子是否存在合法的分析，却无法给出推导，而推导才是分析器真正要做的工作。要把它变成一个能够为给定输入返回所有可能分析的分析器，我们可以对算法做两处简单的改动：第一处改动是扩充表中的条目，使每个非终结符都配以指向其来源表条目的指针（大致如图 19.14 所示）；第二处改动是允许同一非终结符的多个版本进入表中（同样如图 19.14 所示）。经过这些改动，填好的表就包含了给定输入的所有可能分析。返回任意一个

> The algorithm given in Fig. 19.12 is a recognizer, not a parser. That is, it can tell us whether a valid parse exists for a given sentence based on whether or not if finds an S in cell [0,n], but it can’t provide the derivation, which is the actual job for a parser. To turn it into a parser capable of returning all possible parses for a given input, we can make two simple changes to the algorithm: the first change is to augment the entries in the table so that each non-terminal is paired with pointers to the table entries from which it was derived (more or less as shown in Fig. 19.14), the second change is to permit multiple versions of the same non-terminal to be entered into the table (again as shown in Fig. 19.14). With these changes, the completed table contains all the possible parses for a given input. Returning an arbitrary single

![](images/19-cfg-and-parsing/fig_p15_0.png)

*图 19.13 填充 CKY 表中第 [i, j] 个单元格的所有方式。*
*Figure 19.13 All the ways to fill the [i, j]th cell in the CKY table.*

分析的做法就是从单元格 [0,n] 中选出一个 S，然后递归地从表中取回组成它的各个成分。当然，我们通常并不想返回一个句子的每一种分析，而只想要最好的那个分析；下一节我们将看到如何做到这一点。

> parse consists of choosing an S from cell [0,n] and then recursively retrieving its component constituents from the table. Of course, instead of returning every parse for a sentence, we usually want just the best parse; we’ll see how to do that in the next section.

### 19.6.4 CKY 的实践

> 19.6.4 CKY in Practice

最后我们应注意到，虽然限定为 CNF 在理论上并不成为问题，在实践中却会带来一些不小的麻烦。返回的 CNF 树可能与文法开发者构建的原始文法不一致，并且会使任何由句法驱动的语义分析方法变得复杂。

> Finally, we should note that while the restriction to CNF does not pose a problem theoretically, it does pose some non-trivial problems in practice. The returned CNF trees may not be consistent with the original grammar built by the grammar developers, and will complicate any syntax-driven approach to semantic analysis.

绕开这些问题的一种做法是保留足够的信息

> One approach to getting around these problems is to keep enough information
以便在分析的后处理步骤中把我们的树变换回原始文法。对于长度大于 2 的规则所用的那种变换来说，这很容易做到。只要删去新增的哑非终结符并提升它们的女儿结点，就能恢复原来的树。

> around to transform our trees back to the original grammar as a post-processing step of the parse. This is trivial in the case of the transformation used for rules with length greater than 2. Simply deleting the new dummy non-terminals and promoting their daughters restores the original tree.

对于一元产生式，直接修改基本的 CKY 算法来处理它们，比存储恢复正确树所需的信息更为方便。练习 19.3 要求你完成这一改动。附录 E 中介绍的许多概率分析器所使用的，正是按

> In the case of unit productions, it turns out to be more convenient to alter the basic CKY algorithm to handle them directly than it is to store the information needed to recover the correct trees. Exercise 19.3 asks you to make this change. Many of the probabilistic parsers presented in Appendix E use the CKY algorithm altered in

![](images/19-cfg-and-parsing/fig_p16_0.png)

*图 19.14 读入单词 Houston 后填充第 5 列的各单元格。*
*Figure 19.14 Filling the cells of column 5 after reading the word Houston.*

这种方式修改过的 CKY 算法。

> just this manner.

## 19.7 基于跨度的神经成分句法分析

> 19.7 Span-Based Neural Constituency Parsing

虽然我们目前看到的 CKY 分析算法在枚举一个句子的所有可能解析树方面表现很好，但它有一个大问题：它并不告诉我们哪一种分析才是正确的！也就是说，它无法在几种可能的分析之间消除歧义。

> While the CKY parsing algorithm we’ve seen so far does great at enumerating all the possible parse trees for a sentence, it has a large problem: it doesn’t tell us which parse is the correct one! That is, it doesn’t disambiguate among the possible parses.

为了解决消歧问题，我们将使用 CKY 算法的一个简单的神经扩展。这类分析算法（通常称为基于跨度的成分句法分析，或神经 CKY）的基本思路是：训练一个神经分类器为每个成分赋予一个得分，然后用 CKY 的修改版本把这些成分得分组合起来，以找出得分最高的解析树。

> To solve the disambiguation problem we’ll use a simple neural extension of the CKY algorithm. The intuition of such parsing algorithms (often called span-based constituency parsing, or neural CKY), is to train a neural classifier to assign a score to each constituent, and then use a modified version of CKY to combine these constituent scores to find the best-scoring parse tree.

这里我们将介绍 Kitaev et al. (2019) 给出的算法的一个版本。该

> Here we’ll describe a version of the algorithm from Kitaev et al. (2019). This
分析器学习把一个词跨度映射为一个成分，并且像 CKY 一样，逐层组合越来越大的跨度，以自底向上的方式构建解析树。但与经典 CKY 不同，该分析器不使用手工编写的文法来约束哪些成分可以被组合，而只是依靠学习到的跨度神经表示来编码可能的组合。

> parser learns to map a span of words to a constituent, and, like CKY, hierarchically combines larger and larger spans to build the parse-tree bottom-up. But unlike classic CKY, this parser doesn’t use the hand-written grammar to constrain what constituents can be combined, instead just relying on the learned neural representations of spans to encode likely combinations.

### 19.7.1 计算跨度的得分

> 19.7.1 Computing Scores for a Span

我们先只考虑位于两者之间的那个成分（我们称之为跨度）

> Let’s begin by considering just the constituent (we’ll call it a span) that lies between

> `span`（跨度）
>
> 释义：由两个栅栏位置界定的一段连续词序列，是成分分析中被打分和组合的基本单位。

栅栏位置 i 与 j 之间的成分，其非终结符标号为 l。我们将构建一个系统，为这个成分跨度赋予得分 s(i, j,l)。

> fencepost positions i and j with non-terminal symbol label l. We’ll build a system to assign a score s(i, j,l) to this constituent span.

![](images/19-cfg-and-parsing/fig_p17_0.png)

*图 19.15 为标号 NP 的跨度 the flight 计算跨度得分的简化示意图。*
*Figure 19.15 A simplified outline of computing the span score for the span the flight with the label NP.*

图 19.15 勾勒了这一架构。输入的词元先经过一个预训练语言模型（如 BERT）得到嵌入表示。由于 BERT 是在子词（wordpiece）单元而非词的层面上运作的，我们首先需要把 BERT 的输出转换为词表示。一种标准的做法是直接用第一个子词单元作为整个词的表示；使用最后一个子词单元，或使用所有子词单元之和，也同样常见。随后这些嵌入可以经过若干后处理层；例如 Kitaev et al.(2019) 使用了 8 层 Transformer。

> Fig. 19.15 sketches the architecture. The input word tokens are embedded by passing them through a pretrained language model like BERT. Because BERT operates on the level of subword (wordpiece) tokens rather than words, we’ll first need to convert the BERT outputs to word representations. One standard way of doing this is to simply use the first subword unit as the representation for the entire word; using the last subword unit, or the sum of all the subword units are also common. The embeddings can then be passed through some postprocessing layers; Kitaev et al.(2019), for example, use 8 Transformer layers.

由此得到的词编码器输出 yt 随后被用来计算跨度得分。

> The resulting word encoder outputs yt are then used to compute a span score.

首先，我们必须把词的编码（以词的位置为索引）映射为跨度的编码（以栅栏位置为索引）。为此，我们用两个不同的值来表示每一个栅栏位置；其思路是，位于某个词右侧的跨度端点所表示的信息，与位于该词左侧的跨度端点不同。我们把每个词的输出 yt 拆成两半，转换为一个指向左侧的值 ←−y t（用于终止于该栅栏位置的跨度）和一个指向右侧的值 −→y t（用于起始于该栅栏位置的跨度）。于是每个跨度从一个双向量栅栏位置延伸到另一个，如下面 the flight（即 span(1,3)）的表示所示：

> First, we must map the word encodings (indexed by word positions) to span encodings (indexed by fenceposts). We do this by representing each fencepost with two separate values; the intuition is that a span endpoint to the right of a word represents different information than a span endpoint to the left of a word. We convert each word output yt into a (leftward-pointing) value for spans ending at this fencepost,←−y t, and a (rightward-pointing) value −→y t for spans beginning at this fencepost, by splitting yt into two halves. Each span then stretches from one double-vector fencepost to another, as in the following representation of the flight, which is span(1,3):

Book the flight through
y0 −→ y0 ←− y1 y1 −→ y1 ←− y2 y2 −→ y2 ←− y3 y3 −→ y3 ←− y4 y4 −→ y4 ←− y5 ...

> START0

$$⃝_{0}⃝_{1}⃝_{2}⃝_{3}⃝_{4}$$

span(1,3)
表示跨度的一种传统做法最初是为基于 RNN 的模型提出的（Wang and Chang, 2016），后来也被推广到 Transformer：取其起点与终点嵌入之差，即用 j 的嵌入减去 i 的嵌入来表示跨度 (i, j)。这里我们则通过拼接跨度各个栅栏位置分量的差值来表示一个跨度：

> A traditional way to represent a span, developed originally for RNN-based models(Wang and Chang, 2016), but extended also to Transformers, is to take the difference between the embeddings of its start and end, i.e., representing span (i, j) by subtracting the embedding of i from the embedding of j. Here we represent a span by concatenating the difference of each of its fencepost components:

v(i, j) = [−→ yj −−→ yi ; ←−− y j+1 −←−− yi+1] (19.5)
跨度向量 v 随后被送入一个 MLP 跨度分类器，其中包含两个全连接层和一个 ReLU 激活函数，其输出维度等于可能的非终结符标号数目：

> The span vector v is then passed through an MLP span classifier, with two fullyconnected layers and one ReLU activation function, whose output dimensionality is the number of possible non-terminal labels:

$$s(i,j,\cdot) =W_{2}\text{ReLU}(\text{LayerNorm}(W_{1}v(i,j)))$$

随后该 MLP 为每一个可能的非终结符输出一个得分。

> The MLP then outputs a score for each possible non-terminal.

### 19.7.2 把跨度得分整合进分析

> 19.7.2 Integrating Span Scores into a Parse

现在我们已经有了每个带标注成分跨度 s(i, j,l) 的得分。但我们需要的是整棵解析树的得分。形式上，一棵树 T 表示为 |T| 个这种带标注跨度的集合，其中第 t 个跨度起始于位置 it、终止于位置 jt，标号为 lt：

> Now we have a score for each labeled constituent span s(i, j,l). But we need a score for an entire parse tree. Formally a tree T is represented as a set of |T| such labeled spans, with the tth span starting at position it and ending at position jt, with label lt:

$$T=\{(i_{t},j_{t},l_{t}):t=1,...,|T|\}$$

因此，一旦有了每个跨度的得分，分析器只需把构成这棵树的所有跨度的得分相加，就能算出整棵树 s(T) 的得分：

> Thus once we have a score for each span, the parser can compute a score for the whole tree s(T) simply by summing over the scores of its constituent spans:

$$\sum_{,j,l)\in}$$

s(T) = s(i, j,l) 我们可以选取得分最大的树作为最终的解析树：

> s(T) = s(i, j,l) And we can choose the final parse tree as the tree with the maximum score:

ˆT = argmax s(T) (19.9)
产生最可能分析的最简单方法是贪心地选择

> The simplest method to produce the most likely parse is to greedily choose the
每个跨度的得分最高的标签。这种贪心方法不保证能产生一棵树，因为某个跨度的最佳标签可能无法嵌入一棵完整的树。然而在实践中，贪心方法往往能找到树；Gaddy et al. (2018) 在实验中发现，95% 的预测括号结构能形成有效的树。

> highest scoring label for each span. This greedy method is not guaranteed to produce a tree, since the best label for a span might not fit into a complete tree. In practice, however, the greedy method tends to find trees; in their experiments Gaddy et al.(2018) finds that 95% of predicted bracketings form valid trees.

> T

尽管如此，更常见的做法是使用 CKY 算法的一个变体来找出

> Nonetheless it is more common to use a variant of the CKY algorithm to find the
完整的分析。Gaddy et al. (2018) 中定义的变体工作方式如下。我们定义 sbest(i, j) 为覆盖 (i, j) 的最佳子树的得分。对于长度为 1 的跨度，我们选择最佳标签：

> full parse. The variant defined in Gaddy et al. (2018) works as follows. Let’s define sbest(i, j) as the score of the best subtree spanning (i, j). For spans of length one, we choose the best label:

$$s_{\text{best}}(i,i+1) =\text{max}_{l}s(i,i+1,l)$$

> l

对于其他跨度 (i, j)，递推式为：

> For other spans (i, j), the recursion is:

$$s_{\text{best}}(i,j)=\text{max}_{l}s(i,j,l)$$

> l

$$+\text{max}_{k}[s_{\text{best}}(i,k)+s_{\text{best}}(k,j)]$$

注意，分析器使用的是跨度 (i, j) 的最大标签加上跨度 (i,k) 与 (k, j) 的最大标签，而不考虑这些决策在给定文法下是否合理。在经典句法分析中，文法的作用是帮助约束成分的可能组合（NP 之后倾向于跟 VP）。相比之下，神经模型似乎在从跨度到非终结符的映射过程中学到了这类上下文约束。

> Note that the parser is using the max label for span (i, j) + the max labels for spans(i,k) and (k, j) without worrying about whether those decisions make sense given a grammar. The role of the grammar in classical parsing is to help constrain possible combinations of constituents (NPs like to be followed by VPs). By contrast, the neural model seems to learn these kinds of contextual constraints during its mapping from spans to non-terminals.

关于基于跨度的分析的更多细节，包括基于间隔（margin-based）的训练算法，参见 Stern et al. (2017)、Gaddy et al. (2018)、Kitaev and Klein (2018) 和 Kitaev et al. (2019)。

> For more details on span-based parsing, including the margin-based training algorithm, see Stern et al. (2017), Gaddy et al. (2018), Kitaev and Klein (2018), and Kitaev et al. (2019).

## 19.8 分析器的评估

> 19.8 Evaluating Parsers

评估为句子分配单个解析树的分析器的标准工具是 PARSEVAL 指标（Black et al., 1991）。PARSEVAL 指标衡量

> The standard tool for evaluating parsers that assign a single parse tree to a sentence is the PARSEVAL metrics (Black et al., 1991). The PARSEVAL metric measures

> `PARSEVAL`（PARSEVAL 指标）
>
> 释义：通过比较假设解析树与参考解析树中成分的起点、终点和非终结符是否一致，来评估分析器精确率与召回率的指标体系。

假设解析树中的成分在多大程度上与人工标注的参考分析中的成分相似。因此，PARSEVAL 需要为测试集中的每个句子提供人工标注的参考（或“金标准”）解析树；我们通常从宾州树库（Penn Treebank）这样的树库中获取这些参考分析。

> how much the constituents in the hypothesis parse tree look like the constituents in a hand-labeled, reference parse. PARSEVAL thus requires a human-labeled reference(or “gold standard”) parse tree for each sentence in the test set; we generally draw these reference parses from a treebank like the Penn Treebank.

如果句子 s 的假设分析 Ch 中的某个成分

> A constituent in a hypothesis parse Ch of a sentence s is labeled correct if there
在参考分析 Cr 中存在一个起点、终点和非终结符符号都相同的成分，则该成分被标记为正确。然后我们就可以像之前见过的命名实体标注等任务那样测量精确率和召回率：

> is a constituent in the reference parse Cr with the same starting point, ending point, and non-terminal symbol. We can then measure the precision and recall just as for tasks we’ve seen already like named entity tagging:

带标注召回率：= s 的假设分析中正确成分的数目

> labeled recall: = # of correct constituents in hypothesis parse of s
s 的参考分析中成分的总数目

> # of total constituents in reference parse of s
带标注精确率：= s 的假设分析中正确成分的数目

> labeled precision: = # of correct constituents in hypothesis parse of s
s 的假设分析中成分的总数目

> # of total constituents in hypothesis parse of s

![](images/19-cfg-and-parsing/fig_p20_0.png)

*图 19.16 Collins (1999) 中的一个词汇化树。*
*Figure 19.16 A lexicalized tree from Collins (1999).*

与往常一样，我们通常报告两者的组合，F1：

> As usual, we often report a combination of the two, F1:

F1 = 2PR (19.12)
P+R
此外，我们还对每个句子 s 使用一个新的指标，交叉括号：

> We additionally use a new metric, crossing brackets, for each sentence s:

交叉括号：参考分析中括号结构为

> cross-brackets: the number of constituents for which the reference parse has a
诸如 ((A B) C)，而假设分析中括号结构为 (A (B C)) 的成分的数目。

> bracketing such as ((A B) C) but the hypothesis parse has a bracketing such as (A (B C)).

为了比较使用不同文法的分析器，PARSEVAL 指标包含一个规范化算法，用于去除可能因文法而异的信息（助动词、不定式前的 “to” 等），并计算一个简化得分（Black et al., 1991）。PARSEVAL 指标的规范实现称为 evalb（Sekine and Collins, 1997）。

> For comparing parsers that use different grammars, the PARSEVAL metric includes a canonicalization algorithm for removing information likely to be grammarspecific (auxiliaries, pre-infinitival “to”, etc.) and for computing a simplified score(Black et al., 1991). The canonical implementation of the PARSEVAL metrics is called evalb (Sekine and Collins, 1997).

> `evalb`
>
> 释义：PARSEVAL 指标的规范实现程序，用于计算分析器在带标注精确率、召回率和交叉括号上的得分。

## 19.9 中心词与中心词查找

> 19.9 Heads and Head-Finding

句法成分可以与一个词汇中心词相关联；N 是 NP 的中心词，V 是 VP 的中心词。为每个成分指定中心词这一思想可追溯到 Bloomfield 1914，并且是我们在第 20 章将要介绍的依存文法和依存分析的核心。事实上，中心词可以用作在成分分析与依存分析之间建立映射的一种方式。中心词在概率分析（附录 E）以及基于成分的文法形式体系（如中心词驱动的短语结构文法（Pollard and Sag, 1994））中也很重要。

> Syntactic constituents can be associated with a lexical head; N is the head of an NP, V is the head of a VP. This idea of a head for each constituent dates back to Bloomfield 1914, and is central to the dependency grammars and dependency parsing we’ll introduce in Chapter 20. Indeed, heads can be used as a way to map between constituency and dependency parses. Heads are also important in probabilistic parsing (Appendix E) and in constituent-based grammar formalisms like Head-Driven Phrase Structure Grammar (Pollard and Sag, 1994)..

在一种简单的词汇中心词模型中，每条上下文无关规则都关联一个

> In one simple model of lexical heads, each context-free rule is associated with
中心词（Charniak 1997；Collins 1999）。中心词是短语中在语法上最重要的词。中心词沿着解析树向上传递；因此，解析树中的每个非终结符都标注有一个单词，即其词汇中心词。

> a head (Charniak 1997, Collins 1999). The head is the word in the phrase that is grammatically the most important. Heads are passed up the parse tree; thus, each non-terminal in a parse tree is annotated with a single word, which is its lexical head.

图 19.16 展示了 Collins (1999) 中这样一棵树的示例，其中每个非终结符都标注了其中心词。

> Figure 19.16 shows an example of such a tree from Collins (1999), in which each non-terminal is annotated with its head.

为了生成这样的树，每条 CFG 规则都必须加以扩充，以标识

> For the generation of such a tree, each CFG rule must be augmented to identify
右侧的一个成分为中心词子节点。节点的中心词随后被设为其中心词子节点的中心词。对于教科书中的例子（NN 是 NP 的中心词），选择这些中心词子节点很简单，但对大多数短语而言既复杂，也确有争议。（在不定式动词短语中，标补词 to 还是动词应该作为中心词？）现代句法语言学理论通常包含一个定义中心词的组件（例如参见（Pollard and Sag, 1994））。

> one right-side constituent to be the head child. The headword for a node is then set to the headword of its head child. Choosing these head children is simple for textbook examples (NN is the head of NP) but is complicated and indeed controversial for most phrases. (Should the complementizer to or the verb be the head of an infinite verb phrase?) Modern linguistic theories of syntax generally include a component that defines heads (see, e.g., (Pollard and Sag, 1994)).

寻找中心词的另一种方法用于大多数实用的计算

> An alternative approach to finding a head is used in most practical computational
系统中。不是在文法本身中规定中心词规则，而是在具体句子的解析树上下文中动态识别中心词。换言之，一旦句子被分析，就遍历所得的解析树，为每个节点标注相应的中心词。当前大多数系统依赖一套简单的手写规则，例如 Collins（1999）给出的、适用于宾州树库（Penn Treebank）文法的一套实用规则，它最初由 Magerman（1995）提出。例如，寻找 NP 中心词的规则如下（Collins, 1999, p. 238）：

> systems. Instead of specifying head rules in the grammar itself, heads are identified dynamically in the context of trees for specific sentences. In other words, once a sentence is parsed, the resulting tree is walked to decorate each node with the appropriate head. Most current systems rely on a simple set of handwritten rules, such as a practical one for Penn Treebank grammars given in Collins (1999) but developed originally by Magerman (1995). For example, the rule for finding the head of an NP is as follows (Collins, 1999, p. 238):

> • 若最后一个词的词性标注为 POS，则返回 last-word。
>
> *• If the last word is tagged POS, return last-word.*

> • 否则从右到左查找第一个为 NN、NNP、NNPS、NX、POS 或 JJR 的子节点。
>
> *• Else search from right to left for the first child which is an NN, NNP, NNPS, NX, POS, or JJR.*

> • 否则从左到右查找第一个为 NP 的子节点。
>
> *• Else search from left to right for the first child which is an NP.*

> • 否则从右到左查找第一个为 $、ADJP 或 PRN 的子节点。
>
> *• Else search from right to left for the first child which is a $, ADJP, or PRN.*

> • 否则从右到左查找第一个为 CD 的子节点。
>
> *• Else search from right to left for the first child which is a CD.*

> • 否则从右到左查找第一个为 JJ、JJS、RB 或 QP 的子节点。
>
> *• Else search from right to left for the first child which is a JJ, JJS, RB or QP.*

> • 否则返回最后一个词
>
> *• Else return the last word*

该规则集中的其他部分规则见图 19.17。例如，对于 VP

> Selected other rules from this set are shown in Fig. 19.17. For example, for VP
形如 VP →Y1 ··· Yn 的规则，算法会从 Y1 ···Yn 的左侧开始，查找第一个类型为 TO 的 Yi；若没有找到 TO，则查找第一个类型为 VBD 的 Yi；若没有找到 VBD，则查找 VBN，依此类推。

> rules of the form VP →Y1 ··· Yn, the algorithm would start from the left of Y1 ···Yn looking for the first Yi of type TO; if no TOs are found, it would search for the first Yi of type VBD; if no VBDs are found, it would search for a VBN, and so on.

更多细节参见 Collins（1999）。

> See Collins (1999) for more details.

<!--figbox-->
> 父节点 方向 优先级列表 ADJP 左 NNS QP NN $ ADVP JJ VBN VBG ADJP JJR NP JJS DT FW RBR RBS
>
> *Parent Direction Priority List ADJP Left NNS QP NN $ ADVP JJ VBN VBG ADJP JJR NP JJS DT FW RBR RBS*

> SBAR RB

> ADVP 右 RB RBR RBS FW ADVP TO CD JJR JJ IN NP JJS NN PRN 左 PRT 右 RP QP 左 $ IN NNS NN JJ RB DT CD NCD QP JJR JJS S 左 TO IN VP S SBAR ADJP UCP NP SBAR 左 WHNP WHPP WHADVP WHADJP IN DT S SQ SINV SBAR FRAG VP 左 TO VBD VBN MD VBZ VB VBG VBP VP ADJP NN NNS NP
>
> *ADVP Right RB RBR RBS FW ADVP TO CD JJR JJ IN NP JJS NN PRN Left PRT Right RP QP Left $ IN NNS NN JJ RB DT CD NCD QP JJR JJS S Left TO IN VP S SBAR ADJP UCP NP SBAR Left WHNP WHPP WHADVP WHADJP IN DT S SQ SINV SBAR FRAG VP Left TO VBD VBN MD VBZ VB VBG VBP VP ADJP NN NNS NP*
<!--/figbox-->

*图 19.17 取自 Collins（1999）的部分中心词规则。中心词规则也称为中心词渗透表。*
*Figure 19.17 Some head rules from Collins (1999). The head rules are also called a head percolation table.*

## 19.10 小结

> 19.10 Summary

本章介绍了成分句法分析。以下是主要内容的总结：

> This chapter introduced constituency parsing. Here’s a summary of the main points:

- 在许多语言中，连续的若干词作为一个组或一个成分起作用，这可以用上下文无关文法（也称为短语结构文法）来建模。
- 上下文无关文法由一组规则（或称产生式）组成，这些规则建立在一组非终结符和一组终结符之上。形式上，一个特定的上下文无关语言是可以从某个特定上下文无关文法推导出的字符串集合。

> In many languages, groups of consecutive words act as a group or a constituent, which can be modeled by context-free grammars (which are also known as phrase-structure grammars).
> A context-free grammar consists of a set of rules or productions, expressed over a set of non-terminal symbols and a set of terminal symbols. Formally, a particular context-free language is the set of strings that can be derived from a particular context-free grammar.

- 结构歧义是分析器面临的一个重要问题。结构歧义的常见来源包括 PP 附着歧义和并列歧义。
- 动态规划分析算法（如 CKY）使用部分分析结果的表格来高效地分析有歧义的句子。
- CKY 把文法的形式限制为乔姆斯基范式（CNF）。
- 基本的 CKY 算法紧凑地表示句子的所有可能分析，但不选出单一的最佳分析。
- 从所有可能分析中选出单一分析（消歧）可以由神经成分分析器完成。
- 基于跨度的神经成分分析器训练一个神经分类器为每个成分打分，然后使用修改版的 CKY 组合这些成分得分，以找出得分最佳的解析树。
- 分析器用三个指标评价：带标注召回率、带标注精确率和交叉括号。
- 部分分析和组块（chunking）是识别文本中浅层句法成分的方法。它们由在句法标注数据上训练的序列模型来解决。

> Structural ambiguity is a significant problem for parsers. Common sources of structural ambiguity include PP-attachment and coordination ambiguity.
> Dynamic programming parsing algorithms, such as CKY, use a table of partial parses to efficiently parse ambiguous sentences.
> CKY restricts the form of the grammar to Chomsky normal form (CNF).
> The basic CKY algorithm compactly represents all possible parses of the sentence but doesn’t choose a single best parse.
> Choosing a single parse from all possible parses (disambiguation) can be done by neural constituency parsers.
> Span-based neural constituency parses train a neural classifier to assign a score to each constituent, and then use a modified version of CKY to combine these constituent scores to find the best-scoring parse tree.
> Parsers are evaluated with three metrics: labeled recall, labeled precision, and cross-brackets.
> Partial parsing and chunking are methods for identifying shallow syntactic constituents in a text. They are solved by sequence models trained on syntactically-annotated data.

## 历史注记

> Historical Notes

据 Percival（1976），把句子分解为成分层级的想法出现在富有开创性的心理学家 Wilhelm Wundt 的著作 Völkerpsychologie 中（Wundt, 1900）：

> According to Percival (1976), the idea of breaking up a sentence into a hierarchy of constituents appeared in the V¨olkerpsychologie of the groundbreaking psychologist Wilhelm Wundt (Wundt, 1900):

...den sprachlichen Ausdruck für die willkürliche Gliederung einer Gesammtvorstellung in ihre in logische Beziehung zueinander gesetzten Bestandteile

> ...den sprachlichen Ausdruck f¨ur die willk¨urliche Gliederung einer Gesammtvorstellung in ihre in logische Beziehung zueinander gesetzten Bestandteile
[把总体观念任意划分成

> [the linguistic expression for the arbitrary division of a total idea
彼此处于逻辑关系中的各组成部分的语言表达]

> into its constituent parts placed in logical relations to one another]
Wundt 的成分思想被 Leonard Bloomfield 在其早期著作 An Introduction to the Study of Language 中引入语言学（Bloomfield, 1914）。

> Wundt’s idea of constituency was taken up into linguistics by Leonard Bloomfield in his early book An Introduction to the Study of Language (Bloomfield, 1914).

到他的后期著作《语言》（Language，Bloomfield, 1933）问世之时，当时所谓的“直接成分分析”已成为美国句法研究中一种成熟的方法。相比之下，可追溯到古典时期的欧洲传统文法定义的是词与词之间的关系，而不是成分之间的关系，欧洲句法学家一直保留着对这种依存文法的重视，这正是第 20 章的主题。（实际上，依存文法和成分文法在不同时期都曾在计算语言学中风行。）

> By the time of his later book, Language (Bloomfield, 1933), what was then called“immediate-constituent analysis” was a well-established method of syntactic study in the United States. By contrast, traditional European grammar, dating from the Classical period, defined relations between words rather than constituents, and European syntacticians retained this emphasis on such dependency grammars, the subject of Chapter 20. (And indeed, both dependency and constituency grammars have been in vogue in computational linguistics at different times).
美国结构主义提出了若干关于直接成分的具体定义，

> American Structuralism saw a number of specific definitions of the immediate
其表述基于他们对“发现程序”的追寻：一种用于描写一种语言句法的方法论算法。总体而言，这些定义试图抓住这样一种直觉：“直接成分的首要标准是各组合在多大程度上表现得像简单单位”（Bazell, 1952/1966, p. 284）。这些具体定义中最为人所知的是 Harris 的与单个单位在分布上相似的思想，即替换测试。本质上，该方法通过尝试用简单结构替换可能的成分，把一个结构切分为若干成分——如果某个简单形式（例如 man）能在结构中替换一个更复杂的组合（如 intense young man），那么这个形式 intense young man 很可能就是一个成分。Harris 的测试是“成分是一种等价类”这一直觉的开端。

> constituent, couched in terms of their search for a “discovery procedure”: a methodological algorithm for describing the syntax of a language. In general, these attempt to capture the intuition that “The primary criterion of the immediate constituent is the degree in which combinations behave as simple units” (Bazell, 1952/1966, p. 284). The most well known of the specific definitions is Harris’ idea of distributional similarity to individual units, with the substitutability test. Essentially, the method proceeded by breaking up a construction into constituents by attempting to substitute simple structures for possible constituents—if a substitution of a simple form, say, man, was substitutable in a construction for a more complex set (like intense young man), then the form intense young man was probably a constituent. Harris’s test was the beginning of the intuition that a constituent is a kind of equivalence class.

上下文无关文法是对这种层级成分思想的形式化，

> The context-free grammar was a formalization of this idea of hierarchical
其定义见于 Chomsky（1956），并在 Chomsky（1957）与 Chomsky（1956/1975）中得到进一步扩展（以及被反驳）。在 Chomsky 最初的工作之后不久，上下文无关文法被 Backus（1959）重新发明，并由 Naur 等人（1960）在描述 ALGOL 程序设计语言时独立地重新发明；Backus（1996）指出，他受到了 Emil Post 的产生式的影响，而 Naur 的工作独立于他（Backus）本人的工作。在这些早期工作之后，由于高效分析算法的早期发展，大量自然语言处理的计算模型都基于上下文无关文法。

> constituency defined in Chomsky (1956) and further expanded upon (and argued against) in Chomsky (1957) and Chomsky (1956/1975). Shortly after Chomsky’s initial work, the context-free grammar was reinvented by Backus (1959) and independently by Naur et al. (1960) in their descriptions of the ALGOL programming language; Backus (1996) noted that he was influenced by the productions of Emil Post and that Naur’s work was independent of his (Backus’) own. After this early work, a great number of computational models of natural language processing were based on context-free grammars because of the early development of efficient parsing algorithms.

动态规划分析有一段被独立发现的历史。据已故的 Martin Kay（私人交流），一个包含 CKY 算法雏形的动态规划分析器最早由 John Cocke 于 1960 年实现。后续工作扩展并形式化了该算法，并证明了其时间复杂度（Kay 1967, Younger 1967, Kasami 1965）。与此相关的合式子串表（wellformed substring table, WFST）似乎是由

> Dynamic programming parsing has a history of independent discovery. According to the late Martin Kay (personal communication), a dynamic programming parser containing the roots of the CKY algorithm was first implemented by John Cocke in 1960. Later work extended and formalized the algorithm, as well as proving its time complexity (Kay 1967, Younger 1967, Kasami 1965). The related wellformed substring table (WFST) seems to have been independently proposed by

> `WFST`（合式子串表）
>
> 释义：分析过程中存储此前所有计算结果的数据结构，用于避免重复计算。

Kuno（1965）独立提出的，作为一种在分析过程中存储此前所有计算结果的数据结构。基于对 Cocke 工作的推广，Kay（1967）（以及 Kay 1973）也独立描述了类似的数据结构。把动态规划自顶向下地应用于分析，由 Earley 的博士论文给出（Earley 1968, Earley 1970）。Sheil（1976）证明了 WFST 与 Earley 算法的等价性。Norvig（1991）表明，动态规划所提供的效率可以在任何具有记忆化函数的语言（例如 LISP）中获得，只需把记忆化操作包裹在一个简单的自顶向下分析器外面即可。

> Kuno (1965) as a data structure that stores the results of all previous computations in the course of the parse. Based on a generalization of Cocke’s work, a similar data structure had been independently described in Kay (1967) (and Kay 1973). The top-down application of dynamic programming to parsing was described in Earley’s Ph.D. dissertation (Earley 1968, Earley 1970). Sheil (1976) showed the equivalence of the WFST and the Earley algorithm. Norvig (1991) shows that the efficiency offered by dynamic programming can be captured in any language with a memoization function (such as in LISP) simply by wrapping the memoization operation around a simple top-down parser.

最早用于分析的消歧算法基于概率

> The earliest disambiguation algorithms for parsing were based on probabilistic

> `probabilistic context-free grammars`（概率上下文无关文法）
>
> 释义：为每条规则赋予概率、以规则概率的乘积给解析树打分的文法，用于在多个分析中选优。

上下文无关文法，最早由 Booth（1969）和 Salomaa（1969）研究出来；参见

> context-free grammars, first worked out by Booth (1969) and Salomaa (1969); see
更多历史见附录 E。神经网络方法最早被应用于句法分析，其时间与统计句法分析方法的提出大致相同（Henderson, 1994）。在最早的工作中，神经网络被用来估计统计成分句法分析器的部分概率（Henderson, 2003, 2004; Emami and Jelinek, 2005）。此后数十年间出现了多种多样的神经网络句法分析算法，包括递归神经网络架构（Socher et al., 2011, 2013）、编码器-解码器模型（Vinyals et al., 2015; Choe and Charniak, 2016），以及聚焦于跨度的思路（Cross and Huang, 2016）。关于本章所描述的基于跨度的自注意力方法，更多内容参见 Stern et al. (2017)、Gaddy et al. (2018)、Kitaev and Klein (2018) 和 Kitaev et al. (2019)。神经网络依存句法分析的并行历史见第 20 章。

> Appendix E for more history. Neural methods were first applied to parsing at around the same time as statistical parsing methods were developed (Henderson, 1994). In the earliest work neural networks were used to estimate some of the probabilities for statistical constituency parsers (Henderson, 2003, 2004; Emami and Jelinek, 2005). The next decades saw a wide variety of neural parsing algorithms, including recursive neural architectures (Socher et al., 2011, 2013), encoder-decoder models(Vinyals et al., 2015; Choe and Charniak, 2016), and the idea of focusing on spans(Cross and Huang, 2016). For more on the span-based self-attention approach we describe in this chapter see Stern et al. (2017), Gaddy et al. (2018), Kitaev and Klein(2018), and Kitaev et al. (2019). See Chapter 20 for the parallel history of neural dependency parsing.

句法分析算法的经典参考文献是 Aho and Ullman (1972)；尽管

> The classic reference for parsing algorithms is Aho and Ullman (1972); although
该书关注的是计算机语言，但其中大多数算法都已被应用于自然语言。

> the focus of that book is on computer languages, most of the algorithms have been applied to natural language.

## 练习

> Exercises

19.1 实现将任意上下文无关文法转换为 CNF 的算法。

> 19.1 Implement the algorithm to convert arbitrary context-free grammars to CNF.

将你的程序应用于 L1 文法。

> Apply your program to the L1 grammar.

19.2 实现 CKY 算法，并用你转换后的 L1 文法对它进行测试。19.3 重写第 438 页图 19.12 中给出的 CKY 算法，使其能够

> 19.2 Implement the CKY algorithm and test it with your converted L1 grammar. 19.3 Rewrite the CKY algorithm given in Fig. 19.12 on page 438 so that it can
接受包含单元产生式的文法。

> accept grammars that contain unit productions.

19.4 讨论如何扩充分析器，以处理可能不正确的输入，例如

> 19.4 Discuss how to augment a parser to deal with input that may be incorrect, for
包含拼写错误或由自动语音识别所产生的错误的输入。

> example, containing spelling errors or mistakes arising from automatic speech recognition.

19.5 实现 19.8 节中描述的 PARSEVAL 指标。接下来，使用一个

> 19.5 Implement the PARSEVAL metrics described in Section 19.8. Next, use a
分析器和一个树库，将你的指标与标准实现进行比较。分析你的方法中出现的错误。

> parser and a treebank, compare your metrics against a standard implementation. Analyze the errors in your approach.
