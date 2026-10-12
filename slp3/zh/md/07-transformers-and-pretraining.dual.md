# 第 7 章 Transformer 与预训练

### 章

> CHAPTER

# 7 Transformer 与预训练

> 7 Transformers and Pretraining

“记忆的真正艺术就是注意的艺术”

> “The true art of memory is the art of attention ”

塞缪尔·约翰逊（Samuel Johnson），《Idler》第 74 期，1759 年 9 月

> Samuel Johnson, Idler #74, September 1759

本章介绍 Transformer —— 构建大型语言模型的标准架构，以及如何预训练它们、如何用它们生成文本。我们将介绍用于从左到右（有时称为因果、自回归或解码器）语言建模的 Transformer，其中给定一个输入词元序列，通过条件于先前的上下文逐个预测输出词元；其他架构（如编码器架构）将在第 9 章介绍。

> In this chapter we introduce the transformer, the standard architecture for building large language models, and how to pretrain them and how to use them to generate text. We’ll introduce transformers for left-to-right (sometimes called causal or autoregressive or decoder) language modeling, in which we are given a sequence of input tokens and predict output tokens one by one by conditioning on the prior context; we’ll introduce other architectures like the encoder architecture in Chapter 9.

| 输出概率（对词元）<br>Softmax<br>反嵌入<br>+<br>前馈<br>层归一化<br>残差 L 次<br>流 +<br>多头<br>注意力<br>层归一化<br>+ 位置<br>嵌入<br>输入词元<br>output probabilities (over tokens)<br>Softmax<br>Unembedding<br>+<br>Feedforward<br>Layer Norm<br>residual L times<br>stream +<br>MultiHead<br>Attention<br>Layer Norm<br>+ Positional<br>Embedding<br>input token |  |
| --- | --- |
| 图 7.1<br>Figure 7.1 | 用于语言建模的 Transformer 解码器，展示残差流如何<br>A transformer decoder for language modeling, showing the residual stream for |

> 输出概率（对词元）
>
> *output probabilities (over tokens)*

> Softmax

> 反嵌入
>
> *Unembedding*

![](images/img_40.png)

![](images/img_42.png)

> + +

> 前馈 前馈
>
> *Feedforward Feedforward*

> 层归一化 层归一化
>
> *Layer Norm Layer Norm*

> 残差 残差 L 次 流 流 + +
>
> *residual residual L times stream stream + +*

> 多头 多头 注意力 注意力
>
> *MultiHead MultiHead Attention Attention*

> 层归一化 层归一化
>
> *Layer Norm Layer Norm*

> +

> 位置
>
> *Positional*

> 嵌入
>
> *Embedding*

> 输入词元
>
> *input token*

> 处理一个输入词元的过程。单个词元被嵌入并在网络中向前传递，前馈与注意力组件在其中添加信息。多头注意力层从相邻的词元流中获取输入（未详细展示）。因此，这是自回归 Transformer 语言模型中的一列，接受一个输入词元并输出下一个词元上的分布。
>
> *processing an input token. A single token is embedded and passed forward in the network, with the feedforward and attention components adding information. The multihead attention layer takes inputs (not shown in detail) from the neighboring token streams. This is thus one column of an autoregressive transformer language model, taking an input token and outputting a distribution over next tokens.*

图 7.1 勾勒了 Transformer 架构，追踪单个词元

> Fig. 7.1 sketches the transformer architecture following a single token as it

在网络各层中向上传递的过程。每个词元首先从嵌入矩阵 E 转换为一个嵌入。回忆第 6 章 6.5 节，E 是一个线性层，把词元 id 映射为表示该词元的向量嵌入。词汇表中的每个词元在 E 中都有一个初始的嵌入表示。

> passes up through the layers of the network. Each token is first converted to an embedding from the embedding matrix E. Recall from Chapter 6 in Section 6.5 that E is a linear layer that maps a token id to a vector embedding representing that token. Each token in the vocabulary has an initial embedding representation in E.

Transformer 还有一种特殊机制，用于编码词元在输入字符串中的位置/索引，并将它直接加到嵌入上。所得的 178 第 7 章 • Transformer 与预训练 嵌入同时表示该词及其位置，然后通过一组 L 个 Transformer 块。

> Transformers also have a special mechanism for encoding the position/index of the token in the input string, which is simply added to the embedding. The resulting 178 CHAPTER 7 • TRANSFORMERS AND PRETRAINING embedding represents both the word and its position, and is then passed through a set of L transformer blocks.

通常把每个这类 Transformer 块看作一条流的一部分，

> It’s common to think of each of these transformer blocks as part of a stream in

在这条流中，输入嵌入被直接向上传递到输出，同时又通过应用各种处理模块而得到丰富：多头注意力层、前馈网络以及层归一化。对任意输入词元而言，任意层处流的值都是一个向量，它等于该词元的原始嵌入与之前所有层和块的全部输出之和。

> which the input embedding is directly passed up to the output, while simultaneously being enriched by the application of various processing modules: the multi-head attention layer, feedforward networks and the layer normalization. The value of the stream at any layer for any input token is a vector that is the sum of the original embedding for that token and all the outputs from all the previous layers and blocks.

Transformer 的核心直觉，以及使它

> The core intuition of the transformer, and the component that distinguishes it

区别于第 6 章所见前馈层的组件，就是这个多头注意力层，也叫自注意力层。注意力可以看作一种方式：通过注意并整合来自周围词元的信息来构建词元含义的上下文表示，帮助模型学习词元在长跨度上如何相互关联。它也可以看作一种把信息从一条残差流移动到另一条残差流的方式，用一个词元位置上的信息来增强另一个词元位置上的流。

> from the feedforward layers we saw in Chapter 6, is this multi-head attention layer, also called a self-attention layer. Attention can be thought of as a way to build contextual representations of a token’s meaning by attending to and integrating information from surrounding tokens, helping the model learn how tokens relate to each other over large spans. It can also be thought of as a way to move information from one residual stream to another, augmenting the stream at one token position with information from another token position.

经过 L 个 Transformer 块之后，我们取

> After the L transformer blocks we take the output embedding that is produced

最后一个 Transformer 块产生的输出嵌入，让它通过线性反嵌入矩阵 U，再对词汇表做 softmax，生成可能的下一个词元上的分布。最后这两个组件（反嵌入矩阵和 softmax）有时称为语言建模头。本章余下部分将更详细地介绍注意力以及其余这些模块。

> by the final transformer block, pass it through a linear unembedding matrix U and then a softmax over the vocabulary to generate a distribution over possible next tokens. These last two components (the unembedding matrix and the softmax) are sometimes called the language modeling head. In the rest of this chapter we’ll introduce attention and the rest of these modules in more detail.

| 下一个词元 long and thanks for all<br>语言 …<br>建模 logits logits logits logits logits<br>U U U U U<br>头<br>… … … … …<br>堆叠的<br>Transformer …<br>块<br>x1 x2 x3 x4 x5 …<br>+ 1 + 2 + 3 + 4 + 5<br>输入 …<br>编码 E E E E E<br>输入词元 So long and thanks for<br>Next token long and thanks for all<br>Language …<br>Modeling logits logits logits logits logits<br>U U U U U<br>Head<br>… … … … …<br>Stacked<br>Transformer …<br>Blocks<br>x1 x2 x3 x4 x5 …<br>+ 1 + 2 + 3 + 4 + 5<br>Input …<br>Encoding E E E E E<br>Input tokens So long and thanks for |  |
| --- | --- |
| 图 7.2<br>Figure 7.2 | （从左到右的）Transformer 架构，展示每个输入词元如何<br>The architecture of a (left-to-right) transformer, showing how each input token |

> long and thanks for all

> 下一个词元
>
> *Next token*

![](images/img_87.png)

![](images/img_87.png)

![](images/img_87.png)

![](images/img_87.png)

![](images/img_87.png)

> 语言
>
> *Language*

…

> logits logits logits logits logits

> 建模
>
> *Modeling*

> U U U U U

> 头
>
> *Head*

![](images/img_79.png)

![](images/img_79.png)

![](images/img_79.png)

![](images/img_79.png)

![](images/img_79.png)

… … … … …

> 堆叠的
>
> *Stacked*

…

> Transformer 块
>
> *Transformer Blocks*

…

> x1 x2 x3 x4 x5

![](images/img_85.png)

![](images/img_85.png)

![](images/img_85.png)

![](images/img_85.png)

![](images/img_85.png)

> 输入 + 1 + 2 + 3 + 4 + 5
>
> *Input + 1 + 2 + 3 + 4 + 5*

…

> 编码
>
> *Encoding*

> E E E E E

> So long and thanks for

> 输入词元
>
> *Input tokens*

> 被编码，经过一组堆叠的 transformer 块，然后通过一个预测下一个词元的语言模型头。残差流中每个词元位置上的嵌入沿堆栈向上传递，图中的箭头显示了前序词元的隐藏表示中的信息是如何一并被整合进来的。
>
> *gets encoded, passed through a set of stacked transformer blocks, and then a language model head that predicts the next token. The embeddings at each token position in the residual stream are passed up the stack, and the arrows in the figure shows how information from the hidden representations of preceding tokens are also incorporated.*

图 7.2 展示了应用于一个上下文窗口的 transformer 架构，该窗口包含

> Fig. 7.2 shows the transformer architecture applied to a context window with the

单词 So long and thanks for，并在每个词元位置显示最可能生成的词元。在这张完整的图中，n 个词元上堆叠的 L 个块将整个输入向量上下文窗口（x1,...,xn）映射为相同长度的输出向量窗口（h1,...,hn）。一列可以包含从 L = 12 到 L = 96 个甚至更多个堆叠的块。图中的箭头显示了前序词元的隐藏表示中的信息如何被整合进 transformer 7.1 • 注意力 179 块。

> words So long and thanks for, showing at each token position what is the most likely token to be generated. In this full figure, the stack of L blocks over n tokens maps an entire context window of input vectors (x1,...,xn) to a window of output vectors (h1,...,hn) of the same length. A column might contain from L = 12 to L = 96 or more stacked blocks. The arrows in the figure show how information from the hidden representations of preceding tokens is incorporated into the transformer 7.1 • ATTENTION 179 block.

基于 transformer 的语言模型很复杂，因此细节将

> Transformer-based language models are complex, and so the details will unfold

在本章以及接下来几章中展开，此外第 1 章还给出了高层概览。本章将介绍多头注意力、transformer 块的其余部分、transformer 的输入编码和语言建模头组件、生成输出文本的解码与采样的概念，以及预训练的细节。第 8 章介绍后训练：为完成 NLP 任务而对语言模型进行微调和指令微调，以及使模型与人类偏好对齐。第 9 章介绍掩码语言建模和双向 transformer 编码器模型 BERT 系列。第 13 章将介绍采用编码器-解码器架构的机器翻译。而在第 16 章，我们将看到 transformer 在语音识别中的应用，以及编码器-解码器架构的进一步使用。

> over this chapter and the next few chapters, in addition to the high-level overview in Chapter 1. This chapter will introduce multi-head attention, the rest of the transformer block, the input encoding and language modeling head components of the transformer, the concepts of decoding and sampling to generate output text, and the details of pretraining. Chapter 8 introduces post-training: fine-tuning and instructiontuning language models to perform NLP tasks, and aligning the model with human preferences. Chapter 9 introduces masked language modeling and the BERT family of bidirectional transformer encoder models. Chapter 13 will introduce machine translation with the encoder-decoder architecture. And we’ll see application of the transformer to speech recognition, as well as further use of the encoder-decoder architecture, in Chapter 16.

## 7.1 注意力

> 7.1 Attention

回想第 5 章，对于 word2vec 和其他静态嵌入，一个词的含义表示总是不随上下文改变的同一个向量：例如单词 chicken 总是由同一个固定向量表示。因此，单词 it 的静态向量也许能以某种方式编码出它是一个用于动物和无生命实体的代词。但在上下文中，它的含义要丰富得多。

> Recall from Chapter 5 that for word2vec and other static embeddings, the representation of a word’s meaning is always the same vector irrespective of the context: the word chicken, for example, is always represented by the same fixed vector. So a static vector for the word it might somehow encode that this is a pronoun used for animals and inanimate entities. But in context it has a much richer meaning.

考虑 it 在下面这两个句子之一中的情况：

> Consider it in one of these two sentences:

（7.1）鸡没有过马路，因为它太累了。（7.2）鸡没有过马路，因为它太宽了。

> (7.1) The chicken didn’t cross the road because it was too tired.(7.2) The chicken didn’t cross the road because it was too wide.

在（7.1）中，it 指的是鸡（即读者知道是鸡太累了），而在（7.2）中，it 指的是路（读者知道是路太宽了）。1 也就是说，如果我们要计算这个句子的含义，就需要让 it 的含义在第一个句子中与鸡相关联、在第二个句子中与路相关联，即对上下文敏感。

> In (7.1) it is the chicken (i.e., the reader knows that the chicken was tired), while in (7.2) it is the road (and the reader knows that the road was wide).1 That is, if we are to compute the meaning of this sentence, we’ll need the meaning of it to be associated with the chicken in the first sentence and associated with the road in the second one, sensitive to the context.

此外，考虑像因果语言模型那样从左到右阅读，把句子处理到单词 it 为止：

> Furthermore, consider reading left to right like a causal language model, processing the sentence up to the word it:

（7.3）鸡没有过马路，因为 it

> (7.3) The chicken didn’t cross the road because it

此时我们还不知道它最终会指代哪个事物！因此，此刻 it 的表示可能同时带有鸡和路两方面的成分，因为读者正试图猜测接下来会发生什么。

> At this point we don’t yet know which thing it is going to end up referring to! So a representation of it at this point might have aspects of both chicken and road as the reader is trying to guess what happens next.

词语与可能

> This fact that words have rich linguistic relationships with other words that may

相距很远的其他词语之间存在丰富的语言关系，这一现象贯穿于语言之中。再看两个例子：

> be far away pervades language. Consider two more examples:

（7.4）柜子的钥匙在桌子上。（7.5）我沿着池塘走，注意到岸边的一棵树。

> (7.4) The keys to the cabinet are on the table.(7.5) I walked along the pond, and noticed one of the trees along the bank.

在（7.4）中，短语 The keys 是句子的主语，在英语和许多语言中它必须在语法数上与动词 are 保持一致；在此例中两者都是复数。在英语中，我们不能把像 is 这样的单数动词与像 keys 这样的复数主语连用（我们将在第 19 章进一步讨论一致性）。在（7.5）中，我们知道 bank 指的是

> In (7.4), the phrase The keys is the subject of the sentence, and in English and many languages, must agree in grammatical number with the verb are; in this case both are plural. In English we can’t use a singular verb like is with a plural subject like keys(we’ll discuss agreement more in Chapter 19). In (7.5), we know that bank refers

> 我们说在第一个例子中 it 与鸡同指，在第二个例子中 it 与
>
> *We say that in the first example it corefers with the chicken, and in the second it corefers with the*

> 1

> 路同指；我们将在第 24 章回到这个问题。
>
> *road; we’ll return to this in Chapter 24.*

180 第 7 章 • TRANSFORMERS 与预训练

> 180 CHAPTER 7 • TRANSFORMERS AND PRETRAINING

池塘或河流的岸边，而不是金融机构，这是由于上下文，包括像 pond 这样的词。（我们将在第 9 章进一步讨论词义。）

> to the side of a pond or river and not a financial institution because of the context, including words like pond. (We’ll discuss word senses more in Chapter 9.)

所有这些例子的要点在于，这些帮助我们计算上下文中词义的上下文词，在句子或段落中可能相距相当远。Transformer 能够构建词义的上下文相关表示，即上下

> The point of all these examples is that these contextual words that help us compute the meaning of words in context can be quite far away in the sentence or paragraph. Transformers can build contextual representations of word meaning, contex-

> 上下文的
>
> *contextual*

文嵌入，其方式是整合这些有帮助的上下文词的含义。在一个

> tual embeddings, by integrating the meaning of these helpful contextual words. In a

> 嵌入
>
> *embeddings*

transformer 中，我们逐层构建越来越丰富的输入词元含义的上下文相关表示。在每一层，我们通过把来自上一层的关于词元 i 的信息与关于相邻词元的信息相结合，来计算词元 i 的表示，从而为每个位置上的每个词生成上下文相关表示。

> transformer, layer by layer, we build up richer and richer contextualized representations of the meanings of input tokens. At each layer, we compute the representation of a token i by combining information about i from the previous layer with information about the neighboring tokens to produce a contextualized representation for each word at each position.

注意力是 transformer 中的一种机制，它对

> Attention is the mechanism in the transformer that weighs and combines the

来自第 k 层上下文中适当其他词元的表示进行加权和组合，以构建第 k + 1 层中词元的表示。

> representations from appropriate other tokens in the context from layer k to build the representation for tokens in layer k +1.

| 与输入词元对应的列<br>chicken because<br>didn’t<br>cross tired<br>第 k+1 层 road<br>The the was too<br>it<br>自注意力分布<br>chicken because<br>didn’t<br>第 k 层 cross road tired<br>The the was too<br>it<br>columns corresponding to input tokens<br>chicken because<br>didn’t<br>cross tired<br>Layer k+1 road<br>The the was too<br>it<br>self-attention distribution<br>chicken because<br>didn’t<br>Layer k cross road tired<br>The the was too<br>it |  |
| --- | --- |
| 图 7.3<br>Figure 7.3 | 作为……计算的一部分的自注意力权重分布 α<br>The self-attention weight distribution α that is part of the computation of the |

> 与输入 token 对应的列
>
> *columns corresponding to input tokens*

> chicken didn’t because

> Layer k+1 cross road tired

> The the it was too

> 自注意力分布
>
> *self-attention distribution*

> chicken didn’t because

> Layer k cross road tired

> The the it was too

> 第 k+1 层中单词 it 的表示。在计算 it 的表示时，我们对第 k 层的各个单词给予不同的关注，颜色越深表示自注意力值越高。注意，transformer 高度关注与 token chicken 和 road 对应的列，这是一个合理的结果，因为在 it 出现的位置上，它有可能与 the chicken 或 the road 同指，因此我们希望 it 的表示能够利用这些较早单词的表示。图改编自 Uszkoreit (2017)。
>
> *representation for the word it at layer k +1. In computing the representation for it, we attend differently to the various words at layer k, with darker shades indicating higher self-attention values. Note that the transformer is attending highly to the columns corresponding to the tokens chicken and road, a sensible result, since at the point where it occurs, it could plausibly corefer with the chicken or the road, and hence we’d like the representation for it to draw on the representation for these earlier words. Figure adapted from Uszkoreit (2017).*

图 7.3 展示了一个从 transformer 简化而来的示意图（Uszkoreit，

> Fig. 7.3 shows a schematic example simplified from a transformer (Uszkoreit,

2017）。该图描述的情形是：当前 token 为 it，而我们需要在 transformer 的第 k+1 层为这个 token 计算上下文表示，并利用此前每个 token（第 k 层）的表示。图中用颜色表示对各上下文单词的注意力分布：token chicken 和 road 都具有很高的注意力权重，这意味着在计算 it 的表示时，我们会最多地利用 chicken 和 road 的表示。这将有助于构建 it 的最终表示，因为它最终会与 chicken 或 road 之一同指。

> 2017). The figure describes the situation when the current token is it and we need to compute a contextual representation for this token at layer k+1 of the transformer, drawing on the representations (from layer k) of every prior token. The figure uses color to represent the attention distribution over the contextual words: the tokens chicken and road both have a high attention weight, meaning that as we are computing the representation for it, we will draw most heavily on the representation for chicken and road. This will be useful in building the final representation for it, since it will end up coreferring with either chicken or road.

下面我们来看这种注意力分布是如何表示和计算的。

> Let’s now turn to how this attention distribution is represented and computed.

### 7.1.1 更形式化的注意力

> 7.1.1 Attention more formally

如我们所说，注意力计算是一种为 transformer 某一层中的 token 计算向量表示的方法，它通过有选择地关注并整合上一层中此前 token 的信息来实现。注意力接收一个 7.1 • ATTENTION 181 与位置 i 处输入 token 对应的输入表示 xi，以及由此前输入 x1..xi−1 构成的上下文窗口，并产出一个输出 ai。

> As we’ve said, the attention computation is a way to compute a vector representation for a token at a particular layer of a transformer, by selectively attending to and integrating information from prior tokens at the previous layer. Attention takes an 7.1 • ATTENTION 181 input representation xi corresponding to the input token at position i, and a context window of prior inputs x1..xi−1, and produces an output ai.

在因果式、从左到右的语言模型中，上下文是此前出现过的任何词。

> In causal, left-to-right language models, the context is any of the prior words.

也就是说，在处理 xi 时，模型可以访问 xi 以及上下文窗口中所有此前 token 的表示（上下文窗口由数千个 token 组成），但无法访问 i 之后的任何 token。（相比之下，在第 9 章中我们会将注意力推广，使其也能向前看到未来的词。）

> That is, when processing xi, the model has access to xi as well as the representations of all the prior tokens in the context window (context windows consist of thousands of tokens) but no tokens after i. (By contrast, in Chapter 9 we’ll generalize attention so it can also look ahead to future words.)

图 7.4 展示了整个因果自注意力层中的这一信息流动，

> Fig. 7.4 illustrates this flow of information in an entire causal self-attention layer,

其中相同的注意力计算在每个 token 位置上并行发生。

> in which this same attention computation happens in parallel at each token position

- 因此，一个自注意力层将输入序列 (x1,...,xn) 映射为长度相同的输出序列 (a1,...,an)。

> Thus a self-attention layer maps input sequences (x1,...,xn) to output sequences of the same length (a1,...,an).

| a1 a2 a3 a4 a5<br>自注意力<br>注意力 注意力 注意力 注意力 注意力<br>层<br>x1 x2 x3 x4 x5<br>a1 a2 a3 a4 a5<br>Self-Attention<br>attention attention attention attention attention<br>Layer<br>x1 x2 x3 x4 x5 |  |
| --- | --- |
| 图 7.4<br>Figure 7.4 | 因果自注意力中的信息流。在处理每个输入 x i 时，<br>Information flow in causal self-attention. When processing each input x i, the |

> a1 a2 a3 a4 a5

![](images/img_149.png)

> 自注意力
>
> *Self-Attention*

> 注意力 注意力 注意力 注意力 注意力
>
> *attention attention attention attention attention*

> 层
>
> *Layer*

> x1 x2 x3 x4 x5

> 图 7.4 因果自注意力中的信息流。在处理每个输入 xi 时，模型会关注直到并包括 xi 在内的所有输入。
>
> *Figure 7.4 Information flow in causal self-attention. When processing each input xi, the model attends to all the inputs up to, and including xi.*

注意力的简化版本 从本质上讲，注意力其实只是上下文向量的加权和，只是在权重如何计算以及求和的对象上附加了许多复杂之处。出于教学目的，我们先描述一种简化的注意力直觉：token 位置 i 处的注意力输出 ai 就是所有表示 x j（对所有 j ≤i）的加权和；我们用 αij 表示 xj 应对 ai 贡献多少：

> Simplified version of attention At its heart, attention is really just a weighted sum of context vectors, with a lot of complications added to how the weights are computed and what gets summed. For pedagogical purposes let’s first describe a simplified intuition of attention, in which the attention output ai at token position i is simply the weighted sum of all the representations x j, for all j ≤i; we’ll use αij to mean how much xj should contribute to ai:

X

简化版本：

> Simplified version:

> (7.6)

ai = αijxj

> j≤i

每个 αi j 都是一个标量，用于在对输入求和时对输入 x j 的值加权，

> Each αi j is a scalar used for weighing the value of input x j when summing up

以计算 ai。我们该如何计算这个 α 权重？在注意力中，我们按照每个先前嵌入与当前 token 的相似程度成比例地为其加权。

> the inputs to compute ai. How shall we compute this α weighting? In attention we weight each prior embedding proportionally to how similar it is to the current token

- 因此，注意力的输出是先前 token 的嵌入之和，其权重为它们与当前 token 嵌入的相似度。我们通过点积计算相似度分数，点积将两个向量映射为一个取值范围从 −∞ 到 ∞ 的标量值。分数越大，被比较的向量就越相似。我们会用 softmax 对这些分数进行归一化，得到权重向量 αij，j ≤i。

> So the output of attention is a sum of the embeddings of prior tokens weighted by their similarity with the current token embedding. We compute similarity scores via dot product, which maps two vectors into a scalar value ranging from −∞to∞. The larger the score, the more similar the vectors that are being compared. We’ll normalize these scores with a softmax to create the vector of weights αij, j ≤i.

简化版本：score(xi,x j) = xi ·xj

> Simplified Version: score(xi,x j) = xi ·xj

> (7.7)

αij = softmax(score(xi,x j)) ∀j ≤i

> (7.8)

因此，在图 7.4 中，我们通过计算三个分数来计算 a3：x3 ·x1、x3 ·x2 和 x3 ·x3，用 softmax 将它们归一化，并把得到的概率用作权重，表示它们各自与当前位置 3 的相关程度。当然，softmax 权重很可能对 xi 最高，因为 xi 与自身非常相似，从而得到较高的点积。但其他上下文词也可能与 i 相似，softmax 也会给这些词分配一些权重。然后我们用这些权重作为式 7.6 中的 α 值，计算出作为 a3 的加权和。

> Thus in Fig. 7.4 we compute a3 by computing three scores: x3 ·x1, x3 ·x2 and x3 ·x3, normalizing them by a softmax, and using the resulting probabilities as weights indicating each of their proportional relevance to the current position 3. Of course, the softmax weight will likely be highest for xi, since xi is very similar to itself, resulting in a high dot product. But other context words may also be similar to i, and the softmax will also assign some weight to those words. Then we use these weights as the α values in Eq. 7.6 to compute the weighted sum that is our a3.

式 7.6 – 7.8 中的简化注意力展示了这种基于注意力的

> The simplified attention in equations 7.6 – 7.8 demonstrates the attention-based

计算 ai 的方法：将 xi 与之前的向量进行比较，把这些分数归一化 182 第 7 章 • TRANSFORMERS 与预训练 为用于对之前向量之和加权的概率分布。但现在我们准备去掉这些简化。

> approach to computing ai: compare the xi to prior vectors, normalize those scores 182 CHAPTER 7 • TRANSFORMERS AND PRETRAINING into a probability distribution used to weight the sum of the prior vectors. But now we’re ready to remove the simplifications.

使用查询、键和值矩阵的单个注意力头 既然我们已经对注意力有了简单的直观认识，下面就来介绍真正的注意力头，也就是

> A single attention head using query, key, and value matrices Now that we’ve seen a simple intuition of attention, let’s introduce the actual attention head, the

> 注意力头
>
> *attention head*

Transformer 中使用的注意力版本。（head 一词在

> version of attention that’s used in transformers. (The word head is often used in

> 头
>
> *head*

Transformer 中常用于指代特定的结构化层。）注意力头让我们能够明确地表示每个输入嵌入在注意力过程中所扮演的三种不同角色：

> transformers to refer to specific structured layers). The attention head allows us to distinctly represent three different roles that each input embedding plays during the course of the attention process:

- 作为与之前的输入相比较的当前元素。我们把这一角色称为查询。

> As the current element being compared to the preceding inputs. We’ll refer to this role as a query.

> 查询
>
> *query*

- 作为与当前元素相比较以确定相似度权重的之前输入。我们把这一角色称为键。

> In its role as a preceding input that is being compared to the current element to determine a similarity weight. We’ll refer to this role as a key.

> 键
>
> *key*

- 最后，作为之前元素的值，被加权并求和

> And finally, as a value of a preceding element that gets weighted and summed

> 值
>
> *value*

以计算当前元素的输出。

> up to compute the output for the current element.

为了刻画这三种不同的角色，Transformer 引入了权重矩阵

> To capture these three different roles, transformers introduce weight matrices

WQ、WK 和 WV。这些权重会把每个输入向量 xi 投影为它作为查询、键或值的角色表示：

> WQ, WK, and WV. These weights will project each input vector xi into a representation of its role as a query, key, or value:

qi = xiWQ; ki = xiWK; vi = xiWV

> (7.9)

给定这些投影，在计算当前元素 xi 与某个之前元素 x j 的相似度时，我们使用当前元素的查询向量 qi 与之前元素的键向量 kj 之间的点积。此外，点积的结果可能是任意大的（正或负）值，而对大值取指数会在训练中导致数值问题并造成梯度丢失。为避免这一点，我们通过与查询和键向量维度（dk）的平方根相除，按与嵌入规模相关的因子对点积进行缩放。因此我们用式 7.11 替换简化的式 7.7。随后得到 αij 的 softmax 计算保持不变，但 headi 的输出计算现在基于对值向量 v 的加权求和（式 7.13）。

> Given these projections, when we are computing the similarity of the current element xi with some prior element x j, we’ll use the dot product between the current element’s query vector qi and the preceding element’s key vector kj. Furthermore, the result of a dot product can be an arbitrarily large (positive or negative) value, and exponentiating large values can lead to numerical issues and loss of gradients during training. To avoid this, we scale the dot product by a factor related to the size of the embeddings, via dividing by the square root of the dimensionality of the query and key vectors (dk). We thus replace the simplified Eq. 7.7 with Eq. 7.11. The ensuing softmax calculation resulting in αij remains the same, but the output calculation for headi is now based on a weighted sum over the value vectors v (Eq. 7.13).

下面是最后的一组等式，用于从单个输入向量 xi 计算单个自注意力输出向量 ai 的自注意力。这个版本的注意力通过对之前元素的值求和来计算 ai，其中每个值都按其键与当前元素查询的相似度加权：

> Here’s a final set of equations for computing self-attention for a single selfattention output vector ai from a single input vector xi. This version of attention computes ai by summing the values of the prior elements, each weighted by the similarity of its key to the query from the current element:

qi = xiWQ; kj = xjWK; vj = x jWV

> (7.10)

score(xi,x j) = qi ·kj

> (7.11)

√dk

αij = softmax(score(xi,x j)) ∀j ≤i

> (7.12)

X

> (7.13)

headi = αijvj

> j≤i

ai = headiWO

> (7.14)

我们在图 7.5 中展示了在序列中计算第三个输出 a3 的情形。

> We illustrate this in Fig. 7.5 for the case of calculating the value of the third output a3 in a sequence.

注意我们还引入了另一个矩阵 WO，它被左乘

> Note that we’ve also introduced one more matrix, WO, which is left-multiplied

于注意力头。这是为了重塑注意力头的输出所必需的。注意力的输入 xi 与注意力的输出 ai 都具有相同的维度[1 × d]。我们通常把 d 称为模型维度，而事实上，正如我们将在 7.1 • 注意力 183 中讨论的

> by the attention head. This is necessary to reshape the output of the head. The input to attention xi and the output from attention ai both have the same dimensionality[1 × d]. We often call d the model dimensionality, and indeed as we’ll discuss in 7.1 • ATTENTION 183

|  |  |
| --- | --- |
|  | 8. 自注意力的输出 a 3 [1 × d]<br>7. 重塑为 [1 x d] WO [d v × d]<br>[1 × d]<br>v<br>6. 对加权后的<br>值向量求和<br>[1 × d] [1 × d] [1 × d]<br>v v v<br>5. 对每个值向量加权 × ×<br>𝛼 𝛼 𝛼<br>3,1 3,2 3,3<br>4. 通过 softmax 转换为 𝛼i,j 权重<br>3. 将标量分数除以 √d ÷ ÷ ÷<br>k √dk √dk √dk<br>2. 将 x3 的查询与<br>x1、x2 和 x3 的键进行比较<br>[1 × d] [1 × d] [1 x d]<br>v v v<br>1. 生成<br>k q v k q v k q v<br>键、查询、值<br>WK WQ WV WK WQ WV WK WQ WV<br>向量<br>x x x<br>1 2 3<br>[1 × d] [1 × d] [1 × d]<br>8. Output of self-attention a 3 [1 × d]<br>7. Reshape to [1 x d] WO [d v × d]<br>[1 × d]<br>v<br>6. Sum the weighted<br>value vectors<br>[1 × d] [1 × d] [1 × d]<br>v v v<br>5. Weigh each value vector × ×<br>𝛼 𝛼 𝛼<br>3,1 3,2 3,3<br>4. Turn into 𝛼i,j weights via softmax<br>3. Divide scalar score by √d ÷ ÷ ÷<br>k √dk √dk √dk<br>2. Compare x3’s query with<br>the keys for x1, x2, and x3<br>[1 × d] [1 × d] [1 x d]<br>v v v<br>1. Generate<br>k q v k q v k q v<br>key, query, value<br>WK WQ WV WK WQ WV WK WQ WV<br>vectors<br>x x x<br>1 2 3<br>[1 × d] [1 × d] [1 × d] |
| 图<br>Fig | 7.5<br>ure 7.5 |
| to-ri |  |

|  | 8. 自注意力的输出 a 3 [1 × d]<br>7. 重塑为 [1 x d] WO [d v × d]<br>[1 × d]<br>v<br>6. 对加权后的<br>值向量求和<br>[1 × d] [1 × d] [1 × d]<br>v v v<br>5. 对每个值向量加权 × ×<br>𝛼 𝛼 𝛼<br>3,1 3,2 3,3<br>4. 通过 softmax 转换为 𝛼i,j 权重<br>3. 将标量分数除以 √d ÷ ÷ ÷<br>k √dk √dk √dk<br>2. 将 x3 的查询与<br>x1、x2 和 x3 的键进行比较<br>[1 × d] [1 × d] [1 x d]<br>v v v<br>1. 生成<br>k q v k q v k q v<br>键、查询、值<br>WK WQ WV WK WQ WV WK WQ WV<br>向量<br>x x x<br>1 2 3<br>[1 × d] [1 × d] [1 × d]<br>8. Output of self-attention a 3 [1 × d]<br>7. Reshape to [1 x d] WO [d v × d]<br>[1 × d]<br>v<br>6. Sum the weighted<br>value vectors<br>[1 × d] [1 × d] [1 × d]<br>v v v<br>5. Weigh each value vector × ×<br>𝛼 𝛼 𝛼<br>3,1 3,2 3,3<br>4. Turn into 𝛼i,j weights via softmax<br>3. Divide scalar score by √d ÷ ÷ ÷<br>k √dk √dk √dk<br>2. Compare x3’s query with<br>the keys for x1, x2, and x3<br>[1 × d] [1 × d] [1 x d]<br>v v v<br>1. Generate<br>k q v k q v k q v<br>key, query, value<br>WK WQ WV WK WQ WV WK WQ WV<br>vectors<br>x x x<br>1 2 3<br>[1 × d] [1 × d] [1 × d] |
| --- | --- |

> a3

> 8. 自注意力的输出
>
> *8. Output of self-attention*

> [1 × d]

> WO [dv × d]

> 7. 重塑为 [1 x d]
>
> *7. Reshape to [1 x d]*

> [1 × dv]

> 6. 对加权后的值向量求和
>
> *6. Sum the weighted value vectors*

> [1 × dv] [1 × dv] [1 × dv]

> 𝛼3,1 𝛼3,2 𝛼3,3

> 5. 对每个值向量加权
>
> *5. Weigh each value vector*

> × ×

> 4. 通过 softmax 转化为 𝛼i,j 权重
>
> *4. Turn into 𝛼i,j weights via softmax*

> ÷ ÷ ÷

> 3. 将标量得分除以 √dk
>
> *3. Divide scalar score by √dk*

> √dk √dk √dk

> 2. 将 x3 的查询与 x1、x2 和 x3 的键进行比较
>
> *2. Compare x3’s query with the keys for x1, x2, and x3*

> [1 × dv] [1 × dv] [1 x dv]

> 1. 生成
>
> *1. Generate*

> k q v k q v k q v

> 键、查询、值
>
> *key, query, value*

> WK WQ WV WK WQ WV WK WQ WV

> 向量
>
> *vectors*

x1 x2 x3

> [1 × d] [1 × d] [1 × d]

> 图 7.5 使用因果（从左到右）自注意力计算 a3 的值，a3 是序列的第三个元素。
>
> *Figure 7.5 Calculating the value of a3, the third element of a sequence using causal (leftto-right) self-attention.*

7.2 节 每个 transformer 块的输出 hi，以及 transformer 块内部的中间向量，也都具有相同的维度 [1×d]。让所有内容都保持相同的维度，使 transformer 非常模块化。

> Section 7.2 the output hi of each transformer block, as well as the intermediate vectors inside the transformer block also have the same dimensionality [1×d]. Having everything be the same dimensionality makes the transformer very modular.

那么让我们来谈谈形状。我们如何从输入处的 [1 × d] 得到

> So let’s talk shapes. How do we get from [1 × d] at the input to [1 × d] at the

输出处的 [1 × d] 呢？让我们看看所有的内部形状。我们为查询向量和键向量设置一个维度 dk。查询向量和键向量都是维度 [1 × dk]，因此我们可以取它们的点积 qi · kj 得到一个标量。我们为值向量设置一个单独的维度 dv。变换矩阵 WQ 的形状为 [d × dk]，WK 为 [d × dk]，WV 为 [d × dv]。因此方程 Eq. 7.13 中 headi 的输出形状为 [1 × dv]。为了得到所需的输出形状 [1 × d]，我们需要重塑 head 的输出，因此 WO 的形状为 [dv ×d]。在最初的 transformer 工作（Vaswani et al., 2017）中，d 为 512，dk 和 dv 都是 64。

> output? Let’s look at all the internal shapes. We’ll have a dimension dk for the query and key vectors. The query vector and the key vector are both dimensionality[1 × dk], so we can take their dot product qi · kj to produce a scalar. We’ll have a separate dimension dv for the value vectors. The transform matrix WQ has shape[d × dk], WK is [d × dk], and WV is [d × dv]. So the output of headi in equation Eq. 7.13 is of shape [1 × dv]. To get the desired output shape [1 × d] we’ll need to reshape the head output, and so WO is of shape [dv ×d]. In the original transformer work (Vaswani et al., 2017), d was 512, dk and dv were both 64.

多头注意力 方程 7.11-7.13 描述了单个注意力头。但实际上，transformer 使用多个注意力头。其直觉是，每个头可能出于不同的目的关注上下文：头可能专门用于表示上下文元素与当前 token 之间不同的语言关系，或者用于在上下文中寻找特定类型的模式。

> Multi-head Attention Equations 7.11-7.13 describe a single attention head. But actually, transformers use multiple attention heads. The intuition is that each head might be attending to the context for different purposes: heads might be specialized to represent different linguistic relationships between context elements and the current token, or to look for particular kinds of patterns in the context.

> 多头
>
> *multi-head*

因此在多头注意力中，我们有 A 个独立的注意力头，它们位于

> So in multi-head attention we have A separate attention heads that reside in

> 注意力
>
> *attention*

模型中相同深度的并行层，每个头都有自己的一组参数，使该头能够对输入之间关系的不同方面进行建模。因此，自注意力层中的每个头 i 都有自己的一组查询、键和值矩阵：WQi、WKi 和 WVi。这些矩阵用于将输入投影为每个头各自的查询、键和值嵌入。

> parallel layers at the same depth in a model, each with its own set of parameters that allows the head to model different aspects of the relationships among inputs. Thus each head i in a self-attention layer has its own set of query, key, and value matrices: WQi, WKi, and WVi. These are used to project the inputs into separate query, key, and value embeddings for each head.

使用多个头时，模型维度 d 仍用于输入

> When using multiple heads the model dimension d is still used for the input

和输出，查询和键嵌入的维度为 dk，值嵌入的维度为 dv（同样，在最初的 transformer 论文中 dk = 184 第 7 章 • TRANSFORMERS 与预训练 dv = 64，A = 8，d = 512）。因此对于每个头 i，我们有形状为 [d ×dk] 的权重层 WQi、形状为 [d ×dk] 的 WKi，以及形状为 [d ×dv] 的 WVi。

> and output, the query and key embeddings have dimensionality dk, and the value embeddings are of dimensionality dv (again, in the original transformer paper dk = 184 CHAPTER 7 • TRANSFORMERS AND PRETRAINING dv = 64, A = 8, and d = 512). Thus for each head i, we have weight layers WQi of shape [d ×dk], WKi of shape [d ×dk], and WVi of shape [d ×dv].

下面是用多个头增强的注意力方程；图 7.6

> Below are the equations for attention augmented with multiple heads; Fig. 7.6

展示了一种直觉。

> shows an intuition.

qc i = xiWQc; kc j = x jWKc; vc j = xjWVc; ∀c 1 ≤c ≤A

> (7.15)

qc i ·kc

> j

scorec(xi,x j) =

> (7.16)

√dk

αc ij = softmax(scorec(xi,x j)) ∀j ≤i

> (7.17)

headc X αc ijvc

> (7.18)

i =

> j

> j≤i

ai = (head1 ⊕head2...⊕headA)WO (7.19)

MultiHeadAttention(xi,[x1,··· ,xi−1]) = ai

> (7.20)

注意，式 7.20 中的 MultiHeadAttention 是当前输入 xi 以及所有其他输入的函数。对于本章所使用的因果（causal）注意力或从左到右的注意力，其他输入只位于左侧；但在第 9 章我们还会看到一种注意力版本，其中注意力同时也是右侧词元的函数。

> Note in Eq. 7.20 that MultiHeadAttention is a function of the current input xi, as well as all the other inputs. For the causal or left-to-right attention that we use in this chapter, the other inputs are only to the left, but we’ll also see a version of attention in Chapter 9 where attention is a function of the tokens to the right as well.

当我们在式 7.35 中引入掩蔽右侧上下文这一概念时，会再回到关于因果输入的这一想法。

> We’ll return to this idea about causal inputs in Eq. 7.35 when we introduce the idea of masking the right context.

这 A 个头中每一个的输出形状都是 [1 × dv]，因此

> The output of each of the A heads is of shape [1 × dv], and so the output of the

具有 A 个头的多头层由 A 个形状为 [1 × dv] 的向量组成。这些向量被拼接起来，产生一个维度为 [1 × Adv] 的单一输出。随后我们再用一个线性投影 WO ∈RAdv×d 对其重新塑形，从而在每个输入 i 处得到输出形状正确为 [1 × d] 的多头注意力向量 ai。各头的维度 dv 取为 dv = d/A，这意味着多头注意力在参数开销上与单头注意力大致相同。

> multi-head layer with A heads consists of A vectors of shape [1 × dv]. These are concatenated to produce a single output with dimensionality [1 × Adv]. Then we use yet another linear projection WO ∈RAdv×d to reshape it, resulting in the multihead attention vector ai with the correct output shape [1 × d] at each input i. The dimensionality dv of the heads is set so that dv = d/A, which means that multihead attention costs about the same in parameters as having a single head.

## 7.2 Transformer 块

> 7.2 Transformer Blocks

自注意力计算是所谓 transformer 块（transformer block）的核心；除自注意力层之外，transformer 块还包括另外三类层：（1）前馈层，（2）残差连接，（3）归一化层（俗称“层归一化”）。

> The self-attention calculation lies at the core of what’s called a transformer block, which, in addition to the self-attention layer, includes three other kinds of layers: (1) a feedforward layer, (2) residual connections, and (3) normalizing layers (colloquially called “layer norm”).

图 7.7 展示了一个 transformer 块，勾勒出一种常见的思考方式，

> Fig. 7.7 illustrates a transformer block, sketching a common way of thinking

即把该块视为残差流（residual stream）的方式（Elhage et al., 2021）。在残差流的视角下，我们把单个词元 i 通过 transformer 块的处理看作词元位置 i 上的一条 d 维表示的单一数据流。这条残差流以原始输入向量为起点，各个组件从残差流中读取自己的输入，再把输出加回到该流中。

> about the block that is called the residual stream (Elhage et al., 2021). In the residual stream viewpoint, we consider the processing of an individual token i through the transformer block as a single stream of d-dimensional representations for token position i. This residual stream starts with the original input vector, and the various components read their input from the residual stream and add their output back into the stream.

> 残差流
>
> *residual stream*

位于该流底部的输入是某个词元的嵌入，其

> The input at the bottom of the stream is an embedding for a token, which has

维度为 d。这个初始嵌入（通过残差连接）向上传递，并由 transformer 的其他组件逐步累加其上：我们已经见过的注意力层，以及我们即将介绍的前馈层。

> dimensionality d. This initial embedding gets passed up (by residual connections), and is progressively added to by the other components of the transformer: the attention layer that we have seen, and the feedforward layer that we will introduce.

在注意力层和前馈层之前，是一个称为层归一化（layer norm）的计算。

> Before the attention and feedforward layer is a computation called the layer norm.

因此，初始向量先经过层归一化和注意力层，

> Thus the initial vector is passed through a layer norm and attention layer, and

其结果被加回到该流中，在这里是加到原始输入向量上 7.2 • TRANSFORMER 块 185

> the result is added back into the stream, in this case to the original input vector 7.2 • TRANSFORMER BLOCKS 185

| a<br>i<br>[1 x d]<br>[Ad x d]<br>v<br>WO<br>投影到最终表示<br>通常 d =d/A，因此为 [d x d]<br>v<br>拼接输出 [1 x Ad ] 此处 A=4<br>v<br>[1 x d ] [1 x d ] [1 x d ] [1 x d ]<br>每个头 v v v v<br>头 1 头 2 头 3 头 4<br>以不同方式<br>关注上下文 WK1WV1 WQ1 WK2WV2WQ2 WK3WV3W WKQ43 WK4WV4WQ4<br>… x x x x<br>i-3 i-2 i-1 i<br>[1 x d]<br>a<br>i<br>[1 x d]<br>[Ad x d]<br>v<br>WO<br>Project to final representation<br>usually d =d/A, hence [d x d]<br>v<br>Concatenate Outputs [1 x Ad ] here A=4<br>v<br>[1 x d ] [1 x d ] [1 x d ] [1 x d ]<br>Each head v v v v<br>Head 1 Head 2 Head 3 Head 4<br>attends differently<br>to context WK1WV1 WQ1 WK2WV2WQ2 WK3WV3W WKQ43 WK4WV4WQ4<br>… x x x x<br>i-3 i-2 i-1 i<br>[1 x d] |  |
| --- | --- |
| 图 7.6<br>Figure 7.6 | 针对输入 x i 的多头注意力计算，产生输出 a i。一个多头注意力<br>The multi-head attention computation for input x i, producing output a i. A multi-head attention |

### ai

> [1 x d]

|  |  |  |  |
| --- | --- | --- | --- |
| WO |  |  |  |
|  |  |  |  |

> [Adv x d]

> 投影到最终表示
>
> *Project to ﬁnal representation*

> 通常 dv=d/A，因此为 [d x d]
>
> *usually dv=d/A, hence [d x d]*

> 拼接输出
>
> *Concatenate Outputs*

> [1 x Adv ] 此处 A=4
>
> *[1 x Adv ] here A=4*

> [1 x dv ] [1 x dv ] [1 x dv ] [1 x dv ]

> 每个头
>
> *Each head*

> 以不同方式关注 头 1 头 2 头 3 头 4
>
> *attends diﬀerently Head 1 Head 2 Head 3 Head 4*

> 关注上下文 WK1 WV1 WQ1 WK2 WV2WQ2 WK3 WV3 WQ3 WK4 WK4 WV4WQ4
>
> *to context WK1 WV1 WQ1 WK2 WV2WQ2 WK3 WV3 WQ3 WK4 WK4 WV4WQ4*

### xi …

xi-3 xi-2 xi-1

> [1 x d]

> 图 7.6 对输入 xi 的多头注意力计算，产生输出 ai。一个多头注意力层有 A 个头，每个头都有自己的查询、键和值权重矩阵。在此图中，我们展示 A = 4，比通常使用的值小，只是为了能放在页面上。每个头的输出形状为 [1×dv]，它们被拼接起来，然后由 WO 矩阵投影到另一个空间。通常头部的维度 dv 被设定为 dv = d/A，其结果是 WO 是一个形状为 [Adv ×d] = [d ×d] 的方阵。
>
> *Figure 7.6 The multi-head attention computation for input xi, producing output ai. A multi-head attention layer has A heads, each with its own query, key, and value weight matrices. In this figure, we show A = 4, a smaller value than is usually used, just to fit on the page. The outputs from each of the heads are of shape [1×dv] and are concatenated and then projected into a different space by the WO matrix. Usually the dimensionality dv of the heads is set so that dv = d/A, with the result that WO is a square matrix of shape [Adv ×d] = [d ×d].*

> 结果被投影到 d，产生的输出与输入大小相同。
>
> *The result is projected to d, producing an output of the same size as the input.*

| h h h<br>i-2 i-1 i<br>+<br>前馈<br>层归一化<br>… +<br>多头<br>注意力<br>层归一化<br>x x x<br>i-2 i-1 i<br>h h h<br>i-2 i-1 i<br>+<br>Feedforward<br>Layer Norm<br>… +<br>MultiHead<br>Attention<br>Layer Norm<br>x x x<br>i-2 i-1 i |  |
| --- | --- |
| 图 7.7<br>Figure 7.7 | 一个 transformer 块的架构，展示残差流，展示<br>The architecture of a transformer block showing the residual stream, showing |

> hi-2 hi-1 hi

![](images/img_249.png)

![](images/img_247.png)

![](images/img_245.png)

+

> 前馈
>
> *Feedforward*

> 层归一化
>
> *Layer Norm*

+

…

> 多头注意力
>
> *MultiHead Attention*

> 层归一化
>
> *Layer Norm*

> xi-2 xi-1 xi

> 大多数信息如何沿着残差流向上流动，并且只有注意力模块对来自先前 token 位置上其他流的信息敏感。在此图中以及全章中，我们使用该架构的 prenorm（前置归一化）版本，其中层归一化发生在注意力和前馈层之前，而不是之后。
>
> *how most information flows up through the residual stream, and only the attention module is sensitive to information from other streams at prior token positions. In this figure and throughout the chapter, we use the prenorm version of the architecture, in which the layer norms happen before the attention and feedforward layers rather than after.*

xi。然后这个求和后的向量再次经过另一个层归一化和一个前馈层，它们的输出被加回残差中，我们将用 hi 指代 token i 经过 transformer 块后得到的输出。

> xi. And then this summed vector is again passed through another layer norm and a feedforward layer, and the output of those is added back into the residual, and we’ll use hi to refer to the resulting output of the transformer block for token i.

我们已经见过注意力层，所以现在在处理 token 位置 i 上的单个输入 xi 的语境中，介绍前馈 186 第 7 章 • TRANSFORMERS 与预训练 以及层归一化的计算。

> We’ve already seen the attention layer, so let’s now introduce the feedforward 186 CHAPTER 7 • TRANSFORMERS AND PRETRAINING and layer norm computations in the context of processing a single input xi at token position i.

### 7.2.1 前馈层

> 7.2.1 Feedforward layer

前馈层是一个全连接的 2 层网络，即一个隐藏层、两个权重矩阵（第 6 章）。

> The feedforward layer is a fully-connected 2-layer network, i.e., one hidden layer, two weight matrices (Chapter 6).

前馈层是逐位置的，这意味着它作用于每个 token

> The feedforward layer is position-wise, meaning that it operates on each token

位置 i 上是独立的。这与注意力网络形成对比，注意力网络的职责是混合来自不同 token 位置的信息。前馈权重在各位置之间共享，这意味着相同的参数被应用于每个 token 位置，但层与层之间是不同的。

> position i independently. This makes a contrast with the attention network, whose job is to mix information from different token positions. The feedforward weights are shared across positions, meaning that the same parameters are applied to every token position, but are different from layer to layer.

通常会让前馈网络隐藏层的维度 dff 比模型维度 d 大 4 倍。（例如在最初的 transformer 模型中，d = 512，dff = 2048。）这意味着前馈网络拥有 transformer 的大部分参数，而这些前馈网络参数似乎编码了 transformer 中的大部分事实性知识。（Geva et al., 2021; Meng et al., 2022）。

> It is common to make the dimensionality dff of the hidden layer of the feedforward network be 4 times larger than the model dimensionality d. (For example in the original transformer model, d = 512 and dff = 2048.) This means the feedforward networks have most of the parameters of the transformers, and these feedforward network parameters seem to encode most of the factual knowledge in the transformer. (Geva et al., 2021; Meng et al., 2022).

> 门控
>
> *gated*

现在大多数 LLM 实际上都在使用门控前馈层，采用的是名为 SwiGLU（Shazeer, 2020）的激活函数，它的效果比 ReLU 之类的更简单函数更好。SwiGLU 属于门控线性单元（Gated Linear Unit, GLU）函数家族（Dauphin et al., 2017），这类函数对输入的两种线性变换做逐分量乘积（⊗）。其思想是，其中一个函数是值，另一个是门，门指定有多少该值能够通过。SwiGLU 使用 Swish 函数（Ramachandran et al., 2017）作为门：

> Most LLMs now actually use gated feedforward layers, by employing an activation function called SwiGLU (Shazeer, 2020) that works better than simpler functions like ReLU. SwiGLU is in the family of Gated Linear Unit (GLU) functions(Dauphin et al., 2017), which do a component-wise product (⊗) of two linear transformations of the input. The idea is that one of the functions is a value, and the other is a gate that specifies how much of that value goes through. SwiGLU uses the Swish function (Ramachandran et al., 2017) as the gate:

> 前馈
>
> *feedforward*

> 层
>
> *layers*

Swishβ(x) = xσ(βx)

> (7.21)

那么 SwiGLU 前馈方程为：

> The SwiGLU feedforward equation is then:

  

FFNSwiGLU(x,W1,W2,W3,b1,b2,b3,β) = Swishβ(xW1 +b1)⊗(xW2 +b2) W3 +b3 (7.22)

由于门控激活函数为门控额外增加了参数，门控模型的维度 dff 通常被设定为略小于通常的 4d。

> Because gated activation functions have extra parameters for the gating, the dimensionality dff of gated models is usually set to be slightly less than the normal 4d.

### 7.2.2 层归一化

> 7.2.2 Layer Norm

在 transformer 块中有两个阶段，我们对向量做归一化（Ba et al., 2016）。

> At two stages in the transformer block we normalize the vector (Ba et al., 2016).

这个过程称为层归一化（layer norm，layer normalization 的简称），它是众多

> This process, called layer norm (short for layer normalization), is one of many

> 层归一化
>
> *layer norm*

归一化形式之一，通过把隐藏层的值保持在一个有利于基于梯度的训练的范围，可用于提升深度神经网络的训练性能。

> forms of normalization that can be used to improve training performance in deep neural networks by keeping the values of a hidden layer in a range that facilitates gradient-based training.

层归一化是统计学中 z-score 的一种变体，应用于隐藏层中的单个向量。也就是说，层归一化这个术语有点令人困惑；层归一化并不应用于整个 transformer 层，而只应用于单个 token 的嵌入向量。因此层归一化的输入是一个维度为 d 的单个向量，输出是归一化后的该向量，维度同样为 d。层归一化的第一步是计算待归一化向量各元素的均值 µ 和标准差 σ。给定一个维度为 d 的嵌入 7.2 • TRANSFORMER 块 187 向量 x，这些值计算如下。

> Layer norm is a variation of the z-score from statistics, applied to a single vector in a hidden layer. That is, the term layer norm is a bit confusing; layer norm is not applied to an entire transformer layer, but just to the embedding vector of a single token. Thus the input to layer norm is a single vector of dimensionality d and the output is that vector normalized, again of dimensionality d. The first step in layer normalization is to calculate the mean, µ, and standard deviation, σ, over the elements of the vector to be normalized. Given an embedding vector x of dimen- 7.2 • TRANSFORMER BLOCKS 187 sionality d, these values are calculated as follows.

> d

µ = 1 X

x[j]

> (7.23)

d

> j=1

v u

> d

u t1 X

(x[j]−µ)2

> (7.24)

σ = d

> j=1

给定这些值，向量各分量通过各自减去均值并除以标准差来完成归一化。该计算的结果是一个均值为零、标准差为一的新向量。

> Given these values, the vector components are normalized by subtracting the mean from each and dividing by the standard deviation. The result of this computation is a new vector with zero mean and a standard deviation of one.

ˆx = (x−µ)

> (7.25)

σ

最后，在层归一化的标准实现中，引入了两个可学习参数 γ 和 β，分别表示增益值与偏移值。

> Finally, in the standard implementation of layer normalization, two learnable parameters, γ and β, representing gain and offset values, are introduced.

LayerNorm(x) = γ (x−µ)

> (7.26)

+β

σ

在实践中，许多现代网络使用一种更简单的归一化，称为 RMSNorm（Zhang

> In practice, many modern networks use a simpler norm, called RMSNorm (Zhang

> RMSNorm

与 Sennrich，2019），它通过除以均方根统计量来重新缩放向量，但跳过了均值中心化步骤。

> and Sennrich, 2019), which rescales the vectors by dividing by the root-mean-square statistic, but skips the mean-centering step.

### 7.2.3 整合起来

> 7.2.3 Putting it all together

transformer 块所计算的函数可以这样表达：将其分解为每个组件计算对应一个方程，用 t（形状为 [1 × d]）表示 transformer，并用上标标示块内的每一次计算：

> The function computed by a transformer block can be expressed by breaking it down with one equation for each component computation, using t (of shape [1 × d]) to stand for transformer and superscripts to demarcate each computation inside the block:

t1 = LayerNorm(xi)

> (7.27)

> i

 

t2 = MultiHeadAttention(t1 t1 1,··· ,t1

> (7.28)

i , )

> i i−1

t3 = t2

> (7.29)

i +xi

> i

t4 = LayerNorm(t3

> (7.30)

i )

> i

t5 = FFN(t4

> (7.31)

i )

> i

hi = t5 i +t3

> (7.32)

> i

注意，唯一会从其他词元（其他残差流）接收信息作为输入的组件是多头注意力，正如我们从式 7.28 中看到的，它会关注上下文中所有相邻的词元。不过，注意力的输出随后会被加进当前词元的嵌入流。事实上，Elhage et al. (2021) 表明，我们可以把注意力头看作是把信息从相邻词元的残差流真正搬运到当前流中。因此，每个位置的高维嵌入空间既包含当前词元的信息，也包含相邻词元的信息，只不过它们位于向量空间的不同子空间中。

> Notice that the only component that takes as input information from other tokens(other residual streams) is multi-head attention, which (as we see from Eq. 7.28) looks at all the neighboring tokens in the context. The output from attention, however, is then added into this token’s embedding stream. In fact, Elhage et al. (2021) show that we can view attention heads as literally moving information from the residual stream of a neighboring token into the current stream. The high-dimensional embedding space at each position thus contains information about the current token and about neighboring tokens, albeit in different subspaces of the vector space.

图 7.8 展示了这种搬运的可视化。因此我们称注意力函数为该架构的词元混合（token-mixing）组件，因为它把信息

> Fig. 7.8 shows a visualization of this movement. We therefore call the attention function the token-mixing component of the architecture, because it mixes information

> 词元混合
>
> *token-mixing*

从相邻词元的流混合进当前流。

> from neighboring token streams into the current stream.

关键在于，Transformer 块的输入维度与输出维度是相互匹配的，因此

> Crucially, the input and output dimensions of transformer blocks are matched so

它们才能被堆叠起来。块输入端的每个词元向量 xi 的维度为 188 第 7 章 • TRANSFORMERS 与预训练

> they can be stacked. Each token vector xi at the input to the block has dimensionality 188 CHAPTER 7 • TRANSFORMERS AND PRETRAINING

| 词元 A 词元 B<br>残差流 残差流<br>Token A Token B<br>residual residual<br>stream stream |  |
| --- | --- |
| 图 7.8<br>Figure 7.8 | 一个注意力头可以把信息从词元 A 的残差流搬运到<br>An attention head can move information from token A’s residual stream into |

> 词元 A 词元 B 残差流 残差流
>
> *Token A Token B residual residual stream stream*

> 词元 B 的残差流。
>
> *token B’s residual stream.*

维度 d，而输出 hi 的维度同样为 d。用于大型语言模型的 Transformer 会堆叠许多这样的块，从 12 层（用于 T5 或 GPT-3-small 语言模型）到 96 层（用于 GPT-3 175B），再到更近期的模型所用的更多层数。稍后我们会回到堆叠这个问题。

> d, and the output hi also has dimensionality d. Transformers for large language models stack many of these blocks, from 12 layers (used for the T5 or GPT-3-small language models) to 96 layers (used for GPT-3 175B), to even more for more recent models. We’ll come back to this issue of stacking in a bit.

式 7.27 及其后续公式只是单个 Transformer 块的公式，

> Equation 7.27 and following are just the equation for a single transformer block,

但在一个 12 层的 Transformer 中，残差流的比喻贯穿所有 Transformer 层，从最初的几个块直到第 12 个块。在较靠前的 Transformer 块中，残差流表示的是当前词元。在最高的几个 Transformer 块中，残差流表示的通常是后一个词元，因为在最末端它被训练来预测下一个词元。

> but the residual stream metaphor goes through all the transformer layers, from the first transformer blocks to the 12th, in a 12-layer transformer. At the earlier transformer blocks, the residual stream is representing the current token. At the highest transformer blocks, the residual stream is usually representing the following token, since at the very end it’s being trained to predict the next token.

一旦堆叠许多块，就还有一个额外要求：在最末尾

> Once we stack many blocks, there is one more requirement: at the very end of

也就是最后一个（最高层）Transformer 块之后，要对每个词元流的最后一个 hi 额外单独运行一次层归一化（它就在我们稍后将定义的语言模型头层下面）。2

> the last (highest) transformer block, there is a single extra layer norm that is run on the last hi of each token stream (just below the language model head layer that we will define soon). 2

## 7.3 使用单个矩阵 X 并行化计算

> 7.3 Parallelizing computation using a single matrix X

以上对多头注意力以及 Transformer 块其余部分的描述，是从单个残差流中、在单个时间步 i 上计算单个输出的视角出发的。但正如我们之前指出的，为计算 ai 而对每个词元所做的注意力计算，与对其他每个词元的计算相互独立；对于 Transformer 块中由输入 xi 计算 hi 的全部计算，这一点同样成立。这意味着我们可以利用高效的矩阵乘法例程，轻松地把整个计算并行化。

> This description of multi-head attention and the rest of the transformer block has been from the perspective of computing a single output at a single time step i in a single residual stream. But as we pointed out earlier, the attention computation performed for each token to compute ai is independent of the computation for each other token, and that’s also true for all the computation in the transformer block computing hi from the input xi. That means we can easily parallelize the entire computation, taking advantage of efficient matrix multiplication routines.

我们的做法是把输入序列中 N 个词元的输入嵌入打包为一个大小为 [N × d] 的单个矩阵 X。X 的每一行是输入中一个词元的嵌入。用于大型语言模型的 Transformer 输入长度 N 可达数十万个词元，而借助我们在此不讨论的长上下文机制还能达到数百万个词元。因此对于普通 Transformer，可以认为 X 有数十万行，每一行的维度都是嵌入维度 d（模型维度）。

> We do this by packing the input embeddings for the N tokens of the input sequence into a single matrix X of size [N × d]. Each row of X is the embedding of one token of the input. Transformers for large language models can have an input length N of hundreds of thousands of tokens, and millions of tokens can be achieved with long-context mechanisms that we don’t discuss here. So for vanilla transformers, we can think of X having hundreds of thousands of rows, each of the dimensionality of the embedding d (the model dimension).

> 这是最常见的 Transformer 架构，即 prenorm 架构。最初的
>
> *This is the most common transformer architecture, the prenorm architecture. The original definition*

> 2

> Transformer 定义出自 Vaswani et al. (2017)，那里采用的是另一种架构，即 postnorm transformer，其中层归一化发生在注意力和 FFN 层之后；把层归一化提前效果更好，但确实需要在末尾多加这一层。
>
> *of the transformer in Vaswani et al. (2017) used an alternative architecture, the postnorm transformer, in which the layer norm happens after the attention and FFN layers; having the layer norm beforehand works better, but does require this one extra layer at the end.*

7.3 • 使用单个矩阵 X 并行化计算 189

> 7.3 • PARALLELIZING COMPUTATION USING A SINGLE MATRIX X 189

并行化注意力　我们先看单个注意力头的情况，然后转向多头，再补上 Transformer 块中的其余组件。对单个头，我们用查询矩阵 WQ（形状 [d × dk]）、键矩阵 WK（形状 [d × dk]）和值矩阵 WV（形状 [d × dv]）乘以 X，得到形状为 [N × dk] 的矩阵 Q、形状为 [N × dk] 的 K 以及形状为 [N × dv] 的 V，其中包含所有的键、查询和值向量：

> Parallelizing attention Let’s first see this for a single attention head and then turn to multiple heads, and then add in the rest of the components in the transformer block. For one head we multiply X by the query, key, and value matrices WQ of shape [d ×dk], WK of shape [d ×dk], and WV of shape [d ×dv], to produce matrices Q of shape [N ×dk], K of shape [N ×dk], and V of shape [N ×dv], containing all the key, query, and value vectors:

Q = XWQ; K = XWK; V = XWV

> (7.33)

有了这些矩阵，我们只需做一次矩阵乘法，把 Q 与 K⊺ 相乘，就能同时计算出所有需要的查询–键比较。乘积的形状为 N × N，其可视化见图 7.9。

> Given these matrices we can compute all the requisite query-key comparisons simultaneously by multiplying Q and K⊺in a single matrix multiplication. The product is of shape N ×N, visualized in Fig. 7.9.

| q1•k1 q1•k2 q1•k3 q1•k4<br>q2•k1 q2•k2 q2•k3 q2•k4<br>N<br>q3•k1 q3•k2 q3•k3 q3•k4<br>q4•k1 q4•k2 q4•k3 q4•k4<br>N |  |
| --- | --- |
| 图 7.9<br>Figure 7.9 | ⊺<br>N × N 的 QK 矩阵，展示它如何把所有的 qi · kj 比较放在一次<br>⊺<br>The N × N QK matrix showing how it computes all qi · kj comparisons in a |

| q1•k1 q1•k2 q1•k3 q1•k4<br>q2•k1 q2•k2 q2•k3 q2•k4<br>N<br>q3•k1 q3•k2 q3•k3 q3•k4<br>q4•k1 q4•k2 q4•k3 q4•k4<br>N | q1•k1 | q1•k2 | q1•k3 | q1•k4 |
| --- | --- | --- | --- | --- |
|  | q2•k1 | q2•k2 | q2•k3 | q2•k4 |
|  | q3•k1 | q3•k2 | q3•k3 | q3•k4 |
|  | q4•k1 | q4•k2 | q4•k3 | q4•k4 |

> N

> N

> 图 7.9　N × N 的 QK⊺ 矩阵，展示它如何在一次矩阵乘法中计算所有 qi · kj 比较。
>
> *Figure 7.9 The N × N QK⊺matrix showing how it computes all qi · kj comparisons in a single matrix multiple.*

一旦得到这个 QK⊺ 矩阵，我们就能非常高效地对这些分数做缩放、取

> Once we have this QK⊺matrix, we can very efficiently scale these scores, take

softmax，然后把结果乘以 V，得到一个形状为 N × d 的矩阵：输入中每个词元的向量嵌入表示。这样一来，我们就把单个头对整个 N 个词元序列的整个自注意力步骤化简为如下计算：

> the softmax, and then multiply the result by V resulting in a matrix of shape N ×d: a vector embedding representation for each token in the input. We’ve reduced the entire self-attention step for an entire sequence of N tokens for one head to the following computation:

 QK⊺ 

head = softmax mask

> (7.34)

√dk V

A = head WO

> (7.35)

屏蔽未来　你可能已经注意到，我们在上面的式 7.34 中引入了一个 mask（掩码）函数。这是因为按我们上述的方式计算自注意力存在一个问题：QK⊺ 的计算会为每个查询值与每一个键值之间产生一个分数，其中也包括位于该查询之后的键值。这在语言建模的设定下是不合适的：如果你已经知道下一个词是什么，猜出它就太简单了！为解决这个问题，矩阵上三角部分的元素被设为 −∞，softmax 会将其变为零，从而消除对序列中后续词语的任何了解。在实践中，这是通过加入一个掩码矩阵 M 来实现的，其中当 j > i 时（即位于上三角部分）Mij = −∞，其余情况下 Mij = 0。

> Masking out the future You may have noticed that we introduced a mask function in Eq. 7.34 above. This is because the self-attention computation as we’ve described it has a problem: the calculation of QK⊺results in a score for each query value to every key value, including those that follow the query. This is inappropriate in the setting of language modeling: guessing the next word is pretty simple if you already know it! To fix this, the elements in the upper-triangular portion of the matrix are set to −∞, which the softmax will turn to zero, thus eliminating any knowledge of words that follow in the sequence. This is done in practice by adding a mask matrix M in which Mi j = −∞∀j > i (i.e. for the upper-triangular portion) and Mij = 0 otherwise.

图 7.10 展示了由此得到的、经过掩码的 QK⊺ 矩阵。正如我们将在 7.7 节中看到的，正是掩码的使用使得窗口中的每个位置都能充当一个训练样本，从而使 transformer 的训练非常高效。我们将在第 9 章看到如何调整掩码，以便在需要时利用未来的词。

> Fig. 7.10 shows the resulting masked QK⊺matrix. As we’ll see in Section 7.7, the use of the mask is what lets every position in the window serve as a training example, making the transformer very efficient to train. And we’ll see in Chapter 9 how to adjust the mask to make use of words in the future for tasks that need it.

图 7.11 展示了单个注意力头全部计算过程的示意图

> Fig. 7.11 shows a schematic of all the computations for a single attention head

以矩阵形式并行化。

> parallelized in matrix form.

图 7.9 和图 7.10 也清楚地表明，注意力在输入长度上

> Fig. 7.9 and Fig. 7.10 also make it clear that attention is quadratic in the length

呈二次方复杂度，因为在每一层我们都需要计算每一对之间的点积 190 第 7 章 • Transformer 与预训练

> of the input, since at each layer we need to compute dot products between each pair 190 CHAPTER 7 • TRANSFORMERS AND PRETRAINING

| q1•k1 −∞ −∞ −∞<br>q2•k1 q2•k2 −∞ −∞<br>N<br>q3•k1 q3•k2 q3•k3 −∞<br>q4•k1 q4•k2 q4•k3 q4•k4<br>N |  |
| --- | --- |
| 图 7.10<br>Figure 7.10 | ⊺<br>N × N 的 QK 矩阵，展示了 qi · k j 值，其中上三角<br>⊺<br>The N × N QK matrix showing the qi · k j values, with the upper-triangle |

| q1•k1 −∞ −∞ −∞<br>q2•k1 q2•k2 −∞ −∞<br>N<br>q3•k1 q3•k2 q3•k3 −∞<br>q4•k1 q4•k2 q4•k3 q4•k4<br>N |  | −∞ | −∞ | −∞ |
| --- | --- | --- | --- | --- |
|  | 1•k1 |  |  |  |
|  |  |  |  |  |
|  |  |  | −∞ | −∞ |
|  | 2•k1 | q2•k2 |  |  |
|  |  |  |  |  |
|  |  |  |  | −∞ |
|  | 3•k1 | q3•k2 | q3•k3 |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 4•k1 | q4•k2 | q4•k3 | q4•k4 |
|  |  |  |  |  |

> q2•k1 q2•k2

> N

> q3•k1 q3•k2 q3•k3

> q4•k1 q4•k2 q4•k3 q4•k4

> N

> 图 7.10　N × N 的 QK⊺ 矩阵，展示了 qi · k j 值，其中比较矩阵的上三角部分被置零（设为 −∞，softmax 会将其变为零）。
>
> *Figure 7.10 The N × N QK⊺matrix showing the qi · k j values, with the upper-triangle portion of the comparisons matrix zeroed out (set to −∞, which the softmax will turn to zero).*

| X Q X K X V<br>ToIn kp eu nt WQ TQ oku ee nry ToIn kp eu nt WK ToK kee ny ToIn kp eu nt WV ToV ka elu ne<br>1 1 1 1 1 1<br>输入查询 输入键 输入值<br>Token 2 x = Token 2 Token 2 x = Token 2 Token 2 x = Token 2<br>输入查询 输入键 输入值<br>Token 3 Token 3 Token 3 Token 3 Token 3 Token 3<br>输入查询 输入键 输入值<br>Token 4 d x d Token 4 Token 4 d x d k Token 4 Token 4 d x d v Token 4<br>k<br>N x d N x d k N x d N x d k N x d N x d v<br>T<br>Q K QKT QKT masked V A<br>q1 x = q1•k1q1•k2q1•k3q1•k4 qq11••kk11 −∞ −∞ −∞ v1 a1 k1 k2 k3 k4<br>mask q2 q2•k1 q2•k2q2•k3q2•k4 = q2•k1q2•k2 −∞ −∞ x v2 = a2<br>q3 q3•k1 q3•k2 q3•k3q3•k4 q3•k1q3•k2 q3•k3 −∞ v3 a3<br>q4 d k x N q4•k1 q4•k2 q4•k3 q4•k4 q4•k1q4•k2 q4•k3 q4•k4 v4 a4<br>N x d k N x N N x N N x d v N x d v<br>X Q X K X V<br>ToIn kp eu nt WQ TQ oku ee nry ToIn kp eu nt WK ToK kee ny ToIn kp eu nt WV ToV ka elu ne<br>1 1 1 1 1 1<br>Input Query Input Key Input Value<br>Token 2 x = Token 2 Token 2 x = Token 2 Token 2 x = Token 2<br>Input Query Input Key Input Value<br>Token 3 Token 3 Token 3 Token 3 Token 3 Token 3<br>Input Query Input Key Input Value<br>Token 4 d x d Token 4 Token 4 d x d k Token 4 Token 4 d x d v Token 4<br>k<br>N x d N x d k N x d N x d k N x d N x d v<br>T<br>Q K QKT QKT masked V A<br>q1 x = q1•k1q1•k2q1•k3q1•k4 qq11••kk11 −∞ −∞ −∞ v1 a1 k1 k2 k3 k4<br>mask q2 q2•k1 q2•k2q2•k3q2•k4 = q2•k1q2•k2 −∞ −∞ x v2 = a2<br>q3 q3•k1 q3•k2 q3•k3q3•k4 q3•k1q3•k2 q3•k3 −∞ v3 a3<br>q4 d k x N q4•k1 q4•k2 q4•k3 q4•k4 q4•k1q4•k2 q4•k3 q4•k4 v4 a4<br>N x d k N x N N x N N x d v N x d v |  |
| --- | --- |
| 图 7.11<br>Figure 7.11 | 单个注意力头并行注意力计算的示意图。第一行展示了<br>Schematic of the attention computation for a single attention head in parallel. The first row shows |

> X Q X K X V

> WK WV

> WQ

> 输入查询 输入键 输入值 Token 1 Token 1 Token 1 Token 1 Token 1 Token 1 输入查询 输入键 输入值 Token 2 Token 2 Token 2 Token 2
>
> *Input Query Input Key Input Value Token 1 Token 1 Token 1 Token 1 Token 1 Token 1 Input Query Input Key Input Value Token 2 Token 2 Token 2 Token 2*

> =

> Token 2

> x

> Token 2

> x = x =

> 输入查询 输入键 输入值 Token 3 Token 3 Token 3 Token 3 Token 3 Token 3 输入查询 输入键 输入值 Token 4 Token 4 Token 4 Token 4
>
> *Input Query Input Key Input Value Token 3 Token 3 Token 3 Token 3 Token 3 Token 3 Input Query Input Key Input Value Token 4 Token 4 Token 4 Token 4*

> d x dk d x dv

> Token 4 Token 4

> d x dk

> N x d N x dk

> N x dk N x d N x d N x dv

> KT QKT

> Q QKT masked V A

| k1 | k2 |  | k3 | k4 |
| --- | --- | --- | --- | --- |

|  |  |  |  |
| --- | --- | --- | --- |
| q1•k1 | q1•k2 | q1•k3 | q1•k4 |
| q2•k1 | q2•k2 | q2•k3 | q2•k4 |
|  |  |  |  |
| q3•k1 | q3•k2 | q3•k3 | q3•k4 |
|  |  |  |  |
| q4•k1 | q4•k2 | q4•k3 | q4•k4 |

|  | −∞ | −∞ | −∞ |
| --- | --- | --- | --- |
| qq11••kk11 |  |  |  |
| q2•k1 | q2•k2 | −∞ | −∞ |
|  |  |  | −∞ |
| q3•k1 | q3•k2 | q3•k3 |  |
|  |  |  |  |
| q4•k1 | q4•k2 | q4•k3 | q4•k4 |

> x

> q1

> =

> k1 k2 k3 k4 q1•k1 q1•k2 q1•k3 q1•k4 q1•k1 q1•k1 q1•k1 v1 a1

> 掩码 x =
>
> *mask x =*

> q2

> =

> q2•k1 q2•k2 q2•k3 q2•k4 q2•k1 q2•k2 v2 a2

> q3

> q3•k1 q3•k2 q3•k3 q3•k4 q3•k1 q3•k2 q3•k3 v3 a3

> dk x N

> q4 q4•k1 q4•k2 q4•k3 q4•k4 q4•k1 q4•k2 q4•k3 q4•k4 v4 a4

> N x dk N x N N x dv N x dv

> N x N

> Q、K 和 V 矩阵的计算。第二行展示了 QKT 的计算、掩码（softmax 计算和按维度归一化未显示），以及随后对值向量进行加权求和以得到最终的注意力向量。
>
> *the computation of the Q, K, and V matrices. The second row shows the computation of QKT, the masking(the softmax computation and the normalizing by dimensionality are not shown) and then the weighted sum of the value vectors to get the final attention vectors.*

输入中词元的数量。这使得在非常长的文档（例如整部小说）上计算注意力变得代价高昂。尽管如此，现代大型语言模型仍能使用长达数千甚至数万个词元的相当长的上下文。

> of tokens in the input. This makes it expensive to compute attention over very long documents (like entire novels). Nonetheless modern large language models manage to use quite long contexts of thousands or tens of thousands of tokens.

并行化多头注意力 在多头注意力中，与自注意力一样，输入和输出的模型维度为 d，键和查询嵌入的维度为 dk，值嵌入的维度为 dv（同样，在原始 transformer 论文中 dk = dv = 64，A = 8，d = 512）。因此对于每个头 c，我们有形状为 [d ×dk] 的权重层 WQc、形状为 [d ×dk] 的 WKc，以及形状为 [d ×dv] 的 WVc，它们与打包成 X 的输入相乘，产生形状为 [N × dk] 的 Q、形状为 [N × dk] 的 K 和形状为 [N × dv] 的 V。A 个头中每个头的输出形状为 [N × dv]，因此具有 A 个头的多头层的输出由 A 个形状为 [N × dv] 的矩阵组成。为了在后续处理中使用这些矩阵，它们被拼接起来，产生一个维度为 [N × Adv] 的单一输出。最后，我们使用一个形状为 [Adv ×d] 的最终线性投影 WO，将其重新变换为每个词元的原始输出维度。

> Parallelizing multi-head attention In multi-head attention, as with self-attention, the input and output have the model dimension d, the key and query embeddings have dimensionality dk, and the value embeddings are of dimensionality dv (again, in the original transformer paper dk = dv = 64, A = 8, and d = 512). Thus for each head c, we have weight layers WQc of shape [d ×dk], WKc of shape [d ×dk], and WVc of shape [d ×dv], and these get multiplied by the inputs packed into X to produce Q of shape [N × dk], K of shape [N × dk], and V of shape [N × dv]. The output of each of the A heads is of shape [N × dv], and so the output of the multihead layer with A heads consists of A matrices of shape [N × dv]. To make use of these matrices in further processing, they are concatenated to produce a single output with dimensionality [N × Adv]. Finally, we use a final linear projection WO of shape [Adv ×d], that reshapes it to the original output dimension for each token.

7.4 • 输入：词元与位置的嵌入 191

> 7.4 • THE INPUT: EMBEDDINGS FOR TOKEN AND POSITION 191

将拼接后的 [N × Adv] 矩阵输出与形状为 [Adv × d] 的 WO 相乘，得到形状为 [N ×d] 的自注意力输出 A。

> Multiplying the concatenated [N × Adv] matrix output by WO of shape [Adv × d] yields the self-attention output A of shape [N ×d].

Qi = XWQi ; Ki = XWKi ; Vi = XWVi

> (7.36)

 QiKi⊺ 

headi = SelfAttention(Qi,Ki,Vi) = softmax mask Vi

> (7.37)

√dk

MultiHeadAttention(X) = (head1 ⊕head2...⊕headA)WO (7.38)

结合并行输入矩阵 X 统一起来 由一整层 N 个 transformer 块——每个块作用于 N 个输入词元中的一个——并行计算的函数可以表示为：

> Putting it all together with the parallel input matrix X The function computed in parallel by an entire layer of N transformer blocks—each block over one of the N input tokens—can be expressed as:

O = X+MultiHeadAttention(LayerNorm(X))

> (7.39)

H = O+FFN(LayerNorm(O))

> (7.40)

注意，在式 7.39 中我们用 X 表示该层的输入，无论它来自何处。对于第一层，正如我们将在下一节看到的，该输入就是我们一直用 X 描述的初始词 + 位置嵌入向量。但对于后续的第 k 层，输入是上一层的输出 Hk−1。我们还可以分解 transformer 层中执行的计算，为每个组件的计算给出一个方程。我们将用 T（形状为 [N ×d]）表示 transformer，并用上标标出块内的每一次计算，同样用 X 表示来自上一层的块输入或初始嵌入：

> Note that in Eq. 7.39 we are using X to mean the input to the layer, wherever it comes from. For the first layer, as we will see in the next section, that input is the initial word + positional embedding vectors that we have been describing by X. But for subsequent layers k, the input is the output from the previous layer Hk−1. We can also break down the computation performed in a transformer layer, showing one equation for each component computation. We’ll use T (of shape [N ×d]) to stand for transformer and superscripts to demarcate each computation inside the block, and again use X to mean the input to the block from the previous layer or the initial embedding:

T1 = LayerNorm(X)

> (7.41)

T2 = MultiHeadAttention(T1)

> (7.42)

T3 = T2 +X

> (7.43)

T4 = LayerNorm(T3)

> (7.44)

T5 = FFN(T4)

> (7.45)

H = T5 +T3

> (7.46)

这里，当我们使用像 FFN(T3) 这样的记号时，我们指的是同一个 FFN 被并行地施加于窗口中 N 个嵌入向量中的每一个。类似地，N 个词元中的每一个都在 LayerNorm 中被并行地归一化。关键在于，Transformer 模块的输入维度与输出维度是匹配的，因此它们可以被堆叠。由于模块输入处的每个词元 xi 都由一个维度为 [1×d] 的嵌入表示，这意味着输入 X 和输出 H 的形状都是 [N ×d]。

> Here when we use a notation like FFN(T3) we mean that the same FFN is applied in parallel to each of the N embedding vectors in the window. Similarly, each of the N tokens is normed in parallel in the LayerNorm. Crucially, the input and output dimensions of transformer blocks are matched so they can be stacked. Since each token xi at the input to the block is represented by an embedding of dimensionality[1×d], that means the input X and output H are both of shape [N ×d].

## 7.4 输入：词元嵌入与位置嵌入

> 7.4 The input: embeddings for token and position

我们来谈谈输入 X 从何而来。给定一个包含 N 个词元的序列（N 是以词元计的上下文长度），形状为 [N × d] 的矩阵 X 为

> Let’s talk about where the input X comes from. Given a sequence of N tokens (N is the context length in tokens), the matrix X of shape [N × d] has an embedding for

> 嵌入
>
> *embedding*

上下文中的每个词都有一个嵌入。Transformer 通过分别计算两种嵌入来做到这一点：输入词元嵌入和输入位置嵌入。

> each word in the context. The transformer does this by separately computing two embeddings: an input token embedding, and an input positional embedding.

词元嵌入（在第 6 章中介绍）是一个维度为 d 的向量，它将

> A token embedding, introduced in Chapter 6, is a vector of dimension d that will

成为输入词元的初始表示。（当我们在残差流中把向量逐层向上传递通过 Transformer 的各层时，这种嵌入表示会发生变化 192 第 7 章 • TRANSFORMERS 与预训练 并不断增长，它会纳入上下文，并根据我们正在构建的语言模型类型扮演不同的角色。）初始嵌入的集合存储在嵌入矩阵 E 中，该矩阵为词表中 |V| 个词元各存一行。（提醒：这里的 V 指的是词元的词表，这个 V 与值向量无关。）因此每个词都是一个 d 维的行向量，而 E 的形状为 [|V|×d]。

> be our initial representation for the input token. (As we pass vectors up through the transformer layers in the residual stream, this embedding representation will change 192 CHAPTER 7 • TRANSFORMERS AND PRETRAINING and grow, incorporating context and playing a different role depending on the kind of language model we are building.) The set of initial embeddings are stored in the embedding matrix E, which has a row for each of the |V| tokens in the vocabulary.(Reminder that V here means the vocabulary of tokens, this V is not related to the value vector.) Thus each word is a row vector of d dimensions, and E has shape[|V|×d].

给定一个输入词元串，例如 Thanks for all the，我们首先把这些词元

> Given an input token string like Thanks for all the we first convert the tokens

转换为词表索引（这些索引是在我们最初使用 BPE 或 SentencePiece 对输入进行分词时创建的）。因此 thanks for all the 的表示可能是 w =[5,4000,10532,2224]。接下来我们用索引从 E 中选出对应的行（第 5 行、第 4000 行、第 10532 行、第 2224 行）。

> into vocabulary indices (these were created when we first tokenized the input using BPE or SentencePiece). So the representation of thanks for all the might be w =[5,4000,10532,2224]. Next we use indexing to select the corresponding rows from E, (row 5, row 4000, row 10532, row 2224).

另一种理解从嵌入矩阵中选取词元嵌入的方式

> Another way to think about selecting token embeddings from the embedding

是把词元表示为形状为 [1 × |V|] 的独热向量，即为词表中的每个词各留一个维度。回想一下，在独热向量中所有

> matrix is to represent tokens as one-hot vectors of shape [1 × |V|], i.e., with one dimension for each word in the vocabulary. Recall that in a one-hot vector all the

> 独热向量
>
> *one-hot vector*

元素都是 0，只有一个例外，即维度为该词在词表中索引的那个元素，其值为 1。因此，如果词 “thanks” 在词表中的索引为 5，那么 x5 = 1，且 xi = 0 ∀i̸ = 5，如下所示：

> elements are 0 except one, the element whose dimension is the word’s index in the vocabulary, which has value 1. So if the word “thanks” has index 5 in the vocabulary, x5 = 1, and xi = 0 ∀i̸ = 5, as shown here:

[0 0 0 0 1 0 0 ... 0 0 0 0] 1 2 3 4 5 6 7 ... ... |V|

乘以一个只有一个非零元素 xi = 1 的独热向量，其实就只是

> Multiplying by a one-hot vector that has only one non-zero element xi = 1 simply

选出词 i 对应的行向量，从而得到词 i 的嵌入，如图 7.12 所示。

> selects out the relevant row vector for word i, resulting in the embedding for word i, as depicted in Fig. 7.12.

| d<br>5<br>5 \|V\| d<br>1 0 0 0 0 1 0 0 … 0 0 0 0 ✕ E = 1<br>\|V\| |  |
| --- | --- |
| 图 7.12<br>Figure 7.12 | 选出词 V 的嵌入向量，方法是将嵌入<br>5<br>Selecting the embedding vector for word V by multiplying the embedding<br>5 |

> d

> 5 |V| 5 d

### = ✕ E

| 0 0 0 0 1 | 0 0 … 0 0 0 0 |
| --- | --- |

> 0 0 0 0 1 0 0 … 0 0 0 0

> |V|

> 图 7.12 通过将嵌入矩阵 E 与一个在第 5 个索引处为 1 的独热向量相乘，选出词 V5 的嵌入向量。
>
> *Figure 7.12 Selecting the embedding vector for word V5 by multiplying the embedding matrix E with a one-hot vector with a 1 in index 5.*

我们可以扩展这一思路，把整个词元序列表示为一个独热向量矩阵，为 Transformer 上下文窗口中的 N 个位置各用一个独热向量，如图 7.13 所示。

> We can extend this idea to represent the entire token sequence as a matrix of onehot vectors, one for each of the N positions in the transformer’s context window, as shown in Fig. 7.13.

| d<br>\|V\| d<br>0 0 0 0 1 0 0 … 0 0 0 0<br>0 0 0 0 0 0 0 … 0 0 1 0 ✕ =<br>1 0 0 0 0 0 0 … 0 0 0 0 E<br>…<br>N<br>N 0 0 0 0 1 0 0 … 0 0 0 0<br>\|V\| |  |
| --- | --- |
| 图 7.13<br>Figure 7.13 | 选出输入词元 id 序列 W 的嵌入矩阵，方法是乘以<br>Selecting the embedding matrix for the input sequence of token ids W by mul- |

> d

> |V| d

| 0 0 0 0 |  | 1 0 0 … 0 0 0 0 |  |  |
| --- | --- | --- | --- | --- |
| 0 0 0 0 0 0 0 … 0 0 |  |  | 1 | 0 |
| 1 | 0 0 0 0 0 0 … 0 0 0 0 |  |  |  |

> 0 0 0 0 1 0 0 … 0 0 0 0

### =

> 0 0 0 0 0 0 0 … 0 0 1 0

### ✕ E

> 1 0 0 0 0 0 0 … 0 0 0 0

> … N

> N

| 0 0 0 0 | 1 0 0 … 0 0 0 0 |
| --- | --- |

> 0 0 0 0 1 0 0 … 0 0 0 0

|V|

> 将对应于 W 的 one-hot 矩阵乘以嵌入矩阵 E。
>
> *tiplying a one-hot matrix corresponding to W by the embedding matrix E.*

这些词元嵌入与位置无关。为了表示位置

> These token embeddings are not position-dependent. To represent the position

序列中每个词元的位置，我们将这些词元嵌入与位置

> of each token in the sequence, we combine these token embeddings with positional

> 位置
>
> *positional*

嵌入相结合，这些位置嵌入针对输入序列中的每一个位置。

> embeddings specific to each position in an input sequence.

> 嵌入
>
> *embeddings*

这些位置嵌入从何而来？最简单的方法称为

> Where do we get these positional embeddings? The simplest method, called

> 绝对
>
> *absolute*

绝对位置（absolute position），即从随机初始化的嵌入开始，这些嵌入对应于

> absolute position, is to start with randomly initialized embeddings corresponding

> 位置
>
> *position*

7.5 • 语言建模头 193

> 7.5 • THE LANGUAGE MODELING HEAD 193

每一个可能的输入位置，最长直到某个最大长度。例如，正如我们为单词 fish 有一个嵌入一样，我们也会为位置 3 有一个嵌入。

> to each possible input position up to some maximum length. For example, just as we have an embedding for the word fish, we’ll have an embedding for the position 3.

与词嵌入一样，这些位置嵌入在训练过程中与其他参数一起学习。我们可以将它们存储在一个形状为 [N ×d] 的矩阵 Epos 中。

> As with word embeddings, these positional embeddings are learned along with other parameters during training. We can store them in a matrix Epos of shape [N ×d].

为了生成能够捕获位置信息的输入嵌入，我们只需将

> To produce an input embedding that captures positional information, we just add

每个输入的词嵌入加到其对应的位置嵌入上。单个词元嵌入和位置嵌入的维度都是 [1×d]，因此它们的和也是 [1 × d]。这个新的嵌入作为进一步处理的输入。图 7.14 展示了这一思路。

> the word embedding for each input to its corresponding positional embedding. The individual token and position embeddings are both of size [1×d], so their sum is also[1 × d]. This new embedding serves as the input for further processing. Fig. 7.14 shows the idea.

| Transformer 块<br>X = 复合<br>嵌入<br>（词 + 位置）<br>+ + + + +<br>词 Janet will back the bill<br>嵌入<br>位置 1 2 3 4 5<br>嵌入<br>Janet will back the bill<br>Transformer Block<br>X = Composite<br>Embeddings<br>(word + position)<br>+ + + + +<br>Word Janet will back the bill<br>Embeddings<br>Position 1 2 3 4 5<br>Embeddings<br>Janet will back the bill |  |
| --- | --- |
| 图 7.14<br>Figure 7.14 | 一种简单的建模位置的方式：将绝对位置的嵌入加到<br>A simple way to model position: add an embedding of the absolute position to |

![](images/img_395.png)

Transformer 块

> Transformer Block

> X = 复合嵌入（词 + 位置）
>
> *X = Composite Embeddings(word + position)*

+ + + + +

> 词
>
> *Word*

> Janet will back the bill

> 嵌入
>
> *Embeddings*

> 位置
>
> *Position*

> 1 2 3 4 5

> 嵌入
>
> *Embeddings*

> Janet will back the bill

> 词元嵌入，以生成一个维度相同的新嵌入。
>
> *the token embedding to produce a new embedding of the same dimensionality.*

输入的最终表示，即矩阵 X，是一个 [N ×d] 矩阵，其中

> The final representation of the input, the matrix X, is an [N ×d] matrix in which

每一行 i 是输入中第 i 个词元的表示，其计算方式是将 E[id(i)]——即在位置 i 出现的词元的 id 的嵌入——加到 Epos[i]，也就是位置 i 的位置嵌入上。

> each row i is the representation of the ith token in the input, computed by adding E[id(i)]—the embedding of the id of the token that occurred at position i—, to Epos[i], the positional embedding of position i.

这种简单的位置嵌入方法有一个潜在问题：

> A potential problem with the simple position embedding approach is that there

输入中靠前的位置会有大量训练样本，而在长度上限附近的位置则相应地少得多。后者的嵌入可能训练不足，在测试时可能无法很好地泛化。另一种做法是选择一个静态函数，以更好地处理任意长度序列的方式将整数输入映射为实值向量。原始的 transformer 工作中使用了不同频率的正弦和余弦函数的组合。正弦位置嵌入也可能有助于捕获位置之间的内在关系，例如输入中的位置 4 与位置 5 的关系比与位置 17 的关系更密切。

> will be plenty of training examples for the initial positions in our inputs and correspondingly fewer at the outer length limits. These latter embeddings may be poorly trained and may not generalize well during testing. An alternative is to choose a static function that maps integer inputs to real-valued vectors in a way that better handles sequences of arbitrary length. A combination of sine and cosine functions with differing frequencies was used in the original transformer work. Sinusoidal position embeddings may also help in capturing the inherent relationships among the positions, like the fact that position 4 in an input is more closely related to position 5 than it is to position 17.

更复杂的一类位置嵌入方法进一步扩展了这种捕获关系的思路，直接表示相对位置，而不是

> A more complex style of positional embedding methods extend this idea of capturing relationships even further to directly represent relative position instead of

> 相对
>
> *relative*

> 位置
>
> *position*

绝对位置，通常是在每一层的注意力机制中实现的，而不是在初始输入处只添加一次。此类位置嵌入机制中最流行的是旋转位置嵌入（RoPE）（Su et al., 2024）。

> absolute position, often implemented in the attention mechanism at each layer rather than being added once at the initial input. The most popular such positional embedding mechanism is the Rotary Position Embedding (RoPE) (Su et al., 2024).

> RoPE

## 7.5 语言建模头

> 7.5 The Language Modeling Head

我们必须介绍的 transformer 最后一个组件是语言建模

> The last component of the transformer we must introduce is the language modeling

> 语言
>
> *language*

头。这里我们用 head 一词指我们额外增加的神经网络电路，我们

> head. Here we are using the word head to mean the additional neural circuitry we

> 建模头
>
> *modeling head*

在把预训练 trans-

> add on top of the basic transformer architecture when we apply pretrained trans-

> 头
>
> *head*

194 第 7 章 • TRANSFORMER 与预训练

> 194 CHAPTER 7 • TRANSFORMERS AND PRETRAINING

former 模型应用于各种任务时，把它加在基础 transformer 架构之上。语言建模头就是我们做语言建模所需的电路。

> former models to various tasks. The language modeling head is the circuitry we need to do language modeling.

回忆一下，语言模型——从第 3 章简单的 n-gram 模型到

> Recall that language models, from the simple n-gram models of Chapter 3 through

第 6 章的前馈模型——都是词预测器。给定一个词的上下文，它们为每个可能的下一个词分配一个概率。例如，如果前面的上下文是“Thanks for all the”，而我们想知道下一个词是“fish”的可能性有多大，我们会计算：

> the feedforward models of Chapter 6, are word predictors. Given a context of words, they assign a probability to each possible next word. For example, if the preceding context is “Thanks for all the” and we want to know how likely the next word is“fish” we would compute:

P(fish|Thanks for all the)

语言模型使我们能够为每个可能的下一个词分配这样的条件概率，从而给出整个词表上的分布。第 3 章的 n-gram 语言模型根据一个词与前面 n −1 个词共现的计数来计算该词的概率。因此上下文大小为 n −1。对于 transformer 语言模型，上下文就是 transformer 上下文窗口的大小，正如上文所述，它可以从数十万词元到数百万词元。

> Language models give us the ability to assign such a conditional probability to every possible next word, giving us a distribution over the entire vocabulary. The n-gram language models of Chapter 3 compute the probability of a word given counts of its occurrence with the n −1 prior words. The context is thus of size n −1. For transformer language models, the context is the size of the transformer’s context window, which as we mentioned above can range from hundreds of thousands of tokens to millions.

| y1 y2 … y\|V\| 词概率 [1 x \|V\|]<br>语言建模头<br>Softmax 对词表 V 做 Softmax<br>L<br>接收 h 并输出<br>分布N 覆盖词表 V u1 u2 … u\|V\| Logits [1 x \|V\|]<br>反嵌入层<br>反嵌入 [d x \|V\|]<br>U = ET<br>hL hL hL [1 x d]<br>1 2 N<br>第 L 层<br>Transformer<br>块 …<br>w w w<br>1 2 N<br>y1 y2 … y\|V\| Word probabilities [1 x \|V\|]<br>Language Model Head<br>Softmax Softmax over vocab V<br>L<br>takes h and outputs a<br>distributionN o ver vocabulary V u1 u2 … u\|V\| Logits [1 x \|V\|]<br>Unembedding layer<br>Unembedding [d x \|V\|]<br>U = ET<br>hL hL hL [1 x d]<br>1 2 N<br>Layer L<br>Transformer<br>Block …<br>w w w<br>1 2 N |  |
| --- | --- |
| 图 7.15<br>Figure 7.15 | 语言建模头：位于 transformer 顶部的电路，它把<br>The language modeling head: the circuit at the top of a transformer that maps |

### …

> 词概率
>
> *Word probabilities*

> y1 y2 y|V| [1 x |V|]

> 语言建模头
>
> *Language Model Head*

|  | Soft | max |  |
| --- | --- | --- | --- |

> 接收 hL Softmax 对词表 V 做 Softmax
>
> *takes hL Softmax Softmax over vocab V*

> N 并输出
>
> *N and outputs a*

### …

> u1 u2 u|V|

> Logits

> [1 x |V|]

> 词表 V 上的分布
>
> *distribution over vocabulary V*

> 反嵌入层 反嵌入
>
> *Unembedding layer Unembedding*

> [d x |V|]

> U = ET

> hL hL hL [1 x d]

> 1 2 N

> 第 L 层 Transformer
>
> *Layer L Transformer*

|  |  |
| --- | --- |

### …

> 块
>
> *Block*

> w1 w2 wN

> 从最后一个 transformer 层中词元 N 的输出嵌入（hL N）映射到词表 V 中所有词上的概率分布。
>
> *from the output embedding for token N from the last transformer layer (hL N) to a probability distribution over words in the vocabulary V.*

语言建模头的工作是取最后一个 transformer 层在每个词元 i 处的输出，并用它预测位置 i+1 处即将出现的词。

> The job of the language modeling head is to take the output of the final transformer layer at each token i and use it to predict the upcoming word at position i+1.

在推理时，我们只需对最后一个词元 N 运行该头，并用它预测位置 N + 1 处即将出现的词。3 图 7.15 展示了如何完成这一任务：取最后一个词元在最后一层的输出（形状为 [1×d] 的 d 维输出嵌入），并生成词上的概率分布（我们将从中选一个词来生成）。

> For inference, we just run the head on the very last token N and use it to predict the upcoming word at position N + 1.3 Fig. 7.15 shows how to accomplish this task, taking the output of the last token at the last layer (the d-dimensional output embedding of shape [1×d]) and producing a probability distribution over words (from which we will choose one to generate).

图 7.15 中的第一个模块是一个线性层，其作用是从

> The first module in Fig. 7.15 is a linear layer, whose job is to project from the

输出 hL N（它表示来自最终块 L 位置 N 的输出 token 嵌入，因此形状为 [1×d]）映射到 logit 向量，或称得分向量，该向量将具有

> output hL N, which represents the output token embedding at position N from the final block L, (hence of shape [1×d]) to the logit vector, or score vector, that will have a

> logit

词表 V 中 |V| 个可能词各一个得分。因此 logit 向量 u 的维度为 [1×|V|]。

> single score for each of the |V| possible words in the vocabulary V. The logit vector u is thus of dimensionality [1×|V|].

这个线性层是可以学习的，但也很常见的是把这个矩阵绑定到

> This linear layer can be learned, but it is also very common to tie this matrix to

（转置后的）嵌入矩阵 E。回顾一下，在权重绑定中，我们使用

> (the transpose of) the embedding matrix E. Recall that in weight tying, we use the

> 权重绑定
>
> *weight tying*

模型中的两个不同矩阵使用相同的权重。因此在 transformer 的输入阶段

> same weights for two different matrices in the model. Thus at the input stage of the

> 3

> 而在训练时，语言建模头会在每个 token 位置预测一个词，而不仅仅是最后一个位置。
>
> *While for training, the language modeling head predicts a word at every token position, not just the last one.*

7.5 • 语言建模头 195

> 7.5 • THE LANGUAGE MODELING HEAD 195

transformer 中，嵌入矩阵（形状为 [|V|×d]）用于把词表上的 one-hot 向量（形状为 [1 × |V|]）映射为嵌入（形状为 [1 × d]）。

> transformer the embedding matrix (of shape [|V|×d]) is used to map from a one-hot vector over the vocabulary (of shape [1 × |V|]) to an embedding (of shape [1 × d]).

然后在语言建模头中，ET（嵌入矩阵的转置，形状为 [d ×|V|]）用于把嵌入（形状 [1×d]）反向映射为词表上的向量（形状 [1×|V|]）。在学习过程中，E 会被优化为擅长完成这两种映射。因此我们有时把转置 ET 称为反嵌入层（unembedding layer），因为它执行的是这种反向映射。

> And then in the language model head, ET, the transpose of the embedding matrix (of shape [d ×|V|]) is used to map back from an embedding (shape [1×d]) to a vector over the vocabulary (shape [1×|V|]). In the learning process, E will be optimized to be good at doing both of these mappings. We therefore sometimes call the transpose ET the unembedding layer because it is performing this reverse mapping.

> 反嵌入
>
> *unembedding*

softmax 层把 logit 向量 u 转换为词表上的概率 y。

> A softmax layer turns the logits u into the probabilities y over the vocabulary.

u = hL N ET

> (7.47)

y = softmax(u)

> (7.48)

我们可以用这些概率来做一些事情，比如帮助为一个

> We can use these probabilities to do things like help assign a probability to a

给定文本赋予概率。但最重要的用途是生成文本，我们将在下一节看到如何通过反复从概率向量 y 中采样一个元素 yk，并生成索引为 k 的词来实现。

> given text. But the most important usage is to generate text, which we’ll see how to do in the next section by repeatedly sampling an entry yk from the probability vector y, and generating the word with index k.

| … w<br>token 概率 y1 y2 y\|V\| i+1<br>采样 token 以<br>语言 softmax<br>在位置 i+1 生成<br>建模<br>头 logits u1 u2 … u\|V\|<br>U<br>hL<br>i<br>额外的层归一化<br>前馈<br>层 L 层归一化<br>注意力<br>层归一化<br>… hL-1 i = xL i<br>h2 = x3<br>i i<br>前馈<br>层归一化<br>层 2<br>注意力<br>层归一化<br>h1 = x2<br>i i<br>前馈<br>层 1 层归一化<br>注意力<br>层归一化<br>x1<br>i<br>+ i<br>输入<br>E 编码<br>输入 token w i<br>… w<br>Token probabilities y1 y2 y\|V\| i+1<br>Sample token to<br>Language softmax<br>generate at position i+1<br>Modeling<br>Head logits u1 u2 … u\|V\|<br>U<br>hL<br>i<br>extra layer norm<br>feedforward<br>Layer L layer norm<br>attention<br>layer norm<br>… hL-1 i = xL i<br>h2 = x3<br>i i<br>feedforward<br>layer norm<br>Layer 2<br>attention<br>layer norm<br>h1 = x2<br>i i<br>feedforward<br>Layer 1 layer norm<br>attention<br>layer norm<br>x1<br>i<br>+ i<br>Input<br>E Encoding<br>Input token w i |  |
| --- | --- |
| 图 7.16<br>Figure 7.16 | 一个 transformer 语言模型（仅解码器），堆叠 transformer 块<br>A transformer language model (decoder-only), stacking transformer blocks |

### …

wi+1

> y1 y2 y|V|

> token 概率
>
> *Token probabilities*

![](images/img_433.png)

> 语言 softmax 采样 token 以 建模 在位置 i+1 生成 头 logits
>
> *Language softmax Sample token to Modeling generate at position i+1 Head logits*

> u1 u2 … u|V|

> U

> hL i

> 额外的层归一化
>
> *extra layer norm*

![](images/img_435.png)

![](images/img_441.png)

> 前馈
>
> *feedforward*

> 层归一化
>
> *layer norm*

> 层 L
>
> *Layer L*

> 注意力
>
> *attention*

> 层归一化
>
> *layer norm*

> hL-1 i = xL

…

> i

> h2 i = x3

> i 前馈
>
> *i feedforward*

![](images/img_437.png)

> 层归一化
>
> *layer norm*

> 第 2 层
>
> *Layer 2*

> 注意力
>
> *attention*

> 层归一化
>
> *layer norm*

> h1 i = x2

> i

![](images/img_439.png)

> 前馈
>
> *feedforward*

> 层归一化
>
> *layer norm*

> 第 1 层
>
> *Layer 1*

> 注意力 层归一化
>
> *attention layer norm*

> x1

> i

> + i 输入
>
> *+ i Input*

> 编码
>
> *Encoding*

> E

wi

> 输入词元
>
> *Input token*

> 以及从输入词元 wi 到预测的下一个词元 wi+1 的映射。
>
> *and mapping from an input token wi to a predicted next token wi+1.*

图 7.16 展示了一个词元 i 的完整堆叠架构。注意，输入

> Fig. 7.16 shows the total stacked architecture for one token i. Note that the input

到每个 transformer 层的是 xℓ i，它与前一层 hℓ−1 的输出相同。

> to each transformer layer xℓ i is the same as the output from the preceding layer hℓ−1 .

> i

在结束之前说明一个术语问题：你有时会看到，用于这类单向因果语言模型的 transformer 被称为解码器—— 196 第 7 章 • Transformer 与预训练

> A terminological note before we conclude: You will sometimes see a transformer used for this kind of unidirectional causal language model called a decoder- 196 CHAPTER 7 • TRANSFORMERS AND PRETRAINING

> 仅解码器
>
> *decoder-only*

模型。这是因为该模型大致构成了 transformer 编码器-解码器模型的一半，我们将在第 13 章看到如何把它应用于机器翻译。（令人困惑的是，transformer 最初提出时采用的是编码器-解码器架构，直到后来，因果语言模型的标准范式才被定义为仅使用这一原始架构中的解码器部分。）

> only model. This is because this model constitutes roughly half of the encoderdecoder model for transformers that we’ll see how to apply to machine translation in Chapter 13. (Confusingly, the original introduction of the transformer had an encoder-decoder architecture, and it was only later that the standard paradigm for causal language model was defined by using only the decoder part of this original architecture).

> 模型
>
> *model*

## 7.6 解码

> 7.6 Decoding

根据模型的概率选择要生成的词元，这一任务称为解码。如上所述，以从左到右的方式（对于阿拉伯语等从右到左阅读的语言，则从右到左）从语言模型解码，从而基于先前选择反复选择下一个词元，称为因果生成或自回归生成。4

> The task of choosing a token to generate based on the model’s probabilities is called decoding. As we mentioned above, decoding from a language model in a left-toright manner (or right-to-left for languages like Arabic in which we read from right to left), and thus repeatedly choosing the next token conditioned on our previous choices is called causal or autoregressive generation.4

> 解码
>
> *decoding*

> 因果
>
> *causal*

> 自回归
>
> *autoregressive*

我们是从形状为 [1×|V|] 的概率向量 y 进行解码，它为

> We’re decoding from the probability vector y, of shape [1×|V|], which assigns a

> 生成
>
> *generation*

词汇表中的每个词元分配一个概率。图 7.17 展示了一个例子，出于教学目的，softmax 是在仅含 4 个词的简化词汇表上计算的。让我们用这个例子来研究生成时不同的采样方法。

> probability to each token in the vocabulary. Fig. 7.17 shows an example in which the softmax is computed for pedagogical purposes on a simplified vocabulary of only 4 words. Let’s use this example to investigate different methods of sampling words to generate.

| u y<br>logits softmax 概率<br>all 1.2 all .44<br>the 0.9 the .33<br>your 0.1 your .15<br>Transformer（或其他解码器） that -0.5 that .08<br>So long and thanks for ?<br>u y<br>logits softmax probabilities<br>all 1.2 all .44<br>the 0.9 the .33<br>your 0.1 your .15<br>Transformer (or other decoder) that -0.5 that .08<br>So long and thanks for ? |  |
| --- | --- |
| 图 7.17<br>Figure 7.17 | 使用 softmax 从 logit 向量 u 创建概率向量 y。<br>Using the softmax to create a probability vector y from the logit vector u. |

> u y logits softmax 概率
>
> *u y logits softmax probabilities*

![](images/img_465.png)

> 1.2 .44

> all all

> 0.9 .33

> the the

> 0.1 .15

> your your

![](images/img_463.png)

> that -0.5 .08

> that

> Transformer（或其他解码器）
>
> *Transformer (or other decoder)*

> ?

> So long and thanks for

### 7.6.1 贪心解码

> 7.6.1 Greedy decoding

生成 token 最简单的方式是始终生成最可能出现的 token

> The simplest way to generate tokens is to always generate the most likely token

> 贪心
>
> *greedy*

即在给定上下文的情况下最可能出现的那个 token，这被称为贪心解码。贪心算法是一种

> given the context, which is called greedy decoding. A greedy algorithm is one

> 解码
>
> *decoding*

只做出局部最优选择的算法，而不论事后看来它是否恰好是最佳选择。因此在贪心解码中，在生成过程的每一个时间步，我们都把 logits 转换为词表上 token 的概率分布，然后选择词表中概率最高的 token 作为输出 wt（即 argmax）：

> that makes a choice that is locally optimal, whether or not it will turn out to have been the best choice with hindsight. Thus in greedy decoding, at each time step in generation, we turn the logits into a probability distribution over tokens and then we choose as the output wt the token in the vocabulary that has the highest probability(the argmax):

ˆwt = argmaxw∈V P(w|w<t)

> (7.49)

> 严格来说，自回归模型基于若干值的线性函数来预测时刻 t 的一个值
>
> *Technically an autoregressive model predicts a value at time t based on a linear function of the values*

> 4

> 这些值取自时刻 t −1、t −2 等等。尽管语言模型并非线性（正如我们将看到的，它们具有许多层非线性变换），我们仍粗略地把这种生成技术称为自回归，因为每个时间步生成的 token 都以上一步网络所选出的 token 为条件。正如我们将看到的，第 9 章的掩码语言模型等替代方案是非因果的，因为它们可以同时依据过去和未来的 token 来预测 token。
>
> *at times t −1, t −2, and so on. Although language models are not linear (since, as we will see, they have many layers of non-linearities), we loosely refer to this generation technique as autoregressive since the token generated at each time step is conditioned on the token selected by the network from the previous step. As we’ll see, alternatives like the masked language models of Chapter 9 are non-causal because they can predict tokens based on both past and future tokens.*

7.6 • 解码 197

> 7.6 • DECODING 197

图 7.18 显示，在我们的例子中，模型选择生成 all。

> Fig. 7.18 shows that in our example, the model chooses to generate all.

| u y<br>logits softmax 概率<br>all 1.2 all .44<br>the 0.9 the .33<br>your 0.1 your .15<br>Transformer（或其他解码器） that -0.5 that .08<br>So long and thanks for ?<br>u y<br>logits softmax probabilities<br>all 1.2 all .44<br>the 0.9 the .33<br>your 0.1 your .15<br>Transformer (or other decoder) that -0.5 that .08<br>So long and thanks for ? |  |
| --- | --- |
| 图 7.18<br>Figure 7.18 | 贪心解码：选择概率最高的词。<br>Greedy decoding: choose the highest probability word. |

> u y

> logits softmax 概率
>
> *logits softmax probabilities*

![](images/img_489.png)

> 1.2 .44

> all all

> 0.9 .33

> the the

> 0.1 .15

> your your

![](images/img_487.png)

> -0.5 .08

> Transformer（或其他解码器）
>
> *Transformer (or other decoder)*

> that that

> ?

> So long and thanks for

然而在实践中，我们并不会对大型语言模型使用贪心解码。

> In practice, however, we don’t use greedy decoding with large language models.

贪心解码的一个主要问题是，由于它选择的 token（按定义）极容易预测，生成出的文本平淡无奇且往往相当重复。事实上，贪心解码的可预测性高到具有确定性：如果上下文完全相同，概率模型也相同，贪心解码总会生成完全相同的字符串。

> A major problem with greedy decoding is that because the tokens it chooses are(by definition) extremely predictable, the resulting text is generic and often quite repetitive. Indeed, greedy decoding is so predictable that it is deterministic; if the context is identical, and the probabilistic model is the same, greedy decoding will always result in generating exactly the same string.

我们将在第 13 章看到，贪心解码的一种扩展方法——束搜索（beam search）

> We’ll see in Chapter 13 that an extension to greedy decoding called beam search

在机器翻译这类任务中表现良好，因为这类任务约束很强：我们始终是以另一种语言中一段非常具体的文本为条件，生成某一语言的文本。

> works well in tasks like machine translation, which are very constrained in that we are always generating a text in one language conditioned on a very specific text in another language.

然而在大多数其他任务中，人们更偏好由

> In most other tasks, however, people prefer text which has been generated by

能为生成结果引入更多多样性的采样方法所生成的文本。

> sampling methods that introduce a bit more diversity into the generations.

### 7.6.2 随机采样

> 7.6.2 Random sampling

因此，大语言模型中最常见的解码方法涉及采样。回忆第 3 章，从分布中采样意味着依据其可能性来随机选取点。于是，从语言模型（它表示后续 token 上的一个分布）中采样，意味着根据模型赋予的概率来选择下一个要生成的 token。因此，我们更可能生成模型认为概率高的 token，而更不可能生成模型认为概率低的 token。

> Thus the most common method for decoding in large language models involves sampling. Recall from Chapter 3 that sampling from a distribution means to choose random points according to their likelihood. Thus sampling from a language model—which represents a distribution over following tokens—means to choose the next token to generate according to its probability assigned by the model. Thus we are more likely to generate tokens that the model thinks have a high probability and less likely to generate tokens that the model thinks have a low probability.

> 采样
>
> *sampling*

也就是说，我们依据 token 在

> That is, we randomly select a token to generate according to its probability in

模型所定义的上下文中的概率，随机选择要生成的 token，生成它，然后迭代。我们可以把它想象成掷骰子并依据所得概率选择一个 token，正如我们在第 3 章所见。这样的模型当然更可能生成概率最高的 token，就像贪心算法一样，但它也可能生成任何 token，只是机会更小。不过总体而言，我们更可能生成模型认为在上下文中概率高的 token，而更不可能生成模型认为概率低的 token。

> context as defined by the model, generate it, and iterate. We could think of this as rolling a die and choosing a token according to the resulting probability, as we saw in Chapter 3. Such a model is of course more likely to generate the highest probability token, just like the greedy algorithm, but it could also generate any token, just with smaller chances. But in general we are more likely to generate tokens that the model thinks have a high probability in the context and less likely to generate tokens that the model thinks have a low probability.

从语言模型中采样这一想法很早就由 Shannon

> Sampling from language models was first suggested very early on by Shannon

（1948）以及 Miller 和 Selfridge（1950）提出；我们在第 3 章第 79 页看到过，如何从一元语言模型生成文本：反复依据概率随机采样 token，直到达到预定长度或选中句子结束 token。

> (1948) and Miller and Selfridge (1950), and we saw back in Chapter 3 on page 79 how to generate text from a unigram language model by repeatedly randomly sampling tokens according to their probability until we either reach a pre-determined length or select the end-of-sentence token.

要从大语言模型生成文本，我们只需把这个模型

> To generate text from a large language model we’ll just generalize this model

稍微推广一点：每一步我们都根据在先前选择条件下 198 第 7 章 • TRANSFORMERS 与预训练 的概率来采样 token，并把大语言模型用作告诉我们这一概率的概率模型。

> a bit: at each step we’ll sample tokens according to their probability conditioned 198 CHAPTER 7 • TRANSFORMERS AND PRETRAINING on our previous choices, and we’ll use the large language model as the probability model that tells us this probability.

> 随机
>
> *random*

该算法称为随机采样，或称随机多项分布采样

> The algorithm is called random sampling, or random multinomial sampling

> 采样
>
> *sampling*

（因为我们是从跨词的多项分布中采样）。我们可以把随机采样形式化如下：我们生成一个 token 序列{w1,w2,...,wN}，直到遇到序列结束 token，其中用 x ∼p(x) 表示「从分布 p(x) 中采样来选取 x」：

> (because we are sampling from a multinomial distribution across words). We can formalize random sampling as follows: we are generating a sequence of tokens{w1,w2,...,wN} until we hit the end-of-sequence token, using x ∼p(x) to mean‘choose x by sampling from the distribution p(x)’:

> i←1 wi ∼p(w) while wi != EOS i←i + 1 wi ∼p(wi|w<i)

| u y<br>采样<br>logits softmax 概率<br>一个词<br>all 1.2 all .44<br>the 0.9 the .33<br>your 0.1 your .15 the<br>Transformer（或其他解码器） that -0.5 that .08<br>… …<br>So long and thanks for ?<br>u y<br>sample<br>logits softmax probabilities<br>a word<br>all 1.2 all .44<br>the 0.9 the .33<br>your 0.1 your .15 the<br>Transformer (or other decoder) that -0.5 that .08<br>… …<br>So long and thanks for ? |  |
| --- | --- |
| 图 7.19<br>Figure 7.19 | 随机多项分布采样：我们随机选择了一个词，依据其<br>Random multinomial sampling: we randomly chose a word according to its |

> u y 采样 logits softmax 概率 一个词
>
> *u y sample logits softmax probabilities a word*

![](images/img_513.png)

![](images/img_515.jpeg)

> 1.2 .44

> all all

> 0.9 .33

> the the

> 0.1 .15

> your your the

![](images/img_511.png)

> -0.5 .08

> that that

> Transformer（或其他解码器）
>
> *Transformer (or other decoder)*

> … …

> ?

> So long and thanks for

> 概率。
>
> *probability.*

唉，事实证明随机采样效果同样不佳。问题在于

> Alas, it turns out random sampling doesn’t work well either. The problem is that

尽管随机采样大多会生成合理的高概率 token，但分布的尾部仍然存在许多古怪的低概率 token。

> even though random sampling is mostly going to generate sensible, high-probable tokens, there are many odd, low-probability tokens in the tail of the distribution.

尽管每一个的概率都很低，但这些罕见 token 的总和构成了分布中不可忽视的一部分。结果，这些 token 被选中的频率足以导致生成出奇怪的句子。

> Even though each one is low-probability, the sum of these rare tokens constitutes a non-trivial portion of the distribution. As a result, these tokens get chosen often enough to result in weird sentences being generated.

换句话说，贪心解码太无聊，而随机采样又太随机。我们需要一种方法，既不每次都贪心地选取最优项，又不至于深入概率极低的事件。

> In other words, greedy decoding is too boring, and random sampling is too random. We need something that doesn’t greedily choose the top choice every time, but doesn’t stray down too far into the very low-probability events.

有三种标准采样方法通过对随机采样进行改造来解决这些问题：温度采样、top-k 和 top-p。

> There are three standard sampling methods that modify random sampling to address these issues. Temperature sampling, top-k, and top-p.

### 7.6.3 温度采样

> 7.6.3 Temperature sampling

接下来介绍的三种方法可以在生成中权衡两个重要因素：质量与多样性。强调最可能词的方法往往生成被人类评为更准确、更连贯、更符合事实的文本，但也更无聊、更重复。稍微更重视中等概率词的方法往往更有创造性、更多样，但更不符合事实，也更可能不连贯或质量低下。

> The next three methods we introduce enable trading off two important factors in generation: quality and diversity. Methods that emphasize the most probable words tend to produce generations that are rated by people as more accurate, more coherent, and more factual, but also more boring and more repetitive. Methods that give a bit more weight to the middle-probability words tend to be more creative and more diverse, but less factual and more likely to be incoherent or otherwise low-quality.

> 温度
>
> *temperature*

温度采样的思想是重塑概率分布，以

> The idea of temperature sampling is to reshape the probability distribution to

> 采样
>
> *sampling*

提高高概率 token 的概率，并降低低概率 token 的概率。其结果是，我们更不可能生成概率极低的 token，而更可能生成概率较高的 token。

> increase the probability of the high probability tokens and decrease the probability of the low probability tokens. The result is that we are less likely to generate very lowprobability tokens, and more likely to generate tokens that are higher probability.

实现这一直觉的做法很简单：在把 logit 送入 softmax 之前，先将其除以温度参数 τ。在低温采样中，τ ∈(0,1]。

> We implement this intuition by simply dividing the logit by a temperature parameter τ before passing it through the softmax. In low-temperature sampling, τ ∈(0,1].

7.6 • 解码 199

> 7.6 • DECODING 199

因此，我们不再像下面这样（重复自式 7.48）直接从 logit 计算整个词表上的概率分布：

> Thus instead of computing the probability distribution over the vocabulary directly from the logit as in the following (repeated from Eq. 7.48):

y = softmax(u)

> (7.50)

而是先把 logits 除以 τ，把概率向量 y 计算为

> we instead first divide the logits by τ, computing the probability vector y as

y = softmax(u/τ)

> (7.51)

也就是说，通常情况下我们按图 7.20(a) 所示从 logits 转换到 softmax。

> That is, normally we convert from logits to softmax as shown in Fig. 7.20(a).

但当我们使用温度参数时，要如图 7.20(b) 所示先对 logit 进行缩放。

> But when we use a temperature parameter we first scale the logit as in Fig. 7.20(b).

| u y u softmax y<br>logits 经 softmax 的概率 logits 加上温度后的概率<br>温度<br>a o3DmndcO74+qpyTJYhlgAXU/KBPVtv1fGr6kwHM<aexi>exp(a) a vOkKb+sum5nl2Jw1894QIEZChYxP7eHXADMdGW3RUqpN/zVSa6TFyftjLr=<i>exp(a/⌧)<br>b Z 其中 b Z 其中<br>exp(b) exp(b/⌧)<br>c Z = exp(a) c Z = exp(a/⌧)<br>Z Z<br>+exp(b) +exp(b/⌧)<br>d exp(c) d exp(c/⌧)<br>… Z +exp(c) … Z +exp(c/⌧)<br>exp(d) +exp(d) exp(d/⌧) +exp(d/⌧)<br>Z +... Z +...<br>… …<br>(a) (b)<br>u y u softmax y<br>logits softmax probabilities logits with probabilities<br>temperature<br>a o3DmndcO74+qpyTJYhlgAXU/KBPVtv1fGr6kwHM<aexi>exp(a) a vOkKb+sum5nl2Jw1894QIEZChYxP7eHXADMdGW3RUqpN/zVSa6TFyftjLr=<i>exp(a/⌧)<br>b Z where b Z where<br>exp(b) exp(b/⌧)<br>c Z = exp(a) c Z = exp(a/⌧)<br>Z Z<br>+exp(b) +exp(b/⌧)<br>d exp(c) d exp(c/⌧)<br>… Z +exp(c) … Z +exp(c/⌧)<br>exp(d) +exp(d) exp(d/⌧) +exp(d/⌧)<br>Z +... Z +...<br>… …<br>(a) (b) |  |
| --- | --- |
| 图 7.20<br>Figure 7.20 | (a)：未使用温度缩放的普通 softmax （b）为 softmax 加入温度缩放<br>(a): Normal softmax without temperature scaling (b) Adding temperature scaling to the softmax |

![](images/img_580.png)

> u y u softmax y logits 经 softmax 的概率 logits 加上温度后的概率
>
> *u y u softmax y logits softmax probabilities logits with probabilities*

![](images/img_578.png)

> 温度
>
> *temperature*

a a

> o3DmndcO74+qpydT+JYhl3Ygyp4cAJncAlXUAcOT/AK7/BhPVtv1mfJGrd+7ADv6pkfwHMyrcq</latexit>exp(a) vOkOKb+sum5n+sl2Jw1894lKQIEZsvClJhY2xPE7eHXAJDMdGCMsn1XW32RnUwqP+lpENw/z5VbSva269Vn+6qTbuF3EUyQk5IxfEJbekQR5Jk7QI19GwbCMsvFt7pkV83jeahqLmQr5VebpD24juks=</latexit>exp(a/⌧)

> Z Z

b b

> 其中 其中
>
> *where where*

> exp(b) Z = exp(a) exp(b/⌧) Z = exp(a/⌧)

c c

> Z +exp(b) Z +exp(b/⌧)

d d

> exp(c) exp(c/⌧)

> +exp(c) +exp(c/⌧)

… …

> Z Z exp(d) +exp(d) exp(d/⌧) +exp(d/⌧)

> Z +... Z +...

> … …

> (a) (b)

> 即先除以温度参数 τ。
>
> *by first dividing by the temperature parameter τ.*

为什么除以 τ 会增大高概率元素，并减小

> Why does dividing by τ increase the high probability elements and decrease the

词表项上的向量中的低概率元素呢？当 τ 为 1 时，我们执行的是普通 softmax，因此当 τ 接近 1 时分布变化不大。但当 τ 更小时，除以 τ < 1 会使更大的分数传入 softmax 函数。

> low probability elements in the vector over vocabulary items? When τ is 1, we are doing normal softmax, and so when τ is close to 1 the distribution doesn’t change much. But for smaller τ, dividing by τ < 1 results in larger scores being passed to the softmax function.

回忆一下，softmax 的一个有用性质是它倾向于把高

> Recall that one of the useful properties of a softmax is that it tends to push high

值推向 1、把低值推向 0。因此，当传入 softmax 的数值更大时，得到的分布会提高最高概率词元的概率、降低低概率词元的概率，使分布更加贪婪。而当 τ 趋近 0 时，除以 τ 意味着最可能的词的概率趋近 1，从而导致贪婪解码。

> values toward 1 and low values toward 0. Thus when larger numbers are passed to a softmax the result is a distribution with increased probabilities of the most highprobability tokens and decreased probabilities of the low probability tokens, making the distribution more greedy. And as τ approaches 0, dividing by τ means the probability of the most likely word approaches 1, resulting in greedy decoding.

温度采样的直觉来自热力学，在热力学中，处于高温的

> The intuition for temperature sampling comes from thermodynamics, where a

系统非常灵活，可以探索许多可能的状态；而处于较低温度的系统则倾向于探索能量更低（更好）状态的一个子集。在低温采样中，我们平滑地提高最可能词元的概率，并降低稀有词元的概率。

> system at a high temperature is very flexible and can explore many possible states, while a system at a lower temperature is likely to explore a subset of lower energy(better) states. In low-temperature sampling, we smoothly increase the probability of the most probable tokens and decrease the probability of the rare tokens.

图 7.21 展示了一个示意性例子，同样简化为词表中

> Fig. 7.21 shows a schematic example again simplified to have a vocabulary with

只有 4 个词元（all、the、your、that），并说明不同的温度值如何影响由初始 logits 计算出的概率。τ = 1 是普通 softmax，可以看到设 τ = 0.5 会把最靠前候选的概率从 .44 提高到 .59。设 τ = 0.1 会把最靠前候选的概率提高到 .95，使我们接近贪婪解码。

> only 4 tokens (all, the, your, that), and showing how different temperature values influence the probabilities computed from the initial logits. τ = 1 is the normal softmax, and we can see how setting τ = 0.5 increases the probability of the top candidate from .44 to .59. Setting τ = 0.1 increases the probability of the top candidate to .95, getting us close to greedy decoding.

在图 7.21 中我们还能看到另一些选项，适用于我们可能希望

> We can also see in Fig. 7.21 some other options for situations where we may want

把词概率分布拉平而不是让它变贪婪的情形。温度采样在这种情形下也有帮助，此时即高温采样，我们使用 τ > 1。

> to flatten the word probability distribution instead of making it greedy. Temperature sampling can help with this situation too, in this case high-temperature sampling, in which case we use τ > 1.

200 第 7 章 • Transformer 与预训练

> 200 CHAPTER 7 • TRANSFORMERS AND PRETRAINING

> 带温度 𝜏 的 softmax 输出
>
> *softmax output with temperature 𝜏*

| 带温度 𝜏 的 softmax 输出<br>贪心 softmax 均匀<br>se to rm a l se to<br>c lo n o c lo<br>logits 𝜏=0.1 𝜏=0.5 𝜏=1 𝜏=10 𝜏=100<br>all 1.2 .95 .59 .44 .27 .25<br>the 0.9 .05 .32 .33 .26 .25<br>your 0.1 0 .07 .15 .24 .25<br>that -0.5 0 .02 .08 .23 .25<br>低温 高温<br>采样 采样<br>（趋向贪心） （趋向均匀）<br>softmax output with temperature 𝜏<br>g re e d y so ftm a x u n ifo rm<br>se to rm a l se to<br>c lo n o c lo<br>logits 𝜏=0.1 𝜏=0.5 𝜏=1 𝜏=10 𝜏=100<br>all 1.2 .95 .59 .44 .27 .25<br>the 0.9 .05 .32 .33 .26 .25<br>your 0.1 0 .07 .15 .24 .25<br>that -0.5 0 .02 .08 .23 .25<br>low temperature high temperature<br>sampling sampling<br>(towards greedy) (towards uniform) |  |
| --- | --- |
| 图 7.21<br>Figure 7.21 | 温度采样：τ 的不同取值会改变所得到的概率<br>Temperature sampling: different values of τ change the resulting probabilities |

> 接近贪心 标准 softmax 接近均匀 𝜏=0.1 𝜏=0.5 𝜏=1 𝜏=10 𝜏=100
>
> *close to greedy normal softmax close to uniform𝜏=0.1 𝜏=0.5 𝜏=1 𝜏=10 𝜏=100*

> logits

> 1.2 .95 .59 .44 .27 .25

> all

> 0.9 .05 .32 .33 .26 .25

> the

> 0.1 0 .07 .15 .24 .25

> your

> -0.5 0 .02 .08 .23 .25

> that

> 低温 高温
>
> *low temperature high temperature*

> 采样 采样
>
> *sampling sampling*

> （趋向贪心） （趋向均匀）
>
> *(towards greedy) (towards uniform)*

> 由初始 logits 得到（词表中仅有 4 个词元的简化示例）。
>
> *from the initial logits (simplified example with just 4 tokens in the vocabulary).*

### 7.6.4 Top-k 与 top-p 采样

> 7.6.4 Top-k and top-p sampling

Top-k 采样是贪婪解码的一种简单推广。它不是挑选

> Top-k sampling is a simple generalization of greedy decoding. Instead of choosing

> top-k 采样
>
> *top-k sampling*

生成概率最高的单个词，而是先把分布截断为概率最高的 k 个词，再重新归一化以产生一个合法的概率分布，然后在这 k 个词中按它们重新归一化后的概率随机采样。更形式化地说：

> the single most probable word to generate, we first truncate the distribution to the top k most likely words, renormalize to produce a legitimate probability distribution, and then randomly sample from within these k words according to their renormalized probabilities. More formally:

- 预先选定一个词数 k
- 对词表 V 中的每个词，用语言模型计算该词在给定上下文下的可能性 p(wt|w<t)
- 按可能性对这些词排序，丢弃任何不属于概率最高的 k 个词的词。
- 对这 k 个词的分数重新归一化，使其成为合法的概率分布。
- 在这余下的 k 个最可能的词中，按其概率随机采样一个词。

> Choose in advance a number of words k
> For each word in the vocabulary V, use the language model to compute the likelihood of this word given the context p(wt|w<t)
> Sort the words by their likelihood, and throw away any word that is not one of the top k most probable words.
> Renormalize the scores of the k words to be a legitimate probability distribution.
> Randomly sample a word from within these remaining k most-probable words according to its probability.

当 k = 1 时，top-k 采样与贪婪解码完全相同。把 k 设为比 1 更大的

> When k = 1, top-k sampling is identical to greedy decoding. Setting k to a larger

数值，会使我们有时选到一个并不一定最可能、但概率仍然足够高的词，这样的选择能生成更多样但质量仍足够高的文本。

> number than 1 leads us to sometimes select a word which is not necessarily the most probable, but is still probable enough, and whose choice results in generating more diverse but still high-enough-quality text.

top-k 采样的一个问题是 k 是固定的，但不同上下文中词的概率分布形状并不相同。如果我们设 k = 10，有时概率最高的 10 个词会非常可能，并包含大部分概率质量；但在另一些时候概率分布会更平坦，概率最高的 10 个词只包含一小部分概率质量。

> One problem with top-k sampling is that k is fixed, but the shape of the probability distribution over words differs in different contexts. If we set k = 10, sometimes the top 10 words will be very likely and include most of the probability mass, but other times the probability distribution will be flatter and the top 10 words will only include a small part of the probability mass.

另一种方法称为 top-p 采样或核采样（nucleus sampling）（Holtzman 等，

> An alternative, called top-p sampling or nucleus sampling (Holtzman et al.,

> top-p 采样
>
> *top-p sampling*

2020），它保留的不是概率最高的 k 个词，而是概率质量中占比最高的那个 p 比例。

> 2020), is to keep not the top k words, but the top p percent of the probability mass.

目标是一样的：截断分布，以去除极不可能的词。

> The goal is the same; to truncate the distribution to remove the very unlikely words.

但通过以概率而非词数来度量，人们希望这种度量在差异极大的上下文中更为稳健，能动态地扩大和缩小候选词池。

> But by measuring probability rather than the number of words, the hope is that the measure will be more robust in very different contexts, dynamically increasing and decreasing the pool of word candidates.

7.7 • 预训练 Transformer 大语言模型 201

> 7.7 • PRETRAINING TRANSFORMER LLMS 201

给定一个分布 P(wt|w<t)，我们把这分布从概率最大开始排序，

> Given a distribution P(wt|w<t), we sort the distribution from most probable, and

那么 top-p 词表 V (p) 是满足下式的最小词集合：

> then the top-p vocabulary V (p) is the smallest set of words such that

X

P(w|w<t) ≥p.

> (7.52)

> w∈V (p)

也许令人意外的是，把 top-k 和 top-p 两种采样结合起来是很常见的做法，

> Perhaps surprisingly, it is common to combine both top-k and top-p sampling,

即先用 top-k 作为一种硬性过滤器剔除垃圾，再用 top-p 来适应模型的置信水平。

> using top-k first as a kind of a hard filter to eliminate garbage, and then using top-p to adapt to the model’s confidence level.

## 7.7 预训练 Transformer 大语言模型

> 7.7 Pretraining Transformer LLMs

如第 1 章所讨论的，在预训练中，我们把大规模文本语料分词作为训练材料，通常是在大规模网页抓取数据之外再补充其他高质量数据。然后在每个词元 t 处，我们要求模型预测下一个词元，并通过误差反向传播配合梯度下降来训练模型的参数（嵌入、前馈、注意力及其他权重矩阵）。我们把这样的模型称为自监督模型，因为我们不必为数据添加任何特殊的金标注；词的自然序列本身就是它的监督！我们只是训练模型，使其在预测训练序列中真实的下一个词时的误差最小。

> In pretraining, as we discussed in Chapter 1, we tokenize a large corpus of text as training material, usually by augmenting large crawls of the web with other high quality data. Then at each token t we ask the model to predict the next token, and train the parameters of the model (the embedding, feedforward, attention, and other weight matrices) via error backpropagation with gradient descent. We call such a model self-supervised because we don’t have to add any special gold labels to the data; the natural sequence of words is its own supervision! We simply train the model to minimize the error in predicting the true next word in the training sequence.

我们最小化并回传经过网络的损失函数，就是我们在第 4 章和第 6 章已经见过两次的交叉熵损失函数。回忆一下，交叉熵损失衡量的是预测概率分布与正确分布之间的差异。该概率分布定义在词元词表之上，因此损失为：

> The loss function we minimize and pass back through the network is the crossentropy loss function we’ve now seen twice, in Chapter 4 and Chapter 6. Recall that the cross-entropy loss measures the difference between a predicted probability distribution and the correct distribution. The probability distribution is over the token vocabulary, making the loss be:

X

LCE(ˆyt,yt) = − yt[w]log ˆyt[w]

> (7.53)

> w∈V

在语言建模的情形中，正确的分布 yt 来自对下一个词的已知信息。它表示为一个与词表对应的独热向量，其中实际下一个词对应的项为 1，其他所有项均为 0。因此，语言建模的交叉熵损失由模型赋予正确的下一个词元的概率决定（其他所有词元都会被式 7.53 中的第一项乘以零）。

> In the case of language modeling, the correct distribution yt comes from knowing the next word. This is represented as a one-hot vector corresponding to the vocabulary where the entry for the actual next word is 1, and all the other entries are 0. Thus, the cross-entropy loss for language modeling is determined by the probability the model assigns to the correct next token (all other tokens get multiplied by zero by the first term in Eq. 7.53).

因此，不失一般性，我们可以说在时刻 t，下式中的交叉熵损失

> So without loss of generality we can say that at time t the cross-entropy loss in

式 7.53 可以简化为模型赋予训练序列中下一个词的负对数概率 −log p(wt+1)，或者更形式化地说，用 ˆy 表示语言模型估计出的词元概率向量：

> Eq. 7.53 can be simplified as the negative log probability the model assigns to the next word in the training sequence, −log p(wt+1), or more formally, using ˆy to mean the vector of estimated token probabilities from the language model:

LCE(ˆyt,yt) = −log ˆyt[wt+1]

> (7.54)

因此，在输入的每个词位置 t，模型以正确的词元序列 w1:t 作为输入，并用它们计算可能的下一个词元上的概率分布，从而计算模型对下一个词元 wt+1 的损失。接着我们移到下一个词，我们忽略模型对下一个词所作出的预测，转而使用正确的词元序列 w1:t+1 让模型估计词元 wt+2 的概率。这种始终把正确的历史序列交给模型来预测下一个词（而不是把上一时间步模型的最佳猜测喂给模型）的做法，称为教师强制（teacher forcing）。

> Thus at each word position t of the input, the model takes as input the correct sequence of tokens w1:t, and uses them to compute a probability distribution over possible next tokens so as to compute the model’s loss for the next token wt+1. Then we move to the next word, we ignore what the model predicted for the next word and instead use the correct sequence of tokens w1:t+1 to get the model to estimate the probability of token wt+2. This idea that we always give the model the correct history sequence to predict the next word (rather than feeding the model its best guess from the previous time step) is called teacher forcing.

> 教师强制
>
> *teacher forcing*

202 第 7 章 • TRANSFORMERS 与预训练

> 202 CHAPTER 7 • TRANSFORMERS AND PRETRAINING

图 7.22 展示了通用的训练方法。在每一步，给定所有

> Fig. 7.22 illustrates the general training approach. At each step, given all the

前面的词元，最后的 Transformer 层会在整个词表上产生一个输出分布。训练时，赋予正确词的概率被用来计算序列中每一项的交叉熵损失。每个批次的损失是整个序列上负对数概率的平均交叉熵损失，更形式化地说：

> preceding tokens, the final transformer layer produces an output distribution over the entire vocabulary. During training, the probability assigned to the correct word is used to calculate the cross-entropy loss for each item in the sequence. The loss for each batch is the average cross-entropy loss over the entire sequence of negative log probabilities, or more formally:

> T

1 X

LCE(batch of length T) = −log ˆyt[wt+1]

> (7.55)

T

> t=1

随后通过梯度下降调整网络中的权重，使该批次上的平均交叉熵损失最小（图 4.5），并利用计算图上的误差反向传播来计算梯度。训练会调整网络的所有权重，包括包含每个词嵌入的嵌入矩阵 E。这样学到的嵌入将最擅长预测即将出现的词。

> The weights in the network are then adjusted to minimize this average cross-entropy loss over the batch via gradient descent (Fig. 4.5), using error backpropagation on the computation graph to compute the gradient. Training adjusts all the weights of the network, including the embedding matrix E that contains the embeddings for each word. Thus embeddings will be learned that are most successful at predicting upcoming words.

| 真实下一个词元 long and thanks for all …<br>CE 损失 −log y long −log y and −log y thanks −log y for −log y all …<br>每词元<br>ŷ ŷ ŷ ŷ ŷ<br>反向 反向 反向 反向 反向<br>传播 传播 传播 传播 传播<br>…<br>LLM<br>输入词元 So long and thanks for …<br>True next token long and thanks for all …<br>CE Loss −log y long −log y and −log y thanks −log y for −log y all …<br>per token<br>ŷ ŷ ŷ ŷ ŷ<br>back back back back back<br>prop prop prop prop prop<br>…<br>LLM<br>Input tokens So long and thanks for … |  |
| --- | --- |
| 图 7.22<br>Figure 7.22 | 预训练 LLM。在每个词元位置，模型向上输出 yˆ，即其概率<br>Pretraining an LLM. At each token position, the model passes up yˆ, its proba- |

### …

long and thanks for all

> 真实下一个词元
>
> *True next token*

> CE 损失
>
> *CE Loss*

> −log ylong −log yand −log ythanks −log yfor −log yall

### …

> 每词元
>
> *per token*

ŷ ŷ ŷ ŷ ŷ

> 反向 反向 反向 反向 反向 传播 传播 传播 传播 传播
>
> *back back back back back prop prop prop prop prop*

### …

> LLM

So long and thanks for

### …

> 输入词元
>
> *Input tokens*

> 图 7.22 预训练 LLM。在每个词元位置，模型向上输出 ˆy，即其对可能的下一个词的概率估计。模型对正确词元的概率估计的负对数被用作损失，该损失通过模型反向传播以训练所有权重，包括嵌入。损失在一个批次内的所有词元上取平均。
>
> *Figure 7.22 Pretraining an LLM. At each token position, the model passes up ˆy, its probability estimate over possible next words. The negative log of the model’s probability estimate for the correct token is used as the loss, which is backpropagated through the model to train all the weights, including the embeddings. Losses are averaged over all the tokens in a batch.*

Transformer 的优点之一是训练可以并行进行，

> One of the strengths of the transformer is that training can be done in parallel,

这使得在数万亿词元上进行预训练变得实际可行。之所以能够并行，是因为我们预先知道期望的输出 (wt+1)，而且因果掩码阻止每个位置关注其自身的目标，从而使每个词元的输出可以分别计算。这意味着上下文窗口中的所有 N 个位置都可以一次性对照其真实的下一词元进行评分，从而在一次网络前向传播中得到 N 个训练样本。

> making it practical to pretrain on trillions of tokens. Parallelism is possible because we know in advance the desired output (wt+1), and the causal mask prevents each position from attending to its own target, allowing the output for each token to be computed separately. This means that all N positions in the context window can be scored at once against their true next tokens, giving N training examples from one pass through the network.

大型模型通常通过用文本填满整个上下文窗口（包含数十万个 token）来训练。如果文档比这个长度短，就把多个文档打包进同一个窗口，文档之间用一个特殊的文本结束 token 分隔。梯度下降的批大小通常相当大（最大的 GPT-3 模型使用的批大小为 320 万个 token）。

> Large models are generally trained by filling the full context window (of hundreds of thousands of tokens) with text. If documents are shorter than this, multiple documents are packed into the window with a special end-of-text token between them. The batch size for gradient descent is usually quite large (the largest GPT-3 model uses a batch size of 3.2 million tokens).

### 7.7.1 评估大语言模型：困惑度

> 7.7.1 Evaluating Large Language Models: Perplexity

正如我们在第 3 章首次看到的，评估语言模型的一种方式是衡量它对未见文本的预测效果。更好的语言模型更擅长预测 7.7 • 预训练 Transformer 大语言模型 203 即将出现的词，因此当每个词在测试集中出现时，它会更不感到意外（即赋予更高的概率）。于是我们可以通过把文本中每个 token 的条件概率相乘来计算该文本的概率，并将其作为一个指标：

> As we first saw in Chapter 3, one way to evaluate language models is to measure how well they predict unseen text. A better language model is better at predicting 7.7 • PRETRAINING TRANSFORMER LLMS 203 upcoming words, and so it will be less surprised by (i.e., assign a higher probability to) each word when it occurs in the test set. So we can compute the probability of a text by multiplying the conditional probabilities for each token in the text, and use that as a metric:

TY

likelihood(w1:T) = P(wi|w<i)

> (7.56)

> i=1

然而，测试集的概率取决于它的长度，长度越长，概率越小。（T 越大，我们相乘的概率就越多，而由于每个概率都小于 1，乘积会越来越小。）因此，有一个按 token、按长度归一化的指标是很有用的，这样我们就能比较不同长度的文本。

> However, the probability of a test set depends on its length, and gets smaller the longer it is. (The higher T is, the more probabilities we multiply, and since probabilities are each less than 1 the product will get smaller and smaller). So it’s useful to have a metric that is per-token, normalized by length, so we can compare across texts of different lengths.

我们已经有了一个按长度归一化的指标，它在第 3 章介绍过：困惑度（perplexity）。回想一下，模型在未见测试集上的困惑度，就是模型赋予该测试集的概率的倒数，

> We have a length-normalized metric already, introduced in Chapter 3: perplexity. Recall that the perplexity of a model on an unseen test set is the inverse proba-

> 困惑度
>
> *perplexity*

并按测试集的 token 长度归一化。

> bility that the model assigns to the test set normalized by the test set length in tokens.

对于一个包含 T 个 token 的测试集 w1:T，其困惑度为

> For a test set of T tokens w1:T, the perplexity is

Perplexity(w1:T) = P(w1:T)−1

> T

TY ! 1

> T

P(wt|w<t)−1

> (7.57)

=

> t=1

但困惑度的式 7.57 应当让上一节的内容显得似曾相识。它

> But Eq. 7.57 for perplexity should look familiar from the previous section. It’s

几乎与我们在训练时使用的平均交叉熵损失函数（式 7.55）相同。我们在这里把该等式重复一遍，并稍微改变记号，用 P 代替 ˆyt：

> almost the same as the mean cross-entropy loss function that we used to train, Eq. 7.55. We’ve repeated that equation here, changing the notation a bit to use P instead of ˆyt:

> T

1 X

LCE(batch of length T) = −logP(wt|w<t)

> (7.58)

T

> t=1

事实上，一段文本的困惑度就是该文本平均交叉熵损失的指数。我们把这一证明留作读者的练习。（注意，由于这里的 log 指自然对数，平均交叉熵损失的单位是 nat（熵的单位，

> In fact, the perplexity of a text is simply the exponent of the mean cross-entropy loss for the text. We leave showing this as an exercise for the reader. (Note that because log here means natural log, mean cross-entropy loss is in nats (the units of entropy

> nat
>
> *nats*

即当我们使用 ln 而非 log2 时）。）

> when we use ln as opposed to log2).)

注意，由于式 7.57 中的倒数（以及它等价于

> Note that because of the inverse in Eq. 7.57 (and the fact that it’s equivalent to

一个损失这一事实），词序列的概率越高，困惑度就越低。

> a loss), the higher the probability of the word sequence, the lower the perplexity.

因此，模型在数据上的困惑度越低，模型就越好。

> Thus the lower the perplexity of a model on the data, the better the model.

最小化困惑度等价于按照语言模型最大化测试集的概率。

> Minimizing perplexity is equivalent to maximizing the test set probability according to the language model.

有一点需要注意：由于困惑度取决于文本中 token 的数量 n，它

> One caveat: because perplexity depends on the number of tokens n in a text, it

对分词算法的差异非常敏感。这意味着，如果两个语言模型使用的分词器差别很大，就很难精确比较它们各自产生的困惑度。因此，困惑度最好用于比较使用同一分词器的语言模型。

> is very sensitive to differences in the tokenization algorithm. That means that it’s hard to exactly compare perplexities produced by two language models if they have very different tokenizers. For this reason perplexity is best used when comparing language models that use the same tokenizer.

困惑度衡量的是某一类准确率：预测词的准确率。在

> Perplexity measures one kind of accuracy: accuracy at predicting words. In

第 1 章中，我们还介绍了 MMLU 以及其他用于衡量问答任务准确率的数据集。在后续章节中，我们会介绍更多针对特定任务的评估方法，用于衡量大语言模型在其他任务上的准确率：第 13 章的机器翻译、第 11 章的信息检索，以及第 16 章的语音识别。

> Chapter 1 we also introduced MMLU and other datasets for measuring accuracy at question answering tasks. In future chapters we’ll introduce more task-specific evaluations for measuring LLM accuracy at other tasks: for machine translation in Chapter 13, information retrieval in Chapter 11, and speech recognition in Chapter 16.

204 第 7 章 • Transformer 与预训练

> 204 CHAPTER 7 • TRANSFORMERS AND PRETRAINING

## 7.8 当前模型与一些数据

> 7.8 Current models and some numbers

当前的 Transformer 语言模型采用了一系列高级设置。其中一些我们在上文已经提到过，例如旋转位置嵌入（rotary position embeddings，RoPE）、RMSNorm，以及带 SwiGLU 激活的门控前馈层（Shazeer, 2020）。这些主要是让模型更好、更准确的办法。

> Current transformer language models use a number of advanced settings. Some of these we’ve mentioned above, like rotary position embeddings (RoPE), RMSNorm, and gated feedforward layers with SwiGLU activation (Shazeer, 2020). These are mainly ways to make models better, more accurate.

另一些我们完全没有讨论过的进展则着眼于效率，即让模型

> Others advances that we haven’t discussed at all focus on efficiency, ways to

运行得更快或占用更少内存的办法。为了略作展示，我们在这里简要介绍其中一项进展：KV 缓存。

> make models faster or use less memory. Just to give a flavor of these, here we give a short introduction to one such advance, the KV cache.

回想图 7.11 和式 7.34（重复如下）中，注意力向量

> Recall from Fig. 7.11 and in Eq. 7.34 (repeated below) that the attention vector

在训练时可以通过两次矩阵乘法非常高效地并行计算：

> can be very efficiently computed in parallel for training, via two matrix multiplications:

QK⊺ 

head = softmax

> (7.59)

√dk V

遗憾的是，在推理时我们无法像训练时那样进行同样高效的注意力计算。这是因为在推理时，我们每次迭代地生成一个下一个 token。对于刚刚生成的新 token（记为 xi），我们需要分别乘以 WQ、WK 和 Wv 来计算它的 query、key 和 value。但对所有先前的 token x<i 重新计算 key 和 value 向量会浪费计算时间；在之前的步骤中我们已经计算过这些 key 和 value 向量了！

> Unfortunately we can’t do quite the same efficient attention computation in inference as in training. That’s because at inference time, we iteratively generate the next tokens one at a time. For a new token that we have just generated, call it xi, we need to compute its query, key, and values by multiplying by WQ, WK, and WV respectively. But it would be a waste of computation time to recompute the key and value vectors for all the prior tokens x<i; at prior steps we already computed these key and value vectors!

KV 缓存是一种避免这种时间浪费的技术。我们不再重新计算

> The KV cache is a technique to avoid this waste of time. Instead of recomputing

> KV 缓存
>
> *KV cache*

这些向量，而是在每次计算 key 和 value 向量时把它们存入内存中的缓存，之后需要时直接从缓存中取出即可。图 7.23 修改自图 7.11，用以展示针对单个新 token 所进行的计算，并标明哪些值可以从 KV 缓存中取出而不必重新计算。

> these, whenever we compute the key and value vectors we store them in memory in a cache, and then we can just grab them from the cache when we need them. Fig. 7.23 modifies Fig. 7.11 to show the computation that takes place for a single new token, showing which values we can take from the KV cache rather than recompute.

| T V A<br>Q QK<br>T<br>K<br>v1<br>x = x v2 = k1 k2 k3 k4<br>v3<br>d x N<br>q4 k q4•k1 q4•k2 q4•k3 q4•k4 v4 a4<br>1 x d k 1 x N N x d v 1 x d v |  |
| --- | --- |
| 图 7.23<br>Figure 7.23 | 部分注意力计算（摘取自图 7.11），以黑色显示，<br>Parts of the attention computation (extracted from Fig. 7.11) showing, in black, |

> Q QKT V A

> KT

> v1

| k1 | k2 | k3 | k4 |
| --- | --- | --- | --- |

> x =

> v2

> x

> =

> v3

> dk x N

|  |  |  |  |
| --- | --- | --- | --- |
| q4•k1 | q4•k2 | q4•k3 | q4•k4 |

> q4 q4•k1 q4•k2 q4•k3 q4•k4 v4 a4

> 1 x dk 1 x N N x dv 1 x dv

> 即在计算第 4 个 token 的注意力分数时可存入缓存而不必重新计算的向量。
>
> *the vectors that can be stored in the cache rather than recomputed when computing the attention score for the 4th token.*

还有许多其他这类以效率为核心的创新，包括专家混合（Mixture-of-Experts）模型、分组查询注意力（Grouped-Query Attention，GQA）和量化。我们希望能在第二卷的未来版本中介绍这些内容。

> There are many other such efficiency-focused innovations, including Mixtureof-Experts models, Grouped-Query Attention (GQA), and quantization. We hope to get to these in a future version of Volume II.

为了大致了解架构参数的取值范围，图 7.24 给出了

> To give a basic idea of the range of architectural parameters, Fig. 7.24 shows

当前与较早的一些 LLM 的若干架构参数。由于 GPT-5、Claude 和 Gemini 等前沿专有模型的开发者不公开任何此类信息，我们只列出开放模型。请注意，由于其中一些模型采用了 GQA 和 SwiGLU 等现代架构（它们的 A 不同，也并不严格把 df f 设为 d 的 4 倍），这些参数数值只能视为粗略近似，仅用于了解规模。

> some architectural parameters for a small selection of current and older LLMs. Because makers of frontier proprietary models like GPT-5, Claude, and Gemini don’t disclose any of this information, we only list open models. Note that because some of these models use modern architectures like GQA and SwiGLU (which have different A and don’t exactly set df f to be 4 times d), these parameters numbers should be taken as rough approximations just to get ideas of scale.

7.9 • 小结 205

> 7.9 • SUMMARY 205

模型 年份 L d A dff |V| 上下文 参数量 GPT-2 XL 2019 48 1600 25 6400 50K 1K 1.5B GPT-3 2020 96 12288 96 49152 50K 2K 175B Qwen3-0.6B 2025 28 1024 16 3072 152K 32K 0.6B Qwen3-32B 2025 64 5120 64 25600 152K 128K 32B Llama 3.1 8B 2024 32 4096 32 14336 128K 128K 8B Llama 3.1 405B 2024 126 16384 128 53248 128K 128K 405B

> Model Year L d A dff |V| Context Params GPT-2 XL 2019 48 1600 25 6400 50K 1K 1.5B GPT-3 2020 96 12288 96 49152 50K 2K 175B Qwen3-0.6B 2025 28 1024 16 3072 152K 32K 0.6B Qwen3-32B 2025 64 5120 64 25600 152K 128K 32B Llama 3.1 8B 2024 32 4096 32 14336 128K 128K 8B Llama 3.1 405B 2024 126 16384 128 53248 128K 128K 405B

| 模型 年份 L d A d ff \|V \| 上下文 参数量<br>Model Year L d A d ff \|V \| Context Params |  |
| --- | --- |
| GPT-2 XL 2019 48 1600 25 6400 50K 1K 1.5B<br>GPT-3 2020 96 12288 96 49152 50K 2K 175B<br>Qwen3-0.6B 2025 28 1024 16 3072 152K 32K 0.6B<br>Qwen3-32B 2025 64 5120 64 25600 152K 128K 32B<br>Llama 3.1 8B 2024 32 4096 32 14336 128K 128K 8B<br>Llama 3.1 405B 2024 126 16384 128 53248 128K 128K 405B |  |
| 图 7.24<br>Figure 7.24 | 一些 Transformer 语言模型的配置。L 是层<br>Configurations of some transformer language models. L is the number of lay- |

> 数，d 是模型维度，A 是注意力头数，dff 是前馈维度，|V| 是词表大小。
>
> *ers, d the model dimension, A the number of attention heads, dff the feedforward dimension, and |V| the vocabulary size.*

## 7.9 小结

> 7.9 Summary

本章介绍了用于语言建模的 Transformer 及其组件，以及预训练和解码过程。以下是我们所涵盖要点的总结：

> This chapter has introduced the transformer and its components for language modeling, and the pretraining and decoding processes. Here’s a summary of the main points that we covered:

- Transformer 是基于注意力思想的网络。
- 多头注意力计算接收一个输入向量 xi，通过加上来自先前 token 的向量把它映射为输出 ai，这些向量的权重取决于它们对处理当前词的相关程度。
- Transformer 块由一个残差流构成：来自前一层的输入沿残差流向上传递到下一层，不同组件的输出被加到其中。这些组件包括一个多头注意力层，其后是一个前馈层，两者之前都各有层归一化。

> Transformers are networks based on the idea of attention.
> A multi-head attention computation takes an input vector xi and maps it to an output ai by adding in vectors from prior tokens, weighted by how relevant they are for the processing of the current word.
> A transformer block consists of a residual stream in which the input from the prior layer is passed up to the next layer, with the output of different components added to it. These components include a multi-head attention layer followed by a feedforward layer, each preceded by layer normalizations.

把 Transformer 块堆叠起来，就能构成更深、更强大的网络。

> Transformer blocks are stacked to make deeper and more powerful networks.

- Transformer 的输入由嵌入（用嵌入矩阵计算得到）与位置编码相加得到，位置编码表示该 token 在窗口中的顺序位置。
- 语言模型可以由多层 transformer 块堆叠而成，顶部设有一个语言模型头，它对顶层输出 H 应用反嵌入矩阵以生成 logits，这些 logits 随后经过 softmax 生成词概率。
- 基于 transformer 的语言模型具有很宽的上下文窗口（从数十万到数百万个 token），使它们能够利用巨量的上下文来预测接下来出现的词。
- 在 transformer 大语言模型中，生成哪个词是通过从可能的下一个词的分布中采样决定的。
- 一种常见的采样方法是温度采样，它介于两个极端之间：一端是贪心解码，即我们总是生成概率最大的词；另一端是随机采样，即我们按照词的概率随机生成一个词。
- 温度采样提高高概率词的概率，降低低概率词的概率，然后从这个新分布中采样。
- 大语言模型通过交叉熵损失进行预训练，在通常从网络抓取的数万亿 token 数据集上预测词。
- 语言模型的预测准确度可以用困惑度来评估，而困惑度正是交叉熵损失的指数。

> The input to a transformer is computed by adding an embedding (computed with an embedding matrix) to a positional encoding that represents the sequential position of the token in the window.
> Language models can be built out of stacks of transformer blocks, with a language model head at the top, which applies an unembedding matrix to the output H of the top layer to generate the logits, which are then passed through a softmax to generate word probabilities.
> Transformer-based language models have a wide context window (hundreds of thousands to millions of tokens) allowing them to draw on enormous amounts of context to predict upcoming words.
> The choice of which word to generate in transformer LLMs is done by sampling from the distribution of possible next words.
> A common sampling approach is temperature sampling, which lies in between two extremes, those of greedy decoding in which we always generate the most probable word, and at the other end random sampling, in which we generate a random word according to its probability.
> Temperature sampling increases the probabilities of the high-probability words, decreases the probability of the low-probability words, and then samples from this new distribution.
> Large language models are pretrained via cross-entropy loss to predict words on datasets of trillions of tokens generally scraped from the web.
> Language model predictive accuracy can be evaluated by perplexity, which turns out to be the exponent of the cross-entropy loss.

206 第 7 章 • TRANSFORMERS 与预训练

> 206 CHAPTER 7 • TRANSFORMERS AND PRETRAINING

## 历史注记

> Historical Notes

正如我们在第 3 章所讨论的，最早的语言模型是由 IBM 托马斯·J·沃森研究中心的 Fred Jelinek 及其同事，以及 CMU 的 James Baker（大致同时且各自独立地）开发的 N-gram 语言模型。正是 Jelinek 和 IBM 团队首次创造了 language model（语言模型）这一术语，用来指代一个描述任何种类的语言属性（语法、语义、语篇、说话人特征）如何影响词序列概率的模型（Jelinek et al., 1975）。他们把语言模型与声学模型对照起来，后者刻画音素序列的声学/语音特征。

> As we discussed in Chapter 3, the earliest language models were the n-gram language models developed (roughly simultaneously and independently) by Fred Jelinek and colleagues at the IBM Thomas J. Watson Research Center, and James Baker at CMU. It was Jelinek and the IBM team who first coined the term language model to mean a model of the way any kind of linguistic property (grammar, semantics, discourse, speaker characteristics), influenced word sequence probabilities(Jelinek et al., 1975). They contrasted the language model with the acoustic model which captured acoustic/phonetic characteristics of phone sequences.

在接下来的 40 年里，N-gram 语言模型被极其广泛地使用，跨越

> N-gram language models were very widely used over the next 40 years, across

诸如语音识别和机器翻译等各种 NLP 任务，通常作为模型的多个组件之一。这些 N-gram 模型的上下文变得越来越长，5-gram 模型已被非常高效的 LM 工具包普遍使用（Stolcke, 2002; Heafield, 2011）。

> a wide variety of NLP tasks like speech recognition and machine translation, often as one of multiple components of the model. The contexts for these n-gram models grew longer, with 5-gram models used quite commonly by very efficient LM toolkits(Stolcke, 2002; Heafield, 2011).

神经大语言模型的根源存在于多个地方。其中之一是

> The roots of the neural large language model lie in multiple places. One was

20 世纪 90 年代，同样是在 IBM 研究院 Jelinek 的小组中，判别式分类器被应用于语言模型。Roni Rosenfeld 在其博士论文（Rosenfeld, 1994）中，首次在该 IBM 实验室把逻辑回归（当时称为最大熵模型或 maxent 模型）应用于语言建模，并在 Rosenfeld (1996) 中发表了更完整的版本。他的模型在逻辑回归预测器中整合了各种信息，包括 N-gram 信息以及来自上下文的其他特征，例如远程 N-gram 和称为触发词对（trigger pairs）的关联词对。Rosenfeld 的模型预示了现代语言模型：它是一个统计词预测器，以自监督方式训练，仅通过学习预测语料中即将出现的词。

> the application in the 1990s, again in Jelinek’s group at IBM Research, of discriminative classifiers to language models. Roni Rosenfeld in his dissertation (Rosenfeld, 1994) first applied logistic regression (under the name maximum entropy or maxent models) to language modeling in that IBM lab, and published a more fully formed version in Rosenfeld (1996). His model integrated various sorts of information in a logistic regression predictor, including n-gram information along with other features from the context, including distant n-grams and pairs of associated words called trigger pairs. Rosenfeld’s model prefigured modern language models by being a statistical word predictor trained in a self-supervised manner simply by learning to predict upcoming words in a corpus.

另一个是首次使用预训练的嵌入来建模词义，见于

> Another was the first use of pretrained embeddings to model word meaning in

LSA/LSI 模型（Deerwester et al., 1988）。回顾第 5 章的历史部分：在 LSA（潜在语义分析）中，先在语料上训练一个词项-文档矩阵，然后应用奇异值分解，用前 300 个维度作为表示词的向量嵌入。正是 Landauer et al. (1997) 首次使用了“embedding（嵌入）”一词。除了发展预训练和嵌入的思想之外，LSA 社群还开发了把 LSA 嵌入与 N-gram 结合在一个一体化语言模型中的方法（Bellegarda, 1997; Coccaro and Jurafsky, 1998）。

> the LSA/LSI models (Deerwester et al., 1988). Recall from the history section of Chapter 5 that in LSA (latent semantic analysis) a term-document matrix was trained on a corpus and then singular value decomposition was applied and the first 300 dimensions were used as a vector embedding to represent words. It was Landauer et al. (1997) who first used the word “embedding”. In addition to their development of the idea of pretraining and of embeddings, the LSA community also developed ways to combine LSA embeddings with n-grams in an integrated language model(Bellegarda, 1997; Coccaro and Jurafsky, 1998).

在一系列极具影响力的、发展神经语言模型思想的论文中，

> In a very influential series of papers developing the idea of neural language

（Bengio et al. 2000; Bengio et al. 2003; Bengio et al. 2006），Yoshua Bengio 及其同事汲取了这两条自监督语言建模工作路线的核心思想（判别式训练的词预测器，以及预训练的嵌入）。与 Rosenfeld 的最大熵模型一样，Bengio 的模型把连续文本中的下一个词作为监督信号。与 LSA 模型一样，Bengio 的模型学习了一个嵌入，但与 LSA 模型不同的是，它把这一学习作为语言建模过程的一部分。Bengio et al. (2003) 的模型是一个神经语言模型：一个学习根据前面的词预测下一个词的神经网络，并且通过在预测过程中学习嵌入来完成这件事。

> models, (Bengio et al. 2000; Bengio et al. 2003; Bengio et al. 2006), Yoshua Bengio and colleagues drew on the central ideas of both these lines of self-supervised language modeling work (the discriminatively trained word predictor, and the pretrained embeddings). Like the maxent models of Rosenfeld, Bengio’s model used the next word in running text as its supervision signal. Like the LSA models, Bengio’s model learned an embedding, but unlike the LSA models did it as part of the process of language modeling. The Bengio et al. (2003) model was a neural language model: a neural network that learned to predict the next word from prior words, and did so via learning embeddings as part of the prediction process.

多年来，神经语言模型以各种方式得到扩展，其中或许

> The neural language model was extended in various ways over the years, perhaps

最重要的是 Mikolov et al. (2010) 和 Mikolov et al. (2011) 的 RNN 语言模型形式。RNN 语言模型也许是第一个精确到足以超越传统 5-gram 练习 207 语言模型性能的神经模型。

> most importantly in the form of the RNN language model of Mikolov et al. (2010) and Mikolov et al. (2011). The RNN language model was perhaps the first neural model that was accurate enough to surpass the performance of a traditional 5-gram EXERCISES 207 language model.

不久之后，Mikolov et al. (2013a) 和 Mikolov et al. (2013b) 提出，

> Soon afterwards, Mikolov et al. (2013a) and Mikolov et al. (2013b) proposed to

简化这些神经网络语言模型的隐藏层，以创建预训练的 word2vec 词嵌入。

> simplify the hidden layer of these neural net language models to create pretrained word2vec word embeddings.

像 LSA 和 word2vec 这样的静态嵌入模型实例化了一种特定的

> The static embedding models like LSA and word2vec instantiated a particular

预训练模式：先在预训练数据集上训练一个表示，然后这些表示可用于后续任务。Dai and Le (2015) 和 Peters et al. (2018) 重新框定了这一思想，提出先用语言模型目标预训练模型，随后同一个模型既可以冻结并直接用于语言建模，也可以继续用语言模型目标进一步微调。例如 ELMo 使用一个 biLSTM，用语言模型目标在大型预训练数据集上自监督，然后在特定领域数据集上微调，之后冻结权重并添加任务特定的头。ELMo 这项工作尤其具有影响力，它的出现也许正是社群清楚意识到语言模型可以作为 NLP 问题通用解决方案的时刻。

> model of pretraining: a representation was trained on a pretraining dataset, and then the representations could be used in further tasks. Dai and Le (2015) and Peters et al. (2018) reframed this idea by proposing models that were pretrained using a language model objective, and then the identical model could be either frozen and directly applied for language modeling or further fine-tuned still using a language model objective. For example ELMo used a biLSTM self-supervised on a large pretrained dataset using a language model objective, then fine-tuned on a domainspecific dataset, and then froze the weights and added task-specific heads. The ELMo work was particularly influential and its appearance was perhaps the moment when it became clear to the community that language models could be used as a general solution for NLP problems.

Transformer 最初被用作编码器-解码器（Vaswani et al., 2017），

> Transformers were first applied as encoder-decoders (Vaswani et al., 2017) and

随后被用于掩码语言建模（Devlin et al., 2019）（我们将在第 13 章和第 9 章看到）。Radford et al. (2019) 随后表明，基于 transformer 的自回归语言模型 GPT-2 能对许多 NLP 任务（如摘要和问答）执行零样本。

> then to masked language modeling (Devlin et al., 2019) (as we’ll see in Chapter 13 and Chapter 9). Radford et al. (2019) then showed that the transformer-based autoregressive language model GPT-2 could perform zero-shot on many NLP tasks like summarization and question answering.

用于语言模型的技术也可以应用于其他领域

> The technology used for language models can also be applied to other domains

> 基础
>
> *foundation*

和任务，如视觉、语音和遗传学。当我们要计算的对象不必然是词时，术语 foundation model（基础模型）有时被用作更一般的说法，指这种跨领域和跨区域使用大语言模型技术的情形。Bommasani et al. (2021) 是一篇概述基础模型机遇与风险的广泛综述，其中特别关注大语言模型。

> and tasks, like vision, speech, and genetics. The term foundation model is sometimes used as a more general term for this use of large language model technology across domains and areas, when the elements we are computing over are not necessarily words. Bommasani et al. (2021) is a broad survey that sketches the opportunities and risks of foundation models, with special attention to large language models.

> 模型
>
> *model*

Transformer（Vaswani et al., 2017）是在两条

> The transformer (Vaswani et al., 2017) was developed drawing on two lines of

先前研究的基础上发展起来的：自注意力与记忆网络。

> prior research: self-attention and memory networks.

编码器-解码器注意力，即对输入词的编码使用软加权

> Encoder-decoder attention, the idea of using a soft weighting over the encodings

来指导生成式解码器的思想（见第 13 章），由 Graves (2013) 在手写生成背景下提出，并由 Bahdanau et al. (2015) 用于机器翻译。这一思想通过去掉对独立的编码序列和解码序列的需求，转而把注意力视为在汇集从低层向高层传递的信息时对 token 加权的方式，从而扩展到自注意力（Ling et al., 2015; Cheng et al., 2016; Liu et al., 2016）。

> of input words to inform a generative decoder (see Chapter 13) was developed by Graves (2013) in the context of handwriting generation, and Bahdanau et al. (2015) for MT. This idea was extended to self-attention by dropping the need for separate encoding and decoding sequences and instead seeing attention as a way of weighting the tokens in collecting information passed from lower layers to higher layers (Ling et al., 2015; Cheng et al., 2016; Liu et al., 2016).

Transformer 的其他方面，包括键（key）、查询（query）和

> Other aspects of the transformer, including the terminology of key, query, and

值，来自记忆网络（memory networks）——一种通过用查询的嵌入去匹配表示联想记忆中内容的键、从而给网络添加外部读写记忆的机制（Sukhbaatar 等，2015；Weston 等，2015；Graves 等，2014）。

> value, came from memory networks, a mechanism for adding an external readwrite memory to networks, by using an embedding of a query to match keys representing content in an associative memory (Sukhbaatar et al., 2015; Weston et al., 2015; Graves et al., 2014).

[更多 transformer 历史待下一稿补充。]

> [More transformer history is TBD in the next draft.]

## 练习

> Exercises

7.1 一个 transformer 有 L 层、模型维度 d、A 个注意力头，其中 dk =

> 7.1 A transformer has L layers, model dimension d, A attention heads with dk =

dv = d/A，前馈维度 d f f = 4d。

> dv = d/A, and feedforward dimension d f f = 4d.

208 第 7 章 • TRANSFORMER 与预训练

> 208 CHAPTER 7 • TRANSFORMERS AND PRETRAINING

- 统计一个注意力层中 W Q、W K、WV 和 W O 的参数个数。

> Count the parameters in one attention layer’s W Q, W K, WV, and W O.

你的答案是否依赖于 A？

> Does your answer depend on A?

- 统计一个前馈层中的参数个数。
- 证明完整的 L 个模块堆叠大约有 12Ld2 个参数，忽略偏置和层归一化。

> Count the parameters in one feedforward layer.
> Show that the full stack of L blocks has about 12Ld2 parameters, ignoring biases and layer norm.

7.2 为什么图 7.10 中的注意力掩码使用 −∞ 而不是 0？如果

> 7.2 Why does the attention mask in Fig. 7.10 use −∞rather than 0? What would

改用 0 会发生什么？

> happen if we used 0?

7.3 计算语言模型在字符串 It was a dream 上的困惑度，

> 7.3 Compute the perplexity of a language model on the string It was a dream,

假设各个词各自的条件概率分别为 .0001、.0002、.000005 和 .0000001。

> assuming the conditional probabilities of each respective word are .0001, .0002,.000005, and .0000001.

7.4 证明一段文本的困惑度等于平均交叉熵

> 7.4 Prove that the perplexity of a text is equal to the exp of the mean cross-entropy

损失的 exp。

> loss for the text.

7.5 利用图 7.17 中的 logits，计算 τ = 0.2 和 τ = 2 时的概率。

> 7.5 With the logits in Fig. 7.17, compute the probabilities at τ = 0.2 and τ = 2.

验证每个结果之和都为 1。当 τ →0 时会发生什么？当 τ →∞ 时呢？

> Verify each sums to 1. What happens as τ →0? As τ →∞?
