# 第 13 章 机器翻译

### 章

> CHAPTER

# 13 机器翻译

> 13 Machine Translation

“我想说你们族人的方言。除非人们能听懂你说的话，否则说了也没有用。”

> “I want to talk the dialect of your people. It’s no use of talking unless people understand what you say.”

> Zora Neale Hurston, Moses, Man of the Mountain, 1939, 第 121 页
>
> *Zora Neale Hurston, Moses, Man of the Mountain 1939, p. 121*

> `machine`（机器）
>
> 释义：本书中指用计算机自动完成语言间转换的一类系统，与人工翻译相对。

本章介绍机器翻译（MT），即使用计算机从一种语言翻译成另一种语言。

> This chapter introduces machine translation (MT), the use of computers to translate from one language to another.

> `translation MT`（翻译 MT）
>
> 释义：指用计算机把一种语言的文本自动转换为另一种语言的缩写形式，是本章的核心研究对象。

当然，就其完整意义而言的翻译，例如文学翻译，或

> Of course translation, in its full generality, such as the translation of literature, or
诗歌翻译，是一项困难、迷人且极具人性的事业，其丰富程度不亚于人类创造力的任何其他领域。

> poetry, is a difficult, fascinating, and intensely human endeavor, as rich as any other area of human creativity.

因此，当前形态的机器翻译聚焦于若干非常

> Machine translation in its present form therefore focuses on a number of very
实用的任务。也许当前机器翻译最常见的用途是

> practical tasks. Perhaps the most common current use of machine translation is

> `information access`（信息获取）
>
> 释义：指用户为读取外文网页或资料而借助翻译取得所需信息，而非产出可供发表的正式译文。

用于信息获取。我们可能想翻译网页上的某些说明，

> for information access. We might want to translate some instructions on the web,
也许是某道喜爱菜肴的菜谱，或者是把某件家具组装起来的步骤。

> perhaps the recipe for a favorite dish, or the steps for putting together some furniture.

或者我们可能想读报纸上的一篇文章，或从维基百科（Wikipedia）这类在线资源、或用其他语言写成的政府网页中获取信息。

> Or we might want to read an article in a newspaper, or get information from an online resource like Wikipedia or a government webpage in some other language.

用于信息获取的机器翻译很可能是自然语言处理（NLP）技术最常见的用途之一，仅谷歌翻译（Google Translate）（见上图）每天就在 100 多种语言之间翻译数千亿个词。因此，机器翻译的改进有助于缩小信息获取中常被称作数字鸿沟的现象：即大量

> MT for information access is probably one of the most common uses of NLP technology, and Google Translate alone (shown above) translates hundreds of billions of words a day between over 100 languages. Improvements in machine translation can thus help reduce what is often called the digital divide in information access: the fact that much

![](images/13-machine-translation/img_24.png)

> `digital divide`（数字鸿沟）
>
> 释义：指不同语言或地区之间在可获取信息量上的悬殊差距，英语等高资源语言占据明显优势。

信息以英语以及富裕国家使用的其他语言提供。用英语进行网络搜索所返回的信息远多于用其他语言搜索，维基百科这类在线资源在英语及其他高资源语言中也大得多。高质量的翻译有助于把信息提供给低资源语言的使用者。

> more information is available in English and other languages spoken in wealthy countries. Web searches in English return much more information than searches in other languages, and online resources like Wikipedia are much larger in English and other higher-resourced languages. High-quality translation can help provide information to speakers of lower-resourced languages.

机器翻译的另一种常见用途是辅助人工译员。机器翻译系统通常被用来产出一份草稿译文，随后在译后编辑

> Another common use of machine translation is to aid human translators. MT systems are routinely used to produce a draft translation that is fixed up in a post-editing

> `post-editing`（译后编辑）
>
> 释义：指人工译员在机器生成的初稿上修改润色，是计算机辅助翻译流程中的关键环节。

阶段由人工译员加以修正。这项任务常被称为计算机辅助翻译，即 CAT。CAT 常作为本地化工作的一部分来使用：本地化即把内容

> phase by a human translator. This task is often called computer-aided translation or CAT. CAT is commonly used as part of localization: the task of adapting content

> `CAT`（CAT（计算机辅助翻译））
>
> 释义：指人工译员借助翻译记忆库、术语库与机器译文等工具完成翻译的工作方式，有别于全自动翻译。

或产品适配到某一特定语言社群的任务。

> or a product to a particular language community.

> `localization`（本地化）
>
> 释义：指把内容或产品加以调整，以适配某一特定语言与地区用户的文化、格式和使用习惯。

最后，机器翻译一项较新的应用是满足即时的交流需求。这包括增量翻译，即在整句说完之前就实时翻译语音，如同同声传译中常用的那样。以图像为中心的翻译可用于例如把手机拍摄图像上的文字经 OCR 识别后作为机器翻译系统的输入，以翻译菜单或路牌。

> Finally, a more recent application of MT is to in-the-moment human communication needs. This includes incremental translation, translating speech on-the-fly before the entire sentence is complete, as is commonly used in simultaneous interpretation. Image-centric translation can be used for example to use OCR of the text on a phone camera image as input to an MT system to translate menus or street signs.

> `encoder-`（编码器-）
>
> 释义：指序列到序列架构中把源语言句子压缩为向量表示的那一部分，与下一项合为完整模型。

机器翻译的标准算法是编码器-解码器模型。我们在第 9 章简要提到，编码器-解码器模型或称序列到序列模型，用于需要把一个输入序列映射为一个输出序列的任务，而该输出序列是整个输入序列的复杂函数，例如机器翻译或语音

> The standard algorithm for MT is the encoder-decoder model. We briefly mentioned in Chapter 9 that encoder-decoder or sequence-to-sequence models are used for tasks in which we need to map an input sequence to an output sequence that is a complex function of the entire input sequence, like machine translation or speech

> `decoder`（解码器）
>
> 释义：指依据编码结果逐词生成目标语言句子的网络部件，生成时以自回归方式依次输出词元。

识别。的确，在机器翻译中，目标语言的词在数量或顺序上未必与源语言的词一一对应。请考虑把下面这个自造的英语句子翻译成日语。

> recognition. Indeed, in machine translation, the words of the target language don’t necessarily agree with the words of the source language in number or order. Consider translating the following made-up English sentence into Japanese.

(13.1) 英语：He wrote a letter to a friend

> (13.1) English: He wrote a letter to a friend
日语：tomodachi ni tegami-o kaita

> Japanese: tomodachi ni tegami-o kaita
朋友 向 信 写

> friend to letter wrote
请注意，这些句子的成分在不同语言中所在的位置差别很大。在英语中，动词位于句子中间，而在日语中，动词 kaita 出现在句末。日语句子不需要代词 he，而英语需要。

> Note that the elements of the sentences are in very different places in the different languages. In English, the verb is in the middle of the sentence, while in Japanese, the verb kaita comes at the end. The Japanese sentence doesn’t require the pronoun he, while English does.

语言之间的这类差异可能相当复杂。在下面这个来自联合国的真实句子中，请注意汉语句子（我们已用红色标出这些汉字的逐词英文释义）与人工译员产出的英文对应句之间的诸多变化。(13.2) 大会/General Assembly 在/on 1982年/1982 12月/December 10日/10 通过

> Such differences between languages can be quite complex. In the following actual sentence from the United Nations, notice the many changes between the Chinese sentence (we’ve given in red a word-by-word gloss of the Chinese characters) and its English equivalent produced by human translators.(13.2) 大会/General Assembly 在/on 1982年/1982 12月/December 10日/10 通过
了/adopted 第37号/37th 决议/resolution ，核准了/approved 第二次/second 探索/exploration 及/and 和平peaceful 利用/using 外层空间/outer space 会议/conference 的/of 各项/various 建议/suggestions 。

1982 年 12 月 10 日，联合国大会通过了第 37 号决议，其中核可了第二次联合国探索及和平利用外层空间会议的各项建议。

> On 10 December 1982 , the General Assembly adopted resolution 37 in which it endorsed the recommendations of the Second United Nations Conference on the Exploration and Peaceful Uses of Outer Space .

请注意英语和汉语在诸多方面的差异。例如语序有重大差异；汉语中该名词短语的顺序是“和平利用外层空间会议的各项建议”，而英语是“suggestions of the ... conference on peaceful use of outer space”）。此外语序还有若干细微差异（日期的排列顺序不同）。英语在许多地方需要 the，而汉语不需要，并且还添加了一些汉语中不必需的细节（如“in which”和“it”）。汉语在语法上不标记名词的复数（不像英语，“recommendations”中带有“-s”），因此汉语必须用修饰语 各项/various 来表明建议不止一项。英语中有些词大写而另一些不大写。编码器-解码器网络非常擅长处理这类复杂的序列映射情况。

> Note the many ways the English and Chinese differ. For example the ordering differs in major ways; the Chinese order of the noun phrase is “peaceful using outer space conference of suggestions” while the English has “suggestions of the ... conference on peaceful use of outer space”). And the order differs in minor ways(the date is ordered differently). English requires the in many places that Chinese doesn’t, and adds some details (like “in which” and “it”) that aren’t necessary in Chinese. Chinese doesn’t grammatically mark plurality on nouns (unlike English, which has the “-s” in “recommendations”), and so the Chinese must use the modifier 各项/various to make it clear that there is not just one recommendation. English capitalizes some words but not others. Encoder-decoder networks are very successful at handling these sorts of complicated cases of sequence mappings.

下一节我们将先考察语言学背景，涉及语言

> We’ll begin in the next section by considering the linguistic background about
如何变化，以及这种变异对机器翻译任务的影响。然后我们会勾勒出标准算法，给出输入分词、构建平行句对训练语料库等方面的细节，再给出编码器-解码器网络的一些更底层的细节，最后讨论机器翻译如何评估，并介绍简单的 chrF 指标。

> how languages vary, and the implications this variance has for the task of MT. Then we’ll sketch out the standard algorithm, give details about things like input tokenization and creating training corpora of parallel sentences, give some more low-level details about the encoder-decoder network, and finally discuss how MT is evaluated, introducing the simple chrF metric.

## 13.1 语言差异与类型学

> 13.1 Language Divergences and Typology

世界上大约有 7,000 种语言。人类语言的某些方面似乎是普遍的，对其中每一种语言都成立，或者是统计意义上的

> There are about 7,000 languages in the world. Some aspects of human language seem to be universal, holding true for every one of these languages, or are statistical

> `universal`（语言共性）
>
> 释义：对世界上每一种语言都成立的语言性质或结构特征；只在多数语言中成立的则称为统计共性。

共性，即对其中大多数语言都成立。许多共性源于语言作为人类交流系统的功能角色。例如，每一种语言似乎都有用来指称人、谈论吃喝、表示礼貌或不礼貌的词语。也存在结构上的语言共性；例如，每一种语言似乎都有名词和动词（第 18 章），都有提问或发出命令的方式，都有表示同意或不同意的语言机制。

> universals, holding true for most of these languages. Many universals arise from the functional role of language as a communicative system by humans. Every language, for example, seems to have words for referring to people, for talking about eating and drinking, for being polite or not. There are also structural linguistic universals; for example, every language seems to have nouns and verbs (Chapter 18), has ways to ask questions, or issue commands, has linguistic mechanisms for indicating agreement or disagreement.

然而，语言在许多方面也存在差异（正如自古以来

> Yet languages also differ in many ways (as has been pointed out since ancient

> `translation divergence`（翻译差异）
>
> 释义：不同语言在词汇划分、语序等系统层面上的差别，会迫使翻译做出结构或词汇上的调整。

就有人指出的那样；见图 13.1）。理解造成这类翻译差异的原因

> times; see Fig. 13.1). Understanding what causes such translation divergences
（Dorr，1994）有助于我们构建更好的机器翻译模型。我们常常把必须逐一处理的特异差异和词汇差异（“狗”这个词在不同语言中差别极大），与能够以一般方式建模的系统性差异（许多语言把动词放在语法宾语之前；另一些语言把动词放在语法宾语之后）区分开来。对这类系统性的跨语言相似与差异的研究称为语言类型学。本节概述一些影响机器翻译的类型学事实；有兴趣的读者还应查阅 WALS，即《世界语言结构地图集》，其中给出了大量关于语言的类型学事实（Dryer and Haspelmath，2013）。

> (Dorr, 1994) can help us build better MT models. We often distinguish the idiosyncratic and lexical differences that must be dealt with one by one (the word for “dog”differs wildly from language to language), from systematic differences that we can model in a general way (many languages put the verb before the grammatical object; others put the verb after the grammatical object). The study of these systematic cross-linguistic similarities and differences is called linguistic typology. This section sketches some typological facts that impact machine translation; the interested reader should also look into WALS, the World Atlas of Language Structures, which gives many typological facts about languages (Dryer and Haspelmath, 2013).

> `typology`（类型学）
>
> 释义：按语言的结构特征对语言进行归类和比较的研究，可刻画跨语言系统性的相似与差异。

![](images/13-machine-translation/fig_p3_0.png)

*图 13.1 《巴别塔》，Pieter Bruegel，1563 年。Wikimedia Commons，藏于维也纳艺术史博物馆。*
*Figure 13.1 The Tower of Babel, Pieter Bruegel 1563. Wikimedia Commons, from the Kunsthistorisches Museum, Vienna.*

### 13.1.1 语序类型学

> 13.1.1 Word Order Typology

正如我们在上文比较英语和日语的例子中所提示的，各种语言在简单陈述从句中动词、主语和宾语的基本语序上存在差异。例如，德语、法语、英语和汉语普通话都属于 SVO

> As we hinted at in our example above comparing English and Japanese, languages differ in the basic word order of verbs, subjects, and objects in simple declarative clauses. German, French, English, and Mandarin, for example, are all SVO

> `SVO`（主-动-宾）
>
> 释义：主语先于动词、动词先于宾语的基本语序类型，动词倾向于位于主语与宾语之间。

（主-动-宾）语言，意思是动词倾向于出现在主语和宾语之间。相比之下，印地语和日语是 SOV 语言，意思是动词倾向于出现在基本从句的末尾，而爱尔兰语和阿拉伯语是 VSO 语言。基本语序类型相同的两种语言往往还具有

> (Subject-Verb-Object) languages, meaning that the verb tends to come between the subject and object. Hindi and Japanese, by contrast, are SOV languages, meaning that the verb tends to come at the end of basic clauses, and Irish and Arabic are VSO languages. Two languages that share their basic word order type often have

> `SOV`（主-宾-动）
>
> 释义：宾语先于动词的基本语序类型，动词通常出现在基本从句的末尾。

> `VSO`（动-主-宾）
>
> 释义：动词位于最前的基本语序类型，其后依次为主语和宾语。

其他相似之处。例如，VO 语言一般使用前置词，而 OV 语言一般使用后置词。

> other similarities. For example, VO languages generally have prepositions, whereas OV languages generally have postpositions.

让我们更仔细地看一看上文所见的例子。在这个 SVO 的英语

> Let’s look in more detail at the example we saw above. In this SVO English
句子中，动词 wrote 后面跟着它的宾语 a letter 和介词短语 to a friend，其中介词 to 后面跟着它的论元 a friend。阿拉伯语采用 VSO 语序，同样把动词放在宾语和介词之前。相比之下，在下面这个日语例子中，这些顺序都被颠倒过来；动词前面是它的论元，而后置词跟在它的论元之后。

> sentence, the verb wrote is followed by its object a letter and the prepositional phrase to a friend, in which the preposition to is followed by its argument a friend. Arabic, with a VSO order, also has the verb before the object and prepositions. By contrast, in the Japanese example that follows, each of these orderings is reversed; the verb is preceded by its arguments, and the postposition follows its argument.

（13.3）英语：He wrote a letter to a friend

> (13.3) English: He wrote a letter to a friend
日语：tomodachi ni tegami-o kaita

> Japanese: tomodachi ni tegami-o kaita
friend to letter wrote
阿拉伯语：katabt ris¯ala li ˙sadq

> Arabic: katabt ris¯ala li ˙sadq
wrote letter to friend
其他种类的排序偏好因语言不同而随机变化。在一些 SVO 语言中（如英语和汉语普通话），形容词倾向于出现在名词之前，而在另一些语言如西班牙语和现代希伯来语中，形容词出现在名词之后：

> Other kinds of ordering preferences vary idiosyncratically from language to language. In some SVO languages (like English and Mandarin) adjectives tend to appear before nouns, while in others languages like Spanish and Modern Hebrew, adjectives appear after the noun:

（13.4）西班牙语 bruja verde 英语 green witch

> (13.4) Spanish bruja verde English green witch

![](images/13-machine-translation/fig_p4_0.png)

*图 13.2 其他语序差异的例子：（a）在德语中，英语里更自然地靠后出现的副词会出现在句首位置，而有时态的动词出现在第二位。（b）在汉语普通话中，表示目标的介词短语常常出现在动词之前，这与英语不同。*
*Figure 13.2 Examples of other word order differences: (a) In German, adverbs occur in initial position that in English are more natural later, and tensed verbs occur in second position. (b) In Mandarin, preposition phrases expressing goals often occur pre-verbally, unlike in English.*

图 13.2 给出了其他语序差异的例子。所有这些语

> Fig. 13.2 shows examples of other word order differences. All of these word
言之间的语序差异都会给翻译带来问题，要求系统在生成输出时进行大规模的结构重排。

> order differences between languages can cause problems for translation, requiring the system to do huge structural reorderings as it generates the output.

### 13.1.2 词汇差异

> 13.1.2 Lexical Divergences

当然，我们还需要把个别词语从一种语言翻译到另一种语言。对于任何翻译而言，恰当的词语都会随语境而变化。

> Of course we also need to translate the individual words from one language to another. For any translation, the appropriate word can vary depending on the context.

例如，英语源语言词 bass 在西班牙语中可以是表示鱼的 lubina，也可以是表示乐器的 bajo。对于英语中称为 wall 的东西，德语使用两个不同的词：建筑物内部的墙用 Wand，建筑物外部的墙用 Mauer。英语用 brother 表示任何男性同胞，而汉语和许多其他语言对哥哥和弟弟使用不同的词（汉语普通话分别为 gege 和 didi）。在所有这些情况下，把英语的 bass、wall 或 brother 翻译过去都需要某种专门化处理，即消除一个词不同用法的歧义。因此，机器翻译与词义消歧（附录 I）这两个领域紧密相关。

> The English source-language word bass, for example, can appear in Spanish as the fish lubina or the musical instrument bajo. German uses two distinct words for what in English would be called a wall: Wand for walls inside a building, and Mauer for walls outside a building. Where English uses the word brother for any male sibling, Chinese and many other languages have distinct words for older brother and younger brother (Mandarin gege and didi, respectively). In all these cases, translating bass, wall, or brother from English would require a kind of specialization, disambiguating the different uses of a word. For this reason the fields of MT and Word Sense Disambiguation (Appendix I) are closely linked.

有时，一种语言对词语选择施加的语法约束会多于

> Sometimes one language places more grammatical constraints on word choice
另一种语言。我们上文看到，英语会对名词标记单数还是复数。汉语普通话则不会。又如法语和西班牙语，会在形容词上标记语法性别，因此从英语译成法语时需要明确指出形容词的性别。

> than another. We saw above that English marks nouns for whether they are singular or plural. Mandarin doesn’t. Or French and Spanish, for example, mark grammatical gender on adjectives, so an English translation into French requires specifying adjective gender.

各种语言在词汇上划分概念空间的方式可能

> The way that languages differ in lexically dividing up conceptual space may be
比这种一对多的翻译问题更为复杂，从而导致多对多的映射。例如，图 13.3 概括了 Hutchins 和 Somers（1992）在把英语的 leg、foot 和 paw 翻译成法语时所讨论的一些复杂情况。

> more complex than this one-to-many translation problem, leading to many-to-many mappings. For example, Fig. 13.3 summarizes some of the complexities discussed by Hutchins and Somers (1992) in translating English leg, foot, and paw, to French.

例如，当 leg 用于指动物时，译成法语的 patte；但用于指一段旅程时，译成法语的 etape；如果 leg 指椅子腿，则用法语的 pied。

> For example, when leg is used about an animal it’s translated as French patte; but about the leg of a journey, as French etape; if the leg is of a chair, we use French pied.

此外，一种语言可能存在词汇空缺，即没有任何词或短语，若不借助

> Further, one language may have a lexical gap, where no word or phrase, short

> `lexical gap`（词汇空缺）
>
> 释义：一种语言中缺少能与另一种语言的某个词精确对应的词或短语，只能迂回表达。

解释性脚注，能够表达另一种语言中某个词的确切含义。例如，英语没有与汉语普通话的 xi`ao 或日语的 oyak¯ok¯o 完全对应的词（在英语中只能用一些别扭的说法来将就，如 filial piety 或 loving child，或者对两者都用 good son/daughter）。

> of an explanatory footnote, can express the exact meaning of a word in the other language. For example, English does not have a word that corresponds neatly to Mandarin xi`ao or Japanese oyak¯ok¯o (in English one has to make do with awkward phrases like filial piety or loving child, or good son/daughter for both).

![](images/13-machine-translation/fig_p5_0.png)

*图 13.3 如 Hutchins 和 Somers（1992）所讨论的，英语 leg、foot 等与各种法语译法之间复杂的重叠关系。*
*Figure 13.3 The complex overlap between English leg, foot, etc., and various French translations as discussed by Hutchins and Somers (1992).*

最后，各语言在将一个事件的概念属性

> Finally, languages differ systematically in how the conceptual properties of an
映射到具体词语上的方式上存在系统性差异。Talmy（1985，1991）指出，语言可以按其运动方向和运动方式是标示在动词上还是标示在“卫星成分”（satellites）上来刻画：卫星成分即小品词、介词短语或副词短语。例如，一个瓶子漂浮着离开洞穴，用英语描述时方向标示在小品词 out 上，而用西班牙语时方向则标示在动词上：

> event are mapped onto specific words. Talmy (1985, 1991) noted that languages can be characterized by whether direction of motion and manner of motion are marked on the verb or on the “satellites”: particles, prepositional phrases, or adverbial phrases. For example, a bottle floating out of a cave would be described in English with the direction marked on the particle out, while in Spanish the direction would be marked on the verb:

(13.5) 英语：The bottle floated out.

> (13.5) English: The bottle floated out.

西班牙语：La botella sali´o flotando.

> Spanish: La botella sali´o flotando.

The bottle exited floating.

动词框架型语言把运动方向标示在动词上（而让

> Verb-framed languages mark the direction of motion on the verb (leaving the

> `verb-framed`（动词框架型）
>
> 释义：指把运动方向编码在主要动词上、由其他成分承担运动方式的语言类型，如西班牙语。

卫星成分来标示运动方式），如西班牙语的 acercarse“接近”、alcanzar“到达”、entrar“进入”、salir“离开”。卫星框架型语言把

> satellites to mark the manner of motion), like Spanish acercarse ‘approach’, alcanzar ‘reach’, entrar ‘enter’, salir ‘exit’. Satellite-framed languages mark the

> `satellite-framed`（卫星框架型）
>
> 释义：指把运动方向编码在小品词等从属成分上、由动词承担运动方式的语言类型，如英语。

运动方向标示在卫星成分上（而让动词去标示运动方式），如英语的 crawl out、float off、jump down、run after。日语、泰米尔语，以及罗曼语族、闪米特语族、玛雅语系中的许多语言，都属于动词框架型；汉语以及英语、瑞典语、俄语、印地语、波斯语等非罗曼语族的印欧语言，则属于卫星框架型（Talmy 1991，Slobin 1996）。

> direction of motion on the satellite (leaving the verb to mark the manner of motion), like English crawl out, float off, jump down, run after. Languages like Japanese, Tamil, and the many languages in the Romance, Semitic, and Mayan languages families, are verb-framed; Chinese as well as non-Romance Indo-European languages like English, Swedish, Russian, Hindi, and Farsi are satellite framed (Talmy 1991, Slobin 1996).

### 13.1.3 指称密度

> 13.1.3 Referential density

最后，各语言还会在一个与它们倾向于省略什么有关的类型学维度上有所不同。像英语这样的语言，在谈论语篇中已经给出的指称对象时，要求我们使用显式代词。然而在其他语言中，我们有时可以完全省略代词，如下面的西班牙语例子所示1：

> Finally, languages vary along a typological dimension related to the things they tend to omit. Some languages, like English, require that we use an explicit pronoun when talking about a referent that is given in the discourse. In other languages, however, we can sometimes omit pronouns altogether, as the following example from Spanish shows1:

(13.6) [El jefe]i dio con un libro. /0i Mostr´o su hallazgo a un descifrador ambulante.

[The boss] came upon a book. [He] showed his find to a wandering decoder.

能够省略代词的语言称为代词脱落语言。即便在

> Languages that can omit pronouns are called pro-drop languages. Even among

> `pro-drop`（代词脱落）
>
> 释义：指允许在句中省略代词性主语、其指称需由语境恢复的语言特征。

这些代词脱落语言当中，省略出现的频率也存在显著差异。

> the pro-drop languages, there are marked differences in frequencies of omission.

例如，日语和汉语的省略倾向要远强于西班牙语。语言之间的这一变异维度称为指称密度维度。我们说，倾向于使用更多代词的语言，其指称密度要比

> Japanese and Chinese, for example, tend to omit far more than does Spanish. This dimension of variation across languages is called the dimension of referential density. We say that languages that tend to use more pronouns are more referentially

> `referential density`（指称密度）
>
> 释义：衡量语篇中代词等显式指称形式使用多少的维度，使用越多则越密集。

使用零形式更多的语言更高。像汉语或日语这类指称稀疏、要求听者付出更多推理才能恢复先行语的语言，也被称为冷语言。而那些更为显式、使听者

> dense than those that use more zeros. Referentially sparse languages, like Chinese or Japanese, that require the hearer to do more inferential work to recover antecedents are also called cold languages. Languages that are more explicit and make it easier

> `cold language hot language`（冷语言；热语言）
>
> 释义：借自麦克卢汉对媒体的划分，指需听者靠推理补足所指的语言与表述更为显式的语言。

更容易理解的语言则被称为热语言。hot 与 cold 这两个术语借自

> for the hearer are called hot languages. The terms hot and cold are borrowed from
马歇尔·麦克卢汉（Marshall McLuhan）1964 年提出的区分：像电影这样的热媒体为观看者补足了许多细节，而像漫画这样的冷媒体则要求读者做更多推理工作来补全表征（Bickel，2003）。

> Marshall McLuhan’s 1964 distinction between hot media like movies, which fill in many details for the viewer, versus cold media like comics, which require the reader to do more inferential work to fill out the representation (Bickel, 2003).

从汉语或日语这类代词脱落现象广泛的语言翻译到

> Translating from languages with extensive pro-drop, like Chinese or Japanese, to
英语这类非代词脱落语言可能很困难，因为模型必须以某种方式识别出每个零形式，并恢复出所谈论的是谁或是什么，才能插入恰当的代词。

> non-pro-drop languages like English can be difficult since the model must somehow identify each zero and recover who or what is being talked about in order to insert the proper pronoun.

## 13.2 使用编码器-解码器的机器翻译

> 13.2 Machine Translation using Encoder-Decoder

机器翻译的标准架构是编码器-解码器 Transformer，即序列到序列模型。关于如何把这一架构应用到 Transformer 上的细节，我们将在 13.3 节中介绍，但首先来讨论整体任务。

> The standard architecture for MT is the encoder-decoder transformer or sequenceto-sequence model. We’ll see the details of how to apply this architecture to transformers in Section 13.3, but first let’s talk about the overall task.

大多数机器翻译任务都作了这样的简化：我们可以独立地翻译每个

> Most machine translation tasks make the simplification that we can translate each
句子，因此眼下我们只考虑单个句子。给定源语言中的一个句子，机器翻译的任务就是生成目标语言中与之对应的句子。例如，给机器翻译系统一个这样的英语句子：

> sentence independently, so we’ll just consider individual sentences for now. Given a sentence in a source language, the MT task is then to generate a corresponding sentence in a target language. For example, an MT system is given an English sentence like

The green witch arrived
并须把它翻译成西班牙语句子：

> and must translate it into the Spanish sentence:

Lleg´o la bruja verde
机器翻译使用监督式机器学习：在训练时，系统会得到

> MT uses supervised machine learning: at training time the system is given a
大量平行句对（源语言中的每个句子都与目标语言中的一个句子相配），并学会把源语言句子映射为目标语言句子。在实践中，我们并不是像上面的例子那样以词为单位，而是把句子切分成子词词元序列（词元可以是词、子词或单个字符）。然后训练系统，使其在给定源语言词元序列 x1,...,xn 的条件下，最大化目标语言词元序列 y1,...,ym 的概率：

> large set of parallel sentences (each sentence in a source language matched with a sentence in the target language), and learns to map source sentences into target sentences. In practice, rather than using words (as in the example above), we split the sentences into a sequence of subword tokens (tokens can be words, or subwords, or individual characters). The systems are then trained to maximize the probability of the sequence of tokens in the target language y1,...,ym given the sequence of tokens in the source language x1,...,xn:

$$P ( y _{1} ,..., y _{m} | x _{1} ,..., x _{n} )$$

编码器-解码器架构并不直接使用输入词元，而是由两个组件构成：编码器和解码器。编码器接收输入词 x = [x1,...,xn]，产生一个中间上下文 h。在解码时，系统以 h 为输入，逐词生成输出 y：

> Rather than use the input tokens directly, the encoder-decoder architecture consists of two components, an encoder and a decoder. The encoder takes the input words x = [x1,...,xn] and produces an intermediate context h. At decoding time, the system takes h and, word by word, generates the output y:

h = encoder(x) yt+1 = decoder(h,y1,...,yt) ∀t ∈[1,...,m] 接下来的两节中，我们将讨论子词分词，然后讨论如何获得用于训练的平行语料库，之后我们将介绍编码器-解码器架构的细节。

> h = encoder(x) yt+1 = decoder(h,y1,...,yt) ∀t ∈[1,...,m] In the next two sections we’ll talk about subword tokenization, then how to get parallel corpora for training, and then we’ll introduce the details of the encoderdecoder architecture.

### 13.2.1 分词

> 13.2.1 Tokenization

机器翻译系统使用一个事先固定的词表，而且这个词表不是由按空格分隔的词构成的，而是用子词分词算法生成的，比如第 2 章简述的 BPE 算法。源语言和目标语言共用一个词表，这使得把词元（如人名）从源语言复制到目标语言变得容易。采用在不同语言之间共享词元的子词分词，使得在像英语或印地语这样用空格分隔词语的语言，与像汉语或泰语这样不用空格的语言之间进行翻译变得自然。

> Machine translation systems use a vocabulary that is fixed in advance, and rather than using space-separated words, this vocabulary is generated with subword tokenization algorithms, like the BPE algorithm sketched in Chapter 2. A shared vocabulary is used for the source and target languages, which makes it easy to copy tokens (like names) from source to target. Using subword tokenization with tokens shared between languages makes it natural to translate between languages like English or Hindi that use spaces to separate words, and languages like Chinese or Thai that don’t.

我们通过在同时包含源语言和目标语言数据的语料库上运行子词分词算法来构建词表。

> We build the vocabulary by running a subword tokenization algorithm on a corpus that contains both source and target language data.

现代系统往往不采用图 2.6 中那种简单的 BPE 算法，而是使用

> Rather than the simple BPE algorithm from Fig. 2.6, modern systems often use
更强大的分词算法。有些系统（如 BERT）使用一种称为 wordpiece 算法的 BPE 变体，它不是选择出现最频繁的

> more powerful tokenization algorithms. Some systems (like BERT) use a variant of BPE called the wordpiece algorithm, which instead of choosing the most frequent

> `wordpiece`（词片）
>
> 释义：BPE 的变体，以语言模型概率的增益为准选择合并，常在词首用特殊符号标记，BERT 采用这种子词切分方法。

词元集合，而是根据哪种合并最能提高该分词结果的语言模型概率来选择合并。词片在每个词元的开头使用一个特殊符号；下面是 Google 机器翻译系统（Wu et al., 2016）得到的一个分词结果：

> set of tokens to merge, chooses merges based on which one most increases the language model probability of the tokenization. Wordpieces use a special symbol at the beginning of each token; here’s a resulting tokenization from the Google MT system(Wu et al., 2016):

> 词：Jet makers feud over seat width with big orders at stake 词片：J et makers fe ud over seat width with big orders at stake
>
> *words: Jet makers feud over seat width with big orders at stake wordpieces: J et makers fe ud over seat width with big orders at stake*

wordpiece 算法会接收一个训练语料库和一个期望的词表大小

> The wordpiece algorithm is given a training corpus and a desired vocabulary size
V，并按如下步骤进行：

> V, and proceeds as follows:

- 用字符初始化 wordpiece 词表（例如取 Unicode 字符的一个子集，把所有剩余字符合并为一个特殊的未知字符词元）。
- 重复以下步骤，直到得到 V 个词片：

> Initialize the wordpiece lexicon with characters (for example a subset of Unicode characters, collapsing all the remaining characters to a special unknown character token).
> Repeat until there are V wordpieces:

（a）使用当前的

> (a) Train an n-gram language model on the training corpus, using the current
词片集合，在训练语料库上训练一个 n 元语言模型。

> set of wordpieces.

（b）考虑把两个

> (b) Consider the set of possible new wordpieces made by concatenating two
当前词表中的词片拼接起来所能构成的所有可能新词片，选择其中最能提高训练语料库语言模型概率的那个新词片。

> wordpieces from the current lexicon. Choose the one new wordpiece that most increases the language model probability of the training corpus.

回忆一下，使用 BPE 时我们必须指定要执行的合并次数；而在

> Recall that with BPE we had to specify the number of merges to perform; in
wordpiece 中则相反，我们指定词表总量，这是一个更直观的参数。常用的词表规模是 8K 到 32K 个词片。

> wordpiece, by contrast, we specify the total vocabulary, which is a more intuitive parameter. A vocabulary of 8K to 32K word pieces is commonly used.

还有一种使用更广的分词算法，被（多少有些含混地）称为 unigram 算法（Kudo, 2018），有时也被称为 SentencePiece

> An even more commonly used tokenization algorithm is (somewhat ambiguously) called the unigram algorithm (Kudo, 2018) or sometimes the SentencePiece

> `unigram`（一元分词算法）
>
> 释义：从庞大的初始词表出发，迭代地为词元估计概率并逐批删减词元，逐步缩减到目标规模的一种子词切分方法。

算法，并被 ALBERT（Lan et al., 2020）和 T5（Raffel et al., 2020）等系统采用。（因为一元算法是名为 SentencePiece 的库所使用的默认分词算法，该库为各种分词算法提供了一个有用的封装（Kudo 和 Richardson, 2018），所以作者们常说自己在使用 SentencePiece 分词，但实际意思是他们在用一元算法）。

> algorithm, and is used in systems like ALBERT (Lan et al., 2020) and T5 (Raffel et al., 2020). (Because unigram is the default tokenization algorithm used in a library called SentencePiece that adds a useful wrapper around tokenization algorithms (Kudo and Richardson, 2018), authors often say they are using SentencePiece tokenization but really mean they are using the unigram algorithm).

> `SentencePiece`
>
> 释义：一种开源的子词分词工具库，为多种分词算法提供统一封装，其默认算法是一元分词。

在一元分词中，我们不是通过合并词元来逐步建立词表，

> In unigram tokenization, instead of building up a vocabulary by merging tokens,
而是从一个巨大的词表开始，它包含每一个单独的 Unicode 字符以及所有频繁出现的字符序列（对于有空格的语言，包括所有以空格分隔的单词），然后迭代地删除一些词元，以达到期望的最终词表大小。该算法很复杂（涉及用于高效存储大量词元的后缀树，以及用于迭代地为词元分配概率的 EM 算法），因此这里不给出，可参见 Kudo (2018) 和 Kudo 与 Richardson (2018)。大致来说，该算法迭代进行：先估计每个词元的概率，用多种分词方式对输入数据分词，然后删掉一定比例的不出现在高概率分词结果中的词元，如此不断迭代，直到词表缩减到期望的词元数量。

> we start with a huge vocabulary of every individual unicode character plus all frequent sequences of characters (including all space-separated words, for languages with spaces), and iteratively remove some tokens to get to a desired final vocabulary size. The algorithm is complex (involving suffix-trees for efficiently storing many tokens, and the EM algorithm for iteratively assigning probabilities to tokens), so we don’t give it here, but see Kudo (2018) and Kudo and Richardson (2018). Roughly speaking the algorithm proceeds iteratively by estimating the probability of each token, tokenizing the input data using various tokenizations, then removing a percentage of tokens that don’t occur in high-probability tokenization, and then iterates until the vocabulary has been reduced down to the desired number of tokens.

为什么一元分词比 BPE 效果更好？BPE 倾向于产生大量

> Why does unigram tokenization work better than BPE? BPE tends to create lots
非常小的、没有意义的词元（因为 BPE 只能通过一次合并一个字符来造出更大的单词或语素），而且它还倾向于把非常常见的词元（如后缀 ed）合并到其相邻词元上。从 Bostrom 和 Durrett (2020) 给出的这些例子可以看出，一元分词倾向于产生语义上更有意义的词元：

> of very small non-meaningful tokens (because BPE can only create larger words or morphemes by merging characters one at a time), and it also tends to merge very common tokens, like the suffix ed, onto their neighbors. We can see from these examples from Bostrom and Durrett (2020) that unigram tends to produce tokens that are more semantically meaningful:

| 原文：<br>Original: | corrupted | 原文：<br>Original: | Completely preposterous suggestions |
| --- | --- | --- | --- |
| BPE：<br>BPE: | cor rupted | BPE：<br>BPE: | Comple t ely prep ost erous suggest ions |
| 一元分词：<br>Unigram: | corrupt ed | 一元分词：<br>Unigram: | Complete ly pre post er ous suggestion s |

一元分词：corrupt ed 一元分词：Complete ly pre post er ous suggestion s

> Unigram: corrupt ed Unigram: Complete ly pre post er ous suggestion s

### 13.2.2 创建训练数据

> 13.2.2 Creating the Training data

机器翻译模型在平行语料库上训练，这种语料库有时也称为

> Machine translation models are trained on a parallel corpus, sometimes called a

> `parallel corpus`（平行语料库）
>
> 释义：由两种或更多种语言互为译文的文本构成的语料库，是训练机器翻译模型的基础资源。

双语文本，即以两种（或更多种）语言呈现的文本。已有大量平行语料库可供使用。有些出自政府机构：Europarl 语料库（Koehn，

> bitext, a text that appears in two (or more) languages. Large numbers of parallel corpora are available. Some are governmental; the Europarl corpus (Koehn,

> `Europarl`（Europarl 语料库）
>
> 释义：由欧洲议会会议记录抽取而成的多语平行语料库，涵盖 21 种欧洲语言，常用于机器翻译的训练与评测。

2005），提取自欧洲议会会议记录，包含 21 种欧洲语言各 40 万到 200 万句。联合国平行语料库包含约 1000 万句联合国六种官方语言（阿拉伯语、汉语、英语、法语、俄语、西班牙语）的句子，Ziemski et al. (2016)。另一些平行语料库由电影和电视字幕构建，如 OpenSubtitles 语料库（Lison 和 Tiedemann, 2016），或者由一般网页文本构建，如从 CommonCrawl 中抽取的 ParaCrawl 语料库，其中包含 23 种欧盟语言与英语之间的 2.23 亿个句对，Ba˜n´on et al. (2020)。

> 2005), extracted from the proceedings of the European Parliament, contains between 400,000 and 2 million sentences each from 21 European languages. The United Nations Parallel Corpus contains on the order of 10 million sentences in the six official languages of the United Nations (Arabic, Chinese, English, French, Russian, Spanish) Ziemski et al. (2016). Other parallel corpora have been made from movie and TV subtitles, like the OpenSubtitles corpus (Lison and Tiedemann, 2016), or from general web text, like the ParaCrawl corpus of 223 million sentence pairs between 23 EU languages and English extracted from the CommonCrawl Ba˜n´on et al. (2020).

句对齐

> Sentence alignment
机器翻译的标准训练语料以对齐的句对形式提供。在创建新语料库时，例如针对资源匮乏的语言或新的领域，必须创建这些句对齐。图 13.4 给出了一个假设的句对齐示例。

> Standard training corpora for MT come as aligned pairs of sentences. When creating new corpora, for example for underresourced languages or new domains, these sentence alignments must be created. Fig. 13.4 gives a sample hypothetical sentence alignment.

给定两篇互为译文的文档，我们通常需要两个

> Given two documents that are translations of each other, we generally need two
步骤来生成句对齐：

> steps to produce sentence alignments:

- 一个代价函数，它接收一段源语言句子和一段目标语言句子，返回一个衡量这两段互为译文的可能性有多大的分数。
- 一个对齐算法，它利用这些分数在文档之间找到良好的对齐。

> a cost function that takes a span of source sentences and a span of target sentences and returns a score measuring how likely these spans are to be translations.
> an alignment algorithm that takes these scores to find a good alignment between the documents.

为了给跨语言的句子相似度打分，我们需要利用

> To score the similarity of sentences across languages, we need to make use of
一个多语言嵌入空间，其中来自不同语言的句子处于同一个嵌入空间（Artetxe 和 Schwenk, 2019）。给定这样一个空间，这类嵌入的余弦相似度就提供了一种自然的打分函数（Schwenk, 2018）。Thompson 和 Koehn (2019) 给出如下两个

> a multilingual embedding space, in which sentences from different languages are in the same embedding space (Artetxe and Schwenk, 2019). Given such a space, cosine similarity of such embeddings provides a natural scoring function (Schwenk, 2018). Thompson and Koehn (2019) give the following cost function between two

![](images/13-machine-translation/fig_p9_0.png)

*图 13.4 英语与法语句子之间的一个对齐示例，句子抽取自 Antoine de Saint-Exupery 的 Le Petit Prince 以及一个假设的译文。句对齐接收句子 e1,...,en 和 f1,..., fm，找出互为译文的最小句子集合，包括像 (e1,f1)、(e4,f3)、(e5,f4)、(e6,f6) 这样的单句映射，以及 2-1 对齐 (e2/e3,f2)、(e7/e8,f7) 和空对齐 (f5)。*
*Figure 13.4 A sample alignment between sentences in English and French, with sentences extracted from Antoine de Saint-Exupery’s Le Petit Prince and a hypothetical translation. Sentence alignment takes sentences e1,...,en, and f1,..., fm and finds minimal sets of sentences that are translations of each other, including single sentence mappings like (e1,f1), (e4,f3), (e5,f4), (e6,f6) as well as 2-1 alignments (e2/e3,f2), (e7/e8,f7), and null alignments (f5).*

分别来自源文档和目标文档的句子或片段 x、y：

> sentences or spans x,y from the source and target documents respectively:

$$( 1 - \text{cos} ( x , y )) \text{nSents} ( _{S} x ) \text{nSents} ( y )$$

c(x,y) = (13.10)
PS s=1 1−cos(x,ys)+PS s=1 1−cos(xs,y)
其中 nSents() 给出句子的数量（这使该指标偏向于将大量单句相互对齐，而不是对齐非常大的片段）。分母有助于对相似度进行归一化，而 x1,...,xS,y1,...,yS 则是从各自文档中随机抽取的句子。

> where nSents() gives the number of sentences (this biases the metric toward many alignments of single sentences instead of aligning very large spans). The denominator helps to normalize the similarities, and so x1,...,xS,y1,...,yS, are randomly selected sentences sampled from the respective documents.

通常使用动态规划作为对齐算法（Gale 和

> Usually dynamic programming is used as the alignment algorithm (Gale and
Church，1993），这是对我们在第 2 章介绍的最小编辑距离算法的一个简单扩展。

> Church, 1993), in a simple extension of the minimum edit distance algorithm we introduced in Chapter 2.

最后，通过移除有噪声的句对来做一些语料库清理是很有帮助的。

> Finally, it’s helpful to do some corpus cleanup by removing noisy sentence pairs.

这可以包括用手写规则移除低精度的句对（例如移除过长、过短、URL 不同的句子，甚至移除过于相似的句对，因为这意味着它们是复制而非翻译）。也可以按句对的多语言嵌入余弦得分对其进行排序，并丢弃得分低的句对。

> This can involve handwritten rules to remove low-precision pairs (for example removing sentences that are too long, too short, have different URLs, or even pairs that are too similar, suggesting that they were copies rather than translations). Or pairs can be ranked by their multilingual embedding cosine score and low-scoring pairs discarded.

## 13.3 编码器-解码器模型的细节

> 13.3 Details of the Encoder-Decoder Model

机器翻译的标准架构是编码器-解码器 transformer。图 13.5 在高层次上展示了该架构的直观思路。你会看到，编码器-解码器架构由两个 transformer 组成：一个是编码器，它与第 7 章中的基础 transformer 相同；另一个是解码器，它为架构增加了一个称为交叉注意力层的特殊新层。编码器接收源语言的输入词元 X = x1,...,xn，并通过一堆编码器块将它们映射为输出表示 Henc = h1,...,hn；

> The standard architecture for MT is the encoder-decoder transformer. Fig. 13.5 shows the intuition of the architecture at a high level. You’ll see that the encoderdecoder architecture is made up of two transformers: an encoder, which is the same as the basic transformers from Chapter 7, and a decoder, which is augmented with a special new layer called the cross-attention layer. The encoder takes the source language input word tokens X = x1,...,xn and maps them to an output representation Henc = h1,...,hn; via a stack of encoder blocks.

解码器本质上是一个条件语言模型，它关注编码器的表示并逐个生成目标词，在每个时间步以源句子和先前生成的目标语言词为条件来生成一个词元。解码可以使用所讨论的任何解码方法

> The decoder is essentially a conditional language model that attends to the encoder representation and generates the target words one by one, at each timestep conditioning on the source sentence and the previously generated target language words to generate a token. Decoding can use any of the decoding methods discussed

![](images/13-machine-translation/fig_p10_0.png)

*图 13.5 用于机器翻译的编码器-解码器 transformer 架构。编码器使用我们在第 7 章看到的 transformer 块，而解码器使用一个更强大的块，该块带有一个额外的交叉注意力层，可以关注编码器的所有词。我们将在下一节更详细地看到这一点。*
*Figure 13.5 The encoder-decoder transformer architecture for machine translation. The encoder uses the transformer blocks we saw in Chapter 7, while the decoder uses a more powerful block with an extra crossattention layer that can attend to all the encoder words. We’ll see this in more detail in the next section.*

第 7 章中的方法，如贪心、温度采样或核采样。但机器翻译中最常见的解码算法是我们将在 13.4 节介绍的束搜索算法。

> in Chapter 7 like greedy, or temperature or nucleus sampling. But the most common decoding algorithm for MT is the beam search algorithm that we’ll introduce in Section 13.4.

但该架构的各组成部分与我们所见的 transformer

> But the components of the architecture differ somewhat from the transformer
块略有不同。首先，为了关注源语言，解码器中的 transformer 块增加了一个额外的交叉注意力层。回想第 7 章的 transformer 块由一个自注意力层组成，它关注来自上一层的输入，其前面是层归一化，后面是另一个层归一化和前馈层。解码器的 transformer 块包含一个额外的层，该层使用一种特殊的注意力，即交叉注意力（有时也称为编码器-解码器

> block we’ve seen. First, in order to attend to the source language, the transformer blocks in the decoder have an extra cross-attention layer. Recall that the transformer block of Chapter 7 consists of a self-attention layer that attends to the input from the previous layer, preceded by layer norm, and followed by another layer norm and the feed forward layer. The decoder transformer block includes an extra layer with a special kind of attention, cross-attention (also sometimes called encoder-decoder

> `cross-attention`（交叉注意力）
>
> 释义：解码器中额外的一层注意力，其 query 来自解码器上一层，而 key 和 value 来自编码器的输出。

注意力或源注意力）。交叉注意力与普通 transformer 块中的多头注意力形式相同，区别在于：query 照常来自解码器的上一层，而 key 和 value 则来自编码器的输出。

> attention or source attention). Cross-attention has the same form as the multi-head attention in a normal transformer block, except that while the queries as usual come from the previous layer of the decoder, the keys and values come from the output of the encoder.

也就是说，在标准多头注意力中，每个注意力层的输入

> That is, where in standard multi-head attention the input to each attention layer
是 X，而在交叉注意力中，输入是编码器的最终输出 Henc = h1,...,hn。

> is X, in cross attention the input is the final output of the encoder Henc = h1,...,hn.

Henc 的形状为 [n × d]，每一行代表一个输入词元。为了将来自编码器的 key 和 value 与来自解码器上一层的 query 相连接，我们将编码器输出 Henc 乘以交叉注意力层的 key 权重 WK 和 value 权重 WV。query 来自上一层解码器层的输出 Hdec[ℓ−1]，它乘以交叉注意力层的 query 权重 WQ：

> Henc is of shape [n × d], each row representing one input token. To link the keys and values from the encoder with the query from the prior layer of the decoder, we multiply the encoder output Henc by the cross-attention layer’s key weights WK and value weights WV. The query comes from the output from the prior decoder layer Hdec[ℓ−1], which is multiplied by the cross-attention layer’s query weights WQ:

$$Q = H ^{\text{dec} [ ℓ - 1 ]} W ^{Q} ; K = H ^{\text{enc}} W ^{K} ; V = H ^{\text{enc}} W ^{V}$$

QK⊺  (13.12)
CrossAttention(Q,K,V) = softmax
√dk V
因此，交叉注意力使解码器能够关注源语言的每个词，这些词被投影到编码器的整个最终输出表示中。每个解码器块中的另一个注意力层，即多头注意力层，与我们在第 7 章看到的因果（从左到右）注意力相同。不过，编码器中的多头注意力被允许向前查看整个源语言文本，因此它没有被掩码。

> The cross attention thus allows the decoder to attend to each of the source language words as projected into the entire encoder final output representations. The other attention layer in each decoder block, the multi-head attention layer, is the same causal (left-to-right) attention that we saw in Chapter 7. The multi-head attention in the encoder, however, is allowed to look ahead at the entire source language text, so it is not masked.

要训练一个编码器-解码器模型，我们把源文本提供给网络，然后

> To train an encoder-decoder model, we give the network the source text, and then
从分隔符词元开始，以自回归的方式训练它预测下一个词元，并使用交叉熵损失。回想一下，语言建模的交叉熵损失为

> starting with the separator token train it autoregressively to predict the next token, using cross-entropy loss. Recall that cross-entropy loss for language modeling is

![](images/13-machine-translation/fig_p11_0.png)

*图 13.6 编码器和解码器的 transformer 块，展示了残差流视角。编码器的最终输出 Henc = h1,...,hn 是解码器所使用的上下文。解码器是标准的 transformer，只是多了一个额外的层，即交叉注意力层，它接收编码器输出 Henc 并用它来形成其 K 和 V 输入。*
*Figure 13.6 The transformer block for the encoder and the decoder, showing the residual stream view. The final output of the encoder Henc = h1,...,hn is the context used in the decoder. The decoder is a standard transformer except with one extra layer, the cross-attention layer, which takes that encoder output Henc and uses it to form its K and V inputs.*

由模型赋予正确的下一个词的概率决定。因此在时刻 t，CE 损失是模型赋予训练序列中下一个词的概率的负对数：

> determined by the probability the model assigns to the correct next word. So at time t the CE loss is the negative log probability the model assigns to the next word in the training sequence:

$$L _{\text{CE}} ( y ˆ _{t} , y _{t} ) = - \text{log ˆ} y _{t} [ w _{t + 1} ]$$

与那种情况一样，我们在解码器中使用教师强制。回想一下，在教师强制中，解码的每个时间步我们都强制系统使用训练中的标准答案目标词元作为下一个输入 xt+1，而不是让它依赖（可能有误的）解码器输出 ˆyt。

> As in that case, we use teacher forcing in the decoder. Recall that in teacher forcing, at each time step in decoding we force the system to use the gold target token from training as the next input xt+1, rather than allowing it to rely on the (possibly erroneous) decoder output ˆyt.

> `teacher forcing`（教师强制）
>
> 释义：训练解码器时，每个时间步都强制把训练数据中的正确目标词元作为下一输入，而非使用模型自己生成的输出。

## 13.4 机器翻译中的解码：束搜索

> 13.4 Decoding in MT: Beam Search

回想第 7 章中的贪心解码算法：在生成过程的每个时间步 t，输出 yt 的选定方式是计算词表中每个词的概率，然后选择概率最高的词（即 argmax）：

> Recall the greedy decoding algorithm from Chapter 7: at each time step t in generation, the output yt is chosen by computing the probability for each word in the vocabulary and then choosing the highest probability word (the argmax):

$$w ˆ _{t} = \text{argmax} _{w \in V} P ( w | w _{< t} )$$

贪心解码的一个问题是：在词 t 处看起来概率很高的选择，到了词 t +1 时可能被证明是错误的选择。束搜索算法会保留多个选择，直到稍后我们能够看出哪一个最好。

> A problem with greedy decoding is that what looks high probability at word t might turn out to have been the wrong choice once we get to word t +1. The beam search algorithm maintains multiple choices until later when we can see which one is best.

在束搜索中，我们把解码建模为在可能的生成结果空间中搜索，该空间表示为一棵搜索树，其分支表示动作（生成一个词元），节点表示状态（已经生成了某个特定的前缀）。我们搜索最佳的动作序列，即概率最高的字符串。

> In beam search we model decoding as searching the space of possible generations, represented as a search tree whose branches represent actions (generating a token), and nodes represent states (having generated a particular prefix). We search for the best action sequence, i.e., the string with the highest probability.

该问题的一个示例

> An illustration of the problem
图 13.7 展示了一个虚构的例子。概率最高的序列是 ok ok EOS（其概率为 .4× .7× 1.0）。但贪心搜索找不到它，而是错误地选择 yes 作为第一个词，因为它具有最高的局部概率（0.5）。

> Fig. 13.7 shows a made-up example. The most probable sequence is ok ok EOS (its probability is .4× .7× 1.0). But greedy search doesn’t find it, incorrectly choosing yes as the first word since it has the highest local probability (0.5).

![](images/13-machine-translation/fig_p12_0.png)

*图 13.7 从词表 V = {yes,ok,<s>} 生成目标字符串 T = t1,t2,... 的搜索树，展示了从该状态生成每个词元的概率。贪心搜索选择 yes 后跟 yes，而不是全局概率最高的序列 ok ok。*
*Figure 13.7 A search tree for generating the target string T = t1,t2,... from vocabulary V = {yes,ok,<s>}, showing the probability of generating each token from that state. Greedy search chooses yes followed by yes, instead of the globally most probable sequence ok ok.*

对于某些问题，例如词性标注或句法分析，正如我们将要在

> For some problems, like part-of-speech tagging or parsing as we will see in
在第 18 章或第 19 章中，我们可以使用动态规划搜索（Viterbi 算法）来解决这个问题。遗憾的是，动态规划并不适用于输出决策之间存在长距离依赖的生成问题。唯一能保证找到最优解的方法是穷举搜索：计算 V^T 个可能句子（对某个长度值 T）中每一个的概率，这显然太慢了。

> Chapter 18 or Chapter 19, we can use dynamic programming search (the Viterbi algorithm) to address this problem. Unfortunately, dynamic programming is not applicable to generation problems with long-distance dependencies between the output decisions. The only method guaranteed to find the best solution is exhaustive search: computing the probability of every one of theV T possible sentences (for some length value T) which is obviously too slow.

解决方案：束搜索

> The solution: beam search
相反，机器翻译系统通常使用束搜索进行解码，这是一种启发式搜索方法，

> Instead, MT systems generally decode using beam search, a heuristic search method

> `beam search`（束搜索）
>
> 释义：解码时每一步只保留概率最高的 k 个候选序列、其余剪枝，用有限的搜索宽度近似取代穷举搜索。

由 Lowerre（1976）首次提出。在束搜索中，我们并非在每个时间步只选择要生成的最佳词元，而是在每一步保留 k 个可能的词元。这个固定大小的内存占用 k 被称为束宽，取自手电筒光束的隐喻，

> first proposed by Lowerre (1976). In beam search, instead of choosing the best token to generate at each timestep, we keep k possible tokens at each step. This fixed-size memory footprint k is called the beam width, on the metaphor of a flashlight beam

> `beam width`（束宽）
>
> 释义：搜索中每一步保留的候选序列数目 k，取值越大搜索越充分但计算开销越高，机器翻译通常取 5 到 10。

它可以被参数化为更宽或更窄。

> that can be parameterized to be wider or narrower.

因此，在解码的第一步，我们对整个词表计算 softmax，为每个词分配一个概率。然后我们从该 softmax 输出中选出最优的 k 个选项。这最初的 k 个输出就是搜索前沿，而这 k 个初始词被称为候选假设。一个候选假设是一个输出序列，即迄今为止的译文，连同它的概率。

> Thus at the first step of decoding, we compute a softmax over the entire vocabulary, assigning a probability to each word. We then select the k-best options from this softmax output. These initial k outputs are the search frontier and these k initial words are called hypotheses. A hypothesis is an output sequence, a translation-sofar, together with its probability.

在随后的步骤中，这 k 个最优候选假设中的每一个都会被增量式地扩展，

> At subsequent steps, each of the k best hypotheses is extended incrementally
即被传给不同的解码器，每个解码器都对整个词表生成一个 softmax，从而把该候选假设扩展到每一个可能的下一个词元。这 k×V 个候选假设中的每一个都由 P(yi|x,y<i) 评分：即当前词选择的概率乘以通向它的路径的概率。然后我们把 k×V 个候选假设剪枝到最优的 k 个候选假设，因此搜索前沿中永远不超过 k 个候选假设，解码器也永远不超过 k 个。图 13.8 以 The green witch arrived. 的开头为例、取束宽为 2 说明了这一点。

> by being passed to distinct decoders, which each generate a softmax over the entire vocabulary to extend the hypothesis to every possible next token. Each of these k×V hypotheses is scored by P(yi|x,y<i): the product of the probability of the current word choice multiplied by the probability of the path that led to it. We then prune the k ×V hypotheses down to the k best hypotheses, so there are never more than k hypotheses at the frontier of the search, and never more than k decoders. Fig. 13.8 illustrates this with a beam width of 2 for the beginning of The green witch arrived.

![](images/13-machine-translation/fig_p13_0.png)

*图 13.8 束宽为 k = 2 的束搜索解码。在每个时间步，我们选出 k 个最优候选假设，为每个候选假设构造 V 种可能的扩展，对这 k×V 个候选假设评分，并选出最优的 k = 2 个继续。在时间 1，搜索前沿包含来自初始解码器状态的最优 2 个选项：arrived 和 the。我们扩展每一个，计算迄今为止所有候选假设的概率（arrived the、arrived aardvark、the green、the witch），并再次选出最优的 2 个（the green 和 the witch）作为搜索前沿。弧线上的图像示意性地表示每一步为给下一个词评分而必须运行的解码器（为简便起见未画出交叉注意力）。*
*Figure 13.8 Beam search decoding with a beam width of k = 2. At each time step, we choose the k best hypotheses, form the V possible extensions of each, score those k ×V hypotheses and choose the best k = 2 to continue. At time 1, the frontier has the best 2 options from the initial decoder state: arrived and the. We extend each, compute the probability of all the hypotheses so far (arrived the, arrived aardvark, the green, the witch) and again chose the best 2 (the green and the witch) to be the search frontier. The images on the arcs schematically represent the decoders that must be run at each step to score the next words (for simplicity not depicting cross-attention).*

这一过程持续进行，直到生成 EOS，表明已找到一个完整的候选输出。此时，已完成的候选假设会从搜索前沿中移除，束的大小减一。搜索继续进行，直到束的大小减为 0。结果将得到 k 个候选假设。

> This process continues until an EOS is generated indicating that a complete candidate output has been found. At this point, the completed hypothesis is removed from the frontier and the size of the beam is reduced by one. The search continues until the beam has been reduced to 0. The result will be k hypotheses.

为了用对数概率给每个节点评分，我们使用概率的链式法则，把

> To score each node by its log probability, we use the chain rule of probability to
p(y|x) 分解为每个词在给定其先前上下文的条件下概率的乘积，我们可以把它转化为对数之和（对于一个长度为 t 的输出字符串）：

> break down p(y|x) into the product of the probability of each word given its prior context, which we can turn into a sum of logs (for an output string of length t):

score(y) = logP(y|x)
= log(P(y1|x)P(y2|y1,x)P(y3|y1,y2,x)...P(yt|y1,...,yt−1,x)) tX

$$\text{log} P ( y _{i} | y _{1} ,..., y _{i - 1} , x )$$

= (13.15)
因此，在每一步，为计算一个部分句子的概率，我们只需把迄今为止前缀句子的对数概率与生成下一个词元的对数概率相加。图 13.9 用一些简单虚构的概率展示了图 13.8 中示例句子的评分过程。对数概率为负数或 0，两个对数概率中较大者（更接近 0）即为最大值。

> Thus at each step, to compute the probability of a partial sentence, we simply add the log probability of the prefix sentence so far to the log probability of generating the next token. Fig. 13.9 shows the scoring for the example sentence shown in Fig. 13.8, using some simple made-up probabilities. Log probabilities are negative or 0, and the max of two log probabilities is the one that is greater (closer to 0).

> i=1

![](images/13-machine-translation/fig_p14_0.png)

*图 13.9 束宽为 k = 2 的束搜索解码的评分。我们通过增量累加生成每个下一个词元的对数概率，来维护束中每个候选假设的对数概率。只有最优的 k 条路径会被扩展到下一步。*
*Figure 13.9 Scoring for beam search decoding with a beam width of k = 2. We maintain the log probability of each hypothesis in the beam by incrementally adding the logprob of generating each next token. Only the top k paths are extended to the next step.*

图 13.10 给出了该算法。这个版本的算法存在一个问题，

> Fig. 13.10 gives the algorithm. One problem with this version of the algorithm is
即已完成的候选假设可能具有不同的长度。由于语言模型通常给较长的字符串分配较低的概率，一个朴素的算法会为 y 选择较短的字符串。（这在解码的较早步骤中不是问题；因为束搜索是广度优先的，所有被比较的候选假设长度都相同。）因此，我们常常采用长度归一化方法，例如将对数概率除以词数：

> that the completed hypotheses may have different lengths. Because language models generally assign lower probabilities to longer strings, a naive algorithm would choose shorter strings for y. (This is not an issue during the earlier steps of decoding; since beam search is breadth-first, all the hypotheses being compared had the same length.) For this reason we often apply length normalization methods, like dividing the logprob by the number of words:

score(y) = 1 t logP(y|x) = 1 tX

$$\text{log} P ( y _{i} | y _{1} ,..., y _{i - 1} , x )$$

t
对于机器翻译，我们通常使用 5 到 10 之间的束宽 k，最终得到 k 个候选假设。我们可以把这 k 个候选假设连同它们各自的分数一起传给下游应用；如果只需要一个译文，就传概率最大的那个候选假设。

> For MT we generally use beam widths k between 5 and 10, giving us k hypotheses at the end. We can pass all k to the downstream application with their respective scores, or if we just need a single translation we can pass the most probable hypothesis.

> i=1

### 13.4.1 最小贝叶斯风险解码

> 13.4.1 Minimum Bayes Risk Decoding

> `minimum Bayes risk MBR`（最小贝叶斯风险 MBR）
>
> 释义：一种解码策略，不选概率最大的译文，而选与其余候选译文整体最相似、期望错误最小的那个译文。

最小贝叶斯风险（MBR）解码是一种替代性的解码算法，它

> Minimum Bayes risk or MBR decoding is an alternative decoding algorithm that
甚至可能比束搜索效果更好，也往往优于其他

> can work even better than beam search and also tends to be better than the other
解码算法，例如第 7.6 节介绍的温度采样。

> decoding algorithms like temperature sampling introduced in Section 7.6.

最小贝叶斯风险的直观思想是：我们不去尝试选择概率最大的译文，而是选择很可能错误最少的那个译文。

> The intuition of minimum Bayes risk is that instead of trying to choose the translation which is most probable, we choose the one that is likely to have the least error.

例如，我们可能希望解码算法找到在某个评价指标上得分最高的译文。例如在第 13.6 节中，我们将介绍 chrF 或 BERTScore 等指标，它们衡量一个候选译文与一组人工参考译文之间的拟合优度。一个使该分数最大化的译文，特别是在假定存在大量完美的人工

> For example, we might want our decoding algorithm to find the translation which has the highest score on some evaluation metric. For example in Section 13.6 we will introduce metrics like chrF or BERTScore that measure the goodness-of-fit between a candidate translation and a set of reference human translations. A translation that maximizes this score, especially with a hypothetically huge set of perfect human

![](images/13-machine-translation/fig_p15_0.png)

*图 13.10 束搜索解码。*
*Figure 13.10 Beam search decoding.*

译文的情况下，很可能是一个好的译文（具有最小风险），即使按我们特定的概率估计器它并不是概率最大的译文。

> translations is likely to be a good one (have minimum risk) even if it is not the most probable translation by our particular probability estimator.

在实践中，我们并不知道给定句子的完美译文集合。因此

> In practice, we don’t know the perfect set of translations for a given sentence. So
MBR 解码算法中使用的标准简化做法是：转而选择与某组候选译文最相似（按某种拟合优度度量）的那个候选译文。我们本质上是用一个较小的可能候选译文集合 Y 来近似所有可能译文的巨大空间 U。

> the standard simplification used in MBR decoding algorithms is to instead choose the candidate translation which is most similar (by some measure of goodness-offit) with some set of candidate translations. We’re essentially approximating the enormous space of all possible translations U with a smaller set of possible candidate translations Y.

给定这个可能候选译文的集合 Y，以及某个相似度或对齐函数 util，我们选择最佳译文 ŷ 为与所有其他候选译文最相似的那个译文：

> Given this set of possible candidate translations Y, and some similarity or alignment function util, we choose the best translation ˆy as the translation which is most similar to all the other candidate translations:

$$\sum_{c \in Y}$$

ˆy = argmax util(y,c) (13.17)
可以使用各种 util 函数，例如 chrF、BERTscore 或 BLEU。我们可以通过采样获得候选译文集合，使用第 7.6 节中的某种基础采样算法，例如温度采样；即使候选只有 32 或 64 个，也能获得不错的结果。

> Various util functions can be used, like chrF or BERTscore or BLEU. We can get the set of candidate translations by sampling using one of the basic sampling algorithms of Section 7.6 like temperature sampling; good results can be obtained with as few as 32 or 64 candidates.

> y∈Y c∈Y

最小贝叶斯风险解码也可用于其他 NLP 任务；事实上

> Minimum Bayes risk decoding can also be used for other NLP tasks; indeed
在被应用于机器翻译（Kumar and Byrne, 2004）之前，它就已被广泛用于语音识别（Stolcke et al., 1997; Goel and Byrne, 2000），并且已被证明在许多其他生成任务上同样效果良好（例如摘要、对话和图像描述（Suzgun et al., 2023a））。

> it was widely applied to speech recognition (Stolcke et al., 1997; Goel and Byrne, 2000) before being applied to machine translation (Kumar and Byrne, 2004), and has been shown to work well across many other generation tasks as well (e.g., summarization, dialogue, and image captioning (Suzgun et al., 2023a)).

## 13.5 低资源情境下的翻译

> 13.5 Translating in low-resource situations

对于某些语言，尤其是英语，在线资源十分丰富。存在许多大型平行语料库，包含英语与多种语言之间的译文。但世界上绝大多数语言并没有可用的大型平行训练文本。一个重要且仍在持续的研究问题是：如何为资源较少的语言获得良好的翻译。当我们需要翻译到低资源领域（例如某种恰好只有极少双语文本的特定文体）时，即使是高资源语言也可能存在资源问题。

> For some languages, and especially for English, online resources are widely available. There are many large parallel corpora that contain translations between English and many languages. But the vast majority of the world’s languages do not have large parallel training texts available. An important ongoing research question is how to get good translation with lesser resourced languages. The resource problem can even be true for high resource languages when we need to translate into low resource domains (for example in a particular genre that happens to have very little bitext).

这里我们简要介绍两种应对这一问题的常用方法

> Here we briefly introduce two commonly used approaches for dealing with this
即数据稀疏：回译（backtranslation），它是被称为数据增强的一般统计技术的一个特例，以及多语言模型；我们还会讨论一些社会技术问题。

> data sparsity: backtranslation, which is a special case of the general statistical technique called data augmentation, and multilingual models, and also discuss some socio-technical issues.

### 13.5.1 数据增强

> 13.5.1 Data Augmentation

数据增强是一种用于应对训练数据不足的统计技术，它通过添加由当前自然数据生成的新的合成数据来实现。

> Data augmentation is a statistical technique for dealing with insufficient training data, by adding new synthetic data that is generated from the current natural data.

机器翻译中最常用的数据增强技术被称为

> The most common data augmentation technique for machine translation is called
回译。回译依赖于这样一种直觉：尽管平行语料库

> backtranslation. Backtranslation relies on the intuition that while parallel corpora

> `backtranslation`（回译）
>
> 释义：利用目标语单语语料，经反向翻译系统生成源语文本，从而人工构造合成平行句对以扩充训练数据的方法。

对特定语言或领域而言可能有限，但我们往往能找到大型（或至少更大）的单语语料库，用以补充现有的较小平行语料库。该算法通过构造合成双语文本，来利用目标语中的单语语料库。

> may be limited for particular languages or domains, we can often find a large (or at least larger) monolingual corpus, to add to the smaller parallel corpora that are available. The algorithm makes use of monolingual corpora in the target language by creating synthetic bitexts.

在回译中，我们的目标是改进从源语到目标语的机器翻译，给定少量

> In backtranslation, our goal is to improve source-to-target MT, given a small
源语/目标语的平行文本（双语文本），以及目标语中的一些单语数据。我们首先用该双语文本训练一个反向的机器翻译系统：目标语到源语的机器翻译系统。然后我们用它把目标语单语数据翻译成源语。现在我们可以把这个合成双语文本（自然的目标语句子，与机器翻译生成的源语句子对齐）加入训练数据，并重新训练我们的源语到目标语机器翻译模型。例如，假设我们要从纳瓦霍语（Navajo）翻译成英语，但只有少量纳瓦霍语-英语双语文本，当然我们可以找到大量英语单语数据。我们用这个小双语文本构建一个反方向的机器翻译引擎（从英语到纳瓦霍语）。一旦把英语单语文本翻译成纳瓦霍语，我们就可以把这个合成的纳瓦霍语/英语双语文本加入训练数据。

> parallel text (a bitext) in the source/target languages, and some monolingual data in the target language. We first use the bitext to train a MT system in the reverse direction: a target-to-source MT system. We then use it to translate the monolingual target data to the source language. Now we can add this synthetic bitext (natural target sentences, aligned with MT-produced source sentences) to our training data, and retrain our source-to-target MT model. For example suppose we want to translate from Navajo to English but only have a small Navajo-English bitext, although of course we can find lots of monolingual English data. We use the small bitext to build an MT engine going the other way (from English to Navajo). Once we translate the monolingual English text to Navajo, we can add this synthetic Navajo/English bitext to our training data.

回译有各种参数。一是我们如何生成回译数据；我们可以用贪心推理运行解码器，或者使用束搜索。或者我们可以进行采样，如第 7 章中看到的温度采样算法。

> Backtranslation has various parameters. One is how we generate the backtranslated data; we can run the decoder in greedy inference, or use beam search. Or we can do sampling, like the temperature sampling algorithm we saw in Chapter 7.

另一个参数是回译数据与自然双语文本数据的比例；我们可以选择对双语文本数据上采样（纳入每个句子的多个副本）。总体而言，回译效果出奇地好；一项估计表明，用回译文本训练的系统所获得的增益约为用同等数量自然双语文本训练的 2/3（Edunov et al., 2018）。

> Another parameter is the ratio of backtranslated data to natural bitext data; we can choose to upsample the bitext data (include multiple copies of each sentence). In general backtranslation works surprisingly well; one estimate suggests that a system trained on backtranslated text gets about 2/3 of the gain as would training on the same amount of natural bitext (Edunov et al., 2018).

### 13.5.2 多语言模型

> 13.5.2 Multilingual models

到目前为止我们描述的模型都用于双语翻译：一种源语言、一种目标语言。也可以构建多语言翻译器。

> The models we’ve described so far are for bilingual translation: one source language, one target language. It’s also possible to build a multilingual translator.

在多语言翻译器中，我们通过向系统提供许多不同语言对的平行句

> In a multilingual translator, we train the system by giving it parallel sentences
来训练系统。这意味着我们需要告诉系统从哪种语言翻译、翻译到哪种语言！我们通过向编码器添加一个特殊词元 ls 来指定我们翻译所用的源语言，并向解码器添加一个特殊词元 lt 来告诉它我们想翻译成的目标语言。

> in many different pairs of languages. That means we need to tell the system which language to translate from and to! We tell the system which language is which by adding a special token ls to the encoder specifying the source language we’re translating from, and a special token lt to the decoder telling it the target language we’d like to translate into.

因此我们略微修改上面的式 13.9，以在式 13.19 中加入这些词元：

> Thus we slightly update Eq. 13.9 above to add these tokens in Eq. 13.19:

$$h = \text{encoder} ( x , l _{s} )$$

$$y _{i + 1} = \text{decoder} ( h , l _{t} , y _{1} ,..., y _{i} ) ∀ i \in [ 1 ,..., m ]$$

多语言模型的一个优点是，它们可以通过利用训练数据中恰好资源更丰富的相似语言的信息，来改进

> One advantage of a multilingual model is that they can improve the translation
低资源语言的翻译。也许我们不知道加利西亚语（Galician）中某个词的含义，但该词出现在与之相似且资源更丰富的语言西班牙语中。

> of lower-resourced languages by drawing on information from a similar language in the training data that happens to have more resources. Perhaps we don’t know the meaning of a word in Galician, but the word appears in the similar and higherresourced language Spanish.

### 13.5.3 社会技术问题

> 13.5.3 Sociotechnical issues

处理低资源语言的许多问题超出了纯技术范畴。一个问题是，对于低资源语言，尤其是来自低收入国家的语言，母语者往往没有作为内容选择的策展人、语言技术专家或衡量性能的评估者参与其中（Nekoto et al., 2020）。事实上，一项著名的研究手动审计了大量平行语料库和其他主要多语言数据集，发现对许多语料库而言，不到 50% 的句子质量可接受，大量数据由带有网络模板的重复句子或错误翻译组成，这表明母语者可能没有充分参与数据流程（Kreutzer et al., 2022）。

> Many issues in dealing with low-resource languages go beyond the purely technical. One problem is that for low-resource languages, especially from low-income countries, native speakers are often not involved as the curators for content selection, as the language technologists, or as the evaluators who measure performance(Nekoto et al., 2020). Indeed, one well-known study that manually audited a large set of parallel corpora and other major multilingual datasets found that for many of the corpora, less than 50% of the sentences were of acceptable quality, with a lot of data consisting of repeated sentences with web boilerplate or incorrect translations, suggesting that native speakers may not have been sufficiently involved in the data process (Kreutzer et al., 2022).

其他问题，例如许多机器翻译方法倾向于关注其中一种语言是英语的情形

> Other issues, like the tendency of many MT approaches to focus on the case
（Anastasopoulos and Neubig, 2020），则与资源分配有关。大多数大型多语言系统是在英语为两种语言之一的双语文本上训练的，而近期如 Fan et al. (2021) 和 Costa-juss`a et al. (2022) 的大型企业系统以及 Schwenk et al. (2021) 等数据集，则尝试处理大量语言（多达 200 种语言），并在更多语言对之间构建双语文本，而不只是通过英语。

> where one of the languages is English (Anastasopoulos and Neubig, 2020), have to do with allocation of resources. Where most large multilingual systems were trained on bitexts in which English was one of the two languages, recent huge corporate systems like those of Fan et al. (2021) and Costa-juss`a et al. (2022) and datasets like Schwenk et al. (2021) attempt to handle large numbers of languages (up to 200 languages) and create bitexts between many more pairs of languages and not just through English.

在较小的一端，Nekoto et al. (2020) 提出一种参与式设计流程

> At the smaller end, Nekoto et al. (2020) propose a participatory design process
以鼓励说这些低资源语言的内容创作者、策展人和语言技术专家参与开发机器翻译算法。他们提供在线小组、指导和基础设施，并报告了一个为低资源非洲语言开发机器翻译算法的案例研究。他们的结论之一是通过译后编辑而非直接评估来进行机器翻译评估，因为让标注者编辑一个机器翻译系统，然后测量机器翻译输出与其译后编辑版本之间的距离，既更便于训练评估者，也更容易衡量机器翻译输出中的真实错误，而非语言变异所造成的差异（Bentivogli et al., 2018）。

> to encourage content creators, curators, and language technologists who speak these low-resourced languages to participate in developing MT algorithms. They provide online groups, mentoring, and infrastructure, and report on a case study on developing MT algorithms for low-resource African languages. Among their conclusions was to perform MT evaluation by post-editing rather than direct evaluation, since having labelers edit an MT system and then measure the distance between the MT output and its post-edited version both was simpler to train evaluators and makes it easier to measure true errors in the MT output and not differences due to linguistic variation (Bentivogli et al., 2018).

## 13.6 机器翻译评估

> 13.6 MT Evaluation

翻译质量从两个维度来评估：

> Translations are evaluated along two dimensions:

- 充分性：译文在多大程度上准确传达源文的含义

> adequacy: how well the translation captures the exact meaning of the source

> `adequacy`（充分性）
>
> 释义：评价译文是否准确传达源文确切含义的维度，关注内容是否到位，而不看目标语表达是否自然。

句子。有时也被称为忠实度或保真度。

> sentence. Sometimes called faithfulness or fidelity.

- 流畅性：译文在目标语言中有多流畅（它是否合乎语法、

> fluency: how fluent the translation is in the target language (is it grammatical,

> `fluency`（流畅性）
>
> 释义：衡量机器译文在目标语言中是否通顺、清晰、自然的评估维度，与充分性并列构成两大评价维度。

清晰、易读、自然）。

> clear, readable, natural).

使用人工进行评估最为准确，但为了便利也会使用自动指标。

> Using humans to evaluate is most accurate, but automatic metrics are also used for convenience.

### 13.6.1 使用人工评分者评估机器翻译

> 13.6.1 Using Human Raters to Evaluate MT

最准确的评估使用人工评分者（例如在线众包工作者），沿这两个维度对每份译文进行评估。例如，在流畅性维度上，我们可以询问机器翻译输出（目标文本）有多易懂、多清晰、多易读或多自然。我们可以给评分者一个量表，例如从 1（完全无法理解）到 5（完全可理解），或从 1 到 100，并让他们对机器翻译输出的每个句子或段落进行打分。

> The most accurate evaluations use human raters, such as online crowdworkers, to evaluate each translation along the two dimensions. For example, along the dimension of fluency, we can ask how intelligible, how clear, how readable, or how natural the MT output (the target text) is. We can give the raters a scale, for example, from 1 (totally unintelligible) to 5 (totally intelligible), or 1 to 100, and ask them to rate each sentence or paragraph of the MT output.

我们可以用同样的方法评判第二个维度，即充分性，让评分者

> We can do the same thing to judge the second dimension, adequacy, using raters
在一个量表上打分。如果我们有双语评分者，可以把源语句子和一个候选的目标句子交给他们，并按 5 分制或 100 分制评定源语中有多少信息在目标语中得到了保留。如果我们只有单语评分者，但手头有源文本的良好人工译文，就可以把人工参考译文和机器目标译文交给单语评分者，同样评定保留了多少信息。另一种做法是进行排序：给评分者一对候选译文，并问他们哪一个

> to assign scores on a scale. If we have bilingual raters, we can give them the source sentence and a proposed target sentence, and rate, on a 5-point or 100-point scale, how much of the information in the source was preserved in the target. If we only have monolingual raters but we have a good human translation of the source text, we can give the monolingual raters the human reference translation and a target machine translation and again rate how much information is preserved. An alternative is to do ranking: give the raters a pair of candidate translations, and ask them which one

> `ranking`（排序）
>
> 释义：让评估者面对同一源句的一对候选译文并判断哪一个更好，用于替代逐一给出绝对分数的评估方式。

是他们更偏好的。

> they prefer.

对人工评分者（他们往往是在线众包工作者）的培训至关重要；评分者

> Training of human raters (who are often online crowdworkers) is essential; raters
如果没有翻译方面的专业知识，就很难把流畅性和充分性区分开，因此培训会包含能仔细区分这两者的示例。评分者之间常常存在分歧（源句可能有歧义，评分者的世界知识各不相同，评分者运用量表的方式也可能不同）。因此，常见的做法是剔除离群评分者，并且（如果我们使用的量表粒度足够细）通过从评分中减去均值再除以方差来对评分者做归一化。

> without translation expertise find it difficult to separate fluency and adequacy, and so training includes examples carefully distinguishing these. Raters often disagree(source sentences may be ambiguous, raters will have different world knowledge, raters may apply scales differently). It is therefore common to remove outlier raters, and (if we use a fine-grained enough scale) normalizing raters by subtracting the mean from their scores and dividing by the variance.

如上所述，使用人工评分者的另一种方式是让他们

> As discussed above, an alternative way of using human raters is to have them
对译文进行译后编辑，即拿到机器翻译输出并做最小程度的修改，直到他们认为它代表了一个正确的翻译。随后，他们的译后编辑译文与原始机器翻译输出之间的差异就可以作为衡量质量的一种指标。

> post-edit translations, taking the MT output and changing it minimally until they feel it represents a correct translation. The difference between their post-edited translations and the original MT output can then be used as a measure of quality.

### 13.6.2 自动评估

> 13.6.2 Automatic Evaluation

尽管人工能对机器翻译输出给出最好的评估，但开展人工评估既耗时又昂贵。因此，自动指标常被用作临时的替代手段。自动指标不如人工评估准确，但有助于检验潜在的系统改进，甚至可以用作训练时的自动损失函数。本节我们介绍两类这样的指标：基于字符或词重叠的指标，以及基于嵌入相似度的指标。

> While humans produce the best evaluations of machine translation output, running a human evaluation can be time consuming and expensive. For this reason automatic metrics are often used as temporary proxies. Automatic metrics are less accurate than human evaluation, but can help test potential system improvements, and even be used as an automatic loss function for training. In this section we introduce two families of such metrics, those based on character- or word-overlap and those based on embedding similarity.

基于字符重叠的自动评估：chrF

> Automatic Evaluation by Character Overlap: chrF
机器翻译评估中最简单也最稳健的指标称为 chrF，它代表

> The simplest and most robust metric for MT evaluation is called chrF, which stands

> `chrF`
>
> 释义：一种以字符 n 元重叠为基础的自动评估指标，由字符级的精确率与召回率组合而成，对形态变化丰富的语言较稳健。

字符 F 值（Popović, 2015）。chrF（以及许多更早的相关指标，如 BLEU、METEOR、TER 等）基于一个源自 Miller 和 Beebe-Center（1956）开创性工作的简单直觉：好的机器翻译往往会包含与同一句子的人工译文相同的字符和词。考虑来自平行语料库的一个测试集，其中每个源句都既有作为标准的人工目标译文，又有一个我们想要评估的候选机器译文。chrF 指标根据与人工译文的字符 n 元重叠数量构成的函数，对每个机器目标句子进行打分。

> for character F-score (Popovi´c, 2015). chrF (along with many other earlier related metrics like BLEU, METEOR, TER, and others) is based on a simple intuition derived from the pioneering work of Miller and Beebe-Center (1956): a good machine translation will tend to contain characters and words that occur in a human translation of the same sentence. Consider a test set from a parallel corpus, in which each source sentence has both a gold human target translation and a candidate MT translation we’d like to evaluate. The chrF metric ranks each MT target sentence by a function of the number of character n-gram overlaps with the human translation.

给定候选假设和参考译文，chrF 会接受一个参数 k，它表示

> Given the hypothesis and the reference, chrF is given a parameter k indicating
所要考虑的字符 n 元的长度，并计算 k 个精确率（一元精确率、二元精确率，等等）的平均值，以及 k 个召回率（一元召回率、二元召回率，等等）的平均值：

> the length of character n-grams to be considered, and computes the average of the k precisions (unigram precision, bigram, and so on) and the average of the k recalls(unigram recall, bigram recall, etc.):

chrP 候选假设中字符 1 元、2 元、……、k 元的百分比，这些 n 元

> chrP percentage of character 1-grams, 2-grams, ..., k-grams in the hypothesis that
出现在参考译文中，取平均。

> occur in the reference, averaged.

chrR 参考译文中字符 1 元、2 元、……、k 元的百分比，这些 n 元

> chrR percentage of character 1-grams, 2-grams,..., k-grams in the reference that
出现在候选假设中，取平均。

> occur in the hypothesis, averaged.

随后，该指标使用一个权重参数 β 把 chrP 和 chrR 组合起来，计算出一个 F 值。通常设 β = 2，从而使召回率的权重是精确率的两倍：

> The metric then computes an F-score by combining chrP and chrR using a weighting parameter β. It is common to set β = 2, thus weighing recall twice as much as precision:

chrFβ = (1+β 2) chrP·chrR (13.20)

$$β ^{2} \cdot \text{chrP} + \text{chrR}$$

当 β = 2 时，该式即为：

> For β = 2, that would be:

chrF2 = 5·chrP·chrR
4·chrP+chrR
例如，考虑我们想要对照参考译文 witness for the past 打分的两个候选假设。下面是这些候选假设以及使用参数 k = β = 2 计算得到的 chrF 值（在真实例子中，k 会是像 6 这样更大的数）：

> For example, consider two hypotheses that we’d like to score against the reference translation witness for the past. Here are the hypotheses along with chrF values computed using parameters k = β = 2 (in real examples, k would be a higher number like 6):

| REF: witness for the past, |  |
| --- | --- |
| HYP1: witness of the past, | chrF2,2 = .86 |
| HYP2: past witness | chrF2,2 = .62 |

HYP1: witness of the past, chrF2,2 = .86
我们来看看是如何为 HYP1 计算出那个 chrF 值的（HYP2 的 chrF 值计算就留作读者的练习）。首先，chrF 忽略空格，因此我们会把参考译文和候选假设中的空格都去掉：

> Let’s see how we computed that chrF value for HYP1 (we’ll leave the computation of the chrF value for HYP2 as an exercise for the reader). First, chrF ignores spaces, so we’ll remove them from both the reference and hypothesis:

REF: witnessforthepast,（18 个一元组，17 个二元组）HYP1: witnessofthepast,（17 个一元组，16 个二元组）

> REF: witnessforthepast, (18 unigrams, 17 bigrams) HYP1: witnessofthepast, (17 unigrams, 16 bigrams)
接下来看看参考译文和候选假设之间有多少个一元组和二元组相匹配：

> Next let’s see how many unigrams and bigrams match between the reference and hypothesis:

匹配的一元组：w i t n e s s f o t h e p a s t ,（17 个一元组）匹配的二元组：wi it tn ne es ss th he ep pa as st t,（13 个二元组）

> unigrams that match: w i t n e s s f o t h e p a s t , (17 unigrams) bigrams that match: wi it tn ne es ss th he ep pa as st t, (13 bigrams)
我们用这些数量来计算一元组和二元组的精确率与召回率：

> We use that to compute the unigram and bigram precisions and recalls:

unigram P: 17/17 = 1 unigram R: 17/18 = .944 bigram P: 13/16 = .813 bigram R: 13/17 = .765
最后我们取平均得到 chrP 和 chrR，并计算 F 值：

> Finally we average to get chrP and chrR, and compute the F-score:

chrP = (17/17+13/16)/2 = .906
chrR = (17/18+13/17)/2 = .855 chrF2,2 = 5 chrP∗chrR
4chrP+chrR = .86
chrF 简单、稳健，并且在许多

> chrF is simple, robust, and correlates very well with human judgments in many
语言中都与人判断高度相关（Kocmi et al., 2021）。

> languages (Kocmi et al., 2021).

另一种重叠度量：BLEU

> Alternative overlap metric: BLEU
存在多种替代的重叠度量。例如，在 chrF 出现之前，常用一种称为 BLEU（BiLingual Evaluation Understudy，双语评估替补）的基于词的重叠度量，它纯粹基于精确率，而不是像前面那样结合精确率与召回率（Papineni et al., 2002）。一个由候选译文句子组成的语料库的 BLEU 分数，是所有句子上的 n 元词精确率与在整个语料库上计算的长度惩罚的函数。

> There are various alternative overlap metrics. For example, before the development of chrF, it was common to use a word-based overlap metric called BLEU (for BiLingual Evaluation Understudy), that is purely precision-based rather than combining precision and recall (Papineni et al., 2002). The BLEU score for a corpus of candidate translation sentences is a function of the n-gram word precision over all the sentences combined with a brevity penalty computed over the corpus as a whole.

我们所说的 n 元精确率是什么意思？考虑一个由单句组成的

> What do we mean by n-gram precision? Consider a corpus composed of a single
句子。该语料库的一元精确率，是候选译文中同时出现在参考译文里的一元词元所占的百分比，二元及以此类推直到 4 元也是如此。BLEU 通过以下方式把这个一元度量扩展到整个语料库：分子是所有句子中同时出现在参考译文里的所有一元类型的计数之和，分母是所有候选句子中所有一元词元的计数总和。我们对一元、二元、三元和 4 元分别计算这种 n 元精确率，并取几何平均。BLEU 还有许多进一步的复杂之处，包括用于惩罚过短候选译文的长度惩罚，它还需要以某种特定方式对 n 元计数进行截断。

> sentence. The unigram precision for this corpus is the percentage of unigram tokens in the candidate translation that also occur in the reference translation, and ditto for bigrams and so on, up to 4-grams. BLEU extends this unigram metric to the whole corpus by computing the numerator as the sum over all sentences of the counts of all the unigram types that also occur in the reference translation, and the denominator is the total of the counts of all unigrams in all candidate sentences. We compute this n-gram precision for unigrams, bigrams, trigrams, and 4-grams and take the geometric mean. BLEU has many further complications, including a brevity penalty for penalizing candidate translations that are too short, and it also requires the ngram counts be clipped in a particular way.

由于 BLEU 是基于词的度量，它对词的分词非常敏感，

> Because BLEU is a word-based metric, it is very sensitive to word tokenization,
这使得如果不同系统依赖不同的分词标准，就不可能对它们进行比较，而且它在形态复杂的语言中效果不佳。

> making it impossible to compare different systems if they rely on different tokenization standards, and doesn’t work as well in languages with complex morphology.

尽管如此，你有时仍会看到用 BLEU 评估的系统，尤其是翻译成英语的情况。在这种情况下，使用像 SACREBLEU（Post, 2018）这样强制统一分词标准的工具包很重要。

> Nonetheless, you will sometimes still see systems evaluated by BLEU, particularly for translation into English. In such cases it’s important to use packages that enforce standardization for tokenization like SACREBLEU (Post, 2018).

机器翻译评估的统计显著性检验

> Statistical Significance Testing for MT evals
像 chrF（或 BLEU 等）这样基于字符或词重叠的度量，主要用于比较两个系统，目的是回答诸如这样的问题：我们刚发明的这个新算法是否改进了我们的机器翻译系统？为了判断两个机器翻译系统的 chrF 分数之间的差异是否为显著差异，我们使用配对自助法检验（paired bootstrap test），或类似的随机化检验。

> Character or word overlap-based metrics like chrF (or BLEU, or etc.) are mainly used to compare two systems, with the goal of answering questions like: did the new algorithm we just invented improve our MT system? To know if the difference between the chrF scores of two MT systems is a significant difference, we use the paired bootstrap test, or the similar randomization test.

要用自助法检验得到单个 chrF 分数的置信区间，回忆第 4.11 节，我们取自身的测试集（或开发集），通过从原始测试集中反复有放回抽样，创建成千上万个伪测试集。

> To get a confidence interval on a single chrF score using the bootstrap test, recall from Section 4.11 that we take our test set (or devset) and create thousands of pseudo-testsets by repeatedly sampling with replacement from the original test set.

现在我们计算每个伪测试集的 chrF 分数。如果我们去掉最高 2.5% 和最低 2.5% 的分数，剩下的分数将给出我们系统 chrF 分数的 95% 置信区间。

> We now compute the chrF score of each of the pseudo-testsets. If we drop the top 2.5% and bottom 2.5% of the scores, the remaining scores will give us the 95%confidence interval for the chrF score of our system.

为了比较两个机器翻译系统 A 和 B，我们抽取同一组伪测试集，

> To compare two MT systems A and B, we draw the same set of pseudo-testsets,
并分别计算它们的 chrF 分数。然后我们计算 A 的 chrF 分数高于 B 的伪测试集所占的百分比。

> and compute the chrF scores for each of them. We then compute the percentage of pseudo-test-sets in which A has a higher chrF score than B.

chrF：局限性

> chrF: Limitations
虽然像 chrF 或 BLEU 这样自动的字符和词重叠度量很有用，但它们有重要的局限。chrF 非常局部：一个被移动位置的大型短语可能几乎完全不改变 chrF 分数，而且 chrF 无法评估文档的跨句属性，比如其语篇连贯性（第 25 章）。chrF 及类似的自动度量在比较差异很大的系统时也表现不佳，例如把人工辅助翻译与机器翻译相比较，或把不同的机器翻译架构相互比较（Callison-Burch et al., 2006）。相反，像 chrF 这样的自动重叠度量在评估对单个系统的改动时最为合适。

> While automatic character and word-overlap metrics like chrF or BLEU are useful, they have important limitations. chrF is very local: a large phrase that is moved around might barely change the chrF score at all, and chrF can’t evaluate crosssentence properties of a document like its discourse coherence (Chapter 25). chrF and similar automatic metrics also do poorly at comparing very different kinds of systems, such as comparing human-aided translation against machine translation, or different machine translation architectures against each other (Callison-Burch et al., 2006). Instead, automatic overlap metrics like chrF are most appropriate when evaluating changes to a single system.

### 13.6.3 自动评估：基于嵌入的方法

> 13.6.3 Automatic Evaluation: Embedding-Based Methods

chrF 度量基于测量人工参考译文与候选机器翻译共有的精确字符 n 元。然而，这个标准过于严格，因为好的翻译可能使用不同的词或改写。最早在 METEOR（Banerjee and Lavie, 2005）等早期度量中开创的一种解决方案，是允许参考译文 x 与候选译文 ˜x 之间的同义词匹配。较新的度量则使用 BERT 或其他嵌入来实现这一直觉。

> The chrF metric is based on measuring the exact character n-grams a human reference and candidate machine translation have in common. However, this criterion is overly strict, since a good translation may use alternate words or paraphrases. A solution first pioneered in early metrics like METEOR (Banerjee and Lavie, 2005) was to allow synonyms to match between the reference x and candidate ˜x. More recent metrics use BERT or other embeddings to implement this intuition.

例如，在某些情况下，我们可能拥有带有翻译质量人工评估的数据集。这类数据集由元组 (x, ˜x,r) 组成，其中 x = (x1,...,xn) 是参考译文，˜x = (˜x1,..., ˜xm) 是候选机器翻译，r ∈R 是表示 ˜x 相对于 x 质量的人工评分。给定这样的数据，COMET（Rei et al., 2020）、BLEURT（Sellam et al., 2020）等算法在人工标注数据集上训练一个预测器，例如把 x 和 ˜x 通过一个 BERT 版本（经过额外的预训练，然后在人工标注的句子上微调），再接一个线性层，训练该线性层来预测

> For example, in some situations we might have datasets that have human assessments of translation quality. Such datasets consists of tuples (x, ˜x,r), where x = (x1,...,xn) is a reference translation, ˜x = (˜x1,..., ˜xm) is a candidate machine translation, and r ∈R is a human rating that expresses the quality of ˜x with respect to x. Given such data, algorithms like COMET (Rei et al., 2020) BLEURT (Sellam et al., 2020) train a predictor on the human-labeled datasets, for example by passing x and ˜x through a version of BERT (trained with extra pretraining, and then finetuned on the human-labeled sentences), followed by a linear layer that is trained to predict

- 这类模型的输出与人工标注高度相关。

> The output of such models correlates highly with human labels.

然而在其他情况下，我们并没有这样带人工标注的数据集。在这种

> In other cases, however, we don’t have such human-labeled datasets. In that
情况下，我们可以通过 x 与 ˜x 的嵌入相似度来衡量它们的相似度。

> case we can measure the similarity of x and ˜x by the similarity of their embeddings.

例如，图 13.11 所示的 BERTSCORE 算法（Zhang et al., 2020）把参考译文 x 和候选译文 ˜x 通过 BERT，为每个词元 xi 和 ˜xj 计算一个 BERT 嵌入。每对词元 (xi, ˜x j) 由其余弦

> The BERTSCORE algorithm (Zhang et al., 2020) shown in Fig. 13.11, for example, passes the reference x and the candidate ˜x through BERT, computing a BERT embedding for each token xi and ˜xj. Each pair of tokens (xi, ˜x j) is scored by its cosine
|xi||˜xj|。x 中的每个词元都与 ˜x 中的一个词元匹配以计算召回率，˜x 中的每个词元都与 x 中的一个词元匹配以计算精确率（每个词元都贪心地匹配到对应句子中最相似的词元）。BERTSCORE 提供精确率和召回率（以及由此得到的 F1）：

> |xi||˜xj|. Each token in x is matched to a token in ˜x to compute recall, and each token in˜x is matched to a token in x to compute precision (with each token greedily matched to the most similar token in the corresponding sentence). BERTSCORE provides precision and recall (and hence F1):

> xi·˜xj

RBERT = 1 X PBERT = 1 X (13.21)
max ˜x j∈˜x xi · ˜xj max xi∈x xi · ˜xj
|x| |˜x|

> xi∈x ˜x j∈˜x

![](images/13-machine-translation/fig_p22_0.png)

*图 13.11 从参考译文 x 和候选译文 ˆx 计算 BERTSCORE 召回率，出自 Zhang et al. (2020) 的图 1。此版本展示了该度量的一个扩展版本，其中词元还按其 idf 值加权。*
*Figure 13.11 The computation of BERTSCORE recall from reference x and candidate ˆx, from Figure 1 in Zhang et al. (2020). This version shows an extended version of the metric in which tokens are also weighted by their idf values.*

## 13.7 偏见与伦理问题

> 13.7 Bias and Ethical Issues

机器翻译带来了许多与我们在前面章节讨论过的相同的伦理问题。例如，考虑从匈牙利语（它有性别中性代词 ˝o）或西班牙语（常常省略代词）翻译成英语（英语中代词是必需的，并且有语法性别）的机器翻译系统。

> Machine translation raises many of the same ethical issues that we’ve discussed in earlier chapters. For example, consider MT systems translating from Hungarian(which has the gender neutral pronoun ˝o) or Spanish (which often drops pronouns) into English (in which pronouns are obligatory, and they have grammatical gender).

当翻译对一个人的指代且未指明性别时，机器翻译系统常常默认为男性性别（Schiebinger 2014, Prates et al. 2019）。而且机器翻译系统常常按照我们在第 5.8 节看到的那类文化刻板印象来指派性别。图 13.12 展示了 Prates et al. (2019) 中的例子，其中匈牙利语性别中性的 ˝o is a nurse 被译为 she，而性别中性的 ˝o is a CEO 被译为 he。Prates et al. (2019) 发现，这些刻板印象不能完全用美国劳动统计中的性别偏见来解释，因为机器翻译系统放大了这些偏见，代词被映射为男性或女性性别的概率高于基于实际劳动就业统计进行映射时的概率。

> When translating a reference to a person described without specified gender, MT systems often default to male gender (Schiebinger 2014, Prates et al. 2019). And MT systems often assign gender according to culture stereotypes of the sort we saw in Section 5.8. Fig. 13.12 shows examples from Prates et al. (2019), in which Hungarian gender-neutral ˝o is a nurse is translated with she, but gender-neutral ˝o is a CEO is translated with he. Prates et al. (2019) find that these stereotypes can’t completely be accounted for by gender bias in US labor statistics, because the biases are amplified by MT systems, with pronouns being mapped to male or female gender with a probability higher than if the mapping was based on actual labor employment statistics.

> 匈牙利语（性别中性）源文 英语机器翻译输出˝o egy ´apol´o she is a nurse˝o egy tud´os he is a scientist˝o egy m´ern¨ok he is an engineer˝o egy p´ek he is a baker˝o egy tan´ar she is a teacher˝o egy esk¨uv˝oszervez˝o she is a wedding organizer˝o egy vez´erigazgat´o he is a CEO
>
> *Hungarian (gender neutral) source English MT output˝o egy ´apol´o she is a nurse˝o egy tud´os he is a scientist˝o egy m´ern¨ok he is an engineer˝o egy p´ek he is a baker˝o egy tan´ar she is a teacher˝o egy esk¨uv˝oszervez˝o she is a wedding organizer˝o egy vez´erigazgat´o he is a CEO*

*图 13.12 从匈牙利语等性别中立的语言翻译成英语时，当前的机器翻译系统会把传统上男性主导职业的人理解为男性，把传统上女性主导职业的人理解为女性（Prates et al., 2019）。*
*Figure 13.12 When translating from gender-neutral languages like Hungarian into English, current MT systems interpret people from traditionally male-dominated occupations as male, and traditionally female-dominated occupations as female (Prates et al., 2019).*

类似地，最近的一个挑战集，即 WinoMT 数据集（Stanovsky et al., 2019）

> Similarly, a recent challenge set, the WinoMT dataset (Stanovsky et al., 2019)
表明：当要求机器翻译系统翻译那些描述不符合刻板性别角色的人的句子时，它们的表现会更差，例如“The doctor asked the nurse to help her in the operation”（医生让护士在手术中帮助她）。

> shows that MT systems perform worse when they are asked to translate sentences that describe people with non-stereotypical gender roles, like “The doctor asked the nurse to help her in the operation”.

机器翻译中的许多伦理问题仍需进一步研究。一个尚未解决的问题是，

> Many ethical questions in MT require further research. One open problem is
开发能够判断我们的系统不知道什么的度量指标。这是因为机器翻译系统可能被用在人工译者无法到场或会延误的紧急场景中：在医疗领域，帮助语言不通的患者与医生沟通；在法律领域，帮助法官或律师与证人或被告沟通。为了“不造成伤害”，系统需要有为候选译文赋予置信度的方法，从而能够拒绝给出

> developing metrics for knowing what our systems don’t know. This is because MT systems can be used in urgent situations where human translators may be unavailable or delayed: in medical domains, to help translate when patients and doctors don’t speak the same language, or in legal domains, to help judges or lawyers communi- cate with witnesses or defendants. In order to ‘do no harm’, systems need ways to assign confidence values to candidate translations, so they can abstain from giving

> `confidence`（置信度）
>
> 释义：指系统对某条候选译文正确程度的估计值，用于在把握不足时拒绝输出。

可能造成伤害的错误译文。

> incorrect translations that may cause harm.

## 13.8 小结

> 13.8 Summary

机器翻译是自然语言处理中应用最广泛的方向之一，而最初为机器翻译提出的编码器-解码器模型，已成为贯穿自然语言处理各个领域的关键工具。

> Machine translation is one of the most widely used applications of NLP, and the encoder-decoder model, first developed for MT is a key tool that has applications throughout NLP.

- 语言之间存在结构上和词汇上的差异，这些差异使翻译变得困难。
- 语言学的类型学领域研究其中的一些差异；语言可以按照它们在类型学维度上的位置来分类，例如动词是否位于宾语之前。
- 编码器-解码器网络由一个编码器网络和一个解码器组成：编码器网络接收输入序列并为其构造上下文化表示，即上下文；这个上下文表示随后被传给解码器，由解码器生成特定任务的输出序列。
- 交叉注意力使 Transformer 解码器能够查看编码器所有隐藏状态中的信息。
- 机器翻译模型在平行语料库上训练，平行语料库有时也称为双语文本，即以两种（或更多）语言出现的文本。
- 回译是一种利用目标语言单语语料库的方法：将初步的机器翻译引擎反向运行，以生成合成的双语文本。
- 机器翻译的评估通过衡量译文的充分性（它多大程度上捕捉了源句的含义）与流畅性（它在目标语言中是否流畅自然）来进行。人工评估是黄金标准，但诸如 chrF 这类衡量与人译译文之间字符 n 元重叠的自动评估指标，以及更近期基于嵌入相似度的指标，也被普遍使用。

> Languages have divergences, both structural and lexical, that make translation difficult.
> The linguistic field of typology investigates some of these differences; languages can be classified by their position along typological dimensions like whether verbs precede their objects.
> Encoder-decoder networks are composed of an encoder network that takes an input sequence and creates a contextualized representation of it, the context. This context representation is then passed to a decoder which generates a task-specific output sequence.
> Cross-attention allows the transformer decoder to view information from all the hidden states of the encoder.
> Machine translation models are trained on a parallel corpus, sometimes called a bitext, a text that appears in two (or more) languages.
> Backtranslation is a way of making use of monolingual corpora in the target language by running a pilot MT engine backwards to create synthetic bitexts.
> MT is evaluated by measuring a translation’s adequacy (how well it captures the meaning of the source sentence) and fluency (how fluent or natural it is in the target language). Human evaluation is the gold standard, but automatic evaluation metrics like chrF, which measure character n-gram overlap with human translations, or more recent metrics based on embedding similarity, are also commonly used.

## 历史注记

> Historical Notes

机器翻译在 20 世纪 40 年代末被认真提出，当时计算机刚刚诞生不久（Weaver, 1949/1955）。1954 年，机器翻译系统原型的首次公开演示（Dostert, 1955）在新闻界引起了巨大轰动（Hutchins, 1997）。此后十年间思想大量涌现，预示了后来大多数的发展。但这项工作超前于它的时代——其实现受到种种限制，例如在磁盘出现之前，没有存储词典信息的良好方式。

> MT was proposed seriously by the late 1940s, soon after the birth of the computer(Weaver, 1949/1955). In 1954, the first public demonstration of an MT system prototype (Dostert, 1955) led to great excitement in the press (Hutchins, 1997). The next decade saw a great flowering of ideas, prefiguring most subsequent developments. But this work was ahead of its time—implementations were limited by, for example, the fact that pending the development of disks there was no good way to store dictionary information.

由于高质量的机器翻译被证明难以实现（Bar-Hillel, 1960），人们逐渐形成了一种共识，

> As high-quality MT proved elusive (Bar-Hillel, 1960), there grew a consensus
即需要在形式语言学和计算语言学这些新领域中开展更好的评估和更多的基础研究。这一共识最终促成了 1966 年那份著名的批判性 ALPAC（自动语言处理咨询委员会）报告（Pierce et al., 1966），该报告在 20 世纪 60 年代中期导致美国对机器翻译的资助急剧削减。随着机器翻译研究失去学术声誉，机器翻译与计算语言学协会把机器翻译从其名称中去掉。然而，一些机器翻译开发者仍然坚持，出现了诸如 Météo 这样把天气预报从英语译成法语的早期机器翻译系统（Chandioux, 1976），以及诸如 Systran 这样的工业系统。

> on the need for better evaluation and more basic research in the new fields of formal and computational linguistics. This consensus culminated in the famously critical ALPAC (Automatic Language Processing Advisory Committee) report of 1966(Pierce et al., 1966) that led in the mid 1960s to a dramatic cut in funding for MT in the US. As MT research lost academic respectability, the Association for Machine Translation and Computational Linguistics dropped MT from its name. Some MT developers, however, persevered, and there were early MT systems like M´et´eo, which translated weather forecasts from English to French (Chandioux, 1976), and industrial systems like Systran.

在早期，机器翻译的架构空间涵盖三种通用模型。在直接翻译中，系统逐词地处理源语言文本，逐步翻译每一个词。直接翻译使用一部大型双语词典，其中每个词条都是一个负责翻译一个词的小程序。在转换方法中，我们首先解析输入文本，然后应用规则把源语言的分析结果转换为目标语言的分析结果，再从分析树生成目标语言句子。在中间语言方法中，我们把源语言文本分析成某种抽象的意义表示，称为中间语言，然后从这种中间语言表示生成目标语言。可视化这三种早期方法的一种常见方式，是图 13.13 所示的 Vauquois 三角。该三角展示了

> In the early years, the space of MT architectures spanned three general models. In direct translation, the system proceeds word-by-word through the sourcelanguage text, translating each word incrementally. Direct translation uses a large bilingual dictionary, each of whose entries is a small program with the job of translating one word. In transfer approaches, we first parse the input text and then apply rules to transform the source-language parse into a target language parse. We then generate the target language sentence from the parse tree. In interlingua approaches, we analyze the source language text into some abstract meaning representation, called an interlingua. We then generate into the target language from this interlingual representation. A common way to visualize these three early approaches was the Vauquois triangle shown in Fig. 13.13. The triangle shows the

> `Vauquois`
>
> 释义：法国机器翻译研究者，1968 年提出用于比较早期翻译架构的三角图。

> `triangle`（三角）
>
> 释义：一种用顶点表示分析深度、用层级表示所需转换知识量的架构比较图示。

从直接方法经转换方法到中间语言方法，所需的分析深度（在分析和生成两端）不断增加。此外，它还展示出：随着我们沿三角向上移动，所需的转换知识量不断减少——从直接层面的海量转换（几乎全部知识都是每个词的转换知识），到转换层面（转换规则仅针对分析树或论旨角色），再到中间语言层面（没有特定的转换知识）。我们可以把编码器-解码器网络视为一种中间语言方法，其中注意力起到整合直接方法与转换方法的作用，使解码器能够直接访问词或其表示。

> increasing depth of analysis required (on both the analysis and generation end) as we move from the direct approach through transfer approaches to interlingual approaches. In addition, it shows the decreasing amount of transfer knowledge needed as we move up the triangle, from huge amounts of transfer at the direct level (almost all knowledge is transfer knowledge for each word) through transfer (transfer rules only for parse trees or thematic roles) through interlingua (no specific transfer knowledge). We can view the encoder-decoder network as an interlingual approach, with attention acting as an integration of direct and transfer, allowing words or their representations to be directly accessed by the decoder.

![](images/13-machine-translation/fig_p24_0.png)

*图 13.13 Vauquois（1968）三角。*
*Figure 13.13 The Vauquois (1968) triangle.*

统计方法在 1990 年前后开始得到应用，最初得益于像加拿大议会辩论记录 Hansard 语料库这样的大型双语语料库的发展——该语料库同时以法语和英语保存——随后又得益于互联网的成长。早期，若干研究者表明，可以利用词语或句子长度之类的简单线索，从双语语料库中抽取对齐的句对（Kay and Röscheisen 1988, Gale and Church 1991, Gale and Church 1993, Kay and Röscheisen 1993）。

> Statistical methods began to be applied around 1990, enabled first by the development of large bilingual corpora like the Hansard corpus of the proceedings of the Canadian Parliament, which are kept in both French and English, and then by the growth of the web. Early on, a number of researchers showed that it was possible to extract pairs of aligned sentences from bilingual corpora, using words or simple cues like sentence length (Kay and R¨oscheisen 1988, Gale and Church 1991, Gale and Church 1993, Kay and R¨oscheisen 1993).

与此同时，IBM 团队直接借鉴噪声信道模型

> At the same time, the IBM group, drawing directly on the noisy channel model
（用于语音识别的那种），提出了两种相关的统计机器翻译范式。这些

> for speech recognition, proposed two related paradigms for statistical MT. These

> `statistical MT IBM Models`（统计机器翻译 IBM 模型）
>
> 释义：IBM 团队提出的一组生成式翻译算法，编号 1 至 5，用于对词对齐与翻译概率建模。

范式包括后来被称为 IBM 模型 1 至

> include the generative algorithms that became known as IBM Models 1 through
5 的生成式算法，它们在 Candide 系统中实现。这些算法（解码器除外）被完整而详细地发表——这受到部分资助该工作的美国政府的鼓励——从而使它们对研究界产生了巨大影响（Brown et al. 1990, Brown et al. 1993）。

> 5, implemented in the Candide system. The algorithms (except for the decoder) were published in full detail— encouraged by the US government who had par- tially funded the work— which gave them a huge impact on the research community(Brown et al. 1990, Brown et al. 1993).

该团队还开发了一种判别式方法，称为 MaxEnt（maximum entropy，即最大熵，是逻辑回归的另一种表述），它允许以判别式而非生成式的方式组合多种特征（Berger et al., 1996），后由 Och 和 Ney（2002）进一步发展。

> The group also developed a discriminative approach, called MaxEnt (for maximum entropy, an alternative formulation of logistic regression), which allowed many features to be combined discriminatively rather than generatively (Berger et al., 1996), which was further developed by Och and Ney (2002).

到世纪之交，机器翻译的大多数学术研究都使用

> By the turn of the century, most academic research on machine translation used
统计机器翻译，或采用生成式，或采用判别式。生成式方法的一个扩展版本

> statistical MT, either in the generative or discriminative mode. An extended version

> `phrase-based translation`（基于短语的翻译）
>
> 释义：一种以短语对为单位学习对应关系、再组合成整句译文的统计方法。

被称为基于短语的翻译，它建立在

> of the generative approach, called phrase-based translation was developed, based
为短语对归纳译文的基础上（Och 1998, Marcu and Wong 2002, Koehn et al. (2003), Och and Ney 2004, Deng and Byrne 2005, 等等）。

> on inducing translations for phrase-pairs (Och 1998, Marcu and Wong 2002, Koehn et al. (2003), Och and Ney 2004, Deng and Byrne 2005, inter alia).

在 BLEU 这样的自动评估指标被开发出来之后（Papineni et al., 2002），

> Once automatic metrics like BLEU were developed (Papineni et al., 2002), the
借鉴 IBM 的 MaxEnt 工作（Berger et al., 1996）的判别式对数线性形式（Och and Ney, 2004），被用来直接优化 BLEU 之类的评估指标，所用的方法称为最小错误率训练（Minimum Error Rate Training），简称 MERT（Och,

> discriminative log linear formulation (Och and Ney, 2004), drawing from the IBM MaxEnt work (Berger et al., 1996), was used to directly optimize evaluation metrics like BLEU in a method known as Minimum Error Rate Training, or MERT (Och,

> `MERT`
>
> 释义：最小错误率训练，一种直接以 BLEU 等评估指标为目标来调优翻译系统参数的方法。

2003），这也借鉴了语音识别模型（Chou et al., 1993）。像 GIZA（Och and Ney, 2003）和 Moses（Koehn et al. 2006, Zens and Ney 2007）这样的工具包

> 2003), also drawing from speech recognition models (Chou et al., 1993). Toolkits like GIZA (Och and Ney, 2003) and Moses (Koehn et al. 2006, Zens and Ney 2007)

> `Moses`
>
> 释义：一款被广泛使用的开源统计机器翻译系统工具包，支持基于短语的翻译建模。

被广泛使用。

> were widely used.

世纪之交还有一些方法基于

> There were also approaches around the turn of the century that were based on

> `transduction grammars`（转换语法）
>
> 释义：一种用树到树的规则刻画源语言与目标语言结构对应关系的语法形式。

句法结构（第 19 章）。基于转换语法的模型（也

> syntactic structure (Chapter 19). Models based on transduction grammars (also
称为同步语法）为不同语言的一对句子指派平行的句法树结构，目标是通过在树上施加重排操作来翻译这些句子。从生成式视角看，可以把转换语法视为生成两种语言中互相对齐的句对。一些使用最广泛的模型包括反转转换

> called synchronous grammars) assign a parallel syntactic tree structure to a pair of sentences in different languages, with the goal of translating the sentences by applying reordering operations on the trees. From a generative perspective, we can view a transduction grammar as generating pairs of aligned sentences in two languages. Some of the most widely used models included the inversion transduction

> `inversion`（反转）
>
> 释义：指合并两个子成分时交换其先后次序的操作，用于刻画两种语言之间的语序重排。

语法（Wu, 1996）与同步上下文无关语法（Chiang, 2005），

> grammar (Wu, 1996) and synchronous context-free grammars (Chiang, 2005),

> `transduction grammar`（转换语法）
>
> 释义：又称同步语法，为两种语言的一对句子同时指派平行的句法树，通过在树上做重排操作实现互译。

神经网络曾在不同时期被应用于机器

> Neural networks had been applied at various times to various aspects of machine
翻译的各个方面；例如 Schwenk 等人（2006）展示了如何在基于 IBM 模型 4 的西班牙语-英语系统中用神经语言模型替代 n 元语言模型。现代神经编码器-解码器方法由 Kalchbrenner 和 Blunsom（2013）开创，他们使用 CNN 编码器和 RNN 解码器，该方法由 Bahdanau 等人（2015）首次应用于机器翻译。Transformer 编码器-解码器由 Vaswani 等人（2017）提出（参见第 7 章的历史回顾一节）。

> translation; for example Schwenk et al. (2006) showed how to use neural language models to replace n-gram language models in a Spanish-English system based on IBM Model 4. The modern neural encoder-decoder approach was pioneered by Kalchbrenner and Blunsom (2013), who used a CNN encoder and an RNN decoder, and was first applied to MT by Bahdanau et al. (2015). The transformer encoderdecoder was proposed by Vaswani et al. (2017) (see the History section of Chapter 7).

机器翻译评估的研究起步相当早。Miller 和

> Research on evaluation of machine translation began quite early. Miller and
Beebe-Center（1956）提出了若干借鉴心理语言学工作的方法。这些方法包括用 cloze 任务和 Shannon 任务来测量可理解性，以及一个度量与人工译文之间编辑距离的指标，这一直觉正是所有现代基于重叠的自动评估指标的基础。ALPAC 报告收录了由 John Carroll 开展的一项极具影响力的早期评估研究（Pierce 等人，1966，附录 10）。Carroll 为忠实度和可理解性提出了不同的度量，并让评分者在 9 点量表上对它们进行主观打分。

> Beebe-Center (1956) proposed a number of methods drawing on work in psycholinguistics. These included the use of cloze and Shannon tasks to measure intelligibility as well as a metric of edit distance from a human translation, the intuition that underlies all modern overlap-based automatic evaluation metrics. The ALPAC report included an early evaluation study conducted by John Carroll that was extremely influential (Pierce et al., 1966, Appendix 10). Carroll proposed distinct measures for fidelity and intelligibility, and had raters score them subjectively on 9-point scales.

许多早期评估工作聚焦于自动的词重叠指标，如 BLEU（Papineni 等人，2002）、NIST（Doddington，2002）、TER（Translation Error Rate，翻译错误率）（Snover 等人，2006）、精确率与召回率（Turian 等人，2003）以及 METEOR（Banerjee 和 Lavie，2005）；像 chrF（Popovi´c，2015）这样的字符 n 元重叠方法出现得更晚。较晚近的评估工作与 ALPAC 报告相呼应，强调了严谨统计方法以及使用人工评估的重要性（Kocmi 等人，2021；Marie 等人，2021）。

> Much early evaluation work focuses on automatic word-overlap metrics like BLEU(Papineni et al., 2002), NIST (Doddington, 2002), TER (Translation Error Rate)(Snover et al., 2006), Precision and Recall (Turian et al., 2003), and METEOR(Banerjee and Lavie, 2005); character n-gram overlap methods like chrF (Popovi´c, 2015) came later. More recent evaluation work, echoing the ALPAC report, has emphasized the importance of careful statistical methodology and the use of human evaluation (Kocmi et al., 2021; Marie et al., 2021).

机器翻译的早期历史综述见 Hutchins 1986 和 1997；Nirenburg 等人

> The early history of MT is surveyed in Hutchins 1986 and 1997; Nirenburg et al.
（2002）汇编了早期的文献选读。语言类型学的入门介绍可参见 Croft（1990）或 Comrie（1989）。

> (2002) collects early readings. See Croft (1990) or Comrie (1989) for introductions to linguistic typology.

## 习题

> Exercises

13.1 手工计算第 294 页中 HYP2 的 chrF2,2 分数（答案应

> 13.1 Compute by hand the chrF2,2 score for HYP2 on page 294 (the answer should
四舍五入为 .62）。

> round to .62).
