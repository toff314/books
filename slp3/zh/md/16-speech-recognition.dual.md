# 第 16 章 自动语音识别

### 章

> CHAPTER

# 16 自动语音识别

> 16 Automatic Speech Recognition

我不知是否领会了你的意思：倘若领会了，它便栖居在你话语的层层涟漪之上，如溪流里黄昏的影，朦朦胧胧，

> I KNOW not whether I see your meaning: if I do, it lies Upon the wordy wavelets of your voice, Dim as an evening shadow in a brook,
理解口语，或者至少把话语转写成文字，

> Understanding spoken language, or at least transcribing the words into writing, is
是计算机语言处理最早的目标之一。事实上，语音处理比计算机早出现好几十年！第一台能识别语音的机器是 1920 年代的一件玩具。右图所示的“Radio Rex”是一只赛璐珞做的狗，当 500 Hz 的声能松开弹簧时，它便会（借助弹簧）动起来。由于 500 Hz 大致就是“Rex”中元音 [eh] 的第一共振峰，所以 Rex 一被叫到似乎就会跑过来（David, Jr. and Selfridge, 1962）。

> one of the earliest goals of computer language processing. In fact, speech processing predates the computer by many decades! The first machine that recognized speech was a toy from the 1920s. “Radio Rex”, shown to the right, was a celluloid dog that moved (by means of a spring) when the spring was released by 500 Hz acoustic energy. Since 500 Hz is roughly the first formant of the vowel [eh] in “Rex”, Rex seemed to come when he was called(David, Jr. and Selfridge, 1962).

> Thomas Lovell Beddoes，1851 年
>
> *Thomas Lovell Beddoes, 1851*

![](images/16-speech-recognition/img_29.jpeg)

到了现代，我们对自动系统有了更高的期待。自动语音识别（ASR）的任务，就是把如下这样的任意波形：

> In modern times, we expect more of our automatic systems. The task of automatic speech recognition (ASR) is to map any waveform like this:

> `ASR`
>
> 释义：自动语音识别（Automatic Speech Recognition）的缩写，指把语音波形映射为对应词串的任务。

映射为恰当的词串：

> to the appropriate string of words:

该吃午饭啦！

> It’s time for lunch!

由任意说话人在任意环境中进行的语音自动转写仍远未解决，但 ASR 技术已经成熟到足以胜任许多实际任务。语音是与家电、数字助理或聊天机器人交流的自然接口，尤其是在键盘不太方便的手机上。ASR 对一般性的转写也很有用，例如为音频或视频文本自动生成字幕（转写电影、视频或现场讨论）。在口述占据重要地位的法律等领域，转写十分重要。最后，ASR 还是辅助交流（计算机与因某种残障而在打字或听觉上有困难或无能的用户之间的交互）的一部分，这一点也很重要。双目失明的弥尔顿曾向女儿们口述《失乐园》，亨利·詹姆斯则在重复性劳损之后口述了他后期的小说。

> Automatic transcription of speech by any speaker in any environment is still far from solved, but ASR technology has matured to the point where it is now viable for many practical tasks. Speech is a natural interface for communicating with appliances, or with digital assistants or chatbots, especially on cellphones, where keyboards are less convenient. ASR is also useful for general transcription, for example for automatically generating captions for audio or video text (transcribing movies or videos or live discussions). Transcription is important in fields like law where dictation plays an important role. Finally, ASR is important as part of augmentative communication (interaction between computers and humans with some disability resulting in difficulties or inabilities in typing or audition). The blind Milton famously dictated Paradise Lost to his daughters, and Henry James dictated his later novels after a repetitive stress injury.

接下来的几节中，我们将介绍 ASR 任务的各种目标，描述

> In the next sections we’ll introduce the various goals of the ASR task, describe
如何提取声学特征，并介绍在语音识别任务中常被用作初始层的卷积神经网络架构。

> how acoustic features are extracted, and introduce the convolutional neural net architecture which is commonly used as an initial layer in speech recognition tasks.

随后我们将介绍两大类 ASR 方法。第一类是编码器-解码器范式，我们将介绍基于注意力的编码器-解码器基线算法，它因早期的一项实现有时也被称为 listen, attend and spell。

> We’ll then introduce two families of methods for ASR. The first is the encoderdecoder paradigm, and we’ll introduce the baseline attention-based encoder decoder algorithm, sometimes called Listen Attend and Spell after an early implementation.

我们还会介绍一个更先进的编码器-解码器系统，即 OpenAI 的 Whisper 系统（Radford et al., 2023），以及一个基于相同架构的开放系统 OWSM（the Open Whisper-style Speech Model，开放 Whisper 式语音模型）（Peng et al., 2023）。（这些模型还有翻译等额外能力，我们稍后会讨论。）第二类是使用 wav2vec 2.0 或 HuBERT 这类自监督语音模型（有时称为 SSL，即自监督学习），它们是编码器，能学得语音的抽象表示，再与 CTC 损失函数配对进行解码，即可用于 ASR。

> We’ll also introduce a more advanced encoder-decoder system, OpenAI’s Whisper system (Radford et al., 2023) as well an open system based on the same architecture, OWSM (the Open Whisper-style Speech Model) (Peng et al., 2023). (These models have additional capabilities including translation, as we’ll discuss later). The second is the use of self-supervised speech models (sometimes called SSL for selfsupervised learning) like Wav2Vec2.0 or HuBERT, which are encoders that learn abstract representations of speech that can be used for ASR by pairing them with the CTC loss function for decoding.

最后，我们将介绍用于评估 ASR 的标准指标——词错误率。

> We’ll conclude with the standard word error rate metric used to evaluate ASR.

## 16.1 自动语音识别任务

> 16.1 The Automatic Speech Recognition Task

在介绍 ASR 算法之前，我们先谈谈 ASR 任务本身有哪些变化。变化的一个维度是词汇量大小。有些 ASR 任务早已能以极高的准确率解决，比如词汇表只有 2 个词的任务（yes

> Before describing algorithms for ASR, let’s talk about how the ASR task itself varies. One dimension of variation is vocabulary size. Some ASR tasks have long been solved with extremely high accuracy, like those with a 2-word vocabulary (yes

> `digit`（数字）
>
> 释义：指 0 到 9 这类单个数字，数字识别任务要求识别由它们构成的序列。

还是 no），或像数字识别这样 11 个词的词汇表（识别由

> versus no) or an 11 word vocabulary like digit recognition (recognizing sequences

> `recognition`（识别）
>
> 释义：指数字识别，即把语音中的数字序列判定为零到九等数字串。

零到九再加 oh 组成的数字序列）。像准确转写视频或人类对话这类词汇量达 60,000 词以上、范围开放的任务，则要难得多。

> of digits including zero to nine plus oh). Open-ended tasks like accurately transcribing videos or human conversations, with large vocabularies of 60,000 or more words, are much harder.

变化的第二个维度是说话人在对谁说。人对着机器说话（无论是口述还是与对话系统交谈）比人对着人说话更容易识别。朗读语音，即人

> A second dimension of variation is who the speaker is talking to. Humans speaking to machines (either dictating or talking to a dialogue system) are easier to recognize than humans speaking to humans. Read speech, in which humans are reading

> `read speech`（朗读语音）
>
> 释义：指说话人照着书面文本念出来的语音，如有声书录音。

出声读出来的语音，例如有声书，也相对容易识别。而识别两个人在对话语音中相互交谈的语音，

> out loud, for example in audio books, is also relatively easy to recognize. Recognizing the speech of two humans talking to each other in conversational speech,

> `conversational speech`（对话语音）
>
> 释义：指人与人之间自然交谈时的语音，例如商务会议录音，识别难度最大。

例如转写一场商务会议，则是最难的。看来，当人对着机器说话，或在没有听众在场的情况下朗读时，他们会把话说得简化不少，讲得更慢也更清楚。

> for example, for transcribing a business meeting, is the hardest. It seems that when humans talk to machines, or read without an audience present, they simplify their speech quite a bit, talking more slowly and more clearly.

变化的第三个维度是信道与噪声。语音

> A third dimension of variation is channel and noise. Speech is easier to recognize
如果用头戴式麦克风在安静的房间里录制，比用远场麦克风在嘈杂的城市街道上录制、或在开着车窗的车里录制，更容易识别。

> if it’s recorded in a quiet room with head-mounted microphones than if it’s recorded by a distant microphone on a noisy city street, or in a car with the window open.

最后一个变化维度是口音或说话人类别特征。如果说话人所说的方言或变体

> A final dimension of variation is accent or speaker-class characteristics. Speech
与系统训练时所用的相同，语音就更容易识别。如果系统只用标准方言的说话人、或只用成年说话人训练，那么地区方言或族群方言说话人的语音，以及儿童的语音，识别起来可能相当困难。

> is easier to recognize if the speaker is speaking the same dialect or variety that the system was trained on. Speech by speakers of regional or ethnic dialects, or speech by children can be quite difficult to recognize if the system is only trained on speakers of standard dialects, or only adult speakers.

若干带有真人撰写转写的公开语料库被用于

> A number of publicly available corpora with human-created transcripts are used
构建 ASR 测试集和训练集，以探究上述种种变化；这里我们提到其中几个，因为你会在文献中遇到它们。LibriSpeech 是一个大型

> to create ASR test and training sets to explore this variation; we mention a few of them here since you will encounter them in the literature. LibriSpeech is a large

> `LibriSpeech`
>
> 释义：一个开源朗读语音数据集，含 LibriVox 项目逾 1000 小时的有声书，采样率 16 kHz。

16 kHz 开源朗读语音数据集，包含来自 LibriVox 项目的 1000 多小时有声书录音，该项目由志愿者朗读并录制无版权的书籍（Panayotov et al., 2015）。它的转写在句子层面进行了对齐。它被划分为较容易的（“clean”）和较困难的（“other”）两部分，其中 clean 部分录音质量更高，口音也更接近美式英语。这一划分是在该语料库首次发布时完成的：用一个（在《华尔街日报》朗读语音上训练的）语音识别器对全部音频运行，依据金标转写为每位说话人计算词错误率（WER，正式定义见下文），再把说话人大致平分为两半，来自较低 WER 说话人的录音称为“clean”，来自较高 WER 说话人的录音称为“other”。

> open-source read-speech 16 kHz dataset with over 1000 hours of audio books from the LibriVox project, which has volunteers read and record copyright-free books(Panayotov et al., 2015). It has transcripts aligned at the sentence level. It is divided into an easier (“clean”) and a more difficult portion (“other”) with the clean portion of higher recording quality and with accents closer to US English. The division was done when the corpus was first released by running a speech recognizer (trained on read speech from the Wall Street Journal) on all the audio, computing the word error rate (WER, formally defined below) for each speaker based on the gold transcripts, and dividing the speakers roughly in half, with recordings from lower-WER speakers called “clean” and recordings from higher-WER speakers “other”.

Switchboard 语料库收录的是陌生人之间被提示进行的电话交谈，

> The Switchboard corpus of prompted telephone conversations between strangers

> `Switchboard`
>
> 释义：一个电话对话语音语料库，收集于 1990 年代初，附有大量人工语言学标注。

它于 1990 年代初收集；包含 2430 段平均各约 6 分钟的对话，共 240 小时 8 kHz 语音、约 300 万词（Godfrey et al., 1992）。Switchboard 有一个独特优势，即拥有大量辅助性的人工语言学标注，包括句法分析、对话行为标签、语音与韵律标注，以及话语与信息结构标注。CALLHOME

> was collected in the early 1990s; it contains 2430 conversations averaging 6 minutes each, totaling 240 hours of 8 kHz speech and about 3 million words (Godfrey et al., 1992). Switchboard has the singular advantage of an enormous amount of auxiliary hand-done linguistic labeling, including parses, dialogue act tags, phonetic and prosodic labeling, and discourse and information structure. The CALLHOME

> `CALLHOME`
>
> 释义：一个电话对话语音语料库，收集于 1990 年代末，为亲友之间的 30 分钟电话交谈。

语料库收集于 1990 年代末，由 120 段无脚本的 30 分钟电话对话组成，对话者是通常为密友或亲属的英语母语者（Canavan et al., 1997）。

> corpus was collected in the late 1990s and consists of 120 unscripted 30-minute telephone conversations between native speakers of English who were usually close friends or family (Canavan et al., 1997).

多种语料库试图纳入更自然的输入。CHiME

> A variety of corpora try to include input that is more natural. The CHiME

> `CHiME`
>
> 释义：语音识别领域一系列高难度共享任务，其语料库专门考察 ASR 的鲁棒性。

该挑战赛是一系列高难度共享任务，其语料库专门应对 ASR 中的鲁棒性问题。例如，CHiME 6 任务是对真实家庭环境（具体而言是晚餐聚会）中对话语音的 ASR。该语料库包含在真实家庭中举行的二十场不同晚餐聚会的录音，每场有四名参与者，录制地点包括三个位置（厨房、用餐区、客厅），使用远场麦克风录制。

> Challenge is a series of difficult shared tasks with corpora that deal with robustness in ASR. The CHiME 6 task, for example, is ASR of conversational speech in real home environments (specifically dinner parties). The corpus contains recordings of twenty different dinner parties in real homes, each with four participants, and in three locations (kitchen, dining area, living room), recorded with distant microphones.

AMI 会议语料库包含 100 小时的团体会议录音（其中一些

> The AMI Meeting Corpus contains 100 hours of recorded group meetings (some

> `AMI`
>
> 释义：会议语料库的名称，收录 100 小时小组会议录音，并附带人工转写与部分手工标注。

是自然会议，一些是特意组织的会议），配有手工转写和一些额外的人工标注（Renals et al., 2007）。CORAAL 是一个由 150 多

> natural meetings, some specially organized), with manual transcriptions and some additional hand-labels (Renals et al., 2007). CORAAL is a collection of over 150

> `CORAAL`
>
> 释义：面向非裔美国人英语的社会语言学访谈语料库，含 150 多段访谈及其话语级对齐转写。

段与非裔美国人说话人的社会语言学访谈，目标是研究非裔美国人英语（AAE）——非裔美国人社区及其他群体所使用的诸多语言变体（Kendall and Farrington, 2020）。这些访谈经过匿名化处理，转写文本按话语级别对齐。

> sociolinguistic interviews with African American speakers, with the goal of studying African American English (AAE), the many variations of language used in African American communities and others (Kendall and Farrington, 2020). The interviews are anonymized with transcripts aligned at the utterance level.

其他语言中也有丰富多样的语料库可供使用。在中文方面，

> There are a wide variety of corpora available in other languages. In Chinese,
例如，HKUST 普通话电话语音语料库包含 1206 段转写的

> for example, the HKUST Mandarin Telephone Speech corpus has 1206 transcribed

> `HKUST`（香港科技大学）
>
> 释义：香港科技大学的英文缩写，本章中它指该校发布的普通话电话语音语料库。

十分钟电话对话，对话双方是中国各地讲普通话的说话人，既包括朋友之间的对话，也包括陌生人之间的对话（Liu et al., 2006）。AISHELL-1 语料库包含 170 小时的普通话朗读语音，其句子取自

> ten-minute telephone conversations between speakers of Mandarin across China including conversations between friends and between strangers (Liu et al., 2006). The AISHELL-1 corpus contains 170 hours of Mandarin read speech of sentences taken

> `AISHELL-1`
>
> 释义：一个开源普通话语音识别语料库，收录 170 小时朗读语音，句子来自多个领域。

不同领域，主要由中国北方的不同说话人朗读（Bu et al., 2017）。

> from various domains, read by different speakers mainly from northern China (Bu et al., 2017).

最后，还有许多多语种语料库。Common Voice（Ardila et al.,

> Finally, there are many multilingual corpora. Common Voice (Ardila et al.,
2020）是一个可免费获取的众包语料库，收录经过转写的朗读语音，以 MPEG-3 格式存储，专为 ASR 设计。众包志愿者录制自己朗读脚本语音的内容，脚本往往摘自维基百科文章。录音随后由其他贡献者进行校验。截至本章撰写时，Common Voice 收录了来自 133 种语言的 33,150 小时语音。

> 2020) is a freely available crowd-sourced corpus of transcribed read speech, stored in MPEG-3 format and designed for ASR. Crowd-working volunteers record themselves reading scripted speech, with scripts often extracted from Wikipedia articles. The recordings are then verified by other contributors. As of the writing of this chapter, Common Voice includes 33,150 hours of speech from 133 languages.

FLEURS（Conneau et al., 2023）是一个平行语音数据集，建立在 MT 基准 FLoRes-101（Goyal et al., 2022）之上，后者包含 3001 个句子，从英文维基百科抽取并由人工译员翻译成另外 101 种语言。

> FLEURS (Conneau et al., 2023) is a parallel speech dataset, built on the MT benchmark FLoRes-101 (Goyal et al., 2022), which has 3001 sentences extracted from English Wikipedia and translated into 101 other languages by human translators.

对于 102 种语言中每种语言的 2009 个句子子集，FLEURS 收录了 3 位不同母语者朗读这些句子的录音，每种语言总计约 12 小时语音。

> For a subset of 2009 of the sentences in each of the 102 languages, FLEURS has recordings of 3 different native speakers reading the sentence, in total about 12 hours of speech per language.

图 16.1 显示了错误词的大致百分比（词错误率，

> Figure 16.1 shows the rough percentage of incorrect words (the word error rate,
即 WER，定义见第 378 页），这些数据来自本章撰写时在其中一些任务上大致达到最先进水平的系统。请注意，英语朗读语音（如 LibriSpeech 干净有声书语料库）的错误率约为 2%；用英语朗读语音的转写准确率非常高。相比之下，人类之间对话的转写错误率更高：Switchboard 和 CALLHOME 语料库或 AMI 会议为 5.8% 到 11%。对于非裔美国人英语等变体的说话人，错误率还要更高；而对于 4 名说话人晚餐聚会语音的转写这类困难的对话任务，错误率则进一步升高，可高达 25.5%。普通话自然对话的字符错误率（CER）也高于普通话朗读语音。资源较少的语言错误率甚至更高；我们展示了少数几个例子。

> or WER, defined on page 378) from roughly state-of-the-art systems as of the time of this writing on some of these tasks. Note that the error rate on English read speech(like the LibriSpeech clean audiobook corpus) is around 2% ; transcription of speech read in English is highly accurate. By contrast, the error rate for transcribing conversations between humans is higher; 5.8 to 11% for the Switchboard and CALLHOME corpora or AMI meetings. The error rate is higher yet again for speakers of varieties like African American English, and yet again for difficult conversational tasks like transcription of 4-speaker dinner party speech, which can have error rates as high as 25.5%. Character error rates (CER) are also higher for Mandarin natural conversation than for Mandarin read speech. Error rates are even higher for lower resource languages; we’ve shown a handful of examples.

<!--figbox-->
> 英语任务 WER%LibriSpeech 有声书 960 小时干净集 1.4 LibriSpeech 有声书 960 小时其他集 2.6 Switchboard 陌生人之间的电话对话 5.8 CALLHOME 家人之间的电话对话 11 AMI 会议 11 社会语言学访谈，CORAAL（AAE）16.2 CHiME6 使用远场麦克风的晚餐聚会 25.5 其他语言的示例任务 WER%Common Voice 15 越南语 39.8 Common Voice 15 斯瓦希里语 51.2 FLEURS 孟加拉语 50 中文（普通话）任务 CER%AISHELL-1 普通话朗读语音语料库 3.9 HKUST 普通话电话对话 18.5
>
> *English Tasks WER%LibriSpeech audiobooks 960hour clean 1.4 LibriSpeech audiobooks 960hour other 2.6 Switchboard telephone conversations between strangers 5.8 CALLHOME telephone conversations between family 11 AMI meetings 11 Sociolinguistic interviews, CORAAL (AAE) 16.2 CHiME6 dinner parties with distant microphones 25.5 Sample tasks in other languages WER%Common Voice 15 Vietnamese 39.8 Common Voice 15 Swahili 51.2 FLEURS Bengali 50 Chinese (Mandarin) Tasks CER%AISHELL-1 Mandarin read speech corpus 3.9 HKUST Mandarin Chinese telephone conversations 18.5*
<!--/figbox-->

*图 16.1 约 2023—2024 年报告的、在多种美式英语及其他语言识别任务上 ASR 的大致词错误率（WER = 误识别词所占百分比），以及两个中文识别任务的字符错误率（CER）。*
*Figure 16.1 Rough Word Error Rates (WER = % of words misrecognized) reported around 2023-4 for ASR on various American English and other language recognition tasks, and character error rates (CER) for two Chinese recognition tasks.*

## 16.2 卷积神经网络

> 16.2 Convolutional Neural Networks

卷积神经网络（convolutional neural network，即 CNN，有时也简称为 convnet），

> The convolutional neural network, or CNN (and sometimes shortened as convnet),

> `CNN`
>
> 释义：一种尤其适合在语音与视觉应用中提取特征的网络架构，由卷积层堆叠构成。

是一种网络架构，在语音和视觉应用中提取特征尤为有用。用于语音的卷积层以音频输入的表示（原始音频或梅尔频谱）为输入，输出输入语音的潜在表示序列。在 Whisper、wav2vec2.0 或 HuBERT 等 ASR 系统中，卷积层被堆叠为最初的一组层，产生语音表示，随后再送入 Transformer 层。

> is a network architecture that is particularly useful for extracting features in speech and vision applications. A convolutional layer for speech takes as input a representation of the audio input (either as the raw audio or as Mel spectra) and produces as output a sequence of latent representations of the input speech. In ASR systems like Whisper, wav2vec2.0, or HuBERT, convolutional layers are stacked as an initial set of layers producing speech representations that are then passed to transformer layers.

标准前馈层是全连接的；每个输入都与每个输出相连。相比之下，卷积网络利用了卷积核（kernel）的思想——一种在输入上滑动的小型网络。例如在图像分类任务中，我们让卷积核在图像上水平和垂直地滑动以识别视觉特征，因此把视觉任务描述为 2d（2 维）卷积网络。对于语音，我们让卷积核在时间维度上滑过信号以提取语音特征，因此用于语音的 CNN 是 1d 卷积网络。

> A standard feedforward layer is fully connected; every input is connected to every output. By contrast, a convolutional network makes use of the idea of a kernel, a kind of smaller network that we pass over the input. For example in image classification tasks, we pass the kernel horizontally and vertically over the image to recognize visual features, and so we describe a visual as a 2d (for 2 dimensional) convolutional network. For speech, we will slide our kernel over the signal in the time dimension to extract speech features, so CNNs for speech are 1d convolutional networks.

让我们把这一直觉再展开一点。我们先看一个非常示意的版本

> Let’s flesh out this intuition a bit more. We’ll start with a very schematic version
——一个卷积层，它以单个向量序列 x1 ...xt 为输入，输出同一长度 t 的单个向量序列 z1 ...zt。

> of a convolutional layer that takes as input a single sequence of vectors x1 ...xt and produces as output a single sequence of vectors z1 ...zt, of the same length t.

之后我们再看看如何处理更复杂的输入和输出。

> Afterwards we’ll see how to deal with more complex inputs and outputs.

CNN 使用一个卷积核，即一个小的权重向量 w1 ...wk，来提取特征。它

> A CNN uses a kernel, a small vector of weights w1 ...wk, to extract features. It

> `kernel`（卷积核）
>
> 释义：在输入上滑动的小型权重向量，通过卷积从输入中提取局部特征；语音 CNN 沿时间维度滑动它。

的做法是把该卷积核与输入进行卷积。卷积核与信号的卷积包含 3 个步骤：

> does this by convolving this kernel with the input. The convolution of a kernel with a signal has 3 steps:

> `convolving`（卷积）
>
> 释义：把卷积核（小权重向量）沿输入逐帧滑过、在每一帧与局部输入求点积，从而得到输出序列的运算。

- 将卷积核左右翻转
- 逐帧（沿时间）让卷积核滑过输入
- 在每一帧计算卷积核与局部输入值的点积
- 输出即所得到的点积序列

> Flip the kernel left-to-right
> Pass the kernel frame by frame (temporally) across the input
> At each frame computing the dot product of the kernel with the local input values
> The output is the resulting sequence of dot products

我们可以把卷积过程看作在信号中寻找与卷积核

> We can think of the convolution process as finding regions in the signal that are
相似的区域，因为当两个向量相似时点积较大。卷积运算用 * 运算符表示（这个符号不幸被重载，也用来表示简单的乘法）。我们来看看如何计算 x ∗w，即单个向量 x 与卷积核向量 w 的卷积。先考虑卷积核宽度为 1 的简单情形。我们把每个输出元素 z j 计算为卷积核与 x j 的乘积：

> similar to the kernel, since the dot product is high when two vectors are similar. The convolution operation is represented by the * operator (an unfortunate overloading of this symbol that also refers to simple multiplication). Let’s see how to compute x ∗w, the convolution of a single vector x with a kernel vector w. Let’s first think about the simple case of a kernel width of 1. We compute each output element z j as the product of the kernel with x j:

宽度为 1 的卷积核的卷积：zj = x jw0 ∀j : 1 ≤j ≤t (16.1)

> convolution with width-1 kernel: zj = x jw0 ∀j : 1 ≤j ≤t (16.1)
图 16.2 展示了这一计算的直观示意。

> Fig. 16.2 shows an intuition of this computation.

![](images/16-speech-recognition/fig_p5_0.png)

*图 16.2 宽度为 1 的卷积核（滤波器）w 的卷积示意图。*
*Figure 16.2 A schematic view of convolution with a kernel (filter) w whose width is 1.*

> 卷积核在输入上逐格移动，每一帧的输出 zi 是卷积核与该输入帧的点积。卷积核长度为 1 时，我们无需担心翻转卷积核，点积就是标量乘积。图中展示了 z3 计算为 x3 ×w1。
>
> *The kernel is walked across the input, and the output at each frame zi is the dot product of the kernel with the input frame. With a kernel of length 1 we don’t have to worry about flipping the kernel, and the dot product is just the scalar product. The figure shows the computation of z3 as x3 ×w1.*

现在来看更长的卷积核。尽管我们已经描述了第一步

> Let’s now turn to longer kernels. Although we’ve described the first step of the
将卷积视为翻转卷积核，实际上在 ASR 系统中（或在 pytorch 之类的组件库里）我们会跳过这一步。从技术上讲，这意味着我们所用的算法

> convolution as flipping the kernel, in fact in ASR systems (or in component libraries like pytorch) we skip this step. Technically this means that the algorithm we are

> `cross-`（互相关）
>
> 释义：指不翻转卷积核、直接沿信号滑动并逐帧求点积的运算，ASR 实现实际采用的就是它。

所使用的实际上并不是卷积，而是互相关（cross-correlation），后者是如下这种运算的名称

> using is not in fact convolution, it’s instead cross-correlation, which is the name for

> `correlation`（互相关）
>
> 释义：卷积核不先翻转、直接在信号上滑动求点积的做法，与教科书定义的卷积仅在核是否翻转上有别。

一种让卷积核沿信号滑过、逐帧计算其点积而事先不翻转它的算法。这一差别无关紧要，因为卷积核的参数会在训练中学习得到，因此模型很容易学会以任意一种顺序排列参数的卷积核。不过，出于历史原因，我们仍把这一过程称为一维卷积，而非互相关。

> an algorithm of walking a kernel across a signal, computing its dot product frame by frame, without flipping it first. The difference doesn’t matter, since the parameters of the kernel will be learned during training, and so the model could easily learn a kernel with the parameters in either order. Still, for historical reasons we still call this process a 1d convolution rather than cross-correlation.

下面来看这些较长卷积核更一般的公式。为避免卷积在信号左右边缘处无定义，我们可以对

> Let’s see a more general equation for these longer kernels. To avoid the convolution being undefined at the left and right edges of the signal, we can pad the

> `pad`（填充）
>
> 释义：在信号首尾各补上若干零值，使卷积核中心能对准第一个元素、且在边缘处有确定值可取。

输入进行填充，即在信号的首尾各加入少量的 p 个零，这样我们就能把卷积核的中心对准第一个元素 x1，且在 x1 左侧也有确定的值可取。这也恰好使得让输出长度与输入长度保持一致变得简单。为此，方便的做法是把卷积核向量定义为具有奇数个元素、长度为 k = 2p+1，从而中心元素两侧各有 p 个元素。输出向量 z 的每个元素 zj 随后按如下点积计算：

> input by adding a small number p of zeros at the beginning and end of the signal, so that we can start the center of the kernel at the first element x1, and there will be a defined value to the left of x1. This also turns out to make it simple to have the output length as the same as the input length. To do this, it’s convenient to define the kernel vector as having an odd number of elements of length k = 2p+1, thus with the center element having p elements on either side. Each element zj of the output vector z is then computed as the following dot product:

> p

X
z j = xj+iwi+p (16.2)
图 16.3 展示了卷积 x∗w 的计算，其中卷积核宽度为 3，并分别在 x 的首尾各填充 1 帧、取值为零。

> Fig. 16.3 shows the computation of the convolution x∗w with a kernel whose width is 3, and with padding of 1 frame at the beginning and end of x with a value of zero.

> i=−p

![](images/16-speech-recognition/fig_p6_0.png)

*图 16.3 卷积的示意图，卷积核（滤波器）宽度为 3，填充为 1，即在信号的首尾各加入一个零值。已经翻转过的卷积核沿输入滑过，每一帧 zi 处的输出是卷积核与窗口内输入的点积。图中展示了 z3 的计算。*
*Figure 16.3 A schematic view of convolution with a kernel (filter) width of 3, and with a padding of 1, showing a zero value added at the start and end of the signal. The (already flipped) kernel is walked across the input, and the output at each frame zi is the dot product of the kernel with the input in the window. The figure shows the computation of z3.*

注意卷积核的尺寸 k（感受野）被设计得很小

> Note that the size k (the receptive field) of the kernel is designed to be small
相较于信号而言。例如在 Whisper 的卷积层中，卷积核宽度为 3 帧，即该卷积核是长度为 3 的向量（我们说该卷积核的感受野为 3）。这意味着该卷积核是在与

> compared to the signal. For example for the convolutional layers in Whisper, the kernel width is 3 frames, meaning the kernel is a vector of length 3 (we say that the kernel has a receptive field of 3). That means that the kernel is being compared

> `receptive field`（感受野）
>
> 释义：卷积核一次覆盖并参与运算的输入帧数，决定它从多长的语音片段中提取信息。

3 帧语音进行比较。在 Whisper 中每 10 ms 有一帧，而每一帧代表 25 ms 语音信息的窗口。这意味着每个卷积核从约 45 ms 的语音中提取信息（10 + 10 + 12.5 + 12.5）。这已足够长，可以提取诸如共振峰过渡、塞音闭塞或送气等多种语音特征。

> to 3 frames of speech. In Whisper there is a frame every 10 ms and each frame represent a window of 25ms of speech information. That means each kernel is extracting information from about 45 ms of speech (10 + 10 + 12.5 + 12.5). That’s long enough to extract various phonetic features like formant transitions or stop closures or aspiration.

至此我们描述了一种简化的卷积视角，其中输入是一个

> We’ve now described a simplified view of convolution in which the input is a
单一向量 x，输出也是一个单一向量 z，二者都对应随时间变化的信号。实际上，卷积层的输入通常是对数梅尔频谱的输出，这意味着它有多个（比如 128 个）通道，每个通道对应一个对数梅尔滤波器的输出。卷积核会为这些输入通道各自准备一个单独的向量。我们说该卷积核的深度为 128，意味着该卷积核的形状是

> single vector x and the output is a single vector z, both corresponding to a signal over time. In practice, the input to a convolutional layer is commonly the output from a log mel spectrum, which means it has many (say 128) channels, one for each log mel filters output. The kernel will have separate vectors for each of these input channels. We say that the kernel has a depth of 128, meaning that the kernel is of

> `depth`（深度）
>
> 释义：卷积核为每个输入通道各配一个向量，深度即输入通道数，表示它覆盖的通道维度大小。

形状为 [128,3]。

> shape [128,3].

为得到卷积核的输出，我们对所有输入通道求和。也就是说，我们

> To get the output of the kernel, we sum over all the input channels. That is, we
对每个输入通道 xc 用卷积核 w 与之卷积，得到单个输出 zc，然后把所有得到的输出相加：

> get a single output zc for each of the input channels xc by convolving the kernel w with it, and then we sum up all the resulting outputs:

> Ci

X
xc ∗w
z = (16.3)
因此，第 j 帧的输出 zj 综合了来自所有输入通道的信息。

> The output at frame j, zj, thus integrates information from all of the input channels.

> c=1

最后，卷积层的输出也比仅仅一个

> Finally, the output from a convolution layer is also more complex than just a
由单个标量值来表示每一帧的向量更复杂。相反，对于给定的输入帧，卷积层的输出需要是一个嵌入，即该帧的潜在表示。与所有神经模型一样，潜在表示应具有模型维度，无论该维度是多少。例如 Whisper 的模型维度为 1280，因此卷积层需要为这 1280 个模型维度各设一个输出通道。为此，我们实际上会为每个模型维度学习一个独立的卷积核。也就是说，我们将学习 1280 个独立的卷积核，每个卷积核的深度等于输入通道数（例如 128），并具有一个滤波器宽度（比如为 3）。这样，每一帧的嵌入表示将包含 1280 个对输入信号独立计算出的特征。我们在图 16.4 中给出示意图

> vector consisting of a single scalar value to represent each frame. Instead, the output of the convolution layer for a given input frame needs to be an embedding, a latent representation of that frame. As with all neural models, latent representations should have the model dimensionality, whatever that is. For example the model dimensionality of Whisper is 1280, and so the convolutional layer needs to have one output channel for each of these 1280 dimensions of the model. In order to do this, we’ll actually learn one separate kernel for each of the model dimensions. That is, we’ll learn 1280 separate kernels, each kernel having the depth of the number of input channels (for example 128), and a filter-width (say of 3). That way, the embedding representation of each frame will have 1280 independently computed features of the input signal. We show a schematic in Fig. 16.4

![](images/16-speech-recognition/fig_p7_0.png)

*图 16.4 一个具有 128 个输入通道和 1024 个输出通道的卷积网络的示意图。可以看到在时间点 i，1024 个卷积核之一（“卷积核 35”，深度均为 128、宽度为 3）如何与 128 个对数梅尔频谱输入向量（逐一）做点积，然后求和，从而为时间 i 处输出嵌入的某一个维度产生单个数值。*
*Figure 16.4 A schematic view of a convolutional net with 128 input channels and 1024 output channels. We see how at time point i one of the 1024 kernels (“kernel 35”, each of depth 128 and width 3) is dot-product-ed with (each of) the 128 log mel spectrum input vectors, and then summed to produce a single value for one dimension of the output embedding at time i.*

一维卷积层还可以有步长。步长是指我们

> A 1d convolution layer can also have a stride. Stride is the amount that we move

> `stride`（步长）
>
> 释义：卷积核在输入上每前进一步所移动的位置数；步长越大，输出序列越短。

每一步之间把卷积核在输入上移动的量。上图展示的是步长为 1，即我们先把卷积核放在 x1 上，然后是 x2，再是 x3，依此类推。若步长为 2，我们就会先把卷积核放在 x1 上，然后是 x3，再是 x5，依此类推。

> the kernel over the input between each step. The figures above show a stride of 1, meaning that we first position the kernel over x1, then x2, then x3, and so on. For a stride of 2, we would first position the kernel over x1, then x3, then x5, and so on.

步长越大，输出序列越短；步长为 2 意味着输出序列 z 的长度将是输入序列 x 的一半。步长大于 1 的卷积层常用来缩短输入序列。这样做有用，部分是因为更短的信号占用更少的内存和计算带宽，同时也如我们在下一节将看到的，是因为它有助于缓解声学帧嵌入的长度（10 ms）与字母或单词长度之间的不匹配——后者覆盖的信号要长得多。

> A longer stride means a shorter output sequence; a stride of two means the output sequence z will be half the length of the input sequence x. Convolutional layers with strides greater than 1 are commonly used to shorten an input sequence. This is useful partly because a shorter signal takes less memory and computational bandwidth, but also, as we’ll see in the next section, because it helps address the mismatch between the length of acoustic frame embeddings (10 ms) and letters or words, which cover much more of the signal.

最后，在实践中，卷积层之后可以接一个输出非线性层，例如 ReLU 层。

> Finally, in practice a convolutional layer can be followed by an output nonlinearity, like a ReLU layer.

## 16.3 用于 ASR 的编码器-解码器架构

> 16.3 The Encoder-Decoder Architecture for ASR

我们要介绍的第一个 ASR 架构是编码器-解码器架构，与第 13 章为机器翻译（MT）引入的架构相同。图 16.5 勾勒了该架构，它被称为基于注意力的编码器解码器（attention-based encoder decoder，AED），或 listen attend and spell

> The first ASR architecture we introduce is the encoder-decoder architecture, the same architecture introduced for MT in Chapter 13. Fig. 16.5 sketches this architecture, called attention-based encoder decoder or AED, or listen attend and spell

> `AED`
>
> 释义：基于注意力机制的编码器-解码器语音识别架构，解码器通过交叉注意力读取编码器输出，逐步生成转写文本。

> `listen attend and spell`（listen, attend and spell）
>
> 释义：一种端到端语音识别架构，先用编码器提取声学表示，再以注意力完成对齐并由解码器逐字符生成转写结果。

（LAS），这一缩写取自最早将其应用于语音的两篇论文（Chorowski et al. 2014，

> (LAS) after the two papers which first applied it to speech (Chorowski et al. 2014,
Chan et al. 2016）。

> Chan et al. 2016).

该架构的输入 x 是 t 个声学特征向量构成的序列 X =

> The input to the architecture x is a sequence of t acoustic feature vectors X =
x1,x2,...,xt，每 10 ms 一帧对应一个向量。我们通常以前一节所述的对数梅尔频谱特征作为起点，不过也可以从原始波形文件开始。输出序列 Y 既可以是字母，也可以是标记（BPE 或 sentencepiece）；这里为简化说明，我们假定它是字母。因此输出序列 Y = (⟨SOS⟩,y1,...,ym⟨EOS⟩)，其中假定使用特殊的序列起始标记和序列结束标记 ⟨sos⟩ 与 ⟨eos⟩，且每个 yi 是一个字符；对于英语，我们可能选择如下字符集：

> x1,x2,...,xt, one vector per 10 ms frame. We often start from the log mel spectral features described in the previous section, although it’s also possible to start from a raw wavefile. The output sequence Y can be either letters or tokens (BPE or sentencepiece); we’ll assume letters just to simplify the explanation here. Thus the output sequence Y = (⟨SOS⟩,y1,...,ym⟨EOS⟩), assuming special start of sequence and end of sequence tokens ⟨sos⟩and ⟨eos⟩and each yi is a character; for English we might choose the set:

yi ∈{a,b,c,...,z,0,...,9,⟨space⟩,⟨comma⟩,⟨period⟩,⟨apostrophe⟩,⟨unk⟩}

![](images/16-speech-recognition/fig_p8_0.png)

*图 16.5 编码器-解码器语音识别器的示意架构。*
*Figure 16.5 Schematic architecture for an encoder-decoder speech recognizer.*

这一架构也被 OpenAI 的 Whisper 模型所采用（Radford et al.,

> This architecture is also used in the Whisper model from OpenAI (Radford et al.,
2023）。图 16.6 展示了 Whisper 架构的一个子部分（Whisper 还执行其他语音任务，如语音翻译和语音活动检测，我们将在下一章讨论）。Whisper 的模型和推理代码已公开发布，但训练代码和训练数据并未公开。不过，有一些开源项目采用 Whisper 风格的架构，例如 Open Whisper-style

> 2023). Fig. 16.6 shows a subpart of the Whisper architecture (Whisper also does other speech tasks like speech translation and voice activity detection, which we’ll discuss in the next chapter). Whisper models and inference code are publicly released, but the training code and training data are not. However, there are opensource projects that use a Whisper-style architecture, like the Open Whisper-style

![](images/16-speech-recognition/fig_p9_0.png)

*图 16.6 Radford et al. (2023) 给出的 Whisper 架构草图。由于 Whisper 是一个还执行翻译的多任务系统，其转写格式包含一个转写起始符（SOT）标记、一个语言标签，以及一个说明是转写还是翻译的指令标记。*
*Figure 16.6 A sketch of the Whisper architecture from Radford et al. (2023). Because Whisper is a multitask system that also does translation, Whisper’s transcription format has a Start of Transcript (SOT) token, a language tag, and then an instruction token for whether to transcribe or translate.*

Speech Model（OWSM），它复现了 Whisper 风格的训练，但提供了完全开源的工具箱和公开可用的数据（Peng et al., 2023）。

> Speech Model (OWSM), which reproduces Whisper-style training but offers a fully open-source toolkit and publicly available data (Peng et al., 2023).

### 16.3.1 输入与卷积层

> 16.3.1 Input and Convolutional Layers

当输入序列与输出序列的长度差异极大时，编码器-解码器架构尤为适用，语音正是如此：很长的声学特征序列要映射到短得多的字母或词序列。例如在英语中，词平均由 5 个字母或 1.3 个 BPE 标记组成（Bostrom and Durrett, 2020），而在自然对话中，一个词平均持续约 250 毫秒（Yuan et al., 2006），即 25 帧（每帧 10ms）。因此以 10ms 帧表示的语音信号，比以词或标记表示的文本信号长约 5（25/5）到 19（25/1.3）倍。

> The encoder-decoder architecture is particularly appropriate when input and output sequences have stark length differences, as they do for speech, with long acoustic feature sequences mapping to much shorter sequences of letters or words. For example English, words are on average 5 letters or 1.3 BPE tokens long (Bostrom and Durrett, 2020) and, in natural conversation, the average word lasts about 250 milliseconds (Yuan et al., 2006), or 25 frames of 10ms. So the speech signal in 10ms frames is about 5 (25/5) to 19 (25/1.3) times longer than the text signal in words or tokens.

由于语音的这种长度差异极为悬殊，面向语音的编码器-解码器架构通常在编码器阶段之前设有一个压缩阶段，以缩短声学特征序列。（我们还可以利用一种为良好应对压缩而设计的损失函数，比如我们后面将介绍的 CTC 损失函数。）

> Because this length difference is so extreme for speech, encoder-decoder architectures for speech usually have a compression stage that shortens the acoustic feature sequence before the encoder stage. (We can additionally make use of a loss function that is designed to deal well with compression, like the CTC loss function we’ll introduce later.)
下采样的目标是产生一个更短的序列 X = x1,...,xn，

> The goal of the subsampling is to produce a shorter sequence X = x1,...,xn that
它将作为 Transformer 编码器的输入。一个非常简单的基线算法是有时被称为低帧率的方法（Pundak and Sainath, 2016）：对于时刻 i，我们

> will be the input to the transformer encoder. A very simple baseline algorithm is a method sometimes called low frame rate (Pundak and Sainath, 2016): for time i we

> `low frame rate`（低帧率）
>
> 释义：一种降低输入采样速率的做法，把相邻若干帧声学特征拼接为更长的向量，并按更长的时间间隔取样，从而缩短序列。

把声学特征向量 fi 与其前两个向量 fi−1 和 fi−2 堆叠（拼接）成一个长度为其三倍的新向量。然后直接删除 fi−1 和 fi−2。

> stack (concatenate) the acoustic feature vector fi with the prior two vectors fi−1 and fi−2 to make a new vector three times longer. Then we simply delete fi−1 and fi−2.

这样，我们就不再是每隔 10 ms 得到一个（比如）40 维的声学特征向量，而是每隔 30 ms 得到一个更长的向量（比如 120 维），序列长度缩短为 n = t 3。

> Thus instead of (say) a 40-dimensional acoustic feature vector every 10 ms, we have a longer vector (say 120-dimensional) every 30 ms, with a shorter sequence length n = t 3.

但生成更短输入序列最常见的方式，是使用

> But the most common way of creating a shorter input sequence is to use the
我们在前一节介绍的卷积层。当卷积层的步长大于 1 时，输出序列会比输入序列更短。下面以两个常用的 ASR 系统为例来看。

> convolutional layers we introduced in the previous section. When a convolutional layer has a stride greater than 1, the output sequence becomes shorter than the input sequence. Let’s see this in two commonly used ASR systems.

Whisper 系统（Radford et al., 2023）的音频上下文窗口为 30

> The Whisper system (Radford et al., 2023) has an audio context window of 30
秒。它为每一帧提取 128 通道的对数梅尔特征，窗口为 25ms、步长为 10ms。随后将这些特征归一化为 0 均值、范围为 -1 到 1。10 ms 的步长（每秒 100 帧）意味着 30 秒的上下文窗口中共有 3000 个输入帧。这 3000 帧被送入两个卷积层，每个卷积层之后都接一个非线性（Whisper 使用 GELU（高斯误差线性单元），它是 ReLU 的更平滑版本）。第一个卷积层有 128 个输入通道，步长为 1，输出通道数即模型维度，窗口长度为 3000。第二个卷积层的输入和输出通道数均为模型维度，步长为 2。第二个卷积层中的步长 2 使输出序列长度为输入序列的一半，把输出窗口长度降至 1500，并每 20 ms 产生一个音频标记。在这个前端的输出送入 Transformer 编码器之前，会先为这些音频编码加上正弦位置嵌入。

> seconds. It extracts 128 channel log mel features for each frame, with a 25ms window and a stride of 10ms. These are then normalized to 0 mean and a range of -1 to 1. A stride of 10 ms (100 frames per second) means there are 3000 input frames in a 30 second context window. These 3000 frames are passed to two convolutional layers, each one followed by a nonlinearity (Whisper uses GELU (Gaussian Error Linear Unit), which is a smoother version of ReLU). The first convolutional layer has 128 input channels and uses a stride of 1, with number of output channels being the model dimensionality, and the window length is 3000. For the second convolutional layer the number of input and output channels is the model dimensionality, and there is a stride of 2. The stride of 2 in the second convolutional layer makes the output sequence half the length of the input sequence, bringing the output window length down to 1500 and producing an audio token every 20 ms. Sinusoidal position embeddings are added to these audio encodings before the output of this front end is passed to the transformer encoder.

HuBERT（Hsu et al., 2021）采用了另一种前端架构，其中

> HuBERT (Hsu et al., 2021) uses an alternative front end architecture, in which
用卷积层完全取代了频谱的计算。

> convolutional layers are used to completely replace the computation of the spectrum.

因此输入是原始的 16kHz 采样音频，它依次经过七个 512 通道的层，步长为 [5,2,2,2,2,2,2]，卷积核宽度为 [10,3,3,3,3,2,2]，这些层既学习提取频谱信息，又把输入序列缩短 320 倍，从 16kHz（= 每 .0625 ms 一个表示）降到 20 ms 的帧率。输入上会加上位置编码，然后应用 GELU 和层归一化，之后输出才送入 Transformer 编码器。

> So the input is raw 16kHz sampled audio, and it is passed through seven 512-channel layers with strides [5,2,2,2,2,2,2] and kernel widths [10,3,3,3,3,2,2] which learn both to extract spectral information, and to shorten the input sequence by 320x, from 16kHz (= one representation per .0625 ms) down to a 20 ms framerate. Positional encodings are added to the input, and then a GELU and layer norm are applied before the output is passed to the transformer encoder.

### 16.3.2 推理

> 16.3.2 Inference

经过卷积阶段之后，面向语音的编码器-解码器采用与机器翻译相同的架构（带交叉注意力的 Transformer）。

> After the convolutional stage, encoder-decoders for speech use the same architecture(transformer with cross-attention) as for MT.

让我们回顾一下我们介绍过的编码器-解码器架构，

> Let’s remind ourselves of the encoder-decoder architecture that we introduced
它出现在第 13 章。该架构使用两个 Transformer：一个编码器，与第 7 章的基本 Transformer 相同；以及一个解码器，后者多了一处：一个称为交叉注意力层的新层。编码器接收声学输入 X = x1,...,xn，并通过一系列编码器块将其映射为输出表示 Henc = h1,...,hn；

> in Chapter 13. It uses two transformers: an encoder, which is the same as the basic transformer from Chapter 7, and a decoder, which has one addition: a new layer called the cross-attention layer. The encoder takes the acoustic input X = x1,...,xn and maps them to an output representation Henc = h1,...,hn; via a stack of encoder blocks.

解码器本质上是一个条件语言模型，它关注编码器的表示并逐个生成目标文本（字母或标记），在每个时间步以来自编码器的音频表示和此前生成的文本为条件，生成一个新的字母或标记。

> The decoder is essentially a conditional language model that attends to the encoder representation and generates the target text (letters or tokens) one by one, at each timestep conditioning on the audio representations from the encoder and the previously generated text to generate a new letter or token.

解码器中的 Transformer 块多了一个额外的层，它带有一种特殊类型的

> The transformer blocks in the decoder have an extra layer with a special kind
注意力，即交叉注意力。交叉注意力与普通 Transformer 块中的多头

> of attention, cross-attention. Cross-attention has the same form as the multi-head

> `cross-attention`（交叉注意力）
>
> 释义：解码器中的额外注意力层，其查询照常来自解码器上一层，而键和值取自编码器输出，用于把声学表示与生成文本关联起来。

注意力形式相同，只是查询照常来自解码器的上一层，而键和值则来自编码器的输出。

> attention in a normal transformer block, except that while the queries as usual come from the previous layer of the decoder, the keys and values come from the output of the encoder.

也就是说，在标准多头注意力中，每个注意力层的输入

> That is, where in standard multi-head attention the input to each attention layer
是 X，而在交叉注意力中，输入是编码器的最终输出 Henc = h1,...,hn。

> is X, in cross attention the input is the final output of the encoder Henc = h1,...,hn.

Henc 的形状为 [n×d]，每一行表示一个声学输入标记。为了把来自编码器的键和值与来自解码器上一层的查询关联起来，

> Henc is of shape [n×d], each row representing one acoustic input token. To link the keys and values from the encoder with the query from the prior layer of the decoder,

![](images/16-speech-recognition/fig_p11_0.png)

*图 16.7 编码器与解码器的 Transformer 块，展示残差流视角。编码器的最终输出 Henc = h1,...,hn 是解码器所使用的上下文。解码器是标准的 Transformer，只是多了一个额外的层，即交叉注意力层，它接收编码器输出 Henc 并用它构成自己的 K 和 V 输入。*
*Figure 16.7 The transformer block for the encoder and the decoder, showing the residual stream view. The final output of the encoder Henc = h1,...,hn is the context used in the decoder. The decoder is a standard transformer except with one extra layer, the cross-attention layer, which takes that encoder output Henc and uses it to form its K and V inputs.*

我们将编码器输出 Henc 与交叉注意力层的键权重 WK 和值权重 WV 相乘。查询来自前一个解码器层的输出 Hdec[ℓ−1]，它与交叉注意力层的查询权重 WQ 相乘：

> we multiply the encoder output Henc by the cross-attention layer’s key weights WK and value weights WV. The query comes from the output from the prior decoder layer Hdec[ℓ−1], which is multiplied by the cross-attention layer’s query weights WQ:

Q = Hdec[ℓ−1]WQ; K = HencWK; V = HencWV (16.4)
QK⊺  (16.5)
CrossAttention(Q,K,V) = softmax
√dk V
因此，交叉注意力使解码器能够关注整个编码器最终输出表示中所投影的声学输入。每个解码器块中的另一个注意力层，即多头注意力层，与我们在第 7 章看到的因果（从左到右）注意力相同。但编码器中的多头注意力则允许前看整个源音频，因此它没有被掩蔽。

> The cross attention thus allows the decoder to attend to the acoustic input as projected into the entire encoder final output representations. The other attention layer in each decoder block, the multi-head attention layer, is the same causal (left-toright) attention that we saw in Chapter 7. But the multi-head attention in the encoder, however, is allowed to look ahead at the entire source audio, so it is not masked.

在推理时，输出字符串 y 的概率分解为：

> For inference, the probability of the output string y is decomposed as:

> n

Y
p(y1,...,yn) = p(yi|y1,...,yi−1,X) (16.6)
我们可以通过贪心解码产生输出的每个字母：

> We can produce each letter of the output via greedy decoding:

> i=1

ˆyi = argmaxchar∈AlphabetP(char|y1...yi−1,X) (16.7)
另外，像 Whisper 或 OWSM 这样的编码器-解码器也使用下一节所述的束搜索。这在我们加入语言模型时尤为相关。

> Alternatively encoder-decoders like Whisper or OWSM also use beam search as described in the next section. This is particularly relevant when we are adding a language model.

加入语言模型　由于编码器-解码器模型本质上是一个条件语言模型，编码器-解码器会从训练数据中隐式地学习一个针对字母输出域的语言模型。然而，训练数据（与文本转写配对的语音）可能并不包含足够的文本，无法训练出一个好的语言模型。毕竟，找到海量纯文本训练数据比找到与语音配对的文本要容易。因此，我们通常可以通过引入一个非常大的语言模型，至少略微改进模型。

> Adding a language model Since an encoder-decoder model is essentially a conditional language model, encoder-decoders implicitly learn a language model for the output domain of letters from their training data. However, the training data (speech paired with text transcriptions) may not include sufficient text to train a good language model. After all, it’s easier to find enormous amounts of pure text training data than it is to find text paired with speech. Thus we can can usually improve a model at least slightly by incorporating a very large language model.

最简单的方法是使用束搜索得到一束假设句子的最终束；这个束有时被称为 n-best 候选列表。然后我们用一个

> The simplest way to do this is to use beam search to get a final beam of hypothesized sentences; this beam is sometimes called an n-best list. We then use a

> `n-best list rescore`（n-best 候选列表重打分）
>
> 释义：用外部语言模型对束搜索得到的多个候选转写重新计算得分，以便在其中选出最优结果。

语言模型对束中的每个假设重新打分。打分方式是将语言模型给出的分数与用于生成该束的编码器-解码器分数进行插值，权重 λ 在留出集上调优。此外，由于大多数模型偏好较短的句子，ASR 系统通常有某种加入长度因子的方式。一种做法是用假设中的字符数 |Y|c 对概率做归一化。以下是 listen, attend and spell（Chan 等，2016）的打分函数：

> language model to rescore each hypothesis on the beam. The scoring is done by interpolating the score assigned by the language model with the encoder-decoder score used to create the beam, with a weight λ tuned on a held-out set. Also, since most models prefer shorter sentences, ASR systems normally have some way of adding a length factor. One way to do this is to normalize the probability by the number of characters in the hypothesis |Y|c. The following is the scoring function for Listen, Attend, and Spell (Chan et al., 2016):

1
score(Y|X) = logP(Y|X)+λ logPLM(Y) (16.8)
|Y|c

### 16.3.3 学习

> 16.3.3 Learning

用于语音的编码器-解码器使用条件语言模型通常采用的普通交叉熵损失进行训练。在解码的时间步 i，损失是正确词元（字母）yi 的对数概率：

> Encoder-decoders for speech are trained with the normal cross-entropy loss generally used for conditional language models. At timestep i of decoding, the loss is the log probability of the correct token (letter) yi:

LCE = −log p(yi|y1,...,yi−1,X) (16.9)
整个句子的损失是这些损失之和：

> The loss for the entire sentence is the sum of these losses:

> m

X
LCE = − log p(yi|y1,...,yi−1,X) (16.10)
然后该损失通过整个端到端模型反向传播，以训练整个编码器-解码器。

> This loss is then backpropagated through the entire end-to-end model to train the entire encoder-decoder.

> i=1

正如我们在第 13 章所述，我们通常使用教师强制，其中

> As we described in Chapter 13, we normally use teacher forcing, in which the
解码器历史被强制设为正确的标准答案 yi，而不是预测的 ˆyi。也可以混合使用标准答案与解码器输出，例如 90% 的时间使用标准答案输出，而以 0.1 的概率改用解码器输出：

> decoder history is forced to be the correct gold yi rather than the predicted ˆyi. It’s also possible to use a mixture of the gold and decoder output, for example using the gold output 90% of the time, but with probability .1 taking the decoder output instead:

LCE = −log p(yi|y1,..., ˆyi−1,X) (16.11)
现代数据规模相当大。例如，Whisper-v2 在一个语料库上训练，该语料库

> Modern data sizes are quite large. For example Whisper-v2 is trained on a corpus
由 680,000 小时语音组成，主要来自英语，但也包括来自其他 96 种语言的 118,000 小时。数据质量很重要，因此从网络抓取训练数据的系统会实现一些方法，从训练语料中移除由 ASR 生成的转写，例如过滤全大写或全小写的数据。开放的 OWSM 系统在 180k 小时数据上训练，主要是人工转写的公开可用数据，包括 LibriSpeech 和 Multilingual LibriSpeech、Common Voice、FLEURS、Switchboard、AMI 等数据集；详见（Peng 等，2023）。

> of 680,000 hours of speech, mostly from English, but also including 118,000 hours from 96 other languages. Data quality is important, so systems that scrape web data for training implement methods to remove ASR-generated transcripts from their training corpora, such as filtering data that is all uppercase or all lowercase. The open OWSM system is trained on 180k hours, mainly hand-transcribed publicly available data, including such datasets as LibriSpeech and Multilingual LibriSpeech, Common Voice, FLEURS, Switchboard, AMI, and others; see (Peng et al., 2023) for details.

## 16.4 自监督模型：HuBERT

> 16.4 Self-supervised models: HuBERT

编码器-解码器架构的一种替代方案是这一类自监督

> An alternative to the encoder-decoder architecture are the class of self-supervised

> `self-supervised`（自监督）
>
> 释义：指不依赖人工标注转写、只利用无标注语音波形自行构造训练目标的预训练方式。

语音模型。这些模型并不直接学习将声学输入映射为字母和词元组成的字符串。相反，它们先从声学输入中自助地构造出一组离散的音素单元，学习从波形映射到这些诱导出的单元。这个预训练阶段不需要转写，只需要无标注的语音文件。

> speech models. These models don’t directly learn to map an acoustic input to a string of letters and tokens. Instead, they first bootstrap a set of discrete phonetic units from the acoustic input, learning to map from waveforms to these induced units. This pretraining phase doesn’t require transcripts; just unlabeled speech files.

预训练之后，这些模型可以在较小的有标注数据集（与转写配对的音频）上微调来做 ASR。这些模型的优势在于，它们能在训练的大部分阶段利用大量未转写的音频。

> After they are pretrained, these models can then be fine-tuned to do ASR on a smaller set of labeled data, audio paired with transcripts. These models have the advantage that they can take advantage of large amounts of untranscribed audio for most of their training.

这里我们将介绍一个名为 HuBERT 的自监督模型（Hsu 等，

> Here we’ll introduce one self-supervised model called HuBERT (Hsu et al.,

> `HuBERT`
>
> 释义：一种自监督语音表示学习模型，通过预测被掩码帧所属的聚类声学单元来完成预训练。

2021）。HuBERT 以及 wav2vec 2.0（Baevski 等，2020）等类似模型使用了

> 2021). HuBERT and similar models like wav2vec 2.0 (Baevski et al., 2020) use the

> `wav2vec 2.0`
>
> 释义：一种自监督语音预训练模型，在隐层表示上施加掩码并预测量化后的离散单元。

与第 9 章介绍的 BERT 等掩码语言模型相同的思路：我们遮蔽输入的一部分，并训练模型去猜测被掩码遮住的内容。

> same intuition as the masked language models like BERT introduced in Chapter 9: we mask out some part of the input and train the model to guess what was hidden by the mask.

![](images/16-speech-recognition/fig_p13_0.png)

*图 16.8 训练中 HuBERT 推理过程的示意架构。一个 16kHz 的 wav 文件经过一系列卷积层，部分帧被替换为 MASK 词元，随后该序列经过 Transformer 堆栈，再经过一个线性层，将 Transformer 的输出投影为输出嵌入。该嵌入与 100/500 个语音类各自的嵌入通过余弦进行比较，产生一个 logit，再经过 softmax 得到每一帧上各类别的概率分布。*
*Figure 16.8 Schematic architecture for the HuBERT inference pass in training. A 16kHz wavfile is passed through a series of convolutional layers, some frames are replaced with a MASK token, and then the sequence is passed though a transformer stack, and then a linear layer that projects the transformer output to an output embedding. This embedding is compared via cosine with the embeddings for each of the 100/500 phonetic classes to produce a logit which is passed through softmax to get a probability distribution over the classes at each frame.*

### 16.4.1 HuBERT 的前向传播

> 16.4.1 HuBERT forward pass

我们先只展示训练中所用的 HuBERT 前向传播，然后再结合反向传播在完整的训练语境中来看它。如前所述，HuBERT 前向传播的输入是原始的 16kHz 波形文件，而在每个 20ms 时间帧上的输出是定义在诱导出的一组语音类别 C（100 类或 500 类，取决于所处阶段）上的概率分布。图 16.8 给出了各部件的示意图。波形文件经过 7 个 512 通道的卷积层，这些卷积层既要学习提取频谱信息，又要将输入序列缩短到 20 ms 一帧，之后加入位置编码，再经过 GELU 和层归一化。随后，部分选定的词元被替换为一个掩码词元，这是一个训练得到的嵌入，被所有被掩码的帧共享。

> Let’s first show just the forward pass for HuBERT used during training, and then we’ll see this in its full training context with the backwards pass. As discussed earlier, the input to the HuBERT forward pass is raw 16kHz wavefiles as input, and the output at each 20ms time frame will be a probability distribution over a set of induced phonetic classes C (100 classes or 500 classes, depending on the stage). Fig. 16.8 shows a sketch of the components. The wavefile is passed through 7 512-channel convolutional layers which learn both to extract spectral information, and to shorten the input sequence down to a 20 ms frame, after which positional encodings are added, and then GELU and layer norm. Selected tokens are then replaced with a mask token, a trained embedding that is shared by all masked frames.

整个序列经过一个 Transformer 堆栈，其输出再经过一个线性投影层 A。随后，每个 20ms 帧上的输出嵌入与 100（/500）个语音类各自的嵌入通过余弦进行比较，得到一组 100 个 logit，表示当前 20ms 音频时间步与每一个类别的相似度。这些 logit 再经过 softmax，得到各类别上的概率分布。

> The whole sequence is passed through a transformer stack, and the output is passed through a linear projection layer A. The output embedding at each 20ms frame is then compared via cosine with each of the embeddings for the 100 (/500) phonetic classes, resulting in a set of 100 logits representing the similarity of the current 20ms audio timestep to each class. These are then passed through a softmax to get a probability distribution over the classes.

### 16.4.2 HuBERT 的学习

> 16.4.2 Learning for HuBERT

我们先讨论如何诱导出作为训练目标的 100 或 500 个语音类别。为了启动这些单元，HuBERT 从梅尔频率倒谱系数（mel frequency cepstral coefficients，MFCC）向量入手，这是一种 39 维特征向量，强调信号中与检测语音单元相关的方面。这些向量可以按第 15.6 节所述从声学信号中提取。我们对整个声学训练数据集提取 MFCC 向量（原始 HuBERT 实现使用了 960 小时的 LibriSpeech 数据，得到 1.72 亿个向量）。接着，我们用第 16.4.3 节所述的 k-means 聚类算法对 MFCC 向量进行聚类。聚类是指把向量分成 k 类。聚类的输出是一个包含 k 个向量的码本，这些向量称为码字或模板或原型，每个代表一个聚类。这 k 个聚类中的每一个都是一个声学单元，可用作训练的黄金目标。

> Let’s first discuss how we induce the 100 or 500 phonetic classes that are the target of training. To bootstrap these units, HuBERT starts with mel frequency cepstral coefficients, or MFCC vectors, a 39-dimensional feature vector that emphasizes aspects of the signal that are relevant for detection of phonetic units. These vectors can be extracted from the acoustic signal as summarized in Section 15.6. We extract MFCC vectors for the entire acoustic training dataset (the original HuBERT implementation used 960 hours of LibriSpeech data resulting in 172 million vectors). Next we cluster the MFCC vectors using the k-means clustering algorithm described below in Section 16.4.3. Clustering means to group the vectors into k classes. The output of clustering is a codebook of k vectors, called codewords or templates or prototypes, each representing a cluster. Each of these k clusters is an acoustic unit that we can use as the gold targets for training.

现在我们来看整个训练过程。声学输入经过

> Now let’s consider the entire training process. After the acoustic input is run
CNN 层之后，上下文窗口中有一段词元被选作掩码，对这些词元而言，CNN 的输出被替换为一个 MASK 嵌入。

> through the CNN layers, a span of tokens in the context window is chosen to be masked, and for those tokens the CNN output is replaced by a MASK embedding.

整个上下文窗口经过 Transformer 层，每个时间步 t 上的 Transformer 输出 hL t 乘以投影层矩阵 A，将其投影到类别嵌入空间。得到的表示再与 C 中每个类别的嵌入进行比较（使用余弦相似度），并用 softmax（温度参数 τ=0.1）把相似度转成概率：

> The entire context window is passed through the transformer layers, and the transformer output hL t at each timestep t is multiplied by the projection layer matrix A to project it into the class embedding space. The resulting representation is then compared to the embedding for each of the classes in C (using cosine), and a softmax(with temperature parameter τ=0.1) is used to turn the similarity into a probability:

exp(sim(Aht,ec)/τ)
p(c|X,t) = (16.12)
PC c′=1 exp(sim(Aht,ec′)/τ)
如图 16.9 所示，与这一前向传播并行地，输入波形

> As Fig. 16.9 shows, in parallel with this forward pass, the input waveform is
经过 MFCC 处理，生成一个 39 维向量，再通过在码本中选择最相似的质心，将其映射到 100 个类别之一。于是损失函数就是模型赋予这些正确单元的概率在掩码词元集合 M 上的求和：

> passed through an MFCC to create a 39-dimensional vector which is then mapped to one of the 100 classes by choosing the most similar centroid in the codebook. The loss function is then the sum, over the set of masked tokens M, of the probability that the model assigns to these correct units:

X
L = log p(zt|X) (16.13)
因此，正如掩码语言建模那样，模型被训练来预测与掩码帧相关联的单元。该损失随后通过模型反向传播

> Thus, as in masked language modeling, the model is being trained to predict the units associated with the masked frames. This loss is then backpropagated through the model

![](images/16-speech-recognition/fig_p15_0.png)

*图 16.9 HuBERT 训练的第一阶段。一个包含 100 个单元的码本（定义为 39 维 MFCC 向量的聚类）被用作训练目标。对每个时间步 t，计算该类别的概率，并用对数概率作为损失。*
*Figure 16.9 The first phase of HuBERT training. A codebook of 100 units (defined as clusters of 39-dimensional MFCC vectors) is used as the targets for training. For each timestep t, computes the probability of that class, and uses the logprob as the loss.*

一旦模型初步训练到能够映射到 MFCC 向量质心，

> Once the model has been initially trained to map to MFCC vector centroids, a
就进入训练的第二阶段：我们取模型产生的表示，将它们聚成 500 个聚类，并改用这些聚类作为训练目标。

> second stage of training occurs, where we take the representations produced by the model, cluster them into 500 clusters, and use those instead as the target for training.

其直觉是：初始的 MFCC 聚类会使模型偏向语音表示，但经过足够的训练后，模型会学到更准确、更细粒度的表示。图 16.10 展示了这一直觉。

> The intuition is that the initial MFCC clusters will bias the model toward phonetic representations, but after enough training the model will learn more accurate and fine-grained representations. Fig. 16.10 shows the intuition.

![](images/16-speech-recognition/fig_p15_1.png)

*图 16.10 为 HuBERT 两个训练阶段创建目标。在第一阶段，通过对整个训练数据计算 39 维 MFCC 向量并用 k-means 对其聚类，创建出 100 个声学单元。在第二阶段，通过在第一阶段训练之后将训练数据的一个子样本送入 HuBERT 模型，取中间某一层 Transformer（第 6 层）的输出并用 k-means 对其聚类，创建出 500 个单元。*
*Figure 16.10 Creating the targets for the two stages of HuBERT training. In the first stage, 100 acoustic units are created by computing 39-dimensional MFCC vectors for the entire training data and then clustering them with k-means. In the second stage, 500 units are created by passing a subsample of the training data through the HuBERT model after the first stage training, taking the output of an intermediate transformer layer (layer 6) and clustering them with k-means.*

HuBERT 预训练完成后，投影层和余弦层被移除，

> After HuBERT has been pretrained, the projection and cosine layers are removed
并加入一个随机初始化的线性 + softmax 层，映射到 29 个类别

> and a randomly initialized linear + softmax layer is added, mapping into 29 classes

![](images/16-speech-recognition/fig_p16_0.png)

*图 16.11 预训练之后 HuBERT 的微调过程。投影层和余弦步骤被移除，只留下一个随机初始化的投影/softmax 层。CNN 层被冻结，模型其余部分在带有转写文本的音频数据集上微调，使用 CTC 损失（第 16.5 节）训练，输出为字母。微调中更新的参数以红色显示（投影层和 Transformer 堆栈）。*
*Figure 16.11 The HuBERT fine-tuning pass after pretraining. The projection layer and cosine steps are removed, leaving only a randomly initialized projection/softmax layer. The CNN layers are frozen, and the rest of the model is fine-tuned on a dataset of audio with transcripts, trained with the CTC loss (Section 16.5) to produce letters as output. The parameters that are updated in fine-tuning are shown in red (the projection layer and the transformer stack).*

（对应 26 个英文字母和少量额外字符），以用于 ASR 任务。

> (corresponding to the 26 English letters and a few extra characters) for the ASR task.

CNN 被冻结，模型其余部分使用将在第 16.5 节描述的 CTC 损失函数针对 ASR 进行微调。

> The CNNs are frozen and the rest of the model is fine-tuned for ASR using the CTC loss function to be described in Section 16.5.

### 16.4.3 k-means 聚类

> 16.4.3 K-means clustering

本节我们更正式地给出 k-means 聚类算法。k-means

> In this section we give the k-means clustering algorithm more formally. K-means

> `k-means`
>
> 释义：一种迭代式聚类算法，通过反复更新 k 个质心把向量划归到 k 类，用于离散化连续向量。

是一类把一组向量数据划分成 k 个聚类的算法。每当我们希望以相同方式对待一组元素时，聚类就很有用。在语音处理中，每当我们需把一组实值向量转换为一组离散符号时，就常会用到它。除了在 HuBERT 中的这一用途，我们还会在第 18 章重新回到它，把它作为为 TTS 创建离散声学词元的算法。

> is a family of algorithms for grouping a set of vector data into k clusters. Clustering is useful whenever we want to treat a group of elements in the same way. In speech processing it is very commonly used whenever we need to convert a set of vectors over real values into a set of discrete symbols. Besides its use here in HuBERT, we’ll return to it in Chapter 18 as an algorithm for creating discrete acoustic tokens for TTS.

我们通常用 k-means 这个名字指代这一族中最简单的版本：

> We generally use the name k-means to mean a simple version of the family:

一种两步迭代算法，给定 N 个向量 v(1)..v(N)，每个为 d 维，即 ∀i,v(i) ∈Rd，以及一个常数 k，通常 N >> k。

> a two-step iterative algorithm that is given a set of N vectors v(1)..v(N) each of d dimensions, i.e. ∀i,v(i) ∈Rd, and a constant k, where usually N >> k.

这一两步算法基于对 k 个质心向量的迭代更新。质心是一组点在 n 维空间中的几何中心。

> The two-step algorithm is based on iteratively updating a set of k centroid vectors. A centroid is the geometric center of a set of a points in n-dimensional space.

> `centroid`（质心）
>
> 释义：指一组点在 n 维空间中的几何中心，在 k-means 中作为每个聚类的代表向量。

该算法包含两个步骤。在分配步骤中，给定一组 k 个当前质心和一组向量数据集，它把每个向量分配到码字与其最接近（以平方欧氏距离衡量）的簇。在重估步骤中，它通过重新计算均值向量来重新计算每个簇的码字。注意，得到的均值向量不必是数据集中的实际点。我们在这两个步骤之间反复迭代。

> The algorithm has two steps. In the assignment step, given a set of k current centroids and a dataset of vectors, it assigns each vector to the cluster whose codeword is the closest (by squared Euclidean distance). In the re-estimation step, it recomputes the codeword for each cluster by recomputing the mean vector. Note that the resulting mean vector need not be an actual point from the dataset. We iterate back and forth between these two steps.

算法如下：初始化：对每个簇 k，随机选择一个向量 µk ∈Rd 作为该簇的码字（也称为模板或原型）。其结果是一个码本，其中 k 个簇各有一个码字。

> Here’s the algorithm: Initialization: For each cluster k choose a random vector µk ∈Rd to be the codeword (also called template or prototype) for the cluster. The result is a codebook that has one codeword for each of the k clusters.

> `codeword template prototype codebook`（码字、模板、原型、码本）
>
> 释义：聚类中代表每个簇的向量；簇的码字也称模板或原型，全部簇的码字合起来构成码本。

然后迭代重复直至收敛：

> Then repeat iteratively until convergence:

- 分配：对数据集中的每个向量 v(i)，将其分配到 k 个簇之一，即选择码字 µ 最近的那个簇。最简单地，我们可以把“最近”定义为码字到 v(i) 的平方欧氏距离最小的簇。

> Assignment: For each vector v(i) in the dataset assign it to one of the k clusters by choosing the one with the nearest codeword µ. Most simply we can define‘nearest’ as the cluster whose codeword has the smallest squared Euclidean distance to v(i).

cluster(i) = argmin ||v(i) −µj||2 (16.14)
其中 ||v|| 是向量 Pd j=1 v2 的 L2 范数

> where ||v|| is the L2 norm of the vector Pd j=1 v2

> 1<j<k

> j

- 重估：通过重新计算簇中所有向量的均值（质心）来重新估计每个簇的码字。若 Si 是簇 i 中向量的集合，则

> Re-estimation: Re-estimate the codeword for each cluster by recomputing the mean (centroid) of all the vectors in the cluster. If Si is the set of vectors in cluster i, then

∀i :

1 X (16.15)
µi = |Si| v

> v∈Si

## 16.5 CTC

在上一节我们指出，语音识别有两个特殊性质，使它非常适合编码器-解码器架构——在该架构中，编码器产生输入的编码，解码器用注意力来探索这一编码。第一，语音中很长的声学输入序列 X 映射到短得多的字母序列 Y；第二，很难确切知道 X 的哪一部分映射到 Y 的哪一部分。

> We pointed out in the previous section that speech recognition has two particular properties that make it very appropriate for the encoder-decoder architecture, where the encoder produces an encoding of the input that the decoder uses attention to explore. First, in speech we have a very long acoustic input sequence X mapping to a much shorter sequence of letters Y, and second, it’s hard to know exactly which part of X maps to which part of Y.

本节我们简要介绍编码器-解码器的一种替代方案：一种称为 CTC 的算法和损失函数，CTC 是 Connectionist Temporal Classification（连接主义时间分类）的缩写（Graves et al., 2006），它以非常不同的方式处理这些问题。CTC 的直观想法是：为输入的每一帧输出单个字符，使输出与输入长度相同，然后应用一个折叠函数把相同的字母序列合并，从而得到更短的序列。

> In this section we briefly introduce an alternative to encoder-decoder: an algorithm and loss function called CTC, short for Connectionist Temporal Classification (Graves et al., 2006), that deals with these problems in a very different way. The intuition of CTC is to output a single character for every frame of the input, so that the output is the same length as the input, and then to apply a collapsing function that combines sequences of identical letters, resulting in a shorter sequence.

> `CTC`
>
> 释义：连接主义时间分类，一种为输入的每一帧输出一个字符、再用折叠函数合并相同字母的语音识别算法与损失函数。

让我们设想对某人说出单词 dinner 时进行推断，并假设

> Let’s imagine inference on someone saying the word dinner, and let’s suppose
我们有一个函数，它为每个输入频谱帧表示 xi 选出最可能的字母。我们把与每个输入帧对应的字母序列称为一个对齐，因为它告诉我们每个字母对齐到声学信号中的哪个位置

> we had a function that chooses the most probable letter for each input spectral frame representation xi. We’ll call the sequence of letters corresponding to each input frame an alignment, because it tells us where in the acoustic signal each letter aligns

> `alignment`（对齐）
>
> 释义：将假设词串与参考词串逐词匹配，标出替换、插入和删除的位置，用于统计错误数量。

的位置。图 16.12 展示了这样一种对齐，以及如果我们使用仅删除连续重复字母的折叠函数会发生什么。

> to. Fig. 16.12 shows one such alignment, and what happens if we use a collapsing function that just removes consecutive duplicate letters.

嗯，这样并不奏效；我们朴素的算法把这段语音转写成了 diner，

> Well, that doesn’t work; our naive algorithm has transcribed the speech as diner,
而不是 dinner！折叠无法处理重复的字母。我们朴素的函数还有另一个问题：它没有告诉我们输入中的静音应当对齐到哪个符号。我们可不想把静音转写成随机的字母！

> not dinner! Collapsing doesn’t handle double letters. There’s also another problem with our naive function; it doesn’t tell us what symbol to align with silence in the input. We don’t want to be transcribing silence as random letters!

CTC 算法通过向转写字母表中加入

> The CTC algorithm solves both problems by adding to the transcription alphabet
一个表示空白的特殊符号来解决这两个问题，我们把它记作 。该空白符号可用于

> a special symbol for a blank, which we’ll represent as . The blank can be used in

> `blank`（空白符号）
>
> 释义：CTC 字母表中新增的特殊符号，用于在不需要转写字母的位置（如静音处）占位。

对齐中任何我们不想转写字母的位置。空白符号也可以用在字母之间；由于我们的折叠函数只折叠连续的重复字母，它不会跨越 折叠。更形式化地，让我们定义映射 B : a →y

> the alignment whenever we don’t want to transcribe a letter. Blank can also be used between letters; since our collapsing function collapses only consecutive duplicate letters, it won’t collapse across . More formally, let’s define the mapping B : a →y

![](images/16-speech-recognition/fig_p18_0.png)

*图 16.12 一种用于折叠输入与字母之间对齐的朴素算法。*
*Figure 16.12 A naive algorithm for collapsing an alignment between input and letters.*

表示对齐 a 与输出 y 之间的映射，它折叠所有重复的字母，然后删除所有空白。图 16.13 勾勒了这个折叠函数 B。

> between an alignment a and an output y, which collapses all repeated letters and then removes all blanks. Fig. 16.13 sketches this collapsing function B.

![](images/16-speech-recognition/fig_p18_1.png)

*图 16.13 CTC 折叠函数 B，展示了空格 空白字符 ；对齐 A 中重复（连续）的字符被删除以形成输出 Y。*
*Figure 16.13 The CTC collapsing function B, showing the space blank character ; repeated (consecutive) characters in an alignment A are removed to form the output Y.*

CTC 折叠函数是多对一的；许多不同的对齐都映射

> The CTC collapsing function is many-to-one; lots of different alignments map
到同一个输出字符串。例如，图 16.13 所示的对齐并不是唯一能产生字符串 dinner 的对齐。图 16.14 展示了其他一些会得到相同输出的对齐。

> to the same output string. For example, the alignment shown in Fig. 16.13 is not the only alignment that results in the string dinner. Fig. 16.14 shows some other alignments that would produce the same output.

![](images/16-speech-recognition/fig_p18_2.png)

*图 16.14 另外三个产生转写结果 dinner 的合法对齐。*
*Figure 16.14 Three other legitimate alignments producing the transcript dinner.*

考虑可能产生同一输出的所有对齐所构成的集合是有用的

> It’s useful to think of the set of all alignments that might produce the same output

- 我们将使用 B 函数的逆像，称为 B−1，并把该集合表示为 B−1(Y)。

> We’ll use the inverse image of our B function, called B−1, and represent that set as B−1(Y).

### 16.5.1 CTC 推断

> 16.5.1 CTC Inference

在我们了解如何计算 PCTC(Y|X) 之前，先看看 CTC 如何为一个特定的对齐 ˆA = { ˆa1,..., ˆan} 分配概率。CTC 做了一个很强的条件独立性假设：它假设在给定输入 X 的条件下，CTC 模型在时刻 t 的输出与任何其他时刻 ai 的输出标签相互独立。因此：

> Before we see how to compute PCTC(Y|X) let’s first see how CTC assigns a probability to one particular alignment ˆA = { ˆa1,..., ˆan}. CTC makes a strong conditional independence assumption: it assumes that, given the input X, the CTC model output at at time t is independent of the output labels at any other time ai. Thus:

TY
PCTC(A|X) = p(at|X) 因此，为了找到最佳对齐 ˆA = { ˆa1,..., ˆaT}，我们可以在每个时间步 t 贪心地选择概率最大的字符：

> PCTC(A|X) = p(at|X) Thus to find the best alignment ˆA = { ˆa1,..., ˆaT} we can greedily choose the character with the max probability at each time step t:

ˆat = argmax pt(c|X) (16.17)
随后，我们把得到的序列 A 传给 CTC 合并函数 B，从而得到输出序列 Y。

> We then pass the resulting sequence A to the CTC collapsing function B to get the output sequence Y.

> c∈C

我们来讨论一下这个用于寻找最佳对齐 A 的简单推理算法将如何实现。由于我们在每个时间点都要做出决策，可以把 CTC 视为一个序列建模任务：在时间步 t 输出一个字母 ˆyt，对应于每个输入 token xt，从而无需完整的解码器。图 16.15 给出了该架构的示意：我们取一个编码器，在每个时间步产生一个隐状态 ht，并在每个时间步对字符词表做 softmax 来完成解码。

> Let’s talk about how this simple inference algorithm for finding the best alignment A would be implemented. Because we are making a decision at each time point, we can treat CTC as a sequence-modeling task, where we output one letterˆyt at time t corresponding to each input token xt, eliminating the need for a full decoder. Fig. 16.15 sketches this architecture, where we take an encoder, produce a hidden state ht at each timestep, and decode by taking a softmax over the character vocabulary at each time step.

![](images/16-speech-recognition/fig_p19_0.png)

*图 16.15 使用 CTC 进行推理：采用仅编码器模型，在每个输出步对隐状态 ht 做简单的 softmax 来完成解码。*
*Figure 16.15 Inference with CTC: using an encoder-only model, with decoding done by simple softmaxes over the hidden state ht at each output step.*

可惜的是，(式 16.17) 中勾勒的推理算法存在一个潜在缺陷

> Alas, there is a potential flaw with the inference algorithm sketched in (Eq. 16.17)
以及图 16.14 中。问题在于，我们选择了最可能对齐 A，但最可能的对齐未必对应于最可能的最终合并输出串 Y。这是因为有许多可能的对齐都会导致相同的输出串，因此最可能的输出串未必对应于最可能的对齐。例如，设想输入 X = [x1x2x3] 最可能的对齐 A 是串 [a b ϵ]，而次可能的两个对齐是 [b ϵ b] 和 [ϵ b b]。输出 Y =[b b] 对这两个对齐求和后，可能比 Y =[a b] 更可能。

> and Fig. 16.14. The problem is that we chose the most likely alignment A, but the most likely alignment may not correspond to the most likely final collapsed output string Y. That’s because there are many possible alignments that lead to the same output string, and hence the most likely output string might not correspond to the most probable alignment. For example, imagine the most probable alignment A for an input X = [x1x2x3] is the string [a b ϵ] but the next two most probable alignments are [b ϵ b] and [ϵ b b]. The output Y =[b b], summing over those two alignments, might be more probable than Y =[a b].

出于这个原因，最可能的输出序列 Y 并不是拥有

> For this reason, the most probable output sequence Y is the one that has, not
单个最佳 CTC 对齐的那个，而是其所有可能对齐概率求和最高者：

> the single best CTC alignment, but the highest sum over the probability of all its possible alignments:

X
PCTC(Y|X) = P(A|X)
X TY
= p(at|ht)
ˆY = argmax PCTC(Y|X) 可惜的是，对所有对齐求和代价极高（对齐数量非常庞大），因此我们通过一种 Viterbi 束搜索的变体来近似这个求和：它巧妙地在束中保留那些映射到同一输出串的高概率对齐，并将它们求和作为 (式 16.18) 的近似。关于这种针对 CTC 的束搜索扩展的清晰解释，参见 Hannun (2017)。

> ˆY = argmax PCTC(Y|X) Alas, summing over all alignments is very expensive (there are a lot of alignments), so we approximate this sum by using a version of Viterbi beam search that cleverly keeps in the beam the high-probability alignments that map to the same output string, and sums those as an approximation of (Eq. 16.18). See Hannun (2017) for a clear explanation of this extension of beam search for CTC.

> A∈B−1(Y)

> A∈B−1(Y) t=1

由于前面提到的强条件独立性假设

> Because of the strong conditional independence assumption mentioned earlier
（即在给定输入的条件下，时间 t 的输出与时间 t−1 的输出相互独立），CTC 并不会在数据上隐式地学习一个语言模型（不同于基于注意力的编码器-解码器架构）。因此，使用 CTC 时，必须用在一个开发集上训练得到的插值权重来插值一个语言模型（以及某种长度因子 L(Y)）：

> (that the output at time t is independent of the output at time t −1, given the input), CTC does not implicitly learn a language model over the data (unlike the attentionbased encoder-decoder architectures). It is therefore essential when using CTC to interpolate a language model (and some sort of length factor L(Y)) using interpolation weights that are trained on a devset:

scoreCTC(Y|X) = logPCTC(Y|X)+λ1 logPLM(Y)λ2L(Y) (16.19)

### 16.5.2 CTC 训练

> 16.5.2 CTC Training

为了训练基于 CTC 的 ASR 系统，我们使用带有特殊 CTC 损失函数的负对数似然损失。于是，整个数据集 D 的损失就是每个输入 X 对应正确输出 Y 的负对数似然之和：

> To train a CTC-based ASR system, we use negative log-likelihood loss with a special CTC loss function. Thus the loss for an entire dataset D is the sum of the negative log-likelihoods of the correct output Y for each input X:

X
LCTC = −logPCTC(Y|X) (16.20)
要计算单个输入对 (X,Y) 的 CTC 损失函数，我们需要给定输入 X 时输出 Y 的概率。正如我们在式 16.18 中看到的，要计算给定输出 Y 的概率，我们需要对所有会合并为 Y 的可能对齐求和。换言之：

> To compute CTC loss function for a single input pair (X,Y), we need the probability of the outputY given the input X. As we saw in Eq. 16.18, to compute the probability of a given output Y we need to sum over all the possible alignments that would collapse to Y. In other words:

> (X,Y)∈D

X TY
PCTC(Y|X) = p(at|ht) (16.21)
朴素地对所有可能对齐求和并不可行（对齐数量太多）。不过，我们可以用动态规划来合并对齐，从而高效地计算这个求和，所用的是一种同样用于训练 HMM（附录 A）和 CRF 的前向-后向算法。训练与推理各自的原始动态规划算法见 (Graves et al., 2006)；关于两者的详细解释参见 (Hannun, 2017)。

> Naively summing over all possible alignments is not feasible (there are too many alignments). However, we can efficiently compute the sum by using dynamic programming to merge alignments, with a version of the forward-backward algorithm also used to train HMMs (Appendix A) and CRFs. The original dynamic programming algorithms for both training and inference are laid out in (Graves et al., 2006); see (Hannun, 2017) for a detailed explanation of both.

> A∈B−1(Y) t=1

### 16.5.3 结合 CTC 与编码器-解码器

> 16.5.3 Combining CTC and Encoder-Decoder

也可以把我们描述的两种架构/损失函数结合起来，即来自编码器-解码器架构的交叉熵损失与 CTC 损失。

> It’s also possible to combine the two architectures/loss functions we’ve described, the cross-entropy loss from the encoder-decoder architecture, and the CTC loss.

图 16.16 给出了示意。训练时，我们只需用在开发集上调好的 λ 对两种损失加权：

> Fig. 16.16 shows a sketch. For training, we can simply weight the two losses with aλ tuned on a devset:

L = −λ logPencdec(Y|X)−(1−λ)logPctc(Y|X) (16.22)
推理时，我们可以把两者与语言模型（或长度惩罚）结合，同样使用学习得到的权重：

> For inference, we can combine the two with the language model (or the length penalty), again with learned weights:

ˆY = argmax [λ logPencdec(Y|X)+(1−λ)logPCTC(Y|X)+γ logPLM(Y)] (16.23)

![](images/16-speech-recognition/fig_p21_0.png)

*图 16.16 结合 CTC 与编码器-解码器损失函数。*
*Figure 16.16 Combining the CTC and encoder-decoder loss functions.*

### 16.5.4 流式模型：用 RNN-T 改进 CTC

> 16.5.4 Streaming Models: RNN-T for improving CTC

由于 CTC 中的强独立性假设（假设时间 t 的输出与时间 t−1 的输出相互独立），基于 CTC 的识别器无法达到基于注意力的编码器-解码器识别器那样高的准确率。然而，CTC 识别器的优势在于它们可用于流式处理。流式意味着在线识别词语，而不必等到

> Because of the strong independence assumption in CTC (assuming that the output at time t is independent of the output at time t −1), recognizers based on CTC don’t achieve as high an accuracy as the attention-based encoder-decoder recognizers. CTC recognizers have the advantage, however, that they can be used for streaming. Streaming means recognizing words on-line rather than waiting until

> `streaming`（流式处理）
>
> 释义：指边接收语音输入边进行识别、不等待整句说完就输出结果的识别方式。

句子结束才能识别它们。流式处理对许多应用都至关重要，从命令到听写，我们都希望在用户仍在说话时就开始识别。使用注意力机制的算法必须先在整个输入上计算隐状态序列，以便为注意力分布提供上下文，之后解码器才能开始解码。相比之下，CTC 算法可以立即从左到右输入字母。

> the end of the sentence to recognize them. Streaming is crucial for many applications, from commands to dictation, where we want to start recognition while the user is still talking. Algorithms that use attention need to compute the hidden state sequence over the entire input first in order to provide the attention distribution context, before the decoder can start decoding. By contrast, a CTC algorithm can input letters from left to right immediately.

如果我们想实现流式处理，就需要一种方法来改进 CTC 识别，以去除条件独立假设，使其能够了解输出历史。图 16.17 所示的 RNN 转换器（RNN-T）正是这样一个模型

> If we want to do streaming, we need a way to improve CTC recognition to remove the conditional independent assumption, enabling it to know about output history. The RNN-Transducer (RNN-T), shown in Fig. 16.17, is just such a model

> `RNN-T`（RNN 转换器）
>
> 释义：一种流式语音识别架构，将 CTC 声学编码器与以输出标记历史为条件的预测器语言模型结合，共同预测下一个输出。

（Graves 2012，Graves 等人 2013）。RNN-T 有两个主要组成部分：一个 CTC 声学模型，以及一个称为预测器的独立语言模型组件，它以输出标记历史为条件。在每个时间步 t，CTC 编码器根据输入 x1...xt 输出隐状态 henc。语言模型预测器以前一个输出标记（不计空白）作为输入，输出隐状态 hpred。

> (Graves 2012, Graves et al. 2013). The RNN-T has two main components: a CTC acoustic model, and a separate language model component called the predictor that conditions on the output token history. At each time step t, the CTC encoder outputs a hidden state henc given the input x1...xt. The language model predictor takes as input the previous output token (not counting blanks), outputting a hidden state hpred .

> t

> u

两者被送入另一个网络，其输出再经过 softmax，以预测下一个字符。

> The two are passed through another network whose output is then passed through a softmax to predict the next character.

X
PRNN−T(Y|X) = P(A|X)
X TY
= p(at|ht,y<ut)

> A∈B−1(Y)

> A∈B−1(Y) t=1

## 16.6 ASR 评估：词错误率

> 16.6 ASR Evaluation: Word Error Rate

语音识别系统的标准评估指标是词错误

> The standard evaluation metric for speech recognition systems is the word error

> `word error`（词错误）
>
> 释义：识别器输出词串与参考转写比较时单词层面的错误，由替换、插入与删除三类操作构成。

率。词错误率基于识别器返回的词串（假设词串）与参考转写之间的差异程度。

> rate. The word error rate is based on how much the word string returned by the recognizer (the hypothesized word string) differs from a reference transcription.

计算词错误的第一步是计算最小编辑距离

> The first step in computing word error is to compute the minimum edit distance in

![](images/16-speech-recognition/fig_p22_0.png)

*图 16.17 RNN-T 模型通过整合 CTC 声学编码器的输出与独立的“预测器”语言模型的输出，计算时刻 t 的输出标记分布。*
*Figure 16.17 The RNN-T model computing the output token distribution at time t by integrating the output of a CTC acoustic encoder and a separate ‘predictor’ language model.*

计算假设词串与正确词串之间的词级最小编辑距离，即把正确词串映射为假设词串所需的最少词替换、词插入和词删除次数。词错误率（WER）的定义如下（注意，由于公式中包含插入，错误率可能超过 100%）：

> words between the hypothesized and correct strings, giving us the minimum number of word substitutions, word insertions, and word deletions necessary to map between the correct and hypothesized strings. The word error rate (WER) is then defined as follows (note that because the equation includes insertions, the error rate can be greater than 100%):

Word Error Rate = 100× Insertions+Substitutions+Deletions
Total Words in Correct Transcript
下面给出一个参考话语与假设话语之间的对齐示例，来自

> Here is a sample alignment between a reference and a hypothesis utterance from

> `alignment`（对齐）
>
> 释义：将假设词串与参考词串逐词匹配，标出替换、插入和删除的位置，用于统计错误数量。

CallHome 语料库，展示了用于计算错误率的各项计数：

> the CallHome corpus, showing the counts used to compute the error rate:

> REF: i *** ** UM the PHONE IS i LEFT THE portable **** PHONE UPSTAIRS last night HYP: i GOT IT TO the ***** FULLEST i LOVE TO portable FORM OF STORES last night Eval: I I S D S S S I S S

这句话语有六处替换、三处插入和一处删除：

> This utterance has six substitutions, three insertions, and one deletion:

Word Error Rate = 1006+3+1
= 76.9%
13
计算词错误率的标准方法是一个名为 sclite 的免费脚本，

> The standard method for computing word error rates is a free script called sclite,
可从美国国家标准与技术研究院（NIST）获取（NIST，2005）。Sclite 接收一系列参考句子（人工转写的金标准）以及一组与之匹配的假设句子。除了执行对齐并计算词错误率，sclite 还完成许多其他有用的任务。例如，在错误分析方面，它提供诸如混淆矩阵之类的有用信息，显示哪些词常常被误识别成其他词，并汇总经常被插入或删除的词的统计。sclite 还给出按说话人划分的错误率（如果句子标注了说话人 ID），以及诸如句

> available from the National Institute of Standards and Technologies (NIST) (NIST, 2005). Sclite is given a series of reference (hand-transcribed, gold-standard) sentences and a matching set of hypothesis sentences. Besides performing alignments, and computing word error rate, sclite performs a number of other useful tasks. For example, for error analysis it gives useful information such as confusion matrices showing which words are often misrecognized for others, and summarizes statistics of words that are often inserted or deleted. sclite also gives error rates by speaker(if sentences are labeled for speaker ID), as well as useful statistics like the sentence

> `Sentence error rate`（句子错误率）
>
> 释义：至少含有一个词错误的句子在所有句子中所占的百分比，用于补充词错误率进行系统评估。

错误率，即至少含有一个词错误的句子所占的百分比。

> error rate, the percentage of sentences with at least one word error.

评估前的文本规范化

> Text normalization before evaluation
系统在计算词错误率之前对文本进行规范化是常见做法。有各种软件包可用于实现规范化规则。例如，一些标准的英语规范化规则包括：

> It’s normal for systems to normalize text before computing word error rate. There are a variety of packages for implementing normalization rules. For example some standard English normalization rules include:

- 删除出现在成对括号（[, ]）之间的元语言［非语言内容、注释、转写说明］
- 删除或规范化感叹词或填充停顿（“uh”“um”“err”）
- 统一英语的缩略形式与非缩略形式（“I’m”/“I am”）

> Removing metalanguage [non-language, notes, transcription comments] that occur between matching brackets ([, ])
> Remove or standardize interjections or filled pauses (“uh”, “um”, “err”)
> Standardize contracted and non-contracted forms of English (“I’m”/“I am”)

- 规范化非标准词（数字、数量、日期、时间）［例如“$100
- “One hundred dollars”］
- 统一美式与英式拼写习惯

> Normalize non-standard-words (number, quantities, dates, times) [e.g., “$100
> “One hundred dollars”]
> Unify US and UK spelling conventions

ASR 的统计显著性：MAPSSWE 或 MacNemar

> Statistical significance for ASR: MAPSSWE or MacNemar
与其他语言处理算法一样，我们需要知道词错误率的某一改进是否显著。

> As with other language processing algorithms, we need to know whether a particular improvement in word error rate is significant or not.

用于判断两个词错误率是否不同的标准统计检验

> The standard statistical tests for determining if two word error rates are different
是配对句子片段词错误（Matched-Pair Sentence Segment Word Error，MAPSSWE）检验，由 Gillick 和 Cox（1989）提出。

> is the Matched-Pair Sentence Segment Word Error (MAPSSWE) test, introduced in Gillick and Cox (1989).

MAPSSWE 检验是一种参数检验，它考察的是

> The MAPSSWE test is a parametric test that looks at the difference between
两个系统在若干片段上平均产生的词错误数之间的差异。片段可以相当短，也可以长到整句话语；一般来说，我们希望片段（较短）的数量尽可能多，以便满足正态性假设并使检验效力最大化。该检验要求一个片段中的错误与另一个片段中的错误在统计上相互独立。由于 ASR 系统倾向于使用三元语言模型，我们可以把一个片段定义为两侧都由两个识别器均识别正确的词（或由话轮/话语边界）所界定的区域，以此近似满足这一要求。下面是 NIST（2007）给出的一个包含四个区域的例子：

> the number of word errors the two systems produce, averaged across a number of segments. The segments may be quite short or as long as an entire utterance; in general, we want to have the largest number of (short) segments in order to justify the normality assumption and to maximize power. The test requires that the errors in one segment be statistically independent of the errors in another segment. Since ASR systems tend to use trigram LMs, we can approximate this requirement by defining a segment as a region bounded on both sides by words that both recognizers get correct (or by turn/utterance boundaries). Here’s an example from NIST (2007) with four regions:

> I II III IV

> REF: |it was|the best|of|times it|was the worst|of times| |it was

> SYS A:|ITS |the best|of|times it|IS the worst |of times|OR|it was

> SYS B:|it was|the best| |times it|WON the TEST |of times| |it was

在区域 I 中，系统 A 有两个错误（一个删除和一个插入），而系统 B

> In region I, system A has two errors (a deletion and an insertion) and system B
为零；在区域 III 中，系统 A 有一个错误（一个替换），系统 B 有两个。

> has zero; in region III, system A has one error (a substitution) and system B has two.

我们按如下方式定义变量序列 Z，用以表示两个系统错误数之间的差异：

> Let’s define a sequence of variables Z representing the difference between the errors in the two systems as follows:

Ni 为系统 A 在片段 i 上产生的错误数

> Ni the number of errors made on segment i by system A
Ni 为系统 B 在片段 i 上产生的错误数

> Ni the number of errors made on segment i by system B
Z Ni A −Ni B，i = 1,2,··· ,n，其中 n 是片段数。在上面的例子中，Z 值序列为 {2,−1,−1,1}。直观地说，如果

> Z Ni A −Ni B,i = 1,2,··· ,n where n is the number of segments In the example above, the sequence of Z values is {2,−1,−1,1}. Intuitively, if
两个系统完全相同，那么我们预期平均差异，也就是 Z 值的平均值，应为零。若把差异的真实平均记为 muz，我们便想知道 muz = 0 是否成立。严格遵循 Gillick 和 Cox（1989）的原始提法与记号，我们可以由有限的样本估计真实平均值，即 ˆµz = Pn

> the two systems are identical, we would expect the average difference, that is, the average of the Z values, to be zero. If we call the true average of the differences muz, we would thus like to know whether muz = 0. Following closely the original proposal and notation of Gillick and Cox (1989), we can estimate the true average from our limited sample as ˆµz = Pn
i=1 Zi/n。Zi 的方差的估计值

> i=1 Zi/n. The estimate of the variance of the Zi’s
为

> is
1 X (Zi −µz)2
σ2 (16.24)
z = n−1
令

> Let
ˆµz
W = (16.25)
σz/√n
当 n 足够大（> 50）时，W 近似服从单位方差的正态分布。原假设为 H0 : µz = 0，因此当 2 ∗P(Z ≥|w|) ≤0.05（双尾）或 P(Z ≥|w|) ≤0.05（单尾）时即可拒绝该原假设，其中 Z 服从标准正态分布，w 为 W 的实现值；这些概率可在正态分布的标准表中查得。

> For a large enough n (> 50), W will approximately have a normal distribution with unit variance. The null hypothesis is H0 : µz = 0, and it can thus be rejected if 2 ∗P(Z ≥|w|) ≤0.05 (two-tailed) or P(Z ≥|w|) ≤0.05 (one-tailed), where Z is standard normal and w is the realized value W; these probabilities can be looked up in the standard tables of the normal distribution.

> A

> B

> n

> i=1

早期工作有时使用 McNemar 检验来判定显著性，但 McNemar

> Earlier work sometimes used McNemar’s test for significance, but McNemar’s

> `McNemar’s test`（McNemar 检验）
>
> 释义：一种比较两个识别系统错误率的配对显著性检验，仅在各错误相互独立时适用，而连续语音中相邻词的错误高度相关，故其前提难以满足。

仅当系统产生的错误相互独立时才适用，而这在连续语音识别中并不成立，因为某个词上产生的错误与相邻词上产生的错误高度相关。

> is only applicable when the errors made by the system are independent, which is not true in continuous speech recognition, where errors made on a word are extremely dependent on errors made on neighboring words.

我们能否改进词错误率这一度量？例如，如果有一种不给每个词同等权重的度量会更好，也许对 Tuesday 这类实义词赋予比 a 或 of 这类功能词更高的权重。尽管研究者普遍认为这是个好主意，但要就一种适用于所有 ASR 应用场景的度量达成一致却很困难。

> Could we improve on word error rate as a metric? It would be nice, for example, to have something that didn’t give equal weight to every word, perhaps valuing content words like Tuesday more than function words like a or of. While researchers generally agree that this would be a good idea, it has proved difficult to agree on a metric that works in every application of ASR.

## 16.7 小结

> 16.7 Summary

本章介绍了自动语音识别（ASR）的基本算法。

> This chapter introduced the fundamental algorithms of automatic speech recognition(ASR).

- 语音识别（或称语音转文本）的任务是把声波波形映射为字素序列。
- 语音识别器的输入是一系列声波，这些声波经过采样、量化，并被转换为对数梅尔谱之类的频谱表示。
- 语音识别有两种常见范式：带注意力机制的编码器-解码器模型，以及基于 CTC 损失函数的模型。基于注意力的模型准确率更高，但基于 CTC 的模型更容易适应流式处理：在线输出字素，而不必等到声学输入结束。
- ASR 使用词错误率来评估，即识别假设与标准转写之间的编辑距离。

> The task of speech recognition (or speech-to-text) is to map acoustic waveforms to sequences of graphemes.
> The input to a speech recognizer is a series of acoustic waves. that are sampled, quantized, and converted to a spectral representation like the log mel spectrum.
> Two common paradigms for speech recognition are the encoder-decoder with attention model, and models based on the CTC loss function. Attentionbased models have higher accuracies, but models based on CTC more easily adapt to streaming: outputting graphemes online instead of waiting until the acoustic input is complete.
> ASR is evaluated using the Word Error Rate; the edit distance between the hypothesis and the gold transcription.

## 历史注记

> Historical Notes

到 20 世纪 40 年代末和 50 年代初，人们已开发出若干语音识别系统。贝尔实验室的一个早期系统能够识别单个说话人所说的 10 个数字中的任意一个（Davis 等，1952）。该系统有 10 个依赖于说话人的存储模式，每个数字对应一个，每个模式大致表示该数字的前两个元音共振峰。他们通过选取与输入具有最高相对相关系数的模式，达到了 97%–99% 的准确率。Fry（1959）和 Denes（1959）在伦敦大学学院构建了一个音素识别器，基于类似的模式识别原理识别四个元音和九个辅音。

> A number of speech recognition systems were developed by the late 1940s and early 1950s. An early Bell Labs system could recognize any of the 10 digits from a single speaker (Davis et al., 1952). This system had 10 speaker-dependent stored patterns, one for each digit, each of which roughly represented the first two vowel formants in the digit. They achieved 97%–99% accuracy by choosing the pattern that had the highest relative correlation coefficient with the input. Fry (1959) and Denes(1959) built a phoneme recognizer at University College, London, that recognized four vowels and nine consonants based on a similar pattern-recognition principle.

Fry 和 Denes 的系统首次使用音素转移概率来约束识别器。

> Fry and Denes’s system was the first to use phoneme transition probabilities to constrain the recognizer.

20 世纪 60 年代末和 70 年代初出现了若干重要的范式转变。

> The late 1960s and early 1970s produced a number of important paradigm shifts.

首先是若干特征提取算法，包括高效的快速傅里叶变换（FFT）（Cooley and Tukey, 1965）、倒谱处理在语音上的应用（Oppenheim et al., 1968），以及用于语音编码的 LPC 的提出（Atal and Hanauer, 1971）。其次是若干处理弯折的方法；即对输入信号进行拉伸或压缩，以应对语速和音段长度的差异。求解这一问题的自然算法是动态规划，而且正如我们在附录 A 中所见，该算法为处理此问题被多次重新发明。它在语音处理中的首次应用由 Vintsyuk（1968）完成，不过他的成果未被其他研究者采纳，之后又被 Velichko 和 Zagoruyko（1970）以及 Sakoe 和 Chiba（1971）（以及 1984）重新发明。不久之后，Itakura（1975）把这一动态规划思想与先前仅用于语音编码的 LPC 系数结合起来。由此得到的系统从输入词中提取 LPC 特征，并用动态规划将其与存储的 LPC 模板进行匹配。

> First were a number of feature-extraction algorithms, including the efficient fast Fourier transform (FFT) (Cooley and Tukey, 1965), the application of cepstral processing to speech (Oppenheim et al., 1968), and the development of LPC for speech coding (Atal and Hanauer, 1971). Second were a number of ways of handling warp- ing; stretching or shrinking the input signal to handle differences in speaking rate and segment length when matching against stored patterns. The natural algorithm for solving this problem was dynamic programming, and, as we saw in Appendix A, the algorithm was reinvented multiple times to address this problem. The first application to speech processing was by Vintsyuk (1968), although his result was not picked up by other researchers, and was reinvented by Velichko and Zagoruyko (1970) and Sakoe and Chiba (1971) (and 1984). Soon afterward, Itakura (1975) combined this dynamic programming idea with the LPC coefficients that had previously been used only for speech coding. The resulting system extracted LPC features from incoming words and used dynamic programming to match them against stored LPC templates.

> `warping`（弯折）
>
> 释义：指匹配已存储模式时对输入信号做拉伸或压缩，以应对语速与音段长度差异的处理方式。

这种以非概率方式使用动态规划、将模板与输入语音进行匹配的做法，称为动态时间规整。

> The non-probabilistic use of dynamic programming to match a template against incoming speech is called dynamic time warping.

> `dynamic time warping`（动态时间规整）
>
> 释义：指用动态规划以非概率方式把模板与输入语音对齐匹配的方法，用于处理语速差异。

这一时期的第三项创新是 HMM 的兴起。隐马尔可夫

> The third innovation of this period was the rise of the HMM. Hidden Markov
模型似乎于 1972 年前后在两个实验室被各自独立地应用于语音。其中一个应用源于统计学家的工作，特别是普林斯顿国防分析研究所（Institute for Defense Analyses）的 Baum 及其同事，他们把 HMM 应用于各种预测问题（Baum and Petrie 1966, Baum and Eagon 1967）。

> models seem to have been applied to speech independently at two laboratories around 1972. One application arose from the work of statisticians, in particular Baum and colleagues at the Institute for Defense Analyses in Princeton who applied HMMs to various prediction problems (Baum and Petrie 1966, Baum and Eagon 1967).

James Baker 得知了这项工作，并在 CMU 读研究生期间把该算法应用于语音处理（Baker, 1975a）。与此同时，Frederick Jelinek 及其合作者（从他们受 Shannon（1948）工作影响的信息论模型研究中汲取思路）在 IBM Thomas J. Watson 研究中心把 HMM 应用于语音（Jelinek et al., 1975）。早期的一处差异在解码算法上；Baker 的 DRAGON 系统采用 Viterbi（动态规划）解码，而 IBM 系统采用 Jelinek 的栈解码算法（Jelinek, 1969）。此后 Baker 曾在 IBM 小组短暂工作，随后创办了语音识别公司 Dragon Systems。

> James Baker learned of this work and applied the algorithm to speech processing(Baker, 1975a) during his graduate work at CMU. Independently, Frederick Jelinek and collaborators (drawing from their research in information-theoretical models influenced by the work of Shannon (1948)) applied HMMs to speech at the IBM Thomas J. Watson Research Center (Jelinek et al., 1975). One early difference was the decoding algorithm; Baker’s DRAGON system used Viterbi (dynamic programming) decoding, while the IBM system applied Jelinek’s stack decoding algorithm(Jelinek, 1969). Baker then joined the IBM group for a brief time before founding the speech-recognition company Dragon Systems.

HMM 的使用——以高斯混合模型（GMM）作为音素

> The use of the HMM, with Gaussian Mixture Models (GMMs) as the phonetic
成分——在语音共同体中逐渐传播，到 1990 年代成为主导范式。原因之一是 ARPA（美国国防部高级研究计划局）的推动。ARPA 于 1971 年启动了一项为期五年的计划，旨在构建 1000 词、受限语法、少说话人的语音理解系统（Klatt, 1977），并资助了四个相互竞争的系统，其中卡内基-梅隆大学的 Harpy 系统（Lowerre, 1976）使用了 Baker 基于 HMM 的 DRAGON 系统的简化版本，是被测系统中表现最好的。ARPA（以及后来的 DARPA）资助了许多新的语音研究计划，起初是像“Resource Management”（Price et al., 1988）这样的 1000 词、说话人无关的朗读语音任务，随后是朗读《华尔街日报》（WSJ）句子的识别、Broadcast News 领域（LDC 1998, Graff 1997）（真实新闻广播的转写，包括街头采访之类相当困难的片段），以及 Switchboard、CallHome、CallFriend 和 Fisher 领域（Godfrey et al. 1992, Cieri et al. 2004）（朋友或陌生人之间的自然电话交谈）。每个 ARPA 任务都包含一次大约每年举行的评测竞赛，在

> component, slowly spread through the speech community, becoming the dominant paradigm by the 1990s. One cause was encouragement by ARPA, the Advanced Research Projects Agency of the U.S. Department of Defense. ARPA started a five-year program in 1971 to build 1000-word, constrained grammar, few speaker speech understanding (Klatt, 1977), and funded four competing systems of which Carnegie-Mellon University’s Harpy system (Lowerre, 1976), which used a simplified version of Baker’s HMM-based DRAGON system was the best of the tested systems. ARPA (and then DARPA) funded a number of new speech research programs, beginning with 1000-word speaker-independent read-speech tasks like “Resource Management” (Price et al., 1988), recognition of sentences read from the Wall Street Journal (WSJ), Broadcast News domain (LDC 1998, Graff 1997) (transcription of actual news broadcasts, including quite difficult passages such as on-the-street interviews) and the Switchboard, CallHome, CallFriend, and Fisher domains (Godfrey et al. 1992, Cieri et al. 2004) (natural telephone conversations between friends or strangers). Each of the ARPA tasks involved an approximately annual bakeoff at

> `bakeoff`（评测竞赛）
>
> 释义：指 ARPA 每年组织的横向对比评测，各实验室用同一任务互相比较系统的识别性能。

该竞赛中各个系统相互比较评测。ARPA 的竞赛使得各实验室之间大规模地相互借鉴技术，因为很容易看出上一年哪些想法减少了错误；而这些竞赛很可能是 HMM 范式最终得以普及的重要因素。

> which systems were evaluated against each other. The ARPA competitions resulted in wide-scale borrowing of techniques among labs since it was easy to see which ideas reduced errors the previous year, and the competitions were probably an important factor in the eventual spread of the HMM paradigm.

到 1990 年前后，用于 ASR 的 HMM/GMM 架构的神经网络替代方案

> By around 1990 neural alternatives to the HMM/GMM architecture for ASR
出现了，其基础是此前一系列把神经网络用于音素识别及其他语音任务的实验。相关架构包括时延神经网络（TDNN）——卷积网络在语音上的首次应用——（Waibel et al. 1989, Lang et al. 1990）、RNN（Robinson and Fallside, 1991），以及混合式 HMM/MLP 架构，其中前馈神经网络被训练为音素分类器，其输出被用作基于 HMM 的架构的概率估计（Morgan and Bourlard 1990, Bourlard and Morgan 1994, Morgan and Bourlard 1995）。

> arose, based on a number of earlier experiments with neural networks for phoneme recognition and other speech tasks. Architectures included the time-delay neural network (TDNN)—the first use of convolutional networks for speech— (Waibel et al. 1989, Lang et al. 1990), RNNs (Robinson and Fallside, 1991), and the hybrid HMM/MLP architecture in which a feedforward neural network is trained as a phonetic classifier whose outputs are used as probability estimates for an HMM-based architecture (Morgan and Bourlard 1990, Bourlard and Morgan 1994, Morgan and Bourlard 1995).

> `hybrid`（混合式）
>
> 释义：本书指把前馈神经网络当作音素分类器、其输出用作 HMM 概率估计的混合 HMM/MLP 架构。

尽管混合系统表现出接近标准 HMM/GMM

> While the hybrid systems showed performance close to the standard HMM/GMM
模型的性能，但问题在于速度：大型混合模型在当时那个年代的 CPU 上训练起来太慢。例如，最大的混合系统是一个前馈网络，其隐层被限制为 4000 个单元，只能给出几十个单音素的概率。然而训练这个模型仍然需要该研究组设计专门的硬件板来做向量处理（Morgan and Bourlard, 1995）。

> models, the problem was speed: large hybrid models were too slow to train on the CPUs of that era. For example, the largest hybrid system, a feedforward network, was limited to a hidden layer of 4000 units, producing probabilities over only a few dozen monophones. Yet training this model still required the research group to design special hardware boards to do vector processing (Morgan and Bourlard, 1995).

后来的一项分析性研究表明，即使控制参数总量不变，这类简单前馈 MLP 用于 ASR 时，其性能在隐层数超过 1 层后会急剧提升（Maas et al., 2017）。但当时的计算资源不足以支持更多层。

> A later analytic study showed the performance of such simple feedforward MLPs for ASR increases sharply with more than 1 hidden layer, even controlling for the total number of parameters (Maas et al., 2017). But the computational resources of the time were insufficient for more layers.

在接下来的二十年里，摩尔定律与 GPU 的兴起共同

> Over the next two decades a combination of Moore’s law and the rise of GPUs
使得具有许多层的深度神经网络成为可能。到 2009 年，在 TIMIT 音素识别这类较小任务上，性能已接近传统系统（Mohamed et al., 2009）；而到 2012 年，混合系统的性能已超过传统的 HMM/GMM 系统（Jaitly et al. 2012, Dahl et al. 2012 等）。

> allowed deep neural networks with many layers. Performance was getting close to traditional systems on smaller tasks like TIMIT phone recognition by 2009 (Mohamed et al., 2009), and by 2012, the performance of hybrid systems had surpassed traditional HMM/GMM systems (Jaitly et al. 2012, Dahl et al. 2012, inter alia).

最初看来，使用深度信念网络之类技术对网络进行无监督预训练似乎很重要，但到 2013 年已清楚：对于混合 HMM/GMM 前馈网络而言，真正重要的只是使用大量数据和足够多的层，不过还有少数其他组件确实提升了性能：使用对数梅尔特征而非 MFCC、使用 dropout，以及使用修正线性单元（Deng et al. 2013, Maas et al. 2013, Dahl et al. 2013）。

> Originally it seemed that unsupervised pretraining of the networks using a technique like deep belief networks was important, but by 2013, it was clear that for hybrid HMM/GMM feedforward networks, all that mattered was to use a lot of data and enough layers, although a few other components did improve performance: using log mel features instead of MFCCs, using dropout, and using rectified linear units (Deng et al. 2013, Maas et al. 2013, Dahl et al. 2013).

与此同时，早期工作已在 2006 年提出 CTC 损失函数（Graves

> Meanwhile early work had proposed the CTC loss function by 2006 (Graves
et al., 2006）；到 2012 年，RNN-Transducer 被提出并应用于音素识别（Graves 2012, Graves et al. 2013），随后用于端到端语音识别的重打分（Graves and Jaitly, 2014），再用于识别本身（Maas et al., 2015），其间还出现了专门化束搜索之类的进展（Hannun et al., 2014）。（本章对 CTC 的描述参考了 Hannun（2017），我们鼓励感兴趣的读者参阅该文献。）

> et al., 2006), and by 2012 the RNN-Transducer was defined and applied to phone recognition (Graves 2012, Graves et al. 2013), and then to end-to-end speech recognition rescoring (Graves and Jaitly, 2014), and then recognition (Maas et al., 2015), with advances such as specialized beam search (Hannun et al., 2014). (Our description of CTC in the chapter draws on Hannun (2017), which we encourage the interested reader to follow).
编码器-解码器架构大约在同一时期被应用于语音，

> The encoder-decoder architecture was applied to speech at about the same time
由两个不同的小组完成，分别是 Chan et al.（2016）的 Listen Attend and Spell 系统，以及 Chorowski et al.（2014）与 Bahdanau et al.（2016）的基于注意力的编码器-解码器架构。到 2018 年，Transformer 被纳入这一编码器-解码器架构。Karita et al.（2019）很好地比较了用于 ASR、TTS 和语音到语音翻译的编码器架构中 RNN 与 Transformer 的差异。

> by two different groups, in the Listen Attend and Spell system of Chan et al. (2016) and the attention-based encoder decoder architecture of Chorowski et al. (2014) and Bahdanau et al. (2016). By 2018 Transformers were included in this encoderdecoder architecture. Karita et al. (2019) is a nice comparison of RNNs vs Transformers in encoder-architectures for ASR, TTS, and speech-to-speech translation.

语音处理领域流行的工具包包括 Kaldi（Povey et al., 2011）和

> Popular toolkits for speech processing include Kaldi (Povey et al., 2011) and

> `Kaldi ESPnet`（Kaldi 与 ESPnet）
>
> 释义：本书指语音处理领域两个广泛使用的开源工具包，分别由 Povey 等人和 Watanabe 等人推出。

ESPnet（Watanabe et al. 2018, Hayashi et al. 2020）。

> ESPnet (Watanabe et al. 2018, Hayashi et al. 2020).

## 习题

> Exercises
