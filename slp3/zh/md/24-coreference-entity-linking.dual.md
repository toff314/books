# 第 24 章 共指消解与实体链接

### 章

> CHAPTER

# 24 共指消解与实体链接

> 24 Coreference Resolution and Entity Linking

> 甚至连那位爱国的坎特伯雷大主教 Stigand 也觉得它可取——”’
>
> *and even Stigand, the patriotic archbishop of Canterbury, found it advisable–”’*

> “找到了什么？”鸭子说。
>
> *‘Found WHAT?’ said the Duck.*

> “找到了它，”老鼠相当恼怒地回答，“你当然知道‘它’是什么意思。”
>
> *‘Found IT,’ the Mouse replied rather crossly: ‘of course you know what “it”means.’*

> “当我找到一样东西时，我完全知道‘它’是什么意思，”鸭子说，“它通常是青蛙或虫子。问题是，那位大主教找到了什么？”
>
> *‘I know what “it”means well enough, when I find a thing,’ said the Duck: ‘it’s generally a frog or a worm. The question is, what did the archbishop find?’*

> Lewis Carroll，《爱丽丝漫游奇境记》
>
> *Lewis Carroll, Alice in Wonderland*

语言处理的一个重要组成部分是知道文本中正在谈论的是谁。请看下面这段文字：

> An important component of language processing is knowing who is being talked about in a text. Consider the following passage:

（24.1）Victoria Chen，Megabucks Banking 的首席财务官，眼看自己的薪酬跃升至 2.3

> (24.1) Victoria Chen, CFO of Megabucks Banking, saw her pay jump to $2.3
百万美元，这位 38 岁的人成了该公司的总裁。众所周知，她是从竞争对手 Lotsabucks 来到 Megabucks 的。

> million, as the 38-year-old became the company’s president. It is widely known that she came to Megabucks from rival Lotsabucks.

这段文字中每一个加下划线的短语，都是作者用来指称

> Each of the underlined phrases in this passage is used by the writer to refer to
一个名叫 Victoria Chen 的人。我们把像 her 或 Victoria Chen 这样的语言表达式称为提及或指称表达式，而把被指称的话语实体

> a person named Victoria Chen. We call linguistic expressions like her or Victoria Chen mentions or referring expressions, and the discourse entity that is referred

> `mention referent`（提及；所指对象）
>
> 释义：提及是用于指称某个实体的语言表达式，所指对象则是它在话语模型中所指向的那个实体。

（Victoria Chen）称为所指对象。（为了区分指称表达式与

> to (Victoria Chen) the referent. (To distinguish between referring expressions and
它们的所指对象，我们给前者加上斜体。）1 两个或更多用来指称同一话语实体的指称表达式被称为共指；因此，Victoria Chen

> their referents, we italicize the former.)1 Two or more referring expressions that are used to refer to the same discourse entity are said to corefer; thus, Victoria Chen

> `corefer`（共指）
>
> 释义：指两个或更多指称表达式在话语模型中指向同一话语实体，如 (24.1) 中的 Victoria Chen 与 she。

和 she 在（24.1）中构成共指。

> and she corefer in (24.1).

共指是自然语言处理的一个重要组成部分。一个刚刚告诉用户“美联航有一班下午 2 点的航班，国泰航空有一班下午 4 点的航班”的对话系统，必须知道用户说“我要第二班”时指的是哪一班航班。一个用维基百科来回答关于 Marie Curie 的问题的问答系统，必须知道“She was born in Warsaw”这句话中的 she 指的是谁。而一个从西班牙语这类可以省略代词的语言进行翻译的机器翻译系统，则必须利用上一句的共指信息来决定西班牙语句子‘“Me encanta el conocimiento”, dice.’ 应当译成‘“I love knowledge”, he says’，还是‘“I love knowledge”, she says’。

> Coreference is an important component of natural language processing. A dialogue system that has just told the user “There is a 2pm flight on United and a 4pm one on Cathay Pacific” must know which flight the user means by “I’ll take the second one”. A question answering system that uses Wikipedia to answer a question about Marie Curie must know who she was in the sentence “She was born in Warsaw”. And a machine translation system translating from a language like Spanish, in which pronouns can be dropped, must use coreference from the previous sentence to decide whether the Spanish sentence ‘“Me encanta el conocimiento”, dice.’ should be translated as ‘“I love knowledge”, he says’, or ‘“I love knowledge”, she says’.

事实上，这个例子来自《El País》上一篇关于一位女教授的真实的新闻报道，由于共指消解不准确，它在机器翻译中被误译成了“he”（Schiebinger, 2013）。

> Indeed, this example comes from an actual news article in El Pa´ıs about a female professor and was mistranslated as “he” in machine translation because of inaccurate coreference resolution (Schiebinger, 2013).

自然语言处理系统（以及人类）是相对于话语模型来解释语言表达式的（Karttunen, 1969）。话语模型

> Natural language processing systems (and humans) interpret linguistic expressions with respect to a discourse model (Karttunen, 1969). A discourse model

> `discourse model`（话语模型）
>
> 释义：理解者在解读文本时逐步构建的心理模型，包含文本所提及实体的表示，以及实体的属性和它们之间的关系。

（图 24.1）是理解者在解读文本时逐步构建的心理模型，其中包含文本所提及实体的表示，以及实体的属性和它们之间的关系。当某个所指对象在话语中首次被提及时，我们说它的表示被唤起进入

> (Fig. 24.1) is a mental model that the understander builds incrementally when interpreting a text, containing representations of the entities referred to in the text, as well as properties of the entities and relations among them. When a referent is first mentioned in a discourse, we say that a representation for it is evoked into the

> `evoked accessed`（唤起；访问）
>
> 释义：前者指所指对象首次被提及时其表示被引入话语模型，后者指此后再次提及时从模型中取用该表示。

模型。在随后的提及中，这一表示从模型中被访问。

> model. Upon subsequent mention, this representation is accessed from the model.

> 作为一种方便的简略说法，我们有时说指称表达式指称某个所指对象，例如，
>
> *As a convenient shorthand, we sometimes speak of a referring expression referring to a referent, e.g.,*

![](images/24-coreference-entity-linking/fig_p2_0.png)

*图 24.1 提及如何在话语模型中唤起和访问话语实体。*
*Figure 24.1 How mentions evoke and access discourse entities in a discourse model.*

文本中对先前已引入

> Reference in a text to an entity that has been previously introduced into the
话语的某个实体的指称称为回指，而所使用的指称表达式被称为

> discourse is called anaphora, and the referring expression used is said to be an

> `anaphora anaphor`（回指；回指语）
>
> 释义：回指是文本中指称先前已引入话语的实体，回指语则是执行这种指称的那个指称表达式。

回指语，或回指性的。2 在（24.1）这段文字中，代词 she 和 her 以及定指 NP the 38-year-old 因此都是回指性的。回指语与先前的一个提及（在此例中是 Victoria Chen）构成共指，该提及被称为先行语。并非每一个指称

> anaphor, or anaphoric.2 In passage (24.1), the pronouns she and her and the definite NP the 38-year-old are therefore anaphoric. The anaphor corefers with a prior mention (in this case Victoria Chen) that is called the antecedent. Not every refer-

> `antecedent`（先行语）
>
> 释义：与后面出现的回指语构成共指的那个先前的提及，回指语通过它来确定所指对象。

表达式都是先行语。在文本中只有一个提及的实体（如（24.1）中的 Lotsabucks）称为单例。

> ring expression is an antecedent. An entity that has only a single mention in a text(like Lotsabucks in (24.1)) is called a singleton.

> `singleton coreference resolution`（单例；共指消解）
>
> 释义：单例是文本中仅出现一次的实体，共指消解则是判定两个提及是否指向同一话语实体的任务。

本章我们关注共指消解这一任务。共指消解

> In this chapter we focus on the task of coreference resolution. Coreference
是判定两个提及是否共指的任务，我们所说的共指指的是它们指向话语模型中的同一实体（同一话语实体）。

> resolution is the task of determining whether two mentions corefer, by which we mean they refer to the same entity in the discourse model (the same discourse entity).

> `coreference chain`（共指链）
>
> 释义：一组互相共指的指称表达式构成的集合，也称簇，即同一实体在文本中的所有提及。

这组共指的指称表达式通常被称为共指链或簇。

> The set of coreferring expressions is often called a coreference chain or a cluster.

例如，在处理（24.1）时，共指消解算法需要

> For example, in processing (24.1), a coreference resolution algorithm would need

> `cluster`（簇）
>
> 释义：共指链的另一种称呼，指指向同一话语实体的一组指称表达式。

找出至少四条共指链，对应图 24.1 话语模型中的四个实体。

> to find at least four coreference chains, corresponding to the four entities in the discourse model in Fig. 24.1.

- {Victoria Chen, her, the 38-year-old, She}
- {Megabucks Banking, the company, Megabucks}
- {her pay}
- {Lotsabucks} 注意，提及可以嵌套；例如提及 her 在句法上

> {Victoria Chen, her, the 38-year-old, She}
> {Megabucks Banking, the company, Megabucks}
> {her pay}
> {Lotsabucks} Note that mentions can be nested; for example the mention her is syntactically

是另一个提及 her pay 的一部分，而后者指称一个完全不同的话语实体。

> part of another mention, her pay, referring to a completely different discourse entity.

因此，共指消解包含两个任务（尽管它们通常联合完成）：（1）识别提及，（2）将它们聚类为共指链/话语实体。

> Coreference resolution thus comprises two tasks (although they are often performed jointly): (1) identifying the mentions, and (2) clustering them into coreference chains/discourse entities.

我们 _3 说过，如果两个提及与同一话语实体相关联，那么它们就是共指的。但我们常常希望更进一步，确定与这个话语实体相关联的是哪个现实世界实体。例如，提及 Washington 可能指美国的一个州，或首都，或人物 George Washington；对这些不同的所指，句子的解释自然大不相同。实体链接（Ji and Grishman, 2011）或实体消解的任务，就是把

> We _3said that two mentions corefered if they are associated with the same discourse entity. But often we’d like to go further, deciding which real world entity is associated with this discourse entity. For example, the mention Washington might refer to the US state, or the capital city, or the person George Washington; the interpretation of the sentence will of course be very different for each of these. The task of entity linking (Ji and Grishman, 2011) or entity resolution is the task of mapping

> `entity linking`（实体链接）
>
> 释义：指把文本中出现的提及映射到知识库中某个具体实体的表示，从而确定其指向的现实对象。

a_2 话语实体映射到某个现实世界个体。3 我们通常把实体

> a_2 discourse entity to some real-world individual.3 We usually operationalize entity
链接或消解，即映射到一个本体：世界上实体的列表，如地名词典（附录 H）。这项任务最常用的本体大概就是 Wikipedia；每个 Wikipedia 页面充当某个特定实体的唯一 id。因此，维基化（Mihalcea and Csomai, 2007）这一实体链接任务，就是确定某个提及所指的是与某个个体对应的哪个 Wikipedia 页面。不过，实体链接可以用任何本体来完成；例如，如果我们有一个基因本体，就可以把文本中基因的提及链接到该本体中消歧后的基因名称。

> linking or resolution by mapping to an ontology: a list of entities in the world, like a gazeteer (Appendix H). Perhaps the most common ontology used for this task is Wikipedia; each Wikipedia page acts as the unique id for a particular entity. Thus the entity linking task of wikification (Mihalcea and Csomai, 2007) is the task of deciding which Wikipedia page corresponding to an individual is being referred to by a mention. But entity linking can be done with any ontology; for example if we have an ontology of genes, we can link mentions of genes in text to the disambiguated gene name in the ontology.

> 我们将遵循 NLP 中 anaphor 的常见用法，即指任何具有先行语的提及，而不是更狭义的用法——只指那些解释依赖于先行语的提及（如代词）（在狭义解释下，重复出现的名称不是回指语）。
>
> *We will follow the common NLP usage of anaphor to mean any mention that has an antecedent, rather than the more narrow usage to mean only mentions (like pronouns) whose interpretation depends on the antecedent (under the narrower interpretation, repeated names are not anaphors).*

> 因此，计算语言学/NLP 在使用 reference 这一术语上与形式语义学领域不同，后者用 reference 和 coreference 这两个词来描述提及与现实世界实体之间的关系。相比之下，我们遵循功能语言学传统，其中提及指称话语实体（Webber, 1978），而话语实体与现实世界之间的关系
>
> *Computational linguistics/NLP thus differs in its use of the term reference from the field of formal semantics, which uses the words reference and coreference to describe the relation between a mention and a real-world entity. By contrast, we follow the functional linguistics tradition in which a mention refers to a discourse entity (Webber, 1978) and the relation between a discourse entity and the real world*

在接下来的几节中，我们将更详细地介绍共指消解任务，并综述各种消解架构。我们还会介绍两种用于实体链接任务的架构。

> In the next sections we introduce the task of coreference resolution in more detail, and survey a variety of architectures for resolution. We also introduce two architectures for the task of entity linking.

不过，在转向算法之前，我们先提及一些重要任务，我们

> Before turning to algorithms, however, we mention some important tasks we
只会到本章末尾才简要涉及。首先是著名的 Winograd 模式问题（之所以这样称呼，是因为 Terry Winograd 在其学位论文中首次指出了它们）。这些实体共指消解问题被设计得极为困难，无法用本章所描述的消解方法解决，而它们所需的那类现实世界知识，使它们成为自然语言处理的一类挑战性任务。例如，考虑确定下例中代词 they 的正确先行语这一任务：

> will only touch on briefly at the end of this chapter. First are the famous Winograd Schema problems (so-called because they were first pointed out by Terry Winograd in his dissertation). These entity coreference resolution problems are designed to be too difficult to be solved by the resolution methods we describe in this chapter, and the kind of real-world knowledge they require has made them a kind of challenge task for natural language processing. For example, consider the task of determining the correct antecedent of the pronoun they in the following example:

（24.2）市议会拒绝给示威者发放许可，因为

> (24.2) The city council denied the demonstrators a permit because

- 他们害怕暴力。
- 他们鼓吹暴力。

> they feared violence.
> they advocated violence.

确定代词 they 的正确先行语需要理解

> Determining the correct antecedent for the pronoun they requires understanding
第二个分句意在作为第一个分句的解释，并且市议会也许比示威者更可能害怕暴力，而示威者也许更可能主张暴力。解决 Winograd 模式问题需要找到表示或发现所需现实世界知识的方法。

> that the second clause is intended as an explanation of the first clause, and also that city councils are perhaps more likely than demonstrators to fear violence and that demonstrators might be more likely to advocate violence. Solving Winograd Schema problems requires finding way to represent or discover the necessary real world knowledge.

本章不讨论的一个问题是相关的事件共指任务，即判断两个事件提及（例如下面两句话中的 buy 和 acquisition

> A problem we won’t discuss in this chapter is the related task of event coreference, deciding whether two event mentions (such as the buy and the acquisition in

> `event`（事件）
>
> 释义：在本书中，指文本里表示某种发生或状态的事件提及，可以是动词性的，也可以是名词性的。

> `coreference`（共指）
>
> 释义：两个提及与同一话语实体相关联、即指称同一个现实对象的关系。

均出自 ECB+ 语料库）是否指同一事件：（24.3）AMD 同意以约 $5.4 billion 收购位于安大略省 Markham 的 [buy] ATI

> these two sentences from the ECB+ corpus) refer to the same event:(24.3) AMD agreed to [buy] Markham, Ontario-based ATI for around $5.4 billion
以现金和股票支付，两家公司于周一宣布。

> in cash and stock, the companies announced Monday.

（24.4）这次 [acquisition] 将使 AMD 成为世界最大的供应商之一

> (24.4) The [acquisition] would turn AMD into one of the world’s largest providers
（即）图形芯片。

> of graphics chips.

事件提及比实体提及难检测得多，因为它们既可以是动词性的，也可以是名词性的。一旦检测出来，用于实体的那套提及对模型和提及排序模型往往也被应用于事件。

> Event mentions are much harder to detect than entity mentions, since they can be verbal as well as nominal. Once detected, the same mention-pair and mention-ranking models used for entities are often applied to events.

一种更为复杂的共指是话语指示（Webber, 1988），

> An even more complex kind of coreference is discourse deixis (Webber, 1988),

> `discourse deixis`（话语指示）
>
> 释义：回指语指向前面的一个话语片段（如命题、言语行为），而非指向某个实体的现象。

其中回指语指向前面的一个话语片段，而话语片段往往很难界定或归类，如（24.5）中改编自 Webber (1991) 的这些例子：

> in which an anaphor refers back to a discourse segment, which can be quite hard to delimit or categorize, like the examples in (24.5) adapted from Webber (1991):

（24.5）据 Soleil 说，Beau 刚刚开了一家餐馆

> (24.5) According to Soleil, Beau just opened a restaurant

- 但那结果是个谎言。
- 但那是假的。
- 我觉得那是一种描述该情况的滑稽方式。

> But that turned out to be a lie.
> But that was false.
> That struck me as a funny way to describe the situation.

在（24.5a）中 that 的所指对象是一个言语行为（见第 26 章），在（24.5b）中是一个命题，在（24.5c）中是一种描述方式。本章不给出针对这类困难的非名词性先行语的算法，综述请参见 Kolhatkar et al. (2018)。

> The referent of that is a speech act (see Chapter 26) in (24.5a), a proposition in(24.5b), and a manner of description in (24.5c). We don’t give algorithms in this chapter for these difficult types of non-nominal antecedents, but see Kolhatkar et al. (2018) for a survey.

## 24.1 共指现象：语言学背景

> 24.1 Coreference Phenomena: Linguistic Background

下面我们给出一些关于指称现象的语言学背景。我们介绍四种指称表达式类型（定指和不定指 NP、代词和名称），描述它们如何用于唤起和访问话语模型中的实体，并讨论回指语/先行语关系的语言学特征（如数/性一致，或动词语义特性）。

> We now offer some linguistic background on reference phenomena. We introduce the four types of referring expressions (definite and indefinite NPs, pronouns, and names), describe how these are used to evoke and access entities in the discourse model, and talk about linguistic features of the anaphor/antecedent relation (like number/gender agreement, or properties of verb semantics).

### 24.1.1 指称表达式的类型

> 24.1.1 Types of Referring Expressions

不定名词短语：英语中最常见的不定指称形式由限定词 a（或 an）标记，但它也可以用诸如 some 这样的量化词、甚至限定词 this 来标记。不定指称通常向话语语境引入听话者尚不熟悉的实体。

> Indefinite Noun Phrases: The most common form of indefinite reference in English is marked with the determiner a (or an), but it can also be marked by a quantifier such as some or even the determiner this. Indefinite reference generally introduces into the discourse context entities that are new to the hearer.

（24.6）a. Mrs. Martin 非常友善，送了 Mrs. Goddard 一只漂亮的鹅。

> (24.6) a. Mrs. Martin was so very kind as to send Mrs. Goddard a beautiful goose.

- 有一天他过去给她带了些核桃。
- 我今天看到了这颗漂亮的花椰菜。

> He had gone round one day to bring her some walnuts.
> I saw this beautiful cauliflower today.

定名词短语：定指称，例如通过使用英语冠词 the 的 NP，指称听话者可以识别的实体。某个实体之所以对听话者是可识别的，是因为它此前已在文本中被提及，因而已在话语模型中得到表示：

> Definite Noun Phrases: Definite reference, such as via NPs that use the English article the, refers to an entity that is identifiable to the hearer. An entity can be identifiable to the hearer because it has been mentioned previously in the text and thus is already represented in the discourse model:

（24.7）它涉及一匹白马，我已把它卖给了一位军官。但这份血统

> (24.7) It concerns a white stallion which I have sold to an officer. But the pedigree
这匹白马的血统并未完全确立。

> of the white stallion was not fully established.

或者，某个实体之所以可识别，是因为它包含在听话者的

> Alternatively, an entity can be identifiable because it is contained in the hearer’s
关于世界的一组信念，或者该对象的唯一性由描述本身所蕴含——在后一种情况下，它会把所指对象的一个表示引入话语模型，如 (24.9) 所示：

> set of beliefs about the world, or the uniqueness of the object is implied by the description itself, in which case it evokes a representation of the referent into the discourse model, as in (24.9):

(24.8) 我在《纽约时报》上读到过它。(24.9) 你看见车钥匙了吗？

> (24.8) I read about it in the New York Times.(24.9) Have you seen the car keys?

后面这几种用法相当常见；新闻专线文本中超过半数的定指 NP

> These last uses are quite common; more than half of definite NPs in newswire
都是非回指的，这往往是因为它们是某个实体第一次被提及（Poesio and Vieira 1998, Bean and Riloff 1999）。

> texts are non-anaphoric, often because they are the first time an entity is mentioned(Poesio and Vieira 1998, Bean and Riloff 1999).

代词：定指指称的另一种形式是代词化，用于话语中显著性极高的实体（我们将在下文讨论）：

> Pronouns: Another form of definite reference is pronominalization, used for entities that are extremely salient in the discourse, (as we discuss below):

(24.10) Emma 尽可能愉快地微笑着、聊着天，

> (24.10) Emma smiled and chatted as cheerfully as she could,
代词也可以参与后指，即它们先于

> Pronouns can also participate in cataphora, in which they are mentioned before

> `cataphora`（后指）
>
> 释义：回指语出现在其所指对象之前的一种指称现象，与回指的方向相反。

其所指对象被提及，如 (24.11) 所示。

> their referents are, as in (24.11).

(24.11) 甚至在看到它之前，Dorothy 就一直在想着 Emerald City

> (24.11) Even before she saw it, Dorothy had been thinking about the Emerald City
每一天。

> every day.

这里，代词 she 和 it 都出现在其先行语被引入之前。

> Here, the pronouns she and it both occur before their referents are introduced.

代词也会出现在量化语境中，此时它们被认为是

> Pronouns also appear in quantified contexts in which they are considered to be
受约束的，如 (24.12) 所示。

> bound, as in (24.12).

> `bound`（受约束）
>
> 释义：代词在量化语境中不指向具体实体，而是像与量化表达式绑定的变量那样解释。

(24.12) 每位舞者都把她的左臂向前伸出。

> (24.12) Every dancer brought her left arm forward.

在相关的解读下，her 并不指语境中的某个女性，而更像是一个与量化表达式 every dancer 绑定的变量。本章不讨论代词的受约束解读。

> Under the relevant reading, her does not refer to some woman in context, but instead behaves like a variable bound to the quantified expression every dancer. We are not concerned with the bound interpretation of pronouns in this chapter.

在某些语言中，代词可以作为附着于某个词的附着词出现，如

> In some languages, pronouns can appear as clitics attached to a word, like lo
（‘它’）在下面这个取自 AnCora 的西班牙语例子中（Recasens and Mart´ı, 2010）：

> (‘it’) in this Spanish example from AnCora (Recasens and Mart´ı, 2010):

(24.13) La intenci´on es reconocer el gran prestigio que tiene la marat´on y unirlo
con esta gran carrera.‘目标是认可这场马拉松所具有的巨大声望，并将它与这场伟大的比赛结合|起来。”

> con esta gran carrera.‘The aim is to recognize the great prestige that the Marathon has and join|it with this great race.”

指示代词：指示代词 this 和 that 既可以单独出现，也可以作限定词出现，例如 this ingredient、that spice：

> Demonstrative Pronouns: Demonstrative pronouns this and that can appear either alone or as determiners, for instance, this ingredient, that spice:

(24.14) 我刚买了一本 Thoreau 的 Walden。五年前我买过一本。

> (24.14) I just bought a copy of Thoreau’s Walden. I had bought one five years ago.

那一本已经破旧不堪；这一本保存得好得多。

> That one had been very tattered; this one was in much better condition.

注意，这个 NP 是有歧义的；在英语口语中，它既可以是不定指的，

> Note that this NP is ambiguous; in colloquial spoken English, it can be indefinite,
如 (24.6) 所示，也可以是定指的，如 (24.14) 所示。

> as in (24.6), or definite, as in (24.14).

零回指：在某些语言（包括汉语、日语和意大利语）中，可以不使用代词，而是让回指语完全没有任何词汇实现，称为零回指语或零代词，如下面这个意大利语

> Zero Anaphora: Instead of using a pronoun, in some languages (including Chinese, Japanese, and Italian) it is possible to have an anaphor that has no lexical realization at all, called a zero anaphor or zero pronoun, as in the following Italian

> `zero anaphor`（零回指语）
>
> 释义：句中没有任何词汇形式出现、却在语义上有所指的回指成分，常见于汉语和日语。

和下面这个日语例子（取自 Poesio et al. 2016）：

> and Japanese examples from Poesio et al. (2016):

(24.15) EN [John]i 去看望几位朋友。在路上 [他]i 买了些

> (24.15) EN [John]i went to visit some friends. On the way [he]i bought some
葡萄酒。

> wine.

IT [Giovanni]i and`o a far visita a degli amici. Per via φi compr`o del vino.

JA [John]i-wa yujin-o houmon-sita. Tochu-de φi wain-o ka-tta.

或者下面这个汉语例子：

> or this Chinese example:

(24.16) [我] 前一会精神上太紧张。[0] 现在比较平静了
[我] 前一会太紧张了。…… [0] 现在比较平静了。

> [I] was too nervous a while ago. ... [0] am now calmer.

零回指语使这些语言中的提及检测任务变得复杂。

> Zero anaphors complicate the task of mention detection in these languages.

名称：名称（如人名、地名或组织名）既可以用来指称话语中的新实体，也可以指称旧实体：

> Names: Names (such as of people, locations, or organizations) can be used to refer to both new and old entities in the discourse:

(24.17) a. Woodhouse 小姐当然没有公正地对待他。

> (24.17) a. Miss Woodhouse certainly had not done him justice.

- International Business Machines 向 Amazon 索要专利赔偿；IBM 此前曾起诉过其他公司。

> International Business Machines sought patent compensation from Amazon; IBM had previously sued other companies.

### 24.1.2 信息状态

> 24.1.2 Information Status

指称表达式用于将新的所指对象引入话语（引入新信息），或从模型中取用旧有实体的方式，称为它们的信息状态或信息结构。实体可以是

> The way referring expressions are used to evoke new referents into the discourse(introducing new information), or access old entities from the model (old information), is called their information status or information structure. Entities can be

> `information status`（信息状态）
>
> 释义：指称表达式是把新所指对象引入话语，还是从话语模型中取用已有实体，即其所承载信息属于已知还是新信息的状态。

新引入话语或已引入话语，而且通常至少会区分

> discourse-new or discourse-old, and indeed it is common to distinguish at least

> `discourse-new discourse-old`（新引入话语、已引入话语）
>
> 释义：区分实体是首次进入话语（新引入）还是已存在于话语模型中（已引入）的信息状态维度。

三类实体信息状态（Prince，1981）：

> three kinds of entities informationally (Prince, 1981):

新 NP：

> new NPs:

全新 NP：这类提及引入的实体既是新引入话语又是听者新知的，如一个水果或一些核桃。

> brand new NPs: these introduce entities that are discourse-new and hearernew like a fruit or some walnuts.

未使用 NP：这类提及引入的实体是新引入话语但听者已知的

> unused NPs: these introduce entities that are discourse-new but hearer-old
（如 Hong Kong、Marie Curie 或 the New York Times。

> (like Hong Kong, Marie Curie, or the New York Times.

旧 NP：也称被唤起 NP，这类提及引入的实体已经存在于话语模型中，因此既是已引入话语又是听者已知的，如“I went to a new restaurant. It was...”中的 it。

> old NPs: also called evoked NPs, these introduce entities that already in the discourse model, hence are both discourse-old and hearer-old, like it in “I went to a new restaurant. It was...”.

可推断 NP：这类提及引入的实体既非听者已知也非已引入话语，

> inferrables: these introduce entities that are neither hearer-old nor discourse-old,
但听者可以基于话语中其他实体进行推理，从而推断出它们的存在。请看下面的例子：

> but the hearer can infer their existence by reasoning based on other entities that are in the discourse. Consider the following examples:

（24.18）我昨天去了一家很棒的餐厅。厨师刚刚把它开张。（24.19）把面粉、黄油和水混合。把面团揉到光滑。

> (24.18) I went to a superb restaurant yesterday. The chef had just opened it.(24.19) Mix flour, butter and water. Knead the dough until shiny.

无论是厨师还是面团，都不在话语模型中——若只依据第一

> Neither the chef nor the dough were in the discourse model based on the first

> `bridging inference`（桥接推理）
>
> 释义：听者借助世界知识，推断出话语中未明说、但由已有实体关联出的实体（如由餐厅想到厨师）。

句（两个例子各自的第一句）来判断，但读者可以做出桥接推理

> sentence of either example, but the reader can make a bridging inference
：即这些实体应该被加入话语模型，并与那家餐厅和那些配料关联起来，依据是世界知识——餐厅有厨师，面团是面粉与液体混合的产物（Haviland and Clark 1974，Webber and Baldwin 1992，Nissim et al. 2004，Hou et al. 2018）。

> that these entities should be added to the discourse model and associated with the restaurant and the ingredients, based on world knowledge that restaurants have chefs and dough is the result of mixing flour and liquid (Haviland and Clark 1974, Webber and Baldwin 1992, Nissim et al. 2004, Hou et al. 2018).

NP 的形式为其信息状态提供了强有力的线索。我们常常谈论

> The form of an NP gives strong clues to its information status. We often talk
一个实体在已知—新信息维度上的位置，即所指对象在多大程度上是已知的（在话语中显著、听者更容易想起、可被听者预测），相对于是新的（在话语中不显著、不可预测）（Chafe 1976，Prince 1981，Gundel et al. 1993）。一个非常可及的所指对象（Ariel，2001）

> about an entity’s position on the given-new dimension, the extent to which the referent is given (salient in the discourse, easier for the hearer to call to mind, predictable by the hearer), versus new (non-salient in the discourse, unpredictable) (Chafe 1976, Prince 1981, Gundel et al. 1993). A referent that is very accessible (Ariel, 2001)

> `given-new`（已知—新信息）
>
> 释义：衡量所指对象在话语中的显著程度即被听者预测的难易，越偏向已知越倾向用简短表达式指称。

> `accessible`（可及）
>
> 释义：指所指对象在听者心中高度显著、容易被想起，因而可以用较少的语言材料来指称。

即，在听者心中非常显著或容易想起，可以用较少的语言材料来指称。例如，只有当所指对象在话语模型中具有很高的激活度或显著性时，才会使用代词。4 相比之下，不太

> i.e., very salient in the hearer’s mind or easy to call to mind, can be referred to with less linguistic material. For example pronouns are used only when the referent has a high degree of activation or salience in the discourse model.4 By contrast, less

> `salience`（显著性）
>
> 释义：实体在话语模型中被激活、处于听者注意焦点的程度，越显著越倾向用代词指称。

显著的实体，例如刚被引入话语的新所指对象，则需要用更长、更明确的指称表达式来引入，以帮助听者找回所指对象。

> salient entities, like a new referent being introduced to the discourse, will need to be introduced with a longer and more explicit referring expression to help the hearer recover the referent.

因此，当一个实体首次被引入话语时，它的提及很可能

> Thus when an entity is first introduced into a discourse its mentions are likely
带有全名、头衔或角色，或同位语或限制性关系从句，正如（24.1）中对我们主人公的引入：Victoria Chen，Megabucks Banking 的 CFO。随着一个实体在话语中被不断讨论，它对听者变得更加显著，其提及平均而言通常变得更短、信息量更少，例如使用缩短的名字（如 Ms. Chen）、定指描述（the 38-year-old）或代词（she 或 her）（Hawkins 1978）。然而，这种长度上的变化并非单调的，并且对篇章结构敏感（Grosz 1977b，Reichman 1985，Fox 1993）。

> to have full names, titles or roles, or appositive or restrictive relative clauses, as in the introduction of our protagonist in (24.1): Victoria Chen, CFO of Megabucks Banking. As an entity is discussed over a discourse, it becomes more salient to the hearer and its mentions on average typically becomes shorter and less informative, for example with a shortened name (for example Ms. Chen), a definite description(the 38-year-old), or a pronoun (she or her) (Hawkins 1978). However, this change in length is not monotonic, and is sensitive to discourse structure (Grosz 1977b, Reichman 1985, Fox 1993).

### 24.1.3 复杂情况：非指称表达式

> 24.1.3 Complications: Non-Referring Expressions

许多名词短语或其他名词性成分并不是指称表达式，尽管它们可能在表面上具有容易混淆的相似性。例如，在最早的指称消解计算工作中，Karttunen（1969）指出，下面例子中的 NP a car 并不会创建一个话语所指对象：

> Many noun phrases or other nominals are not referring expressions, although they may bear a confusing superficial resemblance. For example in some of the earliest computational work on reference resolution, Karttunen (1969) pointed out that the NP a car in the following example does not create a discourse referent:

（24.20）Janet 没有汽车。

> (24.20) Janet doesn’t have a car.

并且不能被回指性的 it 或 the car 回指：

> and cannot be referred back to by anaphoric it or the car:

（24.21）*它是一辆 Toyota。

> (24.21) *It is a Toyota.

（24.22）*那辆车是红色的。

> (24.22) *The car is red.

这里我们总结四种常见的结构类型，它们在共指任务中不被计为提及，因而使提及检测任务变得复杂：

> We summarize here four common types of structures that are not counted as mentions in coreference tasks and hence complicate the task of mention-detection:

> 代词通常（但并非总是）指称那些在不超过一两句之前才引入的实体
>
> *Pronouns also usually (but not always) refer to entities that were introduced no further than one or two*

同位语：同位结构是紧邻中心名词短语出现、用于描述该中心语的名词短语。在英语中它们通常出现在逗号之间，如与 NP United 同位的“a unit of UAL”，或与 Victoria Chen 同位的 CFO of Megabucks Banking。

> Appositives: An appositional structure is a noun phrase that appears next to a head noun phrase, describing the head. In English they often appear in commas, like“a unit of UAL” appearing in apposition to the NP United, or CFO of Megabucks Banking in apposition to Victoria Chen.

（24.23）Victoria Chen，Megabucks Banking 的 CFO，看到……（24.24）United，作为 UAL 的一个下属单位，匹配了票价。

> (24.23) Victoria Chen, CFO of Megabucks Banking, saw ...(24.24) United, a unit of UAL, matched the fares.

同位 NP 不是指称表达式，而是充当一种

> Appositional NPs are not referring expressions, instead functioning as a kind of
对中心 NP 的补充性插入描述。尽管如此，有时将这些短语与它们所描述的实体链接起来是有用的，因此像 OntoNotes 这样的一些数据集会标注同位关系。

> supplementary parenthetical description of the head NP. Nonetheless, sometimes it is useful to link these phrases to an entity they describe, and so some datasets like OntoNotes mark appositional relationships.

谓语性和前置 NP：谓语性 NP 或属性 NP 描述中心名词的属性。在 United is a unit of UAL 中，NP a unit of UAL 描述的是 United 的一种属性，而不是指称一个不同的实体。因此它们在共指任务中不被标注为提及；在我们的例子中，NP $2.3 million 和 the company’s president 是属性性的，描述了她的薪酬和 the 38-year-old 的属性；（24.27）展示了一个中文例子，其中的谓语 NP（中国最大的城市；China’s biggest city）不是提及。

> Predicative and Prenominal NPs: Predicative or attributive NPs describe properties of the head noun. In United is a unit of UAL, the NP a unit of UAL describes a property of United, rather than referring to a distinct entity. Thus they are not marked as mentions in coreference tasks; in our example the NPs $2.3 million and the company’s president, are attributive, describing properties of her pay and the 38-year-old; Example (24.27) shows a Chinese example in which the predicate NP(中国最大的城市; China’s biggest city) is not a mention.

（24.25）她的薪酬跃升至 230 万美元（24.26）这位 38 岁的人成为了公司总裁（24.27）上海是[中国最大的城市][Shanghai is China’s biggest city]

> (24.25) her pay jumped to $2.3 million(24.26) the 38-year-old became the company’s president(24.27) 上海是[中国最大的城市] [Shanghai is China’s biggest city]
虚指：英语中像 it 这样的代词的许多用法，以及其他语言中相应的代词，都不具有指称性。这类虚指或赘余（pleonastic）情形包括

> Expletives: Many uses of pronouns like it in English and corresponding pronouns in other languages are not referential. Such expletive or pleonastic cases include

> `expletive clefts`（虚指分裂句）
>
> 释义：指 it 在分裂句、外置句等句法结构中的非指称用法，此时它不指向任何实体，只充当句法占位成分。

it is raining 这样的用法、hit it off 这类习语，或像分裂句这样的特定句法情形

> it is raining, in idioms like hit it off, or in particular syntactic situations like clefts
（24.28a），或外置（extraposition）（24.28b）：

> (24.28a) or extraposition (24.28b):

（24.28）a. 是 Emma Goldman 创办了 Mother Earth

> (24.28) a. It was Emma Goldman who founded Mother Earth

- 令我惊讶的是，她的墙上挂着一条鲱鱼。

> It surprised me that there was a herring hanging on her wall.

类指：另一种不回指文本中明确唤起的实体的表达方式是类指（generic reference）。看（24.29）。

> Generics: Another kind of expression that does not refer back to an entity explicitly evoked in the text is generic reference. Consider (24.29).

（24.29）我喜欢芒果。它们非常好吃。

> (24.29) I love mangos. They are very tasty.

这里，they 指的不是某个特定的芒果或某组芒果，而是泛指芒果这一类别。代词 you 也可以用于类指：

> Here, they refers, not to a particular mango or set of mangos, but instead to the class of mangos in general. The pronoun you can also be used generically:

（24.30）七月的旧金山，你得穿件夹克。

> (24.30) In July in San Francisco you have to wear a jacket.

### 24.1.4 共指关系的语言属性

> 24.1.4 Linguistic Properties of the Coreference Relation

既然我们已经了解了单个指称表达式的语言属性，接下来转向先行语/回指语这一对的属性。理解这些属性，对于设计新特征和进行错误分析都很有帮助。

> Now that we have seen the linguistic properties of individual referring expressions we turn to properties of the antecedent/anaphor pair. Understanding these properties is helpful both in designing novel features and performing error analyses.

数一致：指称表达式与其所指对象通常必须在数上保持一致；英语中 she/her/he/him/his/it 是单数，we/us/they/them 是复数，而 you 则在数上没有标明。因此，像 the chefs 这样的复数先行语通常不能与像 she 这样的单数回指语共指。不过，算法不能过于严格地强制数一致。首先，语义上为复数的实体既可以由 it 指称，也可以由 they 指称：

> Number Agreement: Referring expressions and their referents must generally agree in number; English she/her/he/him/his/it are singular, we/us/they/them are plural, and you is unspecified for number. So a plural antecedent like the chefs cannot generally corefer with a singular anaphor like she. However, algorithms cannot enforce number agreement too strictly. First, semantically plural entities can be referred to by either it or they:

（24.31）IBM 昨天发布了一款新的机器翻译产品。他们已

> (24.31) IBM announced a new machine translation product yesterday. They have
为此工作了 20 年。

> been working on it for 20 years.

其次，单数 they 已变得常见得多，其中 they 被用来

> Second, singular they has become much more common, in which they is used to

> `singular they`（单数 they）
>
> 释义：指用复数形式的 they 指代单个个体，常用于不表明性别或性别不明的情形。

指代单个个体，这往往很有用，因为 they 在性别上是中性的。尽管近期才增多，单数 they 其实相当古老，数百年来一直是英语的一部分。5

> describe singular individuals, often useful because they is gender neutral. Although recently increasing, singular they is quite old, part of English for many centuries.5
人称一致：英语区分第一、第二和第三人称，代词的先行语必须在人称上与代词一致。因此，第三人称代词（he、she、they、him、her、them、his、her、their）必须有第三人称的先行语（上述之一或任何其他名词短语）。不过，像引用这样的现象会造成例外；在下面这个例子中，I、my 和 she 是共指的：

> Person Agreement: English distinguishes between first, second, and third person, and a pronoun’s antecedent must agree with the pronoun in person. Thus a third person pronoun (he, she, they, him, her, them, his, her, their) must have a third person antecedent (one of the above or any other noun phrase). However, phenomena like quotation can cause exceptions; in this example I, my, and she are coreferent:

（24.32）“我投票给了 Nader，因为他与我的价值观最一致，”她说。

> (24.32) “I voted for Nader because he was most aligned with my values,” she said.

性或名词类别一致：在许多语言中，所有名词都有语法性（grammatical gender）或名词类别⁶，代词通常与其先行语的语法性保持一致。在英语中，这种一致只出现在第三人称单数代词上，它们区分阳性（he、him、his）、阴性（she、her）和非人称（it）三种语法性。像 ze 或 hir 这样的非二元性别代词也可能出现在较新的文本中。要知道文本中某个名字该关联哪种性别可能很复杂，或许还需要关于该个体的世界知识。一些例子：

> Gender or Noun Class Agreement: In many languages, all nouns have grammatical gender or noun class6 and pronouns generally agree with the grammatical gender of their antecedent. In English this occurs only with third-person singular pronouns, which distinguish between male (he, him, his), female (she, her), and nonpersonal(it) grammatical genders. Non-binary pronouns like ze or hir may also occur in more recent texts. Knowing which gender to associate with a name in text can be complex, and may require world knowledge about the individual. Some examples:

（24.33）Maryam 有一个定理。她很令人兴奋。（she=Maryam，不是那个定理）

> (24.33) Maryam has a theorem. She is exciting. (she=Maryam, not the theorem)
（24.34）Maryam 有一个定理。它很令人兴奋。（it=那个定理，不是 Maryam）

> (24.34) Maryam has a theorem. It is exciting. (it=the theorem, not Maryam)
约束理论限制：约束理论（binding theory）是对同一句子中提及与先行语之间关系的句法限制的统称（Chomsky, 1981）。稍微简化地说，像 himself 和 herself 这样的反身代词与包含它们的最直接小句的主语共指（24.35），而非反身代词则不能与该主语共指（24.36）。

> Binding Theory Constraints: The binding theory is a name for syntactic constraints on the relations between a mention and an antecedent in the same sentence(Chomsky, 1981). Oversimplifying a bit, reflexive pronouns like himself and herself corefer with the subject of the most immediate clause that contains them (24.35), whereas nonreflexives cannot corefer with this subject (24.36).

> `reflexive`（反身代词）
>
> 释义：指 himself、herself 这类代词，须与包含它的最近小句的主语共指。

（24.35）Janet 给自己买了一瓶鱼露。[herself=Janet]（24.36）Janet 给她买了一瓶鱼露。[her̸=Janet] 近因性：在较近的话语中引入的实体往往比在更靠前的话语中引入的实体更显著。因此，在（24.37）中，代词 it 更可能指 Jim 的地图，而不是医生的地图。

> (24.35) Janet bought herself a bottle of fish sauce. [herself=Janet](24.36) Janet bought her a bottle of fish sauce. [her̸=Janet] Recency: Entities introduced in recent utterances tend to be more salient than those introduced from utterances further back. Thus, in (24.37), the pronoun it is more likely to refer to Jim’s map than the doctor’s map.

（24.37）医生在船长的箱子里发现了一张旧地图。Jim 发现了一张更

> (24.37) The doctor found an old map in the captain’s chest. Jim found an even
旧的、藏在架子上的地图。它描绘了一座岛屿。

> older map hidden on the shelf. It described an island.

语法角色：在主语位置提及的实体比在宾语位置的实体更显著，而后者又比在旁格位置提及的实体更显著。因此，尽管（24.38）和（24.39）中的第一句表达了大致相同的命题内容，代词 he 偏好的所指对象却随主语而变化——（24.38）中是 Billy Bones，（24.39）中是 Jim Hawkins。

> Gra_5mmatical Role: Entities mentioned in subject position are more salient than those in object position, which are in turn more salient than those mentioned in oblique positions. Thus although the first sentence in (24.38) and (24.39) expresses roughly the same propositional content, the preferred referent for the pronoun he varies with the subject—Billy Bones in (24.38) and Jim Hawkins in (24.39).

（24.38）Billy Bones 和 Jim Hawkins 一起去了酒吧。他叫了一杯

> (24.38) Billy Bones went to the bar with Jim Hawkins. He called for a glass of
朗姆酒。[ he = Billy ]

> rum. [ he = Billy ]
（24.39）Jim Hawkins 和 Billy Bones 一起去了酒吧。他叫了一杯

> (24.39) Jim Hawkins went to the bar with Billy Bones. He called for a glass of
朗姆酒。[ he = Jim ]

> rum. [ he = Jim ]
动词语义：有些动词在语义上强调其某个论元，从而影响后续代词的解读。比较（24.40）和（24.41）。

> Verb Semantics: Some verbs semantically emphasize one of their arguments, biasing the interpretation of subsequent pronouns. Compare (24.40) and (24.41).

> 下面是一个来自莎士比亚《错误的喜剧》（Comedy of Errors）的约束代词例子：我遇到的每个人没有不向我致意的，仿佛我是他们熟识的朋友
>
> *Here’s a bound pronoun example from Shakespeare’s Comedy of Errors: There’s not a man I meet but doth salute me As if I were their well-acquainted friend*

（24.40）John 给 Bill 打了电话。他弄丢了笔记本电脑。（24.41）John 批评了 Bill。他弄丢了笔记本电脑。

> (24.40) John telephoned Bill. He lost the laptop.(24.41) John criticized Bill. He lost the laptop.

这些例子仅在第一个句子所用的动词上不同，但（24.40）中的“he”通常消解为 John，而（24.41）中的“he”消解为 Bill。这在一定程度上可能是由于隐式因果性与显著性之间的联系：“批评”事件的隐式原因是其宾语，而“打电话”事件的隐式原因是其主语。在这类动词中，作为隐式原因的那个实体可能更显著。

> These examples differ only in the verb used in the first sentence, yet “he” in (24.40) is typically resolved to John, whereas “he” in (24.41) is resolved to Bill. This may be partly due to the link between implicit causality and saliency: the implicit cause of a “criticizing” event is its object, whereas the implicit cause of a “telephoning”event is its subject. In such verbs, the entity which is the implicit cause may be more salient.

选择限制：许多其他类型的语义知识也会影响所指对象的偏好。例如，动词对其论元施加的选择限制（第 22 章）可以帮助排除某些所指对象，如（24.42）所示。

> Selectional Restrictions: Many other kinds of semantic knowledge can play a role in referent preference. For example, the selectional restrictions that a verb places on its arguments (Chapter 22) can help eliminate referents, as in (24.42).

（24.42）在煮了几个小时之后，我在我的新碗里喝了那碗汤

> (24.42) I ate the soup in my new bowl after cooking it for hours
it 有两个可能的所指对象，即 the soup 和 the bowl。然而，动词 eat 要求其直接宾语表示可食用的东西，这一约束可以排除将 bowl 作为可能的所指对象。

> There are two possible referents for it, the soup and the bowl. The verb eat, however, requires that its direct object denote something edible, and this constraint can rule out bowl as a possible referent.

## 24.2 共指任务与数据集

> 24.2 Coreference Tasks and Datasets

我们可以把共指消解任务表述如下：给定一段文本 T，找出其中所有实体以及它们之间的共指链接。我们通过将系统建立的链接与 T 上人工标注的黄金共指标注中的链接进行比较，来评价这项任务。

> We can formulate the task of coreference resolution as follows: Given a text T, find all entities and the coreference links between them. We evaluate our task by comparing the links our system creates with those in human-created gold coreference annotations on T.

让我们回到共指示例，这里用上标数字表示每个

> Let’s return to our coreference example, now using superscript numbers for each
共指链（簇），并用下标字母表示该簇中的各个提及：（24.43）[Victoria Chen]1 a，[Megabucks Banking]2 a 的 CFO，看到 [[her]1 b pay]3 a 跃升至

> coreference chain (cluster), and subscript letters for individual mentions in the cluster:(24.43) [Victoria Chen]1 a, CFO of [Megabucks Banking]2 a, saw [[her]1 b pay]3 a jump
230 万美元，同时 [the 38-year-old]1 c 还成为 [[the company]2 b 的总裁。众所周知，[she]1 d 是从竞争对手 [Lotsabucks]4 a 来到 [Megabucks]2 c 的。

> to $2.3 million, as [the 38-year-old]1 c also became [[the company]2 b’s president. It is widely known that [she]1 d came to [Megabucks]2 c from rival[Lotsabucks]4 a.

假设例（24.43）就是整篇文章的全部内容，那么 her pay 和 Lotsabucks 对应的链就是单例提及：

> Assuming example (24.43) was the entirety of the article, the chains for her pay and Lotsabucks are singleton mentions:

- {Victoria Chen, her, the 38-year-old, She}
- {Megabucks Banking, the company, Megabucks}
- { her pay}
- { Lotsabucks} 对大多数共指评测活动而言，系统的输入是原始的

> {Victoria Chen, her, the 38-year-old, She}
> {Megabucks Banking, the company, Megabucks}
> { her pay}
> { Lotsabucks} For most coreference evaluation campaigns, the input to the system is the raw

文章文本，系统必须检测出提及，再把它们链接成簇。

> text of articles, and systems must detect mentions and then link them into clusters.

解决这一任务需要处理代词性回指（判断出 her 指代 Victoria Chen），过滤掉非指称性代词（如 It has been ten years 中的冗语 It），处理定指名词短语以判断出 the 38-year-old 与 Victoria Chen 共指、the company 与 Megabucks 是同一个。我们还需要处理名称，识别出 Megabucks 与 Megabucks Banking 是同一个。

> Solving this task requires dealing with pronominal anaphora (figuring out that her refers to Victoria Chen), filtering out non-referential pronouns like the pleonastic It in It has been ten years), dealing with definite noun phrases to figure out that the 38-year-old is coreferent with Victoria Chen, and that the company is the same as Megabucks. And we need to deal with names, to realize that Megabucks is the same as Megabucks Banking.

究竟什么算作一个提及、标注哪些链接，因任务

> Exactly what counts as a mention and what links are annotated differs from task
和数据集的不同而不同。例如，有些共指数据集不标注单例，这使任务简单得多。在不含单例的语料上，消解系统能取得高得多的分数，因为单例构成了连续文本中提及的大多数，而且它们往往很难与非指称性 NP 区分开来。有些任务采用黄金提及检测（即系统获得人工标注的提及边界，任务只是对这些黄金提及进行聚类），从而免去了从连续文本中检测并切分提及的需要。

> to task and dataset to dataset. For example some coreference datasets do not label singletons, making the task much simpler. Resolvers can achieve much higher scores on corpora without singletons, since singletons constitute the majority of mentions in running text, and they are often hard to distinguish from non-referential NPs. Some tasks use gold mention-detection (i.e. the system is given human-labeled mention boundaries and the task is just to cluster these gold mentions), which eliminates the need to detect and segment mentions from running text.

共指通常用 CoNLL F1 分数来评价，该分数组合了三个

> Coreference is usually evaluated by the CoNLL F1 score, which combines three
指标：MUC、B³ 和 CEAFe；24.8 节给出细节。

> metrics: MUC, B3, and CEAFe; Section 24.8 gives the details.

下面介绍一个常用共指数据集 OntoNotes 的几个特点

> Let’s mention a few characteristics of one popular coreference dataset, OntoNotes
（Pradhan et al. 2007c, Pradhan et al. 2007a），以及基于它的 CoNLL 2012 共享任务（Pradhan et al., 2012a）。OntoNotes 包含人工标注的中文和英文共指数据集，各约一百万个词，涵盖新闻专线、杂志文章、广播新闻、广播对话、网络数据和会话语音数据，此外还有约 30 万词标注过的阿拉伯语新闻专线。OntoNotes 最重要的显著特点是它不标注单例，从而简化了共指任务，因为单例占全部实体的 60%~70%。在其他方面，它与其他共指数据集类似。相互共指的指称表达式 NP 被标注为提及，但泛指成分和冗语代词不予标注。同位语从句不作为单独的提及标注，但包含在该提及之内。因此在 NP “Richard Godown, president of the Industrial Biotechnology Association” 中，提及是整个短语。前置修饰语只有在是专有名词时才标注为单独实体。因此 wheat 在 wheat fields 中不是一个实体，而 UN 在 UN policy 中是一个实体（但 American policy 中的形容词 American 不是）。

> (Pradhan et al. 2007c, Pradhan et al. 2007a), and the CoNLL 2012 Shared Task based on it (Pradhan et al., 2012a). OntoNotes contains hand-annotated Chinese and English coreference datasets of roughly one million words each, consisting of newswire, magazine articles, broadcast news, broadcast conversations, web data and conversational speech data, as well as about 300,000 words of annotated Arabic newswire. The most important distinguishing characteristic of OntoNotes is that it does not label singletons, simplifying the coreference task, since singletons represent 60%-70% of all entities. In other ways, it is similar to other coreference datasets. Referring expression NPs that are coreferent are marked as mentions, but generics and pleonastic pronouns are not marked. Appositive clauses are not marked as separate mentions, but they are included in the mention. Thus in the NP, “Richard Godown, president of the Industrial Biotechnology Association” the mention is the entire phrase. Prenominal modifiers are annotated as separate entities only if they are proper nouns. Thus wheat is not an entity in wheat fields, but UN is an entity in UN policy (but not adjectives like American in American policy).

若干语料库标注了更丰富的话语现象。ISNotes 语料库

> A number of corpora mark richer discourse phenomena. The ISNotes corpus
对 OntoNotes 的一部分标注了信息状态，其中包括桥接示例（Hou et al., 2018）。LitBank 共指语料库（Bamman et al., 2020）包含来自 100 部不同文学小说的 210,532 个词元的共指标注，其中包括单例以及量化和否定的名词短语。AnCora-CO 共指语料库（Recasens and Mart´ı, 2010）分别包含 40 万词的西班牙语（AnCora-CO-Es）和加泰罗尼亚语（AnCora-CO-Ca）新闻数据，并包含对两种语言中话语指示这类复杂现象的标注。ARRAU 语料库（Uryupina et al., 2020）包含 35 万词标注了全部 NP 的英语数据，这意味着可以获得单例簇。ARRAU 涵盖对话（TRAINS 数据）和小说（Pear Stories）等多种体裁，并对桥接指称、话语指示、泛指成分和歧义回指关系都有标注。

> annotates a portion of OntoNotes for information status, include bridging examples(Hou et al., 2018). The LitBank coreference corpus (Bamman et al., 2020) contains coreference annotations for 210,532 tokens from 100 different literary novels, including singletons and quantified and negated noun phrases. The AnCora-CO coreference corpus (Recasens and Mart´ı, 2010) contains 400,000 words each of Spanish(AnCora-CO-Es) and Catalan (AnCora-CO-Ca) news data, and includes labels for complex phenomena like discourse deixis in both languages. The ARRAU corpus(Uryupina et al., 2020) contains 350,000 words of English marking all NPs, which means singleton clusters are available. ARRAU includes diverse genres like dialog(the TRAINS data) and fiction (the Pear Stories), and has labels for bridging references, discourse deixis, generics, and ambiguous anaphoric relations.

## 24.3 提及检测

> 24.3 Mention Detection

> `mention detection`（提及检测）
>
> 释义：共指消解的第一个阶段，负责在文本中定位哪些片段构成一个个提及。

共指的第一阶段是提及检测：找出那些

> The first stage of coreference is mention detection: finding the spans of text that
构成每个提及的文本跨度。提及检测算法在提出候选提及时通常非常宽松（即强调召回率），只在之后才进行过滤。例如，许多系统对文本运行句法分析器和命名实体标注器，抽取所有属于 NP、物主代词或命名实体的跨度。

> constitute each mention. Mention detection algorithms are usually very liberal in proposing candidate mentions (i.e., emphasizing recall), and only filtering later. For example many systems run parsers and named entity taggers on the text and extract every span that is either an NP, a possessive pronoun, or a named entity.

对我们重复列于（24.44）的示例文本这样做：

> Doing so from our sample text repeated in (24.44):

（24.44）Victoria Chen，Megabucks Banking 的 CFO，眼看自己的薪酬跃升至 230 万美元，同时这位 38 岁的女士还成为了公司的总裁。众所周知，她是从竞争对手 Lotsabucks 来到 Megabucks 的。

> (24.44) Victoria Chen, CFO of Megabucks Banking, saw her pay jump to $2.3 million, as the 38-year-old also became the company’s president. It is widely known that she came to Megabucks from rival Lotsabucks.

可能会得到下面这 13 个潜在提及的列表：

> might result in the following list of 13 potential mentions:

| Victoria Chen | $2.3 million | she |
| --- | --- | --- |
| CFO of Megabucks Banking | the 38-year-old | Megabucks |
| Megabucks Banking | the company | Lotsabucks |
| her | the company’s president |  |
| her pay | It |  |

CFO of Megabucks Banking　the 38-year-old　Megabucks

> CFO of Megabucks Banking the 38-year-old Megabucks
更晚近的提及检测系统更加宽松；基于跨度的

> More recent mention detection systems are even more generous; the span-based
算法（我们将在 24.6 节描述）首先抽取所有长度直到 N=10 的词的 n-gram 跨度。当然，回忆 24.1.3 节的内容：许多 NP——以及随机 n-gram 跨度中的绝大多数——并不是指称表达式。

> algorithm we will describe in Section 24.6 first extracts literally all n-gram spans of words up to N=10. Of course recall from Section 24.1.3 that many NPs—and the overwhelming majority of random n-gram spans—are not referring expressions.

因此，所有这类提及检测系统最终都需要滤除像上面的 It 那样的冗语/虚指代词、像 CFO of Megabucks Banking Inc 那样的同位语，或像 the company’s president 或 $2.3 million 那样的谓语性名词短语。

> Therefore all such mention detection systems need to eventually filter out pleonastic/expletive pronouns like It above, appositives like CFO of Megabucks Banking Inc, or predicate nominals like the company’s president or $2.3 million.

其中一些过滤可以用规则完成。早期的基于规则的系统设计了

> Some of this filtering can be done by rules. Early rule-based systems designed
正则表达式来处理冗语 it，例如 Lappin and Leass（1994）提出的下列规则，它们使用认知动词词典（如 believe、know、anticipate）来捕获 “It is thought that ketchup...” 中的冗语 it，或使用情态形容词（如 necessary、possible、certain、important），例如用于 “It is likely that I...”。这类规则有时被用作现代系统的一部分：

> regular expressions to deal with pleonastic it, like the following rules from Lappin and Leass (1994) that use dictionaries of cognitive verbs (e.g., believe, know, anticipate) to capture pleonastic it in “It is thought that ketchup...”, or modal adjectives(e.g., necessary, possible, certain, important), for, e.g., “It is likely that I...”. Such rules are sometimes used as part of modern systems:

It is Modaladjective that S　It is Modaladjective (for NP) to VP　It is Cogv-ed that S　It seems/appears/means/follows (that) S

> It is Modaladjective that S It is Modaladjective (for NP) to VP It is Cogv-ed that S It seems/appears/means/follows (that) S
提及检测规则有时是专门针对特定评测活动设计的。例如对 OntoNotes 来说，提及不嵌套在更大的提及之中，而且虽然数值量被标注，它们却很少共指。因此对于 CoNLL 2012 这类 OntoNotes 任务（Pradhan et al., 2012a），一种常见的第一遍基于规则的提及检测算法（Lee et al., 2013）是：

> Mention-detection rules are sometimes designed specifically for particular evaluation campaigns. For OntoNotes, for example, mentions are not embedded within larger mentions, and while numeric quantities are annotated, they are rarely coreferential. Thus for OntoNotes tasks like CoNLL 2012 (Pradhan et al., 2012a), a common first pass rule-based mention detection algorithm (Lee et al., 2013) is:

<!--figbox-->
> 取所有 NP、物主代词和命名实体。
>
> *Take all NPs, possessive pronouns, and named entities.*
<!--/figbox-->

然而，基于规则的系统通常不足以处理提及检测，因此现代系统会引入某种学习得到的提及检测组件，例如指称性分类器、回指性分类器（检测某个 NP 是否为回指语），或新引入话语分类器（检测某个提及是否是新引入话语、是否是未来回指语的潜在先行语）。

> Rule-based systems, however, are generally insufficient to deal with mentiondetection, and so modern systems incorporate some sort of learned mention detection component, such as a referentiality classifier, an anaphoricity classifier—detecting whether an NP is an anaphor—or a discourse-new classifier— detecting whether a mention is discourse-new and a potential antecedent for a future anaphor.

> `anaphoricity detector`（回指性检测器）
>
> 释义：判断给定 NP 是否为回指语的两类分类器之一，用于滤除不指称任何对象的提及。

例如，回指性检测器可以获取其正例训练样本

> An anaphoricity detector, for example, can draw its positive training examples
可以来自 OntoNotes、ARRAU 或 AnCora 等人工标注数据集中任何被标注为回指性指称表达式的跨度。其他任何 NP 或命名实体都可以标记为负训练样本。回指性分类器使用候选提及的特征，例如其中心词、周围词、定指性、生命性、长度、在句子/话语中的位置；其中许多特征最早由 Ng 和 Cardie（2002a）的早期工作提出；关于特征的更多内容参见 24.5 节。

> from any span that is labeled as an anaphoric referring expression in hand-labeled datasets like OntoNotes, ARRAU, or AnCora. Any other NP or named entity can be marked as a negative training example. Anaphoricity classifiers use features of the candidate mention such as its head word, surrounding words, definiteness, animacy, length, position in the sentence/discourse, many of which were first proposed in early work by Ng and Cardie (2002a); see Section 24.5 for more on features.

指称性或回指性检测器可以作为过滤器运行，此时只有被分类为回指性或指称性的提及才会被传给共指系统。这样的过滤式提及检测系统在上面的例子上最终得到的可能是以下这组经过过滤的 9 个潜在提及：

> Referentiality or anaphoricity detectors can be run as filters, in which only mentions that are classified as anaphoric or referential are passed on to the coreference system. The end result of such a filtering mention detection system on our example above might be the following filtered set of 9 potential mentions:

| Victoria Chen | her pay | she |
| --- | --- | --- |
| Megabucks Bank | the 38-year-old | Megabucks |
| her | the company | Lotsabucks |

Megabucks Bank the 38-year-old Megabucks
然而事实证明，基于回指性对提及进行硬过滤

> It turns out, however, that hard filtering of mentions based on an anaphoricity
或指称性分类器会导致性能不佳。如果回指性分类器的阈值设得过高，就会过滤掉过多提及，召回率受损。如果分类器的阈值设得过低，就会纳入过多赘余的或非指称性提及，精确率受损。

> or referentiality classifier leads to poor performance. If the anaphoricity classifier threshold is set too high, too many mentions are filtered out and recall suffers. If the classifier threshold is set too low, too many pleonastic or non-referential mentions are included and precision suffers.

而现代方法则是把提及检测、回指性和

> The modern approach is instead to perform mention detection, anaphoricity, and
共指在单个端到端模型中联合完成（Ng 2005b；Denis 和 Baldridge 2007；Rahman 和 Ng 2009）。例如，Lee 等（2017b，2018）系统中的提及检测基于单个端到端神经网络，它为每个提及的指称性计算一个分数，为两个提及是否共指计算一个分数，并将两者结合起来做出决策，用一个端到端损失来训练所有这些分数。我们将在 24.6 节详细描述该方法。7

> coreference jointly in a single end-to-end model (Ng 2005b, Denis and Baldridge 2007, Rahman and Ng 2009). For example mention detection in the Lee et al.(2017b),2018 system is based on a single end-to-end neural network that computes a score for each mention being referential, a score for two mentions being coreference, and combines them to make a decision, training all these scores with a single end-to-end loss. We’ll describe this method in detail in Section 24.6. 7
尽管有这些进展，正确检测指称性提及似乎仍然

> Despite these advances, correctly detecting referential mentions seems to still be
是一个尚未解决的问题，因为系统错误地把像 it 这样的赘余代词以及其他非指称性 NP 标记为共指，是现代共指消解系统的一大错误来源（Kummerfeld 和 Klein 2013；Martschat 和 Strube 2014；Martschat 和 Strube 2015；Wiseman 等 2015；Lee 等 2017a）。

> an unsolved problem, since systems incorrectly marking pleonastic pronouns like it and other non-referential NPs as coreferent is a large source of errors of modern coreference resolution systems (Kummerfeld and Klein 2013, Martschat and Strube 2014, Martschat and Strube 2015, Wiseman et al. 2015, Lee et al. 2017a).

因此，提及、指称性或回指性检测是一个重要的开放

> Mention, referentiality, or anaphoricity detection is thus an important open area
研究领域。其他知识来源可能会被证明是有帮助的，尤其是与无监督和半监督算法结合使用时，这也能减轻标注数据集的成本。例如在早期工作中，Bean 和 Riloff（1999）学习了用于刻画回指性或非回指性 NP 的模式；（通过抽取并泛化文本中最先出现的 NP，这些 NP 保证是非回指性的）。Chang 等（2012）寻找在训练数据中频繁出现但从未作为金标提及出现的中心名词，以帮助发现非指称性 NP。

> of investigation. Other sources of knowledge may turn out to be helpful, especially in combination with unsupervised and semisupervised algorithms, which also mitigate the expense of labeled datasets. In early work, for example Bean and Riloff(1999) learned patterns for characterizing anaphoric or non-anaphoric NPs; (by extracting and generalizing over the first NPs in a text, which are guaranteed to be non-anaphoric). Chang et al. (2012) look for head nouns that appear frequently in the training data but never appear as gold mentions to help find non-referential NPs.

Bergsma 等（2008b）把网络计数作为一种半监督方式，用来扩充针对英语 it 的回指性检测的标准特征；这是一项重要任务，因为 it 既常见又有歧义：有四分之一到二分之一的 it 例子是非回指性的。

> Bergsma et al. (2008b) use web counts as a semisupervised way to augment standard features for anaphoricity detection for English it, an important task because it is both common and ambiguous; between a quarter and half it examples are non-anaphoric.

考虑以下两个例子：

> Consider the following two examples:

(24.45) You can make [it] in advance. [回指性](24.46) You can make [it] in Hollywood. [非回指]

> (24.45) You can make [it] in advance. [anaphoric](24.46) You can make [it] in Hollywood. [non-anaphoric]
make it 中的 it 是非回指性的，是习语 make it 的一部分。Bergsma 等（2008b）把每个例子周围的上下文转成模式，比如来自（24.45）的“make * in advance”和来自（24.46）的“make * in Hollywood”。然后他们使用 Google n-gram 来枚举模式中可以替换 it 的所有词。非回指性上下文往往只在通配符位置出现 it，而回指性上下文则会与许多其他 NP 一同出现（例如在他们的数据中，make them in advance 与

> The_7 it in make it is non-anaphoric, part of the idiom make it. Bergsma et al. (2008b) turn the context around each example into patterns, like “make * in advance” from(24.45), and “make * in Hollywood” from (24.46). They then use Google n-grams to enumerate all the words that can replace it in the patterns. Non-anaphoric contexts tend to only have it in the wildcard positions, while anaphoric contexts occur with many other NPs (for example make them in advance is just as frequent in their data
make it in advance 一样频繁，但 make them in Hollywood 则完全没有出现）。这些 n-gram 上下文可以用作监督式回指性分类器中的特征。

> as make it in advance, but make them in Hollywood did not occur at all). These n-gram contexts can be used as features in a supervised anaphoricity classifier.

> 有些系统试图完全避免提及检测或回指性检测。对于像 OntoNotes 这样不标注单例的数据集，除了过滤掉非指称性提及之外的另一种做法是运行
>
> *Some systems try to avoid mention detection or anaphoricity detection altogether. For datasets like OntoNotes which don’t label singletons, an alternative to filtering out non-referential mentions is to run*

> 另一个提及。这很可能不如显式建模指称性那样奏效，而且无法解决
>
> *another mention. This likely doesn’t work as well as explicitly modeling referentiality, and cannot solve*

## 24.4 共指算法的架构

> 24.4 Architectures for Coreference Algorithms

现代共指系统基于有监督的神经机器学习，其监督来自 OntoNotes 等人工标注数据集。本节我们概述现代系统的各种架构，沿用 Ng（2010）的分类，该分类根据算法做出每个共指决策的方式是以基于实体的方式——即在话语模型中表示每个实体——还是仅基于提及的方式——即独立地考虑每个提及——以及它们是否使用排序模型直接比较潜在的先行语，来区分不同算法。之后，我们将在 24.6 节更详细地介绍一种当前最优算法。

> Modern systems for coreference are based on supervised neural machine learning, supervised from hand-labeled datasets like OntoNotes. In this section we overview the various architecture of modern systems, using the categorization of Ng (2010), which distinguishes algorithms based on whether they make each coreference decision in a way that is entity-based—representing each entity in the discourse model—or only mention-based—considering each mention independently, and whether they use ranking models to directly compare potential antecedents. Afterwards, we go into more detail on one state-of-the-art algorithm in Section 24.6.

### 24.4.1 提及对架构

> 24.4.1 The Mention-Pair Architecture

我们从提及对架构开始，它是最简单也最具影响力的

> We begin with the mention-pair architecture, the simplest and most influential

> `mention-pair`（提及对）
>
> 释义：一种共指模型：把回指语与每个候选先行语配成对，逐对判定二者是否指向同一实体。

共指架构，它引入了许多更复杂算法的特征，尽管其他架构表现更好。提及对架构围绕一个分类器构建，顾名思义，该分类器接收一对提及——一个候选回指语和一个候选先行语——并做出二元分类决策：是否共指。

> coreference architecture, which introduces many of the features of more complex algorithms, even though other architectures perform better. The mention-pair architecture is based around a classifier that— as its name suggests—is given a pair of mentions, a candidate anaphor and a candidate antecedent, and makes a binary classification decision: coreferring or not.

> `mention-pair`（提及对）
>
> 释义：一种共指模型：把回指语与每个候选先行语配成对，逐对判定二者是否指向同一实体。

让我们考虑该分类器在我们的例子中针对代词 she 的任务，并

> Let’s consider the task of this classifier for the pronoun she in our example, and
假定图 24.2 中经过略微简化的潜在先行语集合。

> assume the slightly simplified set of potential antecedents in Fig. 24.2.

![](images/24-coreference-entity-linking/fig_p13_0.png)

*图 24.2 对于每一对提及（如 she）与一个潜在的先行语提及（如 Victoria Chen 或 her），提及对分类器都会赋予一个共指链接的概率。*
*Figure 24.2 For each pair of a mention (like she), and a potential antecedent mention (like Victoria Chen or her), the mention-pair classifier assigns a probability of a coreference link.*

对于每个在先提及（Victoria Chen、Megabucks Banking、her 等），该二元

> For each prior mention (Victoria Chen, Megabucks Banking, her, etc.), the binary
分类器计算一个概率：该提及是否为 she 的先行语。我们希望对于真正的先行语（Victoria Chen、her、the 38-year-old），该概率较高；而对于非先行语（Megabucks Banking、her pay），该概率较低。

> classifier computes a probability: whether or not the mention is the antecedent of she. We want this probability to be high for actual antecedents (Victoria Chen, her, the 38-year-old) and low for non-antecedents (Megabucks Banking, her pay).

早期的分类器使用手工构建的特征（24.5 节）；较新的分类器

> Early classifiers used hand-built features (Section 24.5); more recent classifiers
使用神经表示学习（24.6 节）

> use neural representation learning (Section 24.6)
为了训练，我们需要一种选择训练样本的启发式方法；由于文档中的大多数提及对

> For training, we need a heuristic for selecting training samples; since most pairs
都不是共指的，选择每一对都会导致负样本大量过剩。最常见的启发式方法来自（Soon 等，2001），即选择最近的先行语作为正例，并把两者之间的所有配对作为负例。更形式化地说，对于每个回指语提及 mi，我们创建

> of mentions in a document are not coreferent, selecting every pair would lead to a massive overabundance of negative samples. The most common heuristic, from(Soon et al., 2001), is to choose the closest antecedent as a positive example, and all pairs in between as the negative examples. More formally, for each anaphor mention mi we create

- 一个正例 (mi, mj)，其中 mj 是离 mi 最近的先行语，以及

> one positive instance (mi,m j) where mj is the closest antecedent to mi, and

- 对位于 mj 与 mi 之间的每个 mk，各取一个负例 (mi, mk) 因此对于回指语 she，我们会选择 (she, her) 作为正例

> a negative instance (mi,mk) for each mk between mj and mi Thus for the anaphor she, we would choose (she, her) as the positive example

而没有负例。类似地，对于回指语 the company，我们会选择 (the company, Megabucks) 作为正例，并把 (the company, she)、(the company, the 38-year-old)、(the company, her pay) 和 (the company, her) 作为负例。

> and no negative examples. Similarly, for the anaphor the company we would choose(the company, Megabucks) as the positive example and (the company, she) (the company, the 38-year-old) (the company, her pay) and (the company, her) as negative examples.

一旦分类器训练完成，它就会在一个聚类

> Once the classifier is trained, it is applied to each test sentence in a clustering
步骤中应用于每个测试句子。对于文档中的每个提及 i，分类器会考察在先的 i−1 个提及中的每一个。在最近优先聚类（Soon 等，2001）中，分类器从右向左运行（从提及 i−1 一直到提及 1），第一个概率 > .5 的先行语会与 i 建立链接。如果没有先行语的概率 > 0.5，则不会为其选择先行语

> step. For each mention i in a document, the classifier considers each of the prior i−1 mentions. In closest-first clustering (Soon et al., 2001), the classifier is run right to left (from mention i−1 down to mention 1) and the first antecedent with probability> .5 is linked to i. If no antecedent has probably > 0.5, no antecedent is selected for

- 在最佳优先聚类中，分类器会在全部 i −1 个先行语上运行，并把最可能的前一个提及选作 i 的先行语。该成对关系的传递闭包即被当作簇。

> In best-first clustering, the classifier is run on all i −1 antecedents and the most probable preceding mention is chosen as the antecedent for i. The transitive closure of the pairwise relation is taken as the cluster.

虽然提及对模型具有简单这一优点，但它有两个主要

> While the mention-pair model has the advantage of simplicity, it has two main
问题。第一，分类器并不直接相互比较候选先行语，因此它没有被训练来判断在两个可能的先行语之间哪一个实际上更好。第二，它忽略了话语模型，只关注提及，而不关注实体。每一个分类器决策都完全局部于该对作出，无法考虑同一实体的其他提及。接下来两个模型分别解决这两个缺陷之一。

> problems. First, the classifier doesn’t directly compare candidate antecedents to each other, so it’s not trained to decide, between two likely antecedents, which one is in fact better. Second, it ignores the discourse model, looking only at mentions, not entities. Each classifier decision is made completely locally to the pair, without being able to take into account other mentions of the same entity. The next two models each address one of these two flaws.

### 24.4.2 提及排序架构

> 24.4.2 The Mention-Rank Architecture

提及排序模型直接相互比较候选先行语，为每个回指语选出得分最高的先行语。

> The mention ranking model directly compares candidate antecedents to each other, choosing the highest-scoring antecedent for each anaphor.

在早期的表述中，对于提及 i，分类器判定 {1,...,i−

> In early formulations, for mention i, the classifier decides which of the {1,...,i−
1} 中哪一个在先提及是先行语（Denis and Baldridge, 2008）。但假设 i 实际上并非回指性，不应选择任何先行语呢？这样的模型就需要对 i 单独运行一个回指性分类器。相反，事实证明更好的是用一个单一损失联合学习回指性检测与共指（Rahman and Ng, 2009）。

> 1} prior mentions is the antecedent (Denis and Baldridge, 2008). But suppose i is in fact not anaphoric, and none of the antecedents should be chosen? Such a model would need to run a separate anaphoricity classifier on i. Instead, it turns out to be better to jointly learn anaphoricity detection and coreference together with a single loss (Rahman and Ng, 2009).

因此，在现代提及排序系统中，对于第 i 个提及（回指语），我们有一个

> So in modern mention-ranking systems, for the ith mention (anaphor), we have
相关联的随机变量 yi，其取值范围为 Y(i) = {1,...,i−1,ϵ}。值 ϵ 是一个特殊的虚拟提及，表示 i 没有先行语（即要么是新引入话语并开启一条新的共指链，要么是非回指）。

> an associated random variable yi ranging over the values Y(i) = {1,...,i−1,ϵ}. The value ϵ is a special dummy mention meaning that i does not have an antecedent (i.e., is either discourse-new and starts a new coref chain, or is non-anaphoric).

![](images/24-coreference-entity-linking/fig_p14_0.png)

*图 24.3 对于每个候选回指性提及（如 she），提及排序系统会在所有先前提及加上特殊虚拟提及 ϵ 之上分配一个概率分布。*
*Figure 24.3 For each candidate anaphoric mention (like she), the mention-ranking system assigns a probability distribution over all previous mentions plus the special dummy mention ϵ.*

在测试时，对于给定的提及 i，模型会在所有

> At test time, for a given mention i the model computes one softmax over all the
先行语（加上 ϵ）上计算一个 softmax，为每个候选先行语（或没有）给出概率。

> antecedents (plus ϵ) giving a probability for each candidate antecedent (or none).

图 24.3 展示了针对单个候选回指语 she 的计算示例。

> Fig. 24.3 shows an example of the computation for the single candidate anaphor she.

一旦为每个回指语分类出先行语，就可以在

> Once the antecedent is classified for each anaphor, transitive closure can be run
成对决策上运行传递闭包，以得到一个完整的聚类。

> over the pairwise decisions to get a complete clustering.

提及排序模型的训练比提及对模型更棘手，

> Training is trickier in the mention-ranking model than the mention-pair model,
因为对于每个回指语，我们并不知道在全部可能的金标先行语中该用哪一个来训练。相反，每个提及的最佳先行语是隐变量；也就是说，对于每个提及，我们有一整簇合法的金标先行语可供选择。早期工作使用启发式方法来选择先行语，例如选择最近的先行语作为金标先行语，并把两个句子窗口内的所有非先行语作为负例（Denis and Baldridge, 2008）。存在各种对隐变量先行语建模的方式（Fernandes et al. 2012, Chang et al. 2013, Durrett and Klein 2013）。最简单的方式是通过对所有合法先行语求和来给任一个合法先行语记分，并使用一个损失函数来优化来自金标聚类的所有正确先行语的似然（Lee et al., 2017b）。我们将在 24.6 节看到细节。

> because for each anaphor we don’t know which of all the possible gold antecedents to use for training. Instead, the best antecedent for each mention is latent; that is, for each mention we have a whole cluster of legal gold antecedents to choose from. Early work used heuristics to choose an antecedent, for example choosing the closest antecedent as the gold antecedent and all non-antecedents in a window of two sentences as the negative examples (Denis and Baldridge, 2008). Various kinds of ways to model latent antecedents exist (Fernandes et al. 2012, Chang et al. 2013, Durrett and Klein 2013). The simplest way is to give credit to any legal antecedent by summing over all of them, with a loss function that optimizes the likelihood of all correct antecedents from the gold clustering (Lee et al., 2017b). We’ll see the details in Section 24.6.

提及排序模型可以用手工构建的特征实现，也可以用

> Mention-ranking models can be implemented with hand-build features or with
神经表示学习实现（后者也可能纳入一些手工构建的特征）。我们将在 24.5 节和 24.6 节探索这两个方向。

> neural representation learning (which might also incorporate some hand-built features). we’ll explore both directions in Section 24.5 and Section 24.6.

### 24.4.3 基于实体的模型

> 24.4.3 Entity-based Models

提及对模型和提及排序模型都针对提及作出决策。相比之下，基于实体的模型把每个提及链接到的不是先前的提及，而是先前的话语实体（提及的簇）。

> Both the mention-pair and mention-ranking models make their decisions about mentions. By contrast, entity-based models link each mention not to a previous mention but to a previous discourse entity (cluster of mentions).

只要让分类器在提及的簇上而非单个提及上作出决策，

> A mention-ranking model can be turned into an entity-ranking model simply
提及排序模型就可以被简单地转化为实体排序模型（Rahman and Ng, 2009）。

> by having the classifier make its decisions over clusters of mentions rather than individual mentions (Rahman and Ng, 2009).

对于传统的基于特征的模型，这可以通过在簇上抽取特征来实现。

> For traditional feature-based models, this can be done by extracting features over

簇的大小是一个有用的特征，它的“形状”也是，形状即簇中各提及的类型列表，也就是说，由 (P)专有、(D)定指、(I)不定指、(Pr)代词 这些标记构成的序列，因此由 {Victoria, her, the 38-year-old} 组成的簇其形状为 P-Pr-D（Bj¨orkelund and Kuhn, 2014）。一个包含提及对分类器的基于实体的模型可以使用提及对概率的聚合作为特征，例如计算两个簇中所有提及对的共指平均概率（Clark and Manning 2015）。

> clusters. The size of a cluster is a useful feature, as is its ‘shape’, which is the list of types of the mentions in the cluster i.e., sequences of the tokens (P)roper,(D)efinite, (I)ndefinite, (Pr)onoun, so that a cluster composed of {Victoria, her, the 38-year-old} would have the shape P-Pr-D (Bj¨orkelund and Kuhn, 2014). An entitybased model that includes a mention-pair classifier can use as features aggregates of mention-pair probabilities, for example computing the average probability of coreference over all mention-pairs in the two clusters (Clark and Manning 2015).

神经模型可以自动学习簇的表示，例如

> Neural models can learn representations of clusters automatically, for example
通过在簇的提及序列上使用 RNN 来编码对应于簇表示的状态（Wiseman et al., 2016），或者通过对学习到的提及对表示进行池化来为簇对学习分布式表示（Clark and Manning, 2016b）。

> by using an RNN over the sequence of cluster mentions to encode a state corresponding to a cluster representation (Wiseman et al., 2016), or by learning distributed representations for pairs of clusters by pooling over learned representations of mention pairs (Clark and Manning, 2016b).

然而，尽管基于实体的模型表达力更强，但在实践中使用簇级信息并未带来性能上的大幅提升，因此提及排序模型仍然更常用。

> However, although entity-based models are more expressive, the use of clusterlevel information in practice has not led to large gains in performance, so mentionranking models are still more commonly used.

## 24.5 使用手工构建特征的分类器

> 24.5 Classifiers using hand-built features

基于特征的分类器在逻辑回归、SVM 或随机森林分类器中使用手工设计的特征来完成共指消解。这些分类器的表现不如神经分类器。尽管如此，在算力或数据稀缺时，它们有时仍可用于构建轻量级系统，而且即使在神经系统中，这些特征本身对错误分析也很有用。

> Feature-based classifiers, use hand-designed features in logistic regression, SVM, or random forest classifiers for coreference resolution. These classifiers don’t per- form as well as neural ones. Nonetheless, they are still sometimes useful to build lightweight systems when compute or data are sparse, and the features themselves are useful for error analysis even in neural systems.

给定一个回指语提及和一个潜在的先行语提及，基于特征的

> Given an anaphor mention and a potential antecedent mention, feature based
分类器利用三类特征：(i) 回指语的特征，(ii) 候选先行语的特征，以及 (iii) 该对之间关系的特征。

> classifiers make use of three types of features: (i) features of the anaphor, (ii) features of the candidate antecedent, and (iii) features of the relationship between the pair.

基于实体的模型还可以额外利用两个额外的类别：(iv) 来自先行语实体簇中所有提及的特征，以及 (v) 回指语与先行语实体簇中各提及之间关系的特征。

> Entity-based models can make additional use of two additional classes: (iv) feature of all mentions from the antecedent’s entity cluster, and (v) features of the relation between the anaphor and the mentions in the antecedent entity cluster.

<!--figbox-->
> 回指语或先行语提及的特征
>
> *Features of the Anaphor or Antecedent Mention*

> 首（末）词 Victoria/she 先行语/回指语的首个或末个词（或其嵌入） 中心词 Victoria/she 先行语/回指语的中心词（或中心词嵌入） 属性 Sg-F-A-3-PER/ 先行语/回指语的数、性、生命度、人称、命名实体类型
>
> *First (last) word Victoria/she First or last word (or embedding) of antecedent/anaphor Head word Victoria/she Head word (or head embedding) of antecedent/anaphor Attributes Sg-F-A-3-PER/ The number, gender, animacy, person, named entity type*

> Sg-F-A-3-PER （先行语/回指语）的属性
>
> *Sg-F-A-3-PER attributes of (antecedent/anaphor)*

> 长度 2/1 （先行语/回指语）的词数 提及类型 P/Pr 先行语/回指语的类型：(P)专有、(D)定指、(I)不定指、(Pr)代词）
>
> *Length 2/1 length in words of (antecedent/anaphor) Mention type P/Pr Type: (P)roper, (D)efinite, (I)ndefinite, (Pr)onoun) of antecedent/anaphor*

> 先行语实体的特征
>
> *Features of the Antecedent Entity*

> 实体形状 P-Pr-D 先行语实体（簇）中各提及的“形状”或类型列表，即由
>
> *Entity shape P-Pr-D The ‘shape’ or list of types of the mentions in the*

> (P)专有、(D)定指、(I)不定指、(Pr)代词 构成的序列。
>
> *antecedent entity (cluster), i.e., sequences of (P)roper,(D)efinite, (I)ndefinite, (Pr)onoun.*

> 实体属性 Sg-F-A-3-PER 数、性、生命度、人称、命名实体类型
>
> *Entity attributes Sg-F-A-3-PER The number, gender, animacy, person, named entity type*

> 先行语实体的属性
>
> *attributes of the antecedent entity*

> 先行语簇大小 3 先行语簇中提及的数量
>
> *Ant. cluster size 3 Number of mentions in the antecedent cluster*

> 提及对的特征
>
> *Features of the Pair of Mentions*

> 句子距离 1 先行语与回指语之间的句子数 提及距离 4 先行语与回指语之间的提及数 i-within-i F 回指语与先行语之间具有 i-within-i 关系 Cosine 先行语与回指语嵌入之间的余弦值
>
> *Sentence distance 1 The number of sentences between antecedent and anaphor Mention distance 4 The number of mentions between antecedent and anaphor i-within-i F Anaphor has i-within-i relation with antecedent Cosine Cosine between antecedent and anaphor embeddings*

> 实体对的特征
>
> *Features of the Pair of Entities*

> 精确字符串匹配 F 若来自先行语的任意两个提及的字符串
>
> *Exact String Match F True if the strings of any two mentions from the antecedent*

> 与回指语簇相同则为真。
>
> *and anaphor clusters are identical.*

> 中心词匹配 F 若来自先行语簇的任一提及具有
>
> *Head Word Match F True if any mentions from antecedent cluster has same*

> 与回指语簇中任一提及相同的中心词则为真
>
> *headword as any mention in anaphor cluster*

> 词语包含 F 回指语簇中的所有词语都包含在先行语簇中
>
> *Word Inclusion F All words in anaphor cluster included in antecedent cluster*
<!--/figbox-->

*图 24.4 基于特征的共指：回指语“she”与潜在先行语“Victoria Chen”的示例特征值。*
*Figure 24.4 Feature-based coreference: sample feature values for anaphor “she” and potential antecedent“Victoria Chen”.*

图 24.4 展示了一组常用特征，并展示了

> Figure 24.4 shows a selection of commonly used features, and shows the value
在示例句中为潜在回指语“she”与潜在先行语“Victoria Chen”计算得到的取值，该例句在下面重复给出：

> that would be computed for the potential anaphor “she” and potential antecedent“Victoria Chen” in our example sentence, repeated below:

(24.47) Victoria Chen，Megabucks Banking 的首席财务官，眼看着自己的薪酬跃升至 2.3

> (24.47) Victoria Chen, CFO of Megabucks Banking, saw her pay jump to $2.3
百万美元，同时这位 38 岁的人士还成为了公司总裁。众所周知，她是从竞争对手 Lotsabucks 来到 Megabucks 的。

> million, as the 38-year-old also became the company’s president. It is widely known that she came to Megabucks from rival Lotsabucks.

以往研究发现特别有用的特征包括精确字符串

> Features that prior work has found to be particularly useful are exact string
匹配、实体中心词一致、提及距离，以及（对于代词）精确属性匹配与 i-within-i，（对于名词性成分与专有名词）词语包含与余弦相似度。对于词汇特征（如中心词），通常只使用出现次数足够多（>20 次）的词语。

> match, entity headword agreement, mention distance, as well as (for pronouns) exact attribute match and i-within-i, and (for nominals and proper names) word inclusion and cosine. For lexical features (like head words) it is common to only use words that appear enough times (>20 times).

在基于特征的系统中，使用特征组合至关重要；一项实验表明，将分类器中的单个特征改为多个特征的组合，可使 F1 值提高 4 个百分点（Lee et al., 2017a）。具体的特征组合可以手工设计（Durrett and Klein, 2013），可以将所有特征两两组合（Bengtson and Roth, 2008），也可以使用决策树或随机森林分类器来学习特征组合（Ng and Cardie 2002a, Lee et al. 2017a）。

> It is crucial in feature-based systems to use conjunctions of features; one experiment suggested that moving from individual features in a classifier to conjunctions of multiple features increased F1 by 4 points (Lee et al., 2017a). Specific conjunctions can be designed by hand (Durrett and Klein, 2013), all pairs of features can be conjoined (Bengtson and Roth, 2008), or feature conjunctions can be learned using decision tree or random forest classifiers (Ng and Cardie 2002a, Lee et al. 2017a).

特征同样也可以用于神经模型。神经模型使用上下文词嵌入，因此无法从字符串匹配或提及类型这类浅层特征中获益。不过，提及长度、提及之间的距离或体裁等特征可以补充神经上下文嵌入模型。

> Features can also be used in neural models as well. Neural systems use contextual word embeddings so don’t benefit from shallow features like string match or or mention types. However features like mention length, distance between mentions, or genre can complement neural contextual embedding models.

## 24.6 一种神经提及排序算法

> 24.6 A neural mention-ranking algorithm

本节介绍 Lee et al. (2017b) 的神经 e2e-coref 算法（做了少许简化和扩展，并借鉴了 Joshi et al. (2019) 等人的工作）。这是一种提及排序算法，它考虑文档中所有可能的文本跨度，为每个跨度赋予一个提及得分，依据该得分对提及进行剪枝，然后为剩余的提及分配共指链接。

> In this section we describe the neural e2e-coref algorithms of Lee et al. (2017b)(simplified and extended a bit, drawing on Joshi et al. (2019) and others). This is a mention-ranking algorithm that considers all possible spans of text in the document, assigns a mention-score to each span, prunes the mentions based on this score, then assigns coreference links to the remaining mentions.

更形式化地说，给定一个含 T 个词的文档 D，模型考虑

> More formally, given a document D with T words, the model considers all of
D 中全部 T(T+1)/2 个文本跨度（一元、二元、三元、四元等；实践中

> the T(T+_21) text spans in D (unigrams, bigrams, trigrams, 4-grams, etc; in practice
我们只考虑最大长度约为 10 的跨度）。任务是为每个跨度 i 分配一个先行语 yi，这是一个随机变量，取值范围为 Y(i) ={1,...,i −1,ϵ}，即每个先前的跨度以及一个特殊的哑元标记 ϵ。选择哑元标记意味着 i 没有先行语，原因可能是 i 是新引入话语并开启了一条新的共指链，也可能是 i 为非回指。

> we only consider spans up a maximum length around 10). The task is to assign to each span i an antecedent yi, a random variable ranging over the values Y(i) ={1,...,i −1,ϵ}; each previous span and a special dummy token ϵ. Choosing the dummy token means that i does not have an antecedent, either because i is discoursenew and starts a new coreference chain, or because i is non-anaphoric.

对于每一对跨度 i 和 j，系统为跨度 i 与跨度 j 之间的共指链接赋予一个得分 s(i, j)。随后系统学习跨度 i 的先行语上的一个分布 P(yi)：

> For each pair of spans i and j, the system assigns a score s(i, j) for the coreference link between span i and span j. The system then learns a distribution P(yi) over the antecedents for span i:

$$\text{exp} ( s ( i , y _{i} ))$$

P(yi) = P

$$_{y ′ \in Y ( i )} \text{exp} ( s ( i , y ^{′} ))$$

该得分 s(i, j) 包含三个我们将在下面定义的因子：m(i)，即跨度 i 是否为提及；m(j)，即跨度 j 是否为提及；以及 c(i, j)，即 j 是否为 i 的先行语：

> This score s(i, j) includes three factors that we’ll define below: m(i); whether span i is a mention; m(j); whether span j is a mention; and c(i, j); whether j is the antecedent of i:

s(i, j) = m(i)+m(j)+c(i, j) (24.49)
对于哑元先行语 ϵ，得分 s(i,ϵ) 固定为 0。这样，只要有任何非哑元得分为正，模型就预测得分最高的先行语；而如果所有得分均为负，模型则弃权。

> For the dummy antecedent ϵ, the score s(i,ϵ) is fixed to 0. This way if any nondummy scores are positive, the model predicts the highest-scoring antecedent, but if all the scores are negative it abstains.

### 24.6.1 计算跨度表示

> 24.6.1 Computing span representations

为了计算为跨度 i 或跨度对 (i, j) 打分的两个函数 m(i) 与 c(i, j)，我们需要一种表示跨度的方法。e2e-coref 系列算法通过设法捕捉 3 个词/词元来表示每个跨度：第一个词、最后一个词和最重要的词。我们首先将每个段落或子文档送入编码器（如 BERT），为每个词元 i 生成嵌入 hi。跨度 i 随后由一个向量 gi 表示，该向量是跨度第一个（起始）词元的编码器输出嵌入、跨度最后一个（结束）词元的编码器输出，以及第三个基于注意力的表示的拼接：

> To compute the two functions m(i) and c(i, j) which score a span i or a pair of spans(i, j), we’ll need a way to represent a span. The e2e-coref family of algorithms represents each span by trying to capture 3 words/tokens: the first word, the last word, and the most important word. We first run each paragraph or subdocument through an encoder (like BERT) to generate embeddings hi for each token i. The span i is then represented by a vector gi that is a concatenation of the encoder output embedding for the first (start) token of the span, the encoder output for the last (end) token of the span, and a third vector which is an attention-based representation:

$$g _{i} = [ h _{\text{START} ( i )} , h _{\text{END} ( i )} , h _{\text{ATT} ( i )} ]$$

注意力向量的目标是表示哪个词/词元是该跨度可能的

> The goal of the attention vector is to represent which word/token is the likely
句法中心词；我们在前一节中看到，中心词是一种有用的特征；中心词匹配是共指的一个良好指示。注意力表示按通常方式计算；系统学习一个权重向量 wα，并计算它与经 FFN 变换后的隐藏状态 ht 的点积：

> syntactic head-word of the span; we saw in the prior section that head-words are a useful feature; a matching head-word is a good indicator of coreference. The attention representation is computed as usual; the system learns a weight vector wα, and computes its dot product with the hidden state ht transformed by a FFN:

$$α _{t} = w _{α} \cdot ^{\text{FFN}} _{α} ( h _{t} )$$

注意力得分通过 softmax 归一化为一个分布：

> The attention score is normalized into a distribution via a softmax:

$$\text{exp} ( α _{t} )$$

$$a _{i , t} =$$

PEND(i) k=START(i) exp(αk)
然后用这一注意力分布构造向量 hATT(i)，它是对跨度 i 中每个词的嵌入 et 所做的注意力加权求和：

> And then the attention distribution is used to create a vector hATT(i) which is an attention-weighted sum of the embeddings et of each of the words in span i:

> END(i)

$$\sum_{\text{START}}^{\text{END} (}$$

$$a _{i , t} \cdot e _{t}$$

$$h _{\text{ATT} ( i )} =$$

> t=START(i)

图 24.5 展示了跨度表示的计算以及提及

> Fig. 24.5 shows the computation of the span representation and the mention
得分的计算。

> score.

![](images/24-coreference-entity-linking/fig_p18_0.png)

*图 24.5 e2e-coref 模型的 BERT 版本中跨度表示 g（以及提及得分 m）的计算（Lee et al. 2017b，Joshi et al. 2019）。模型考虑所有跨度，最大宽度设为 10；图中给出了二元组和三元组跨度中的一小部分。*
*Figure 24.5 Computation of the span representation g (and the mention score m) in a BERT version of the e2e-coref model (Lee et al. 2017b, Joshi et al. 2019). The model considers all spans up to a maximum width of say 10; the figure shows a small subset of the bigram and trigram spans.*

### 24.6.2 计算提及得分与先行语得分 m 和 c

> 24.6.2 Computing the mention and antecedent scores m and c

既然已经知道如何计算表示跨度 i 的向量 gi，我们就可以来看两个打分函数 m(i) 和 c(i, j) 的细节了。二者都由前馈网络计算：

> Now that we know how to compute the vector gi for representing span i, we can see the details of the two scoring functions m(i) and c(i, j). Both are computed by feedforward networks:

m(i) = wm ·FFNm(gi) (24.54)

$$c ( i , j ) = w _{c} \cdot \text{FFN} _{c} ([ g _{i} , g ^{j} , g _{i} ◦ g _{j} , ])$$

在推断阶段，该提及得分 m 被用作过滤器，只保留得分最高的少数几个提及。

> At inference time, this mention score m is used as a filter to keep only the best few mentions.

随后我们为得分高的提及计算先行语得分。先行语

> We then compute the antecedent score for high-scoring mentions. The antecedent
得分 c(i, j) 的输入是跨度 i 与 j 的表示，此外还有两个跨度彼此的逐元素相似度 gi ◦gj（这里 ◦ 表示逐元素相乘）。图 24.6 展示了图 24.5 的例句中 the company 的三个可能先行语的得分 s 的计算。

> score c(i, j) takes as input a representation of the spans i and j, but also the elementwise similarity of the two spans to each other gi ◦gj (here ◦is element-wise multiplication). Fig. 24.6 shows the computation of the score s for the three possible antecedents of the company in the example sentence from Fig. 24.5.

![](images/24-coreference-entity-linking/fig_p19_0.png)

*图 24.6 图 24.5 例句中 the company 的三个可能先行语的得分 s 的计算。图取自 Lee et al. (2017b)。*
*Figure 24.6 The computation of the score s for the three possible antecedents of the company in the example sentence from Fig. 24.5. Figure after Lee et al. (2017b).*

给定提及集合后，每个文档的先行语联合分布可在一次前向传播中算出，之后我们可以对先行语做传递闭包，从而得到该文档的最终聚类。

> Given the set of mentions, the joint distribution of antecedents for each document is computed in a forward pass, and we can then do transitive closure on the antecedents to create a final clustering for the document.

图 24.7 给出了该模型的一些预测示例，展示了注意力

> Fig. 24.7 shows example predictions from the model, showing the attention
权重，Lee et al. (2017b) 发现这些权重与传统语义中心词相关。

> weights, which Lee et al. (2017b) find correlate with traditional semantic heads.

注意，模型在第二个例子上出了错，大概是因为 attendants 和 pilot 的词嵌入很可能彼此接近。

> Note that the model gets the second example wrong, presumably because attendants and pilot likely have nearby word embeddings.

![](images/24-coreference-entity-linking/fig_p19_1.png)

*图 24.7 Lee et al. (2017b) 模型的预测示例，每个例子一个簇，展示了一个正确例子和一个错误例子。加粗并带括号的跨度是预测簇中的提及。某个词上红色的多少表示式 24.52 中寻找中心词的注意力权重 ai,t。图改编自 Lee et al. (2017b)。*
*Figure 24.7 Sample predictions from the Lee et al. (2017b) model, with one cluster per example, showing one correct example and one mistake. Bold, parenthesized spans are mentions in the predicted cluster. The amount of red color on a word indicates the head-finding attention weight ai,t in Eq. 24.52. Figure adapted from Lee et al. (2017b).*

### 24.6.3 学习

> 24.6.3 Learning

训练时，每个提及并没有唯一的黄金先行语；共指标注只给出由共指提及构成的整个簇；因此一个提及只有潜在的先行语。所以我们使用的损失函数要让任一合法先行语的共指概率之和最大化。对于给定提及 i，其可能的先行语为 Y(i)，令 GOLD(i) 表示包含 i 的黄金簇中的提及集合。由于出现在 i 之前的提及集合是 Y(i)，该黄金簇中同样出现在 i 之前的提及集合就是 Y(i)∩GOLD(i)。因此我们希望最大化：

> For training, we don’t have a single gold antecedent for each mention; instead the coreference labeling only gives us each entire cluster of coreferent mentions; so a mention only has a latent antecedent. We therefore use a loss function that maximizes the sum of the coreference probability of any of the legal antecedents. For a given mention i with possible antecedents Y(i), let GOLD(i) be the set of mentions in the gold cluster containing i. Since the set of mentions occurring before i is Y(i), the set of mentions in that gold cluster that also occur before i is Y(i)∩GOLD(i). We therefore want to maximize:

$$\sum_{∩}$$

P(ˆy) (24.56)
若提及 i 不在黄金簇中，则 GOLD(i) = ϵ。

> If a mention i is not in a gold cluster GOLD(i) = ϵ.

> ˆy∈Y(i)∩GOLD(i)

为把这个概率变成损失函数，我们将使用交叉熵损失

> To turn this probability into a loss function, we’ll use the cross-entropy loss
函数（我们在第 4 章式 4.19 中定义过），即取该概率的 −log。

> function we defined in Eq. 4.19 in Chapter 4, by taking the −log of the probability.

如果再把所有提及求和，就得到用于训练的最终损失函数：

> If we then sum over all mentions, we get the final loss function for training:

> N

X X
L = −log P(ˆy) (24.57)

> i=2 ˆy∈Y(i)∩GOLD(i)

## 24.7 实体链接

> 24.7 Entity Linking

实体链接是把文本中的一个提及与……的表示相关联的任务

> Entity linking is the task of associating a mention in text with the representation of

> `entity linking`（实体链接）
>
> 释义：指把文本中出现的提及映射到知识库中某个具体实体的表示，从而确定其指向的现实对象。

本体或知识库中的某个现实世界实体（Ji and Grishman, 2011）。它是共指消解的自然延续；共指消解的任务是把指向同一实体的文本提及关联起来。实体链接则更进一步，要识别出该实体究竟是谁。对于任何需要链接到知识库的 NLP 任务来说，它尤为重要。

> some real-world entity in an ontology or knowledge base (Ji and Grishman, 2011). It is the natural follow-on to coreference resolution; coreference resolution is the task of associating textual mentions that corefer to the same entity. Entity linking takes the further step of identifying who that entity is. It is especially important for any NLP task that links to a knowledge base.

虽然存在各种各样的潜在知识库，但本节我们将聚焦于

> While there are all sorts of potential knowledge-bases, we’ll focus in this section
Wikipedia，因为它被广泛用作 NLP 任务的本体。在这种用法下，每个唯一的 Wikipedia 页面充当某个特定实体的唯一 id。判断一个文本提及究竟指称哪个人物所对应的 Wikipedia 页面，这项任务有自己的名字：维基化（wikification，Mihalcea and Csomai, 2007）。

> on Wikipedia, since it’s widely used as an ontology for NLP tasks. In this usage, each unique Wikipedia page acts as the unique id for a particular entity. This task of deciding which Wikipedia page corresponding to an individual is being referred to by a text mention has its own name: wikification (Mihalcea and Csomai, 2007).

> `wikification`（维基化）
>
> 释义：把一个文本提及链接到对应的 Wikipedia 实体页面，从而确定该提及究竟指称哪个具体实体。

自最早的系统问世以来（Mihalcea and Csomai 2007, Cucerzan 2007, Milne

> Since the earliest systems (Mihalcea and Csomai 2007, Cucerzan 2007, Milne
and Witten 2008），实体链接（大致）分两个阶段完成：提及检测与提及消歧。我们将给出两种算法，一种是使用锚词典和来自 Wikipedia 图结构信息的简单经典基线（Ferragina and Scaiella, 2011），另一种是现代神经算法（Li et al., 2020）。这里我们主要关注实体链接在问题上的应用，因为大量文献都处于这一语境中。

> and Witten 2008), entity linking is done in (roughly) two stages: mention detection and mention disambiguation. We’ll give two algorithms, one simple classic baseline that uses anchor dictionaries and information from the Wikipedia graph structure (Ferragina and Scaiella, 2011) and one modern neural algorithm (Li et al., 2020). We’ll focus here mainly on the application of entity linking to questions, since a lot of the literature has been in that context.

### 24.7.1 基于锚词典与 Web 图的链接

> 24.7.1 Linking based on Anchor Dictionaries and Web Graph

作为一个简单基线，我们介绍用于 Wikipedia 的 TAGME 链接器（Ferragina and Scaiella, 2011），它本身借鉴了更早的算法（Mihalcea and Csomai 2007, Cucerzan 2007, Milne and Witten 2008）。维基化算法把实体集合定义为 Wikipedia 页面的集合，因此我们把每个 Wikipedia 页面称为一个唯一实体 e。TAGME 首先建立所有实体的目录（即所有 Wikipedia 页面，去除一些消歧页面和其他元页面），并把它们索引到一个标准 IR 引擎（如 Lucene）中。对于每个页面 e，该算法计算一个入链计数 in(e)：即从其他 Wikipedia 页面指向 e 的入链总数。

> As a simple baseline we introduce the TAGME linker (Ferragina and Scaiella, 2011) for Wikipedia, which itself draws on earlier algorithms (Mihalcea and Csomai 2007, Cucerzan 2007, Milne and Witten 2008). Wikification algorithms define the set of entities as the set of Wikipedia pages, so we’ll refer to each Wikipedia page as a unique entity e. TAGME first creates a catalog of all entities (i.e. all Wikipedia pages, removing some disambiguation and other meta-pages) and indexes them in a standard IR engine like Lucene. For each page e, the algorithm computes an in-link count in(e): the total number of in-links from other Wikipedia pages that point to e.

这些计数可以从 Wikipedia 数据转储中导出。

> These counts can be derived from Wikipedia dumps.

最后，该算法需要一本锚词典。一本锚词典

> Finally, the algorithm requires an anchor dictionary. An anchor dictionary
为每个 Wikipedia 页面列出它的锚文本：即带超链接的文本片段

> lists for each Wikipedia page, its anchor texts: the hyperlinked spans of text on

> `anchor texts`（锚文本）
>
> 释义：指向某个 Wikipedia 页面的超链接中显示出来的那段文本，同一个人物或实体往往对应多个不同的锚文本。

这些片段位于指向它的其他页面上。例如，斯坦福大学的网页 http://www.stanford.edu，可能被另一个页面用诸如 Stanford 或 Stanford University 这样的锚文本指向：

> other pages that point to it. For example, the web page for Stanford University, http://www.stanford.edu, might be pointed to from another page using anchor texts like Stanford or Stanford University:

<a href="http://www.stanford.edu">Stanford University</a>
我们这样计算 Wikipedia 锚词典：对每个 Wikipedia

> We compute a Wikipedia anchor dictionary by including, for each Wikipedia
页面 e，收录 e 的标题，以及所有指向 e 的 Wikipedia 页面中的全部锚文本。

> page e, e’s title as well as all the anchor texts from all Wikipedia pages that point to e.

对于每个锚字符串 a，我们还计算它在 Wikipedia 中的总频次 freq(a)（包括非锚用法），a 作为链接出现的次数（我们称之为 link(a)），以及它的链接概率 linkprob(a) = link(a)/freq(a)。最终锚词典还需要做一些清理，例如删除仅由数字或单个字符组成的锚字符串、极为罕见的锚字符串，或者因为 linkprob 很低而极不可能是有用实体的锚字符串。

> For each anchor string a we’ll also compute its total frequency freq(a) in Wikipedia(including non-anchor uses), the number of times a occurs as a link (which we’ll call link(a)), and its link probability linkprob(a) = link(a)/freq(a). Some cleanup of the final anchor dictionary is required, for example removing anchor strings composed only of numbers or single characters, that are very rare, or that are very unlikely to be useful entities because they have a very low linkprob.

提及检测 给定一个问题（或我们试图链接的其他文本），TAGME 通过查询锚词典来检测提及，查询对象是每个长度最多 6 个词的词元序列。这个庞大的序列集合会用一些简单的启发式规则剪枝（例如，若子串的 linkprob 很小就将其剪掉）。问题：

> Mention Detection Given a question (or other text we are trying to link), TAGME detects mentions by querying the anchor dictionary for each token sequence up to 6 words. This large set of sequences is pruned with some simple heuristics (for example pruning substrings if they have small linkprobs). The question:

Ada Lovelace 是什么时候出生的？

> When was Ada Lovelace born?

可能产生锚 Ada Lovelace，也可能产生锚 Ada，但像 Lovelace 这样的子串跨度可能因 linkprob 太低而被剪掉，而像 born 这样的跨度 linkprob 低到根本不会出现在锚词典中。

> might give rise to the anchor Ada Lovelace and possibly Ada, but substrings spans like Lovelace might be pruned as having too low a linkprob, and but spans like born have such a low linkprob that they would not be in the anchor dictionary at all.

提及消歧 如果一个提及跨度是无歧义的（只指向一个实体/Wikipedia 页面），那么实体链接就做完了！然而，许多跨度是有歧义的，能匹配多个 Wikipedia 实体/页面的锚。TAGME 算法使用两个因素来消解有歧义的跨度，它们分别被称为先验概率和关联度/一致性。第一个因素是 p(e|a)，即该跨度指称某个特定实体的概率。对于每个页面 e ∈E(a)，锚 a 指向 e 的概率 p(e|a)，等于以锚文本 a 指向 e 的链接数与 a 作为锚出现的总次数之比：

> Mention Disambiguation If a mention span is unambiguous (points to only one entity/Wikipedia page), we are done with entity linking! However, many spans are ambiguous, matching anchors for multiple Wikipedia entities/pages. The TAGME algorithm uses two factors for disambiguating ambiguous spans, which have been referred to as prior probability and relatedness/coherence. The first factor is p(e|a), the probability with which the span refers to a particular entity. For each page e ∈E(a), the probability p(e|a) that anchor a points to e, is the ratio of the number of links into e with anchor text a to the total number of occurrences of a as an anchor:

prior(a →e) = p(e|a) = count(a →e) (24.58)
link(a)
让我们看看这个因素在下面这个问题中链接实体时是如何起作用的：

> Let’s see how that factor works in linking entities in the following question:

Yuan 之前是中国的哪个朝代？

> What Chinese Dynasty came before the Yuan?

在锚词典中，跨度 Yuan 最常见的关联是中国货币的名称，即概率 p(Yuan currency| yuan) 非常高。

> The most common association for the span Yuan in the anchor dictionary is the name of the Chinese currency, i.e., the probability p(Yuan currency| yuan) is very high.

Yuan 较少见的 Wikipedia 关联包括常见的中国姓氏、一种在泰国使用的语言，以及本例中正确的实体，即中国朝代的名称。因此，如果我们仅根据 p(e|a) 来做选择，就会做出错误的消歧，错过正确的链接 Yuan dynasty。

> Rarer Wikipedia associations for Yuan include the common Chinese last name, a language spoken in Thailand, and the correct entity in this case, the name of the Chinese dynasty. So if we chose based only on p(e|a) , we would make the wrong disambiguation and miss the correct link, Yuan dynasty.

正是为了帮助处理这类情况，TAGME 使用了第二个因素，即

> To help in just this sort of case, TAGME uses a second factor, the relatedness of
该实体与输入问题中其他实体之间的关联度。在我们的例子中，问题还包含跨度 Chinese Dynasty，它有很大概率链接到页面 Dynasties in Chinese history，这一事实应当有助于匹配到 Yuan dynasty。

> this entity to other entities in the input question. In our example, the fact that the question also contains the span Chinese Dynasty, which has a high probability link to the page Dynasties in Chinese history, ought to help match Yuan dynasty.

让我们看看这是如何工作的。给定一个问题 q，对于每个候选锚跨度

> Let’s see how this works. Given a question q, for each candidate anchors span
a（在 q 中检测到的），我们为 a 的每个可能实体 e ∈E(a) 赋予一个关联度分数。

> a detected in q, we assign a relatedness score to each possible entity e ∈E(a) of a.

链接 a →e 的关联度分数，是 e 与 q 中所有其他实体之间关联度的加权平均。两个实体之所以被视为相关，取决于它们的 Wikipedia 页面共享多少入链。更形式化地说，两个实体 A 与 B 之间的关联度计算如下

> The relatedness score of the link a →e is the weighted average relatedness between e and all other entities in q. Two entities are considered related to the extent their Wikipedia pages share many in-links. More formally, the relatedness between two entities A and B is computed as
rel(A,B) = log(max(|in(A)|,|in(B)|))−log(|in(A)∩in(B)|)
log(|W|)−log(min(|in(A)|,|in(B)|)) 其中 in(x) 是指向 x 的 Wikipedia 页面集合，W 是该集合中所有 Wikipedia 页面的集合。

> log(|W|)−log(min(|in(A)|,|in(B)|)) where in(x) is the set of Wikipedia pages pointing to x and W is the set of all Wikipedia pages in the collection.

锚 b 对候选标注 a →X 所投的票是平均值，

> The vote given by anchor b to the candidate annotation a →X is the average,
即在 b 的所有可能实体上，它们与 X 的关联度按各自先验概率加权后的平均：

> over all the possible entities of b, of their relatedness to X, weighted by their prior probability:

1 X
vote(b,X) = rel(X,Y)p(Y|b) (24.60)
|E(b)|
a →X 的总相关度得分，是 q 中检测到的所有其他锚点投票之和：

> The total relatedness score for a →X is the sum of the votes of all the other anchors detected in q:

> Y∈E(b)

$$\sum_{\in X q \\}$$

relatedness(a →X) = vote(b,X) (24.61)
为给 a →X 打分，我们结合相关度与先验概率，做法是选择实体 X

> To score a →X, we combine relatedness and prior by choosing the entity X
该实体具有最高的 relatedness(a →X)；再找出与该值相差不超过一个小量 ϵ 的其他实体，并从这个集合中选择先验 P(X|a) 最高的实体。这一步的结果是为 q 中的每个跨度各指派一个实体。

> that has the highest relatedness(a →X), finding other entities within a small ϵ of this value, and from this set, choosing the entity with the highest prior P(X|a). The result of this step is a single entity assigned to each span in q.

> b∈Xq\a

TAGME 算法还有一个步骤，用于剪除虚假的锚点/实体

> The TAGME algorithm has one further step of pruning spurious anchor/entity
对，并赋予一个将链接概率与一致性取平均的得分。

> pairs, assigning a score averaging link probability with the coherence.

1 X
coherence(a →X) = rel(B,X)
|S|−1
score(a →X) = coherence(a →X)+linkprob(a) (24.62)
2
最后，若 score(a →X) < λ，则剪除相应的对，其中阈值 λ 在一个留出集上设定。

> Finally, pairs are pruned if score(a →X) < λ, where the threshold λ is set on a held-out set.

> B∈S\X

### 24.7.2 基于神经图的链接

> 24.7.2 Neural Graph-based linking

较新的实体链接模型基于双编码器：对候选提及跨度进行编码，对实体进行编码，再计算两个编码之间的点积。这样，知识库中所有实体的嵌入都可以预先计算并缓存（Wu et al., 2020）。下面概述 Li et al. (2020) 的 ELQ 链接算法：该算法输入一个问题 q 以及一组来自 Wikipedia 的候选实体（附带相应的 Wikipedia 文本），输出由实体 id、提及起点和提及终点构成的元组 (e,ms,me)。如图 24.8 所示，其做法是用 Wikipedia 文本对每个 Wikipedia 实体进行编码，用问题文本对每个提及跨度进行编码，再计算二者的相似度，具体如下所述。

> More recent entity linking models are based on bi-encoders, encoding a candidate mention span, encoding an entity, and computing the dot product between the encodings. This allows embeddings for all the entities in the knowledge base to be precomputed and cached (Wu et al., 2020). Let’s sketch the ELQ linking algorithm of Li et al. (2020), which is given a question q and a set of candidate entities from Wikipedia with associated Wikipedia text, and outputs tuples (e,ms,me) of entity id, mention start, and mention end. As Fig. 24.8 shows, it does this by encoding each Wikipedia entity using text from Wikipedia, encoding each mention span using text from the question, and computing their similarity, as we describe below.

实体提及检测 为了得到每个问题词元的 h 维嵌入，算法以常规方式将问题输入 BERT：

> Entity Mention Detection To get an h-dimensional embedding for each question token, the algorithm runs the question through BERT in the normal way:

$$[ q _{1} \cdot \cdot \cdot q _{n} ] = \text{BERT} ([ \texttt{CLS} ] q _{1} \cdot \cdot \cdot q _{n} [ \texttt{SEP} ])$$

随后，它以类似于上文阅读理解器中基于跨度的算法的方式，计算 q 中每个跨度 [i, j] 是实体提及的似然。首先计算 i/j 作为提及起点/终点的得分：

> It then computes the likelihood of each span [i, j] in q being an entity mention, in a way similar to the span-based algorithm we saw for the reader above. First we compute the score for i/j being the start/end of a mention:

$$s _{\text{start}} ( i ) = w _{\text{start}} \cdot q _{i} , s _{\text{end}} ( j ) = w _{\text{end}} \cdot q _{j} ,$$

![](images/24-coreference-entity-linking/fig_p23_0.png)

*图 24.8 ELQ 算法在问题中进行实体链接的推理过程示意（Li et al., 2020）。每个候选的问题提及跨度与候选实体分别编码，然后通过实体/跨度点积打分。*
*Figure 24.8 A sketch of the inference process in the ELQ algorithm for entity linking in questions (Li et al., 2020). Each candidate question mention span and candidate entity are separately encoded, and then scored by the entity/span dot product.*

其中 wstart 与 wend 是训练中学到的向量。接下来，用另一个可训练的嵌入 wmention 计算每个词元属于某个提及的得分：

> where wstart and wend are vectors learned during training. Next, another trainable embedding, wmention is used to compute a score for each token being part of a mention:

$$s _{\text{mention}} ( t ) = w _{\text{mention}} \cdot q _{t}$$

然后通过组合这三个得分来计算提及概率：

> Mention probabilities are then computed by combining these three scores:

!

> j

$$\sum_{t = i}^{j}$$

p([i, j]) = σ sstart(i)+send(j)+ smention(t) (24.66)
实体链接 为了把提及链接到实体，我们接下来为全部 Wikipedia 实体构成的集合 E = e1,··· ,ei,··· ,ew 中的每个实体计算嵌入。对于每个实体 ei，我们取其 Wikipedia 页面的文本，即标题 t(ei) 以及该 Wikipedia 页面的前 128 个词元（我们称之为描述 d(ei)）。这些内容同样输入 BERT，并取 CLS 词元的输出 BERT[CLS] 作为实体表示：

> Entity Linking To link mentions to entities, we next compute embeddings for each entity in the set E = e1,··· ,ei,··· ,ew of all Wikipedia entities. For each entity ei we’ll get text from the entity’s Wikipedia page, the title t(ei) and the first 128 tokens of the Wikipedia page which we’ll call the description d(ei). This is again run through BERT, taking the output of the CLS token BERT[CLS] as the entity representation:

> t=i

$$x _{e i} = \text{BERT} _{\text{[CLS]}} ([ \texttt{CLS} ] t ( e _{i} )[ \texttt{ENT} ] d ( e _{i} )[ \texttt{SEP} ])$$

通过为每个实体 e 与跨度 [i, j] 计算跨度编码（各词元嵌入的平均）与实体编码之间的点积相似度，即可把提及跨度链接到实体。

> Mention spans can be linked to entities by computing, for each entity e and span[i, j], the dot product similarity between the span encoding (the average of the token embeddings) and the entity encoding.

> j

1 X
yi,j = (j −i+1) qt

> t=i

$$s ( e , [ i , j ]) = x ^{\cdot} _{e}$$

$$^{\cdot} _{e} y _{i , j}$$

最后，我们取 softmax，得到每个跨度上关于实体的分布：

> Finally, we take a softmax to get a distribution over entities for each span:

exp(s(e,[i, j])) (24.69)
p(e|[i, j]) = P

$$_{e ′ \in E} \text{exp} ( s ( e ^{′} , [ i , j ]))$$

训练 ELQ 的提及检测与实体链接算法是全监督的。这意味着，与 24.7.1 节中的锚词典算法不同，它要求数据集中的实体边界已被标注并链接。两个这样的标注数据集是 WebQuestionsSP（Yih et al., 2016）和 GraphQuestions（Su et al., 2016），前者是源自 Google 搜索问题的 WebQuestions（Berant et al., 2013）数据集的扩展。二者的问句中实体跨度都已被标注并链接（Sorokin and Gurevych 2018, Li et al. 2020），从而产生了实体标注版本 WebQSPEL 和 GraphQEL（Li et al., 2020）。

> Training The ELQ mention detection and entity linking algorithm is fully supervised. This means, unlike the anchor dictionary algorithms from Section 24.7.1, it requires datasets with entity boundaries marked and linked. Two such labeled datasets are WebQuestionsSP (Yih et al., 2016), an extension of the WebQuestions(Berant et al., 2013) dataset derived from Google search questions, and GraphQuestions (Su et al., 2016). Both have had entity spans in the questions marked and linked (Sorokin and Gurevych 2018, Li et al. 2020) resulting in entity-labeled versions WebQSPEL and GraphQEL (Li et al., 2020).

给定一个训练集，ELQ 的提及检测阶段与实体链接阶段被

> Given a training set, the ELQ mention detection and entity linking phases are
联合训练，优化二者损失之和。提及检测损失是二元交叉熵损失，其中 L 为段落长度，N 为候选数量：

> trained jointly, optimizing the sum of their losses. The mention detection loss is a binary cross-entropy loss, with L the length of the passage and N the number of candidates:

LMD = −1 X
y[i,j] log p([i, j])+(1−y[i,j])log(1−p([i, j])) (24.70)
N
其中若 [i, j] 是标准提及跨度则 y[i,j] = 1，否则为 0。实体链接损失为：

> with y[i,j] = 1 if [i, j] is a gold mention span, else 0. The entity linking loss is:

> 1≤i≤j≤min(i+L−1,n)

$$L _{\text{ED}} = - \text{logp} ( e _{g} | [ i , j ])$$

其中 eg 是提及 [i, j] 对应的标准实体。

> where eg is the gold entity for mention [i, j].

## 24.8 共指消解的评价

> 24.8 Evaluation of Coreference Resolution

我们以模型论的方式评价共指算法，将系统产生的一组假设链或簇 H 与人工标注得到的一组标准链或参考链或簇 R 进行比较，并报告精确率与召回率。

> We evaluate coreference algorithms model-theoretically, comparing a set of hypothesis chains or clusters H produced by the system against a set of gold or reference chains or clusters R from a human labeling, and reporting precision and recall.

然而，进行这种比较的方法多种多样。事实上，

> However, there are a wide variety of methods for doing this comparison. In fact,
有 5 种常用于评价共指算法的指标：基于链接的 MUC（Vilain et al., 1995）和 BLANC（Recasens and Hovy 2011, Luo et al. 2014）指标、基于提及的 B³ 指标（Bagga and Baldwin, 1998）、基于实体的 CEAF 指标（Luo, 2005），以及基于链接且考虑实体的 LEA 指标（Moosavi and Strube, 2016）。

> there are 5 common metrics used to evaluate coreference algorithms: the link based MUC (Vilain et al., 1995) and BLANC (Recasens and Hovy 2011, Luo et al. 2014) metrics, the mention based B3 metric (Bagga and Baldwin, 1998), the entity based CEAF metric (Luo, 2005), and the link based entity aware LEA metric (Moosavi and Strube, 2016).

> `MUC`
>
> 释义：一种基于链接的评价指标，通过统计共指链接的重合数量来计算精确率与召回率。

我们只探讨其中两个指标。MUC F 值（Vilain et al., 1995）

> Let’s just explore two of the metrics. The MUC F-measure (Vilain et al., 1995)

> `F-measure`（F 值）
>
> 释义：精确率与召回率的调和平均，用于把共指评价的两项数值综合为单一分数。

基于 H 与 R 共有的共指链接（提及对）数量，

> is based on the number of coreference links (pairs of mentions) common to H and

- 精确率是共有链接的数量除以 H 中链接的数量。

> Precision is the number of common links divided by the number of links in H.

召回率是共有链接的数量除以 R 中链接的数量；这使得 MUC 偏向于产生大链（以及更少实体）的系统，并且它忽略单例，因为单例不涉及链接。

> Recall is the number of common links divided by the number of links in R; This makes MUC biased toward systems that produce large chains (and fewer entities), and it ignores singletons, since they don’t involve links.

B³ 基于提及而非基于链接。对于参考链中的每个提及

> B3 is mention-based rather than link-based. For each mention in the reference

> `B3`（B³）
>
> 释义：一种基于提及的评价指标，对每个提及分别计算精确率与召回率再加权求和。

链，我们计算一个精确率与召回率，然后对文档中全部 N 个提及进行加权求和，以计算整个任务的精确率与召回率。对于给定的提及 i，令 R 为包含 i 的参考链，H 为包含 i 的假设链。H 中的正确提及集合为 H ∩R。因此提及 i 的精确率为 |H∩R| |H| ，提及 i 的召回率为 |H∩R| |R| 。总精确率是提及 i 精确率的加权求和，权重为 wi。总召回率是提及 i 召回率的加权求和，权重为 wi。等价地：

> chain, we compute a precision and recall, and then we take a weighted sum over all N mentions in the document to compute a precision and recall for the entire task. For a given mention i, let R be the reference chain that includes i, and H the hypothesis chain that has i. The set of correct mentions in H is H ∩R. Precision for mention i is thus |H∩R| |H| , and recall for mention i thus |H∩R| |R| . The total precision is the weighted sum of the precision for mention i, weighted by a weight wi. The total recall is the weighted sum of the recall for mention i, weighted by a weight wi. Equivalently:

> N

X 包含 entityi 的假设链中正确提及的数量

> X # of correct mentions in hypothesis chain containing entityi
精确率 = wi

> Precision = wi
包含 entityi 的假设链中提及的数量

> # of mentions in hypothesis chain containing entityi
X 包含 entityi 的假设链中正确提及的数量

> X # of correct mentions in hypothesis chain containing entityi
召回率 = wi

> Recall = wi
包含 entityi 的参考链中提及的数量 每个实体的权重 wi 可以设为不同的值，以产生该算法的不同版本。

> # of mentions in reference chain containing entityi The weight wi for each entity can be set to different values to produce different versions of the algorithm.

> i=1

遵循 Denis and Baldridge (2009) 的提议，CoNLL 共指

> Following a proposal from Denis and Baldridge (2009), the CoNLL coreference
竞赛基于 MUC、CEAF-e 和 B³ 的平均值进行评分（Pradhan et al. 2011, Pradhan et al. 2012b），因此在许多评测活动中报告这 3 个指标的平均值是很常见的。关于整套指标的详细描述参见 Luo and Pradhan (2016)；应当使用这些指标的参考实现，而不是尝试从零重新实现（Pradhan et al., 2014）。

> competitions were scored based on the average of MUC, CEAF-e, and B3 (Pradhan et al. 2011, Pradhan et al. 2012b), and so it is common in many evaluation campaigns to report an average of these 3 metrics. See Luo and Pradhan (2016) for a detailed description of the entire set of metrics; reference implementations of these should be used rather than attempting to reimplement from scratch (Pradhan et al., 2014).

人们还提出了处理特定共指领域或任务的替代指标。例如，考虑将提及解析为命名实体（人物、组织、地缘政治实体）的任务，这可能对信息抽取或知识库补全有用。一个假设链如果正确地包含了指向某实体的所有代词，却不包含该名称本身的任何形式，或者链接到了错误的名称，那么它对这一任务就毫无用处。我们可能反而想要一种按每个提及的信息量对其加权的指标（名称的信息量最大）（Chen and Ng, 2013），或者一种只有在假设链至少包含名称的某一变体时才认为其与标准链匹配的指标（Agarwal et al. (2019) 的 NEC F1 指标）。

> Alternative metrics have been proposed that deal with particular coreference domains or tasks. For example, consider the task of resolving mentions to named entities (persons, organizations, geopolitical entities), which might be useful for information extraction or knowledge base completion. A hypothesis chain that correctly contains all the pronouns referring to an entity, but has no version of the name itself, or is linked with a wrong name, is not useful for this task. We might instead want a metric that weights each mention by how informative it is (with names being most informative) (Chen and Ng, 2013) or a metric that considers a hypothesis to match a gold chain only if it contains at least one variant of a name (the NEC F1 metric of Agarwal et al. (2019)).

## 24.9 Winograd 模式问题

> 24.9 Winograd Schema problems

从该领域早期开始，研究者就注意到某些共指情形相当困难，似乎需要世界知识或复杂的推理才能解决。Winograd (1972) 用下面这个例子最为著名地指出了该问题：

> From early on in the field, researchers have noted that some cases of coreference are quite difficult, seeming to require world knowledge or sophisticated reasoning to solve. The problem was most famously pointed out by Winograd (1972) with the following example:

(24.72) 市议会拒绝给示威者发放许可，因为

> (24.72) The city council denied the demonstrators a permit because

- 他们害怕暴力。
- 他们鼓吹暴力。

> they feared violence.
> they advocated violence.

Winograd 注意到，在接续句（a）中，大多数读者为代词 they 首选的先行语是市议会，而在（b）中则是示威者。

> Winograd noticed that the antecedent that most readers preferred for the pronoun they in continuation (a) was the city council, but in (b) was the demonstrators.

他指出，这要求理解第二个分句意在作为对第一个分句的解释，并且我们的文化框架表明，市议会也许比示威者更可能害怕暴力，而示威者则也许更可能鼓吹暴力。

> He suggested that this requires understanding that the second clause is intended as an explanation of the first clause, and also that our cultural frames suggest that city councils are perhaps more likely than demonstrators to fear violence and that demonstrators might be more likely to advocate violence.

为了让 NLP 领域更多地关注涉及世界

> In an attempt to get the field of NLP to focus more on methods involving world
知识与常识推理的方法，Levesque（2011）提出了一个名为 Winograd Schema Challenge 的挑战任务。8 该挑战任务中的问题

> knowledge and common-sense reasoning, Levesque (2011) proposed a challenge task called the Winograd Schema Challenge.8 The problems in the challenge task

> `Winograd schema`（Winograd 模式）
>
> 释义：指一类共指测试题：两个句子仅相差一个词，需依据常识而非词汇关联判断代词所指，用以考察世界知识与常识推理。

是一类共指问题，其设计意图是让人类读者能够轻松消解歧义，但希望无法用选择限制之类的简单技术或其他基本的词语关联方法来解决。

> are coreference problems designed to be easily disambiguated by the human reader, but hopefully not solvable by simple techniques such as selectional restrictions, or other basic word association methods.

这些问题被设计为一对语句，它们仅在一个词或

> The problems are framed as a pair of statements that differ in a single word or
短语上有所不同，外加一个共指问题：

> phrase, and a coreference question:

（24.73）奖杯装不进手提箱，因为它太大了。

> (24.73) The trophy didn’t fit into the suitcase because it was too large.

问题：什么太大了？答案：奖杯

> Question: What was too large? Answer: The trophy
（24.74）奖杯装不进手提箱，因为它太小了。

> (24.74) The trophy didn’t fit into the suitcase because it was too small.

> 在 IJCAI 会议上举办的竞赛（Davis et al., 2017），以及一个自然语言推理版本
>
> *competition at the IJCAI conference (Davis et al., 2017), and a natural language inference version of the*

问题：什么太小了？答案：手提箱

> Question: What was too small? Answer: The suitcase
这些问题具有以下特征：

> The problems have the following characteristics:

- 每个问题都涉及两方
- 代词优先指向其中一方，但从语法上讲也可以指向另一方
- 问题询问代词指代的是哪一方
- 如果改动句中的某一个词，人类偏好的答案就会变为另一方

> The problems each have two parties
> A pronoun preferentially refers to one of the parties, but could grammatically also refer to the other
> A question asks which party the pronoun refers to
> If one word in the question is changed, the human-preferred answer changes to the other party

解决这些问题可能需要的那类世界知识会

> The kind of world knowledge that might be needed to solve the problems can
各不相同。在奖杯/手提箱的例子中，它是关于物理世界的知识：较大的物体无法装进较小的物体。在最初的 Winograd 句子中，它是关于政治家和抗议者等社会角色的刻板印象。在下面这类例子中，它是关于轮流发言或致谢等人类行为的知识。

> vary. In the trophy/suitcase example, it is knowledge about the physical world; that a bigger object cannot fit into a smaller object. In the original Winograd sentence, it is stereotypes about social actors like politicians and protesters. In examples like the following, it is knowledge about human actions like turn-taking or thanking.

（24.75）Bill 把 gameboy 递给 John，因为他的轮次[结束/下一个]。谁的

> (24.75) Bill passed the gameboy to John because his turn was [over/next]. Whose
轮次[结束/下一个]？答案：Bill/John

> turn was [over/next]? Answers: Bill/John
（24.76）Joan 确保感谢 Susan 所[给予/接受]的一切帮助。

> (24.76) Joan made sure to thank Susan for all the help she had [given/received].

谁[给予/接受]了帮助？答案：Susan/Joan。

> Who had [given/received] help? Answers: Susan/Joan.

尽管 Winograd 模式的设计初衷是要求常识推理，但原始问题集中有很大一部分可以由在 Winograd 模式句子上微调的预训练语言模型解决（Kocijan et al., 2019）。大型预训练语言模型编码了极其大量的世界知识或常识知识！因此当前的趋势是提出新的数据集，其中包含越来越难的类 Winograd 共指消解问题，例如 KNOWREF（Emami et al., 2019），其示例如下：

> Although the Winograd Schema was designed to require common-sense reasoning, a large percentage of the original set of problems can be solved by pretrained language models, fine-tuned on Winograd Schema sentences (Kocijan et al., 2019). Large pretrained language models encode an enormous amount of world or common-sense knowledge! The current trend is therefore to propose new datasets with increasingly difficult Winograd-like coreference resolution problems like KNOWREF(Emami et al., 2019), with examples like:

（24.77）Marcus 现在无疑比 Jarrett 快，但在[他的]巅峰时期，

> (24.77) Marcus is undoubtedly faster than Jarrett right now but in [his] prime the
差距并没有那么大。

> gap wasn’t all that big.

归根结底，语言建模与知识的某种结合似乎很可能会卓有成效；事实上，基于知识的模型似乎对 Winograd 模式训练集中的词汇特异性过拟合更少（Trichelair et al., 2018），

> In the end, it seems likely that some combination of language modeling and knowledge will prove fruitful; indeed, it seems that knowledge-based models overfit less to lexical idiosyncracies in Winograd Schema training sets (Trichelair et al., 2018),

## 24.10 共指中的性别偏见

> 24.10 Gender Bias in Coreference

与语言处理的其他方面一样，共指模型也表现出性别偏见及其他偏见（Zhao et al. 2018a, Rudinger et al. 2018, Webster et al. 2018）。例如，WinoBias 数据集（Zhao et al., 2018a）使用 Winograd 模式范式的一个变体，来检验共指算法在多大程度上倾向于把带性别的代词与符合文化刻板印象的先行语关联起来。正如我们在第 5 章所总结的，嵌入会在其训练数据中复制社会偏见，例如把男性与医生等历史上属于男性刻板印象的职业关联，把女性与秘书等女性刻板印象的职业关联（Caliskan et al. 2017, Garg et al. 2018）。

> As with other aspects of language processing, coreference models exhibit gender and other biases (Zhao et al. 2018a, Rudinger et al. 2018, Webster et al. 2018). For example the WinoBias dataset (Zhao et al., 2018a) uses a variant of the Winograd Schema paradigm to test the extent to which coreference algorithms are biased toward linking gendered pronouns with antecedents consistent with cultural stereotypes. As we summarized in Chapter 5, embeddings replicate societal biases in their training test, such as associating men with historically sterotypical male occupations like doctors, and women with stereotypical female occupations like secretaries (Caliskan et al. 2017, Garg et al. 2018).

一个 WinoBias 句子包含两个提及，分别对应刻板印象中的男性职业与女性职业，以及一个必须与其中之一关联的带性别代词。该句子无法通过代词的性别来消解歧义，但有偏见的模型可能被这一线索误导。下面是一个示例句子：

> A WinoBias sentence contain two mentions corresponding to stereotypicallymale and stereotypically-female occupations and a gendered pronoun that must be linked to one of them. The sentence cannot be disambiguated by the gender of the pronoun, but a biased model might be distracted by this cue. Here is an example sentence:

（24.78）秘书打电话给医生i，告诉他i有一位新病人

> (24.78) The secretary called the physiciani and told himi about a new patient
[符合刻板印象]

> [pro-stereotypical]
（24.79）秘书打电话给医生i，告诉她i有一位新病人

> (24.79) The secretary called the physiciani and told heri about a new patient
[违背刻板印象]

> [anti-stereotypical]
Zhao et al.（2018a）认为，如果一个共指系统在关联与性别刻板印象相符的职业的代词（例如（24.78）中 him 与 physician）时比在关联与性别刻板印象不符的职业的代词（例如（24.79）中 her 与 physician）时更准确，那么它就是有偏见的。他们表明，所有架构的共指系统（基于规则的、基于特征的机器学习的以及端到端神经的）都表现出显著偏见，在反刻板印象的情形中平均要差 21 个 F1 点。

> Zhao et al. (2018a) consider a coreference system to be biased if it is more accurate at linking pronouns consistent with gender stereotypical occupations (e.g., him with physician in (24.78)) than linking pronouns inconsistent with gender-stereotypical occupations (e.g., her with physician in (24.79)). They show that coreference systems of all architectures (rule-based, feature-based machine learned, and end-toend-neural) all show significant bias, performing on average 21 F1 points worse in the anti-stereotypical cases.

这种偏见的一个可能来源是，女性实体在用于训练大多数共指系统的 OntoNotes 数据集中严重不足。

> One possible source of this bias is that female entities are significantly underrepresented in the OntoNotes dataset, used to train most coreference systems.

Zhao et al.（2018a）提出了一种克服这种偏见的方法：他们生成第二个性别互换的数据集，其中 OntoNotes 里的所有男性实体都被替换为女性实体，反之亦然，并在原始数据与互换后数据合并而成的 OntoNotes 上重新训练共指系统，同时还使用去偏的 GloVE 嵌入（Bolukbasi et al., 2016）。由此得到的共指系统在 WinoBias 数据集上不再表现出偏见，同时对 OntoNotes 共指准确率没有显著影响。

> Zhao et al. (2018a) propose a way to overcome this bias: they generate a second gender-swapped dataset in which all male entities in OntoNotes are replaced with female ones and vice versa, and retrain coreference systems on the combined original and swapped OntoNotes data, also using debiased GloVE embeddings (Bolukbasi et al., 2016). The resulting coreference systems no longer exhibit bias on the WinoBias dataset, without significantly impacting OntoNotes coreference accuracy.

在一篇后续论文中，Zhao et al.（2019）表明，同样的偏见也存在于 ELMo 上下文词向量表示以及使用这些表示的共指系统中。他们表明，用数据增强重新训练 ELMo，同样能减轻或消除 WinoBias 上共指系统中的偏见。

> In a follow-up paper, Zhao et al. (2019) show that the same biases exist in ELMo contextualized word vector representations and coref systems that use them. They showed that retraining ELMo with data augmentation again reduces or removes bias in coreference systems on WinoBias.

Webster et al.（2018）引入了另一个数据集 GAP，以及带性别的

> Webster et al. (2018) introduces another dataset, GAP, and the task of Gendered
代词消解，作为开发更优的带性别代词共指算法的一种工具。GAP 是一个性别平衡的标注语料库，包含 4,454 个带有性别歧义代词的句子（相比之下，英语 OntoNotes 训练数据中只有 20% 的带性别代词是阴性的）。这些例子取自维基百科页面中自然出现的句子，用来构造难以消解的案例：其中包含两个性别相同的命名实体，以及一个可能指代其中任一人（或两人都不指代）的歧义代词，如下所示：

> Pronoun Resolution as a tool for developing improved coreference algorithms for gendered pronouns. GAP is a gender-balanced labeled corpus of 4,454 sentences with gendered ambiguous pronouns (by contrast, only 20% of the gendered pronouns in the English OntoNotes training data are feminine). The examples were created by drawing on naturally occurring sentences from Wikipedia pages to create hard to resolve cases with two named entities of the same gender and an ambiguous pronoun that may refer to either person (or neither), like the following:

（24.80）5 月，Fujisawa 加入 Mari Motohashi 的冰壶队，担任该队的队长（skip），并转移

> (24.80) In May, Fujisawa joined Mari Motohashi’s rink as the team’s skip, moving
从轻井泽回到北见，她曾在那里度过少女时代。

> back from Karuizawa to Kitami where she had spent her junior days.

Webster et al.（2018）表明，在 GAP 上，现代共指算法消解女性代词的表现明显差于消解男性代词。

> Webster et al. (2018) show that modern coreference algorithms perform significantly worse on resolving feminine pronouns than masculine pronouns in GAP.

Kurita et al.（2019）表明，一个基于 BERT 上下文化词表示的系统也表现出类似的偏见。

> Kurita et al. (2019) shows that a system based on BERT contextualized word representations shows similar bias.

## 24.11 小结

> 24.11 Summary

本章介绍了共指消解这一任务。

> This chapter introduced the task of coreference resolution.

- 该任务把文本中具有共指关系（即指称话语模型中同一话语实体）的提及链接在一起，从而得到一组共指链（也称为簇或实体）。
- 提及可以是定指 NP 或不定指 NP、代词（包括零代词）或名称。

> This is the task of linking together mentions in text which corefer, i.e. refer to the same discourse entity in the discourse model, resulting in a set of coreference chains (also called clusters or entities).
> Mentions can be definite NPs or indefinite NPs, pronouns (including zero pronouns) or names.

- 实体提及的表面形式与其信息状态（新、旧或可推断）以及该实体的可及性或显著性相关联。
- 有些 NP 不是指称表达式，例如 It is raining 中的虚指 it。
- 许多语料库带有人工标注的共指标注，可用于监督学习，包括面向英语、中文和阿拉伯语的 OntoNotes、面向英语的 ARRAU，以及面向西班牙语和加泰罗尼亚语的 AnCora。
- 提及检测可以从所有名词和命名实体出发，然后使用回指性分类器或指称性分类器滤除不构成提及的成分。
- 共指消解的三种常见架构是提及对、提及排序和基于实体的架构，每一种都可以使用基于特征的分类器或神经分类器。
- 现代共指系统趋向于端到端，在单一端到端架构中完成提及检测和共指消解。
- 算法学习文本跨度与中心的表示，并学习把回指语跨度与候选先行语跨度进行比较。
- 实体链接是把文本中的提及与本体中某个真实世界实体的表示相关联的任务。
- 共指系统的评估方式是与金标实体标签进行比较，使用 MUC、B³、CEAF、BLANC 或 LEA 等精确率/召回率指标。
- Winograd 模式挑战问题是一些困难的共指问题，似乎需要世界知识或复杂推理才能解决。
- 共指系统表现出性别偏见，可以使用 WinoBias 和 GAP 等数据集进行评估。

> The surface form of an entity mention is linked to its information status(new, old, or inferrable), and how accessible or salient the entity is.
> Some NPs are not referring expressions, such as pleonastic it in It is raining.
> Many corpora have human-labeled coreference annotations that can be used for supervised learning, including OntoNotes for English, Chinese, and Arabic, ARRAU for English, and AnCora for Spanish and Catalan.
> Mention detection can start with all nouns and named entities and then use anaphoricity classifiers or referentiality classifiers to filter out non-mentions.
> Three common architectures for coreference are mention-pair, mention-rank, and entity-based, each of which can make use of feature-based or neural classifiers.
> Modern coreference systems tend to be end-to-end, performing mention detection and coreference in a single end-to-end architecture.
> Algorithms learn representations for text spans and heads, and learn to compare anaphor spans with candidate antecedent spans.
> Entity linking is the task of associating a mention in text with the representation of some real-world entity in an ontology .
> Coreference systems are evaluated by comparing with gold entity labels using precision/recall metrics like MUC, B3, CEAF, BLANC, or LEA.
> The Winograd Schema Challenge problems are difficult coreference problems that seem to require world knowledge or sophisticated reasoning to solve.
> Coreference systems exhibit gender bias which can be evaluated using datasets like Winobias and GAP.

## 历史注记

> Historical Notes

自 20 世纪 70 年代以来，共指一直是自然语言处理的一部分（Woods et al. 1972, Winograd 1972）。话语模型以及共指的实体中心基础由 Karttunen（1969）（在第 3 届 COLING 会议上）提出，在语言语义学中也发挥了作用（Heim 1982, Kamp 1981）。但正是 Bonnie Webber 1978 年的博士论文及其后续工作（Webber 1983）探讨了该模型的计算层面，为实体如何在话语模型中得到表示、以及它们能以何种方式许可后续指称提供了基础性洞见。她给出的许多例子至今仍在挑战指称理论。

> Coreference has been part of natural language processing since the 1970s (Woods et al. 1972, Winograd 1972). The discourse model and the entity-centric foundation of coreference was formulated by Karttunen (1969) (at the 3rd COLING conference), playing a role also in linguistic semantics (Heim 1982, Kamp 1981). But it was Bonnie Webber’s 1978 dissertation and following work (Webber 1983) that explored the model’s computational aspects, providing fundamental insights into how entities are represented in the discourse model and the ways in which they can license subsequent reference. Many of the examples she provided continue to challenge theories of reference to this day.

Hobbs 算法9 是一种树搜索算法，它是一长串中的第一个

> The Hobbs algorithm9 is a tree-search algorithm that was the first in a long

> `Hobbs algorithm`（Hobbs 算法）
>
> 释义：一种基于句法分析树、按固定顺序搜索当前句与前面各句中的 NP 以确定代词先行语的算法。

……一系列基于句法的方法，用于在自然出现的文本中稳健地识别指称。Hobbs 算法的输入是一个待消解的代词，以及截至并包括当前句在内的各句的句法（成分）分析。算法的细节取决于所使用的语法，但可以通过 Kehler et al.（2004）给出的简化版本来理解，该版本只是在当前句和先前句的 NP 列表中搜索。这种简化的 Hobbs 算法按以下顺序搜索 NP：“(i) 在当前句中从右到左，从代词左侧的第一个 NP 开始；(ii) 在前一句中从左到右；(iii) 在前两句中从左到右；(iv) 在当前句中从左到右，从代词右侧的第一个名词组开始（用于后指）。第一个在数、性和人称上与代词一致的名词组被选为先行语”（Kehler et al., 2004）。

> series of syntax-based methods for identifying reference robustly in naturally occurring text. The input to the Hobbs algorithm is a pronoun to be resolved, together with a syntactic (constituency) parse of the sentences up to and including the current sentence. The details of the algorithm depend on the grammar used, but can be understood from a simplified version due to Kehler et al. (2004) that just searches through the list of NPs in the current and prior sentences. This simplified Hobbs algorithm searches NPs in the following order: “(i) in the current sentence from right-to-left, starting with the first NP to the left of the pronoun, (ii) in the previous sentence from left-to-right, (iii) in two sentences prior from left-to-right, and (iv) in the current sentence from left-to-right, starting with the first noun group to the right of the pronoun (for cataphora). The first noun group that agrees with the pronoun with respect to number, gender, and person is chosen as the antecedent” (Kehler et al., 2004).

Lappin and Leass（1994）是一个有影响力的基于实体的系统，它使用权值

> Lappin and Leass (1994) was an influential entity-based system that used weights
来组合句法特征和其他特征，随后不久由 Kennedy and Boguraev（1996）加以扩展，他们的系统免去了对完整句法分析的需要。

> to combine syntactic and other features, extended soon after by Kennedy and Boguraev (1996) whose system avoids the need for full syntactic parses.

大约在同一时期，中心化理论（Grosz et al., 1995）被应用

> Approximately contemporaneously centering (Grosz et al., 1995) was applied
于代词回指消解（Brennan et al. 1987），随后出现了大量聚焦于中心化在共指中应用的工作（Kameyama 1986, Di Eugenio 1990, Walker et al. 1994, Di Eugenio 1996, Strube and Hahn 1996, Kehler 1997a, Tetreault 2001, Iida et al. 2003）。Kehler and Rohde（2013）展示了如何将中心化与连贯性驱动的代词解释理论相结合。关于中心化在度量话语连贯性中的应用，参见第 25 章。

> to pronominal anaphora resolution by Brennan et al. (1987), and a wide variety of work followed focused on centering’s use in coreference (Kameyama 1986, Di Eugenio 1990, Walker et al. 1994, Di Eugenio 1996, Strube and Hahn 1996, Kehler 1997a, Tetreault 2001, Iida et al. 2003). Kehler and Rohde (2013) show how centering can be integrated with coherence-driven theories of pronoun interpretation. See Chapter 25 for the use of centering in measuring discourse coherence.

作为美国 DARPA 资助的 MUC 会议一部分的共指竞赛提供了早期带标注的共指数据集（1995 年的 MUC-6 和 1998 年的 MUC-7 语料库），并为后来的大量工作定下了基调：选择只关注最简单的同指共指情形（忽略桥接、转喻和部分—整体等困难情形），并把学界引向监督机器学习和 MUC 指标之类的评价指标（Vilain et al., 1995）。后来的 ACE 评测产出了英语、中文和阿拉伯语的带标注共指语料库，它们被广泛用于模型训练和评估。

> Coreference competitions as part of the US DARPA-sponsored MUC conferences provided early labeled coreference datasets (the 1995 MUC-6 and 1998 MUC-7 corpora), and set the tone for much later work, choosing to focus exclusively on the simplest cases of identity coreference (ignoring difficult cases like bridging, metonymy, and part-whole) and drawing the community toward supervised machine learning and metrics like the MUC metric (Vilain et al., 1995). The later ACE evaluations produced labeled coreference corpora in English, Chinese, and Arabic that were widely used for model training and evaluation.

这项 DARPA 工作从 90 年代中期开始把学界引向监督学习（Connolly et al. 1994, Aone and Bennett 1995, McCarthy and Lehnert 1995）。Soon et al.（2001）提出了一组基本特征，由 Ng and Cardie（2002b）加以扩展，此后 15 年里涌现了一系列机器学习模型。这些工作往往分别聚焦于代词回指消解（Kehler et al. 2004, Bergsma and Lin 2006）、完整 NP 共指（Cardie and Wagstaff 1999, Ng and Cardie 2002b, Ng 2005a）和定指 NP 指称（Poesio and Vieira 1998, Vieira and Poesio 2000），以及单独的回指性检测（Bean and Riloff 1999, Bean and Riloff 2004, Ng and Cardie 2002a, Ng 2004）或单例检测（de Marneffe et al., 2015）。

> This DARPA work influenced the community toward supervised learning beginning in the mid-90s (Connolly et al. 1994, Aone and Bennett 1995, McCarthy and Lehnert 1995). Soon et al. (2001) laid out a set of basic features, extended by Ng and Cardie (2002b), and a series of machine learning models followed over the next 15 years. These often focused separately on pronominal anaphora resolution (Kehler et al. 2004, Bergsma and Lin 2006), full NP coreference (Cardie and Wagstaff 1999, Ng and Cardie 2002b, Ng 2005a) and definite NP reference (Poesio and Vieira 1998, Vieira and Poesio 2000), as well as separate anaphoricity detection (Bean and Riloff 1999, Bean and Riloff 2004, Ng and Cardie 2002a, Ng 2004), or singleton detection(de Marneffe et al., 2015).

从提及对方法向提及排序方法的转变，其开创者是

> The move from mention-pair to mention-ranking approaches was pioneered by
Yang et al.（2003）和 Iida et al.（2003），他们提出了成对排序方法，随后由 Denis and Baldridge（2008）加以扩展，后者提出通过对所有先前提及做 softmax 来进行排序。在单一端到端模型中联合完成提及检测、回指性和共指消解的想法，源于以下几项早期工作：Ng（2005b）提出为提及排序使用一个虚拟先行语，使“非指称”成为共指分类器的一个选项；Denis and Baldridge 2007 年的联合系统把回指性分类器的概率与共指概率结合起来；Denis and Baldridge（2008）的排序模型；以及 Rahman and Ng（2009）提出的用单一目标联合训练这两个模型。

> Yang et al. (2003) and Iida et al. (2003) who proposed pairwise ranking methods, then extended by Denis and Baldridge (2008) who proposed to do ranking via a softmax over all prior mentions. The idea of doing mention detection, anaphoricity, and coreference jointly in a single end-to-end model grew out of the early proposal of Ng(2005b) to use a dummy antecedent for mention-ranking, allowing ‘non-referential’to be a choice for coreference classifiers, Denis and Baldridge’s 2007 joint system combining anaphoricity classifier probabilities with coreference probabilities, the Denis and Baldridge (2008) ranking model, and the Rahman and Ng (2009) proposal to train the two models jointly with a single objective.

在 2010 年代，用于共指消解的简单基于规则的系统重新受到重视，

> Simple rule-based systems for coreference returned to prominence in the 2010s,
部分原因是它们能够以高精确率的方式编码基于实体的特征（Zhou et al. 2004b, Haghighi and Klein 2009, Raghunathan et al. 2010, Lee et al. 2011, Lee et al. 2013, Hajishirzi et al. 2013），但最终它们因无力处理正确应对普通名词共指情形所必需的语义而受累。

> partly because of their ability to encode entity-based features in a high-precision way(Zhou et al. 2004b, Haghighi and Klein 2009, Raghunathan et al. 2010, Lee et al. 2011, Lee et al. 2013, Hajishirzi et al. 2013) but in the end they suffered from an inability to deal with the semantics necessary to correctly handle cases of common noun coreference.

回归监督学习带来了提及排序方面的一系列进展

> A return to supervised learning led to a number of advances in mention-ranking
模型，这些模型也被扩展为神经架构，例如使用强化学习直接优化共指评价模型 Clark and Manning（2016a），以及从跨度抽取开始一路做端到端共指消解（Lee et al. 2017b, Zhang et al. 2018）。神经模型还被设计为利用全局的实体级信息（Clark and Manning 2016b, Wiseman et al. 2016, Lee et al. 2018）。

> models which were also extended into neural architectures, for example using re- inforcement learning to directly optimize coreference evaluation models Clark and Manning (2016a), doing end-to-end coreference all the way from span extraction(Lee et al. 2017b, Zhang et al. 2018). Neural models also were designed to take advantage of global entity-level information (Clark and Manning 2016b, Wiseman et al. 2016, Lee et al. 2018).

共指还与第 11 章讨论的实体链接任务相关。

> Coreference is also related to the task of entity linking discussed in Chapter 11.

共指可以为实体链接提供更多可能的表层形式，从而有助于链接到正确的维基百科（Wikipedia）页面；反过来，实体链接也有助于改进共指消解。考虑 Hajishirzi 等人（2013）给出的这个例子：

> Coreference can help entity linking by giving more possible surface forms to help link to the right Wikipedia page, and conversely entity linking can help improve coreference resolution. Consider this example from Hajishirzi et al. (2013):

(24.81) [Michael Eisner]1 和 [Donald Tsang]2 宣布了……的盛大开业

> (24.81) [Michael Eisner]1 and [Donald Tsang]2 announced the grand opening of
[[香港]3 迪士尼乐园]4 于昨天。[Eisner]1 感谢了 [总统]2，并欢迎 [粉丝]5 来到 [乐园]4。

> [[Hong Kong]3 Disneyland]4 yesterday. [Eisner]1 thanked [the President]2 and welcomed [fans]5 to [the park]4.

把实体链接整合进共指消解，有助于引入百科知识（例如 Donald Tsang 是总统这一事实），从而帮助消解提及 the President 的歧义。Ponzetto 和 Strube（2006）2007 以及 Ratinov 和 Roth（2012）表明，从维基百科页面中抽取的这类属性可用于构建更丰富的共指中实体提及模型。更晚近的研究展示了如何联合进行链接与共指消解（Hajishirzi et al. 2013, Zheng et al. 2013），甚至还能同时与命名实体标注联合进行（Durrett and Klein 2014）。

> Integrating entity linking into coreference can help draw encyclopedic knowledge (like the fact that Donald Tsang is a president) to help disambiguate the mention the President. Ponzetto and Strube (2006) 2007 and Ratinov and Roth (2012) showed that such attributes extracted from Wikipedia pages could be used to build richer models of entity mentions in coreference. More recent research shows how to do linking and coreference jointly (Hajishirzi et al. 2013, Zheng et al. 2013) or even jointly with named entity tagging as well (Durrett and Klein 2014).

我们前面介绍的共指任务包含一个简化假设，即

> The coreference task as we introduced it involves a simplifying assumption that
回指语与其先行语之间的关系是一种同一关系：两个共指的提及指称同一个话语所指对象。在真实文本中，这种关系可能更为复杂，话语所指对象的不同侧面可能被中和或重新聚焦。例如，(24.82)（Recasens et al., 2011）给出了一个转喻的例子，其中首都城市华盛顿被用作转喻

> the relationship between an anaphor and its antecedent is one of identity: the two coreferring mentions refer to the identical discourse referent. In real texts, the relationship can be more complex, where different aspects of a discourse referent can be neutralized or refocused. For example (24.82) (Recasens et al., 2011) shows an example of metonymy, in which the capital city Washington is used metonymically

> `metonymy`（转喻）
>
> 释义：用与某实体密切相关的另一事物来指代该实体，如以首都城市华盛顿指代美国政府。

来指称美国。(24.83-24.84) 展示了其他例子（Recasens et al., 2011）：

> to refer to the US. (24.83-24.84) show other examples (Recasens et al., 2011):

(24.82) 对某项政策的严格解释要求美国把某些政变阴谋通知外国

> (24.82) a strict interpretation of a policy requires The U.S. to notify foreign
独裁者……华盛顿拒绝了这项提议……

> dictators of certain coup plots ... Washington rejected the bid ...

(24.83) 有一次我在 Nowruz，也就是波斯新年的那天，越过那道边境进入 Ashgh-Abad。

> (24.83) I once crossed that border into Ashgh-Abad on Nowruz, the Persian New

在南部，人人都在庆祝新年；而在北部，那只是一个平常的日子。

> Year. In the South, everyone was celebrating New Year; to the North, it was a regular day.

(24.84) 在法国，总统经选举产生的任期是七年，而在

> (24.84) In France, the president is elected for a term of seven years, while in the
美国，他经选举产生的任期是四年。

> United States he is elected for a term of four years.

关于共指这些复杂问题的进一步语言学讨论，参见 Pustejovsky（1991）、van Deemter 和 Kibble（2000）、Poesio 等人（2006）、Fauconnier 和 Turner（2008）、Versley（2008）以及 Barker（2010）。

> For further linguistic discussions of these complications of coreference see Pustejovsky (1991), van Deemter and Kibble (2000), Poesio et al. (2006), Fauconnier and Turner (2008), Versley (2008), and Barker (2010).

Ng（2017）对共指消解中的机器学习模型给出了简明而有用的历史梳理。关于回指/共指消解，有三部出色的专著篇幅的综述，各自覆盖不同的时期：Hirst（1981）（截至约 1981 年的早期工作）、Mitkov（2002）（1986—2001）以及 Poesio 等人（2016）（2001—2015）。

> Ng (2017) offers a useful compact history of machine learning models in coreference resolution. There are three excellent book-length surveys of anaphora/coreference resolution, covering different time periods: Hirst (1981) (early work until about 1981), Mitkov (2002) (1986-2001), and Poesio et al. (2016) (2001-2015).

Andy Kehler 为本书 2000 年的第一版撰写了话语一章，我们以该章为起点撰写了第二版中相应的一章，而在这一第三版的共指章节中，仍保留着 Andy 优美文字的一些痕迹。

> Andy Kehler wrote the Discourse chapter for the 2000 first edition of this textbook, which we used as the starting point for the second-edition chapter, and there are some remnants of Andy’s lovely prose still in this third-edition coreference chapter.

## 练习

> Exercises
