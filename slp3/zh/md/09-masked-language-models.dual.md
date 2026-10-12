# 第 9 章 掩码语言模型

### 章

> CHAPTER

# 9 掩码语言模型

> 9 Masked Language Models

Larvatus prodeo［戴着面具，我前行］

> Larvatus prodeo [Masked, I go forward]

笛卡尔（Descartes）

> Descartes

在前两章中，我们介绍了 transformer，并了解了如何将 transformer 语言模型预训练为因果（causal）或自左向右的语言模型。在本章中，我们将介绍预训练语言模型的第二种范式——双向 transformer 编码器，以及其中使用最广泛的版本，即 BERT

> In the previous two chapters we introduced the transformer and saw how to pretrain a transformer language model as a causal or left-to-right language model. In this chapter we’ll introduce a second paradigm for pretrained language models, the bidirectional transformer encoder, and the most widely-used version, the BERT

> BERT

模型家族（Devlin 等，2019）。该模型通过掩码语言

> family of models (Devlin et al., 2019). This model is trained via masked language

> 掩码
>
> *masked*

建模来训练：我们不预测下一个词，而是遮盖中间的

> modeling, where instead of predicting the following word, we mask a word in the

> 语言建模
>
> *language modeling*

某个词，并要求模型根据两侧的词来猜出该词。因此，这种方法让模型能够同时看到右侧和左侧的上下文。

> middle and ask the model to guess the word given the words on both sides. This method thus allows the model to see both the right and left context.

我们也已在上一章介绍了微调。这里我们描述一种新的

> We also introduced fine-tuning in the prior chapter. Here we describe a new

> 微调
>
> *fine-tuning*

微调方式：我们取这些预训练模型所学到的 transformer 网络，在网络顶层之后加入一个神经网络分类器，并在一些额外的标注数据上训练它，以执行诸如命名实体标注或自然语言推断之类的下游任务。和之前一样，其直觉是：预训练阶段所学到的语言模型蕴含了词义的丰富表示，从而使模型能够更容易地学到（“被微调以适应”）某个下游语言理解任务的要求。预训练-微调范式的这一

> kind of fine-tuning, in which we take the transformer network learned by these pretrained models, add a neural net classifier after the top layer of the network, and train it on some additional labeled data to perform some downstream task like named entity tagging or natural language inference. As before, the intuition is that the pretraining phase learns a language model that instantiates rich representations of word meaning, that thus enables the model to more easily learn (‘be finetuned to’) the requirements of a downstream language understanding task. This aspect of

> 迁移
>
> *transfer*

方面是机器学习中所谓的迁移学习的一个实例

> the pretrain-finetune paradigm is an instance of what is called transfer learning in

> 学习
>
> *learning*

：即从某一个任务或领域获取知识，然后将其应用（迁移）到解决新任务上的方法。

> machine learning: the method of acquiring knowledge from one task or domain, and then applying it (transferring it) to solve a new task.

## 9.1 语言模型的三种架构

> 9.1 Three architectures for language models

我们在第 7 章中为自左向右或自回归语言模型所描述的架构，实际上只是三种常见 LM 架构之一。

> The architecture we described in Chapter 7 for a left-to-right or autoregressive language model is actually only one of three common LM architectures.

这三种架构分别是编码器、解码器和编码器-解码器。

> The three architectures are the encoder, the decoder, and the encoder-decoder.

图 9.1 给出了这三者的示意图。

> Fig. 9.1 gives a schematic picture of the three.

解码器就是我们前面介绍过的架构。它以一串

> The decoder is the architecture we’ve introduced earlier. It takes as input a series

> 解码器
>
> *decoder*

词元（token）作为输入，并一次一个地迭代生成输出词元。解码器是用于构建 GPT、Claude、Llama 和 Mistral 等大语言模型的架构。解码器中的信息流是自左向右的，这意味着模型仅根据前面的词来预测下一个词。解码器是生成式模型，也就是说，给定输入词元，它们会生成新的输出词元。

> of tokens, and iteratively generates an output token one at a time. The decoder is the architecture used to create large language models like GPT, Claude, Llama, and Mistral. The information flow in decoders goes left-to-right, meaning that the model predicts the next word only from the prior words. Decoders are generative models, meaning that, given input tokens, they generate novel output tokens.

编码器以一串词元作为输入，并为每个词元输出一个向量表示。编码器通常是掩码语言模型，也就是说，它们通过遮盖掉一个词、并学习根据两侧周围的词来预测它而得到训练。BERT、RoBERTA 以及 BERT 家族中的其他掩码语言模型都是编码器模型。编码器模型不是生成式模型；它们不用于生成文本。相反，编码器模型常被用于

> The encoder takes as input a sequence of tokens and outputs a vector representation for each token. Encoders are usually masked language models, meaning they are trained by masking out a word, and learning to predict it by looking at surrounding words on both sides. Masked language models like BERT, RoBERTA, and others in the BERT family are encoder models. Encoder models are not generative models; they aren’t used to generate text. Instead encoder models are often used to

> 编码器
>
> *encoder*

228 第 9 章 • 掩码语言模型

> 228 CHAPTER 9 • MASKED LANGUAGE MODELS

| w w w<br>w w w w w<br>w w w w w w w w w w w w w<br>解码器 编码器 编码器-解码器<br>w w w<br>w w w w w<br>w w w w w w w w w w w w w<br>Decoder Encoder Encoder-Decoder |  |
| --- | --- |
| 图 9.1<br>Figure 9.1 | 语言模型的三种架构：解码器、编码器和编码器-解码器。箭头<br>Three architectures for language models: decoders, encoders, and encoder-decoders. The arrows |

w w w

w w w w w

w w w w w w w w w w w w w

解码器 编码器 编码器-解码器

> Decoder Encoder Encoder-Decoder

> 勾勒出这三种架构中的信息流。解码器以词元作为输入，并生成词元作为输出。编码器以词元作为输入，并产生一个编码（每个词元的向量表示）作为输出。编码器-解码器以词元作为输入，并生成一串词元作为输出。
>
> *sketch out the information flow in the three architectures. Decoders take tokens as input and generate tokens as output. Encoders take tokens as input and produce an encoding (a vector representation of each token) as output. Encoder-decoders take tokens as input and generate a series of tokens as output.*

构建分类器，例如输入是文本、输出是标签，用于情感、主题或其他类别。这是通过对它们进行微调（在有监督数据上训练它们）来完成的。我们将在本章介绍编码器模型。

> create classifiers, for example where the input is text and the output is a label, for example for sentiment or topic or other classes. This is done by fine-tuning them(training them on supervised data). We’ll introduce encoder models in this chapter.

> 编码器-
>
> *encoder-*

编码器-解码器以一串词元作为输入，并输出一串

> The encoder-decoder takes as input a sequence of tokens and outputs a series

> 解码器
>
> *decoder*

词元。它与仅解码器模型的不同之处在于，编码器-解码器的输入词元与输出词元之间的关系要松散得多，而且它们用于在不同种类的词元之间进行映射。也就是说，在编码器-解码器中，输出词元可能来自一套完全不同的词元集合，或者其序列比输入词元序列长得多或短得多。例如，编码器-解码器架构用于机器翻译，其中输入词元属于一种语言，而输出词元（数量可能或多或少）属于另一种语言。编码器-解码器架构还用于语音识别，其中输入是表示语音的词元，输出是表示文本的词元。我们将在第 13 章介绍用于机器翻译的编码器-解码器架构，在第 16 章介绍用于语音识别的编码器-解码器架构。

> of tokens. What makes it different than the decoder-only models, is that an encoderdecoder has a much looser relationship between the input tokens and the output tokens, and they are used to map between different kinds of tokens. That is, in an encoder-decoder, the output tokens might be from a very different token-set or be a much longer or shorter sequence than the input token sequence. For example encoder-decoder architectures are used for machine translation, where the input tokens are in one language and the output tokens (probably more or less of them) are in another language. Encoder-decoder architectures are also used for speech recognition, where the input is tokens representing speech, and the output is tokens representing text. We’ll introduce the encoder-decoder architecture for machine translation in Chapter 13, and for speech recognition in Chapter 16.

这三种架构可以用多种神经网络来构建，但

> These three architectures can be built out of many kinds of neural networks, but

这里我们继续假定使用 Transformer。

> we’ll continue to assume here the use of the transformer.

## 9.2 双向 Transformer 编码器

> 9.2 Bidirectional Transformer Encoders

我们先从双向 Transformer 编码器（bidirectional transformer encoder）入手，它是 BERT 及其后继模型（如 RoBERTa，Liu 等，2019）的基础。第 7 章中解码器式 LLM 的自左向右特性可能是一种限制，因为有些任务在处理某个 token 时，如果能够窥看未来的 token 会很有用。对于序列标注任务尤其如此，这类任务要为每个 token 打上标签，例如我们将在 9.5 节介绍的命名实体标注任务，或者后续章节中会出现的词性标注、句法分析等任务。

> Let’s begin by introducing the bidirectional transformer encoder that underlies models like BERT and its descendants like RoBERTa (Liu et al., 2019). The left-to-right nature of the decoder LLMs of Chapter 7 can be a limitation, because there are tasks for which it would be useful, when processing a token, to be able to peek at future tokens. This is especially true for sequence labeling tasks in which we want to tag each token with a label, such as the named entity tagging task we’ll introduce in Section 9.5, or tasks like part-of-speech tagging or parsing that come up in later chapters.

这里介绍的双向编码器，是一种与

> The bidirectional encoders that we introduce here are a different kind of beast

因果模型截然不同的模型。第 7 章的因果模型是生成模型，其设计目标是能够轻松生成序列中的下一个 token。而双向编码器的重点则在于计算输入 9.2 • 双向 TRANSFORMER 编码器 229 个 token 的语境化表示。双向编码器使用自注意力，把输入嵌入序列 (x1,...,xn) 映射为长度相同的输出嵌入序列 (h1,...,hn)，其中输出向量已经利用整个输入序列的信息进行了语境化。这些输出嵌入是每个输入 token 的语境化表示，在需要根据上下文中的 token 进行分类或决策的各类应用中都非常有用。

> than causal models. The causal models of Chapter 7 are generative models, designed to easily generate the next token in a sequence. But the focus of bidirectional encoders is instead on computing contextualized representations of the input 9.2 • BIDIRECTIONAL TRANSFORMER ENCODERS 229 tokens. Bidirectional encoders use self-attention to map sequences of input embeddings (x1,...,xn) to sequences of output embeddings of the same length (h1,...,hn), where the output vectors have been contextualized using information from the entire input sequence. These output embeddings are contextualized representations of each input token that are useful across a range of applications where we need to do a classification or a decision based on the token in context.

还记得我们说过，第 7 章的模型有时被称为仅解码器（decoder-only），因为它们对应第 13 章将要介绍的编码器-解码器模型中的解码器部分。相比之下，本章的掩码语言模型有时被称为仅编码器（encoder-only），因为它们为每个输入 token 生成一个编码，但通常并不用于通过解码/采样生成连贯的文本。

> Remember that we said the models of Chapter 7 are sometimes called decoderonly, because they correspond to the decoder part of the encoder-decoder model we will introduce in Chapter 13. By contrast, the masked language models of this chapter are sometimes called encoder-only, because they produce an encoding for each input token but generally aren’t used to produce running text by decoding/sampling.

尽管掩码语言模型也可以用于某些生成任务，例如近期涉及扩散（diffusion）的工作，但本书此处暂不讨论这一点。我们将重点关注掩码语言模型在解释性任务中的使用。

> Although it’s possible to use masked language models for some generation tasks, for example in recent work involving diffusion, we don’t discuss this yet here. We’ll focus on the use of masked language models for interpretative tasks.

### 9.2.1 双向掩码模型的架构

> 9.2.1 The architecture for bidirectional masked models

我们先讨论整体架构。基于双向 Transformer 的语言模型与前几章的因果 Transformer 有两点不同。第一，注意力函数不是因果的：token i 的注意力可以查看其后的 token i+1 等等。第二，训练方式略有不同，因为我们预测的是文本中间的内容，而不是末尾的内容。

> Let’s first discuss the overall architecture. Bidirectional transformer-based language models differ in two ways from the causal transformers in the previous chapters. The first is that the attention function isn’t causal; the attention for a token i can look at following tokens i+1 and so on. The second is that the training is slightly different since we are predicting something in the middle of our text rather than at the end.

第一点我们在这里讨论，第二点将在下一节讨论。

> We’ll discuss the first here and the second in the following section.

图 9.2a 在此重印自第 7 章，它展示了

> Fig. 9.2a, reproduced here from Chapter 7, shows the information flow in the

第 7 章自左向右方法中的信息流。每个 token 处的注意力计算都基于之前（以及当前）的输入 token，而忽略了位于所考虑 token 右侧的潜在有用信息。双向编码器允许注意力机制在整个输入上取值，从而克服了这一限制，如图 9.2b 所示。

> left-to-right approach of Chapter 7. The attention computation at each token is based on the preceding (and current) input tokens, ignoring potentially useful information located to the right of the token under consideration. Bidirectional encoders overcome this limitation by allowing the attention mechanism to range over the entire input, as shown in Fig. 9.2b.

| a1 a2 a3 a4 a5 a1 a2 a3 a4 a5<br>注意力 注意力 注意力 注意力 注意力 注意力 注意力 注意力 注意力 注意力<br>x1 x2 x3 x4 x5 x1 x2 x3 x4 x5<br>a）因果自注意力层 b）双向自注意力层<br>a1 a2 a3 a4 a5 a1 a2 a3 a4 a5<br>attention attention attention attention attention attention attention attention attention attention<br>x1 x2 x3 x4 x5 x1 x2 x3 x4 x5<br>a) A causal self-attention layer b) A bidirectional self-attention layer |  |
| --- | --- |
| 图 9.2<br>Figure 9.2 | （a）第 7 章的因果 Transformer，突出显示了 token 3 处的注意力计算。该<br>(a) The causal transformer from Chapter 7, highlighting the attention computation at token 3. The |

> a1 a2 a3 a4 a5 a1 a2 a3 a4 a5

![](images/img_88.png)

![](images/img_88.png)

> 注意力 注意力 注意力 注意力 注意力 注意力 注意力 注意力 注意力 注意力
>
> *attention attention attention attention attention attention attention attention attention attention*

> x1 x2 x3 x4 x5 x1 x2 x3 x4 x5

> a）因果自注意力层 b）双向自注意力层
>
> *a) A causal self-attention layer b) A bidirectional self-attention layer*

> 每个 token 处的注意力值仅使用上下文中较早出现的信息来计算。（b）双向注意力模型中的信息流。在处理每个 token 时，模型会关注当前 token 之前和之后的所有输入。因此，token 3 的注意力可以利用其后 token 的信息。
>
> *attention value at each token is computed using only information seen earlier in the context. (b) Information flow in a bidirectional attention model. In processing each token, the model attends to all inputs, both before and after the current one. So attention for token 3 can draw on information from following tokens.*

实现非常简单！我们只需去掉注意力掩码

> The implementation is very simple! We simply remove the attention masking

这一步是我们在式 7.35 中引入的。回想第 7 章，我们必须对因果 Transformer 的 QK⊺ 矩阵进行掩码，使注意力无法看到未来的 token（此处重复式 7.35，针对单个注意力头）：

> step that we introduced in Eq. 7.35. Recall from Chapter 7 that we had to mask the QK⊺matrix for causal transformers so that attention couldn’t look at future tokens(repeated from Eq. 7.35 for a single attention head):

 QK⊺ 

head = softmax mask

> (9.1)

√dk V

图 9.3 展示了 QK⊺ 的掩码版本和未掩码版本。对于双向注意力，我们使用图 9.3b 中未掩码的版本。因此，双向注意力 230 第 9 章 • 掩码语言模型

> Fig. 9.3 shows the masked version of QK⊺and the unmasked version. For bidirectional attention, we use the unmasked version of Fig. 9.3b. Thus the attention 230 CHAPTER 9 • MASKED LANGUAGE MODELS

| q1•k1 −∞ −∞ −∞ q1•k1 q1•k2 q1•k3 q1•k4<br>q2•k1 q2•k2 −∞ −∞ q2•k1 q2•k2 q2•k3 q2•k4<br>N N<br>q3•k1 q3•k2 q3•k3 −∞ q3•k1 q3•k2 q3•k3 q3•k4<br>q4•k1 q4•k2 q4•k3 q4•k4 q4•k1 q4•k2 q4•k3 q4•k4<br>N N<br>(a) (b) |  |
| --- | --- |
| 图 9.3<br>Figure 9.3 | ⊺<br>N ×N 的 QK 矩阵，展示了 qi ·kj 值。（a）展示了上三角<br>⊺<br>The N ×N QK matrix showing the qi ·kj values. (a) shows the upper-triangle |

| q1•k1 q1•k2 q1•k3 q1•k4<br>q2•k1 q2•k2 q2•k3 q2•k4<br>N<br>q3•k1 q3•k2 q3•k3 q3•k4<br>q4•k1 q4•k2 q4•k3 q4•k4<br>N | q1•k1 | q1•k2 | q1•k3 | q1•k4 |
| --- | --- | --- | --- | --- |
|  | q2•k1 | q2•k2 | q2•k3 | q2•k4 |
|  | q3•k1 | q3•k2 | q3•k3 | q3•k4 |
|  | q4•k1 | q4•k2 | q4•k3 | q4•k4 |

| q1•k1 −∞ −∞ −∞<br>q2•k1 q2•k2 −∞ −∞<br>N<br>q3•k1 q3•k2 q3•k3 −∞<br>q4•k1 q4•k2 q4•k3 q4•k4<br>N |  | −∞ | −∞ | −∞ |
| --- | --- | --- | --- | --- |
|  | q1•k1 |  |  |  |
|  |  |  | −∞ | −∞ |
|  | q2•k1 | q2•k2 |  |  |
|  |  |  |  |  |
|  |  |  |  | −∞ |
|  | q3•k1 | q3•k2 | q3•k3 |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  | q4•k1 | q4•k2 | q4•k3 | q4•k4 |
|  |  |  |  |  |

> q2•k1 q2•k2

> N

> N

> q3•k1 q3•k2 q3•k3 q3•k1 q3•k2 q3•k3 q3•k4

> q4•k1 q4•k2 q4•k3 q4•k4 q4•k1 q4•k2 q4•k3 q4•k4

> N

> N

(a) (b)

> 图 9.3 N ×N 的 QK⊺ 矩阵，展示了 qi ·kj 值。（a）展示了比较矩阵中上三角部分被置零（设为 −∞，softmax 会将其变为零），而（b）展示了未掩码的版本。
>
> *Figure 9.3 The N ×N QK⊺matrix showing the qi ·kj values. (a) shows the upper-triangle portion of the comparisons matrix zeroed out (set to −∞, which the softmax will turn to zero), while (b) shows the unmasked version.*

的计算与式 9.1 完全相同，只是去掉了掩码：

> computation for bidirectional attention is exactly the same as Eq. 9.1 but with the mask removed:

QK⊺ 

head = softmax

> (9.2)

√dk V

除此之外，注意力计算与我们在第 7 章看到的一致，transformer 块架构（前馈层、层归一化等）也是如此。与第 7 章一样，输入同样是一系列子词 token，通常由 3 种常用的分词算法之一计算得到（包括我们在第 2 章已经见过的 BPE 算法，以及另外两种：WordPiece 算法和 SentencePiece Unigram LM 算法）。这意味着每条输入句子都必须先分词，之后所有处理都在子词 token 而非词上进行。正如我们将在教材第三部分看到的，这将要求：对于某些需要“词”这一概念的 NLP 任务（例如句法分析），我们偶尔需要把子词映射回词。

> Otherwise, the attention computation is identical to what we saw in Chapter 7, as is the transformer block architecture (the feedforward layer, layer norm, and so on). As in Chapter 7, the input is also a series of subword tokens, usually computed by one of the 3 popular tokenization algorithms (including the BPE algorithm that we already saw in Chapter 2 and two others, the WordPiece algorithm and the SentencePiece Unigram LM algorithm). That means every input sentence first has to be tokenized, and all further processing takes place on subword tokens rather than words. This will require, as we’ll see in the third part of the textbook, that for some NLP tasks that require notions of words (like parsing) we will occasionally need to map subwords back to words.

为了更具体地说明这一点，最初的纯英文双向 transformer

> To make this more concrete, the original English-only bidirectional transformer

编码器模型 BERT（Devlin 等，2019）由以下部分组成：

> encoder model, BERT (Devlin et al., 2019), consisted of the following:

- 一个仅含英文的子词词表，包含使用 WordPiece 算法（Schuster 和 Nakajima，2012）生成的 30,000 个 token。
- 输入上下文窗口 N=512 个 token，模型维度 d=768
- 因此模型的输入 X 的形状为 [N ×d] = [512×768]。
- L=12 层 transformer 块，每层含 A=12 个（双向）多头注意力层。
- 所得模型约有 100M 个参数。

> An English-only subword vocabulary consisting of 30,000 tokens generated using the WordPiece algorithm (Schuster and Nakajima, 2012).
> Input context window N=512 tokens, and model dimensionality d=768
> So X, the input to the model, is of shape [N ×d] = [512×768].
> L=12 layers of transformer blocks, each with A=12 (bidirectional) multihead attention layers.
> The resulting model has about 100M parameters.

更大的多语言模型 XLM-RoBERTa 在 100 种语言上训练，它具有

> The larger multilingual XLM-RoBERTa model, trained on 100 languages, has

- 一个多语言子词词表，包含使用 SentencePiece Unigram LM 算法（Kudo 和 Richardson，2018）生成的 250,000 个 token。
- 输入上下文窗口 N=512 个 token，模型维度 d=1024，因此模型的输入 X 的形状为 [N ×d] = [512×1024]。
- L=24 层 transformer 块，每层含 A=16 个多头注意力层
- 所得模型约有 550M 个参数。

> A multilingual subword vocabulary with 250,000 tokens generated using the SentencePiece Unigram LM algorithm (Kudo and Richardson, 2018).
> Input context window N=512 tokens, and model dimensionality d=1024, hence X, the input to the model, is of shape [N ×d] = [512×1024].
> L=24 layers of transformer blocks, with A=16 multihead attention layers each
> The resulting model has about 550M parameters.

注意，就大语言模型而言，550M 个参数相对较小

> Note that 550M parameters is relatively small as large language models go

（Llama 3 有 405B 个参数，因此大了 3 个数量级。）的确，掩码语言模型往往比因果语言模型小得多。

> (Llama 3 has 405B parameters, so is 3 orders of magnitude bigger). Indeed, masked language models tend to be much smaller than causal language models.

9.3 • 训练双向编码器 231

> 9.3 • TRAINING BIDIRECTIONAL ENCODERS 231

## 9.3 训练双向编码器

> 9.3 Training Bidirectional Encoders

在第 7 章中，我们通过让因果 transformer 语言模型迭代地预测文本中的下一个词来训练它们。但去掉注意力中的因果掩码会使“猜下一个词”的语言建模任务变得毫无意义——答案可以直接从上下文中获得——因此我们需要一种新的训练方案。

> We trained causal transformer language models in Chapter 7 by making them iteratively predict the next word in a text. But eliminating the causal mask in attention makes the guess-the-next-word language modeling task trivial—the answer is directly available from the context—so we’re in need of a new training scheme.

模型不再尝试预测下一个词，而是学习执行填空任务，这一任务在术语上称为完形填空任务（cloze task，Taylor，1953）。为说明这一点，让我们回到

> Instead of trying to predict the next word, the model learns to perform a fill-in-theblank task, technically called the cloze task (Taylor, 1953). To see this, let’s return

> 完形填空任务
>
> *cloze task*

第 3 章中那个启发性的例子。在这个例子中，我们不再预测接下来可能出现哪些词：

> to the motivating example from Chapter 3. Instead of predicting which words are likely to come next in this example:

瓦尔登湖（Walden Pond）的水是如此美丽

> The water of Walden Pond is so beautifully

而是被要求在给定句子其余部分的情况下预测缺失的内容。

> we’re asked to predict a missing item given the rest of the sentence.

瓦尔登湖（Walden Pond）的　是如此美丽……

> The of Walden Pond is so beautifully ...

也就是说，给定一个缺少一个或多个元素的输入序列，学习任务就是预测缺失的元素。更确切地说，训练时模型被剥夺输入序列中的一个或多个 token，并且必须为每个缺失项生成词表上的概率分布。随后我们利用模型每次预测产生的交叉熵损失来驱动学习过程。

> That is, given an input sequence with one or more elements missing, the learning task is to predict the missing elements. More precisely, during training the model is deprived of one or more tokens of an input sequence and must generate a probability distribution over the vocabulary for each of the missing items. We then use the crossentropy loss from each of the model’s predictions to drive the learning process.

这种方法可以推广到各种会破坏

> This approach can be generalized to any of a variety of methods that corrupt the

训练输入、然后要求模型恢复原始输入的方法。已使用过的这类操纵示例包括掩码、替换、重排、删除，以及向训练文本中插入无关内容。这类训练的通用名称叫做去噪（denoising）：我们以某种方式破坏（向输入添加噪声）

> training input and then asks the model to recover the original input. Examples of the kinds of manipulations that have been used include masks, substitutions, reorderings, deletions, and extraneous insertions into the training text. The general name for this kind of training is called denoising: we corrupt (add noise to) the input in

> 去噪
>
> *denoising*

输入（例如掩码一个词，或填入一个错误的词），而系统的目标就是去除这些噪声。

> some way (by masking a word, or putting in an incorrect word) and the goal of the system is to remove the noise.

### 9.3.1 掩码词

> 9.3.1 Masking Words

> 掩码
>
> *Masked*

下面介绍用于训练双向编码器的掩码语言建模（Masked Language Modeling，MLM）方法（Devlin 等，2019）。与我们已经见过的语言模型训练方法一样，MLM 使用来自大规模语料的未标注文本。在 MLM 训练中，模型接收训练语料中的一系列句子，其中有一定比例的 token（在 BERT 模型中为 15%）被随机选中，接受掩码过程的操纵。给定输入句子 lunch was delicious，并假设我们随机选择第 3 个 token delicious 来操纵，

> Let’s describe the Masked Language Modeling (MLM) approach to training bidirectional encoders (Devlin et al., 2019). As with the language model training methods we’ve already seen, MLM uses unannotated text from a large corpus. In MLM training, the model is presented with a series of sentences from the training corpus in which a percentage of tokens (15% in the BERT model) have been randomly chosen to be manipulated by the masking procedure. Given an input sentence lunch was delicious and assume we randomly chose the 3rd token delicious to be manipulated,

> 语言建模
>
> *Language Modeling*

- 80% 的情况下：该 token 被替换为词表中名为 [MASK] 的特殊 token，例如 lunch was delicious →lunch was [MASK]。
- 10% 的情况下：该 token 被替换为另一个 token，该 token 按 token 一元概率从词表中随机采样。例如 lunch was delicious →lunch was gasp。
- 10% 的情况下：该 token 保持不变。例如 lunch was delicious
- lunch was delicious。

> 80% of the time: The token is replaced with the special vocabulary token named [MASK], e.g. lunch was delicious →lunch was [MASK].
> 10% of the time: The token is replaced with another token, randomly sampled from the vocabulary based on token unigram probabilities. e.g. lunch was delicious →lunch was gasp.
> 10% of the time: the token is left unchanged. e.g. lunch was delicious
> lunch was delicious.

随后我们训练模型猜测被操纵 token 对应的正确 token。为什么要有这三种可能的操纵方式？加入 [MASK] token 会在预训练与下游微调或推理之间造成不匹配，因为当我们使用 MLM 模型执行下游任务时，并不会使用任何 [MASK] token。如果我们只是把 token 替换为 [MASK]，232 第 9 章 • 掩码语言模型 那么模型可能只在看到 [MASK] 时才预测 token，但我们希望模型始终尝试预测输入的 token。

> We then train the model to guess the correct token for the manipulated tokens. Why the three possible manipulations? Adding the [MASK] token creates a mismatch between pretraining and downstream fine-tuning or inference, since when we employ the MLM model to perform a downstream task, we don’t use any [MASK] tokens. If 232 CHAPTER 9 • MASKED LANGUAGE MODELS we just replaced tokens with the [MASK], the model might only predict tokens when it sees a [MASK], but we want the model to try to always predict the input token.

为了让模型完成这种预测，原始输入序列先用子词模型分词，并采样出待操纵的 token。输入中所有 token 的词嵌入都从 E 嵌入矩阵中取出，与位置嵌入相加，构成 transformer 的输入，经过一堆双向 transformer 块，然后送入语言建模头。MLM 的训练目标是预测每个被掩码 token 的原始输入，这些预测产生的交叉熵损失驱动模型全部参数的训练过程。也就是说，所有输入 token 都在自注意力过程中发挥作用，但只有被采样的 token 用于学习。

> To train the model to make the prediction, the original input sequence is tokenized using a subword model and tokens are sampled to be manipulated. Word embeddings for all of the tokens in the input are retrieved from the E embedding matrix and combined with positional embeddings to form the input to the transformer, passed through the stack of bidirectional transformer blocks, and then the language modeling head. The MLM training objective is to predict the original inputs for each of the masked tokens and the cross-entropy loss from these predictions drives the training process for all the parameters in the model. That is, all of the input tokens play a role in the self-attention process, but only the sampled tokens are used for learning.

> long thanks the

> 交叉熵损失
>
> *CE Loss*

![](images/img_171.png)

![](images/img_171.png)

![](images/img_171.png)

> 对词表做 Softmax 的 LM Head
>
> *LM Head with Softmax over Vocabulary*

> hL1 hL2 hL3 hL4 hL5 hL6 hL7 hL8

![](images/img_173.png)

> 双向 Transformer 编码器
>
> *Bidirectional Transformer Encoder*

![](images/img_167.png)

![](images/img_167.png)

![](images/img_167.png)

![](images/img_167.png)

![](images/img_167.png)

![](images/img_167.png)

![](images/img_167.png)

![](images/img_167.png)

> Token +

> + + + + + + + +

> 位置
>
> *Positional*

> p1 p2 p3 p4 p5 p6 p7 p8

> 嵌入
>
> *Embeddings*

> So [mask] and [mask] for all apricot fish
>
> *So [mask] and [mask] for all apricot ﬁsh*

> So long and thanks for all the fish
>
> *So long and thanks for all the ﬁsh*

> 图 9.4 掩码语言模型训练。在此示例中，输入 token 中有三个被选中，其中两个被掩码，第三个被替换为一个无关词。模型为这三项分配的概率被用作训练损失。其余 5 个 token 对训练损失不起作用。
>
> *Figure 9.4 Masked language model training. In this example, three of the input tokens are selected, two of which are masked and the third is replaced with an unrelated word. The probabilities assigned by the model to these three items are used as the training loss. The other 5 tokens don’t play a role in training loss.*

图 9.4 用一个简单示例说明了这一方法。这里，long、thanks 和

> Fig. 9.4 illustrates this approach with a simple example. Here, long, thanks and

the 是从训练序列中采样得到的，其中前两个被掩码，第三个被替换为随机采样得到的 token apricot。由此得到的嵌入经过一个双向 transformer 块堆栈。回顾第 7 章第 7.5 节，为了对每个被掩码 token 产生词汇表上的概率分布，语言建模头（language modeling head）取出每个被掩码 token i 在最终 transformer 层 L 的输出向量 hL i，将其与反嵌入层（unembedding layer）ET 相乘得到 logits u，然后用 softmax 把 logits 转换为词汇表上的概率 y：

> the have been sampled from the training sequence, with the first two masked and the replaced with the randomly sampled token apricot. The resulting embeddings are passed through a stack of bidirectional transformer blocks. Recall from Section 7.5 in Chapter 7 that to produce a probability distribution over the vocabulary for each of the masked tokens, the language modeling head takes the output vector hL i from the final transformer layer L for each masked token i, multiplies it by the unembedding layer ET to produce the logits u, and then uses softmax to turn the logits into probabilities y over the vocabulary:

ui = hL i ET

> (9.3)

yi = softmax(ui)

> (9.4)

有了每个被掩码项的预测概率分布，我们就可以用交叉熵计算每个被掩码项的损失——即分配给实际被掩码词的对数概率的负值，如图 9.4 所示。更形式化地说，对于句子或批次 x 中给定的输入 token 向量，令被掩码的 token 集合为 M，把该句子中某些 token 替换为掩码后得到的版本记为 9.3 • 训练双向编码器 233 xmask，输出向量序列记为 h。对于给定的输入 token xi，例如图 9.4 中的词 long，损失就是在给定 xmask（概括为单个输出向量 hL i）的条件下正确词 long 的概率：

> With a predicted probability distribution for each masked item, we can use crossentropy to compute the loss for each masked item—the negative log probability assigned to the actual masked word, as shown in Fig. 9.4. More formally, for a given vector of input tokens in a sentence or batch x, let the set of tokens that are masked be M, the version of that sentence with some tokens replaced by masks be 9.3 • TRAINING BIDIRECTIONAL ENCODERS 233 xmask, and the sequence of output vectors be h. For a given input token xi, such as the word long in Fig. 9.4, the loss is the probability of the correct word long, given xmask (as summarized in the single output vector hL i ):

LMLM(xi) = −logP(xi|hL i )

作为权重更新依据的梯度，基于单个训练序列（或一批序列）中采样得到的学习项上的平均损失。

> The gradients that form the basis for the weight updates are based on the average loss over the sampled learning items from a single training sequence (or batch of sequences).

LMLM = −1 X

logP(xi|hL i )

|M|

> i∈M

注意，只有 M 中的 token 在学习中起作用；其他词对损失函数没有任何作用，因此从这个意义上说，BERT 及其后继模型效率不高；训练数据中只有 15% 的输入样本真正被用于训练权重。1

> Note that only the tokens in M play a role in learning; the other words play no role in the loss function, so in that sense BERT and its descendents are inefficient; only 15% of the input samples in the training data are actually used for training weights.1

### 9.3.2 下一句预测（Next Sentence Prediction）

> 9.3.2 Next Sentence Prediction

基于掩码的学习的重点是根据周围的上下文预测词，目标是产生有效的词级表示。然而，有一类重要的应用涉及判定句子对之间的关系。这类任务包括释义检测（判定两个句子是否具有相似的含义）、蕴含（判定两个句子的含义是相互蕴含还是相互矛盾）或语篇连贯性（判定两个相邻句子是否构成连贯的语篇）。

> The focus of mask-based learning is on predicting words from surrounding contexts with the goal of producing effective word-level representations. However, an important class of applications involves determining the relationship between pairs of sentences. These include tasks like paraphrase detection (detecting if two sentences have similar meanings), entailment (detecting if the meanings of two sentences entail or contradict each other) or discourse coherence (deciding if two neighboring sentences form a coherent discourse).

为捕捉此类应用所需的那类知识，一些

> To capture the kind of knowledge required for applications such as these, some

BERT 家族中的模型引入了一个称为下一句预测（Next Sentence Prediction，NSP）的第二学习目标。在该任务中，模型接收成对的句子

> models in the BERT family include a second learning objective called Next Sentence Prediction (NSP). In this task, the model is presented with pairs of sentences

> 下一句
>
> *Next Sentence*

> 预测
>
> *Prediction*

并被要求预测每一对句子究竟是训练语料中真正相邻的一对句子，还是一对互不相关的句子。在 BERT 中，50% 的训练句子对为正例对，另外 50% 中句子对的第二个句子是从语料库其他地方随机选取的。NSP 损失取决于模型区分真实句子对与随机句子对的能力。

> and is asked to predict whether each pair consists of an actual pair of adjacent sentences from the training corpus or a pair of unrelated sentences. In BERT, 50% of the training pairs consisted of positive pairs, and in the other 50% the second sentence of a pair was randomly selected from elsewhere in the corpus. The NSP loss is based on how well the model can distinguish true pairs from random pairs.

为便于 NSP 训练，BERT 在输入表示中引入了两个特殊 token（这些 token 在微调中同样会证明有用）。用子词模型对输入进行分词后，token [CLS] 被加到输入句子对的最前面，token [SEP] 被放在两个句子之间以及第二个句子的最后一个 token 之后。实际上还有两个特殊 token：一个「第一段」token 和一个「第二段」token。这些 token 在输入阶段被加到词嵌入和位置嵌入上。也就是说，输入 X 的每个 token 实际上是由 3 种嵌入相加而成：词嵌入、位置嵌入以及第一/第二段嵌入。

> To facilitate NSP training, BERT introduces two special tokens to the input representation (tokens that will prove useful for fine-tuning as well). After tokenizing the input with the subword model, the token [CLS] is prepended to the input sentence pair, and the token [SEP] is placed between the sentences and after the final token of the second sentence. There are actually two more special tokens, a ‘First Segment’ token, and a ‘Second Segment’ token. These tokens are added in the input stage to the word and positional embeddings. That is, each token of the input X is actually formed by summing 3 embeddings: word, position, and first/second segment embeddings.

在训练期间，与

> During training, the output vector hL CLS from the final layer associated with the

[CLS] token 相关联的最终层输出向量 hL CLS 表示下一句预测。与 MLM 目标一样，我们添加一个特殊的头，在此例中即 NSP 头，它由一组可学习的分类权重 WNSP ∈Rd×2 构成，从原始的 [CLS] 向量 hL CLS 得到二分类预测：

> [CLS] token represents the next sentence prediction. As with the MLM objective, we add a special head, in this case an NSP head, which consists of a learned set of classification weights WNSP ∈Rd×2 that produces a two-class prediction from the raw [CLS] vector hL CLS:

yi = softmax(hL CLSWNSP)

> 1

> BERT 家族的另一个成员 ELECTRA 确实使用所有样本进行训练（Clark et al., 2020b）。
>
> *ELECTRA, another BERT family member, does use all examples for training (Clark et al., 2020b).*

234 第 9 章 • 掩码语言模型

> 234 CHAPTER 9 • MASKED LANGUAGE MODELS

交叉熵用于计算呈现给模型的每个句子对的 NSP 损失

> Cross entropy is used to compute the NSP loss for each sentence pair presented

图 9.5 展示了 NSP 训练的总体设置。在 BERT 中，NSP 损失与 MLM 训练目标结合使用，构成最终损失。

> to the model. Fig. 9.5 illustrates the overall NSP training setup. In BERT, the NSP loss was used in conjunction with the MLM training objective to form final loss.

|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |
|  | 1<br>交叉熵损失<br>NSP<br>头<br>h<br>CLS<br>双向 Transformer 编码器<br>Token +<br>Segment + + + + + + + + + + + + + + + + + + +<br>位置<br>s1 p1 s1 p2 s1 p3 s1 p4 s1 p5 s2 p6 s2 p7 s2 p8 s2 p9<br>嵌入<br>[CLS] Cancel my flight [SEP] And the hotel [SEP]<br>1<br>CE Loss<br>NSP<br>Head<br>h<br>CLS<br>Bidirectional Transformer Encoder<br>Token +<br>Segment + + + + + + + + + + + + + + + + + + +<br>Positional<br>s1 p1 s1 p2 s1 p3 s1 p4 s1 p5 s2 p6 s2 p7 s2 p8 s2 p9<br>Embeddings<br>[CLS] Cancel my flight [SEP] And the hotel [SEP] |  |  |
|  |  |  |  |
| 图<br>F | 9.5<br>igure 9.5 | NSP 损失计算的一个示例。<br>An example of the NSP loss calculation. |  |
|  |  |  |  |

> 1

> 交叉熵损失
>
> *CE Loss*

![](images/img_215.png)

> NSP 头
>
> *NSP Head*

> hCLS

![](images/img_217.png)

> 双向 Transformer 编码器
>
> *Bidirectional Transformer Encoder*

> 词元 +分段 +
>
> *Token +Segment +*

![](images/img_213.png)

![](images/img_213.png)

![](images/img_213.png)

![](images/img_213.png)

![](images/img_213.png)

![](images/img_213.png)

![](images/img_213.png)

![](images/img_213.png)

![](images/img_213.png)

> + + + + + + + + + + + + + + + + + +

> 位置
>
> *Positional*

> s1 p1 s1 p2 s1 p3 s1 p4 s1 p5 s2 p6 s2 p7 s2 p8 s2 p9

> 嵌入
>
> *Embeddings*

> [CLS] 取消我的航班 [SEP] 还有酒店 [SEP]
>
> *[CLS] Cancel my ﬂight [SEP] And the hotel [SEP]*

> 图 9.5 NSP 损失计算的一个示例。
>
> *Figure 9.5 An example of the NSP loss calculation.*

### 9.3.3 训练机制

> 9.3.3 Training Regimes

BERT 以及其他早期基于 Transformer 的语言模型是在约 33 亿词的语料上训练的（由英文维基百科和一个名为 BooksCorpus（Zhu et al., 2015）的书籍文本语料库组合而成，出于知识产权原因，该语料库现已不再使用）。如今的掩码语言模型则是在大得多的网络文本数据集上训练，经过一定过滤，并用维基百科之类质量更高的数据加以补充，这与我们在第 7 章讨论的因果大型语言模型相同。

> BERT and other early transformer-based language models were trained on about 3.3 billion words (a combination of English Wikipedia and a corpus of book texts called BooksCorpus (Zhu et al., 2015) that is no longer used for intellectual property reasons). Modern masked language models are now trained on much larger datasets of web text, filtered a bit, and augmented by higher-quality data like Wikipedia, the same as those we discussed for the causal large language models of Chapter 7.

多语言模型同样使用网络文本和多语言维基百科。例如，XLM-R 模型是在 100 种语言、约 3000 亿个词元上训练的，数据经由 Common Crawl（https://commoncrawl.org/）取自网络。

> Multilingual models similarly use webtext and multilingual Wikipedia. For example the XLM-R model was trained on about 300 billion tokens in 100 languages, taken from the web via Common Crawl (https://commoncrawl.org/).

为了训练最初的 BERT 模型，文本片段对是从

> To train the original BERT models, pairs of text segments were selected from the

训练语料中按照下一句预测的 50/50 方案选取的。抽取片段对时保证二者合并后的长度小于 512 个词元的输入长度。随后用 MLM 方法对这些句子对中的词元进行掩码，并以 MLM 与 NSP 两个目标的组合损失作为最终损失。由于该最终损失会反向传播经过整个 Transformer，每个 Transformer 层的嵌入都会学到有助于从邻近词预测目标词的表示。由于 [CLS] 词元是 NSP 分类器的直接输入，其学到的表示往往会包含关于整个序列的信息。模型收敛大约需要对训练数据迭代 40 遍（epoch）。

> training corpus according to the next sentence prediction 50/50 scheme. Pairs were sampled so that their combined length was less than the 512 token input. Tokens within these sentence pairs were then masked using the MLM approach with the combined loss from the MLM and NSP objectives used for a final loss. Because this final loss is backpropagated through the entire transformer, the embeddings at each transformer layer will learn representations that are useful for predicting words from their neighbors. Since the [CLS] tokens are the direct input to the NSP classifier, their learned representations will tend to contain information about the sequence as a whole. Approximately 40 passes (epochs) over the training data was required for the model to converge.

有些模型（例如 RoBERTa）去掉了下一句预测目标，因此训练机制略有改变。此时输入不再是抽取的句子对，而只是一系列连续的句子，仍以特殊的 [CLS] 词元开头。如果在达到 512 个词元之前文档就结束了，则额外加入一个分隔符词元，并把下一篇文档的句子打包进来，直到总共达到 512 个词元。通常使用较大的批大小，介于 8K 到 32K 个词元之间。

> Some models, like the RoBERTa model, drop the next sentence prediction objective, and therefore change the training regime a bit. Instead of sampling pairs of sentences, the input is simply a series of contiguous sentences, still beginning with the special [CLS] token. If the document runs out before 512 tokens are reached, an extra separator token is added, and sentences from the next document are packed in, until we reach a total of 512 tokens. Usually large batch sizes are used, between 8K and 32K tokens.

多语言模型还有一个额外的决定要做：用什么数据来 9.4 • 面向分类的微调 235 构建词表？回想一下，所有语言模型都使用子词切分（BPE 或 SentencePiece Unigram LM 是最常见的两种算法）。既然某些语言比其他语言更容易获取多得多的文本，那么应当用什么文本来学习这种多语言切分？一种做法是随机地从训练数据（也许是来自 Common Crawl 的网络文本）中抽取句子，来构造这个学习词表的数据集。但那样一来，我们会抽到大量来自英语等网络文本丰富语言的句子，词元就会偏向稀有的英语词元，而不是从数据较少的语言中产生高频词元。因此，常见的做法是把训练数据划分为 N 种语言的子语料库，计算每种语言 i 的句子数 ni，再重新调整这些概率，以提高代表性不足语言的概率（Lample and Conneau, 2019）。从 N 种语言（其先验频率为 ni）中选取一个句子的新概率为 {qi}i=1...N，其中：

> Multilingual models have an additional decision to make: what data to use to 9.4 • FINE-TUNING FOR CLASSIFICATION 235 build the vocabulary? Recall that all language models use subword tokenization(BPE or SentencePiece Unigram LM are the two most common algorithms). What text should be used to learn this multilingual tokenization, given that it’s easier to get much more text in some languages than others? One option would be to create this vocabulary-learning dataset by sampling sentences from our training data(perhaps web text from Common Crawl), randomly. In that case we will choose a lot of sentences from languages with lots of web representation like English, and the tokens will be biased toward rare English tokens instead of creating frequent tokens from languages with less data. Instead, it is common to divide the training data into subcorpora of N different languages, compute the number of sentences ni of each language i, and readjust these probabilities so as to upweight the probability of less-represented languages (Lample and Conneau, 2019). The new probability of selecting a sentence from each of the N languages (whose prior frequency is ni) is{qi}i=1...N, where:

pα ni

> i

qi = 其中 pi =

> qi = with pi =

> (9.5)

PN j=1 pα PN k=1 nk

> j

回想第 5 章的式 5.19，α 取值在 0 到 1 之间会给概率较低的样本更高的权重。Conneau et al. (2020) 表明 α = 0.3 效果良好，能让稀有语言在切分中获得更多体现，从而整体上带来更好的多语言性能。

> Recall from Eq. 5.19 in Chapter 5 that an α value between 0 and 1 will give higher weight to lower probability samples. Conneau et al. (2020) show that α = 0.3 works well to give rare languages more inclusion in the tokenization, resulting in better multilingual performance overall.

这一预训练过程的产物既包括学到的词嵌入，

> The result of this pretraining process consists of both learned word embeddings,

也包括双向编码器的全部参数，这些参数用于为新的输入生成上下文嵌入。

> as well as all the parameters of the bidirectional encoder that are used to produce contextual embeddings for novel inputs.

在许多用途上，预训练的多语言模型比

> For many purposes, a pretrained multilingual model is more practical than a

单语模型更实用，因为它免去了构建许多（上百个！）独立单语模型的需要。而且多语言模型可以利用训练数据中恰好资源更多的相似语言所提供的语言学信息，来提升低资源语言的性能。不过，当语言数量变得非常大时，多语言模型会表现出所谓的多语言诅咒（curse of multilinguality）（Conneau et al., 2020）：与在较少语言上训练的模型相比，它在每种语言上的性能都会下降。多语言模型的另一个问题是它们“带有口音”：资源较多语言（往往是英语）的语法结构会渗入资源较少的语言；训练数据中大量的英语使模型对低资源语言的表示略微更像英语（Papadimitriou et al., 2023）。

> monolingual model, since it avoids the need to build many (a hundred!) separate monolingual models. And multilingual models can improve performance on lowresourced languages by leveraging linguistic information from a similar language in the training data that happens to have more resources. Nonetheless, when the number of languages grows very large, multilingual models exhibit what has been called the curse of multilinguality (Conneau et al., 2020): the performance on each language degrades compared to a model training on fewer languages. Another problem with multilingual models is that they ‘have an accent’: grammatical structures in higher-resource languages (often English) bleed into lower-resource languages; the vast amount of English language in training makes the model’s representations for low-resource languages slightly more English-like (Papadimitriou et al., 2023).

## 9.4 面向分类的微调

> 9.4 Fine-Tuning for Classification

预训练语言模型的威力在于它们能从大量文本中提取泛化规律——这些规律对无数下游应用都很有用。要实际利用这些泛化规律来解决下游任务，有两种方式。最常见的方式是用自然语言提示模型，使它进入一种能结合上下文生成我们所需内容的状态。

> The power of pretrained language models lies in their ability to extract generalizations from large amounts of text—generalizations that are useful for myriad downstream applications. There are two ways to make practical use of the generalizations to solve downstream tasks. The most common way is to use natural language to prompt the model, putting it in a state where it contextually generates what we want.

本节我们探讨使用预训练语言模型的另一种方式，

> In this section we explore an alternative way to use pretrained language models

将其用于下游应用，即一种微调。在用于

> for downstream applications, a kind of fine-tuning. In the kind of fine-tuning used

> 微调
>
> *fine-tuning*

掩码语言模型的这种微调中，我们在预训练模型之上添加应用专用的电路（常被称为 236 第 9 章 • 掩码语言模型 特殊头），并把预训练模型的输出作为它的输入。微调过程就是利用该应用的标注数据来训练这些额外的应用专用参数。通常，这种训练会冻结预训练语言模型的参数，或只对其做极小的调整。

> for masked language models, we add application-specific circuitry (often called a 236 CHAPTER 9 • MASKED LANGUAGE MODELS special head) on top of pretrained models, taking their output as its input. The fine-tuning process consists of using labeled data about the application to train these additional application-specific parameters. Typically, this training will either freeze or make only minimal adjustments to the pretrained language model parameters.

以下各节介绍一些常见类别的

> The following sections introduce fine-tuning methods for some common classes

文本应用的微调方法：序列分类、句对分类和序列标注。

> of text-based applications: sequence classification, sentence-pair classification, and sequence labeling.

### 9.4.1 序列分类

> 9.4.1 Sequence Classification

序列分类的任务是用单个标签对整个文本序列进行分类。这类任务通常称为文本分类，例如情感分析或垃圾邮件检测（附录 B），即把一段文本分到两三个类别（如正面或负面）；也包括类别数量众多的分类任务，例如文档级主题分类。

> The task of sequence classification is to classify an entire sequence of text with a single label. This set of tasks is commonly called text classification, like sentiment analysis or spam detection (Appendix B) in which we classify a text into two or three classes (like positive or negative), as well as classification tasks with a large number of categories, like document-level topic classification.

对于序列分类，我们用一个

> For sequence classification we represent the entire input to be classified by a

向量来表示待分类的整个输入。表示序列的方式有多种。一种是对序列中每个词元的最后一层输出向量求和或取平均。

> single vector. We can represent a sequence in various ways. One way is to take the sum or the mean of the last output vector from each token in the sequence.

对于 BERT，我们改为在词表中新增一个名为 [CLS] 的独特词元，并在预训练和编码时都把它加到所有输入序列的开头。

> For BERT, we instead add a new unique token to the vocabulary called [CLS], and prepended it to the start of all input sequences, both during pretraining and encoding.

模型最后一层中 [CLS] 输入对应的输出向量表示整个输入序列，并作为分类器头的输入，这是一个逻辑

> The output vector in the final layer of the model for the [CLS] input represents the entire input sequence and serves as the input to a classifier head, a logistic

> 分类头
>
> *classifier head*

回归或神经网络分类器来做出相应的决策。

> regression or neural network classifier that makes the relevant decision.

举个例子，让我们回到情感分类这个问题上。微调

> As an example, let’s return to the problem of sentiment classification. Finetuning

用于该应用的分类器，涉及学习一组权重 WC，把 [CLS] 标记的输出向量——hL CLS——映射为各可能情感类别上的一组得分。假设是一个三分类情感分类任务（正面、负面、中性），模型维度为 d，则 WC 的尺寸为 [d ×3]。要对一个文档进行分类，我们把输入文本送入预训练语言模型以生成 hL CLS，将其与 WC 相乘，再把所得向量送入 softmax。

> a classifier for this application involves learning a set of weights, WC, to map the output vector for the [CLS] token—hL CLS—to a set of scores over the possible sentiment classes. Assuming a three-way sentiment classification task (positive, negative, neutral) and dimensionality d as the model dimension, WC will be of size [d ×3]. To classify a document, we pass the input text through the pretrained language model to generate hL CLS, multiply it by WC, and pass the resulting vector through a softmax.

y = softmax(hL

> (9.6)

CLSWC)

微调 WC 中的取值需要由输入构成的监督训练数据，

> Finetuning the values in WC requires supervised training data consisting of input

这些输入序列标注有相应的情感类别。训练按通常的方式进行；用 softmax 输出与正确答案之间的交叉熵损失来驱动学习，从而得到 WC。

> sequences labeled with the appropriate sentiment class. Training proceeds in the usual way; cross-entropy loss between the softmax output and the correct answer is used to drive the learning that produces WC.

该损失不仅可以用来学习分类器的权重，还可以用来

> This loss can be used to not only learn the weights of the classifier, but also to

更新预训练语言模型自身的权重。在实践中，通常只需对语言模型参数做极小的改动就能获得合理的分类性能，且往往仅限于更新 Transformer 最后几层。图 9.6 展示了序列分类的这种整体方法。

> update the weights for the pretrained language model itself. In practice, reasonable classification performance is typically achieved with only minimal changes to the language model parameters, often limited to updates over the final few layers of the transformer. Fig. 9.6 illustrates this overall approach to sequence classification.

### 9.4.2 序列对分类

> 9.4.2 Sequence-Pair Classification

如 9.3.2 节所述，有一类重要问题涉及对输入序列对的分类。属于这一类的实际应用包括复述检测（这两个句子互为复述吗？）、逻辑蕴含（句子 A 在逻辑上蕴含句子 B 吗？）以及语篇连贯性（句子 B 作为句子 A 的后续有多连贯？）。

> As mentioned in Section 9.3.2, an important type of problem involves the classification of pairs of input sequences. Practical applications that fall into this class include paraphrase detection (are the two sentences paraphrases of each other?), logical entailment (does sentence A logically entail sentence B?), and discourse coherence(how coherent is sentence B as a follow-on to sentence A?).

为其中某个任务微调应用的过程，与使用 NSP 目标进行预训练时完全一样。在微调过程中，来自标注句子对的 9.4 • 用于分类的微调 237 y

> Fine-tuning an application for one of these tasks proceeds just as with pretraining using the NSP objective. During fine-tuning, pairs of labeled sentences from a 9.4 • FINE-TUNING FOR CLASSIFICATION 237 y

![](images/img_250.png)

> 情感分类
>
> *sentiment classiﬁcation*

> WC

> 分类头
>
> *head*

hCLS

![](images/img_252.png)

双向 Transformer 编码器

> Bidirectional Transformer Encoder

![](images/img_256.png)

![](images/img_256.png)

![](images/img_256.png)

![](images/img_256.png)

![](images/img_256.png)

![](images/img_256.png)

> + + + + + +

> i i i i i i

> E E E E E E

[CLS] 完全可预测且缺乏能量

> [CLS] entirely predictable and lacks energy

> 图 9.6 使用双向 Transformer 编码器进行序列分类。[CLS] 标记的输出向量用作一个简单分类器的输入。
>
> *Figure 9.6 Sequence classification with a bidirectional transformer encoder. The output vector for the [CLS] token serves as input to a simple classifier.*

监督微调集中的句子对被送入模型，并经过模型的所有层，为每个输入标记生成 h 输出。与序列分类一样，与前置的 [CLS] 标记相关联的输出向量代表了模型对输入对的看法。而与 NSP 训练一样，两个输入由 [SEP] 标记分隔。进行分类时，[CLS] 向量与一组学习到的分类权重相乘，再经过 softmax 生成标签预测，随后用这些预测来更新权重。

> supervised fine-tuning set are presented to the model, and run through all the layers of the model to produce the h outputs for each input token. As with sequence classification, the output vector associated with the prepended [CLS] token represents the model’s view of the input pair. And as with NSP training, the two inputs are separated by the [SEP] token. To perform classification, the [CLS] vector is multiplied by a set of learned classification weights and passed through a softmax to generate label predictions, which are then used to update the weights.

举个例子，让我们考虑一个使用 Multi-

> As an example, let’s consider an entailment classification task with the Multi-

Genre 自然语言推理（MultiNLI）数据集（Williams 等，2018）的蕴含分类任务。在

> Genre Natural Language Inference (MultiNLI) dataset (Williams et al., 2018). In

> 自然
>
> *natural*

自然语言推理或 NLI 这一任务中，它也称作识别文本

> the task of natural language inference or NLI, also called recognizing textual

> 语言推理
>
> *language inference*

蕴含，即给定一对句子，模型必须对其含义之间的关系进行分类。例如在 MultiNLI 语料库中，句子对被赋予 3 个标签之一：蕴含、矛盾和中性。这些标签描述的是第一个句子（前提）的含义与第二个句子（假设）的含义之间的关系。以下是该语料库中各类别的代表性示例：

> entailment, a model is presented with a pair of sentences and must classify the relationship between their meanings. For example in the MultiNLI corpus, pairs of sentences are given one of 3 labels: entails, contradicts and neutral. These labels describe a relationship between the meaning of the first sentence (the premise) and the meaning of the second sentence (the hypothesis). Here are representative examples of each class from the corpus:

- 中性

> Neutral

a：Jon 走回镇上的铁匠铺。 b：Jon 回到了他的家乡。

> a: Jon walked back to the town to the smithy. b: Jon traveled back to his hometown.

- 矛盾

> Contradicts

a：游客信息办公室可能非常有帮助。 b：游客信息办公室从来帮不上任何忙。

> a: Tourist Information offices can be very helpful. b: Tourist Information offices are never of any help.

- 蕴含

> Entails

a：我有点困惑。 b：并非所有内容对我来说都很清楚。

> a: I’m confused. b: Not all of it is very clear to me.

矛盾关系意味着前提与假设相矛盾；蕴含意味着前提蕴含假设；中性意味着两者都不必然为真。这些标签的含义比严格的逻辑蕴含或矛盾更为宽松，它表示一个典型的人在读到这些句子时最有可能这样理解其含义。

> A relationship of contradicts means that the premise contradicts the hypothesis; entails means that the premise entails the hypothesis; neutral means that neither is necessarily true. The meaning of these labels is looser than strict logical entailment or contradiction indicating that a typical human reading the sentences would most likely interpret the meanings in this way.

238 第 9 章 • 掩码语言模型

> 238 CHAPTER 9 • MASKED LANGUAGE MODELS

要为 MultiNLI 任务微调一个分类器，我们把前提/假设

> To finetune a classifier for the MultiNLI task, we pass the premise/hypothesis

句子对按上述方式送入双向编码器，并把 [CLS] 标记的输出向量用作分类头的输入。与普通的序列分类一样，该分类头为三分类器提供输入，该分类器可在 MultiNLI 训练语料库上训练。

> pairs through a bidirectional encoder as described above and use the output vector for the [CLS] token as the input to the classification head. As with ordinary sequence classification, this head provides the input to a three-way classifier that can be trained on the MultiNLI training corpus.

## 9.5 面向序列标注的微调：命名实体

> 9.5 Fine-Tuning for Sequence Labeling: Named Entity

## 识别

> Recognition

在序列标注中，网络的任务是为序列中的每个词元（token）从一组固定的小标签集合中指派一个标签。最常见的序列标注任务之一是命名实体识别。

> In sequence labeling, the network’s task is to assign a label chosen from a small fixed set of labels to each token in the sequence. One of the most common sequence labeling task is named entity recognition.

### 9.5.1 命名实体

> 9.5.1 Named Entities

粗略地说，命名实体是指任何可以用专有

> A named entity is, roughly speaking, anything that can be referred to with a proper

> 命名实体 命名实体
>
> *named entity named entity*

名称来指称的事物：人、地点、组织机构。命名实体识别

> name: a person, a location, an organization. The task of named entity recognition

> 识别
>
> *recognition*

（NER）的任务是找出构成专有名称的文本片段，并标注该

> (NER) is to find spans of text that constitute proper names and tag the type of the

> NER

实体的类型。最常用的四类实体标签是：PER（人物）、LOC（地点）、ORG（组织机构）和 GPE（地缘政治实体）。不过，“命名实体”这一术语通常被扩展使用，以涵盖本身并非实体的对象，包括日期和时间等时间表达式，甚至价格等数值表达式。下面是 NER 标注器的一个输出示例：

> entity. Four entity tags are most common: PER (person), LOC (location), ORG(organization), or GPE (geo-political entity). However, the term named entity is commonly extended to include things that aren’t entities per se, including temporal expressions like dates and times, and even numerical expressions like prices. Here’s an example of the output of an NER tagger:

以燃油价格高企为由，[ORG 联合航空（United Airlines）] 表示，[TIME 周五] 它已把飞往部分城市的航班往返票价上调了 [MONEY 6 美元]，这些城市同时也有低成本航空公司运营。[ORG 美国航空（American Airlines）]，即 [ORG AMR 公司] 的一个下属单位，立即跟进调价，其发言人 [PER 蒂姆·瓦格纳（Tim Wagner）] 说。[ORG 联合航空]，即 [ORG UAL 公司] 的一个下属单位，表示此次涨价自 [TIME 周四] 起生效，适用于其与折扣航空公司竞争的大部分航线，例如 [LOC 芝加哥] 至 [LOC 达拉斯] 以及 [LOC 丹佛] 至 [LOC 旧金山]。

> Citing high fuel prices, [ORG United Airlines] said [TIME Friday] it has increased fares by [MONEY $6] per round trip on flights to some cities also served by lower-cost carriers. [ORG American Airlines], a unit of [ORG AMR Corp.], immediately matched the move, spokesman[PER Tim Wagner] said. [ORG United], a unit of [ORG UAL Corp.], said the increase took effect [TIME Thursday] and applies to most routes where it competes against discount carriers, such as [LOC Chicago] to [LOC Dallas] and [LOC Denver] to [LOC San Francisco].

这段文本包含 13 处命名实体提及，其中有 5 个组织机构、4 个地点、2 个时间、1 个人物和 1 处金额。图 9.7 列出了典型的通用命名实体类型。许多应用还需要使用特定的实体类型，例如蛋白质、基因、商品或艺术作品。

> The text contains 13 mentions of named entities including 5 organizations, 4 locations, 2 times, 1 person, and 1 mention of money. Figure 9.7 shows typical generic named entity types. Many applications will also need to use specific entity types like proteins, genes, commercial products, or works of art.

类型 标签 样本类别 例句 人物 PER 人、角色 图灵是计算机科学领域的巨人。

> Type Tag Sample Categories Example sentences People PER people, characters Turing is a giant of computer science.

| 类型 标签 样本类别 例句<br>Type Tag Sample Categories Example sentences |  |
| --- | --- |
| 人物 PER 人、角色 图灵是计算机科学领域的巨人。<br>组织机构 ORG 公司、运动队 IPCC 对气旋发出了警告。<br>地点 LOC 地区、山脉、海洋 Mt. Sanitas 位于 Sunshine Canyon。<br>地缘政治实体 GPE 国家、州 帕洛阿尔托正在提高停车费。<br>People PER people, characters Turing is a giant of computer science.<br>Organization ORG companies, sports teams The IPCC warned about the cyclone.<br>Location LOC regions, mountains, seas Mt. Sanitas is in Sunshine Canyon.<br>Geo-Political Entity GPE countries, states Palo Alto is raising the fees for parking. |  |
| 图 9.7<br>Figure 9.7 | 通用命名实体类型列表，以及它们所指代的实体类别。<br>A list of generic named entity types with the kinds of entities they refer to. |

组织机构 ORG 公司、运动队 IPCC 对气旋发出了警告。

> Organization ORG companies, sports teams The IPCC warned about the cyclone.

地点 LOC 地区、山脉、海洋 Mt. Sanitas 位于 Sunshine Canyon。

> Location LOC regions, mountains, seas Mt. Sanitas is in Sunshine Canyon.

地缘政治实体 GPE 国家、州 帕洛阿尔托正在提高停车费。

> Geo-Political Entity GPE countries, states Palo Alto is raising the fees for parking.

命名实体识别是各类自然语言处理

> Named entity recognition is a useful step in various natural language processing

任务中有用的一步，包括把文本链接到 Wikipedia 等结构化知识源中的信息、度量文本中对某一特定实体的情感或态度，甚至作为为保护隐私而对文本进行匿名化处理的一部分。NER 任务之所以困难，是因为切分 NER 片段存在歧义，需要判断哪些词元是实体、9.5 • 面向序列标注的微调：命名实体识别 239 哪些不是，因为文本中的大多数词都不会是命名实体。另一个困难来自类型歧义。正如我们在图 9.8 中所见，Washington 这一提及可以指人物、运动队、城市或美国政府。

> tasks, including linking text to information in structured knowledge sources like Wikipedia, measuring sentiment or attitudes toward a particular entity in text, or even as part of anonymizing text for privacy. The NER task is difficult because of the ambiguity of segmenting NER spans, figuring out which tokens are entities 9.5 • FINE-TUNING FOR SEQUENCE LABELING: NAMED ENTITY RECOGNITION 239 and which aren’t, since most words in a text will not be named entities. Another difficulty is caused by type ambiguity. The mention Washington can refer to a person, a sports team, a city, or the US government, as we see in Fig. 9.8.

[PER Washington] 生于 James Burroughs 的农场，生来即为奴隶。[ORG Washington] 在四场系列赛中以 2 比 1 领先。

> [PER Washington] was born into slavery on the farm of James Burroughs.[ORG Washington] went up 2 games to 1 in the four-game series.

| [ Washington] 生于 James Burroughs 的农场，生来即为奴隶。<br>PER<br>[ Washington] 在四场系列赛中以 2 比 1 领先。<br>ORG<br>Blair 抵达 [ Washington]，这很可能是他最后一次国事访问。<br>LOC<br>6 月，[ Washington] 通过了一项强制系安全带的法规。<br>GPE<br>[ Washington] was born into slavery on the farm of James Burroughs.<br>PER<br>[ Washington] went up 2 games to 1 in the four-game series.<br>ORG<br>Blair arrived in [ Washington] for what may well be his last state visit.<br>LOC<br>In June, [ Washington] passed a primary seatbelt law.<br>GPE |  |
| --- | --- |
| 图 9.8<br>Figure 9.8 | 名称 Washington 使用中的类型歧义示例。<br>Examples of type ambiguities in the use of the name Washington. |

Blair 抵达 [LOC Washington]，这很可能是他最后一次国事访问。

> Blair arrived in [LOC Washington] for what may well be his last state visit.

6 月，[GPE Washington] 通过了一项强制系安全带的法规。

> In June, [GPE Washington] passed a primary seatbelt law.

### 9.5.2 BIO 标注

> 9.5.2 BIO Tagging

对于 NER 这类片段识别问题，序列标注的一种标准方法是 BIO 标注（Ramshaw and Marcus, 1995）。这种方法使我们能够

> One standard approach to sequence labeling for a span-recognition problem like NER is BIO tagging (Ramshaw and Marcus, 1995). This is a method that allows us

> BIO 标注
>
> *BIO tagging*

把 NER 当作逐词的序列标注任务来处理，所用的标签同时刻画边界和命名实体类型。考察下面这个句子：

> to treat NER like a word-by-word sequence labeling task, via tags that capture both the boundary and the named entity type. Consider the following sentence:

[PER Jane Villanueva] 属于 [ORG United]，后者是 [ORG United Airlines Holding] 的一个下属单位，他说该票价适用于 [LOC Chicago] 航线。

> [PER Jane Villanueva ] of [ORG United] , a unit of [ORG United Airlines Holding] , said the fare applies to the [LOC Chicago ] route.

图 9.9 展示了同一段摘录用 BIO 标注表示的结果，以及

> Figure 9.9 shows the same excerpt represented with BIO tagging, as well as

> BIO

被称为 IO 标注和 BIOES 标注的变体。在 BIO 标注中，我们用标签 B 标注任何开启一个我们关注的片段的词元，出现在片段内部的词元标注为 I，而位于任何关注片段之外的词元标注为 O。虽然只有一个 O 标签，但每个命名实体类别都会有各自不同的 B 标签与 I 标签。

> variants called IO tagging and BIOES tagging. In BIO tagging we label any token that begins a span of interest with the label B, tokens that occur inside a span are tagged with an I, and any tokens outside of any span of interest are labeled O. While there is only one O tag, we’ll have distinct B and I tags for each named entity class.

因此标签的数量为 2n+1，其中 n 是实体类型的数量。BIO 标注能够表示与方括号记法完全相同的信息，但其优点在于，我们可以像词性标注那样，以同样简单的序列建模方式来表示该任务：为每个输入词 xi 指派单个标签 yi：

> The number of tags is thus 2n+1, where n is the number of entity types. BIO tagging can represent exactly the same information as the bracketed notation, but has the advantage that we can represent the task in the same simple sequence modeling way as part-of-speech tagging: assigning a single label yi to each input word xi:

| 词<br>Words |  |  | IO 标签<br>IO Label |  | BIO 标签<br>BIO Label |  | BIOES 标签<br>BIOES Label |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Jane |  |  | I-PER |  | B-PER |  | B-PER |
| Villanueva |  |  | I-PER |  | I-PER |  | E-PER |
| of |  |  | O |  | O |  | O |
| United |  |  | I-ORG |  | B-ORG |  | B-ORG |
| Airlines |  |  | I-ORG |  | I-ORG |  | I-ORG |
| Holding |  |  | I-ORG |  | I-ORG |  | E-ORG |
| discussed |  |  | O |  | O |  | O |
| the |  |  | O |  | O |  | O |
| Chicago |  |  | I-LOC |  | B-LOC |  | S-LOC |
| route |  |  | O |  | O |  | O |
| . |  |  | O |  | O |  | O |
| 图 9.9<br>Figure 9.9 | 将 NER 视为序列模型，展示 IO、BIO 与 BIOES 标注。<br>NER as a sequence model, showing IO, BIO, and BIOES taggings. |  |  |  |  |  |  |

我们还展示了两种变体标注方案：IO 标注，它去掉了 B 标签，因而丢失了一部分

> We’ve also shown two variant tagging schemes: IO tagging, which loses some

信息；以及 BIOES 标注，它为片段的结束增加了一个结束标签 E，并为只由一个词构成的片段增加了一个片段标签 S。

> information by eliminating the B tag, and BIOES tagging, which adds an end tag E for the end of a span, and a span tag S for a span consisting of only one word.

### 9.5.3 序列标注

> 9.5.3 Sequence Labeling

在序列标注中，我们把与每个输入词元对应的最终输出向量传入一个分类器，由它对可能的标签集合 240 第 9 章 • 掩码语言模型 输出 softmax 分布。对于单层前馈分类器，需要学习的权重集合是大小为 [d × k] 的 WK，其中 k 是该任务可能的标签数。可以采用贪心方法生成最终的输出标签序列，即把每个词元的 argmax 标签当作可能的答案。图 9.10 展示了这种方法的一个示例，其中 yi 是标签上的概率向量，k 是标签的索引。

> In sequence labeling, we pass the final output vector corresponding to each input token to a classifier that produces a softmax distribution over the possible set of 240 CHAPTER 9 • MASKED LANGUAGE MODELS tags. For a single feedforward layer classifier, the set of weights to be learned is WK of size [d × k], where k is the number of possible tags for the task. A greedy approach, where the argmax tag for each token is taken as a likely answer, can be used to generate the final output tag sequence. Fig. 9.10 illustrates an example of this approach, where yi is a vector of probabilities over tags, and k indexes the tags.

yi = softmax(hL

> (9.7)

i WK)

ti = argmaxk(yi)

> (9.8)

另一种做法是，把 softmax 为每个输入词元给出的标签分布传入一个条件随机场（conditional random field，CRF）层，该层可以考虑全局的标签级转移（关于 CRF 参见第 18 章）。

> Alternatively, the distribution over labels provided by the softmax for each input token can be passed to a conditional random field (CRF) layer which can take global tag-level transitions into account (see Chapter 18 on CRFs).

B-PER I-PER O B-ORG I-ORG I-ORG O

> argmax

> yi

![](images/img_296.png)

![](images/img_296.png)

![](images/img_296.png)

![](images/img_296.png)

![](images/img_296.png)

![](images/img_296.png)

![](images/img_296.png)

### NER 头

> NER head

> WK WK WK WK WK WK WK

> hi

![](images/img_298.png)

双向 Transformer 编码器

> Bidirectional Transformer Encoder

![](images/img_302.png)

![](images/img_302.png)

![](images/img_302.png)

![](images/img_302.png)

![](images/img_302.png)

![](images/img_302.png)

![](images/img_302.png)

![](images/img_302.png)

> + + + + + + + +

> i i i i i i i i

> E E E E E E E E

[CLS] Jane Villanueva of United Airlines Holding discussed

> 图 9.10 使用双向 Transformer 编码器进行命名实体识别的序列标注。每个输入词元的输出向量被送入一个简单的 k 路分类器。
>
> *Figure 9.10 Sequence labeling for named entity recognition with a bidirectional transformer encoder. The output vector for each input token is passed to a simple k-way classifier.*

分词与 NER

> Tokenization and NER

注意，NER 的监督训练数据通常采用 BIO 标签的形式，这些标签与按词切分的文本相关联。例如，下面这个包含两个命名实体的句子：

> Note that supervised training data for NER is typically in the form of BIO tags associated with text segmented at the word level. For example the following sentence containing two named entities:

[LOC Mt. Sanitas ] is in [LOC Sunshine Canyon] .

会具有如下的一组逐词 BIO 标签。

> would have the following set of per-word BIO tags.

(9.9) Mt. Sanitas is in Sunshine Canyon .

B-LOC I-LOC O O B-LOC I-LOC O

遗憾的是，该句的 WordPiece 词元序列并不能直接

> Unfortunately, the sequence of WordPiece tokens for this sentence doesn’t align

与标注中的 BIO 标签对齐：

> directly with BIO tags in the annotation:

’Mt’, ’.’, ’San’, ’##itas’, ’is’, ’in’, ’Sunshine’, ’Canyon’ ’.’

为解决这种不对齐的问题，我们需要一种在训练期间为子词

> To deal with this misalignment, we need a way to assign BIO tags to subword

词元分配 BIO 标签的方法，以及一种在解码期间从 9.6 • 小结 241 子词中恢复词级标签的对应方法。在训练时，我们只需把与每个词相关联的金标准标签分配给由它派生出的所有子词词元。

> tokens during training and a corresponding way to recover word-level tags from 9.6 • SUMMARY 241 subwords during decoding. For training, we can just assign the gold-standard tag associated with each word to all of the subword tokens derived from it.

对于解码，最简单的做法是使用与

> For decoding, the simplest approach is to use the argmax BIO tag associated with

一个词的首个子词词元相关联的 argmax BIO 标签。因此，在我们的例子中，分配给“Mt”的 BIO 标签会被分配给“Mt.”，分配给“San”的标签会被分配给“Sanitas”，实际上忽略了分配给“.”和“##itas”的标签中所包含的信息。更复杂的方法会综合各子词上的标签概率分布，以试图找到最优的词级标签。

> the first subword token of a word. Thus, in our example, the BIO tag assigned to“Mt” would be assigned to “Mt.” and the tag assigned to “San” would be assigned to “Sanitas”, effectively ignoring the information in the tags assigned to “.” and“##itas”. More complex approaches combine the distribution of tag probabilities across the subwords in an attempt to find an optimal word-level tag.

### 9.5.4 命名实体识别的评估

> 9.5.4 Evaluating Named Entity Recognition

命名实体识别器通过召回率、精确率和 F1 值来评估。回想一下，召回率是正确标注的响应数与应当被标注的响应总数之比；精确率是正确标注的响应数与已标注的响应总数之比；而 F1 值是二者的调和平均。

> Named entity recognizers are evaluated by recall, precision, and F1 measure. Recall that recall is the ratio of the number of correctly labeled responses to the total that should have been labeled; precision is the ratio of the number of correctly labeled responses to the total labeled; and F1 measure is the harmonic mean of the two.

为了判断两个 NER 系统的 F1 分数之间的差异是否为显著差异，我们使用配对自助法检验（paired bootstrap test），或与之类似的随机化检验（randomization test）（第 4.11 节）。

> To know if the difference between the F1 scores of two NER systems is a significant difference, we use the paired bootstrap test, or the similar randomization test(Section 4.11).

对于命名实体标注而言，响应单位是实体而不是词。

> For named entity tagging, the entity rather than the word is the unit of response.

因此在图 9.9 的例子中，两个实体 Jane Villanueva 和 United Airlines Holding 以及非实体 discussed 各自都算作一个响应。

> Thus in the example in Fig. 9.9, the two entities Jane Villanueva and United Airlines Holding and the non-entity discussed would each count as a single response.

命名实体标注包含一个切分成分，而这一成分在

> The fact that named entity tagging has a segmentation component which is not

文本分类或词性标注等任务中并不存在，这给评估带来了一些问题。例如，一个把 Jane 而非 Jane Villanueva 标注为人名的系统会造成两个错误：一个对 O 的假正例和一个对 I-PER 的假负例。此外，以实体作为响应单位、却以词作为训练单位，意味着训练条件与测试条件之间存在不匹配。

> present in tasks like text categorization or part-of-speech tagging causes some problems with evaluation. For example, a system that labeled Jane but not Jane Villanueva as a person would cause two errors, a false positive for O and a false negative for I-PER. In addition, using entities as the unit of response but words as the unit of training means that there is a mismatch between the training and test conditions.

## 9.6 小结

> 9.6 Summary

本章介绍了双向编码器和掩码语言模型。以下是我们所涉及的主要内容的总结：

> This chapter has introduced the bidirectional encoder and the masked language model. Here’s a summary of the main points that we covered:

- 语言模型有三大类主要架构：编码器（本章）、解码器以及编码器-解码器。我们在第 1 章和第 7 章见到了解码器模型，并将在第 13 章见到编码器-解码器。
- 双向编码器可以利用整个输入上下文，为输入嵌入生成上下文相关的表示。
- 基于双向编码器的预训练语言模型可以使用掩码语言模型目标来学习，即训练模型去猜测输入中缺失的信息。
- 特定词元列上每个 Transformer 块或组件的向量输出都是一个上下文嵌入，它表示该词元在上下文中的意义的某个方面。
- 词义是词的意义某一方面的离散表示。上下文嵌入则提供了一种连续的高维意义模型，它比完全离散的词义更为丰富。

> There are three major architectures for language models: the encoder (this chapter), the decoder, and the encoder-decoder. We saw decoder models in Chapter 1 and Chapter 7, and we’ll see encoder-decoders in Chapter 13.
> Bidirectional encoders can be used to generate contextualized representations of input embeddings using the entire input context.
> Pretrained language models based on bidirectional encoders can be learned using a masked language model objective where a model is trained to guess the missing information from an input.
> The vector output of each transformer block or component in a particular token column is a contextual embedding that represents some aspect of the meaning of a token in context.
> A word sense is a discrete representation of one aspect of the meaning of a word. Contextual embeddings offer a continuous high-dimensional model of meaning that is richer than fully discrete senses.

242 第 9 章 • 掩码语言模型

> 242 CHAPTER 9 • MASKED LANGUAGE MODELS

- 上下文嵌入之间的余弦值可作为对上下文中两个词之间相似度建模的一种方式，不过首先需要对嵌入做若干变换。
- 在预训练模型输出之上添加轻量级分类器层，即可针对特定应用对预训练语言模型进行微调。
- 这些应用可以包括诸如情感分析一类的序列分类任务、诸如自然语言推理一类的序列对分类任务，或诸如命名实体识别一类的序列标注任务。

> The cosine between contextual embeddings can be used as one way to model the similarity between two words in context, although some transformations to the embeddings are required first.
> Pretrained language models can be finetuned for specific applications by adding lightweight classifier layers on top of the outputs of the pretrained model.
> These applications can include sequence classification tasks like sentiment analysis, sequence-pair classification tasks like natural language inference, or sequence labeling tasks like named entity recognition.

## 历史注记

> Historical Notes

历史部分待定。

> History TBD.
