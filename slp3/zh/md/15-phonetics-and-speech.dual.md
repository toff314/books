# 第 15 章 语音学与语音特征提取

### 章

> CHAPTER

# 15 语音学与语音特征提取

> 15 Phonetics and Speech Feature Extraction

本书此前一直在讨论的文本由字符构成，而这些字符并不只是随机的符号。它们还是一项了不起的科学发明：一个关于构成人类言语的诸要素的理论模型。

> The characters that make up the texts we’ve been discussing in this book aren’t just random symbols. They are also an amazing scientific invention: a theoretical model of the elements that make up human speech.

我们所知最早的书写系统（苏美尔文、中文、玛雅文）

> The earliest writing systems we know of (Sumerian, Chinese, Mayan) were
主要是表词文字：一个符号代表一整个词。但即使在能够找到的最早阶段，有些符号也被用来表示构成词语的语音。右侧那个在苏美尔语中读作 ba、意为“配给”的楔形文字符号，也可以纯粹用作读音 /ba/。我们所能见到的最早汉字刻在用于占卜的甲骨上，同样含有表音成分。纯粹以语音为基础的书写系统，无论是音节文字（如日语平假名）、字母文字（如罗马字母表）还是辅音文字（如闪米特诸书写系统），都可追溯到这些早期的意音音节系统，而且往往是在两种文化交汇时形成的。因此，阿拉伯文、阿拉米文、希伯来文、希腊文和罗马字母系统都源自一种西闪米特文字，据推测，这种文字是西闪米特雇佣兵从埃及圣书体的草书体改造而来的。日语假名是从汉字表音字符的草书体改造而来，而这些汉字本身在汉语中就被用来为唐代传入中国的佛经中的梵语标音。

> mainly logographic: one symbol representing a whole word. But from the earliest stages we can find, some symbols were also used to represent the sounds that made up words. The cuneiform sign to the right pronounced ba and meaning “ration” in Sumerian could also function purely as the sound /ba/. The earliest Chinese characters we have, carved into bones for divination, similarly contain phonetic elements. Purely sound-based writing systems, whether syllabic(like Japanese hiragana), alphabetic (like the Roman alphabet), or consonantal (like Semitic writing systems), trace back to these early logo-syllabic systems, often as two cultures came together. Thus, the Arabic, Aramaic, Hebrew, Greek, and Roman systems all derive from a West Semitic script that is presumed to have been modified by Western Semitic mercenaries from a cursive form of Egyptian hieroglyphs. The Japanese syllabaries were modified from a cursive form of Chinese phonetic characters, which themselves were used in Chinese to phonetically represent the Sanskrit in the Buddhist scriptures that came to China in the Tang dynasty.

![](images/15-phonetics-and-speech/img_29.png)

这一隐含的观念——口语词由更小的语音单位构成——

> This implicit idea that the spoken word is composed of smaller units of speech
是语音识别（把波形转写为文本）和文本转语音（把文本转换为波形）这两类算法的基础。在本章中，我们从计算的角度考察语音学，这门学科研究的是

> underlies algorithms for both speech recognition (transcribing waveforms into text) and text-to-speech (converting text into waveforms). In this chapter we give a computational perspective on phonetics, the study of the speech sounds used in the

> `phonetics`（语音学）
>
> 释义：研究人类言语中语音的学科，考察语音如何由发音器官产生、在声学上如何实现，以及如何被数字化与处理。

世界诸语言中所使用的语音、这些语音如何在人类声道中发出、如何在声学上得以实现，以及如何被数字化和处理。

> languages of the world, how they are produced in the human vocal tract, how they are realized acoustically, and how they can be digitized and processed.

## 15.1 语音与音标转写

> 15.1 Speech Sounds and Phonetic Transcription

像‘p’或‘a’这样的字母本身已经是人类言语语音的一种有用模型，而且我们将在第 16 章看到如何在字母与波形之间建立映射。

> A letter like ‘p’ or ‘a’ is already a useful model of the sounds of human speech, and indeed we’ll see in Chapter 16 how to map between letters and waveforms.

尽管如此，把语音表示得稍微抽象一些是有帮助的。我们把一个词的读音表示为一串音子，音子即语音，

> Nonetheless, it is helpful to represent sounds slightly more abstractly. We’ll represent the pronunciation of a word as a string of phones, which are speech sounds,

> `phone`（音子）
>
> 释义：实际发出的一段语音片段，是言语中最基本的可标注声音单位，一个词的读音由若干这样的单位组成。

每个音子都用一个取自罗马字母表的符号来表示。

> each represented with symbols adapted from the Roman alphabet.

为世界诸语言进行转写所用的标准语音表示法是

> The standard phonetic representation for transcribing the world’s languages is
国际音标字母表（IPA），这是一个不断演进的标音标准，最早制定于

> the International Phonetic Alphabet (IPA), an evolving standard first developed in

> `IPA`
>
> 释义：国际音标字母表，是为世界诸语言的语音提供统一符号的通行标音系统，自 1888 年起不断修订。

1888 年。但在本章中，我们改用 ARPAbet（Shoup, 1980）来表示音子，这是一种简单的语音字母表（图 15.1），它方便地用 ASCII 符号来表示 IPA 中美国英语的那一子集。

> 1888. But in this chapter we’ll instead represent phones with the ARPAbet (Shoup, 1980), a simple phonetic alphabet (Fig. 15.1) that conveniently uses ASCII symbols to represent an American-English subset of the IPA.

IPA 和 ARPAbet 的许多符号与人们熟悉的罗马字母相同。因此，举例来说，ARPAbet 音子 [p] 表示这样一个辅音，它出现在

> Many of the IPA and ARPAbet symbols are equivalent to familiar Roman letters. So, for example, the ARPAbet phone [p] represents the consonant sound at the

<!--figbox-->
> ARPAbet IPA ARPAbet ARPAbet IPA ARPAbet 符号 符号 单词 转写 符号 符号 单词 转写[p] [p] parsley [p aa r s l iy] [iy] [i] lily [l ih l iy][t] [t] tea [t iy] [ih] [I] lily [l ih l iy][k] [k] cook [k uh k] [ey] [eI] daisy [d ey z iy][b] [b] bay [b ey] [eh] [E] pen [p eh n][d] [d] dill [d ih l] [ae] [æ] aster [ae s t axr][g] [g] garlic [g aa r l ix k] [aa] [A] poppy [p aa p iy][m] [m] mint [m ih n t] [ao] [O] orchid [ao r k ix d][n] [n] nutmeg [n ah t m eh g] [uh] [U] wood [w uh d][ng] [N] baking [b ey k ix ng] [ow] [oU] lotus [l ow dx ax s][f] [f] flour [f l aw axr] [uw] [u] tulip [t uw l ix p][v] [v] clove [k l ow v] [ah] [2] butter [b ah dx axr][th] [T] thick [th ih k] [er] [Ç] bird [b er d][dh] [D] those [dh ow z] [ay] [aI] iris [ay r ix s][s] [s] soup [s uw p] [aw] [aU] flower [f l aw axr][z] [z] eggs [eh g z] [oy] [oI] soil [s oy l][sh] [S] squash [s k w aa sh] [ax] [@] pita [p iy t ax][zh] [Z] ambrosia [ae m b r ow zh ax][ch] [tS] cherry [ch eh r iy][jh] [dZ] jar [jh aa r][l] [l] licorice [l ih k axr ix sh][w] [w] kiwi [k iy w iy][r] [r] rice [r ay s][y] [j] yellow [y eh l ow][h] [h] honey [h ah n iy]
>
> *ARPAbet IPA ARPAbet ARPAbet IPA ARPAbet Symbol Symbol Word Transcription Symbol Symbol Word Transcription[p] [p] parsley [p aa r s l iy] [iy] [i] lily [l ih l iy][t] [t] tea [t iy] [ih] [I] lily [l ih l iy][k] [k] cook [k uh k] [ey] [eI] daisy [d ey z iy][b] [b] bay [b ey] [eh] [E] pen [p eh n][d] [d] dill [d ih l] [ae] [æ] aster [ae s t axr][g] [g] garlic [g aa r l ix k] [aa] [A] poppy [p aa p iy][m] [m] mint [m ih n t] [ao] [O] orchid [ao r k ix d][n] [n] nutmeg [n ah t m eh g] [uh] [U] wood [w uh d][ng] [N] baking [b ey k ix ng] [ow] [oU] lotus [l ow dx ax s][f] [f] flour [f l aw axr] [uw] [u] tulip [t uw l ix p][v] [v] clove [k l ow v] [ah] [2] butter [b ah dx axr][th] [T] thick [th ih k] [er] [Ç] bird [b er d][dh] [D] those [dh ow z] [ay] [aI] iris [ay r ix s][s] [s] soup [s uw p] [aw] [aU] flower [f l aw axr][z] [z] eggs [eh g z] [oy] [oI] soil [s oy l][sh] [S] squash [s k w aa sh] [ax] [@] pita [p iy t ax][zh] [Z] ambrosia [ae m b r ow zh ax][ch] [tS] cherry [ch eh r iy][jh] [dZ] jar [jh aa r][l] [l] licorice [l ih k axr ix sh][w] [w] kiwi [k iy w iy][r] [r] rice [r ay s][y] [j] yellow [y eh l ow][h] [h] honey [h ah n iy]*
<!--/figbox-->

*图 15.1 英语辅音（左）与元音（右）的 ARPAbet 与 IPA 符号。*
*Figure 15.1 ARPAbet and IPA symbols for English consonants (left) and vowels (right).*

platypus、puma 和 plantain 的开头，leopard 的中间，或 antelope 的结尾。不过总体而言，英语正字法的字母与音子之间的对应关系相当不透明；同一个字母在不同语境下可以表示非常不同的语音。英语字母 c 在 cougar [k uw g axr] 中对应音子 [k]，但在 cell [s eh l] 中对应音子 [s]。音子 [k] 除了写作 c 和 k 之外，还可以作为 x 的一部分出现（fox [f aa k s]），写作 ck（jackal [jh ae k el]），以及写作 cc（raccoon [r ae k uw n]）。许多其他语言，例如西班牙语，其语音与正字法的对应关系比英语透明得多。

> beginning of platypus, puma, and plantain, the middle of leopard, or the end of antelope. In general, however, the mapping between the letters of English orthography and phones is relatively opaque; a single letter can represent very different sounds in different contexts. The English letter c corresponds to phone [k] in cougar [k uw g axr], but phone [s] in cell [s eh l]. Besides appearing as c and k, the phone [k] can appear as part of x (fox [f aa k s]), as ck (jackal [jh ae k el]) and as cc (raccoon [r ae k uw n]). Many other languages, for example, Spanish, are much more transparent in their sound-orthography mapping than English.

用于音标转写的语音资源种类繁多。在线发音词典给出单词的音标转写。LDC

> There are a wide variety of phonetic resources for phonetic transcription. Online pronunciation dictionaries give phonetic transcriptions for words. The LDC

> `pronunciation dictionary`（发音词典）
>
> 释义：列出词条及其读音转写的词典，为语音识别与语音合成提供每个词该怎么读的信息。

发布了埃及阿拉伯语、荷兰语、英语、德语、日语、韩语、汉语普通话和西班牙语的发音词库。就英语而言，CELEX 词典（Baayen et al., 1995）收录了 160,595 个词形的读音，并附带音节划分、重音以及形态和词性信息。开源的 CMU 发音词典（CMU, 1993）收录了约 134,000 个词形的读音，而粒度更细、收录 110,000 词的 UNISYN 词典（Fitt, 2002）可免费用于研究目的，给出音节划分、重音，还给出英语数十种方言的读音。

> distributes pronunciation lexicons for Egyptian Arabic, Dutch, English, German, Japanese, Korean, Mandarin, and Spanish. For English, the CELEX dictionary(Baayen et al., 1995) has pronunciations for 160,595 wordforms, with syllabification, stress, and morphological and part-of-speech information. The open-source CMU Pronouncing Dictionary (CMU, 1993) has pronunciations for about 134,000 wordforms, while the fine-grained 110,000 word UNISYN dictionary (Fitt, 2002), freely available for research purposes, gives syllabifications, stress, and also pronunciations for dozens of dialects of English.

另一类有用的资源是语音标注语料库，其中一批波形被人工标注上相应的音子串。TIMIT 语料库（NIST, 1990）最初是德州仪器（TI）、MIT 和 SRI 的联合项目，是一个包含 6300 个朗读句子的语料库，来自 630 位说话人，每人 10 句。这 6300 个句子取自一个包含 2342 个句子的集合，其中一些被挑选来包含特定的方言特征词，另一些则用于最大化语音双音子的覆盖。语料库中的每个句子都经过人工语音标注，音子序列与句子波形文件自动对齐，随后自动得到的音子边界再经人工校正（Seneff and Zue, 1988）。

> Another useful resource is a phonetically annotated corpus, in which a collection of waveforms is hand-labeled with the corresponding string of phones. The TIMIT corpus (NIST, 1990), originally a joint project between Texas Instruments(TI), MIT, and SRI, is a corpus of 6300 read sentences, with 10 sentences each from 630 speakers. The 6300 sentences were drawn from a set of 2342 sentences, some selected to have particular dialect shibboleths, others to maximize phonetic diphone coverage. Each sentence in the corpus was phonetically hand-labeled, the sequence of phones was automatically aligned with the sentence wavefile, and then the automatic phone boundaries were manually hand-corrected (Seneff and Zue, 1988).

> `time-aligned transcription`（时间对齐转写）
>
> 释义：一种转写形式，为每个音子标出其在波形中的起始与结束时间，使语音片段与其声学信号能够对应起来。

其结果就是时间对齐转写：这是一种转写，其中每个音子都

> The result is a time-aligned transcription: a transcription in which each phone is
与波形中的一个起始时间和一个结束时间相关联，如图 15.2 的例子所示。

> associated with a start and end time in the waveform, like the example in Fig. 15.2.

<!--figbox-->
> 她一整年都把你的深色西装泡在油腻的洗涤水里 sh iy hv ae dcl jh axr dcl d aa r kcl s ux q en gcl g r iy s ix w aa sh q w aa dx axr q aa l y ix axr
>
> *she had your dark suit in greasy wash water all year sh iy hv ae dcl jh axr dcl d aa r kcl s ux q en gcl g r iy s ix w aa sh q w aa dx axr q aa l y ix axr*
<!--/figbox-->

*图 15.2 来自 TIMIT 语料库的语音转写，使用特殊的 ARPAbet 特征进行窄式转写，例如 had 中 [d] 的腭化、dark 末尾塞音的不除阻、suit 末尾 [t] 喉化为 [q]，以及 water 中 [t] 的闪音。TIMIT 语料库还包含时间对齐信息（图中未显示）。*
*Figure 15.2 Phonetic transcription from the TIMIT corpus, using special ARPAbet features for narrow transcription, such as the palatalization of [d] in had, unreleased final stop in dark, glottalization of final [t] in suit to [q], and flap of [t] in water. The TIMIT corpus also includes time-alignments (not shown).*

Switchboard 转写项目所建立的语音标注语料库包含

> The Switchboard Transcription Project phonetically annotated corpus consists
从 Switchboard 语料库中抽取的 3.5 小时句子（Greenberg et al., 1996），并附有在音节层面时间对齐的转写。图 15.3 给出一个例子。

> of 3.5 hours of sentences extracted from the Switchboard corpus (Greenberg et al., 1996), together with transcriptions time-aligned at the syllable level. Figure 15.3 shows an example .

<!--figbox-->
> 0.470 0.640 0.720 0.900 0.953 1.279 1.410 1.630 dh er k aa n ax v ih m b ix t w iy n r ay n aw
<!--/figbox-->

*图 15.3 Switchboard 短语 they’re kind of in between right now 的语音转写。注意 they’re 和 of 中的元音弱化、kind 和 right 中的音节尾脱落，以及重新音节划分（of 的 [v] 附着为 in 的音节首）。时间以从句子开始到每个音节起点的秒数表示。*
*Figure 15.3 Phonetic transcription of the Switchboard phrase they’re kind of in between right now. Note vowel reduction in they’re and of, coda deletion in kind and right, and resyllabification (the [v] of of attaches as the onset of in). Time is given in number of seconds from the beginning of sentence to the start of each syllable.*

Buckeye 语料库（Pitt et al. 2007, Pitt et al. 2005）是一个经语音转写的美国自然口语语料库，包含来自 40 位说话人的约 300,000 个词。其他语言也有经语音转写的语料库，包括德语的 Kiel 语料库，以及中国社会科学院转写的汉语普通话语料库（Li et al., 2000）。

> The Buckeye corpus (Pitt et al. 2007, Pitt et al. 2005) is a phonetically transcribed corpus of spontaneous American speech, containing about 300,000 words from 40 talkers. Phonetically transcribed corpora are also available for other languages, including the Kiel corpus of German and Mandarin corpora transcribed by the Chinese Academy of Social Sciences (Li et al., 2000).

## 15.2 发音语音学

> 15.2 Articulatory Phonetics

> `articulatory phonetics`（发音语音学）
>
> 释义：研究口腔、咽喉与鼻腔等器官如何调节来自肺部的气流、从而产生各个音子的学科分支。

发音语音学研究的是，这些音子如何在口腔、咽喉和鼻腔中的各个

> Articulatory phonetics is the study of how these phones are produced as the various
器官调节来自肺部的气流时被发出。

> organs in the mouth, throat, and nose modify the airflow from the lungs.

发音器官

> The Vocal Organs
图15.4展示了发音器官。声音由空气的快速运动产生。人类发出口语中大多数音的方式，是把空气从肺部经气管（windpipe，学名 trachea）排出，再经嘴或鼻送出体外。空气在穿过气管时经过喉（larynx），也就是通常所说的喉结或声匣。喉内有两片细小的肌肉皱褶，即声带（vocal folds，非专业场合常称 vocal cords），它们可以合拢，也可以分开。这两片皱褶之间的空隙称为声门。如果两片皱褶靠得很近（但并未紧贴闭合），那么当空气

> Figure 15.4 shows the organs of speech. Sound is produced by the rapid movement of air. Humans produce most sounds in spoken languages by expelling air from the lungs through the windpipe (technically, the trachea) and then out the mouth or nose. As it passes through the trachea, the air passes through the larynx, commonly known as the Adam’s apple or voice box. The larynx contains two small folds of muscle, the vocal folds (often referred to non-technically as the vocal cords), which can be moved together or apart. The space between these two folds is called the glottis. If the folds are close together (but not tightly closed), they will vibrate as air

> `glottis`（声门）
>
> 释义：两片声带之间的开口，气流由此通过；其开合状态决定所发出的音是否带声。

从它们中间通过时，它们就会振动；如果两片皱褶相距很远，就不会振动。声带合拢并振动时发出的音称为带声（浊音）；没有这种声带

> passes through them; if they are far apart, they won’t vibrate. Sounds made with the vocal folds together and vibrating are called voiced; sounds made without this vocal

> `voiced sound unvoiced sound`（带声、不带声）
>
> 释义：按声带是否合拢振动区分的两类音：合拢振动时发出的为带声（浊音），不振动的为不带声（清音）。

振动而发出的音称为不带声或清音。带声的音包括 [b]、[d]、[g]、

> cord vibration are called unvoiced or voiceless. Voiced sounds include [b], [d], [g],

![](images/15-phonetics-and-speech/fig_p4_0.png)

*图15.4 发音器官的侧视图。（图片来自 OpenStax University Physics，CC BY 4.0）*
*Figure 15.4 The vocal organs, shown in side view. (Figure from OpenStax University Physics, CC BY 4.0)*

[v]、[z] 以及英语的全部元音等等。不带声的音包括 [p]、[t]、[k]、[f]、[s] 等。

> [v], [z], and all the English vowels, among others. Unvoiced sounds include [p], [t],[k], [f], [s], and others.

气管以上的区域称为声道，它由口腔通道

> The area above the trachea is called the vocal tract; it consists of the oral tract
和鼻腔通道组成。空气离开气管后，可以从嘴或鼻排出体外。大多数音是空气通过口腔发出的。空气通过鼻腔发出的音称为鼻音；鼻音（如

> and the nasal tract. After the air leaves the trachea, it can exit the body through the mouth or the nose. Most sounds are made by air passing through the mouth. Sounds made by air passing through the nose are called nasal sounds; nasal sounds (like

> `nasal`（鼻音）
>
> 释义：软腭下降、气流经鼻腔流出并产生共鸣的辅音，如英语的 [m]、[n]、[ng]。

英语的 [m]、[n] 和 [ng]）同时把口腔通道和鼻腔通道用作共鸣腔。

> English [m], [n], and [ng]) use both the oral and nasal tracts as resonating cavities.

音子分为两大类：辅音和元音。这两类

> Phones are divided into two main classes: consonants and vowels. Both kinds

> `consonant vowel`（辅音与元音）
>
> 释义：音子的两大类别：前者发音时气流在通道中受到限制或阻断，后者阻碍较小、通常带声且更响亮持久。

音都是空气经口腔、咽喉或鼻腔运动而形成的。辅音是靠以某种方式限制或阻断气流发出的，可以带声，也可以不带声。元音的阻碍较少，通常带声，并且一般比辅音更响亮、持续更久。这些术语的专业用法与日常用法大体相同；[p]、[b]、[t]、[d]、[k]、[g]、[f]、[v]、[s]、[z]、[r]、[l] 等是辅音；[aa]、[ae]、[ao]、[ih]、[aw]、[ow]、[uw] 等是元音。半元音（如 [y] 和 [w]）兼有两者的部分性质；它们像元音一样带声，却又像辅音一样短促、成音节性较弱。

> of sounds are formed by the motion of air through the mouth, throat or nose. Consonants are made by restriction or blocking of the airflow in some way, and can be voiced or unvoiced. Vowels have less obstruction, are usually voiced, and are generally louder and longer-lasting than consonants. The technical use of these terms is much like the common usage; [p], [b], [t], [d], [k], [g], [f], [v], [s], [z], [r], [l], etc., are consonants; [aa], [ae], [ao], [ih], [aw], [ow], [uw], etc., are vowels. Semivowels (such as [y] and [w]) have some of the properties of both; they are voiced like vowels, but they are short and less syllabic like consonants.

辅音：发音部位

> Consonants: Place of Articulation
由于辅音是靠限制气流发出的，我们可以按

> Because consonants are made by restricting airflow, we can group them into classes

> `place of`（发音部位）
>
> 释义：辅音发音时气流受阻最明显的位置，如双唇、齿龈或软腭等处。

最大阻碍的位置，也就是按发音部位（图15.5）把它们分成若干类。

> by their point of maximum restriction, their place of articulation (Fig. 15.5).

> `articulation`（发音部位）
>
> 释义：气流通道中阻碍最剧烈之处；据此可把辅音分为双唇音、齿龈音、软腭音等类别。

唇音：主要阻碍由上下两唇合拢形成的辅音，其发音部位为双唇。英语中包括 possum 里的 [p]、bear 里的 [b] 和 marmot 里的 [m]。英语的唇齿辅音 [v] 和 [f]，是以下唇抵住上排牙齿、让气流从上齿间的缝隙通过而发出的。

> Labial: Consonants whose main restriction is formed by the two lips coming together have a bilabial place of articulation. In English these include [p] as in possum, [b] as in bear, and [m] as in marmot. The English labiodental consonants [v] and [f] are made by pressing the bottom lip against the upper row of teeth and letting the air flow through the space in the upper teeth.

> `labial`（唇音）
>
> 释义：由嘴唇参与形成主要阻碍的一类辅音，包括双唇音与唇齿音两种。

![](images/15-phonetics-and-speech/fig_p5_0.png)

*图15.5 英语的主要发音部位。*
*Figure 15.5 Major English places of articulation.*

齿音：把舌头抵住牙齿所发出的音是齿音。

> Dental: Sounds that are made by placing the tongue against the teeth are dentals.

> `dental`（齿音）
>
> 释义：舌尖抵住上齿或置于上下齿之间形成阻碍而发出的一类辅音，如英语的 [th]、[dh]。

英语中主要的齿音是 thing 中的 [th] 和 though 中的 [dh]，发音时把舌头置于牙齿后方，舌尖略微伸到上下齿之间。

> The main dentals in English are the [th] of thing and the [dh] of though, which are made by placing the tongue behind the teeth with the tip slightly between the teeth.

齿龈音：齿龈嵴（alveolar ridge）是口腔顶部紧靠上排

> Alveolar: The alveolar ridge is the portion of the roof of the mouth just behind the

> `alveolar`（齿龈音）
>
> 释义：舌尖抵住上齿后方的齿龈嵴形成阻碍而发出的一类辅音，如英语的 [s]、[z]、[t]、[d]。

牙齿的那一部分。大多数美国英语使用者发 [s]、[z]、[t]、[d] 这些音子时，都是把舌尖抵住齿龈嵴。coronal（舌冠音）一词常用来兼指齿音和齿龈音。

> upper teeth. Most speakers of American English make the phones [s], [z], [t], and [d] by placing the tip of the tongue against the alveolar ridge. The word coronal is often used to refer to both dental and alveolar.

硬腭音：口腔顶部（即腭）从齿龈嵴的后方

> Palatal: The roof of the mouth (the palate) rises sharply from the back of the

> `palatal`（硬腭音）
>
> 释义：舌面前部抬向硬腭形成阻碍而发出的一类辅音，如英语 yak 中的 [y]。

急剧向上隆起。腭齿龈音 [sh]（shrimp）、[ch]（china）、[zh]

> alveolar ridge. The palato-alveolar sounds [sh] (shrimp), [ch] (china), [zh]

> `palate`（腭）
>
> 释义：口腔的顶部，自齿龈嵴后方向后延伸，前部为硬腭，后部为可动的软腭。

（Asian）和 [jh]（jar）是舌叶抵住向上隆起的齿龈嵴后部发出的。yak 中的硬腭音 [y] 是舌面前部抬近腭部发出的。

> (Asian), and [jh] (jar) are made with the blade of the tongue against the rising back of the alveolar ridge. The palatal sound [y] of yak is made by placing the front of the tongue up close to the palate.

软腭音：软腭（velum，或称 soft palate）是位于口腔顶部最末端的

> Velar: The velum, or soft palate, is a movable muscular flap at the very back of the

> `velar`（软腭音）
>
> 释义：舌后部抵住软腭形成阻碍而发出的一类辅音，如英语的 [k]、[g]、[N]。

一块可动肌肉瓣。[k]（cuckoo）、[g]（goose）和 [N]（kingfisher）这些音，是把舌后部向上抵住软腭发出的。

> roof of the mouth. The sounds [k] (cuckoo), [g] (goose), and [N] (kingfisher) are made by pressing the back of the tongue up against the velum.

声门音：声门塞音 [q] 是通过关闭声门（把两片声带

> Glottal: The glottal stop [q] is made by closing the glottis (by bringing the vocal

> `glottal`（声门音）
>
> 释义：在声门处构成阻碍而发出的辅音，英语中的 [h] 即属此类。

声带合拢）。

> folds together).

辅音：发音方式

> Consonants: Manner of Articulation
辅音还可以按气流的阻碍方式加以区分，例如气流被完全阻断，或者只是部分受阻。这一特征称为

> Consonants are also distinguished by how the restriction in airflow is made, for example, by a complete stoppage of air or by a partial blockage. This feature is called

> `manner of articulation`（发音方式）
>
> 释义：辅音发音时气流受到阻碍或节制的方式，如塞音、擦音、近音等。

辅音的发音方式。把发音部位与发音方式结合

> the manner of articulation of a consonant. The combination of place and manner
起来，通常就足以唯一地确定一个辅音。以下是英语辅音的主要发音方式：

> of articulation is usually sufficient to uniquely identify a consonant. Following are the major manners of articulation for English consonants:

塞音是指气流在短时间内被完全阻断的辅音。

> A stop is a consonant in which airflow is completely blocked for a short time.

> `stop`（塞音）
>
> 释义：发音时气流被完全阻断、随后释放并爆发成声的辅音，如 [p]、[t]、[k]。

这种阻断之后，气流释放时会伴随一个爆发音。阻断的时段称为成阻，爆发的部分称为除阻。英语中既有 [b]、[d]、[g] 这样的带声塞音，也有 [p]、[t]、[k] 这样的不带声塞音。

> This blockage is followed by an explosive sound as the air is released. The period of blockage is called the closure, and the explosion is called the release. English has voiced stops like [b], [d], and [g] as well as unvoiced stops like [p], [t], and [k].

塞音也称为爆破音。

> Stops are also called plosives.

鼻音 [n]、[m] 和 [ng] 是通过降低软腭、让气流进入鼻腔而发出的。

> The nasal sounds [n], [m], and [ng] are made by lowering the velum and allowing air to pass into the nasal cavity.

> `nasal`（鼻音）
>
> 释义：软腭下降、气流经鼻腔流出并产生共鸣的辅音，如英语的 [m]、[n]、[ng]。

在擦音中，气流受到挤压，但并未被完全切断。由此产生的湍流

> In fricatives, airflow is constricted but not cut off completely. The turbulent

> `fricatives`（擦音）
>
> 释义：发音器官靠近形成窄缝，气流挤过时产生摩擦噪声的辅音。

气流会产生特征性的“嘶嘶”声。

> airflow that results from the constriction produces a characteristic “hissing” sound.

英语的唇齿擦音 [f] 和 [v] 是下唇抵住上齿、使气流受限制地从上齿间通过而发出的。

> The English labiodental fricatives [f] and [v] are produced by pressing the lower lip against the upper teeth, allowing a restricted airflow between the upper teeth.

齿擦音 [th] 和 [dh] 让气流从牙齿之间绕过舌头流出。齿龈擦音 [s] 和 [z] 是舌抵住齿龈、迫使气流从牙齿边缘通过而发出的。在齿龈腭擦音 [sh] 和 [zh] 中，舌面位于齿龈后部，迫使气流通过舌面形成的沟槽。音高较高的擦音（英语中的 [s]、[z]、[sh] 和 [zh]）称为咝音。紧随擦音之后出现的塞音称为塞擦音；英语中的 [ch]（chicken）和 [jh]（giraffe）即属此类。

> The dental fricatives [th] and [dh] allow air to flow around the tongue between the teeth. The alveolar fricatives [s] and [z] are produced with the tongue against the alveolar ridge, forcing air over the edge of the teeth. In the palato-alveolar fricatives[sh] and [zh], the tongue is at the back of the alveolar ridge, forcing air through a groove formed in the tongue. The higher-pitched fricatives (in English [s], [z], [sh] and [zh]) are called sibilants. Stops that are followed immediately by fricatives are called affricates; these include English [ch] (chicken) and [jh] (giraffe).

> `sibilants`（咝音）
>
> 释义：音高较高、带有尖锐嘶声的一类擦音，英语中如 [s]、[z]、[sh]、[zh]。

在近音中，两个发音器官彼此靠近，但还没有近到

> In approximants, the two articulators are close together but not close enough to

> `approximant`（近音）
>
> 释义：两个发音器官靠近但缝隙较宽，气流通过时不产生湍流噪声的辅音。

足以产生湍流气流的程度。英语的 [y]（yellow）中，舌面靠近上腭，但还没有近到产生擦音所特有的湍流。英语的 [w]（wood）中，舌根靠近软腭。

> cause turbulent airflow. In English [y] (yellow), the tongue moves close to the roof of the mouth but not close enough to cause the turbulence that would characterize a fricative. In English [w] (wood), the back of the tongue comes close to the velum.

美式 [r] 至少有两种形成方式：一种是仅将舌尖伸出并靠近硬腭，另一种是把整个舌体在硬腭附近拱起。[l] 是舌尖抵住齿龈或牙齿、舌的一侧或两侧放低让气流从上面通过而形成的。由于舌两侧下垂，[l] 被称为边音。

> American [r] can be formed in at least two ways; with just the tip of the tongue extended and close to the palate or with the whole tongue bunched up near the palate.[l] is formed with the tip of the tongue up against the alveolar ridge or the teeth, with one or both sides of the tongue lowered to allow air to flow over it. [l] is called a lateral sound because of the drop in the sides of the tongue.

闪音 [dx] 是舌尖对齿龈的快速一击。该

> A tap or flap [dx] is a quick motion of the tongue against the alveolar ridge. The

> `tap`（闪音）
>
> 释义：舌尖快速弹击齿龈一次而形成的短促辅音，如美式英语 lotus 中的 [dx]。

词 lotus（[l ow dx ax s]）中间的辅音在多数美式英语方言中是一个闪音；许多英国方言的使用者则会改用 [t]。

> consonant in the middle of the word lotus ([l ow dx ax s]) is a tap in most dialects of American English; speakers of many U.K. dialects would use a [t] instead.

元音

> Vowels
与辅音一样，元音也可以通过发音时发音器官的位置来刻画。与元音最相关的三个参数是：所谓的元音高度，它大致与舌位最高部分的高度相对应；元音的前后性，用来说明这个最高点是朝向口腔通道的前部还是后部；以及双唇的形状是否圆唇。图 15.6 显示了不同元音的舌位。

> Like consonants, vowels can be characterized by the position of the articulators as they are made. The three most relevant parameters for vowels are what is called vowel height, which correlates roughly with the height of the highest part of the tongue, vowel frontness or backness, indicating whether this high point is toward the front or back of the oral tract and whether the shape of the lips is rounded or not. Figure 15.6 shows the position of the tongue for different vowels.

![](images/15-phonetics-and-speech/fig_p6_0.png)

*图 15.6 英语高前元音 [iy]、低前元音 [ae] 与高后元音 [uw] 的舌位。*
*Figure 15.6 Tongue positions for English high front [iy], low front [ae] and high back [uw].*

例如在元音 [iy] 中，舌位的最高点朝向

> In the vowel [iy], for example, the highest point of the tongue is toward the
口腔前部。相反，在元音 [uw] 中，舌位最高点位于口腔后部。舌头向前方抬起的元音称为前元音；舌头向后方抬起的

> front of the mouth. In the vowel [uw], by contrast, the high-point of the tongue is located toward the back of the mouth. Vowels in which the tongue is raised toward the front are called front vowels; those in which the tongue is raised toward the

> `Front vowel back vowel`（前元音、后元音）
>
> 释义：按舌位最高点偏前还是偏后区分出的两类元音。

元音称为后元音。注意，虽然 [ih] 和 [eh] 都是前元音，

> back are called back vowels. Note that while both [ih] and [eh] are front vowels,
但 [ih] 的舌位比 [eh] 更高。舌位最高点相对较高的元音称为高元音；舌位最高点处于中等或较低位置的

> the tongue is higher for [ih] than for [eh]. Vowels in which the highest point of the tongue is comparatively high are called high vowels; vowels with mid or low values

> `high vowel`（高元音）
>
> 释义：发音时舌位最高点抬得较高、接近上腭的元音，如 [iy]、[uw]。

元音则分别称为中元音或低元音。

> of maximum tongue height are called mid vowels or low vowels, respectively.

图 15.7 示意性地刻画了不同元音的高度。

> Figure 15.7 shows a schematic characterization of the height of different vowels.

之所以说是示意性的，是因为高度这一抽象属性只与实际的舌位大致对应；事实上，它更准确地反映的是声学事实。注意该图中有两类元音：一类把舌位高度表示为一个点，另一类则表示为一条路径。发音过程中舌位发生明显变化的元音是双元音。En-

> It is schematic because the abstract property height correlates only roughly with actual tongue positions; it is, in fact, a more accurate reflection of acoustic facts. Note that the chart has two kinds of vowels: those in which tongue height is represented as a point and those in which it is represented as a path. A vowel in which the tongue position changes markedly during the production of the vowel is a diphthong. En-

> `diphthong`（双元音）
>
> 释义：发音过程中舌位发生明显变化、在元音图中表示为一条路径而非单一点的元音；英语中的双元音尤其丰富。

![](images/15-phonetics-and-speech/fig_p7_0.png)

*图 15.7 英语元音的示意性“元音空间”。*
*Figure 15.7 The schematic “vowel space” for English vowels.*

英语中的双元音尤其丰富。

> glish is particularly rich in diphthongs.

元音的第二个重要发音维度是唇的形状。

> The second important articulatory dimension for vowels is the shape of the lips.

某些元音发音时双唇收圆（即吹口哨时所用的唇形）。这些圆唇元音包括 [uw]、[ao] 和 [ow]。

> Certain vowels are pronounced with the lips rounded (the same lip shape used for whistling). These rounded vowels include [uw], [ao], and [ow].

> `rounded vowel`（圆唇元音）
>
> 释义：发音时双唇收圆的元音，如英语中的 [uw]、[ao]、[ow]。

音节

> Syllables
辅音与元音组合起来构成音节。音节是一个类元音（或

> Consonants and vowels combine to make a syllable. A syllable is a vowel-like (or

> `syllable`（音节）
>
> 释义：由一个响音性的音（通常是元音）加上与之联系最紧密的周围辅音构成的最小发音单位。

响音）的音，加上周围与它联系最紧密的一些辅音。在我们的方言中，dog 一词只有一个音节 [d aa g]；catnip 一词有两个音节，[k ae t] 和 [n ih p]。我们把处于音节核心的元音称为音节核。位于其前的辅音（如果有的话）称为音节首。音节首

> sonorant) sound together with some of the surrounding consonants that are most closely associated with it. The word dog has one syllable, [d aa g] (in our dialect); the word catnip has two syllables, [k ae t] and [n ih p]. We call the vowel at the core of a syllable the nucleus. Initial consonants, if any, are called the onset. Onsets

> `nucleus`（音节核）
>
> 释义：音节中以元音为核心的成分，是音节必有的部分，如 dog 中的 [aa]。

包含一个以上辅音的音节首（如 strike [s t r ay k] 中的情形）称为复杂音节首。

> with more than one consonant (as in strike [s t r ay k]), are called complex onsets.

> `onset`（音节首）
>
> 释义：音节核之前的一个或一串辅音，如 dog 中的 [d]；含多个辅音时称为复杂音节首。

音节尾是跟在音节核之后可选的一个辅音或一串辅音。

> The coda is the optional consonant or sequence of consonants following the nucleus.

> `coda`（音节尾）
>
> 释义：音节核之后的辅音成分，可以没有，如 dog 中的 [g]。

因此 [d] 是 dog 的音节首，[g] 是音节尾。韵基（rime，或作 rhyme）是音节核

> Thus [d] is the onset of dog, and [g] is the coda. The rime, or rhyme, is the nucleus

> `rime`（韵基）
>
> 释义：音节中由音节核加音节尾构成的整体，也就是押韵时相互对应的那一部分。

加音节尾。图 15.8 给出了一些音节结构的示例。

> plus coda. Figure 15.8 shows some sample syllable structures.

![](images/15-phonetics-and-speech/fig_p7_1.png)

*图 15.8 ham、green、eggs 的音节结构。σ＝音节。*
*Figure 15.8 Syllable structure of ham, green, eggs. σ=syllable.*

把词自动切分为音节的任务称为音节划分。音节结构还与语言的音位配列（phonotactics）密切相关。

> The task of automatically breaking up a word into syllables is called syllabification. Syllable structure is also closely related to the phonotactics of a language. The

> `syllabification phonotactics`（音节划分；音位配列）
>
> 释义：前者指把词自动切分为音节的处理任务，后者指一种语言中允许哪些音子相邻出现的组合限制。

术语音位配列指的是对一种语言中哪些音子可以彼此跟随出现

> term phonotactics means the constraints on which phones can follow each other in
的限制。例如，英语对哪些种类的辅音可以一起出现在音节首有很强的限制；比如 [zdr] 这一序列就不能成为合法的英语音节首。音位配列可以用音子序列的语言模型或有限状态模型来表示。

> a language. For example, English has strong constraints on what kinds of consonants can appear together in an onset; the sequence [zdr], for example, cannot be a legal English syllable onset. Phonotactics can be represented by a language model or finite-state model of phone sequences.

## 15.3 韵律

> 15.3 Prosody

韵律是对语言中语调与节奏方面的研究，尤其

> Prosody is the study of the intonational and rhythmic aspects of language, and in

> `prosody`（韵律）
>
> 释义：研究语言语调与节奏等超音段层面的分支，关注如何用 F0、能量和时长传达意义。

是运用 F0、能量和时长来传达语用、情感或会话互动方面的意义。1 这些声学量我们将在下一节转向声学语音学时详细介绍，这里可以简单地把能量理解为被我们感知为响度的声学属性，把 F0 理解为所产生声音的频率，也就是我们听成话语音高的声学属性。韵律可以用来标记话语结构，比如陈述与疑问的差别，或者一次会话是如何组织的。韵律用来标记某个词或短语的显著性。韵律在副语言功能中大量使用，例如传达高兴、惊讶或愤怒等情感意义。而韵律在管理会话中的话轮转换方面起着重要作用。

> particular the use of F0, energy, and duration to convey pragmatic, affective, or conversation-interactional meanings.1 We’ll introduce these acoustic quantities in detail in the next section when we turn to acoustic phonetics, but briefly we can think of energy as the acoustic quality that we perceive as loudness, and F0 as the frequency of the sound that is produced, the acoustic quality that we hear as the pitch of an utterance. Prosody can be used to mark discourse structure, like the difference between statements and questions, or the way that a conversation is structured. Prosody is used to mark the saliency of a particular word or phrase. Prosody is heavily used for paralinguistic functions like conveying affective meanings like happiness, surprise, or anger. And prosody plays an important role in managing turn-taking in conversation.

### 15.3.1 韵律突显：重读、词重音与央元音 schwa

> 15.3.1 Prosodic Prominence: Accent, Stress and Schwa

在美式英语的自然话语中，有些词听起来比

> In a natural utterance of American English, some words sound more prominent than

> `prominence`（突显）
>
> 释义：指某个音节或词在语流中被听者感知为比周围成分更突出的程度，由重音、音高和音长等因素共同决定。

另一些词更突显，而这些词中的某些音节也比其他音节更突显。

> others, and certain syllables in these words are also more prominent than others.

我们所说的突显，是指这些词或音节在听者感知上更为显著。在英语中，说话人通过把词或音节说得更响、说得更慢（因而时长更长），或在说这个词时改变 F0、使其更高或更富于变化，来使它更显著。

> What we mean by prominence is that these words or syllables are perceptually more salient to the listener. Speakers make a word or syllable more salient in English by saying it louder, saying it slower (so it has a longer duration), or by varying F0 during the word, making it higher or more variable.

重读 我们通过一种称为音高重音的语言学标记来表示突显。突显的词

> Accent We represent prominence via a linguistic marker called pitch accent. Words

> `pitch accent`（音高重音）
>
> 释义：标记突显的语言学符号；被突显的词或音节被说成承载一个音高重音。

或音节如果突显，就说它承载（关联）一个音高重音。

> or syllables that are prominent are said to bear (be associated with) a pitch accent.

因此这句话可以靠重读带下划线的词来读出：(15.1) 听到它被说成是快乐的，我有点吃惊。

> Thus this utterance might be pronounced by accenting the underlined words:(15.1) I’m a little surprised to hear it characterized as happy.

词重音 承载音高重音的音节称为重读音节。

> Lexical Stress The syllables that bear pitch accent are called accented syllables.

并非一个词的每个音节都能被重读：音高重音必须落在带有词重音的那个音节上。词重音是词典中标注的词读音属性；带有词重音的音节就是当该词被重读时会读得更响或更长的那个音节。例如，surprised 一词的重音在其第二个音节上，而非第一个音节上。（试着把重音放到另一个音节上，说成 SURprised；希望你听起来觉得不对。）因此，如果 surprised 一词在句中带上了音高重音，读得更强的就是第二个音节。下面的示例给出带下划线的重读词，其中承载重音的音节（更响、更长的音节）用粗体标出：(15.2) 听到它被说成是快乐的，我有点吃惊。

> Not every syllable of a word can be accented: pitch accent has to be realized on the syllable that has lexical stress. Lexical stress is a property of the word’s pronunciation in dictionaries; the syllable that has lexical stress is the one that will be louder or longer if the word is accented. For example, the word surprised is stressed on its second syllable, not its first. (Try stressing the other syllable by saying SURprised; hopefully that sounds wrong to you). Thus, if the word surprised receives a pitch accent in a sentence, it is the second syllable that will be stronger. The following example shows underlined accented words with the stressed syllable bearing the accent(the louder, longer syllable) in boldface:(15.2) I’m a little surprised to hear it characterized as happy.

> `lexical stress`（词重音）
>
> 释义：词典中标注的词内重音性质，决定该词被重读时哪个音节读得更响或更长。

重音在词典中会标注出来。例如 CMU 词典（CMU, 1993）用 0（非重读）或 1（重读）标注元音，如 counter 的词条：[K AW1 N T ER0]，或 table：[T EY1 B AH0 L]。词重音的差别会影响词义；名词 content 读作 [K AA1 N T EH0 N T]，而形容词读作 [K AA0 N T EH1 N T]。

> Stress is marked in dictionaries. The CMU dictionary (CMU, 1993), for example, marks vowels with 0 (unstressed) or 1 (stressed) as in entries for counter:[K AW1 N T ER0], or table: [T EY1 B AH0 L]. Difference in lexical stress can affect word meaning; the noun content is pronounced [K AA1 N T EH0 N T], while the adjective is pronounced [K AA0 N T EH1 N T].

> 该词在诗学中有一种不同但相关的用法，指对诗句格律结构的研究。
>
> *The word is used in a different but related way in poetry, to mean the study of verse metrical structure.*

弱化元音与央元音 schwa 非重读元音还可以进一步弱化为弱化元音，其中最常见的是央元音 schwa（[ax]），如第二个元音

> Reduced Vowels and Schwa Unstressed vowels can be weakened even further to reduced vowels, the most common of which is schwa ([ax]), as in the second vowel

> `reduced vowel schwa`（弱化元音 schwa）
>
> 释义：重读程度降低后音质向中央位置靠拢的元音，其发音动作不如完整元音到位，英语中常记为 schwa。

parakeet 一词的发音：[p ae r ax k iy t]。在弱化元音中，发音动作不像

> of parakeet: [p ae r ax k iy t]. In a reduced vowel the articulatory gesture isn’t as
完整元音那样到位。并非所有非重读元音都会弱化；任何元音，尤其是双元音，即使在非重读位置上也能保持其完整音质。例如，元音 [iy] 既可以出现在重读位置上，如单词 eat [iy t]，也可以出现在非重读位置上，如单词 carry [k ae r iy]。

> complete as for a full vowel. Not all unstressed vowels are reduced; any vowel, and diphthongs in particular, can retain its full quality even in unstressed position. For example, the vowel [iy] can appear in stressed position as in the word eat [iy t] or in unstressed position as in the word carry [k ae r iy].

总之，韵律突显构成一个连续统，对此往往

> In summary, there is a continuum of prosodic prominence, for which it is often

> `prominence`（突显）
>
> 释义：指某个音节或词在语流中被听者感知为比周围成分更突出的程度，由重音、音高和音长等因素共同决定。

有必要区分诸如带重音、重读、完整元音和弱化元音这样的等级。

> useful to represent levels like accented, stressed, full vowel, and reduced vowel.

### 15.3.2 韵律结构

> 15.3.2 Prosodic Structure

口语句子具有韵律结构：有些词似乎自然地归为一组，而有些词之间则似乎存在明显的停顿或间断，

> Spoken sentences have prosodic structure: some words seem to group naturally together, while some words seem to have a noticeable break or disjuncture between

> `prosodic`（韵律的）
>
> 释义：与语音的节奏、重音和语调组织有关的，描述的是超出单个音段层面之上的语音结构。

将其分开。韵律结构通常用韵律短语切分来描述，即一个话语具有韵律短语结构，就像它具有句法短语结构一样。例如，句子 I wanted to go to London，

> them. Prosodic structure is often described in terms of prosodic phrasing, meaning that an utterance has a prosodic phrase structure in a similar way to it having a syntactic phrase structure. For example, the sentence I wanted to go to London,

> `phrasing`（短语切分）
>
> 释义：指把连续语流切分成若干短语单位的方式，这些边界可由停顿、音高变化和音节延长等线索标示。

> `intonation phrase`（语调短语）
>
> 释义：韵律层级中较大的单位，通常与一条完整的语调曲线相对应，其末尾带有边界调。

but could only get tickets for France 似乎包含两个主要的语调短语，

> but could only get tickets for France seems to have two main intonation phrases,
二者的边界出现在逗号处。此外，在第一个短语内部，似乎还存在一组层级较低的韵律短语边界（通常称为中间

> their boundary occurring at the comma. Furthermore, in the first phrase, there seems to be another set of lesser prosodic phrase boundaries (often called intermediate

> `intermediate phrase`（中间短语）
>
> 释义：比语调短语更小的韵律单位，其边界处出现较弱的停顿或音高变化，用于把语调短语进一步切分。

短语），它们把词语切分为 I wanted | to go | to London。这类

> phrases) that split up the words as I wanted | to go | to London. These kinds of
语调短语往往与句法结构成分相互对应（Price et al. 1991, Bennett and Elfner 2019）。

> intonation phrases are often correlated with syntactic structure constituents (Price et al. 1991, Bennett and Elfner 2019).

自动预测韵律边界对于诸如

> Automatically predicting prosodic boundaries can be important for tasks like
TTS 这类任务来说可能很重要。现代方法使用序列模型，其输入或是原始文本，或是标注了句法分析树等特征的文本，并在每个词边界处作出停顿/不停顿的判定。这类模型可以用标注了韵律结构的数据来训练，例如波士顿大学广播新闻语料库（Ostendorf et al., 1995）。

> TTS. Modern approaches use sequence models that take either raw text or text annotated with features like parse trees as input, and make a break/no-break decision at each word boundary. They can be trained on data labeled for prosodic structure like the Boston University Radio News Corpus (Ostendorf et al., 1995).

### 15.3.3 调型

> 15.3.3 Tune

两个具有相同突显和短语切分模式的话语，仍可因调型不同而在韵律上存在差异。一个话语的调型是指其

> Two utterances with the same prominence and phrasing patterns can still differ prosodically by having different tunes. The tune of an utterance is the rise and

> `tune`（调型）
>
> 释义：指话语音高随时间升降所形成的整体曲线模式，用于区分陈述、疑问等不同的语句功能。

F0 随时间的升降变化。调型的一个非常明显的例子是英语中陈述句与一般疑问句之间的差别。同样的一些词可以说成句末 F0 上升以表示一般疑问句（称为疑问升调）：

> fall of its F0 over time. A very obvious example of tune is the difference between statements and yes-no questions in English. The same words can be said with a final F0 rise to indicate a yes-no question (called a question rise):

> `question rise`（疑问升调）
>
> 释义：一般疑问句末尾音高上升的调型，用来标示说话人期待对方作出是或否的回答。

> 你知道我的意思吗 ？
>
> *You know what I mean ?*

也可以说成句末 F0 下降（称为句末降调），以表示陈述语调：

> or a final drop in F0 (called a final fall) to indicate a declarative intonation:

> `final fall`（句末降调）
>
> 释义：语调短语末尾音高下降的调型，通常用于陈述句，标示话语的结束。

> 你知道我的意思 。
>
> *You know what I mean .*

各种语言都广泛利用调型来表达意义（Xu, 2005）。在英语中，

> Languages make wide use of tune to express meaning (Xu, 2005). In English,
例如，除了上述一般疑问句的这一为人熟知的升调之外，包含由逗号隔开的名词列举的短语，往往在每个名词之后带有一个简短的升调，称为

> for example, besides this well-known rise for yes-no questions, a phrase containing a list of nouns separated by commas often has a short rise called a continuation

> `continuation rise`（延续升调）
>
> 释义：在列举或并列成分尚未结束时出现的短升调，提示听者话语还要继续下去。

延续升调。其他例子还包括英语中用于

> rise after each noun. Other examples include the characteristic English contours for
表达反驳和表达惊讶的典型音高曲线。

> expressing contradiction and expressing surprise.

联结突显与调型

> Linking Prominence and Tune
音高重音有多种类型，它们与调型相关；例如，高音高重音与低音高重音的功能不同。不同语言中有许多重音类别的分类体系。其中一种分类体系是语调的 ToBI（Tone and Break Indices，音高与间断指数）理论的组成部分（Silverman et al. 1992）。每个

> Pitch accents come in different varieties that are related to tune; high pitched accents, for example, have different functions than low pitched accents. There are many typologies of accent classes in different languages. One such typology is part of the ToBI (Tone and Break Indices) theory of intonation (Silverman et al. 1992). Each

> `ToBI`
>
> 释义：一种标注语调与韵律结构的理论框架，用音高重音、短语重音和边界调等符号描述话语的音高曲线，并标注各成分间的间断等级。

词在 ToBI 中都可以与图 15.9 所示的五种音高重音之一相联系。ToBI 中的每个话语由一串语调短语组成，其中每个语调短语都以图 15.9 所示的四种边界调之一结尾，用以表示

> word in ToBI can be associated with one of five types of pitch accents shown in Fig. 15.9. Each utterance in ToBI consists of a sequence of intonational phrases, each of which ends in one of four boundary tones shown in Fig. 15.9, representing

> `boundary tone`（边界调）
>
> 释义：出现在韵律短语末尾的音高目标，用来标示短语边界，并贡献话语末尾的调型信息。

调型在话语末尾方面的特征。许多语言都有各自版本的 ToBI。

> the utterance final aspects of tune. There are version of ToBI for many languages.

<!--figbox-->
> 音高重音　边界调
>
> *Pitch Accents Boundary Tones*

> H* 峰值重音 L-L%“句末下降”：美式的“陈述句调型”
>
> *H* peak accent L-L% “final fall”: “declarative contour” of American*

> 英语
>
> *English*

> L* 低重音 L-H% 延续上升 L*+H 勺形重音 H-H%“疑问上升”：典型的是非问句
>
> *L* low accent L-H% continuation rise L*+H scooped accent H-H% “question rise”: cantonical yes-no question*

> 调型
>
> *contour*

> L+H* 上升峰值重音 H-L% 句末持平 H+!H* 阶梯下降
>
> *L+H* rising peak accent H-L% final level plateau H+!H* step down*
<!--/figbox-->

*图 15.9 美式英语语调的 ToBI 转写系统中的重音调与边界调标签（Beckman and Ayers 1997, Beckman and Hirschberg 1994）。*
*Figure 15.9 The accent and boundary tones labels from the ToBI transcription system for American English intonation (Beckman and Ayers 1997, Beckman and Hirschberg 1994).*

## 15.4 声学语音学与信号

> 15.4 Acoustic Phonetics and Signals

我们先非常简要地介绍声学波形及其数字化与频率分析；有兴趣的读者可参阅本章末尾的参考文献。

> We begin with a very brief introduction to the acoustic waveform and its digitization and frequency analysis; the interested reader is encouraged to consult the references at the end of the chapter.

### 15.4.1 波

> 15.4.1 Waves

声学分析以正弦函数和余弦函数为基础。图 15.10 画出的是一条正弦波，具体来说就是下面这个函数

> Acoustic analysis is based on the sine and cosine functions. Figure 15.10 shows a plot of a sine wave, in particular the function
y = A∗sin(2π ft) (15.3)
其中我们把振幅 A 设为 1，把频率 f 设为每秒 10 个周期。

> where we have set the amplitude A to 1 and the frequency f to 10 cycles per second.

![](images/15-phonetics-and-speech/fig_p10_0.png)

*图 15.10 频率为 10 Hz、振幅为 1 的正弦波。*
*Figure 15.10 A sine wave with a frequency of 10 Hz and an amplitude of 1.*

回顾基础数学可知，波的两个重要特征是

> Recall from basic mathematics that two important characteristics of a wave are
它的频率和振幅。频率是波每秒重复自身的次数，也就是周期数。我们通常以每秒周期数来度量频率。图 15.10 中的信号在 0.5 秒内重复 5 次，因而是每秒 10 个周期。每秒周期数通常称为赫兹（简称为 Hz），因此图 15.10 中的频率可描述为 10 Hz。正弦波的振幅 A 是 Y 轴上的最大值。波的周期 T 是一个循环完成所需的时间，定义为

> its frequency and amplitude. The frequency is the number of times a second that a wave repeats itself, that is, the number of cycles. We usually measure frequency in cycles per second. The signal in Fig. 15.10 repeats itself 5 times in .5 seconds, hence 10 cycles per second. Cycles per second are usually called hertz (shortened to Hz), so the frequency in Fig. 15.10 would be described as 10 Hz. The amplitude A of a sine wave is the maximum value on the Y axis. The period T of the wave is the time it takes for one cycle to complete, defined as

> `frequency`（频率）
>
> 释义：波在单位时间内重复的次数，单位为赫兹（Hz）；语音中多数有用信息都在 10,000 Hz 以下。

> `amplitude`（振幅）
>
> 释义：正弦波在 Y 轴上的最大值，表示压强偏离常态的最大幅度；振幅越高，声音听起来越响。

> `Hertz`（赫兹）
>
> 释义：频率的单位，表示每秒重复的周期数，语音学中用来度量声音信号的频率高低。

> `period`（周期）
>
> 释义：波完成一个完整循环所需的时间，其数值等于频率的倒数。

T = 1 (15.4)
f
图 15.10 中每个周期持续十分之一秒；因此 T = 0.1 秒。

> Each cycle in Fig. 15.10 lasts a tenth of a second; hence T = .1 seconds.

### 15.4.2 语音声波

> 15.4.2 Speech Sound Waves

让我们从假想的波转向声波。语音识别器的输入与人耳的输入一样，是一系列复杂的气压变化。

> Let’s turn from hypothetical waves to sound waves. The input to a speech recognizer, like the input to the human ear, is a complex series of changes in air pressure.

这些空气压力变化显然源自说话人，是由空气通过声门、再经口腔或鼻腔流出的特定方式造成的。我们通过在时间轴上绘制空气压力的变化来表示声波。

> These changes in air pressure obviously originate with the speaker and are caused by the specific way that air passes through the glottis and out the oral or nasal cavities. We represent sound waves by plotting the change in air pressure over time.

有一种比喻有时有助于理解这些图形，即设想一块垂直的板挡住空气压力波（也许是说话人嘴前麦克风里的板，或者是听者耳中的鼓膜）。图形测量的是这块板处空气分子的压缩或稀疏（非压缩）量。

> One metaphor which sometimes helps in understanding these graphs is that of a vertical plate blocking the air pressure waves (perhaps in a microphone in front of a speaker’s mouth, or the eardrum in a hearer’s ear). The graph measures the amount of compression or rarefaction (uncompression) of the air molecules at this plate.

图 15.11 显示了取自电话语音 Switchboard 语料库的一小段波形，是某人说“she just had a baby”时元音 [iy] 的波形。

> Figure 15.11 shows a short segment of a waveform taken from the Switchboard corpus of telephone speech of the vowel [iy] from someone saying “she just had a baby”.

![](images/15-phonetics-and-speech/fig_p11_0.png)

*图 15.11 元音 [iy] 的波形，该话语见后文第 342 页的图 15.15。y 轴表示高于和低于正常大气压的气压水平。x 轴表示时间。*
*Figure 15.11 A waveform of the vowel [iy] from an utterance shown later in Fig. 15.15 on page 342. The y-axis shows the level of air pressure above and below normal atmospheric pressure. The x-axis shows time.*

> 注意，该波有规律地重复。
>
> *Notice that the wave repeats regularly.*

把像图 15.11 这样的声波数字化的第一步，是把模拟

> The first step in digitizing a sound wave like Fig. 15.11 is to convert the analog
表示（先是空气压力，然后是麦克风中的模拟电信号）转换成数字信号。这种模数转换有两个步骤：采样和

> representations (first air pressure and then analog electric signals in a microphone) into a digital signal. This analog-to-digital conversion has two steps: sampling and

> `sampling`（采样）
>
> 释义：按固定时间间隔测量模拟信号的振幅并记录数值，从而把连续信号变成离散的样本序列。

量化。要对一个信号采样，我们在特定的时刻测量它的振幅；采样率是每秒采集的样本数。要准确地测量一个波，每个周期至少要有两个样本：一个测量波的正半部分，一个测量负半部分。每个周期的样本多于两个会提高振幅的准确度，但少于两个就会完全漏掉该波的频率。因此，能够被测量的最高频率的波，其频率是采样率的一半（因为每个周期都需要两个样本）。给定采样率下的这个最高频率被称为

> quantization. To sample a signal, we measure its amplitude at a particular time; the sampling rate is the number of samples taken per second. To accurately measure a wave, we must have at least two samples in each cycle: one measuring the positive part of the wave and one measuring the negative part. More than two samples per cycle increases the amplitude accuracy, but fewer than two samples causes the frequency of the wave to be completely missed. Thus, the maximum frequency wave that can be measured is one whose frequency is half the sample rate (since every cycle needs two samples). This maximum frequency for a given sampling rate is

> `Nyquist frequency`（奈奎斯特频率）
>
> 释义：给定采样率下能够正确测量到的最高频率，数值等于采样率的一半。

奈奎斯特频率。人类语音中的大部分信息都位于

> called the Nyquist frequency. Most information in human speech is in frequencies
低于 10,000 Hz 的频率范围内；因此，要达到完全的准确度就需要 20,000 Hz 的采样率。但电话语音经过交换网络的滤波，电话只传输低于 4,000 Hz 的频率。因此，对于像 Switchboard 语料库这样的电话带宽语音，8,000 Hz 的采样率已经足够，而麦克风语音通常使用 16,000 Hz 的采样。

> below 10,000 Hz; thus, a 20,000 Hz sampling rate would be necessary for complete accuracy. But telephone speech is filtered by the switching network, and only frequencies less than 4,000 Hz are transmitted by telephones. Thus, an 8,000 Hz sampling rate is sufficient for telephone-bandwidth speech like the Switchboard corpus, while 16,000 Hz sampling is often used for microphone speech.

即使是 8,000 Hz 的采样率，每

> Even an 8,000 Hz sampling rate requires 8000 amplitude measurements for each
秒语音也需要 8000 次振幅测量，因此高效地存储振幅测量值很重要。

> second of speech, so it is important to store amplitude measurements efficiently.

它们通常以整数形式存储，或用 8 位（取值范围 -128–127），或用 16 位（取值范围 -32768–32767）。这种把实数值表示为整数的过程称为量化，因为两个整数之间的差充当

> They are usually stored as integers, either 8 bit (values from -128–127) or 16 bit(values from -32768–32767). This process of representing real-valued numbers as integers is called quantization because the difference between two integers acts as

> `quantization`（量化）
>
> 释义：把连续的实数值振幅近似为有限个整数值的过程，差距小于量化步长的取值会被表示成同一个数。

存在一个最小粒度（量子大小），凡是彼此差距小于该量子大小的取值，都会被表示成完全相同的形式。

> a minimum granularity (a quantum size) and all values that are closer together than this quantum size are represented identically.

数据一旦被量化，就会以各种格式存储。这些格式的一个参数

> Once data is quantized, it is stored in various formats. One parameter of these
格式就是上面讨论过的采样率和样本大小；电话语音通常以 8 kHz 采样并存储为 8 位样本，而麦克风数据通常以 16 kHz 采样并存储为 16 位样本。另一个参数是声道数。对于立体声数据或双方对话，我们可以把两个声道

> formats is the sample rate and sample size discussed above; telephone speech is often sampled at 8 kHz and stored as 8-bit samples, and microphone data is often sampled at 16 kHz and stored as 16-bit samples. Another parameter is the number of channels. For stereo data or for two-party conversations, we can store both channels

> `channel`（通道）
>
> 释义：此处指梅尔滤波器组中单个滤波器的输出数值，代表某一梅尔频带的对数能量。

存放在同一个文件里，也可以把它们存放在不同的文件里。最后一个参数是单个样本的存储方式——线性存储还是压缩存储。电话语音常用的一种压缩格式是 µ-law（常写作 u-law，但读音仍是 mu-law）。像 µ-law 这样的对数压缩算法的直觉依据是：人耳对小强度声音比对大强度声音更敏感；对数表示对小数值的保真度更高，代价是在大数值上误差更大。未经对数变换的线性值通常称为线性 PCM 值（PCM 是脉冲编码

> in the same file or we can store them in separate files. A final parameter is individual sample storage—linearly or compressed. One common compression format used for telephone speech is µ-law (often written u-law but still pronounced mu-law). The intuition of log compression algorithms like µ-law is that human hearing is more sensitive at small intensities than large ones; the log represents small values with more faithfulness at the expense of more error on large values. The linear (unlogged) values are generally referred to as linear PCM values (PCM stands for pulse code

> `PCM`
>
> 释义：脉冲编码调制，即把模拟语音按固定的采样率和量化精度转成数字样本的最基本编码方式。

调制，不过不必在意这一点）。下面是把线性 PCM 样本值 x 压缩成 8 位 µ-law 的公式（8 位时 µ=255）：

> modulation, but never mind that). Here’s the equation for compressing a linear PCM sample value x to 8-bit µ-law, (where µ=255 for 8 bits):

F(x) = sgn(x)log(1+ µ|x|)
−1 ≤x ≤1 (15.5)
log(1+ µ)
存储数字化后得到的波形文件有多种标准文件格式，例如微软的 .wav 和苹果的 AIFF，它们都带有特殊的文件头；此外也使用简单的、不带文件头的“裸”（raw）文件。例如，.wav 格式是微软面向多媒体文件的 RIFF 格式的一个子集；RIFF 是一种通用格式，能够表示一系列相互嵌套的数据块与控制信息块。图 15.12 展示了一个只含单个数据块的简单 .wav 文件，以及它的格式块。

> There are a number of standard file formats for storing the resulting digitized wavefile, such as Microsoft’s .wav and Apple’s AIFF all of which have special headers; simple headerless “raw” files are also used. For example, the .wav format is a subset of Microsoft’s RIFF format for multimedia files; RIFF is a general format that can represent a series of nested chunks of data and control information. Figure 15.12 shows a simple .wav file with a single data chunk together with its format chunk.

![](images/15-phonetics-and-speech/fig_p12_0.png)

*图 15.12 微软波形文件的文件头格式，假设是只含一个数据块的简单文件。紧跟在这个 44 字节文件头之后的将是数据块。*
*Figure 15.12 Microsoft wavefile header format, assuming simple file with one chunk. Following this 44-byte header would be the data chunk.*

### 15.4.3 频率与振幅；音高与响度

> 15.4.3 Frequency and Amplitude; Pitch and Loudness

声波和所有波一样，可以用频率、振幅以及我们前面针对纯正弦波介绍过的其他特征来描述。对声波来说，这些量并不像对正弦波那样容易测量。先看频率。注意图 15.11 中，这段波虽然并非严格的正弦波，但仍然是周期性的，在图中所截取的 38.75 毫秒（0.03875 秒）内重复了 10 次。因此，这段波的频率是 10/0.03875，即 258 Hz。

> Sound waves, like all waves, can be described in terms of frequency, amplitude, and the other characteristics that we introduced earlier for pure sine waves. In sound waves, these are not quite as simple to measure as they were for sine waves. Let’s consider frequency. Note in Fig. 15.11 that although not exactly a sine, the wave is nonetheless periodic, repeating 10 times in the 38.75 milliseconds (.03875 seconds) captured in the figure. Thus, the frequency of this segment of the wave is 10/.03875 or 258 Hz.

这个周期性的 258 Hz 波从何而来？它来自

> Where does this periodic 258 Hz wave come from? It comes from the speed
声带振动的速度；由于图 15.11 的波形来自元音 [iy]，因此它是带声的。回想一下，带声是由声带有规律的开启与闭合造成的。声带张开时，气流从肺部向上推出，形成一个高压区。声带闭合时，肺部不再产生压力。因此，当声带振动时，我们预期会看到图 15.11 中那种规律性的振幅峰值，每个主要峰值对应声带的一次张开。声带振动的频率，或者说

> of vibration of the vocal folds; since the waveform in Fig. 15.11 is from the vowel[iy], it is voiced. Recall that voicing is caused by regular openings and closing of the vocal folds. When the vocal folds are open, air is pushing up through the lungs, creating a region of high pressure. When the folds are closed, there is no pressure from the lungs. Thus, when the vocal folds are vibrating, we expect to see regular peaks in amplitude of the kind we see in Fig. 15.11, each major peak corresponding to an opening of the vocal folds. The frequency of the vocal fold vibration, or the

> `fundamental frequency F0`（基频 F0）
>
> 释义：声带振动即复合波重复的速率，等于波形周期的倒数，也是人耳感知到的音高的物理基础。

复合波的频率，称为该波形的基频，通常缩写为 F0。我们可以在音高轨迹中把 F0 随时间的变化画出来。图 15.13

> frequency of the complex wave, is called the fundamental frequency of the waveform, often abbreviated F0. We can plot F0 over time in a pitch track. Figure 15.13
展示了一个简短问句“Three o’clock?”的音高轨迹，该轨迹被绘制在

> shows the pitch track of a short question, “Three o’clock?” represented below the

> `pitch track`（音高轨迹）
>
> 释义：把基频 F0 随时间的变化画成的一条曲线，用来直观呈示一句话的音高走向。

波形的下方。注意问句末尾 F0 的上升。

> waveform. Note the rise in F0 at the end of the question.

![](images/15-phonetics-and-speech/fig_p13_0.png)

*图 15.13 问句“Three o’clock?”的音高轨迹，显示在波形文件下方。注意问句末尾 F0 的上升。注意在非常安静的部分（“o’clock”中的“o’”）缺少音高曲线；自动音高跟踪基于对带声区域内脉冲的计数，若没有带声（或声音不足）就无法工作。*
*Figure 15.13 Pitch track of the question “Three o’clock?”, shown below the wavefile. Note the rise in F0 at the end of the question. Note the lack of pitch trace during the very quiet part(the “o’” of “o’clock”; automatic pitch tracking is based on counting the pulses in the voiced regions, and doesn’t work if there is no voicing (or insufficient sound).*

图 15.11 的纵轴衡量气压变化的幅度；

> The vertical axis in Fig. 15.11 measures the amount of air pressure variation;

压强是单位面积上的力，以帕斯卡（Pa）为单位。纵轴上的高值（高振幅）表示该时刻的气压高于常态，零值表示气压为正常（大气）压强，负值表示气压低于正常大气压（稀疏）。

> pressure is force per unit area, measured in Pascals (Pa). A high value on the vertical axis (a high amplitude) indicates that there is more air pressure at that point in time, a zero value means there is normal (atmospheric) air pressure, and a negative value means there is lower than normal air pressure (rarefaction).

除了任意时刻的振幅取值之外，我们还常常

> In addition to this value of the amplitude at any point in time, we also often
需要知道某个时间范围内的平均振幅，以便大致了解气压的平均偏移有多大。但我们不能直接对该范围内的振幅取值求平均；正值与负值会（大部分）相互抵消，最终得到一个接近零的数值。因此，我们通常使用 RMS（均方根）振幅，它先把每个数值平方之后再求平均（使其为正），最后再取平方根。

> need to know the average amplitude over some time range, to give us some idea of how great the average displacement of air pressure is. But we can’t just take the average of the amplitude values over a range; the positive and negative values would (mostly) cancel out, leaving us with a number close to zero. Instead, we generally use the RMS (root-mean-square) amplitude, which squares each number before averaging (making it positive), and then takes the square root at the end.

v u
u t 1 X
RMS amplitudeN i=1 = x2 (15.6)
N
信号的功率与振幅的平方有关。若一段声音的样本数为 N，则功率为

> The power of the signal is related to the square of the amplitude. If the number of samples of a sound is N, the power is

> N

> i

> `power`（功率）
>
> 释义：信号振幅平方的均值，反映声音所含能量的多少；书中把它相对于人耳听阈归一化，得到以分贝度量的强度。

> N

Power = 1 X
x2 (15.7)
N
比起功率，我们更常提到声音的强度，它

> Rather than power, we more often refer to the intensity of the sound, which

> i

> i=1

> `intensity`（强度）
>
> 释义：声音能量的对数量度，以人耳听阈为参考进行归一化，单位为分贝，其峰值常用来定位音节核。

它把功率相对于人耳听阈进行归一化，并以 dB 为单位度量。若 P0 为听阈声压（即 2×10−5 Pa），则强度定义如下：

> normalizes the power to the human auditory threshold and is measured in dB. If P0 is the auditory threshold pressure (which is 2×10−5 Pa), then intensity is defined as follows:

> N

1 X
Intensity = 10log10 x2 (15.8)
NP0
图 15.14 给出了句子“Is it a long movie?”的强度曲线，该句取自

> Figure 15.14 shows an intensity plot for the sentence “Is it a long movie?” from
CallHome 语料库，同样绘制在波形图的下方。

> the CallHome corpus, again shown below the waveform plot.

> i

> i=1

![](images/15-phonetics-and-speech/fig_p14_0.png)

*图 15.14 句子“Is it a long movie?”的强度曲线。注意每个元音处都出现强度峰值，而单词 long 处的峰值尤其高。*
*Figure 15.14 Intensity plot for the sentence “Is it a long movie?”. Note the intensity peaks at each vowel and the especially high peak for the word long.*

两个重要的感知属性，即音高与响度，分别与频率和强度相关。声音的音高是一种心理感觉，或者说是一种感知

> Two important perceptual properties, pitch and loudness, are related to frequency and intensity. The pitch of a sound is the mental sensation, or perceptual

> `pitch`（音高）
>
> 释义：人耳对声音基频高低的主观感受属性，基频越高听感越高，二者的关系并不线性。

对应量，它对应于基频；一般来说，如果一个声音的基频更高，我们感知到的音高也更高。我们说“一般来说”，是因为这一关系并不是线性的，人耳对不同频率的分辨能力并不相同。粗略地说，人类的音高感知在 100 Hz 到 1000 Hz 之间最为准确，在这个范围内音高与频率呈线性相关。人耳对 1000 Hz 以上的频率表征得不太准确，超过这一范围后，音高与频率呈对数相关。对数表征意味着高频之间的差异被压缩，因而感知得不够准确。关于音高感知尺度，存在多种心理声学模型。一种常见的模型是梅尔刻度（Stevens et al. 1937，Stevens and

> correlate, of fundamental frequency; in general, if a sound has a higher fundamental frequency we perceive it as having a higher pitch. We say “in general” because the relationship is not linear, since human hearing has different acuities for different frequencies. Roughly speaking, human pitch perception is most accurate between 100 Hz and 1000 Hz and in this range pitch correlates linearly with frequency. Human hearing represents frequencies above 1000 Hz less accurately, and above this range, pitch correlates logarithmically with frequency. Logarithmic representation means that the differences between high frequencies are compressed and hence not as accurately perceived. There are various psychoacoustic models of pitch perception scales. One common model is the mel scale (Stevens et al. 1937, Stevens and

> `Mel`（梅尔）
>
> 释义：用以刻画音高主观感知的单位：凡听感上等距的两个音高，其数值之差也相等。

Volkmann 1940）。mel 是音高的单位，其定义方式为：在感知上音高距离相等的若干对声音，其间隔的 mel 数也相等。mel 频率 m 可由原始声学频率计算得到，公式如下：

> Volkmann 1940). A mel is a unit of pitch defined such that pairs of sounds which are perceptually equidistant in pitch are separated by an equal number of mels. The mel frequency m can be computed from the raw acoustic frequency as follows:

f
m = 1127ln(1+ 700) (15.9)
正如我们将在第 16 章看到的，梅尔刻度在语音

> As we’ll see in Chapter 16, the mel scale plays an important role in speech
识别中起着重要作用。

> recognition.

声音的响度是功率的感知对应量。因此，

> The loudness of a sound is the perceptual correlate of the power. So sounds with
振幅更高的声音听起来更响，但这一关系同样不是线性的。

> higher amplitudes are perceived as louder, but again the relationship is not linear.

首先，正如我们在定义 µ-law 压缩时提到的，人类在低功率范围内具有更高的分辨率；耳朵对微小的功率差异更为敏感。其次，功率、频率与感知响度之间存在复杂的关系；处于某些频率范围内的声音听起来比其他频率范围内的声音更响。

> First of all, as we mentioned above when we defined µ-law compression, humans have greater resolution in the low-power range; the ear is more sensitive to small power differences. Second, it turns out that there is a complex relationship between power, frequency, and perceived loudness; sounds in certain frequency ranges are perceived as being louder than those in other frequency ranges.

存在多种用于自动提取 F0 的算法。这些算法在术语上略有借用，被称为音高提取算法。自相关方法

> Various algorithms exist for automatically extracting F0. In a slight abuse of terminology, these are called pitch extraction algorithms. The autocorrelation method

> `pitch extraction`（音高提取）
>
> 释义：从语音信号中自动估计基频 F0 的一类算法，因沿用音高一词命名而与实际三者的关系略有出入。

例如，音高提取的自相关方法把信号与在不同偏移量下的自身做相关。

> of pitch extraction, for example, correlates the signal with itself at various offsets.

相关性最高的那个偏移量即为信号的周期。有多种公开可用的音高提取工具包；例如，Praat 就提供了一个增强的自相关音高跟踪器（Boersma and Weenink, 2005）。

> The offset that gives the highest correlation gives the period of the signal. There are various publicly available pitch extraction toolkits; for example, an augmented autocorrelation pitch tracker is provided with Praat (Boersma and Weenink, 2005).

### 15.4.4 从波形解读音子

> 15.4.4 Interpretation of Phones from a Waveform

仅凭对波形的目视检查就能获得很多信息。例如，元音非常容易辨认。回想一下，元音是带声的；元音的另一个特点是它们往往较长，而且相对较响（正如我们在图 15.14 的强度曲线中看到的那样）。时间上的长度直接体现在 x 轴上，而响度则与 y 轴上的振幅（的平方）相关。我们在上一节看到，带声表现为图 15.11 中那种规则的振幅峰值，每个主要峰值都对应一次声带的张开。图 15.15 给出了短句“she just had a baby”的波形。我们为这个波形标注了单词标签和音子标签。注意图 15.15 中的六个元音 [iy]、[ax]、[ae]、[ax]、[ey]、[iy] 都具有规则的振幅峰值，表明它们是带声的。

> Much can be learned from a visual inspection of a waveform. For example, vowels are pretty easy to spot. Recall that vowels are voiced; another property of vowels is that they tend to be long and are relatively loud (as we can see in the intensity plot in Fig. 15.14). Length in time manifests itself directly on the x-axis, and loudness is related to (the square of) amplitude on the y-axis. We saw in the previous section that voicing is realized by regular peaks in amplitude of the kind we saw in Fig. 15.11, each major peak corresponding to an opening of the vocal folds. Figure 15.15 shows the waveform of the short sentence “she just had a baby”. We have labeled this waveform with word and phone labels. Notice that each of the six vowels in Fig. 15.15, [iy], [ax], [ae], [ax], [ey], [iy], all have regular amplitude peaks indicating voicing.

![](images/15-phonetics-and-speech/fig_p15_0.png)

*图 15.15 取自 Switchboard 语料库（对话 4325）的句子“She just had a baby”的波形。说话人为女性，1991 年时 20 岁，录音大约就在那前后完成，她说的是美国英语的南中部方言。*
*Figure 15.15 A waveform of the sentence “She just had a baby” from the Switchboard corpus (conversation 4325). The speaker is female, was 20 years old in 1991, which is approximately when the recording was made, and speaks the South Midlands dialect of American English.*

对于塞音，它由闭塞段后接除阻段构成，我们

> For a stop consonant, which consists of a closure followed by a release, we can
常常能看到一段静音或近乎静音，随后是一小段振幅的爆发。

> often see a period of silence or near silence followed by a slight burst of amplitude.

在图 15.15 中，baby 里的两个 [b] 都能看到这一现象。

> We can see this for both of the [b]’s in baby in Fig. 15.15.

在波形中往往也很容易辨认的另一种音子是擦音。回想一下，擦音，尤其是像 [sh] 这样非常刺耳的擦音，是在气流通道狭窄、导致空气产生噪声性湍流时发出的。由此产生的嘶嘶声具有噪声性的、不规则的波形。这一点在图 15.15 中已隐约可见；在图 15.16 中更加清楚，那里我们只放大了第一个单词 she。

> Another phone that is often quite recognizable in a waveform is a fricative. Recall that fricatives, especially very strident fricatives like [sh], are made when a narrow channel for airflow causes noisy, turbulent air. The resulting hissy sounds have a noisy, irregular waveform. This can be seen somewhat in Fig. 15.15; it’s even clearer in Fig. 15.16, where we’ve magnified just the first word she.

![](images/15-phonetics-and-speech/fig_p16_0.png)

*图 15.16 从图 15.15 的波形文件中抽取的第一个单词“she”的更细致视图。注意擦音 [sh] 的随机噪声与元音 [iy] 的规则带声之间的差别。*
*Figure 15.16 A more detailed view of the first word “she” extracted from the wavefile in Fig. 15.15. Notice the difference between the random noise of the fricative [sh] and the regular voicing of the vowel [iy].*

### 15.4.5 频谱与频域

> 15.4.5 Spectra and the Frequency Domain

虽然一些粗略的语音特征（如能量、音高，以及是否带声、是否有塞音闭塞段或擦音）可以直接从波形中解读出来，但大多数计算应用，例如语音识别（以及人类的听觉加工），都基于声音的另一种表示方式，即按组成频率来表示。傅里叶分析的核心洞见是，任何复杂波都可以表示成许多不同频率正弦波之和。考察图 15.17 中的波形。该波形是在 Praat 中把两个正弦波形相加得到的，其中一个频率为 10 Hz，另一个频率为 100 Hz。

> While some broad phonetic features (such as energy, pitch, and the presence of voicing, stop closures, or fricatives) can be interpreted directly from the waveform, most computational applications such as speech recognition (as well as human auditory processing) are based on a different representation of the sound in terms of its component frequencies. The insight of Fourier analysis is that every complex wave can be represented as a sum of many sine waves of different frequencies. Consider the waveform in Fig. 15.17. This waveform was created (in Praat) by summing two sine waveforms, one of frequency 10 Hz and one of frequency 100 Hz.

![](images/15-phonetics-and-speech/fig_p16_1.png)

*图 15.17 由两个正弦波形相加得到的波形，一个频率为 10 Hz（注意它在这半秒窗口内重复了五次），另一个频率为 100 Hz，二者的振幅均为 1。*
*Figure 15.17 A waveform that is the sum of two sine waveforms, one of frequency 10 Hz (note five repetitions in the half-second window) and one of frequency 100 Hz, both of amplitude 1.*

我们可以用频谱来表示这两个组成频率。信号的频谱是对其各个频率成分及其振幅的表示。图 15.18 给出了图 15.17 的频谱。x 轴是频率（Hz），y 轴是振幅。注意图中的两个尖峰，一个在 10 Hz，一个在 100 Hz。因此，频谱是原始波形的另一种表示方式，我们借助频谱这一工具来研究某一特定时刻声波的组成频率。

> We can represent these two component frequencies with a spectrum. The spectrum of a signal is a representation of each of its frequency components and their amplitudes. Figure 15.18 shows the spectrum of Fig. 15.17. Frequency in Hz is on the x-axis and amplitude on the y-axis. Note the two spikes in the figure, one at 10 Hz and one at 100 Hz. Thus, the spectrum is an alternative representation of the original waveform, and we use the spectrum as a tool to study the component frequencies of a sound wave at a particular time point.

> `spectrum`（频谱）
>
> 释义：把信号表示为其各个组成频率及相应幅值的方式，用于考察某一时刻声音的频率构成。

现在我们来看语音波形的频率成分。图 15.19

> Let’s look now at the frequency components of a speech waveform. Figure 15.19
给出了单词 had 中元音 [ae] 的部分波形，它是从图 15.15 所示的句子中截取出来的。

> shows part of the waveform for the vowel [ae] of the word had, cut out from the sentence shown in Fig. 15.15.

注意，图中有一条复合波重复了约十次；但

> Note that there is a complex wave that repeats about ten times in the figure; but
其中还包含一条更小的重复波，它在每个较大的重复模式内重复四次（注意每个重复波内部都有四个小峰）。这条复合波的频率约为 234 Hz（我们可以推算出来，因为它大约重复了 10 次

> there is also a smaller repeated wave that repeats four times for every larger pattern(notice the four small peaks inside each repeated wave). The complex wave has a frequency of about 234 Hz (we can figure this out since it repeats roughly 10 times

![](images/15-phonetics-and-speech/fig_p17_1.png)

*图 15.18 图 15.17 中波形的频谱。*
*Figure 15.18 The spectrum of the waveform in Fig. 15.17.*

![](images/15-phonetics-and-speech/fig_p17_2.png)

*图 15.19 从图 15.15 所示波形中截取的单词 had 中元音 [ae] 的部分波形。*
*Figure 15.19 The waveform of part of the vowel [ae] from the word had cut out from the waveform shown in Fig. 15.15.*

在 .0427 秒内，且 10 个周期/.0427 秒 = 234 Hz）。

> in .0427 seconds, and 10 cycles/.0427 seconds = 234 Hz).

那么这条较小的波的频率应约为较大波频率的四倍，即大约 936 Hz。接着，如果仔细观察，你会发现许多 936 Hz 波的波峰上都还有两个小波。这条最小波的频率必然约为 936 Hz 波的两倍，因此是 1872 Hz。

> The smaller wave then should have a frequency of roughly four times the frequency of the larger wave, or roughly 936 Hz. Then, if you look carefully, you can see two little waves on the peak of many of the 936 Hz waves. The frequency of this tiniest wave must be roughly twice that of the 936 Hz wave, hence 1872 Hz.

图 15.20 给出了图 15.19 中波形的平滑频谱，它是用离散傅里叶变换（DFT）计算得到的。

> Figure 15.20 shows a smoothed spectrum for the waveform in Fig. 15.19, computed with a discrete Fourier transform (DFT).

![](images/15-phonetics-and-speech/fig_p17_0.png)

*图 15.20 图 15.15 中句子 She just had a baby 的波形里单词 had 的元音 [ae] 的频谱。*
*Figure 15.20 A spectrum for the vowel [ae] from the word had in the waveform of She just had a baby in Fig. 15.15.*

频谱的横轴表示频率，纵轴表示对各个频率成分幅值的某种度量（以分贝（dB）为单位，即我们前面见过的振幅的对数度量）。因此，图 15.20 显示出在约 930 Hz、1860 Hz 和 3020 Hz 处有显著的频率成分，此外还有许多幅值更低的频率成分。前两个成分正是我们在时域中观察图 15.19 的波形时所注意到的！

> The x-axis of a spectrum shows frequency, and the y-axis shows some measure of the magnitude of each frequency component (in decibels (dB), a logarithmic measure of amplitude that we saw earlier). Thus, Fig. 15.20 shows significant frequency components at around 930 Hz, 1860 Hz, and 3020 Hz, along with many other lower-magnitude frequency components. These first two components are just what we noticed in the time domain by looking at the wave in Fig. 15.19!

为什么频谱有用？事实证明，这些在频谱中很容易

> Why is a spectrum useful? It turns out that these spectral peaks that are easily
看到的谱峰是不同音子的特征；音子具有特征性的频谱“签名”。正如化学元素燃烧时会发出不同波长的光，使我们能够通过观察光的频谱来探测恒星中的元素，我们也可以通过观察波形的频谱来检测不同音子的特征签名。这种对频谱信息的利用对人类的语音识别和机器的语音识别都至关重要。在人类听觉中，耳蜗（即内耳）的功能就是计算传入波形的频谱。

> visible in a spectrum are characteristic of different phones; phones have characteris- tic spectral “signatures”. Just as chemical elements give off different wavelengths of light when they burn, allowing us to detect elements in stars by looking at the spectrum of the light, we can detect the characteristic signature of the different phones by looking at the spectrum of a waveform. This use of spectral information is essential to both human and machine speech recognition. In human audition, the function of the cochlea, or inner ear, is to compute a spectrum of the incoming waveform.

> `cochlea`（耳蜗）
>
> 释义：内耳中形状如蜗壳的器官，能把传入的声波按频率分解，相当于对声音做实时的频谱分析。

类似地，语音识别中使用的声学特征就是频谱表示。

> Similarly, the acoustic features used in speech recognition are spectral representations.

我们来看看不同元音的频谱。由于有些元音会随着

> Let’s look at the spectrum of different vowels. Since some vowels change over
时间发生变化，我们改用另一种图形，称为语谱图。频谱显示的是一段波在某一时刻的频率成分，而语谱图则是

> time, we’ll use a different kind of plot called a spectrogram. While a spectrum shows the frequency components of a wave at one point in time, a spectrogram is a

> `spectrogram`（语谱图）
>
> 释义：以横轴表示时间、纵轴表示频率、明暗表示振幅的图像，用来观察各频率成分随时间的变化。

一种用来呈现构成波形的各个频率如何随时间变化的方式。横轴表示时间，与波形图一样，但纵轴现在以赫兹表示频率。语谱图上某一点的深浅对应频率成分的振幅。颜色很深的点振幅高，浅的点振幅低。因此，语谱图是把三个维度（时间 × 频率 × 振幅）可视化的有用方式。

> way of envisioning how the different frequencies that make up a waveform change over time. The x-axis shows time, as it did for the waveform, but the y-axis now shows frequencies in hertz. The darkness of a point on a spectrogram corresponds to the amplitude of the frequency component. Very dark points have high amplitude, light points have low amplitude. Thus, the spectrogram is a useful way of visualizing the three dimensions (time x frequency x amplitude).

图 15.21 显示了三个美式英语元音 [ih]、[ae]

> Figure 15.21 shows spectrograms of three American English vowels, [ih], [ae],
和 [uh] 的语谱图。注意，每个元音都在不同频带上呈现一组深色条带，各元音的频带略有差异。其中每一条都代表我们在图 15.19 中见到的那种谱峰。

> and [uh]. Note that each vowel has a set of dark bars at various frequency bands, slightly different bands for each vowel. Each of these represents the same kind of spectral peak that we saw in Fig. 15.19.

![](images/15-phonetics-and-speech/fig_p18_0.png)

*图 15.21 三个美式英语元音 [ih]、[ae] 和 [uh] 的语谱图*
*Figure 15.21 Spectrograms for three American English vowels, [ih], [ae], and [uh]*

每一条深色条带（或称谱峰）称为共振峰。正如我们将在下文讨论的，

> Each dark bar (or spectral peak) is called a formant. As we discuss below, a

> `formant`（共振峰）
>
> 释义：声道对声源频谱中某些频段特别加强而形成的谱峰，前两个共振峰的位置是区分元音的主要依据。

共振峰就是被声道特别放大的某个频带。由于不同元音发音时声道的位置不同，它们会产生不同类型的放大或共振。我们来看前两个共振峰，称为 F1 和 F2。注意，F1 是最靠近底部的深色条带，它在三个元音中的位置各不相同：对 [ih] 来说较低（中心约在 470 Hz），对 [ae] 和 [uh] 则稍高（约在 800 Hz 附近）。相比之下，F2 是从底部数第二条深色条带，它在 [ih] 中最高，在 [ae] 中居中，在 [uh] 中最低。

> formant is a frequency band that is particularly amplified by the vocal tract. Since different vowels are produced with the vocal tract in different positions, they will produce different kinds of amplifications or resonances. Let’s look at the first two formants, called F1 and F2. Note that F1, the dark bar closest to the bottom, is in a different position for the three vowels; it’s low for [ih] (centered at about 470 Hz) and somewhat higher for [ae] and [uh] (somewhere around 800 Hz). By contrast, F2, the second dark bar from the bottom, is highest for [ih], in the middle for [ae], and lowest for [uh].

在连续语流中我们也能看到同样的共振峰，尽管弱化和

> We can see the same formants in running speech, although the reduction and
协同发音过程使它们多少更难看清。图 15.22 显示了“she just had a baby”的语谱图，其波形见图 15.15。

> coarticulation processes make them somewhat harder to see. Figure 15.22 shows the spectrogram of “she just had a baby”, whose waveform was shown in Fig. 15.15.

在 just 的 [ax]、had 的 [ae] 和 baby 的 [ey] 中，F1 和 F2（以及 F3）都相当清晰。

> F1 and F2 (and also F3) are pretty clear for the [ax] of just, the [ae] of had, and the[ey] of baby.

频谱表示能为音子识别提供哪些具体的线索？

> What specific clues can spectral representations give for phone identification?

首先，由于不同元音的共振峰位于各自特有的位置，频谱可以把元音彼此区分开来。我们已经看到，示例波形中 [ae] 的共振峰位于 930 Hz、1860 Hz 和 3020 Hz。再来看元音 [iy]，它位于

> First, since different vowels have their formants at characteristic places, the spectrum can distinguish vowels from each other. We’ve seen that [ae] in the sample waveform had formants at 930 Hz, 1860 Hz, and 3020 Hz. Consider the vowel [iy] at the

![](images/15-phonetics-and-speech/fig_p19_0.png)

*图 15.22 句子“she just had a baby”的语谱图，其波形见图 15.15。*
*Figure 15.22 A spectrogram of the sentence “she just had a baby” whose waveform was shown in Fig. 15.15.*

> 我们可以把语谱图看作一系列频谱（时间切片）的集合，就像把许多幅图 15.20 首尾相接排在一起。
>
> *We can think of a spectrogram as a collection of spectra (time slices), like Fig. 15.20 placed end to end.*

图 15.15 中该话语的开头。这个元音的频谱见图 15.23。[iy] 的第一共振峰是 540 Hz，远低于 [ae] 的第一共振峰，而第二共振峰（2581 Hz）则远高于 [ae] 的第二共振峰。如果仔细观察，你能在图 15.22 中约 0.5 秒处看到这些共振峰表现为深色条带。

> beginning of the utterance in Fig. 15.15. The spectrum for this vowel is shown in Fig. 15.23. The first formant of [iy] is 540 Hz, much lower than the first formant for[ae], and the second formant (2581 Hz) is much higher than the second formant for[ae]. If you look carefully, you can see these formants as dark bars in Fig. 15.22 just around 0.5 seconds.

![](images/15-phonetics-and-speech/fig_p19_1.png)

*图 15.23 She just had a baby 起始处元音 [iy] 的平滑（LPC）频谱。注意，其第一共振峰（540 Hz）远低于图 15.20 中 [ae] 的第一共振峰，第二共振峰（2581 Hz）则远高于 [ae] 的第二共振峰。*
*Figure 15.23 A smoothed (LPC) spectrum for the vowel [iy] at the start of She just had a baby. Note that the first formant (540 Hz) is much lower than the first formant for [ae] shown in Fig. 15.20, and the second formant (2581 Hz) is much higher than the second formant for[ae].*

前两个共振峰（称为 F1 和 F2）的位置在确定元音身份上起很大作用，尽管共振峰仍会因说话人而异。

> The location of the first two formants (called F1 and F2) plays a large role in determining vowel identity, although the formants still differ from speaker to speaker.

较高的共振峰更多是由说话人声道的整体特征造成的，而不是由具体的元音造成的。共振峰还可以用来识别鼻音音子 [n]、[m]、[ng] 以及流音 [l] 和 [r]。

> Higher formants tend to be caused more by general characteristics of a speaker’s vocal tract rather than by individual vowels. Formants also can be used to identify the nasal phones [n], [m], and [ng] and the liquids [l] and [r].

### 15.4.6 源-滤波器模型

> 15.4.6 The Source-Filter Model

为什么不同元音具有不同的频谱签名？正如上文简要提到的，共振峰是由口腔的共振腔造成的。源-滤波器模型是一种通过建模来解释声音声学特性的方法，它描述的是

> Why do different vowels have different spectral signatures? As we briefly mentioned above, the formants are caused by the resonant cavities of the mouth. The sourcefilter model is a way of explaining the acoustics of a sound by modeling how the

> `source-filter model`（源-滤波器模型）
>
> 释义：把语音视为声门产生的周期性脉冲（源）经声道（滤波器）塑造频谱而形成的声学解释模型。

声门产生的脉冲（源）如何被声道（滤波器）塑形。

> pulses produced by the glottis (the source) are shaped by the vocal tract (the filter).

我们来看看这是如何运作的。每当我们有一个波，例如空气的振动

> Let’s see how this works. Whenever we have a wave such as the vibration in air
由声门脉冲引起时，这个波也同样具有谐波。谐波是另一种

> caused by the glottal pulse, the wave also has harmonics. A harmonic is another

> `harmonic`（谐波）
>
> 释义：频率为基波频率整数倍的波；声带脉冲产生的复杂波可分解为一系列这样的分量。

波，其频率是基波的整数倍。因此，举例来说，115 Hz 的声带振动会产生 230 Hz、345 Hz、460 Hz 等谐波（其他波）。一般来说，这些波中的每一个都会更弱，也就是说，其振幅比基频处的波小得多。

> wave whose frequency is a multiple of the fundamental wave. Thus, for example, a 115 Hz glottal fold vibration leads to harmonics (other waves) of 230 Hz, 345 Hz, 460 Hz, and so on on. In general, each of these waves will be weaker, that is, will have much less amplitude than the wave at the fundamental frequency.

然而结果表明，声道起到一种滤波器或放大器的作用；

> It turns out, however, that the vocal tract acts as a kind of filter or amplifier;

事实上，任何空腔，例如一根管子，都会使某些频率的波被放大，而使另一些被衰减。这种放大过程是由空腔的形状造成的；某个特定的形状会使某一频率的声音发生共振，从而被放大。因此，通过改变空腔的形状，我们就能使不同的频率得到放大。

> indeed any cavity, such as a tube, causes waves of certain frequencies to be amplified and others to be damped. This amplification process is caused by the shape of the cavity; a given shape will cause sounds of a certain frequency to resonate and hence be amplified. Thus, by changing the shape of the cavity, we can cause different frequencies to be amplified.

当我们发出特定的元音时，本质上就是在改变

> When we produce particular vowels, we are essentially changing the shape of
声道空腔的形状，办法是把舌头和其他发音器官摆在特定的位置上。结果是，不同的元音会使不同的谐波被放大。因此，同一基频的波通过不同的声道位置，会导致不同的谐波被放大。

> the vocal tract cavity by placing the tongue and the other articulators in particular positions. The result is that different vowels cause different harmonics to be amplified. So a wave of the same fundamental frequency passed through different vocal tract positions will result in different harmonics being amplified.

通过考察声道形状

> We can see the result of this amplification by looking at the relationship between
与相应频谱之间的关系，我们可以看到这种放大的结果。图 15.24 展示了三个元音的声道位置以及由此得到的典型频谱。共振峰是频谱中声道恰好放大某些谐波频率的位置。

> the shape of the vocal tract and the corresponding spectrum. Figure 15.24 shows the vocal tract position for three vowels and a typical resulting spectrum. The formants are places in the spectrum where the vocal tract happens to amplify particular harmonic frequencies.

![](images/15-phonetics-and-speech/fig_p20_0.png)

*图 15.24 把声道位置可视化为滤波器：三个英语元音的舌头位置，以及由此得到的、显示 F1 与 F2 的平滑频谱。*
*Figure 15.24 Visualizing the vocal tract position as a filter: the tongue positions for three English vowels and the resulting smoothed spectra showing F1 and F2.*

## 15.5 用于语音识别的特征提取：对数

> 15.5 Feature Extraction for Speech Recognition: Log

## 梅尔频谱

> Mel Spectrum

我们用来分析波形声学语音学的那些工具，也常常被用作语音处理算法的输入。本节介绍一条信号处理流水线，它常被用作自动语音识别（ASR）等任务的一部分，我们将在第 16 章看到。语音处理的第一步通常是把输入波形转换成一个声学特征向量序列，每个向量表示信号中某个短时间窗内的信息。有时语音识别或语音处理算法会直接从波形入手，在这种情况下，该处理由我们将在第 16 章介绍的卷积网络（convnet）完成。

> The same tools that we used to analyze the acoustic phonetics of the waveforms are also often used as inputs to speech processing algorithms. In this section we introduce a signal processing pipeline that is often used as part of tasks like automatic speech recognition (ASR), as we will see in Chapter 16. The first step in speech processing is often to transform the input waveform into a sequence of acoustic fea- ture vectors, each vector representing the information in a small time window of the signal. Sometimes speech recognition or processing algorithms will start with the waveform, in which case that processing is done by the convolutional networks(convnets) that we will introduce in Chapter 16.

> `feature vector`（特征向量）
>
> 释义：用一串数值概括信号在某个短时窗内声学信息的向量，是语音处理算法的基本输入单位。

另一些系统则从更高的层次开始，即对数梅尔频谱。因此，

> Other systems begin instead at a higher level, with the log mel spectrum. So in
本节我们介绍这种常用的特征向量：对数梅尔频谱向量序列。在下一节中，我们将介绍另一种向量，即 MFCC 表示。我们将以相对高层的视角介绍这些概念；如需更多细节，建议修读一门语音信号处理课程。

> this section we introduce this commonly used feature vector: sequences of log mel spectrum vectors. In the following section we’ll introduce an alternative vector, the MFCC representation. We’ll introduce these concepts at a relatively high level; a speech signal processing course is recommended for more details.

我们首先重复第 15.4.2 节中关于模拟语音波形的数字化与量化过程。

> We begin by repeating from Section 15.4.2 the process of digitizing and quantizing an analog speech waveform.

### 15.5.1 采样与量化

> 15.5.1 Sampling and Quantization

语音识别器的输入是一系列复杂的空气压力变化。

> The input to a speech recognizer is a complex series of changes in air pressure.

这些空气压力变化显然源自说话人，是由空气通过声门、再经口腔或鼻腔流出的特定方式造成的。我们通过在时间轴上绘制空气压力的变化来表示声波。

> These changes in air pressure obviously originate with the speaker and are caused by the specific way that air passes through the glottis and out the oral or nasal cavities. We represent sound waves by plotting the change in air pressure over time.

有一种比喻有时有助于理解这些图形，即设想一块垂直的板挡住空气压力波（也许是说话人嘴前麦克风里的板，或者是听者耳中的鼓膜）。图形测量的是这块板处空气分子的压缩或稀疏（非压缩）量。

> One metaphor which sometimes helps in understanding these graphs is that of a vertical plate blocking the air pressure waves (perhaps in a microphone in front of a speaker’s mouth, or the eardrum in a hearer’s ear). The graph measures the amount of compression or rarefaction (uncompression) of the air molecules at this plate.

图 15.25（重复自图 15.11）显示了取自 Switchboard 电话语音语料库的一小段波形，是某个人说“she just had a baby”时元音 [iy] 的波形。

> Figure 15.25 (repeated from Fig. 15.11) shows a short segment of a waveform taken from the Switchboard corpus of telephone speech of the vowel [iy] from someone saying “she just had a baby”.

![](images/15-phonetics-and-speech/fig_p21_0.png)

*图 15.25 元音 [iy]（单词“baby”中的最后一个元音）的一个实例的波形。纵轴表示高于和低于正常大气压的空气压力水平。横轴表示时间。注意该波有规律地重复。重复自图 15.11。*
*Figure 15.25 A waveform of an instance of the vowel [iy] (the last vowel in the word “baby”). The y-axis shows the level of air pressure above and below normal atmospheric pressure. The x-axis shows time. Notice that the wave repeats regularly. Repeated from Fig. 15.11.*

把像图 15.11 这样的声波数字化的第一步，是把模拟

> The first step in digitizing a sound wave like Fig. 15.11 is to convert the analog
表示（先是空气压力，然后是麦克风中的模拟电信号）转换成数字信号。这种模数转换有两个步骤：采样和

> representations (first air pressure and then analog electric signals in a microphone) into a digital signal. This analog-to-digital conversion has two steps: sampling and

> `sampling`（采样）
>
> 释义：按固定时间间隔测量模拟信号的振幅并记录数值，从而把连续信号变成离散的样本序列。

量化。要对一个信号采样，我们在特定的时刻测量它的振幅；采样率是每秒采集的样本数。要准确地测量一个波，每个周期至少要有两个样本：一个测量波的正半部分，一个测量负半部分。每个周期的样本多于两个会提高振幅的准确度，但少于两个就会完全漏掉该波的频率。因此，能够被测量的最高频率的波，其频率是采样率的一半（因为每个周期都需要两个样本）。给定采样率下的这个最高频率被称为

> quantization. To sample a signal, we measure its amplitude at a particular time; the sampling rate is the number of samples taken per second. To accurately measure a wave, we must have at least two samples in each cycle: one measuring the positive part of the wave and one measuring the negative part. More than two samples per cycle increases the amplitude accuracy, but fewer than two samples causes the frequency of the wave to be completely missed. Thus, the maximum frequency wave that can be measured is one whose frequency is half the sample rate (since every cycle needs two samples). This maximum frequency for a given sampling rate is

> `Nyquist`（奈奎斯特）
>
> 释义：提出采样定理的学者姓氏；对某个采样率而言，可测的最高频率即其一半，超过就会发生混叠。

奈奎斯特频率。人类语音中的大部分信息都位于

> called the Nyquist frequency. Most information in human speech is in frequencies

> `frequency`（频率）
>
> 释义：波在单位时间内重复的次数，单位为赫兹（Hz）；语音中多数有用信息都在 10,000 Hz 以下。

低于 10,000 Hz 的频率范围内；因此，要达到完全的准确度就需要 20,000 Hz 的采样率。但电话语音经过交换网络的滤波，电话只传输低于 4,000 Hz 的频率。因此，对于像 Switchboard 语料库这样的电话带宽语音，8,000 Hz 的采样率已经足够，而麦克风语音通常使用 16,000 Hz 的采样。

> below 10,000 Hz; thus, a 20,000 Hz sampling rate would be necessary for complete accuracy. But telephone speech is filtered by the switching network, and only frequencies less than 4,000 Hz are transmitted by telephones. Thus, an 8,000 Hz sampling rate is sufficient for telephone-bandwidth speech like the Switchboard corpus, while 16,000 Hz sampling is often used for microphone speech.

尽管使用更高的采样率能带来更高的 ASR 准确率，我们也不能

> Although using higher sampling rates produces higher ASR accuracy, we can’t
在训练和测试 ASR 系统时混用不同的采样率。因此，如果我们在像 Switchboard（8 KHz 采样）这样的电话语料库上测试，就必须把训练语料库降采样到 8 KHz。类似地，如果我们在多个语料库上训练，而其中之一包含电话语音，我们就把所有宽带语料库降采样到 8KHz。

> combine different sampling rates for training and testing ASR systems. Thus if we are testing on a telephone corpus like Switchboard (8 KHz sampling), we must downsample our training corpus to 8 KHz. Similarly, if we are training on multiple corpora and one of them includes telephone speech, we downsample all the wideband corpora to 8KHz.

振幅测量值以整数形式存储，要么是 8 位（取值范围为 -128–

> Amplitude measurements are stored as integers, either 8 bit (values from -128–

- 要么是 16 位（取值范围为 -32768–32767）。这种把实数值表示为整数的过程称为量化；所有彼此间距小于

> or 16 bit (values from -32768–32767). This process of representing real-valued numbers as integers is called quantization; all values that are closer together than

> `quantization`（量化）
>
> 释义：把连续的实数值振幅近似为有限个整数值的过程，差距小于量化步长的取值会被表示成同一个数。

最小粒度（即量化步长）的值都被表示为相同的数。我们把数字化、量化后的波形中时间索引为 n 的每个样本记作 x[n]。

> the minimum granularity (the quantum size) are represented identically. We refer to each sample at time index n in the digitized, quantized waveform as x[n].

数据一旦被量化，就会以各种格式存储。这些格式的一个参数

> Once data is quantized, it is stored in various formats. One parameter of these
格式就是上面讨论过的采样率和样本大小；电话语音通常以 8 kHz 采样并存储为 8 位样本，而麦克风数据通常以 16 kHz 采样并存储为 16 位样本。另一个参数是声道数。对于立体声数据或双方对话，我们可以把两个声道

> formats is the sample rate and sample size discussed above; telephone speech is often sampled at 8 kHz and stored as 8-bit samples, and microphone data is often sampled at 16 kHz and stored as 16-bit samples. Another parameter is the number of channels. For stereo data or for two-party conversations, we can store both channels

> `channel`（通道）
>
> 释义：此处指梅尔滤波器组中单个滤波器的输出数值，代表某一梅尔频带的对数能量。

存放在同一个文件里，也可以把它们存放在不同的文件里。最后一个参数是单个样本的存储方式——线性存储还是压缩存储。电话语音常用的一种压缩格式是 µ-law（常写作 u-law，但读音仍是 mu-law）。像 µ-law 这样的对数压缩算法的直觉依据是：人耳对小强度声音比对大强度声音更敏感；对数表示对小数值的保真度更高，代价是在大数值上误差更大。未经对数变换的线性值通常称为线性 PCM 值（PCM 是脉冲编码

> in the same file or we can store them in separate files. A final parameter is individual sample storage—linearly or compressed. One common compression format used for telephone speech is µ-law (often written u-law but still pronounced mu-law). The intuition of log compression algorithms like µ-law is that human hearing is more sensitive at small intensities than large ones; the log represents small values with more faithfulness at the expense of more error on large values. The linear (unlogged) values are generally referred to as linear PCM values (PCM stands for pulse code

> `PCM`
>
> 释义：脉冲编码调制，即把模拟语音按固定的采样率和量化精度转成数字样本的最基本编码方式。

调制，不过不必在意这一点）。下面是把线性 PCM 样本值 x 压缩成 8 位 µ-law 的公式（8 位时 µ=255）：

> modulation, but never mind that). Here’s the equation for compressing a linear PCM sample value x to 8-bit µ-law, (where µ=255 for 8 bits):

F(x) = sgn(x)log(1+ µ|x|)
−1 ≤x ≤1 (15.10)
log(1+ µ)

### 15.5.2 加窗

> 15.5.2 Windowing

从波形的数字化、量化表示出发，我们需要从一小段语音窗中提取频谱特征，用这段窗来刻画某个音位的一部分。在这个小窗内部，我们可以大致把信号视为平稳的（也就是说，它在这一区域内的统计特性是恒定的）。（相对

> From the digitized, quantized representation of the waveform, we need to extract spectral features from a small window of speech that characterizes part of a particular phoneme. Inside this small window, we can roughly think of the signal as stationary (that is, its statistical properties are constant within this region). (By

> `stationary`（平稳）
>
> 释义：指信号在一小段区间内统计特性保持不变的性质；语音只有在一个短窗之内才可近似满足这一条件。

地讲，一般来说语音是非平稳信号，也就是说它的统计

> contrast, in general, speech is a non-stationary signal, meaning that its statistical

> `non-stationary`（非平稳）
>
> 释义：指信号的统计特性随时间而变化；语音整体上随时间变化，因此只能在很短的时间窗内近似视为平稳。

特性随时间并不恒定）。我们用一个在某个区域内非零、在其他地方为零的窗，让这个窗沿语音信号滑动，并与输入波形相乘，从而提取出这段大致平稳的语音，得到加窗后的波形。

> properties are not constant over time). We extract this roughly stationary portion of speech by using a window which is non-zero inside a region and zero elsewhere, running this window across the speech signal and multiplying it by the input waveform to produce a windowed waveform.

从每个窗中取出的语音称为一帧。加窗过程

> The speech extracted from each window is called a frame. The windowing is

> `frame`（帧）
>
> 释义：用窗函数从语音信号中截取出的一小段，是提取频谱信息和构造声学特征时的基本处理单位。

由三个参数刻画：窗大小（或称帧大小，即窗的宽度，以毫秒计）、帧步长（也称为移位或偏移）——即相邻

> characterized by three parameters: the window size or frame size of the window(its width in milliseconds), the frame stride, (also called shift or offset) between

> `stride`（步长）
>
> 释义：相邻两帧起始点之间的时间间隔，也称移位或偏移，它决定了特征序列在时间上的密度。

两个窗之间的间隔，以及窗的形状。

> successive windows, and the shape of the window.

为了提取信号，我们把 n 时刻的信号值 s[n] 与

> To extract the signal we multiply the value of the signal at time n, s[n] by the
n 时刻的窗函数值 w[n] 相乘：

> value of the windowing function at time n, w[n]:

y[n] = w[n]s[n] (15.11)
图 15.26 中画出的窗形状是矩形窗；可以看到，经加窗提取

> The window shape sketched in Fig. 15.26 is rectangular; you can see the ex-

> `rectangular`（矩形）
>
> 释义：指窗内取值恒为 1、在边界处突然截断信号的窗形状；它在傅里叶分析中会带来问题，因此构造声学特征时更常用汉明窗。

![](images/15-phonetics-and-speech/fig_p23_1.png)

*图 15.26 加窗示意，展示一个 25 ms 的矩形窗，其步长为 10 ms。*
*Figure 15.26 Windowing, showing a 25 ms rectangular window with a 10ms stride.*

出的加窗信号看上去与原始信号完全一样。然而，矩形窗会在其边界处突然截断信号，这在我们做傅里叶分析时会带来问题。出于这一原因，在构造声学特征时我们更常使用汉明窗，它把信号的值向

> tracted windowed signal looks just like the original signal. The rectangular window, however, abruptly cuts off the signal at its boundaries, which creates problems when we do Fourier analysis. For this reason, for acoustic feature creation we more commonly use the Hamming window, which shrinks the values of the signal toward

> `Hamming`（汉明（Hamming））
>
> 释义：以人名命名的一种平滑窗函数，两端逐渐衰减到零，可减轻加窗在边界处突然截断造成的后果。

零衰减，从而在窗的边界处避免出现不连续。图 15.27 同时展示了这两种窗；公式如下（假设窗的长度为 L 帧）：

> zero at the window boundaries, avoiding discontinuities. Figure 15.27 shows both; the equations are as follows (assuming a window that is L frames long):

 1
0 ≤n ≤L−1
rectangular w[n] = (15.12)
0 otherwise0.54−0.46cos( 2πn L ) 0 ≤n ≤L−1
Hamming w[n] = (15.13)
0 otherwise

![](images/15-phonetics-and-speech/fig_p23_0.png)

*图 15.27 用矩形窗或汉明窗对一个正弦波加窗。*
*Figure 15.27 Windowing a sine wave with the rectangular or Hamming windows.*

### 15.5.3 离散傅里叶变换

> 15.5.3 Discrete Fourier Transform

下一步是为加窗后的信号提取频谱信息；我们需要知道信号在不同频带中包含多少能量。用于为离散时间

> The next step is to extract spectral information for our windowed signal; we need to know how much energy the signal contains at different frequency bands. The tool for extracting spectral information for discrete frequency bands for a discrete-time

> `Discrete`（离散的）
>
> 释义：指时间与幅度都只取有限个离散数值的信号；数字化之后的语音波形就是这种信号。

（采样）信号在离散频带上提取频谱信息的工具，就是离散傅里叶变换，即 DFT。

> (sampled) signal is the discrete Fourier transform or DFT.

> `Fourier transform`（傅里叶变换）
>
> 释义：把信号分解成不同频率成分的数学变换，是分析语音频谱、求取各频带能量的基础工具。

DFT 的输入是一段加窗信号 x[n]…x[m]，而它的输出，对于其中每个

> The input to the DFT is a windowed signal x[n]...x[m], and the output, for each of

> `DFT`（离散傅里叶变换（DFT））
>
> 释义：把时域采样信号分解为一组离散频率分量，输出各分量的幅度与相位，是计算频谱的基础。

N 个离散频带，则是一个复数 X[k]，表示原始信号中该频率分量的幅度与相位。若把幅度对频率作图，就可以把频谱可视化（关于频谱的更多内容见第 15 章）。例如，图 15.28 给出了信号中一段 25 ms 的汉明窗加窗片段，以及由 DFT 计算得到的频谱（另作了若干额外的平滑）。

> N discrete frequency bands, is a complex number X[k] representing the magnitude and phase of that frequency component in the original signal. If we plot the magnitude against the frequency, we can visualize the spectrum (see Chapter 15 for more on spectra). For example, Fig. 15.28 shows a 25 ms Hamming-windowed portion of a signal and its spectrum as computed by a DFT (with some additional smoothing).

![](images/15-phonetics-and-speech/fig_p24_0.png)

*图 15.28 （a）取自元音 [iy] 的信号中一段 25 ms 的汉明窗加窗片段；（b）由 DFT 计算得到的其频谱。*
*Figure 15.28 (a) A 25 ms Hamming-windowed portion of a signal from the vowel [iy] and (b) its spectrum computed by a DFT.*

这里不介绍 DFT 的数学细节，只指出

> We do not introduce the mathematical details of the DFT here, except to note
傅里叶分析依赖欧拉公式，其中 j 为虚数单位：

> that Fourier analysis relies on Euler’s formula, with j as the imaginary unit:

> `Euler’s formula`（欧拉公式）
>
> 释义：把复指数与三角函数联系起来的等式，傅里叶分析正是借助它把信号表示为一组复指数。

e jθ = cosθ + jsinθ (15.14)
为已经学过信号处理的学生作一点简要回顾：DFT 的定义如下：

> As a brief reminder for those students who have already studied signal processing, the DFT is defined as follows:

> N−1

X x[n]e−j 2π
X[k] = (15.15)

> N kn

> n=0

> `fast Fourier transform`（快速傅里叶变换）
>
> 释义：一种高效计算离散傅里叶变换的算法，把运算量从平方级降到 N log N 级。

计算 DFT 的一个常用算法是快速傅里叶变换

> A commonly used algorithm for computing the DFT is the fast Fourier transform
或称 FFT。这种 DFT 的实现非常高效，但只适用于取值为

> or FFT. This implementation of the DFT is very efficient but only works for values

> `FFT`（快速傅里叶变换（FFT））
>
> 释义：快速傅里叶变换的缩写，语音特征提取中用它把每帧波形转换到频域。

2 的幂的 N。

> of N that are powers of 2.

### 15.5.4 梅尔滤波器组与对数

> 15.5.4 Mel Filter Bank and Log

FFT 的结果给出每个频带上的能量。然而，人的听觉并非对所有频带都同样敏感；它对较高频率的敏感度更低。这种偏向低频的特性有助于人的识别，因为低频信息（如共振峰）对于区分元音或鼻音至关重要，而高频信息（如塞音的爆发或擦音噪声）对成功识别的关键程度较低。对这种人类感知特性加以建模，同样能提升语音识别的性能。

> The results of the FFT tell us the energy at each frequency band. Human hearing, however, is not equally sensitive at all frequency bands; it is less sensitive at higher frequencies. This bias toward low frequencies helps human recognition, since information in low frequencies (like formants) is crucial for distinguishing vowels or nasals, while information in high frequencies (like stop bursts or fricative noise) is less crucial for successful recognition. Modeling this human perceptual property improves speech recognition performance in the same way.

我们实现这一直觉的方式是：收集能量时并非在每个频率上均等

> We implement this intuition by collecting energies, not equally at each frequency
频带，而是按照梅尔刻度——一种听觉频率刻度。梅尔（Stevens 等 1937，Stevens 与 Volkmann 1940）是音高的单位。在感知上音高间距相等的两对声音，其梅尔数之差也相等。梅尔频率 m 可由原始声学频率经对数变换算得：

> band, but according to the mel scale, an auditory frequency scale. A mel (Stevens et al. 1937, Stevens and Volkmann 1940) is a unit of pitch. Pairs of sounds that are perceptually equidistant in pitch are separated by an equal number of mels. The mel frequency m can be computed from the raw acoustic frequency by a log transformation:

> `mel`（梅尔）
>
> 释义：一种音高单位，属于听觉频率刻度；感知上音高间距相等的两对声音，其梅尔数之差也相等。

f
mel(f) = 1127ln(1+ (15.16)
700)
我们通过构造一组滤波器来实现这一直觉：这些滤波器从各个频带收集能量，按对数方式分布，从而使我们在低频处具有很细的分辨率，在高频处分辨率较低。图 15.29 给出了一组实现该思路的三角形滤波器示例，将其与频谱相乘即可得到梅尔频谱。

> We implement this intuition by creating a bank of filters that collect energy from each frequency band, spread logarithmically so that we have very fine resolution at low frequencies, and less resolution at high frequencies. Figure 15.29 shows a sample bank of triangular filters that implement this idea, that can be multiplied by the spectrum to get a mel spectrum.

![](images/15-phonetics-and-speech/fig_p25_0.png)

*图 15.29 梅尔滤波器组（Davis 与 Mermelstein，1980）。每个三角形滤波器沿梅尔刻度按对数间隔排列，从给定的频率范围收集能量。*
*Figure 15.29 The mel filter bank (Davis and Mermelstein, 1980). Each triangular filter, spaced logarithmically along the mel scale, collects energy from a given frequency range.*

最后，我们对每个梅尔频谱值取对数。人对

> Finally, we take the log of each of the mel spectrum values. The human response
信号强度的响应是对数式的（正如人对频率的响应）。与低振幅时相比，在高振幅下人对振幅细微差异的敏感度更低。此外，使用对数还能使特征估计对输入的变化不那么敏感，例如因说话人嘴部靠近或远离麦克风而引起的功率变化。

> to signal level is logarithmic (like the human response to frequency). Humans are less sensitive to slight differences in amplitude at high amplitudes than at low amplitudes. In addition, using a log makes the feature estimates less sensitive to variations in input such as power variations due to the speaker’s mouth moving closer or further from the microphone.

我们把某个滤波器的每个标量输出称为一个通道，因此

> We call each scalar output from a particular filter a channel, and so the output

> `channel`（通道）
>
> 释义：此处指梅尔滤波器组中单个滤波器的输出数值，代表某一梅尔频带的对数能量。

滤波器组对每个输入帧的输出是一个向量，例如包含 80 或 128 个通道，其中每个通道表示某个（按梅尔间隔的）频带的对数能量。

> for each input frame from the filterbank is a vector of, say 80 or 128 channels, each of which represents the log energy of a particular (mel-spaced) frequency band.

在把这个对数梅尔通道向量送入下游的神经网络

> Before we send this log mel channel vector to the downstream neural network
层之前，语音系统通常会对它们重新缩放，使其具有可比的取值范围。语音中一种常见的归一化做法是，在整个预训练数据集上把输入缩放到 -1 与 1 之间并使其均值为零（见第 4 章第 4.3.2 节）。

> layers, it’s common for speech systems to rescale them so they have comparable ranges. A common type of normalization for speech is to scale the input to be between -1 and 1 with zero mean across the entire pretraining dataset (see Section 4.3.2 in Chapter 4).

## 15.6 MFCC：梅尔频率倒谱系数

> 15.6 MFCC: Mel Frequency Cepstral Coefficients

MFCC，即梅尔频率倒谱系数，是波形的一种有用表示，它

> The MFCC, mel frequency cepstral coefficients, is a useful representation of the

> `MFCC`（梅尔频率倒谱系数（MFCC））
>
> 释义：一种 39 维声学特征向量，突出信号中与音子检测相关的成分，广泛用于语音识别。

强调信号中与检测语音单元相关的那些方面。MFCC 是一个 39 维特征向量，由以下部分组成：

> waveform that emphasizes aspects of the signal that are relevant for detection of phonetic units. The MFCC is a 39-dimensional feature vector consisting of:

| 12 个倒谱系数<br>12 cepstral coefficients | 1 个能量系数<br>1 energy coefficient |
| --- | --- |
| 12 个一阶差分倒谱系数<br>12 delta cepstral coefficients | 1 个一阶差分能量系数<br>1 delta energy coefficient |
| 12 个二阶差分倒谱系数<br>12 double delta cepstral coefficients | 1 个二阶差分能量系数<br>1 double delta energy coefficient |

下面简述这些特征是如何计算的；希望了解更多

> Below we sketch how these features are computed; students interested in more
细节感兴趣的读者，建议进一步修读一门信号处理课程。

> detail are encouraged to follow up with a signal processing course.

倒谱：离散傅里叶逆变换

> The Cepstrum: Inverse Discrete Fourier Transform
MFCC 系数以倒谱为基础。理解倒谱的一种方式

> MFCC coefficients are based on the cepstrum. One way to think about the cepstrum

> `cepstrum`（倒谱）
>
> 释义：对信号对数幅度谱再做一次频谱分析所得的结果，能把声门声源与声道滤波特性分离开来，是 MFCC 特征的基础。

是把它看作一种分离声源与滤波器的有用方式。回顾 15.4.6 节可知，语音波形是某一基频的声门源波形通过声道后产生的，而声道因其形状而具有特定的滤波特性。但声门源的许多特性（其基频、声门脉冲的具体细节等）对于区分不同音子并不重要。相反，对音子检测最有用的信息是滤波器，也就是声道的准确位置。如果我们知道声道的形状，就能知道正在发出的是哪个音子。这表明，对音子检测有用的特征应当设法对声源与滤波器进行解卷积（分离），只向我们展示声道滤波器。事实证明，倒谱正是做到这一点的一种途径。

> is as a useful way of separating the source and filter. Recall from Section 15.4.6 that the speech waveform is created when a glottal source waveform of a particular fundamental frequency is passed through the vocal tract, which because of its shape has a particular filtering characteristic. But many characteristics of the glottal source(its fundamental frequency, the details of the glottal pulse, etc.) are not important for distinguishing different phones. Instead, the most useful information for phone detection is the filter, that is, the exact position of the vocal tract. If we knew the shape of the vocal tract, we would know which phone was being produced. This suggests that useful features for phone detection would find a way to deconvolve(separate) the source and filter and show us only the vocal tract filter. It turns out that the cepstrum is one way to do this.

![](images/15-phonetics-and-speech/fig_p26_0.png)

*图 15.30 幅度谱（a）、对数幅度谱（b）和倒谱（c），取自 Taylor（2009），经许可使用。两个谱上都叠加了一条平滑的频谱包络，以便于观察频谱。*
*Figure 15.30 The magnitude spectrum (a), log magnitude spectrum (b), and cepstrum (c), from Taylor (2009), by permission. The two spectra have a smoothed spectral envelope laid on top to help visualize the spectrum.*

为简单起见，我们把对数幅度谱作为输入，并忽略

> For simplicity, let’s consider as input the log magnitude spectrum and ignore
梅尔刻度。倒谱可以看作是谱的对数之谱。这听起来可能令人困惑。但让我们从简单的部分开始：谱的对数。也就是说，倒谱始于一个标准的幅度谱，例如 Taylor（2009）给出的图 15.30(a) 中某个元音的幅度谱。然后我们取对数，即把幅度谱中的每个幅度值替换为它的对数，如图 15.30(b) 所示。

> the mel scaling. The cepstrum can be thought of as the spectrum of the log of the spectrum. This may sound confusing. But let’s begin with the easy part: the log of the spectrum. That is, the cepstrum begins with a standard magnitude spectrum, such as the one for a vowel shown in Fig. 15.30(a) from Taylor (2009). We then take the log, that is, replace each amplitude value in the magnitude spectrum with its log, as shown in Fig. 15.30(b).

下一步是把对数谱想象成它本身就是一段波形。换

> The next step is to visualize the log spectrum as if itself were a waveform. In
言之，考虑图 15.30(b) 中的对数谱。让我们想象去掉那些表明它是一个谱的坐标轴标签（x 轴为频率），并想象我们面对的只是一段普通的语音信号，其 x 轴为时间。那么关于这个“伪信号”的频谱，我们现在能说些什么？注意这个波中存在一个高频重复成分：小波形沿 x 轴大约每 1000 个单位重复 8 次，对应频率约为 120 Hz。这个高频成分由信号的基频引起，代表频谱中信号各次谐波处的小峰。此外，这个“伪信号”中还有一些频率较低的成分；例如，包络（共振峰结构）在该窗口内约有四个大峰，其频率要低得多。

> other words, consider the log spectrum in Fig. 15.30(b). Let’s imagine removing the axis labels that tell us that this is a spectrum (frequency on the x-axis) and imagine that we are dealing with just a normal speech signal with time on the x-axis. What can we now say about the spectrum of this “pseudo-signal”? Notice that there is a high frequency repetitive component in this wave: small waves that repeat about 8 times in each 1000 along the x-axis, for a frequency of about 120 Hz. This high frequency component is caused by the fundamental frequency of the signal and represents the little peaks in the spectrum at each harmonic of the signal. In addition, there are some lower frequency components in this “pseudo-signal”; for example, the envelope or formant structure has about four large peaks in the window, for a much lower frequency.

图 15.30(c) 显示了倒谱，即我们一直在描述的那个谱

> Figure 15.30(c) shows the cepstrum: the spectrum that we have been describing
也就是对数谱的谱。这个倒谱（cepstrum 一词由 spectrum 的前四个字母颠倒而成）以样本为 x 轴单位来显示。这是因为，通过对对数谱再取谱，我们已经离开了频谱的频率域，回到了时域。事实证明，倒谱的正确单位是样本。

> of the log spectrum. This cepstrum (the word cepstrum is formed by reversing the first four letters of spectrum) is shown with samples along the x-axis. This is because by taking the spectrum of the log spectrum, we have left the frequency domain of the spectrum, and gone back to the time domain. It turns out that the correct unit of a cepstrum is the sample.

考察这个倒谱，我们看到在 120 附近确实有一个大峰，

> Examining this cepstrum, we see that there is indeed a large peak around 120,
它对应 F0，代表声门脉冲。在 x 轴取值较低处还有其他各种成分。这些成分代表声道滤波器（舌头及其他发音器官的位置）。因此，如果我们关注音子检测，就只需利用较低的倒谱值。如果我们关注音高检测，就可以利用较高的倒谱值。

> corresponding to the F0 and representing the glottal pulse. There are other various components at lower values on the x-axis. These represent the vocal tract filter(the position of the tongue and the other articulators). Thus, if we are interested in detecting phones, we can make use of just the lower cepstral values. If we are interested in detecting pitch, we can use the higher cepstral values.

就 MFCC 提取而言，我们通常只取前 12 个倒谱

> For the purposes of MFCC extraction, we generally just take the first 12 cepstral
值。这 12 个系数将只表示声道滤波器的信息，与声门声源的信息干净地分离开来。

> values. These 12 coefficients will represent information solely about the vocal tract filter, cleanly separated from information about the glottal source.

事实证明，倒谱系数具有一个极为有用的性质，即

> It turns out that cepstral coefficients have the extremely useful property that the
不同系数的方差往往互不相关。频谱则不然，不同频带的谱系数之间是相关的。

> variance of the different coefficients tends to be uncorrelated. This is not true for the spectrum, where spectral coefficients at different frequency bands are correlated.

对于学过信号处理的人而言，倒谱更形式化的定义是

> For those who have had signal processing, the cepstrum is more formally defined
信号 DFT 的对数幅度的 DFT 逆变换；因此，对于加窗的一帧语音 x[n]，

> as the inverse DFT of the log magnitude of the DFT of a signal; hence, for a windowed frame of speech x[n],
!

> N−1 N−1

X X x[n]e−j 2π ej 2π
c[n] = log (15.17)
能量 在上一节的 12 个倒谱系数之外，我们再加入第 13 个特征：该帧的能量。能量是音子检测的有用线索（例如元音和咝音的能量比塞音更大）。一帧中的能量是

> Energy To the 12 cepstral coefficients from the prior section we add a 13th feature: the energy from the frame. Energy is a useful cue for phone detection (for example vowels and sibilants have more energy than stops). The energy in a frame is the sum

> N kn N kn

> n=0 n=0

> `energy`（能量）
>
> 释义：一帧语音内各样本功率随时间的累加和，是判断音子身份的有效线索，元音与咝音通常高于塞音。

该帧中各样本功率随时间的累加和；因此，对于从时间样本 t1 到时间样本 t2 的窗口内的信号 x，其能量为

> over time of the power of the samples in the frame; thus, for a signal x in a window from time sample t1 to time sample t2, the energy is
X
Energy = x2[t] (15.18)
差分特征 我们还加入与倒谱特征随时间变化有关的特征。语音信号的变化，例如共振峰在过渡处的斜率，或从塞音闭塞到塞音除阻爆发的变化，同样能为音子身份提供有用的线索。对 13 个特征（12 个倒谱特征加能量）中的每一个，都再配上一个差分

> Delta features We also add features related to the change in cepstral features over time. Changes in the speech signal, like the slope of a formant at its transitions, or the change from a stop closure to stop burst, can again provide a useful cue for phone identity. To each of the 13 features (12 cepstral features plus energy) a delta

> t2

> t=t1

> `delta feature double delta`（差分特征；双差分）
>
> 释义：差分特征刻画相邻帧间对应特征取值的改变，即速度；双差分再对差分特征求一次帧间变化，即加速度。

（或速度）特征以及一个双差分（或加速度）特征。这 13 个差分

> or velocity feature and a double delta or acceleration feature. Each of the 13 delta
特征各表示相应的倒谱/能量特征在帧间的变化，而 13 个双差分特征各表示相应的差分特征在帧间的变化。这些差分可以简单地用当前帧的值减去前一帧的值来计算，但在实践中通常的做法是拟合一个多项式，并取其一次和二次导数。

> features represents the change between frames in the corresponding cepstral/energy feature, and each of the 13 double delta features represents the change between frames in the corresponding delta features. These deltas can be simply computed by just subtracting the value at a frame from the prior value, but in practice it’s common to fit a polynomial and take its first and second derivative.

## 15.7 小结

> 15.7 Summary

本章介绍了语音学与计算语音学中的许多重要概念。

> This chapter has introduced many of the important concepts of phonetics and computational phonetics.

- 我们可以用称为音子的单位来表示词的发音。

> We can represent the pronunciation of words in terms of units called phones.

表示音子的标准系统是国际音标字母表（IPA）。英语转写中最常用的计算系统是 ARPAbet，它方便地使用 ASCII 符号。

> The standard system for representing phones is the International Phonetic Alphabet or IPA. The most common computational system for transcription of English is the ARPAbet, which conveniently uses ASCII symbols.

- 音子可以通过发音器官如何以发音动作产生它们来描述；辅音根据其发音部位、发音方式和是否带声来定义；元音则根据其舌位高低、舌位前后和圆唇程度来定义。
- 语音也可以从声学角度来描述。声波可以用频率、振幅，或它们在感知上的对应量——音高与响度来描述。
- 声音的频谱描述其不同的频率成分。虽然有些语音属性可以从波形中辨认出来，但无论是人还是机器，都依赖频谱分析来检测音子。
- 语谱图是频谱随时间变化的图形。元音由称为共振峰的特征谐波来描述。

> Phones can be described by how they are produced articulatorily by the vocal organs; consonants are defined in terms of their place and manner of articulation and voicing; vowels by their height, backness, and roundness.
> Speech sounds can also be described acoustically. Sound waves can be described in terms of frequency, amplitude, or their perceptual correlates, pitch and loudness.
> The spectrum of a sound describes its different frequency components. While some phonetic properties are recognizable from the waveform, both humans and machines rely on spectral analysis for phone detection.
> A spectrogram is a plot of a spectrum over time. Vowels are described by characteristic harmonics called formants.

## 历史注释

> Historical Notes

发音语音学的主要洞见可追溯到公元前 800 年至公元前 150 年的语言学家。

> The major insights of articulatory phonetics date to the linguists of 800–150 B.C.

印度。他们发明了发音部位和发音方式的概念，弄清了带声的声门机制，并理解了同化的概念。欧洲科学直到 2000 多年之后，即 19 世纪晚期，才赶上印度语音学家。希腊人确实有一些初步的语音知识；例如到柏拉图的《泰阿泰德篇》和《克拉底鲁篇》时代，他们已经把元音与辅音区分开来，把塞辅音与持续音区分开来。斯多葛学派发展出音节的概念，并意识到可能词形所受的音位配列限制。12 世纪一位不知名的冰岛学者运用了音位的概念，为冰岛语提出了一套音位书写系统，其中包括表示长度和鼻化的附加符号。但他的著作直到 1818 年才出版，即便在出版之后，在斯堪的纳维亚之外也基本无人知晓（Robins, 1967）。语音学的现代时期通常被认为始于 Sweet，他在 1877 年的《语音学手册》（Handbook of Phonetics）中提出了实质上就是音位的概念。他还设计了一套用于转写的字母表，并区分了宽式转写与窄式转写，提出了许多最终被 IPA 采纳的想法。Sweet 被认为是他那个时代最出色的实践语音学家；他为语音学目的做出了最早的语言科学录音，并推进了发音描述的技术水平。他也以难以相处而闻名，乔治·伯纳德·萧（George Bernard Shaw）以他为原型塑造的舞台角色亨利·希金斯（Henry Higgins）很好地体现了这一特点。音位一词最早由波兰学者博杜安·德·库尔德内（Baudouin de Courtenay）命名，他于 1894 年发表了自己的理论。

> India. They invented the concepts of place and manner of articulation, worked out the glottal mechanism of voicing, and understood the concept of assimilation. European science did not catch up with the Indian phoneticians until over 2000 years later, in the late 19th century. The Greeks did have some rudimentary phonetic knowledge; by the time of Plato’s Theaetetus and Cratylus, for example, they distinguished vowels from consonants, and stop consonants from continuants. The Stoics developed the idea of the syllable and were aware of phonotactic constraints on possible words. An unknown Icelandic scholar of the 12th century exploited the concept of the phoneme and proposed a phonemic writing system for Icelandic, including diacritics for length and nasality. But his text remained unpublished until 1818 and even then was largely unknown outside Scandinavia (Robins, 1967). The modern era of phonetics is usually said to have begun with Sweet, who proposed what is essentially the phoneme in his Handbook of Phonetics 1877. He also devised an alphabet for transcription and distinguished between broad and narrow transcription, proposing many ideas that were eventually incorporated into the IPA. Sweet was considered the best practicing phonetician of his time; he made the first scientific recordings of languages for phonetic purposes and advanced the state of the art of articulatory description. He was also infamously difficult to get along with, a trait that is well captured in Henry Higgins, the stage character that George Bernard Shaw modeled after him. The phoneme was first named by the Polish scholar Baudouin de Courtenay, who published his theories in 1894.

语音学入门教材包括 Ladefoged（1993）以及 Clark 和 Yallop（1995）。Wells（1982）是关于英语方言的权威性三卷本著作。

> Introductory phonetics textbooks include Ladefoged (1993) and Clark and Yallop (1995). Wells (1982) is the definitive three-volume source on dialects of English.

声学语音学中的许多经典洞见在

> Many of the classic insights in acoustic phonetics had been developed by the
20 世纪 50 年代末或 60 年代初就已形成；仅举几例亮点：声谱仪这类技术（Koenig 等，1946），源—滤波器理论以及发音与声学之间映射等其他问题的理论洞见（（Fant, 1960），Stevens 等 1953，Stevens 和 House 1955，Heinz 和 Stevens 1961，Stevens 和 House 1961），元音共振峰的 F1×F2 空间（Peterson 和 Barney, 1952），对重音的语音本质以及用时长和强度作为线索的理解（Fry, 1955），以及对音子感知问题的基本理解（Miller 和 Nicely 1955，Liberman 等 1952）。Lehiste（1967）是声学语音学经典论文的合集。Gunnar Fant 的许多开创性论文收录于 Fant（2004）。

> late 1950s or early 1960s; just a few highlights include techniques like the sound spectrograph (Koenig et al., 1946), theoretical insights like the working out of the source-filter theory and other issues in the mapping between articulation and acoustics ((Fant, 1960), Stevens et al. 1953, Stevens and House 1955, Heinz and Stevens 1961, Stevens and House 1961) the F1xF2 space of vowel formants (Peterson and Barney, 1952), the understanding of the phonetic nature of stress and the use of duration and intensity as cues (Fry, 1955), and a basic understanding of issues in phone perception (Miller and Nicely 1955,Liberman et al. 1952). Lehiste (1967) is a collection of classic papers on acoustic phonetics. Many of the seminal papers of Gunnar Fant have been collected in Fant (2004).

语音特征提取算法在 20 世纪 60 年代和

> Speech feature-extraction algorithms were developed in the 1960s and early
70 年代初发展起来，包括高效的快速傅里叶变换（FFT）（Cooley 和 Tukey, 1965）、倒谱处理在语音中的应用（Oppenheim 等，1968），以及用于语音编码的 LPC 的发展（Atal 和 Hanauer, 1971）。

> 1970s, including the efficient fast Fourier transform (FFT) (Cooley and Tukey, 1965), the application of cepstral processing to speech (Oppenheim et al., 1968), and the development of LPC for speech coding (Atal and Hanauer, 1971).

优秀的声学语音学教材包括 Johnson（2003）和 Ladefoged（1996）。Coleman（2005）包含从语言学视角对声学与语音计算处理的介绍。Stevens（1998）阐述了一套有影响力的语音产生理论。有多种用于声学语音分析的软件包。本书中的许多插图都是由 Praat 软件包（Boersma 和 Weenink, 2005）生成的，该软件包包含音高、

> Excellent textbooks on acoustic phonetics include Johnson (2003) and Ladefoged (1996). Coleman (2005) includes an introduction to computational processing of acoustics and speech from a linguistic perspective. Stevens (1998) lays out an influential theory of speech sound production. There are a number of software packages for acoustic phonetic analysis. Many of the figures in this book were generated by the Praat package (Boersma and Weenink, 2005), which includes pitch,

> `Praat`
>
> 释义：一款广泛使用的声学语音分析软件，可进行音高、频谱与共振峰分析，并支持脚本编程。

频谱和共振峰分析，以及一种脚本语言。

> spectral, and formant analysis, as well as a scripting language.

## 练习

> Exercises

15.1 找出下列单词的 ARPAbet 转写中的错误：

> 15.1 Find the mistakes in the ARPAbet transcriptions of the following words:

- “three” [dh r i]　d. “study” [s t uh d i]　g. “slight” [s l iy t]
- “sing” [s ih n g]　e. “though” [th ow]
- “eyes” [ay s]　f. “planning” [p pl aa n ih ng]

> “three” [dh r i] d. “study” [s t uh d i] g. “slight” [s l iy t]
> “sing” [s ih n g] e. “though” [th ow]
> “eyes” [ay s] f. “planning” [p pl aa n ih ng]

15.2 Ira Gershwin 为《Let’s Call the Whole Thing Off》所写的歌词谈到了“tomato”“potato”和“either”这几个词各自的两个发音。请把这三个词的两个发音都转写为 ARPAbet。

> 15.2 Ira Gershwin’s lyric for Let’s Call the Whole Thing Off talks about two pronunciations (each) of the words “tomato”, “potato”, and “either”. Transcribe into the ARPAbet both pronunciations of each of these three words.

15.3 用 ARPAbet 转写下列单词：

> 15.3 Transcribe the following words in the ARPAbet:

- dark
- suit
- greasy
- wash
- water

15.4 任选一个波形文件。教材网站上有一些示例。

> 15.4 Take a wavefile of your choice. Some examples are on the textbook website.

下载 Praat 软件，用它把波形文件在词一级上转写并转写成 ARPAbet 音子，借助 Praat 播放每个波形文件的片段，并查看波形文件和语谱图。

> Download the Praat software, and use it to transcribe the wavefiles at the word level and into ARPAbet phones, using Praat to help you play pieces of each wavefile and to look at the wavefile and the spectrogram.

15.5 录下你自己说五个英语元音的声音：[aa]、[eh]、[ae]、[iy]、[uw]。

> 15.5 Record yourself saying five of the English vowels: [aa], [eh], [ae], [iy], [uw].

找出你的每个元音的 F1 和 F2。

> Find F1 and F2 for each of your vowels.
