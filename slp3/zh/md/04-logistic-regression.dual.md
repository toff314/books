# 第 4 章 逻辑回归

### 章

> CHAPTER

# 4 逻辑回归与文本分类

> 4 Logistic Regression and Text Classification

> 在其遥远的书页上写着，动物被分为：
>
> *En sus remotas p´aginas est´a escrito que los animales se dividen en:*

> a. 属于皇帝的 h. 包含在此分类中的
>
> *a. pertenecientes al Emperador h. incluidos en esta clasificaci´on*

> b. 经过防腐处理的 i. 像疯子一样躁动的
>
> *b. embalsamados i. que se agitan como locos*

> c. 受过训练的 j. 数不清的
>
> *c. amaestrados j. innumerables*

> d. 乳猪 k. 用极细的骆驼毛画笔绘成的
>
> *d. lechones k. dibujados con un pincel fin´ısimo de pelo de camello*

> e. 美人鱼 l. 等等
>
> *e. sirenas l. etc´etera*

> f. 传说中的 m. 刚刚打破花盆的
>
> *f. fabulosos m. que acaban de romper el jarr´on*

> g. 散养的狗 n. 从远处看起来像苍蝇的
>
> *g. perros sueltos n. que de lejos parecen moscas*

> Borges (1964)

分类处于语言处理与智能的核心。识别一个字母、一个词或一张面孔，分拣邮件，给作业评分；这些都是为输入分配类别的例子。分类所面临的挑战，由寓言作家 Jorge Luis Borges（1964）作出了著名的揭示，他想象出一部古代神话百科全书，把动物分为：

> Classification lies at the heart of language processing and intelligence. Recognizing a letter, a word, or a face, sorting mail, assigning grades to homeworks; these are all examples of assigning a category to an input. The challenges of classification were famously highlighted by the fabulist Jorge Luis Borges (1964), who imagined an ancient mythical encyclopedia that classified animals into:

（a）属于皇帝的，（b）经过防腐处理的，（c）受过训练的，（d）乳猪，（e）美人鱼，（f）传说中的，（g）走失的狗，（h）包含在此分类中的，（i）像疯子一样颤抖的，（j）数不清的，（k）用极细的骆驼毛画笔绘成的，（l）其他的，（m）刚刚打破花瓶的，（n）从远处看起来像苍蝇的。

> (a) those that belong to the Emperor, (b) embalmed ones, (c) those that are trained, (d) suckling pigs, (e) mermaids, (f) fabulous ones, (g) stray dogs, (h) those that are included in this classification, (i) those that tremble as if they were mad, (j) innumerable ones, (k) those drawn with a very fine camel’s hair brush, (l) others, (m) those that have just broken a flower vase, (n) those that resemble flies from a distance.

幸运的是，我们用于语言处理的类别比

> Luckily, the classes we use for language processing are easier to define than
博尔赫斯的那些更容易定义。在本章中，我们介绍用于

> those of Borges. In this chapter we introduce the logistic regression algorithm for

> `text`（文本）

文本分类的逻辑回归算法。作为贯穿本章的示例，我们将应用文本分类，即

> classification. For our running example, we’ll apply text categorization, the task

> `categorization`（分类）

为文本或文档分配标签或类别的任务。我们将介绍情感

> of assigning a label or category to a text or document. We’ll introduce sentiment

> `sentiment`（情感）

分析，即对情感进行分类的任务，情感是

> analysis, the task of classifying sentiment, the positive or negative orientation that

> `analysis`（分析）

作者对某个对象所表达的情感。对一部电影、一本书或一件产品的评论表达了作者对该产品的情感，而一篇社论或政治文本则表达了对某一行动或候选人的情感。抽取情感与从市场营销到政治的诸多领域都相关。其他文本分类任务同样重要。在垃圾邮件检测中，我们把一封电子邮件归入两个类别之一：垃圾邮件或

> a writer expresses toward some object. A review of a movie, book, or product expresses the author’s sentiment toward the product, while an editorial or political text expresses sentiment toward an action or candidate. Extracting sentiment is relevant for fields from marketing to politics. Other text classification tasks are equally important. In spam detection we assign an email to one of the two classes spam or

> `spam detection language id authorship attribution`（垃圾邮件检测 语言识别 作者归属）

非垃圾邮件。语言识别是判断一段文本以何种语言书写的任务，

> not-spam. Language id is the task of determining what language a text is written
而作者归属是确定文本作者的任务，这

> in, while authorship attribution is the task of determining a text’s author, relevant
与人文学科和法证分析都相关。

> to both humanistic and forensic analysis.

但使分类如此重要的原因在于，语言建模也可以

> But what makes classification so important is that language modeling can also
被视为分类：每个词都可以看作一个类别，因此我们可以把预测下一个词看作是把到目前为止的上下文分类到下一个词的类别中！这一直觉正是大语言模型的基础。

> be viewed as classification: each word can be thought of as a class, and so we can think of predicting the next word as classifying the context-so-far into a class for each next word! This intuition underlies large language models.

我们在本章介绍的分类算法，逻辑回归，

> The algorithm for classification we introduce in this chapter, logistic regression,
同样重要。首先，逻辑回归与神经网络有着密切的关系。正如我们将在第 6 章看到的，神经网络可以看作是一系列层层堆叠的逻辑回归分类器。其次，逻辑回归引入了对语言模型至关重要的思想，如 sigmoid 和

> is equally important. First, logistic regression has a close relationship with neural networks. As we will see in Chapter 6, a neural network can be viewed as a series of logistic regression classifiers stacked on top of each other. Second, logistic regression introduces ideas that are fundamental to language models, like the sigmoid and

> `sigmoid`

softmax 函数、logit，以及用于学习的关键算法——梯度下降。

> softmax functions, the logit, and the key gradient descent algorithm for learning.

> `softmax`

最后，逻辑回归也是

> Finally, logistic regression is also one of the most important analytic tools in the

> `logit`

社会科学与自然科学中最重要的分析工具之一。

> social and natural sciences.

最后，我们将思考分类所需的特征。对于

> Finally, we’ll be thinking about the features we need for classification. For
情感分析来说，像 awesome 和 love，或者 awful 和 ridiculously 这样的词，都是分类器可以利用的极具信息量的特征，正如我们从这些电影/餐厅评论的示例摘录中所见：

> sentiment analysis words like awesome and love, or awful and ridiculously are very informative features for a classifier to make use of, as we can see from these sample extracts from movie/restaurant reviews:

+ ……超棒的焦糖酱和香甜的烤杏仁。我爱这个地方！−……糟糕的披萨和贵得离谱……

> + ...awesome caramel sauce and sweet toasty almonds. I love this place!−...awful pizza and ridiculously overpriced...

## 4.1 机器学习与分类

> 4.1 Machine learning and classification

分类的目标是接收单个输入（我们将每个输入称为一个观测样本），提取该输入的一些有用特征或属性，并据此将

> The goal of classification is to take a single input (we call each input an observation), extract some useful features or properties of the input, and thereby classify

> `observation`（观测样本）

该观测样本归入一组离散类别中的某一类。我们将输入记为 x，并说输出来自一个固定的输出类别集合 Y = {y1,y2,...,yM}。我们的目标是从 Y 中返回一个预测类别。有时你会看到输出类别被称为集合 C 而不是 Y。

> the observation into one of a set of discrete classes. We’ll call the input x, and say that the output comes from a fixed set of output classes Y = {y1,y2,...,yM}. Our goal is to return a predicted class from Y. Sometimes you’ll see the output classes referred to as the set C instead of Y.

对于情感分析，输入 x 可能是一段评论，或某些其他文本。而

> For sentiment analysis, the input x might be a review, or some other text. And
输出集合 Y 可能是如下集合：

> the output set Y might be the set:

{positive,negative}
或集合

> or the set
{0,1}
对于语言识别，输入可能是我们想知道它以何种语言写成的一段文本，而输出集合 Y 是各种语言的集合，即

> For language id, the input might be a text that we need to know what language it was written in, and the output set Y is the set of languages, i.e.,
Y = {Abkhaz,Ainu,Albanian,Amharic,...Zulu,Zu˜ni}
进行分类的方法有很多。一种方法是使用人工手写的规则

> There are many ways to do classification. One method is to use rules handwritten
（由人编写）。例如，我们可能有这样一条规则：

> by humans. For example, we might have a rule like:

如果单词 ‘‘love’’ 出现在 x 中，且它前面不是单词 ‘‘don’t"，则归类为 positive

> If the word ‘‘love’’ appears in x, and it’s not preceded by the word ‘‘don’t", classify as positive
手写规则可以作为现代 NLP 系统的组成部分，例如可用于情感分析的人工编写的正面词和负面词列表，我们将在下文看到。但规则可能很脆弱，因为情境或数据会随时间变化，而且许多任务中不同特征之间存在复杂的相互作用（如上文规则中“don’t”的否定示例），因此人类很难想出能在众多情境下都取得成功的规则。

> Handwritten rules can be components of modern NLP systems, such as the handwritten lists of positive and negative words that can be used in sentiment analysis, as we’ll see below. But rules can be fragile, as situations or data change over time, and for many tasks there are complex interactions between different features (like the example of negation with “don’t” in the rule above), so it can be quite hard for humans to come up with rules that are successful over many situations.

我们稍后将介绍的另一种方法是询问大型语言模型，通过

> Another method that we will introduce later is to ask a large language model by
提示模型为某段文本给出标签。提示可以很强大，但同样有弱点：语言模型经常产生幻觉，并且可能无法解释它们为什么选择了某个类别。

> prompting the model to give a label to some text. Prompting can be powerful, but again has weaknesses: language models often hallucinate, and may not be able to explain why they chose the class they did.

由于这些原因，进行分类最常见的方法是使用有监督机器学习。有监督机器学习是一种范式，其中除输入和输出类别集合之外，我们还有带标签的训练集和一个学习算法。我们在第 3 章讨论过训练集，当时它是用于计算 n-gram 统计量的载体。但在有监督机器学习中，训练集是带标签的，也就是说它包含一组输入观测样本，每个观测样本都关联着正确的输出（一个“监督信号”）。我们通常可以把训练集称为 m 个输入/输出对的集合，在文本分类的情形中，每个输入 x 是一段文本，并且每个都手工标注了关联的类别（正确标签）。

> For these reasons the most common way to do classification is to use supervised machine learning. Supervised machine learning is a paradigm in which, in addition to the input and the set of output classes, we have a labeled training set and a learning algorithm. We talked about training sets in Chapter 3 as a locus for computing n-gram statistics. But in supervised machine learning the training set is labeled, meaning that it contains a set of input observations, each observation associated with the correct output (a ‘supervision signal’). We can generally refer to a training set of m input/output pairs, where each input x is a text, in the case of text classification, and each is hand-labeled with an associated class (the correct label).

$$\text{training set:} \{ ( x ^{( 1 )} , y ^{( 1 )} ) , ( x ^{( 2 )} , y ^{( 2 )} ) ,..., ( x ^{( m )} , y ^{( m )} ) \}$$

我们将使用括号中的上标来指代训练集中的各个观测样本或实例。因此对于情感分类，训练集可能是一组句子或其他文本，每个都带有其正确的情感标签。

> We’ll use superscripts in parentheses to refer to individual observations or instances in the training set. So for sentiment classification, a training set might be a set of sentences or other texts, each with their correct sentiment label.

我们的目标是从这个训练集中学习得到一个分类器，它能够将

> Our goal is to learn from this training set a classifier that is capable of mapping
新的输入 x 映射到其正确类别 y ∈Y。它通过学习在这些训练句子中找出特征（也许是像 “awesome” 或 “awful” 这样的词）来实现这一点。像逻辑回归这样的概率分类器，除了给出答案（该观测样本所属的类别）之外，还给出该观测样本属于该类别的概率。这种类别上的分布对于下游决策可能是有用信息；在组合系统时，避免过早做出离散决策可能是有益的。像逻辑回归这样的概率分类器有四个组成部分：

> from a new input x to its correct class y ∈Y. It does this by learning to find features in these training sentences (perhaps words like “awesome” or “awful”). Probabilistic classifiers like logistic regression are classifiers that in addition to giving an answer (the class this observation is in), also give the probability of the observation being in the class. This distribution over the classes can be useful information for downstream decisions; avoiding making discrete decisions early on can be useful when combining systems. Probabilistic classifiers like logistic regression have four components:

- 输入的某种特征表示。对于每个输入观测样本 x(i)，这将是一个特征向量 [x1,x2,...,xn]。我们通常把输入 x(j) 的第 i 个特征记为 x(j) i ，有时简写为 xi，但我们也会看到记号 fi、fi(x)，或者在多分类情形下记为 fi(c,x)。
- 一个分类函数，它通过计算每个输出类别 yi 的概率 P(y = yi|x) 来得出估计的类别。我们将介绍用于分类的 sigmoid 和 softmax 工具。
- 一个我们在学习中想要优化的目标函数，通常涉及最小化对应于训练样本误差的损失函数。

> A feature representation of the input. For each input observation x(i), this will be a vector of features [x1,x2,...,xn]. We will generally refer to feature i for input x(j) as x(j) i , sometimes simplified as xi, but we will also see the notation fi, fi(x), or, for multiclass classification, fi(c,x).
> A classification function that computes the estimated class, by computing the probability P(y = yi|x) for each output class yi. We will introduce the sigmoid and softmax tools for classification.
> An objective function that we want to optimize for learning, usually involving minimizing a loss function corresponding to error on training examples.

我们将介绍交叉熵损失函数。

> We will introduce the cross-entropy loss function.

- 一个用于优化目标函数的算法。我们介绍随机梯度下降算法。

> An algorithm for optimizing the objective function. We introduce the stochastic gradient descent algorithm.

从最高层面看，逻辑回归，实际上任何概率机器

> At the highest level, logistic regression, and really any probabilistic machine
学习分类器，都有两个阶段

> learning classifier, has two phases
训练：我们使用随机梯度下降和交叉熵损失来训练系统（对逻辑回归而言，这意味着训练权重 w 和 b，下文将介绍）。测试：给定一个测试样本 x，我们计算每个输出类别 yi 的概率 P(y = yi|x)。然后，给定这个概率向量，我们返回概率较高的标签 y = 1 或 y = 0。

> training: We train the system (in the case of logistic regression that means training the weights w and b, introduced below) using stochastic gradient descent and the cross-entropy loss. test: Given a test example x we compute the probability P(y = yi|x) for each output class yi. Then, given this vector of probabilities, we return the higher probability label y = 1 or y = 0.

逻辑回归可用于将一个观测样本分类到两个类别中的一个

> Logistic regression can be used to classify an observation into one of two classes
（例如“正面情感”和“负面情感”），或分类到多个类别中的一个。

> (like ‘positive sentiment’ and ‘negative sentiment’), or into one of many classes.

由于两类情形的数学更简单，我们将在接下来几节中首先描述逻辑回归的这一特殊情况，从 sigmoid 函数开始，然后在 4.7 节转向用于多于两个类别的多项逻辑回归以及 softmax 函数的使用。

> Because the mathematics for the two-class case is simpler, we’ll first describe this special case of logistic regression in the next few sections, beginning with the sigmoid function, and then turn to multinomial logistic regression for more than two classes and the use of the softmax function in Section 4.7.

## 4.2 sigmoid 函数

> 4.2 The sigmoid function

二分类逻辑回归的目标是训练一个分类器，使其能对新的输入观测样本的类别做出二元判定。这里我们介绍将帮助我们做出这一判定的 sigmoid 分类器。

> The goal of binary logistic regression is to train a classifier that can make a binary decision about the class of a new input observation. Here we introduce the sigmoid classifier that will help us make this decision.

考虑单个输入观测样本 x，我们将用如下向量来表示它

> Consider a single input observation x, which we will represent by a vector of
特征 [x1,x2,...,xn] 来表示。（我们将在下一小节展示示例特征。）分类器输出 y 可以是 1（表示该观测样本属于该类），也可以是 0（表示该观测样本不属于该类）。我们想知道该观测样本属于该类的概率 P(y = 1|x)。所以也许判定是“正面情感”还是“负面情感”，特征是文档中单词的计数，P(y = 1|x) 是文档具有正面情感的概率，P(y = 0|x) 是文档具有负面情感的概率。

> features [x1,x2,...,xn]. (We’ll show sample features in the next subsection.) The classifier output y can be 1 (meaning the observation is a member of the class) or 0 (the observation is not a member of the class). We want to know the probability P(y = 1|x) that this observation is a member of the class. So perhaps the decision is “positive sentiment” versus “negative sentiment”, the features represent counts of words in a document, P(y = 1|x) is the probability that the document has positive sentiment, and P(y = 0|x) is the probability that the document has negative sentiment.

逻辑回归通过从训练集中学习一个向量来解决这一任务，该向量包含

> Logistic regression solves this task by learning, from a training set, a vector of
权重和一个偏置项。每个权重 wi 是一个实数，并与输入特征 xi 之一相关联。权重 wi 表示该输入特征对分类决策有多重要，它可以是正的（提供证据表明被分类的实例属于正类），也可以是负的（提供证据表明被分类的实例属于负类）。因此，在情感任务中我们可能预期单词 awesome 具有较高的正权重，而 abysmal 具有很负的权重。偏置项，也称为截距，是

> weights and a bias term. Each weight wi is a real number, and is associated with one of the input features xi. The weight wi represents how important that input feature is to the classification decision, and can be positive (providing evidence that the instance being classified belongs in the positive class) or negative (providing evidence that the instance being classified belongs in the negative class). Thus we might expect in a sentiment task the word awesome to have a high positive weight, and abysmal to have a very negative weight. The bias term, also called the intercept, is

> `bias term intercept`（偏置项 截距）

另一个实数，它被加到加权后的输入上。

> another real number that’s added to the weighted inputs.

要对一个测试实例做出判定——在我们于训练中学习到权重之后——

> To make a decision on a test instance—after we’ve learned the weights in training—
分类器首先用权重 wi 乘以每个 xi，对加权后的特征求和，再加上偏置项 b。得到的单个数字 z 表达了该类别的证据加权和。

> the classifier first multiplies each xi by its weight wi, sums up the weighted features, and adds the bias term b. The resulting single number z expresses the weighted sum of the evidence for the class.

n ! X
z = wixi +b (4.2)
在本书余下的部分，我们将使用点积记号来表示这类求和

> In the rest of the book we’ll represent such sums using the dot product notation

> i=1

> `dot product`（点积）

来自线性代数。两个向量 a 和 b 的点积写作 a ·b，是各向量对应元素乘积之和。（注意我们用粗体记号 b 表示向量。）因此下式与式 4.2 等价：

> from linear algebra. The dot product of two vectors a and b, written as a ·b, is the sum of the products of the corresponding elements of each vector. (Notice that we represent vectors using the boldface notation b). Thus the following is an equivalent formation to Eq. 4.2:

z = w ·x+b (4.3)
但请注意，式 4.3 中没有任何东西强制 z 成为一个合法的概率，即位于 0 和 1 之间。事实上，由于权重是实数值，输出甚至可能为负；z 的取值范围是 −∞到 ∞。

> But note that nothing in Eq. 4.3 forces z to be a legal probability, that is, to lie between 0 and 1. In fact, since weights are real-valued, the output might even be negative; z ranges from −∞to ∞.

为了得到概率，我们将 z 通过 sigmoid 函数 σ(z)。

> To create a probability, we’ll pass z through the sigmoid function, σ(z). The

> `sigmoid`

sigmoid 函数（因形状像字母 s 而得名）也称为 logistic 函数，逻辑回归由此得名。sigmoid 的方程如下，

> sigmoid function (named because it looks like an s) is also called the logistic function, and gives logistic regression its name. The sigmoid has the following equation,

> `logistic`

> `function`（函数）

如图 4.1 所示：

> shown graphically in Fig. 4.1:

1 1
σ(z) = 1+e−z = (4.4)
1+exp(−z)
（在本书余下的部分，我们将使用记号 exp(x) 来表示 ex。）sigmoid

> (For the rest of the book, we’ll use the notation exp(x) to mean ex.) The sigmoid
有许多优点；它接受一个实数值并将其映射到区间

> has a number of advantages; it takes a real-valued number and maps it into the range

![](images/04-logistic-regression/fig_p5_0.png)

*图 4.1 sigmoid 函数 σ(z) = 1+e−z 接受一个实数值并将其映射到区间 (0,1)。它在 0 附近近似线性，但离群值会被压缩向 0 或 1。*
*Figure 4.1 The sigmoid function σ(z) = 1+e−z takes a real value and maps it to the range(0,1). It is nearly linear around 0 but outlier values get squashed toward 0 or 1.*

(0,1)，这正是我们对于概率所需要的。由于它在 0 附近近似线性，但在两端趋于平坦，它倾向于将离群值压缩向 0 或 1。而且它是可微的，正如我们将在 4.15 节看到的那样，这将对学习很有帮助。

> (0,1), which is just what we want for a probability. Because it is nearly linear around 0 but flattens toward the ends, it tends to squash outlier values toward 0 or 1. And it’s differentiable, which as we’ll see in Section 4.15 will be handy for learning.

我们就要完成了。如果我们对加权特征之和应用 sigmoid，

> We’re almost there. If we apply the sigmoid to the sum of the weighted features,
就得到一个介于 0 和 1 之间的数字。要把它变成概率，我们只需确保两种情况 P(y = 1) 和 P(y = 0) 之和为 1。我们可以这样做：

> we get a number between 0 and 1. To make it a probability, we just need to make sure that the two cases, P(y = 1) and P(y = 0), sum to 1. We can do this as follows:

P(y = 1) = σ(w ·x+b)
1
= 1+exp(−(w ·x+b))
P(y = 0) = 1−σ(w ·x+b)
1
= 1−
1+exp(−(w ·x+b)) exp(−(w ·x+b))
= 1+exp(−(w ·x+b)) (4.5)
sigmoid 函数具有如下性质

> The sigmoid function has the property
1−σ(x) = σ(−x) (4.6)
因此我们也可以把 P(y = 0) 表示为 σ(−(w ·x+b))。

> so we could also have expressed P(y = 0) as σ(−(w ·x+b)).

最后，有两点术语说明。第一，sigmoid 函数的输入，即

> Finally, two terminological points. First, the input to the sigmoid function, the
式 4.3 中的分数 z = w · x + b，通常称为 logit。这是因为 logit

> score z = w · x + b from Eq. 4.3, is often called the logit. This is because the logit

> `logit`

函数是 sigmoid 的反函数。logit 函数是几率比的对数

> function is the inverse of the sigmoid. The logit function is the log of the odds ratio

> p

$$_{1 - p} ^{p} :$$

logit(p) = σ−1(p) = ln p (4.7)
1−p
用 logit 一词来指代 z，是在提醒我们：借助 sigmoid 把 z（取值范围从 −∞ 到 ∞）转换为概率时，我们实际上是在把 z 隐含地解释为不只是任意一个实数值，而是具体地解释为对数几率。

> Using the term logit for z is a way of reminding us that by using the sigmoid to turn z (which ranges from −∞to ∞) into a probability, we are implicitly interpreting z as not just any real-valued number, but as specifically a log odds.

其次，对于二分类而言，方便起见，我们把如下函数的输出

> Second, for binary classification it will be convenient to refer to the output of
即 sigmoid 函数 σ(w·x+b)，它计算的是 P(y = 1)，记作 ŷ。我们把这个符号读作 y hat。因此我们用 ŷ 表示“输入观测样本

> the sigmoid function σ(w·x+b) which is computing P(y = 1), as ˆy. We pronounce this symbol as y hat. We thus use ˆy to mean “the probability of the input observa-

> `y hat`

ŷ 具有正类别的概率”。当我们在 4.7 节引入多项或 softmax 逻辑

> ˆy tion having the positive class”. When we introduce multinomial or softmax logistic
回归时，我们会引入 ŷ 的一种扩展形式，它是一个在所有输出类别上的概率向量；但对于二分类，我们只保留一个标量概率，因为我们知道缺失的概率 P(y = 0) 总可以按 1−P(y = 1) 计算出来。

> regression in Section 4.7, we will introduce an extension of ˆy that will be a vector of probabilities over all the output classes, but for binary classification we just keep one scalar probability, knowing that we can always compute the missing probability P(y = 0) as 1−P(y = 1).

## 4.3 用逻辑回归进行分类

> 4.3 Classification with Logistic Regression

因此，上一节的 sigmoid 函数为我们提供了一种方法：取一个实例 x，计算概率 P(y = 1|x)。

> The sigmoid function from the prior section thus gives us a way to take an instance x and compute the probability P(y = 1|x).

我们如何决定给一个测试实例 x 赋予哪个类别？对于

> How do we make a decision about which class to apply to a test instance x? For
给定的 x，如果概率 P(y = 1|x) 大于 .5，我们就判为 yes，否则判为 no。

> a given x, we say yes if the probability P(y = 1|x) is more than .5, and no otherwise.

> `decision boundary`（决策边界）

我们把 .5 称为决策边界：

> We call .5 the decision boundary:

1 if P(y = 1|x) > 0.5
decision(x) = 0 otherwise
下面来看一些把逻辑回归用作语言任务分类器的例子。

> Let’s have some examples of applying logistic regression as a classifier for language tasks.

### 4.3.1 情感分类

> 4.3.1 Sentiment Classification

假设我们正在对影评文本进行二分类情感分类，想要知道应给一篇评论文档 doc 赋予情感类别 + 还是 −。我们将每个输入观测样本用下表所示的 6 个特征 x1 ...x6 来表示；图 4.2 显示了一个样本迷你测试文档中的特征。

> Suppose we are doing binary sentiment classification on movie review text, and we would like to know whether to assign the sentiment class + or −to a review document doc. We’ll represent each input observation by the 6 features x1 ...x6 of the input shown in the following table; Fig. 4.2 shows features in a sample mini test document.

变量 定义 图 4.2 中的取值 x1 count(正向词典词 ∈ doc) 3 x2 count(负向词典词 ∈ doc)  2

> Var Definition Value in Fig. 4.2 x1 count(positive lexicon words ∈doc) 3 x2 count(negative lexicon words ∈doc)  2
1 if “no” ∈doc
x3 0 否则 1 x4 count(第一人称和第二人称代词 ∈ doc)  1 if “!” ∈doc 3 x5 0 否则 0 x6 ln(文档的词+标点计数) ln(66) = 4.19

> x3 0 otherwise 1 x4 count(1st and 2nd pronouns ∈doc)  1 if “!” ∈doc 3 x5 0 otherwise 0 x6 ln(word+punctuation count of doc) ln(66) = 4.19

![](images/04-logistic-regression/fig_p6_0.png)

*图 4.2 一个样本迷你测试文档，展示了向量 x 中抽取出的特征。*
*Figure 4.2 A sample mini test document showing the extracted features in the vector x.*

我们暂时假设已经为以下每一个

> Let’s assume for the moment that we’ve already learned a real-valued weight for
特征都学得了一个实数值权重，并且对应于这 6 个特征的 6 个权重为 [2.5,−5.0,−1.2,0.5,2.0,0.7]，而 b = 0.1。（我们将在下一节讨论权重是如何学得的。）例如，权重 w1 表明正向词典词（great、nice、enjoyable 等）的数量对判定为正面情感有多重要，而 w2 则告诉我们负向词典词的重要性。注意 w1 = 2.5 为正，而 w2 = −5.0，这意味着负面词与判定为正面情感呈负相关，并且其重要性大约是正面词的两倍。

> each of these features, and that the 6 weights corresponding to the 6 features are[2.5,−5.0,−1.2,0.5,2.0,0.7], while b = 0.1. (We’ll discuss in the next section how the weights are learned.) The weight w1, for example, indicates how important the number of positive lexicon words (great, nice, enjoyable, etc.) is to a positive sentiment decision, while w2 tells us the importance of negative lexicon words. Note that w1 = 2.5 is positive, while w2 = −5.0, meaning that negative words are negatively associated with a positive sentiment decision, and are about twice as important as positive words.

给定这 6 个特征和输入评论 x，可以用式 4.5 计算 P(+|x) 和 P(−|x)：

> Given these 6 features and the input review x, P(+|x) and P(−|x) can be computed using Eq. 4.5:

P(+|x) = P(y = 1|x) = σ(w ·x+b)
= σ([2.5,−5.0,−1.2,0.5,2.0,0.7]·[3,2,1,3,0,4.19]+0.1)= σ(.833)
= 0.70 (4.8)
P(−|x) = P(y = 0|x) = 1−σ(w ·x+b)
= 0.30

### 4.3.2 其他分类任务与特征

> 4.3.2 Other classification tasks and features

逻辑回归被应用于各种各样的 NLP 任务，输入的任意一种属性

> Logistic regression is applied to all sorts of NLP tasks, and any property of the input

> `period`（句点）

都可以作为特征。考虑句点消歧任务：判断一个句点

> can be a feature. Consider the task of period disambiguation: deciding if a period

> `disambiguation`（消歧）

是句子的结尾还是单词的一部分，即把每个句点分类为两个类别之一：EOS（句末）和非 EOS。我们可能使用如下面的 x1 这样的特征，表示当前词是小写，也许赋予正的权重。或者使用一个特征，表示当前词出现在我们的缩写词典中（“Prof.”），也许赋予负的权重。特征还可以表示属性的组合。例如，一个位于全大写单词之后的句点很可能是 EOS；但如果该词本身是 St.，且前一个词是大写开头的，那么这个句点很可能是街道名之后 street 一词的缩写的一部分。

> is the end of a sentence or part of a word, by classifying each period into one of two classes, EOS (end-of-sentence) and not-EOS. We might use features like x1 below expressing that the current word is lower case, perhaps with a positive weight. Or a feature expressing that the current word is in our abbreviations dictionary (“Prof.”), perhaps with a negative weight. A feature can also express a combination of properties. For example a period following a full upper case word is likely to be an EOS, but if the word itself is St. and the previous word is capitalized then the period is likely part of a shortening of the word street following a street name.

1 if “Case(wi) = Lower”

x1 = 0 otherwise
1 if “wi ∈AcronymDict”

x2 = 0 otherwise
1 if “wi = St. & Case(wi−1) = Upper”

x3 = 0 otherwise
设计特征与学习特征：在经典模型中，特征由人工设计，人们出于语言学直觉并参照文献来审视训练集，从而手工设计特征，并辅以对系统早期版本的训练集做错误分析所获得的洞见

> Designing versus learning features: In classic models, features are designed by hand by examining the training set with an eye to linguistic intuitions and literature, supplemented by insights from error analysis on the training set of an early version

> `feature`（特征）

的早期版本。我们还可以考虑特征交互，即那些由更基本的特征组合而成的复杂特征，

> of a system. We can also consider feature interactions, complex features that are

> `interactions`（交互）

更基本特征的组合。上文我们看到过用于句点消歧的这样一个特征：如果前一个词首字母大写，那么单词 St. 上的句点就不太可能是句子的结尾。特征可以自动创建

> combinations of more primitive features. We saw such a feature for period disambiguation above, where a period on the word St. was less likely to be the end of the sentence if the previous word was capitalized. Features can be created automatically

> `feature`（特征）

通过特征模板来实现，模板是特征的抽象规格说明。例如，一个 bigram

> via feature templates, abstract specifications of features. For example a bigram

> `templates`（模板）

用于句点消歧的模板可能会为训练集中出现在句点之前的每一对词创建一个特征。因此特征空间是稀疏的，因为我们只需在那个 n-gram 出现在训练集该位置时才创建一个特征。特征通常是根据字符串描述做哈希生成的。用户把某个特征描述为“bigram(American breakfast)”，该描述会被哈希成一个唯一的整数 i，这个整数就成为特征编号 fi。

> template for period disambiguation might create a feature for every pair of words that occurs before a period in the training set. Thus the feature space is sparse, since we only have to create a feature if that n-gram exists in that position in the training set. The feature is generally created as a hash from the string descriptions. A user description of a feature as, “bigram(American breakfast)” is hashed into a unique integer i that becomes the feature number fi.

从上一段可以清楚地看出，手工设计特征需要大量人力。因此，近期的 NLP 系统避免使用人工设计的特征，转而关注表示学习：以无监督方式从输入中自动学习特征的方法。我们将在第 5 章和第 6 章介绍表示学习的方法。

> It should be clear from the prior paragraph that designing features by hand requires extensive human effort. For this reason, recent NLP systems avoid handdesigned features and instead focus on representation learning: ways to learn fea- tures automatically in an unsupervised way from the input. We’ll introduce methods for representation learning in Chapter 5 and Chapter 6.

缩放输入特征：当不同的输入特征具有差别极大的取值范围时，通常会对它们重新缩放，使它们的取值范围具有可比性。我们通过对输入值做中心化来进行标准化，使其均值为零、标准

> Scaling input features: When different input features have extremely different ranges of values, it’s common to rescale them so they have comparable ranges. We standardize input values by centering them to result in a zero mean and a standard

> `standardize z-score`（标准化 z 分数）

差为一（这种变换有时称为 z 分数）。也就是说，如果

> deviation of one (this transformation is sometimes called the z-score). That is, if
µi 是特征 xi 在输入数据集中 m 个观测样本上的取值均值，σi 是特征 xi 在输入数据集上的取值标准差（注意这不是 sigmoid），那么我们可以把每个特征 xi 替换为一个新特征 x′

> µi is the mean of the values of feature xi across the m observations in the input dataset, and σi is the standard deviation of the values of features xi across the input dataset (note it’s not the sigmoid), we can replace each feature xi by a new feature x′
计算如下：

> computed as follows:

> i

v u
µi = 1 X t 1 u X  2
x(j) σi = x(j) −µi
m m
i = xi −µi x′ (4.9)

> m m

> i i

> j=1 j=1

$$σ _{i}$$

另一种做法是，把输入特征的取值归一化到 0 与 1 之间：

> Alternatively, we can normalize the input features values to lie between 0 and 1:

> `normalize`（归一化）

xi −min(xi)

$$x _{i} ^{′}$$

i = max(xi)−min(xi)
在跨特征比较取值时，具有可比取值范围的输入数据是很有用的。数据缩放在大规模神经网络中尤为重要，因为它有助于加快梯度下降。

> Having input data with comparable range is useful when comparing values across features. Data scaling is especially important in large neural networks, since it helps speed up gradient descent.

自然语言数据中另一种非常常见的缩放方式是对数变换，

> Another very common type of scaling for natural language data is to take logs,
例如当输入是词频计数、bigram 计数，或任何其他服从 Zipf 分布的数值时。

> for example when inputs are word counts, or bigram counts, or anything else that follows a Zipfian distribution.

### 4.3.3 一次处理多个样本

> 4.3.3 Processing many examples at once

前面展示的逻辑回归方程是针对单个样本的。但在实践中，我们当然希望用许多样本来处理整个测试集。假设我们有一个由 m 个测试样本组成的测试集，希望对其中的每一个样本进行分类。我们将继续沿用第 94 页的记号，其中括号中的上标表示某个数据集（训练集或测试集）中样本的索引。因此在这种情况下，每个测试样本 x(i) 都有一个特征向量 x(i)，1 ≤i ≤m。（和通常一样，我们用粗体表示向量和矩阵。）

> We’ve shown the equations for logistic regression for a single example. But in practice we’ll of course want to process an entire test set with many examples. Let’s suppose we have a test set consisting of m test examples each of which we’d like to classify. We’ll continue to use the notation from page 94, in which a superscript value in parentheses refers to the example index in some set of data (either for training or for test). So in this case each test example x(i) has a feature vector x(i), 1 ≤i ≤m. (As usual, we’ll represent vectors and matrices in bold.)
计算 ˆy(i)（我们用这个符号表示 P(y(i) = 1)，也就是输入 x(i) 的输出取值为 1 的概率）的一种方式，就是用 for 循环一次计算一个测试样本：

> One way to compute ˆy(i) (which is how we refer to P(y(i) = 1), i.e., the probability that the output for input x(i) has the value 1), is just to have a for-loop and compute each test example one at a time:

$$\text{foreach} x ^{( i )} \text{in input} [ x ^{( 1 )} , x ^{( 2 )} ,..., x ^{( m )} ]$$

$$y ˆ ^{( i )} = P ( y ^{( i )} = 1 ) = σ ( w \cdot x ^{( i )} + b )$$

那么，对于前 3 个测试样例，我们将按如下方式分别计算预测输出概率：

> For the first 3 test examples, then, we would be separately computing the predicted output probability as follows:

ˆy(1) = P(y(1) = 1|x(1)) = σ(w ·x(1) +b)ˆy(2) = P(y(2) = 1|x(2)) = σ(w ·x(2) +b)ˆy(3) = P(y(3) = 1|x(3)) = σ(w ·x(3) +b) 但事实证明，我们可以对原方程 Eq. 4.5 稍作修改，从而更高效地完成这一计算。我们将使用矩阵运算，用一次矩阵操作就为所有样例分配类别！

> ˆy(1) = P(y(1) = 1|x(1)) = σ(w ·x(1) +b)ˆy(2) = P(y(2) = 1|x(2)) = σ(w ·x(2) +b)ˆy(3) = P(y(3) = 1|x(3)) = σ(w ·x(3) +b) But it turns out that we can slightly modify our original equation Eq. 4.5 to do this much more efficiently. We’ll use matrix arithmetic to assign a class to all the examples with one matrix operation!

首先，我们将把每个输入 x 的所有输入特征向量打包成一个单一的输入

> First, we’ll pack all the input feature vectors for each input x into a single input
矩阵 X，其中第 i 行是一个行向量，由输入样例 x(i) 的特征向量（即向量 x(i)）构成。假设每个样例有 f 个特征和权重，那么 X 将是一个形状为 [m× f] 的矩阵，如下所示：

> matrix X, where each row i is a row vector consisting of the feature vector for input example x(i) (i.e., the vector x(i)). Assuming each example has f features and weights, X will therefore be a matrix of shape [m× f], as follows:

x(1) x(1) ... x(1)
x(2) x(2) ... x(2)
X = (4.12)

> 1 2 f

> 1 2 f

$$x _{1} ^{( 3 )} x _{2} ^{( 3 )} ... x ^{( 3 )} _{f}$$

> 1 2 f

...

现在，如果我们引入 b 作为长度为 m 的向量，它由标量偏置

> Now if we introduce b as a vector of length m which consists of the scalar bias
项 b 重复 m 次构成，b = [b,b,...,b]，并将 ˆy = [ˆy(1), ˆy(2)..., ˆy(m)] 表示为输出向量（对于每个输入 x(i) 及其特征向量 x(i)，都有一个标量 ˆy(i) = P(y(i) = 1)），同时把权重向量 w 表示为列向量，那么我们就能通过一次矩阵乘法和一次加法计算出所有输出：

> term b repeated m times, b = [b,b,...,b], and ˆy = [ˆy(1), ˆy(2)..., ˆy(m)] as the vector of outputs (one scalar ˆy(i) = P(y(i) = 1) for each input x(i) and its feature vector x(i)), and represent the weight vector w as a column vector, we can compute all the outputs with a single matrix multiplication and one addition:

ˆy = σ(Xw +b) (4.13)
这里我们对向量逐元素地应用 σ 函数，因此 σ[z1,z2,z3] = [σ(z1),σ(z2),σ(z3)]。

> We apply the σ function here to a vector element-wise, so σ[z1,z2,z3] = [σ(z1),σ(z2),σ(z3)].

你应该能确信，Eq. 4.13 计算出的结果与 Eq. 4.11 中的 for 循环相同。例如 ˆy(1)，即输出向量 ˆy 的第一个元素，将正确地等于：

> You should convince yourself that Eq. 4.13 computes the same thing as our for-loop in Eq. 4.11. For example ˆy(1), the first entry of the output vector ˆy, will correctly be:

ˆy(1) = σ [x(1) 1 ,x(1) 2 ,...,x(1) f ]·[w1,w2,...,wf ]+b (4.14)
注意，我们必须把 X 和 w 从它们在 Eq. 4.5 中出现的顺序重新排列，才能使乘法正确进行。下面再次给出 Eq. 4.13，并标注出各部分的形状：

> Note that we had to reorder X and w from the order they appeared in Eq. 4.5 to make the multiplications come out properly. Here is Eq. 4.13 again with the shapes shown:

ˆy = σ(X w + b)
(m×1) (m× f) (f ×1) (m×1) (4.15)
现代编译器和计算硬件能够非常高效地计算这一矩阵运算，使计算速度快得多，这在非常大的数据集上训练或测试时变得十分重要。

> Modern compilers and compute hardware can compute this matrix operation very efficiently, making the computation much faster, which becomes important when training or testing on very large datasets.

顺便提一下，我们本可以让 X 和 w 保持原来的顺序（即

> Note by the way that we could have kept X and w in the original order (as
ˆy = σ(wX + b)），前提是我们选择把 X 定义为一个由列向量组成的矩阵（每个输入样例对应一个向量），而不是行向量，这样它的形状就是 [f ×m]。但我们习惯上将输入表示为行。

> ˆy = σ(wX + b)) if we had chosen to define X differently as a matrix of column vectors, one vector for each input example, instead of row vectors, and then it would have shape [f ×m]. But we conventionally represent inputs as rows.

## 4.4 逻辑回归中的学习

> 4.4 Learning in Logistic Regression

模型的参数，即权重 w 和偏置 b，是如何学习得到的？二分类逻辑回归是有监督分类的一个实例，其中我们知道每个观测样本 x 的正确标签 y（0 或 1）。系统通过 Eq. 4.5 产生的是 ˆy，即系统给出的 y 为 1 的概率，我们可以把它看作对真实 y（为 1 或 0）的估计。我们希望学到这样的参数（即 w 和 b），使每个训练观测样本的概率值 ˆy 尽可能接近真实的 y。也就是说，如果 y 为 1，那么我们希望系统的估计 ˆy = P(y = 1) 很高，即尽可能接近 1。如果 y 实际上为 0，那么我们希望系统的估计 ˆy = P(y = 1) 很低，即尽可能接近 0。

> How are the parameters of the model, the weights w and bias b, learned? Binary logistic regression is an instance of supervised classification in which we know the correct label y (either 0 or 1) for each observation x. What the system produces via Eq. 4.5 is ˆy, the system’s probability of y being 1, which we can think of an estimate of the true y (which is either 1 or 0). We want to learn parameters (meaning w and b) that make the probability value ˆy for each training observation as close as possible to the true y. That is, if y is 1, then we want the system’s estimate ˆy = P(y = 1) to be high, i.e. as close to 1 as possible. If y is in fact 0, then we want the system’s estimate ˆy = P(y = 1) to be low, i.e. as close to 0 as possible.

这需要两个组成部分，我们在引言中已经预先提及过。

> This requires two components that we foreshadowed in the introduction to the

第一个是一种度量，用来衡量 ˆy（系统对观测样本属于正类的概率的估计）与真实金标准标签 y 有多接近。我们通常不度量相似度，而是讨论它的反面：系统输出与金标准输出之间的距离，并把这一距离称为损失函数或

> chapter. The first is a metric for how close ˆy (the system’s estimate of the probability that the observation is in the positive class) is to the true gold label y. Rather than measure similarity, we usually talk about the opposite of this: the distance between the system output and the gold output, and we call this distance the loss function or

> `loss`（损失）

代价函数。在下一节中，我们将介绍一种常用于逻辑回归以及神经网络的损失函数，即交叉熵损失。

> the cost function. In the next section we’ll introduce the loss function that is commonly used for logistic regression and also for neural networks, the cross-entropy loss.

我们需要的第二样东西是一种优化算法，用于迭代地更新

> The second thing we need is an optimization algorithm for iteratively updating
权重，从而最小化这一损失函数。用于此目的的标准算法是梯度下降；我们将在下一节介绍随机梯度下降算法。

> the weights so as to minimize this loss function. The standard algorithm for this is gradient descent; we’ll introduce the stochastic gradient descent algorithm in the following section.

我们将在接下来的两节中，针对更简单的二分类逻辑回归情形描述这些算法，然后在 4.8 节转向多项逻辑回归。

> We’ll describe these algorithms for the simpler case of binary logistic regression in the next two sections, and then turn to multinomial logistic regression in Section 4.8.

## 4.5 交叉熵损失函数

> 4.5 The cross-entropy loss function

我们需要一个损失函数，对于观测样本 x，它表达分类器输出（ˆy = σ(w · x + b)）与正确输出（y，取值为 0 或 1）有多接近。回想一下，ˆy 表示分类器赋予观测样本 x 属于正类 1 的概率。因此 ˆy 和 y 表达的都是概率，但 y 总是 0 或 1，而 ˆy 还可以介于两者之间。我们称这一损失或距离的度量为：

> We need a loss function that expresses, for an observation x, how close the classifier output (ˆy = σ(w · x + b)) is to the correct output (y, which is 0 or 1). Recall thatˆy expresses the probability that the classifier assigns to observation x being in the positive class 1. So both ˆy and y express probabilities, but y is always 0 or 1 while ˆy can also lie in between. We’ll call this measure of loss or distance:

L(ˆy,y) = How much ˆy differs from the true y (4.16)
我们通过一个损失函数来实现这一点，它偏好使训练样例的正确类别标签具有更高的可能性。这称为条件最大似然估计：我们选择参数 w,b，使得在给定观测样本 x 的情况下，训练数据中真实 y 标签的对数概率最大化。由此得到的损失

> We do this via a loss function that prefers the correct class labels of the training examples to be more likely. This is called conditional maximum likelihood estimation: we choose the parameters w,b that maximize the log probability of the true y labels in the training data given the observations x. The resulting loss

> `cross-entropy loss`（交叉熵损失）

函数即负对数似然损失，通常称为交叉熵损失。

> function is the negative log likelihood loss, generally called the cross-entropy loss.

我们来推导这个损失函数，将其应用于单个观测样本 x。我们希望

> Let’s derive this loss function, applied to a single observation x. We’d like to
学习权重，使正确标签的概率 p(y|x) 最大化。由于只有两个离散结果（1 或 0），这是一个伯努利分布，我们可以把分类器对单个观测样本给出的概率 p(y|x) 表示如下（注意，若 y = 1，式 4.17 简化为 ˆy；若 y = 0，式 4.17 简化为 1−ˆy）：

> learn weights that maximize the probability of the correct label p(y|x). Since there are only two discrete outcomes (1 or 0), this is a Bernoulli distribution, and we can express the probability p(y|x) that our classifier produces for one observation as the following (keeping in mind that if y = 1, Eq. 4.17 simplifies to ˆy; if y = 0, Eq. 4.17 simplifies to 1−ˆy):

$$p ( y | x ) = y ˆ ^{y} ( 1 - y ˆ ) ^{1 - y}$$

现在我们对两边取对数。这在数学上会很方便，而且不会带来任何损失；使概率最大化的取值，同样会使概率的对数最大化：

> Now we take the log of both sides. This will turn out to be handy mathematically, and doesn’t hurt us; whatever values maximize a probability will also maximize the log of the probability:

ˆyy (1−ˆy)1−y
log p(y|x) = log
= ylog ˆy+(1−y)log(1−ˆy) 式 4.18 描述了一个应当被最大化的对数似然。为了把它变成损失函数（即我们需要最小化的东西），我们只需将式 4.18 的符号取反。结果就是交叉熵损失 LCE：

> = ylog ˆy+(1−y)log(1−ˆy) Eq. 4.18 describes a log likelihood that should be maximized. In order to turn this into a loss function (something that we need to minimize), we’ll just flip the sign on Eq. 4.18. The result is the cross-entropy loss LCE:

$$L _{\text{CE}} ( y ˆ , y ) = - \text{log} p ( y | x ) = - [ y \text{log ˆ} y +( 1 - y ) \text{log} ( 1 - y ˆ )]$$

最后，我们可以代入 ˆy = σ(w ·x+b) 的定义：

> Finally, we can plug in the definition of ˆy = σ(w ·x+b):

$$L _{\text{CE}} ( y ˆ , y ) = - [ y \text{log} σ ( w \cdot x + b )+( 1 - y ) \text{log} ( 1 - σ ( w \cdot x + b ))]$$

让我们看看这个损失函数对图 4.2 中的例子是否表现正确。我们希望当模型的估计接近正确时损失更小，当模型感到困惑时损失更大。因此，先假设图 4.2 中情感示例的正确金标准标签为正面，即 y = 1。此时我们的模型表现良好，因为由式 4.8 可知，它确实给该示例为正面赋予了比负面更高的概率（.70 对 .30）。如果把 σ(w ·x+b) = .70 和 y = 1 代入式 4.20，等式右边会消失，从而得到如下损失（当未指定底数时，我们用 log 表示自然对数）：

> Let’s see if this loss function does the right thing for our example from Fig. 4.2. We want the loss to be smaller if the model’s estimate is close to correct, and bigger if the model is confused. So first let’s suppose the correct gold label for the sentiment example in Fig. 4.2 is positive, i.e., y = 1. In this case our model is doing well, since from Eq. 4.8 it indeed gave the example a higher probability of being positive (.70) than negative (.30). If we plug σ(w ·x+b) = .70 and y = 1 into Eq. 4.20, the right side of the equation drops out, leading to the following loss (we’ll use log to mean natural log when the base is not specified):

$$L _{\text{CE}} ( y ˆ , y ) = - [ y \text{log} σ ( w \cdot x + b )+( 1 - y ) \text{log} ( 1 - σ ( w \cdot x + b ))]$$

= −[logσ(w ·x+b)]= −log(.70)= .36
相比之下，我们换一种假设，设想图 4.2 中的示例实际上是负面的，即 y = 0（也许评论者接着写道：“但归根结底，这部电影糟透了！我求你别去看！”）。此时我们的模型感到困惑，我们希望损失更高。现在，如果把 y = 0 以及由式 4.8 得到的 1−σ(w ·x+b) = .30 代入式 4.20，等式左边会消失：

> By contrast, let’s pretend instead that the example in Fig. 4.2 was actually negative, i.e., y = 0 (perhaps the reviewer went on to say “But bottom line, the movie is terrible! I beg you not to see it!”). In this case our model is confused and we’d want the loss to be higher. Now if we plug y = 0 and 1−σ(w ·x+b) = .30 from Eq. 4.8 into Eq. 4.20, the left side of the equation drops out:

$$L _{\text{CE}} ( y ˆ , y ) = - [ y \text{log} σ ( w \cdot x + b )+( 1 - y ) \text{log} ( 1 - σ ( w \cdot x + b ))]$$

= −[log(1−σ(w ·x+b))]= −log(.30)= 1.2
果不其然，预测正确标签的损失（.36）小于预测错误标签的损失（1.2）。

> Sure enough, the loss for predicting the correct label (.36) is less than the loss for predicting the incorrect label (1.2).

为什么最小化这个负对数概率就能达到我们的目的？一个完美的

> Why does minimizing this negative log probability do what we want? A perfect
分类器会把概率 1 赋予正确结果（y = 1 或 y = 0），把概率 0 赋予错误结果。这意味着，若 y 等于 1，ˆy 越大（越接近 1），分类器越好；ˆy 越小（越接近 0），分类器越差。反之，若 y 等于 0，则 1−ˆy 越大（越接近 1），分类器越好。ˆy 的负对数（若真实 y 等于 1）或 1 −ˆy 的负对数（若真实 y 等于 0）是一种方便的损失度量，因为它从 0（1 的负对数，无损失）一直延伸到无穷大（0 的负对数，无穷大损失）。这个损失函数还保证了：随着正确答案的概率被最大化，错误答案的概率被最小化；由于二者之和为 1，正确答案概率的任何增加都是以牺牲错误答案为代价的。它被称为交叉熵损失，因为式 4.19 也正是真实概率分布 y 与我们估计的分布 ˆy 之间交叉熵的公式。

> classifier would assign probability 1 to the correct outcome (y = 1 or y = 0) and probability 0 to the incorrect outcome. That means if y equals 1, the higher ˆy is (the closer it is to 1), the better the classifier; the lower ˆy is (the closer it is to 0), the worse the classifier. If y equals 0, instead, the higher 1−ˆy is (closer to 1), the better the classifier. The negative log of ˆy (if the true y equals 1) or 1 −ˆy (if the true y equals 0) is a convenient loss metric since it goes from 0 (negative log of 1, no loss) to infinity (negative log of 0, infinite loss). This loss function also ensures that as the probability of the correct answer is maximized, the probability of the incorrect answer is minimized; since the two sum to one, any increase in the probability of the correct answer is coming at the expense of the incorrect answer. It’s called the crossentropy loss, because Eq. 4.19 is also the formula for the cross-entropy between the true probability distribution y and our estimated distribution ˆy.

现在我们知道了要最小化的目标；下一节我们将看到如何

> Now we know what we want to minimize; in the next section, we’ll see how to
找到最小值。

> find the minimum.

## 4.6 梯度下降

> 4.6 Gradient Descent

梯度下降的目标是找到最优权重：最小化我们为模型定义的损失函数。在下面的式 4.21 中，我们将明确表示交叉熵损失函数 LCE 由权重参数化这一事实。在机器学习中，我们通常把正在学习的参数记作 θ；对于逻辑回归，θ = {w,b}。因此我们将把 ˆy(i) 表示为 f(x(i);θ)，以更明显地体现对 θ 的依赖。目标是找到使损失函数在所有示例上取平均后最小的那组权重：

> Our goal with gradient descent is to find the optimal weights: minimize the loss function we’ve defined for the model. In Eq. 4.21 below, we’ll explicitly represent the fact that the cross-entropy loss function LCE is parameterized by the weights. In machine learning in general we refer to the parameters being learned as θ; in the case of logistic regression θ = {w,b}. So we’ll represent ˆy(i) as f(x(i);θ) to make the dependence on θ more obvious. The goal is to find the set of weights which minimizes the loss function, averaged over all examples:

> m

ˆθ = argmin 1 X

$$L _{\text{CE}} ( f ( x ^{( i )} ; θ ) , y ^{( i )} )$$

m
我们该如何找到这个（或任意）损失函数的最小值？梯度下降是一种通过判断函数（在参数 θ 空间中）的斜率沿哪个方向上升最陡、然后朝相反方向移动来求函数最小值的方法。其直觉是：如果你在峡谷中徒步，想尽快下到谷底的河流，你可能会环顾四周各个方向，找到地面倾斜最陡的方向，然后朝那个方向下坡走去。

> How shall we find the minimum of this (or any) loss function? Gradient descent is a method that finds a minimum of a function by figuring out in which direction (in the space of the parameters θ) the function’s slope is rising the most steeply, and moving in the opposite direction. The intuition is that if you are hiking in a canyon and trying to descend most quickly down to the river at the bottom, you might look around yourself in all directions, find the direction where the ground is sloping the steepest, and walk downhill in that direction.

> θ i=1

对于逻辑回归，这个损失函数恰好是凸的。凸函数至多有一个最小值；不存在会让人陷进去的局部极小值，因此从任意点出发的梯度下降都保证能找到最小值。（相比之下，多层神经网络的损失是非凸的，在神经网络训练中梯度下降可能会陷入局部极小值，永远找不到全局最优解。）

> For logistic regression, this loss function is conveniently convex. A convex function has at most one minimum; there are no local minima to get stuck in, so gradient descent starting from any point is guaranteed to find the minimum. (By contrast, the loss for multi-layer neural networks is non-convex, and gradient descent may get stuck in local minima for neural network training and never find the global optimum.)

> `convex`（凸）

尽管该算法（以及梯度的概念）是为方向

> Although the algorithm (and the concept of gradient) are designed for direction
向量而设计的，但让我们先考察一种可视化情形：我们系统的参数只是一个标量 w，如图 4.3 所示。

> vectors, let’s first consider a visualization of the case where the parameter of our system is just a single scalar w, shown in Fig. 4.3.

给定 w 随机初始化为某个值 w1，并假设损失

> Given a random initialization of w at some value w1, and assuming the loss
函数 L 恰好具有图 4.3 中的形状，我们需要算法告诉我们：在下一次迭代中，为了到达最小值，我们应该向左移动（使 w2 小于 w1）还是向右移动（使 w2 大于 w1）。

> function L happened to have the shape in Fig. 4.3, we need the algorithm to tell us whether at the next iteration we should move left (making w2 smaller than w1) or right (making w2 bigger than w1) to reach the minimum.

梯度下降算法通过求梯度来回答这个问题

> The gradient descent algorithm answers this question by finding the gradient

> `gradient`（梯度）

损失函数在当前点的梯度，并朝相反方向移动。多元函数的梯度是一个指向函数增长最快方向的向量。梯度是斜率的多变量推广，因此对于像图 4.3 中那样的单变量函数，我们可以非正式地把梯度看作斜率。图 4.3 中的虚线显示了该假想损失函数在点 w = w1 处的斜率。你可以看到，这条虚线的斜率是负的。因此，为了找到最小值，梯度下降告诉我们朝相反方向走：让 w 朝正方向移动。

> of the loss function at the current point and moving in the opposite direction. The gradient of a function of many variables is a vector pointing in the direction of the greatest increase in a function. The gradient is a multi-variable generalization of the slope, so for a function of one variable like the one in Fig. 4.3, we can informally think of the gradient as the slope. The dotted line in Fig. 4.3 shows the slope of this hypothetical loss function at point w = w1. You can see that the slope of this dotted line is negative. Thus to find the minimum, gradient descent tells us to go in the opposite direction: moving w in a positive direction.

梯度下降中移动量的大小，等于

> The magnitude of the amount to move in gradient descent is the value of the
斜率 dwL(f(x;w),y) 乘以学习率 η 后的值。学习率越高（越快），

> slope dwL(f(x;w),y) weighted by a learning rate η. A higher (faster) learning

> d

> `learning rate`（学习率）

就意味着每一步都应把 w 移动得更多。我们对参数所做的改变，就是学习率乘以梯度（在单变量示例中即斜率）：

> rate means that we should move w more on each step. The change we make in our parameter is the learning rate times the gradient (or the slope, in our single-variable example):

wt+1 = wt −η d (4.22)
dwL(f(x;w),y)
现在，让我们把这种直觉从一个标量变量 w 的函数推广到多个

> Now let’s extend the intuition from a function of one scalar variable w to many

![](images/04-logistic-regression/fig_p13_0.png)

*图 4.3 迭代寻找该损失函数最小值的第一步：沿与函数斜率相反的方向移动 w。由于斜率为负，我们需要沿正方向（即向右）移动 w。这里用上标表示学习步骤，因此 w1 表示 w 的初始值（为 0），w2 表示第二步时的值，依此类推。*
*Figure 4.3 The first step in iteratively finding the minimum of this loss function, by moving w in the reverse direction from the slope of the function. Since the slope is negative, we need to move w in a positive direction, to the right. Here superscripts are used for learning steps, so w1 means the initial value of w (which is 0), w2 the value at the second step, and so on.*

个变量，因为我们不只是想向左或向右移动，而是想知道在 N 维空间（由构成 θ 的 N 个参数张成的空间）中应该往哪里移动。

> variables, because we don’t just want to move left or right, we want to know where in the N-dimensional space (of the N parameters that make up θ) we should move.

梯度正是这样一个向量；它表示在这 N 个维度上最陡斜率的各方向分量。如果我们只设想两个权重维度（比如一个权重 w 和一个偏置 b），梯度可能是一个具有两个正交分量的向量，每个分量都告诉我们地面在 w 维度和 b 维度上倾斜的程度。图 4.4 展示了在红点处取得的二维梯度向量值的可视化。

> The gradient is just such a vector; it expresses the directional components of the sharpest slope along each of those N dimensions. If we’re just imagining two weight dimensions (say for one weight w and one bias b), the gradient might be a vector with two orthogonal components, each of which tells us how much the ground slopes in the w dimension and in the b dimension. Fig. 4.4 shows a visualization of the value of a 2-dimensional gradient vector taken at the red point.

在实际的逻辑回归中，参数向量 w 的长度远不止 1 或

> In an actual logistic regression, the parameter vector w is much longer than 1 or
2，因为输入特征向量 x 可能相当长，我们需要为每个 xi 配一个权重 wi。对于 w 中的每个维度/变量 wi（再加上偏置 b），梯度都会有一个分量告诉我们在该变量方向上的斜率。在每个维度 wi 上，我们把斜率表示为损失函数的偏导数 ∂wi。本质上

> 2, since the input feature vector x can be quite long, and we need a weight wi for each xi. For each dimension/variable wi in w (plus the bias b), the gradient will have a component that tells us the slope with respect to that variable. In each dimension wi, we express the slope as a partial derivative ∂wi of the loss function. Essentially
我们是在问：“该变量 wi 的微小变化会对总损失函数 L 产生多大影响？”

> we’re asking: “How much would a small change in that variable wi influence the total loss function L?”

> ∂

那么，从形式上说，多变量函数 f 的梯度是一个向量，其中

> Formally, then, the gradient of a multi-variable function f is a vector in which

![](images/04-logistic-regression/fig_p13_1.png)

*图 4.4 在 w 和 b 两个维度上对红点处梯度向量的可视化，图中 x-y 平面内的红色箭头指向我们接下来要前往寻找的方向*
*Figure 4.4 Visualization of the gradient vector at the red point in two dimensions w and b, showing a red arrow in the x-y plane pointing in the direction we will go to look for the*

每个分量都表示 f 关于其中某个变量的偏导数。我们使用倒置的希腊字母 delta 符号 ∇ 表示梯度，并把 ˆy 表示为 f(x;θ)，以便更清楚地体现对 θ 的依赖：

> each component expresses the partial derivative of f with respect to one of the variables. We’ll use the inverted Greek delta symbol ∇to refer to the gradient, and represent ˆy as f(x;θ) to make the dependence on θ more obvious:

∂w1 L(f(x;θ),y)
∂w2 L(f(x;θ),y)
∇L(f(x;θ),y) = ... (4.23)

> ∂

> ∂

$$_{\partial w n} ^{\partial} L ( f ( x ; θ ) , y )$$

> ∂

$$_{\partial b} ^{\partial} L ( f ( x ; θ ) , y )$$

> ∂

因此，基于梯度更新 θ 的最终方程为

> The final equation for updating θ based on the gradient is thus

$$θ ^{t + 1} = θ ^{t} - η ∇ L ( f ( x ; θ ) , y )$$

### 4.6.1 逻辑回归的梯度

> 4.6.1 The Gradient for Logistic Regression

为了更新 θ，我们需要给出梯度 ∇L(f(x;θ),y) 的定义。回忆一下，对于逻辑回归，交叉熵损失函数为：

> In order to update θ, we need a definition for the gradient ∇L(f(x;θ),y). Recall that for logistic regression, the cross-entropy loss function is:

$$L _{\text{CE}} ( y ˆ , y ) = - [ y \text{log} σ ( w \cdot x + b )+( 1 - y ) \text{log} ( 1 - σ ( w \cdot x + b ))]$$

事实证明，该函数对单个观测向量 x 的导数就是式 4.26（感兴趣的读者可参阅第 4.15 节了解该公式的推导）：

> It turns out that the derivative of this function for one observation vector x is Eq. 4.26(the interested reader can see Section 4.15 for the derivation of this equation):

$$\partial L _{\text{CE}} ( y ˆ , y )$$

$$= [ σ ( w \cdot x + b ) - y ] x _{j}$$

$$\partial w _{j}$$

$$= ( y ˆ - y ) x _{j}$$

你有时也会看到该方程写成下面这种等价形式：

> You’ll also sometimes see this equation in the equivalent form:

$$\partial L _{\text{CE}} ( y ˆ , y )$$

$$= - ( y - y ˆ ) x _{j}$$

$$\partial w _{j}$$

请注意，在这些公式中，对单个权重 wj 的梯度表示一个非常直观的值：该观测样本的真实 y 与我们估计的 ŷ = σ(w · x + b) 之差，再乘以对应的输入值 x j。

> Note in these equations that the gradient with respect to a single weight wj represents a very intuitive value: the difference between the true y and our estimatedˆy = σ(w · x + b) for that observation, multiplied by the corresponding input value x j.

顺便说一句，我们还需要一个关于 b 的偏导数的表达式。

> By the way, we’ll also need a term for the partial derivative with respect to b.

结果如下：

> That turns out to be:

$$\partial L _{\text{CE}} ( y ˆ , y )$$

= σ(w ·x+b)−y
∂b
= ˆy−y (4.28)

### 4.6.2 随机梯度下降算法

> 4.6.2 The Stochastic Gradient Descent Algorithm

随机梯度下降是一种在线算法，它在每个训练样本之后计算损失函数的梯度，并把 θ 朝正确的方向（梯度的反方向）微调，从而最小化损失函数。（“在线算法”是指逐个样本处理输入的算法，而不是等到看见整个输入之后才处理。）随机梯度下降之所以被称为随机的，是因为它一次只选择一个随机样本；我们将在 4.6.4 节讨论一次批处理多个样本的其他梯度下降版本。图 4.5 给出了该算法。

> Stochastic gradient descent is an online algorithm that minimizes the loss function by computing its gradient after each training example, and nudging θ in the right direction (the opposite direction of the gradient). (An “online algorithm” is one that processes its input example by example, rather than waiting until it sees the entire input.) Stochastic gradient descent is called stochastic because it chooses a single random example at a time; in Section 4.6.4 we’ll discuss other versions of gradient descent that batch many examples at once. Fig. 4.5 shows the algorithm.

![](images/04-logistic-regression/fig_p15_0.png)

*图 4.5 随机梯度下降算法。第 1 步（计算损失）主要用于报告我们在当前元组上的表现如何；计算梯度并不需要先计算损失。算法可以在收敛时（梯度范数 < ϵ 时）终止，也可以在进展停止时（例如损失在留出集上开始上升时）终止。对于逻辑回归，权重初始化为 0，而对于神经网络，权重初始化为小的随机值，我们将在第 6 章看到这一点。*
*Figure 4.5 The stochastic gradient descent algorithm. Step 1 (computing the loss) is used mainly to report how well we are doing on the current tuple; we don’t need to compute the loss in order to compute the gradient. The algorithm can terminate when it converges (when the gradient norm < ϵ), or when progress halts (for example when the loss starts going up on a held-out set). Weights are initialized to 0 for logistic regression, but to small random values for neural networks, as we’ll see in Chapter 6.*

学习率 η 是一个必须调整的超参数。如果它太高，

> The learning rate η is a hyperparameter that must be adjusted. If it’s too high,

> `hyperparameter`（超参数）

学习器就会迈出过大的步子，越过损失函数的最小值。如果它太低，学习器迈出的步子就会太小，需要很长时间才能到达最小值。常见的做法是先使用较高的学习率再慢慢降低它，使它成为训练迭代次数 k 的函数；记号 ηk 可以表示第 k 次迭代时学习率的取值。

> the learner will take steps that are too large, overshooting the minimum of the loss function. If it’s too low, the learner will take steps that are too small, and take too long to get to the minimum. It is common to start with a higher learning rate and then slowly decrease it, so that it is a function of the iteration k of training; the notationηk can be used to mean the value of the learning rate at iteration k.

我们将在第 6 章更详细地讨论超参数，但简而言之，它们是

> We’ll discuss hyperparameters in more detail in Chapter 6, but in short, they are
任何机器学习模型的一类特殊参数。与由算法从训练集中学习得到的模型常规参数（如 w 和 b 这样的权重）不同，超参数是由算法设计者选择的特殊参数，它们影响算法的工作方式。

> a special kind of parameter for any machine learning model. Unlike regular parameters of a model (weights like w and b), which are learned by the algorithm from the training set, hyperparameters are special parameters chosen by the algorithm designer that affect how the algorithm works.

### 4.6.3 一个示例的完整推演

> 4.6.3 Working Through an Example

让我们完整走过梯度下降算法的一步。我们使用图 4.2 中示例的简化版本：它看到一个观测样本 x，其正确值为 y = 1（这是一条正面评论），特征向量 x = [x1,x2] 由以下两个特征组成：

> Let’s walk through a single step of the gradient descent algorithm. We’ll use a simplified version of the example in Fig. 4.2 as it sees a single observation x, whose correct value is y = 1 (this is a positive review), and with a feature vector x = [x1,x2] consisting of these two features:

x1 = 3（正面词典词的数量） x2 = 2（负面词典词的数量）

> x1 = 3 (count of positive lexicon words) x2 = 2 (count of negative lexicon words)
假设 θ 0 中的初始权重和偏置都设为 0，初始学习率 η 为 0.1：

> Let’s assume the initial weights and bias in θ 0 are all set to 0, and the initial learning rate η is 0.1:

$$w _{1} = w _{2} = b = 0$$

η = 0.1 单次更新步骤要求我们计算梯度，再乘以学习率 θt+1 = θt −η∇θL(f(x(i);θ),y(i)) 在我们的迷你示例中有三个参数，因此梯度向量有 3 个维度，分别对应 w1、w2 和 b。我们可以如下计算第一个梯度：

> η = 0.1 The single update step requires that we compute the gradient, multiplied by the learning rate θt+1 = θt −η∇θL(f(x(i);θ),y(i)) In our mini example there are three parameters, so the gradient vector has 3 dimensions, for w1, w2, and b. We can compute the first gradient as follows:

> ∂LCE(ˆy,y)

(σ(w ·x+b)−y)x1 (σ(0)−1)x1 −0.5x1 −1.5
=
∇w,bL =  (σ(w ·x+b)−y)x2 =  (σ(0)−1)x2 =  −0.5x2 =  −1.0
σ(w ·x+b)−y σ(0)−1 −0.5 −0.5
现在我们有了梯度，就可以把 θ 0 沿梯度的反方向移动，从而计算出新的参数向量 θ 1：

> Now that we have a gradient, we compute the new parameter vector θ 1 by movingθ 0 in the opposite direction from the gradient:

> ∂w1

> ∂LCE(ˆy,y)

> ∂w2

> ∂LCE(ˆy,y)∂b

w1   −1.5   .15
θ 1 =  w2 −η  −1.0 =  .1
b −0.5 .05
因此，经过一步梯度下降之后，权重已经变为：w1 = .15、w2 = .1，b = .05。

> So after one step of gradient descent, the weights have shifted to be: w1 = .15, w2 = .1, and b = .05.

请注意，这个观测样本 x 恰好是一个正例。我们预期

> Note that this observation x happened to be a positive example. We would expect
在看到更多负面词数量很高的负例之后，权重 w2 会变成负值。

> that after seeing more negative examples with high counts of negative words, that the weight w2 would shift to have a negative value.

### 4.6.4 小批量训练

> 4.6.4 Mini-batch training

随机梯度下降之所以被称为随机的，是因为它每次只选择一个随机样本，并移动权重以改进在该单个样本上的性能。这会导致非常剧烈的波动，因此常见的做法是在一批训练实例上计算梯度，而不是在单个实例上计算。

> Stochastic gradient descent is called stochastic because it chooses a single random example at a time, moving the weights so as to improve performance on that single example. That can result in very choppy movements, so it’s common to compute the gradient over batches of training instances rather than a single instance.

例如，在批训练中，我们在整个数据集上计算梯度。

> For example in batch training we compute the gradient over the entire dataset.

> `batch training`（批训练）

通过看到如此多的样本，批训练能够极好地估计出应当朝哪个方向移动权重，代价是要花费大量时间处理训练集中的每一个样本，以计算出这个完美的方向。

> By seeing so many examples, batch training offers a superb estimate of which direction to move the weights, at the cost of spending a lot of time processing every single example in the training set to compute this perfect direction.

折中方案是小批量训练：我们在一组 m 个样本（也许是 512 个或 1024 个）上进行训练，这个数量小于整个数据集。（如果 m 等于数据集的大小，那么我们做的就是批梯度下降；如果 m = 1，我们就又回到了随机梯度下降。）小批量训练还具有计算效率上的优势。小批量可以很容易地被向量化，并根据计算资源来选择小批量的大小。这使我们能够并行处理一个小批量中的所有样本，然后累加损失，这是逐个样本训练无法做到的。

> A compromise is mini-batch training: we train on a group of m examples (perhaps 512, or 1024) that is less than the whole dataset. (If m is the size of the dataset, then we are doing batch gradient descent; if m = 1, we are back to doing stochastic gradient descent.) Mini-batch training also has the advantage of computational efficiency. The mini-batches can easily be vectorized, choosing the size of the minibatch based on the computational resources. This allows us to process all the examples in one mini-batch in parallel and then accumulate the loss, something that’s not possible with individual training.

> `mini-batch`（小批量）

我们只需要定义交叉熵损失函数的小批量版本

> We just need to define mini-batch versions of the cross-entropy loss function
我们在第 4.5 节中定义的交叉熵损失函数，以及第 4.6.1 节中的梯度。让我们把式 4.19 中单个样本的交叉熵损失扩展到大小为 m 的小批量。我们继续使用记号 x(i) 和 y(i)，它们分别表示第 i 个训练特征和训练标签。我们假设训练样本之间是相互独立的：

> we defined in Section 4.5 and the gradient in Section 4.6.1. Let’s extend the crossentropy loss for one example from Eq. 4.19 to mini-batches of size m. We’ll continue to use the notation that x(i) and y(i) mean the ith training features and training label, respectively. We make the assumption that the training examples are independent:

> m

$$\prod_{i = 1}^{m}$$

log p(training labels) = log p(y(i)|x(i))
X= log p(y(i)|x(i))

> i=1 m

> i=1 m

$$\sum_{i = 1}^{m}$$

$$L _{\text{CE}} ( y ˆ ^{( i )} , y ^{( i )} )$$

= −
现在，包含 m 个样本的小批量的代价函数是每个样本损失的平均值：

> Now the cost function for the mini-batch of m examples is the average loss for each example:

> i=1

> m

1 X
Cost(ˆy,y) = LCE(ˆy(i),y(i))
m
= −1 X y(i) logσ(w ·x(i) +b)+(1−y(i))log

> i=1 m

$$1 - σ ( w \cdot x ^{( i )} + b )$$

m
小批量梯度是式 4.26 中各个梯度的平均值：

> The mini-batch gradient is the average of the individual gradients from Eq. 4.26:

> i=1

> m

∂Cost(ˆy,y) 1 X h σ(w ·x(i) +b)−y(i)i

$$x ^{( i )} _{j}$$

= (4.31)
∂w j m
我们可以不使用求和记号，而是更高效地计算梯度

> Instead of using the sum notation, we can more efficiently compute the gradient
以其矩阵形式，按照我们在第 100 页看到的向量化方法，其中有一个大小为 [m × f] 的矩阵 X 表示该批中的 m 个输入，以及一个大小为 [m×1] 的向量 y 表示正确的输出：

> in its matrix form, following the vectorization we saw on page 100, where we have a matrix X of size [m × f] representing the m inputs in the batch, and a vector y of size [m×1] representing the correct outputs:

> j

> i=1

∂Cost(ˆy,y) m (ˆy −y)⊺X 1
=
∂w
m (σ(Xw +b)−y)⊺X 1 (4.32)
=

## 4.7 多项逻辑回归

> 4.7 Multinomial logistic regression

有时我们需要多于两个类别。比如我们可能想做三分类的情感分类（正面、负面或中性）。或者我们可能要标注一些将在第 18 章介绍的标签，例如一个词的词性（从 10 种、30 种甚至 50 种不同词性中选择），或者一个短语的命名实体类型（从 person、location、organization 等标签中选择）。又或者，对于大语言模型，我们要从词表中 |V| 个可能的词中预测下一个词，因此是 |V| 分类。

> Sometimes we need more than two classes. Perhaps we might want to do 3-way sentiment classification (positive, negative, or neutral). Or we could be assigning some of the labels we will introduce in Chapter 18, like the part of speech of a word(choosing from 10, 30, or even 50 different parts of speech), or the named entity type of a phrase (choosing from tags like person, location, organization). Or, for large language models, we’ll be predicting the next word out of the |V| possible words in the vocabulary, so it’s |V|-way classification.

> `multinomial logistic regression`（多项逻辑回归）

在这种情况下，我们使用多项逻辑回归，也称为 softmax 回归（在较早的 NLP 文献中，有时会看到最大熵分类器这个名称）。在多项逻辑回归中，我们希望把每个观测样本标注为 K 个类别集合中的某个类别 k，前提是这些类别中只有一个是正确的（有时称为硬分类；一个观测样本不能属于多个类别）。我们采用如下表示：每个输入 x 的输出 y 将是一个长度为 K 的向量。如果类别 c 是正确的类别，我们就令 yc = 1，并把 y 的所有其他元素设为 0，即 yc = 1 且 yj = 0 ∀j̸ = c。像这样 y 中一个值为 1、其余为 0 的向量，称为独热向量（one-hot vector）。分类器的任务是生成一个估计向量 ˆy。对于每个类别 k，值 ˆyk 将是分类器对概率 P(yk = 1|x) 的估计。

> In such cases we use multinomial logistic regression, also called softmax regression (in older NLP literature you will sometimes see the name maxent classifier). In multinomial logistic regression we want to label each observation with a class k from a set of K classes, under the stipulation that only one of these classes is the correct one (sometimes called hard classification; an observation can not be in multiple classes). Let’s use the following representation: the output y for each input x will be a vector of length K. If class c is the correct class, we’ll set yc = 1, and set all the other elements of y to be 0, i.e., yc = 1 and yj = 0 ∀j̸ = c. A vector like this y, with one value=1 and the rest 0, is called a one-hot vector. The job of the classifier is to produce an estimate vector ˆy. For each class k, the value ˆyk will be the classifier’s estimate of the probability P(yk = 1|x).

### 4.7.1 Softmax

多项逻辑分类器使用 sigmoid 的一种推广形式——softmax 函数，来计算 p(yk = 1|x)。softmax 函数接受一个向量

> The multinomial logistic classifier uses a generalization of the sigmoid, called the softmax function, to compute p(yk = 1|x). The softmax function takes a vector

> `softmax`

z = [z1,z2,...,zK]，其中包含 K 个任意值，并将它们映射为一个概率分布，每个值都落在 [0,1] 范围内，且所有值之和为 1。与 sigmoid 一样，它是一个指数函数。

> z = [z1,z2,...,zK] of K arbitrary values and maps them to a probability distribution, with each value in the range [0,1], and all the values summing to 1. Like the sigmoid, it is an exponential function.

对于维度为 K 的向量 z，softmax 定义为：

> For a vector z of dimensionality K, the softmax is defined as:

$$\text{exp} ( z _{i} )$$

softmax(zi) = 1 ≤i ≤K (4.33)
PK j=1 exp(z j)
因此，输入向量 z = [z1,z2,...,zK] 的 softmax 本身就是一个向量：

> The softmax of an input vector z = [z1,z2,...,zK] is thus a vector itself:

" #
exp(z1) exp(z2) exp(zK)
softmax(z) = (4.34)
PK , PK ,..., PK i=1 exp(zi) i=1 exp(zi) i=1 exp(zi)
分母 PK i=1 exp(zi) 用于把所有值归一化为概率。

> The denominator PK i=1 exp(zi) is used to normalize all the values into probabilities.

因此，例如给定一个向量：

> Thus for example given a vector:

z = [0.6,1.1,−1.5,1.2,3.2,−1.1]
得到的（四舍五入后的）softmax(z) 为

> the resulting (rounded) softmax(z) is
[0.05,0.09,0.01,0.1,0.74,0.01]
与 sigmoid 一样，softmax 具有把值压缩到接近 0 或 1 的性质。

> Like the sigmoid, the softmax has the property of squashing values toward 0 or 1.

因此，如果其中一个输入大于其他输入，它会把自身的概率推向 1，并压低较小输入的概率。

> Thus if one of the inputs is larger than the others, it will tend to push its probability toward 1, and suppress the probabilities of the smaller inputs.

最后请注意，与 sigmoid 一样，我们把 z 这个作为 softmax 输入的分数向量

> Finally, note that, just as for the sigmoid, we refer to z, the vector of scores that
称为 logit（见式 4.7）。

> is the input to the softmax, as logits (see Eq. 4.7).

### 4.7.2 在逻辑回归中应用 softmax

> 4.7.2 Applying softmax in logistic regression

当我们把 softmax 应用于逻辑回归时，其输入（与 sigmoid 一样）将是权重向量 w 与输入向量 x 之间的点积（再加上偏置）。但现在我们需要为 K 个类别中的每一个都准备单独的权重向量 wk 和偏置 bk。于是，每个输出类别 ˆyk 的概率可以计算为：

> When we apply softmax for logistic regression, the input will (just as for the sigmoid) be the dot product between a weight vector w and an input vector x (plus a bias). But now we’ll need separate weight vectors wk and bias bk for each of the K classes. The probability of each of our output classes ˆyk can thus be computed as:

$$_{K} \text{exp} ( w _{k} \cdot x + b _{k} )$$

$$P ( y _{k} = 1 | x ) =$$

> K

$$\sum_{j = 1}^{K}$$

$$\text{exp} ( w ^{j} \cdot x + b _{j} )$$

> j=1

式 4.35 的形式看起来像是要分别计算每个输出。然而，更常见的做法是按照现代向量处理硬件的高效计算方式来建立方程。为此，我们把 K 个权重向量的集合表示为一个权重矩阵 W 和一个偏置向量 b。W 的第 k 行对应于权重向量 wk。因此 W 的形状为 [K × f]，其中 K 是输出类别的数量，f 是输入特征的数量。偏置向量 b 为 K 个输出类别各有一个值。若以这种方式表示权重，我们就可以用一个简洁的方程来计算 ˆy，即 K 个类别各自输出概率构成的向量：

> The form of Eq. 4.35 makes it seem that we would compute each output separately. Instead, it’s more common to set up the equation for more efficient computation by modern vector processing hardware. We’ll do this by representing the set of K weight vectors as a weight matrix W and a bias vector b. Each row k of W corresponds to the vector of weights wk. W thus has shape [K × f], for K the number of output classes and f the number of input features. The bias vector b has one value for each of the K output classes. If we represent the weights in this way, we can compute ˆy, the vector of output probabilities for each of the K classes, by a single elegant equation:

ˆy = softmax(Wx+b) (4.36)
如果你展开矩阵运算，就会看到估计分数

> If you work out the matrix arithmetic, you can see that the estimated score of
第一个输出类别 ˆy1（在我们取 softmax 之前）将正确地等于 w1 ·x+b1。

> the first output class ˆy1 (before we take the softmax) will correctly turn out to be w1 ·x+b1.

对权重矩阵 W 的一种有帮助的解释是把它的每一行 wk 看作

> One helpful interpretation of the weight matrix W is to see each row wk as a
类别 k 的原型。学习到的权重向量 wk 把该类别表示为

> prototype of class k. The weight vector wk that is learned represents the class as

> `prototype`（原型）

一种模板。由于两个彼此越相似的向量其点积越大，点积便充当相似度函数。

> a kind of template. Since two vectors that are more similar to each other have a higher dot product with each other, the dot product acts as a similarity function.

因此，逻辑回归为每个类别学习一种原型表示，使得输入的向量被分配给 K 个类别中与它最相似的类别 k（Doumbouya et al., 2025）。

> Logistic regression is thus learning a prototype representation for each class, such that incoming vectors are assigned the class k they are most similar to from the K classes (Doumbouya et al., 2025).

图 4.6 展示了二分类逻辑回归与多项逻辑回归之间的差异，

> Fig. 4.6 shows the difference between binary and multinomial logistic regression
它通过图示说明了在计算输出类别概率时权重向量与权重矩阵的区别。

> by illustrating the weight vector versus weight matrix in the computation of the output class probabilities.

### 4.7.3 多项逻辑回归中的特征

> 4.7.3 Features in Multinomial Logistic Regression

多项逻辑回归中的特征与二分类逻辑回归中的特征作用相同，区别如前所述：我们需要为 K 个类别中的每一个分别设置权重向量和偏置。回忆第 97 页中我们二分类的感叹号特征 x5：

> Features in multinomial logistic regression act like features in binary logistic regression, with the difference mentioned above that we’ll need separate weight vectors and biases for each of the K classes. Recall our binary exclamation point feature x5 from page 97:

1 如果 “!” ∈doc

> 1 if “!” ∈doc
x5 = 0 否则

> x5 = 0 otherwise
在二分类中，特征上的正权重 w5 会使分类器

> In binary classification a positive weight w5 on a feature influences the classifier
倾向于 y = 1（正面情感），而负权重会使它倾向于 y = 0（负面情感），其绝对值表示该特征有多重要。相比之下，在多项逻辑回归中，由于每个类别有各自的权重，一个特征可以成为支持或反对每个单独类别的证据。

> toward y = 1 (positive sentiment) and a negative weight influences it toward y = 0(negative sentiment) with the absolute value indicating how important the feature is. For multinomial logistic regression, by contrast, with separate weights for each class, a feature can be evidence for or against each individual class.

例如，在三分类的多类别情感分类中，我们必须为每

> In 3-way multiclass sentiment classification, for example, we must assign each
篇文档分配 3 个类别 +、− 或 0（中性）中的一个。此时与感叹号相关的特征对于 0 类文档可能有负权重，而对于 + 或 − 类文档有正权重：

> document one of the 3 classes +, −, or 0 (neutral). Now a feature related to exclamation marks might have a negative weight for 0 documents, and a positive weight for + or −documents:

特征 定义  1 如果 “!” ∈doc w5,+ w5,−w5,0 f5(x) 0 否则 3.5 3.1 −5.3

> Feature Definition  1 if “!” ∈doc w5,+ w5,−w5,0 f5(x) 0 otherwise 3.5 3.1 −5.3
由于这些特征权重既依赖于输入文本又依赖于输出

> Because these feature weights are dependent both on the input text and the output
类别，我们有时会把这种依赖显式表达出来，把特征本身表示为 f(x,y)：即同时以输入和类别为自变量的函数。使用这样的记号，上面的 f5(x) 可以表示为三个特征 f5(x,+)、f5(x,−) 和 f5(x,0)，每个特征只有一个权重。在第 18 章描述 CRF 时，我们将使用这类记号。

> class, we sometimes make this dependence explicit and represent the features themselves as f(x,y): a function of both the input and the class. Using such a notation f5(x) above could be represented as three features f5(x,+), f5(x,−), and f5(x,0), each of which has a single weight. We’ll use this kind of notation in our description of the CRF in Chapter 18.

![](images/04-logistic-regression/fig_p20_0.png)

*图 4.6 二分类逻辑回归与多项逻辑回归的对比。二分类逻辑回归使用单个权重向量 w，输出为标量 ˆy。在多项逻辑回归中，我们有与 K 个类别对应的 K 个独立权重向量，它们全部打包进单个权重矩阵 W，输出为向量 ˆy。为清晰起见，两幅图都省略了偏置。*
*Figure 4.6 Binary versus multinomial logistic regression. Binary logistic regression uses a single weight vector w, and has a scalar output ˆy. In multinomial logistic regression we have K separate weight vectors corresponding to the K classes, all packed into a single weight matrix W, and a vector output ˆy. We omit the biases from both figures for clarity.*

## 4.8 多项逻辑回归中的学习

> 4.8 Learning in Multinomial Logistic Regression

多项逻辑回归的损失函数把二分类逻辑回归的损失函数从 2 个类别推广到 K 个类别。回忆二分类逻辑回归的交叉熵损失（重录自式 4.19）为：

> The loss function for multinomial logistic regression generalizes the loss function for binary logistic regression from 2 to K classes. Recall that the cross-entropy loss for binary logistic regression (repeated from Eq. 4.19) is:

$$L _{\text{CE}} ( y ˆ , y ) = - \text{log} p ( y | x ) = - [ y \text{log ˆ} y +( 1 - y ) \text{log} ( 1 - y ˆ )]$$

多项逻辑回归的损失函数把式 4.37 中的两项（一项在 y = 1 时非零，另一项在 y = 0 时非零）推广为 K 项。如前所述，对于多项回归，我们将把 y 和 ˆy 都表示为向量。真实标签 y 是一个含 K 个元素的向量，每个元素对应一个类别，当正确类别为 c 时 yc = 1，y 的其余元素均为 0。

> The loss function for multinomial logistic regression generalizes the two terms in Eq. 4.37 (one that is non-zero when y = 1 and one that is non-zero when y = 0) to K terms. As we mentioned above, for multinomial regression we’ll represent both y and ˆy as vectors. The true label y is a vector with K elements, each corresponding to a class, with yc = 1 if the correct class is c, with all other elements of y being 0.

而我们的分类器将产生一个含 K 个元素的估计向量 ˆy，其中每个元素 ˆyk 表示估计概率 p(yk = 1|x)。

> And our classifier will produce an estimate vector with K elements ˆy, each elementˆyk of which represents the estimated probability p(yk = 1|x).

单个样本 x 的损失函数由二分类逻辑回归推广而来，它是 K 个输出类别的对数之和，每一项由指示函数 yk 加权（式 4.38）。结果它恰好等于正确类别 c 的负对数概率（式 4.39）：

> The loss function for a single example x, generalizing from binary logistic regression, is the sum of the logs of the K output classes, each weighted by the indicator function yk (Eq. 4.38). This turns out to be just the negative log probability of the correct class c (Eq. 4.39):

> K

$$\sum_{k = 1}^{K}$$

LCE(ˆy,y) = − yk log ˆyk (4.38)
= −log ˆyc，（其中 c 是正确类别）(4.39)

> = −log ˆyc, (where c is the correct class) (4.39)
= −log ˆp(yc = 1|x)（其中 c 是正确类别）

> = −log ˆp(yc = 1|x) (where c is the correct class)
exp(wc ·x+bc) (4.40)
= −log （c 是正确类别）

> = −log (c is the correct class)
PK j=1 exp(wj ·x+bj)
我们是如何从式 4.38 得到式 4.39 的？因为只有一个类别（我们称它为 c）是正确的，向量 y 仅在这个 k 值处取值为 1，即 yc = 1 且对所有 j̸ = c 有 yj = 0。这意味着式 4.38 求和中的各项除对应真实类别 c 的那一项外其余都为 0。因此交叉熵损失就只是正确类别所对应的输出概率的负对数，我们

> How did we get from Eq. 4.38 to Eq. 4.39? Because only one class (let’s call it c) is the correct one, the vector y takes the value 1 only for this value of k, i.e., has yc = 1 and yj = 0 ∀j̸ = c. That means the terms in the sum in Eq. 4.38 will all be 0 except for the term corresponding to the true class c. Hence the cross-entropy loss is simply the negative log of the output probability corresponding to the correct class, and we

> k=1

> `negative log likelihood loss`（负对数似然损失）

因此也把式 4.39 称为负对数似然损失。

> therefore also call Eq. 4.39 the negative log likelihood loss.

当然，对于梯度下降，我们不需要损失本身，我们需要的是它的梯度。

> Of course for gradient descent we don’t need the loss, we need its gradient. The

单个样本的梯度结果与我们在式 4.26 中看到的二分类逻辑回归的梯度 (ˆy−y)x 非常相似。让我们考虑梯度的一个组成部分，即单个权重的导数。对于每个类别 k，输入 x 的第 i 个元素对应的权重是 wk,i。损失对 wk,i 的偏导数是什么？这个导数结果恰好是类别 k 的真实值（取值为 1 或 0）与分类器为类别 k 输出的概率之差，再乘以与类别 k 权重向量第 i 个元素对应的输入 xi 的值：

> gradient for a single example turns out to be very similar to the gradient for binary logistic regression, (ˆy−y)x, that we saw in Eq. 4.26. Let’s consider one piece of the gradient, the derivative for a single weight. For each class k, the weight of the ith element of input x is wk,i. What is the partial derivative of the loss with respect to wk,i? This derivative turns out to be just the difference between the true value for the class k (which is either 1 or 0) and the probability the classifier outputs for class k, weighted by the value of the input xi corresponding to the ith element of the weight vector for class k:

$$\partial L _{\text{CE}}$$

$$= - ( y _{k} - y ˆ _{k} ) x _{i}$$

$$\partial w _{k , i}$$

$$= - ( y _{k} - p ( y _{k} = 1 | x )) x _{i}$$

!

exp(wk ·x+bk) (4.41)
yk − xi
= − PK

$$^{K} _{j = 1} \text{exp} ( w _{j} \cdot x + b _{j} )$$

## 4.9 评估：精确率、召回率、F 值

> 4.9 Evaluation: Precision, Recall, F-measure

为了介绍评估文本分类的方法，我们先来考虑一些简单的二元检测任务。例如，在垃圾邮件检测中，我们的目标是把每段文本标记为属于垃圾邮件类别（“正类”）或不属于垃圾邮件类别（“负类”）。因此，对于每一个项目（电子邮件文档），我们都需要知道我们的系统是否将其判为垃圾邮件。我们还需要知道该邮件实际上是否为垃圾邮件，也就是我们试图匹配的、由人工为每个文档定义的标签。我们将这些人工标签称为金标准标签。

> To introduce the methods for evaluating text classification, let’s first consider some simple binary detection tasks. For example, in spam detection, our goal is to label every text as being in the spam category (“positive”) or not in the spam category(“negative”). For each item (email document) we therefore need to know whether our system called it spam or not. We also need to know whether the email is actually spam or not, i.e. the human-defined labels for each document that we are trying to match. We will refer to these human labels as the gold labels.

> `gold labels`（金标准标签）

或者想象一下，你是 Delicious Pie 公司的 CEO，你需要知道

> Or imagine you’re the CEO of the Delicious Pie Company and you need to know
人们在社交媒体上如何评价你的馅饼，于是你构建了一个系统来检测与 Delicious Pie 有关的推文。这里正类是关于 Delicious Pie 的推文，负类是所有其他推文。

> what people are saying about your pies on social media, so you build a system that detects tweets concerning Delicious Pie. Here the positive class is tweets about Delicious Pie and the negative class is all other tweets.

在这两种情况下，我们都需要一个指标，用来了解我们的垃圾邮件检测器（或

> In both cases, we need a metric for knowing how well our spam detector (or
馅饼推文检测器）表现如何。要评估任何用于检测事物的系统，我们首先要

> pie-tweet-detector) is doing. To evaluate any system for detecting things, we start

> `confusion matrix`（混淆矩阵）

构建一个如图 4.7 所示的混淆矩阵。混淆矩阵

> by building a confusion matrix like the one shown in Fig. 4.7. A confusion matrix
是一种表格，用于可视化算法相对于人工金标准标签的表现如何，它使用两个维度（系统输出和金标准标签），每个单元格标示一组可能的结果。例如在垃圾邮件检测中，真正例是那些确实为垃圾邮件（由人工创建的金标准标签指明）、并且我们的系统正确地判为垃圾邮件的文档。假负例是那些确实为垃圾邮件、但我们的系统错误地标记为非垃圾邮件的文档。

> is a table for visualizing how an algorithm performs with respect to the human gold labels, using two dimensions (system output and gold labels), and each cell labeling a set of possible outcomes. In the spam detection case, for example, true positives are documents that are indeed spam (indicated by human-created gold labels) that our system correctly said were spam. False negatives are documents that are indeed spam but our system incorrectly labeled as non-spam.

表格的右下方是准确率的公式，它问的是

> To the bottom right of the table is the equation for accuracy, which asks what
我们的系统正确标记的观测样本占全部观测样本的百分比（对于垃圾邮件或馅饼这两个例子，这意味着所有邮件或推文）。尽管准确率看起来是一个自然的指标，但我们在文本分类任务中一般并不使用它。这是因为当各类别不平衡时准确率表现不好（垃圾邮件确实如此，它占邮件的很大一部分；推文也是如此，它们大多与馅饼无关）。

> percentage of all the observations (for the spam or pie examples that means all emails or tweets) our system labeled correctly. Although accuracy might seem a natural metric, we generally don’t use it for text classification tasks. That’s because accuracy doesn’t work well when the classes are unbalanced (as indeed they are with spam, which is a large majority of email, or with tweets, which are mainly not about pie).

![](images/04-logistic-regression/fig_p22_0.png)

*图 4.7 混淆矩阵，用于可视化二分类系统相对于金标准标签的表现有多好。*
*Figure 4.7 A confusion matrix for visualizing how well a binary classification system performs against gold standard labels.*

为了更明确地说明这一点，设想我们查看了 100 万条推文，

> To make this more explicit, imagine that we looked at a million tweets, and
假设其中只有 100 条在谈论它们对我们馅饼的喜爱（或厌恶），而其余 999,900 条是与我们完全无关的推文。设想一个简单的分类器，它愚蠢地把每条推文都分类为“与馅饼无关”。这个分类器会有 999,900 个真负例和仅仅 100 个假负例，准确率为 999,900/1,000,000，即 99.99%！多么惊人的准确率水平！我们当然应该对这个分类器感到满意吧？但这个出色的“无馅饼”分类器当然毫无用处，因为它找不到任何一条我们正在寻找的客户评论。换句话说，当目标是发现稀有的事物、或至少在频率上并不完全平衡的事物时，准确率并不是一个好的指标，而这在现实世界中是非常常见的情形。

> let’s say that only 100 of them are discussing their love (or hatred) for our pie, while the other 999,900 are tweets about something completely unrelated. Imagine a simple classifier that stupidly classified every tweet as “not about pie”. This classifier would have 999,900 true negatives and only 100 false negatives for an accuracy of 999,900/1,000,000 or 99.99%! What an amazing accuracy level! Surely we should be happy with this classifier? But of course this fabulous ‘no pie’ classifier would be completely useless, since it wouldn’t find a single one of the customer comments we are looking for. In other words, accuracy is not a good metric when the goal is to discover something that is rare, or at least not completely balanced in frequency, which is a very common situation in the world.

这就是为什么我们一般不用准确率，而是改用

> That’s why instead of accuracy we generally turn to two other metrics shown in

*图 4.7 中所示的另外两个指标：精确率和召回率。精确率衡量的是系统检测出的项目（即*
*Fig. 4.7: precision and recall. Precision measures the percentage of the items that*

> `precision`（精确率）

系统标记为正类的项目）中实际上是正类（即根据人工金标准标签为正类）的项目所占的百分比。精确率定义为

> the system detected (i.e., the system labeled as positive) that are in fact positive (i.e., are positive according to the human gold labels). Precision is defined as
true positives
Precision =
true positives + false positives
召回率衡量的是输入中实际存在的项目里被

> Recall measures the percentage of items actually present in the input that were
系统正确识别出来的百分比。召回率定义为 true positives Recall = true positives + false negatives

> correctly identified by the system. Recall is defined as true positives Recall = true positives + false negatives
精确率和召回率将有助于解决那个无用的“什么都不是

> Precision and recall will help solve the problem with the useless “nothing is
馅饼”分类器所带来的问题。这个分类器尽管拥有 99.99% 的惊人准确率，召回率却糟得只有 0（因为没有真正例，而有 100 个假负例，召回率为 0/100）。你应该能确信，它在找出相关推文方面的精确率同样有问题。因此，与准确率不同，精确率和召回率强调的是真正例：找出我们本应去寻找的东西。

> pie” classifier. This classifier, despite having a fabulous accuracy of 99.99%, has a terrible recall of 0 (since there are no true positives, and 100 false negatives, the recall is 0/100). You should convince yourself that the precision at finding relevant tweets is equally problematic. Thus precision and recall, unlike accuracy, emphasize true positives: finding the things that we are supposed to be looking for.

有很多方法可以定义同时包含精确率和召回率两个方面

> There are many ways to define a single metric that incorporates aspects of both
信息的单一指标。这些组合中最简单的是 F 值（van

> precision and recall. The simplest of these combinations is the F-measure (van

> `F-measure`（F 值）

Rijsbergen, 1975），定义为：

> Rijsbergen, 1975), defined as:

Fβ = (β 2 +1)PR

$$β ^{2} P + R$$

β 参数以不同的方式为召回率和精确率的重要性加权，

> The β parameter differentially weights the importance of recall and precision,
这或许取决于应用的需求。β > 1 的取值偏向召回率，而 β < 1 的取值偏向精确率。当 β = 1 时，精确率与召回率得到同等平衡；这是最常用的指标，称为 Fβ=1，或简称为 F1：

> based perhaps on the needs of an application. Values of β > 1 favor recall, while values of β < 1 favor precision. When β = 1, precision and recall are equally balanced; this is the most frequently used metric, and is called Fβ=1 or just F1:

> `F1`

F1 = 2PR (4.42)
P+R
F 值来自精确率与召回率的加权调和平均。该

> F-measure comes from a weighted harmonic mean of precision and recall. The
一组数的调和平均，是这组数各取倒数后的算术平均的倒数：

> harmonic mean of a set of numbers is the reciprocal of the arithmetic mean of reciprocals:

n

HarmonicMean(a1,a2,a3,a_14,...,an) = (4.43)

$$_{a 1} ^{1} + _{a 2} ^{1}$$

$$_{a 2} ^{1} + _{a 3} ^{1} + ... + _{a n} ^{1}$$

> an

因此 F 值为

> and hence F-measure is
1  with β 2 = 1−α  F = (β 2 +1)PR
F = or (4.44)
α 1 P +(1−α) 1 α β 2P+R
之所以使用调和平均，是因为两个值的调和平均比算术平均更接近这两个值中的最小值。因此它给两个数中较小的那个赋予更大的权重，在这种情况下更为保守。

> Harmonic mean is used because the harmonic mean of two values is closer to the minimum of the two values than the arithmetic mean is. Thus it weighs the lower of the two numbers more heavily, which is more conservative in this situation.

> R

### 4.9.1 多于两个类别时的评估

> 4.9.1 Evaluating with more than two classes

我们在上文定义精确率和召回率时给出的简单示例，只涉及两个类别的文本分类。但正如第 4.7 节所见，许多 NLP 分类任务都多于两个类别。即便在情感分析中，我们也常常有 3 个类别（正面、负面、中性），而在文本分类或情绪检测等任务中，更多类别也很常见，等等。

> The simple example we gave above in defining precision and recall involved text classification with only two classes. But as we saw in Section 4.7, lots of NLP classification tasks have more than two classes. Even for sentiment analysis we often have 3 classes (positive, negative, neutral) and many more classes are common in tasks like text classification or emotion detection, and so on.

为了处理多于两个类别的情况，我们需要对定义稍作修改

> To deal with more than two classes we’ll need to slightly modify our definitions
即精确率和召回率的定义。考虑图 4.8 所示的一个假想三路互斥电子邮件分类决策（紧急、普通、垃圾邮件）的示例混淆矩阵。

> of precision and recall. Consider the sample confusion matrix for a hypothetical 3way one-of email categorization decision (urgent, normal, spam) shown in Fig. 4.8.

例如，该矩阵显示系统把一封垃圾邮件错误地标注为紧急，我们还展示了如何为每个类别计算各自的精确率和召回率值。为了得出一个能说明系统表现如何的单一指标，

> The matrix shows, for example, that the system mistakenly labeled one spam document as urgent, and we have shown how to compute a distinct precision and recall value for each class. In order to derive a single metric that tells us how well the

![](images/04-logistic-regression/fig_p24_1.png)

*图 4.8 三类分类任务的混淆矩阵，对每一对类别 (c1,c2) 显示有多少来自 c1 的文档被（不）正确地分配到 c2。*
*Figure 4.8 Confusion matrix for a three-class categorization task, showing for each pair of classes (c1,c2), how many documents from c1 were (in)correctly assigned to c2.*

系统表现得如何，我们可以用两种方式合并这些值。在宏平均中，

> system is doing, we can combine these values in two ways. In macroaveraging,

> `macroaveraging`（宏平均）

我们计算每个类别的性能，然后对各个类别取平均。在微平均中，我们把所有类别的判定汇总到一个混淆矩阵中，

> we compute the performance for each class, and then average over classes. In microaveraging, we collect the decisions for all classes into a single confusion matrix,

> `microaveraging`（微平均）

然后从该表中计算精确率和召回率。图 4.9 分别显示每个类别的混淆矩阵，并展示了微平均和宏平均精确率的计算。1

> and then compute precision and recall from that table. Fig. 4.9 shows the confusion matrix for each class separately, and shows the computation of microaveraged and macroaveraged precision.1

![](images/04-logistic-regression/fig_p24_0.png)

*图 4.9 上一图中 3 个类别各自的混淆矩阵，展示了汇总混淆矩阵以及微平均和宏平均精确率。*
*Figure 4.9 Separate confusion matrices for the 3 classes from the previous figure, showing the pooled confusion matrix and the microaveraged and macroaveraged precision.*

如该图所示，微平均由出现更频繁的类别（此处

> As the figure shows, a microaverage is dominated by the more frequent class (in
即垃圾邮件）主导，因为计数被汇总在一起。宏平均更好地反映了较小类别的统计特性，因此当所有类别的性能同等重要时，宏平均更为合适。

> this case spam), since the counts are pooled. The macroaverage better reflects the statistics of the smaller classes, and so is more appropriate when performance on all the classes is equally important.

## 4.10 测试集与交叉验证

> 4.10 Test sets and Cross-validation

文本分类的训练与测试流程遵循我们在语言建模（第 3.2 节）中看到的方式：我们用训练集训练模型，然后用

> The training and testing procedure for text classification follows what we saw with language modeling (Section 3.2): we use the training set to train the model, then use

> `development`（开发）

开发测试集（也称为 devset）来调整一些参数，并总体上决定哪个模型最好。一旦我们得出自认为最好的模型，就在（此前未见过的）测试集上运行它，以报告其性能。

> the development test set (also called a devset) to perhaps tune some parameters, and in general decide what the best model is. Once we come up with what we think is the best model, we run it on the (hitherto unseen) test set to report its performance.

虽然使用开发集避免了对测试集的过拟合，但设置固定的训练集、开发集和测试集会带来另一个问题：为了给训练留出大量数据，测试集（或开发集）可能不够大，不足以具有代表性。

> While the use of a devset avoids overfitting the test set, having a fixed training set, devset, and test set creates another problem: in order to save lots of data for training, the test set (or devset) might not be large enough to be representative.

如果我们能以某种方式把全部数据都用于训练，同时仍把全部数据都用于测试，岂不是更好？我们可以通过交叉验证做到这一点。

> Wouldn’t it be better if we could somehow use all our data for training and still use all our data for test? We can do this by cross-validation.

> `cross-validation`（交叉验证）

在交叉验证中，我们选择一个数字 k，并把数据划分为 k 个互不相交的

> In cross-validation, we choose a number k, and partition our data into k disjoint
称为折的子集。现在我们选择这 k 折中的一个作为测试集，将我们的

> subsets called folds. Now we choose one of those k folds as a test set, train our

> `folds`（折）

分类器在剩余的 k−1 折上训练，然后计算测试集上的错误率。接着我们用另一折作为测试集重复这一过程，同样在其他 k−1 折上训练。我们重复这个采样过程 k 次，并对这 k 次运行的测试集错误率取平均，得到平均错误率。如果我们选择 k = 10，就会训练 10 个不同的模型（每个都使用 90% 的数据训练），对模型测试 10 次，并对

> classifier on the remaining k −1 folds, and then compute the error rate on the test set. Then we repeat with another fold as the test set, again training on the other k−1 folds. We do this sampling process k times and average the test set error rate from these k runs to get an average error rate. If we choose k = 10, we would train 10 different models (each on 90% of our data), test the model 10 times, and average

> `10-fold`（10 折）

这 10 个值取平均。这称为 10 折交叉验证。

> these 10 values. This is called 10-fold cross-validation.

> `cross-validation`（交叉验证）

交叉验证唯一的问题在于，由于所有数据都被用于

> The only problem with cross-validation is that because all the data is used for
测试，因此我们需要整个语料库保持“盲态”；我们不能查看任何数据来提出可能的特征，也不能一般性地了解发生了什么，因为那样就等于偷看测试集，而这种作弊会让我们高估自己系统的性能。然而，在设计 NLP 系统时，查看语料库以了解发生了什么是很重要的！该怎么办？出于这个原因，通-

> testing, we need the whole corpus to be blind; we can’t examine any of the data to suggest possible features and in general see what’s going on, because we’d be peeking at the test set, and such cheating would cause us to overestimate the performance of our system. However, looking at the corpus to understand what’s going on is important in designing NLP systems! What to do? For this reason, it is com-

![](images/04-logistic-regression/fig_p25_0.png)

*图 4.10 10 折交叉验证*
*Figure 4.10 10-fold cross-validation*

在构建系统时，我们经常需要比较两个系统的性能。我们如何知道刚刚构建的新系统是否比旧系统更好？或者比文献中描述的其他某个系统更好？这属于统计假设检验的领域，本节我们将介绍针对 NLP 分类器的统计显著性检验，尤其参考 Dror 等人（2020）和 Berg-Kirkpatrick 等人（2012）的工作。

> In building systems we often need to compare the performance of two systems. How can we know if the new system we just built is better than our old one? Or better than some other system described in the literature? This is the domain of statistical hypothesis testing, and in this section we introduce tests for statistical significance for NLP classifiers, drawing especially on the work of Dror et al. (2020) and Berg-Kirkpatrick et al. (2012).

假设我们在比较分类器 A 和 B 在某个度量 M 上的性能

> Suppose we’re comparing the performance of classifiers A and B on a metric M
例如 F1 值或准确率。也许我们想知道，在某个特定测试集 x 上，我们新的情感分类器 A 是否比之前的情感分类器 B 得到更高的 F1 分数。我们把系统 A 在测试集 x 上得到的分数记为 M(A,x)，把 A 与 B 在 x 上的性能差异记为 δ(x)：

> such as F1, or accuracy. Perhaps we want to know if our new sentiment classifier A gets a higher F1 score than our previous sentiment classifier B on a particular test set x. Let’s call M(A,x) the score that system A gets on test set x, and δ(x) the performance difference between A and B on x:

δ(x) = M(A,x)−M(B,x) (4.45)
我们想知道是否 δ(x) > 0，即我们新的分类器 A 在 x 上比旧分类器 B 具有更高的 F1。δ(x) 被称为效应量；δ 越大意味着

> We would like to know if δ(x) > 0, meaning that our new classifier A has a higher F1 than our old classifier B on x. δ(x) is called the effect size; a bigger δ means that

> `effect size`（效应量）

A 似乎比 B 好得多；δ 很小则意味着 A 似乎只是稍微好一点。

> A seems to be way better than B; a small δ means A seems to be only a little better.

为什么我们不直接检查 δ(x) 是否为正呢？假设我们这样做，并发现

> Why don’t we just check if δ(x) is positive? Suppose we do, and we find that
A 的 F1 分数比 B 高出 .04。我们能确定 A 更好吗？不能！这是因为在这个特定的 x 上，A 可能只是碰巧比 B 好。

> the F1 score of A is higher than B’s by .04. Can we be certain that A is better? We cannot! That’s because A might just be accidentally better than B on this particular x.

我们需要更多的东西：我们想知道，如果我们再检查另一个测试集 x′，或者在某种其他情形下，A 相对于 B 的优势是否可能依然成立。

> We need something more: we want to know if A’s superiority over B is likely to hold again if we checked another test set x′, or under some other set of circumstances.

在统计假设检验的范式中，我们通过形式化两个

> In the paradigm of statistical hypothesis testing, we test this by formalizing two
假设来对此进行检验。

> hypotheses.

H0 : δ(x) ≤0 H1 : δ(x) > 0 (4.46)
假设 H0 被称为零假设，它假定 δ(x) 实际上为负或为零，即 A 并不比 B 更好。我们想知道能否有把握地排除这一假设，转而支持 H1，即 A 更好。

> The hypothesis H0, called the null hypothesis, supposes that δ(x) is actually negative or zero, meaning that A is not better than B. We would like to know if we can confidently rule out this hypothesis, and instead support H1, that A is better.

> `null hypothesis`（零假设）

我们通过构造一个取遍所有测试集的随机变量 X 来做到这一点。现在我们

> We do this by creating a random variable X ranging over all test sets. Now we
要问：如果零假设 H0 成立，那么在我们大量重复该实验时，在这些测试集中会遇到我们所发现的那个 δ(x) 值的可能性有多大。我们把这一可能性形式化为 p 值：即这样的概率，

> ask how likely is it, if the null hypothesis H0 was correct, that among these test sets we would encounter the value of δ(x) that we found, if we repeated the experiment a great many times. We formalize this likelihood as the p-value: the probability,

> `p-value`（p 值）

在零假设 H0 为真的前提下，看到我们所看到的 δ(x) 或更大值的概率

> assuming the null hypothesis H0 is true, of seeing the δ(x) that we saw or one even greater

$$P ( δ ( X ) \ge δ ( x ) | H _{0} \text{is true} )$$

所以在我们的例子中，这个 p 值就是假定 A 并不比 B 更好时我们会看到 δ(x) 的概率。如果 δ(x) 很大（比方说 A 在 x 上有非常可观的 F1，为 .9，而 B 的 F1 只有糟糕的 .2），我们可能会感到惊讶，因为如果 H0 实际上成立，这种情况极不可能出现，因此 p 值会很低（如果 A 实际上并不比 B 更好，就不太可能出现这么大的 δ）。但如果 δ(x) 非常小，那么即使 H0 成立、A 并不真的比 B 更好，我们可能也不会太惊讶，因此 p 值会更高。

> So in our example, this p-value is the probability that we would see δ(x) assuming A is not better than B. If δ(x) is huge (let’s say A has a very respectable F1 of .9 and B has a terrible F1 of only .2 on x), we might be surprised, since that would be extremely unlikely to occur if H0 were in fact true, and so the p-value would be low(unlikely to have such a large δ if A is in fact not better than B). But if δ(x) is very small, it might be less surprising to us even if H0 were true and A is not really better than B, and so the p-value would be higher.

很小的 p 值意味着我们观察到的差异非常不可能

> A very small p-value means that the difference we observed is very unlikely
在零假设下发生，因此我们可以拒绝零假设。多小才算非常小呢？通常使用 .05 或 .01 这样的值作为阈值。取值 .01 意味着，如果 p 值（在 H0 成立的前提下观察到我们所看到的 δ 的概率）小于 .01，我们就拒绝零假设，并认为 A 确实更好

> under the null hypothesis, and we can reject the null hypothesis. What counts as very small? It is common to use values like .05 or .01 as the thresholds. A value of .01 means that if the p-value (the probability of observing the δ we saw assuming H0 is true) is less than .01, we reject the null hypothesis and assume that A is indeed better

> `statistically significant`（统计显著）

于 B。我们说一个结果（例如“A 比 B 更好”）具有统计显著性，如果

> than B. We say that a result (e.g., “A is better than B”) is statistically significant if
我们所看到的 δ 的概率低于该阈值，并因此拒绝这个零假设。

> the δ we saw has a probability that is below the threshold and we therefore reject this null hypothesis.

我们如何计算 p 值所需的这个概率呢？在 NLP 中，我们通常不使用你可能熟悉的简单参数检验，如 t 检验或方差分析。参数检验会对检验统计量的分布（例如正态性）作出假设，而这些假设在我们的情形中通常并不成立。因此在 NLP 中，我们通常使用基于采样的非参数检验：我们人为地构造出实验设置的许多版本。例如，如果我们有许多不同的测试集 x′，我们就可以对所有 x′ 测量所有的 δ(x′)。这就给我们一个分布。现在我们设定一个阈值（比如 .01），如果在这个分布中我们看到 99% 或更多的 delta 都小于我们观察到的 delta，也就是说 p 值(x)——看到与我们看到的 δ(x) 一样大的值的概率——小于 .01，那么我们就可以拒绝零假设，并认同 δ(x) 是一个足够令人惊讶的差异，A 确实是比 B 更好的算法。

> How do we compute this probability we need for the p-value? In NLP we generally don’t use simple parametric tests like t-tests or ANOVAs that you might be familiar with. Parametric tests make assumptions about the distributions of the test statistic (such as normality) that don’t generally hold in our cases. So in NLP we usually use non-parametric tests based on sampling: we artificially create many versions of the experimental setup. For example, if we had lots of different test sets x′we could just measure all the δ(x′) for all the x′. That gives us a distribution. Now we set a threshold (like .01) and if we see in this distribution that 99% or more of those deltas are smaller than the delta we observed, i.e., that p-value(x)—the probability of seeing a δ(x) as big as the one we saw—is less than .01, then we can reject the null hypothesis and agree that δ(x) was a sufficiently surprising difference and A is really a better algorithm than B.

NLP 中常用的非参数检验有两种：近似随机化检验（Noreen，1989）和自助检验。我们将描述自助

> There are two common non-parametric tests used in NLP: approximate randomization (Noreen, 1989) and the bootstrap test. We will describe bootstrap

> `approximate randomization`（近似随机化检验）

法，展示该检验的配对版本，这在 NLP 中同样最为常见。

> below, showing the paired version of the test, which again is most common in NLP.

配对检验是指我们比较两组彼此对齐的观测样本的检验：

> Paired tests are those in which we compare two sets of observations that are aligned:

> `paired`（配对）

一个集合中的每个观测样本都可以与另一个集合中的观测样本配对。当我们在同一个测试集上比较两个系统的性能时，这种配对会自然出现；我们可以把系统 A 在某个观测样本 xi 上的性能与系统 B 在同一 xi 上的性能配对。

> each observation in one set can be paired with an observation in another. This happens naturally when we are comparing the performance of two systems on the same test set; we can pair the performance of system A on an individual observation xi with the performance of system B on the same xi.

### 4.11.1 配对自助检验

> 4.11.1 The Paired Bootstrap Test

自助检验（Efron and Tibshirani, 1993）可以适用于任何指标；从精确率、召回率或 F1 值，到机器翻译中使用的 BLEU 指标。bootstrapping 一词指的是反复抽取大量有放回的样本

> The bootstrap test (Efron and Tibshirani, 1993) can apply to any metric; from precision, recall, or F1 to the BLEU metric used in machine translation. The word bootstrapping refers to repeatedly drawing large numbers of samples with replace-

> `bootstrap test`（自助检验）

> `bootstrapping`（自助法（bootstrapping））

（称为自助样本，bootstrap samples），这些样本取自一个原始集合。自助检验的直观想法是：我们可以通过反复从一个已观测的测试集中抽样，由它构造出许多虚拟测试集。该方法只做了一个假设，即样本能够代表总体。

> ment (called bootstrap samples) from an original set. The intuition of the bootstrap test is that we can create many virtual test sets from an observed test set by repeatedly sampling from it. The method only makes the assumption that the sample is representative of the population.

考虑一个微小的文本分类例子，其测试集 x 包含 10 篇文档。

> Consider a tiny text classification example with a test set x of 10 documents. The

图 4.11 的第一行展示了两个分类器（A 和 B）在这个测试集上的结果。

> first row of Fig. 4.11 shows the results of two classifiers (A and B) on this test set.

每篇文档都被标为四种可能情形之一（A 和 B 都正确、都错误、A 正确而 B 错误、A 错误而 B 正确）。字母上带一道斜线（B）表示该分类器答错了。在第一篇文档上，A 和 B 都得到了正确的类别（AB），而在第二篇文档上 A 答对但 B 答错（AB）。为简单起见，假设我们的指标是准确率，则 A 的准确率为 .70，B 为 .50，因此 δ(x) 为 .20。

> Each document is labeled by one of the four possibilities (A and B both right, both wrong, A right and B wrong, A wrong and B right). A slash through a letter (B) means that that classifier got the answer wrong. On the first document both A and B get the correct class (AB), while on the second document A got it right but B got it wrong (AB). If we assume for simplicity that our metric is accuracy, A has an accuracy of .70 and B of .50, so δ(x) is .20.

现在我们创建大量 b 个（也许 105 个）虚拟测试集 x(i)，每个的大小为

> Now we create a large number b (perhaps 105) of virtual test sets x(i), each of size
n = 10。图 4.11 展示了几个例子。要创建每个虚拟测试集 x(i)，我们反复（n = 10 次）从行 x 中有放回地选取一个单元格。例如，要创建第一个虚拟测试集 x(1) 的第一个单元格，如果我们碰巧随机选到了行 x 的第二个单元格，就把值 AB 复制到我们的新单元格中，然后继续创建 x(1) 的第二个单元格，每次都从原始 x 中有放回地抽样（随机选择）。

> n = 10. Fig. 4.11 shows a couple of examples. To create each virtual test set x(i), we repeatedly (n = 10 times) select a cell from row x with replacement. For example, to create the first cell of the first virtual test set x(1), if we happened to randomly select the second cell of the x row, we would copy the value AB into our new cell, and move on to create the second cell of x(1), each time sampling (randomly choosing) from the original x with replacement.

现在我们有了这 b 个测试集，它们给出了一个抽样分布，我们可以做

> Now that we have the b test sets, providing a sampling distribution, we can do
统计 A 偶然占优的频率。计算这一优势有各种方式；这里我们采用 Berg-Kirkpatrick et al. (2012) 给出的版本。假设 H0 成立（A 并不比 B 好），我们会预期在许多测试集上估计出的 δ(X) 为零或负；远高于此的值会令人意外，因为 H0 明确假设 A 并不比 B 好。要精确衡量我们观测到的 δ(x) 有多令人意外，在其他情况下我们会通过统计在许多测试集上 δ(x(i)) 超过预期的零

> statistics on how often A has an accidental advantage. There are various ways to compute this advantage; here we follow the version laid out in Berg-Kirkpatrick et al. (2012). Assuming H0 (A isn’t better than B), we would expect that δ(X), estimated over many test sets, would be zero or negative; a much higher value would be surprising, since H0 specifically assumes A isn’t better than B. To measure exactly how surprising our observed δ(x) is, we would in other circumstances compute the p-value by counting over many test sets how often δ(x(i)) exceeds the expected zero

### 1 2 3 4 5 6 7 8 9 10 A% B% δ()

|  | 1 |  | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | A% | B% | δ() |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| x | AB |  | AB | AB | AB | AB | AB | AB | AB | AB | AB | .70 | .50 | .20 |
| x(1) | AB |  | AB | AB | AB | AB | AB | AB | AB | AB | AB | .60 | .60 | .00 |
| x(2) | AB |  | AB | AB | AB | AB | AB | AB | AB | AB | AB | .60 | .70 | -.10 |
| ... |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| x(b) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 图 4.11<br>Figure 4.11 |  | 配对自助检验：创建 b 个伪测试集 x(i) 的示例<br>The paired bootstrap test: Examples of b pseudo test sets x(i) being created |  |  |  |  |  |  |  |  |  |  |  |  |

x AB AB AB AB AB AB AB AB AB AB .70 .50 .20 x(1) AB AB AB AB AB AB AB AB AB AB .60 .60 .00 x(2) AB AB AB AB AB AB AB AB AB AB .60 .70 -.10
值 δ(x) 或更多的频率：

> value by δ(x) or more:

> 从初始的真实测试集 x 中创建。每个伪测试集都是通过有放回地抽样 n = 10 次创建的；因此单个样本就是一个单元格，即一篇带有其金标准标签以及分类器 A 和 B 正确或错误表现的文档。当然，真实测试集不会只有 10 个样本，b 也需要足够大。
>
> *from an initial true test set x. Each pseudo test set is created by sampling n = 10 times with replacement; thus an individual sample is a single cell, a document with its gold label and the correct or incorrect performance of classifiers A and B. Of course real test sets don’t have only 10 examples, and b needs to be large as well.*

> b

p-value(x) = 1 X
1 δ(x(i))−δ(x) ≥0
b
（我们用记号 1(x) 表示“若 x 为真则为 1，否则为 0”。）然而，尽管在许多测试集上 δ(X) 的期望值（再次假设 A 并不比 B 好）通常为 0，但对我们创建的自助测试集而言并非如此。这是因为我们并非从一个均值为 0 的分布中抽取这些样本；我们恰好是从原始测试集 x 中创建它们的，而该测试集恰好（以 .20 的幅度）偏向 A。因此，为衡量我们观测到的 δ(x) 有多令人意外，我们实际上是统计在许多测试集上 δ(x(i)) 超过 δ(x) 的期望值 δ(x) 或更多的频率来计算 p 值：

> (We use the notation 1(x) to mean “1 if x is true, and 0 otherwise”.) However, although it’s generally true that the expected value of δ(X) over many test sets,(again assuming A isn’t better than B) is 0, this isn’t true for the bootstrapped test sets we created. That’s because we didn’t draw these samples from a distribution with 0 mean; we happened to create them from the original test set x, which happens to be biased (by .20) in favor of A. So to measure how surprising is our observedδ(x), we actually compute the p-value by counting over many test sets how oftenδ(x(i)) exceeds the expected value of δ(x) by δ(x) or more:

> i=1

> b

p-value(x) = 1 X
1 δ(x(i))−δ(x) ≥δ(x)
b
= 1 X
1 δ(x(i)) ≥2δ(x) (4.48)
b
因此，举例来说，如果我们有 10,000 个测试集 x(i) 和 .01 的阈值，而只在其中 47 个测试集中发现 A 偶然更好，即 δ(x(i)) ≥2δ(x)，那么得到的 p 值 .0047 小于 .01，这表明我们发现的差值 δ(x) 确实足够令人意外，不太可能偶然发生，于是我们可以拒绝零假设，并断定 A 比 B 好。

> So if for example we have 10,000 test sets x(i) and a threshold of .01, and in only 47 of the test sets do we find that A is accidentally better δ(x(i)) ≥2δ(x), the resulting p-value of .0047 is smaller than .01, indicating that the delta we found, δ(x) is indeed sufficiently surprising and unlikely to have happened by accident, and we can reject the null hypothesis and conclude A is better than B.

> i=1

> b

> i=1

自助法的完整算法如图 4.12 所示。它接受一个测试集

> The full algorithm for the bootstrap is shown in Fig. 4.12. It is given a test set
x、样本数 b，并统计在 b 个自助测试集中 δ(x(i)) > 2δ(x) 所占的百分比。该百分比随后充当单侧经验 p 值。

> x, a number of samples b, and counts the percentage of the b bootstrap test sets in which δ(x(i)) > 2δ(x). This percentage then acts as a one-sided empirical p-value.

## 4.12 避免分类中的危害

> 4.12 Avoiding Harms in Classification

避免分类器可能造成的危害很重要。一类危害是表征性危害（Crawford 2017, Blodgett et al. 2020），这类危害由

> It is important to avoid harms that may result from classifiers. One class of harms is representational harms (Crawford 2017, Blodgett et al. 2020), harms caused

> `representational harms`（表征性伤害）

由一个贬低某个社会群体的系统造成，例如通过固守关于该群体的负面刻板印象。例如，Kiritchenko 和 Mohammad（2018）考察了 200 个情感分析系统在一组句子对上的表现，这些句子

> by a system that demeans a social group, for example by perpetuating negative stereotypes about them. For example Kiritchenko and Mohammad (2018) examined the performance of 200 sentiment analysis systems on pairs of sentences that

![](images/04-logistic-regression/fig_p29_0.png)

*图 4.12 配对自助法算法的一个版本，取自 Berg-Kirkpatrick 等人（2012）。*
*Figure 4.12 A version of the paired bootstrap algorithm after Berg-Kirkpatrick et al.(2012).*

除了包含一个常见的非裔美国人名字（如 Shaniqua）或一个常见的欧裔美国人名字（如 Stephanie）之外完全相同，这些名字选自第 5 章讨论的 Caliskan 等人（2017）的研究。他们发现，大多数系统给包含非裔美国人名字的句子分配了更低的情感和更负面的情绪，这反映并固守了将非裔美国人与负面情绪联系起来的刻板印象（Popp 等人，2003）。

> were identical except for containing either a common African American first name(like Shaniqua) or a common European American first name (like Stephanie), chosen from the Caliskan et al. (2017) study discussed in Chapter 5. They found that most systems assigned lower sentiment and more negative emotion to sentences with African American names, reflecting and perpetuating stereotypes that associate African Americans with negative emotions (Popp et al., 2003).

在其他任务中，分类器可能同时导致表征性伤害和其他

> In other tasks classifiers may lead to both representational harms and other
伤害，例如消声。例如，毒性检测这一重要的文本分类任务，就是检测仇恨言论、辱骂、骚扰或其他

> harms, such as silencing. For example the important text classification task of toxicity detection is the task of detecting hate speech, abuse, harassment, or other

> `toxicity`（毒性）

> `detection`（检测）

种类的有毒语言。虽然这类分类器的目标是帮助减少社会性伤害，但毒性分类器本身也可能造成伤害。例如，研究人员已表明，一些广泛使用的毒性分类器会错误地将本身无毒、只是提及诸如女性（Park 等人，2018）、盲人（Hutchinson 等人，2020）或同性恋者（Dixon 等人，2018；Dias Oliva 等人，2021）等身份的句子，或只是使用了非裔美国人白话英语这类语言变体所特有语言特征的句子（Sap 等人，2019；Davidson 等人，2019），标记为有毒。

> kinds of toxic language. While the goal of such classifiers is to help reduce societal harm, toxicity classifiers can themselves cause harms. For example, researchers have shown that some widely used toxicity classifiers incorrectly flag as being toxic sentences that are non-toxic but simply mention identities like women (Park et al., 2018), blind people (Hutchinson et al., 2020) or gay people (Dixon et al., 2018; Dias Oliva et al., 2021), or simply use linguistic features characteristic of varieties like African American Vernacular English (Sap et al. 2019, Davidson et al. 2019).

此类假正例错误可能导致这些群体自身或关于这些群体的言论被消声。

> Such false positive errors could lead to the silencing of discourse by or about these groups.

这些模型问题可能由训练数据中的偏差或其他问题引起

> These model problems can be caused by biases or other problems in the training
数据；一般来说，机器学习系统会复制甚至放大其训练数据中的偏差。但这些问题也可能由标签引起（例如由于人工标注者的偏差），由所使用的资源引起（如词典，或预训练嵌入等模型组件），甚至由模型架构引起（如模型被训练去优化的目标）。虽然缓解这些偏差（例如通过仔细考量训练数据来源）是一个重要的研究领域，但我们目前还没有通用的解决方案。因此，在引入任何 NLP 模型时，研究这类因素并将其说明清楚非常重要。做到这一点的一种方式是发布模型卡片（Mitchell 等人，2019），针对

> data; in general, machine learning systems replicate and even amplify the biases in their training data. But these problems can also be caused by the labels (for example due to biases in the human labelers), by the resources used (like lexicons, or model components like pretrained embeddings), or even by model architecture(like what the model is trained to optimize). While the mitigation of these biases(for example by carefully considering the training data sources) is an important area of research, we currently don’t have general solutions. For this reason it’s important, when introducing any NLP model, to study these kinds of factors and make them clear. One way to do this is by releasing a model card (Mitchell et al., 2019) for

> `model card`（模型卡片）

模型的每个版本。模型卡片记录一个机器学习模型的信息，例如：

> each version of a model. A model card documents a machine learning model with information like:

- 训练算法和参数
- 训练数据来源、动机和预处理
- 评估数据来源、动机和预处理
- 预期用途和使用者
- 模型在不同人口群体或其他群体以及环境

> training algorithms and parameters
> training data sources, motivation, and preprocessing
> evaluation data sources, motivation, and preprocessing
> intended use and users
> model performance across different demographic or other groups and envi-

情境下的表现

> ronmental situations

## 4.13 解释模型

> 4.13 Interpreting models

我们往往想知道的不仅仅是一个观测样本的正确分类结果。

> Often we want to know more than just the correct classification of an observation.

我们想知道分类器为什么做出它所做出的决策。也就是说，我们希望自己的决策是可解释的。可解释性很难严格定义，但其

> We want to know why the classifier made the decision it did. That is, we want our decision to be interpretable. Interpretability can be hard to define strictly, but the

> `interpretable`（可解释的）

核心思想是，作为人类，我们应当知道自己的算法为何得出它们所得出的结论。由于逻辑回归的特征通常由人工设计，理解分类器决策的一种方式是理解每个特征在决策中扮演的角色。逻辑回归可以与统计检验（似然比检验或 Wald 检验）结合使用；用其中一种检验考察某个特征是否显著，或检视其量级（与该特征相关联的权重 w 有多大？）有助于我们解释分类器为何做出它所做出的决策。这对构建透明的模型极为重要。

> core idea is that as humans we should know why our algorithms reach the conclusions they do. Because the features to logistic regression are often human-designed, one way to understand a classifier’s decision is to understand the role each feature plays in the decision. Logistic regression can be combined with statistical tests (the likelihood ratio test, or the Wald test); investigating whether a particular feature is significant by one of these tests, or inspecting its magnitude (how large is the weight w associated with the feature?) can help us interpret why the classifier made the decision it makes. This is enormously important for building transparent models.

此外，除了用作分类器之外，逻辑回归在 NLP 和

> Furthermore, in addition to its use as a classifier, logistic regression in NLP and
许多其他领域中被广泛用作分析工具，用于检验关于各种解释变量（特征）效应的假设。在文本分类中，我们也许想知道逻辑上的否定词（no、not、never）是否更可能与负面情感相关联，或者电影的负面评论是否更可能讨论摄影。然而，这样做时必须控制潜在的混杂因素：其他可能影响情感的因素（电影类型、拍摄年份，或许还有评论的词数长度）。又或者我们可能在研究 NLP 抽取的语言特征与非语言结果（再入院、政治结果或产品销售）之间的关系，但需要控制混杂因素（患者年龄、投票所在县、产品品牌）。在这类情况下，逻辑回归让我们能够检验某个特征是否在其他特征效应之外仍与某个结果相关联。

> many other fields is widely used as an analytic tool for testing hypotheses about the effect of various explanatory variables (features). In text classification, perhaps we want to know if logically negative words (no, not, never) are more likely to be associated with negative sentiment, or if negative reviews of movies are more likely to discuss the cinematography. However, in doing so it’s necessary to control for potential confounds: other factors that might influence sentiment (the movie genre, the year it was made, perhaps the length of the review in words). Or we might be studying the relationship between NLP-extracted linguistic features and non-linguistic outcomes (hospital readmissions, political outcomes, or product sales), but need to control for confounds (the age of the patient, the county of voting, the brand of the product). In such cases, logistic regression allows us to test whether some feature is associated with some outcome above and beyond the effect of other features.

## 4.14 进阶：正则化

> 4.14 Advanced: Regularization

Numquam ponenda est pluralitas sine necessitate“除非必要，绝不应提出多样性”

> Numquam ponenda est pluralitas sine necessitate‘Plurality should never be proposed unless needed’

> 奥卡姆的威廉
>
> *William of Occam*

学习使模型与训练数据完美匹配的权重存在一个问题。如果某个特征恰巧只出现在一个类别中，因而对结果具有完美的预测性，它就会被赋予非常高的权重。特征的权重会试图完美拟合训练集的细节，事实上是过于完美，从而把只是碰巧与类别相关的噪声因素也建模进来。这个问题称为过拟合。一个好的模型应当能够从训练

> There is a problem with learning weights that make the model perfectly match the training data. If a feature is perfectly predictive of the outcome because it happens to only occur in one class, it will be assigned a very high weight. The weights for features will attempt to perfectly fit details of the training set, in fact too perfectly, modeling noisy factors that just accidentally correlate with the class. This problem is called overfitting. A good model should be able to generalize well from the training

> `overfitting generalize`（过拟合 泛化）

数据很好地泛化到未见过的测试集，但过拟合的模型泛化能力会很差。

> data to the unseen test set, but a model that overfits will have poor generalization.

为避免过拟合，在式 4.21 的损失函数中加入一个新的正则化项 R(θ)，得到一批 m 个样本的如下损失（相对式 4.21 略有改写，改为最大化对数概率而非最小化损失，并去掉了不影响 argmax 的 1 m 项）：

> To avoid overfitting, a new regularization term R(θ) is added to the loss function in Eq. 4.21, resulting in the following loss for a batch of m examples (slightly rewritten from Eq. 4.21 to be maximizing log probability rather than minimizing loss, and removing the 1 m term which doesn’t affect the argmax):

> m

ˆθ = argmax X

$$\text{log} P ( y ^{( i )} | x ^{( i )} ) - α R ( θ )$$

> θ i=1

新的正则化项 R(θ) 用于惩罚大的权重。因此，一个与训练数据完美匹配——但为此使用了许多取值很高的权重——的权重设置，会比一个与数据匹配程度稍差、但使用较小权重的设置受到更大的惩罚。正则化强度参数 α 越高，模型的权重就越低，从而减少对训练数据的依赖。注意，正则化通常不施加于偏置项，偏置项充当一种阈值，有助于处理未中心化的数据和类别先验。

> The new regularization term R(θ) is used to penalize large weights. Thus a setting of the weights that matches the training data perfectly— but uses many weights with high values to do so—will be penalized more than a setting that matches the data a little less well, but does so using smaller weights. The higher the regularization strength parameter α, the lower the model’s weights will be, reducing its reliance on the training data. Note that regularization is not normally applied to the bias term, which acts as a kind of threshold that helps deal with uncentered data and class priors.

计算这个正则化项 R(θ) 有两种常见方式。L2 正则化是权重值的二次函数，之所以这样命名，是因为它使用了

> There are two common ways to compute this regularization term R(θ). L2 regularization is a quadratic function of the weight values named because it uses the

> `L2`

> `regularization`（正则化）

权重值的 L2 范数的（平方）。L2 范数 ||θ||2 等同于向量 θ 到原点的欧氏距离。如果 θ 由 n 个权重构成，那么：

> (square of the) L2 norm of the weight values. The L2 norm, ||θ||2, is the same as the Euclidean distance of the vector θ from the origin. If θ consists of n weights, then:

> n

$$\sum_{j = 1}^{n}$$

R(θ) = ||θ||2 θ 2

$$_{2} ^{2} =$$

> j

> j=1

L2 正则化后的损失函数变为：

> The L2 regularized loss function becomes:

" m #
ˆθ = argmax X X
logP(y(i)|x(i);θ) θ 2 (4.51)
−α

> n

> j

> θ i=1 j=1

> `L1`

L1 正则化是权重值的线性函数，其名称来自 L1 范数

> L1 regularization is a linear function of the weight values, named after the L1 norm

> `regularization`（正则化）

||W||1，即权重绝对值之和，或称曼哈顿距离（曼哈顿距离是指在像纽约这样有街道网格的城市中，两点之间必须步行的距离）：

> ||W||1, the sum of the absolute values of the weights, or Manhattan distance (the Manhattan distance is the distance you’d have to walk between two points in a city with a street grid like New York):

> n

$$\sum_{i = 1}^{n}$$

$$R ( θ ) = || θ || _{1} =$$

$$| θ _{i} |$$

> i=1

L1 正则化后的损失函数变为：

> The L1 regularized loss function becomes:

" m #
ˆθ = argmax X X

> n

$$\text{log} P ( y ^{( i )} | x ^{( i )} ; θ )$$

−α |θj|
这类正则化来自统计学，其中 L1 正则化被称为 lasso 回归（Tibshirani, 1996），L2 正则化被称为 ridge 回归，

> These kinds of regularization come from statistics, where L1 regularization is called lasso regression (Tibshirani, 1996) and L2 regularization is called ridge regression,

> θ i=1 j=1

> `lasso`

两者都常用于语言处理。L2 正则化更容易

> and both are commonly used in language processing. L2 regularization is easier to

> `ridge`

优化，因为它的导数很简单（θ 2 的导数就是 2θ），而 L1 正则化更复杂（|θ| 的导数在零点处不连续）。

> optimize because of its simple derivative (the derivative of θ 2 is just 2θ), while L1 regularization is more complex (the derivative of |θ| is non-continuous at zero).

不过，L2 偏好包含许多小权重的权重向量，而 L1 偏好稀疏解，即少数权重较大、但更多得多的权重被置为零。因此 L1 正则化会带来稀疏得多的权重向量，也就是特征数量少得多。同样地，对于这两类正则化，我们通常忽略偏置项，只考虑其余权重。

> But while L2 prefers weight vectors with many small weights, L1 prefers sparse solutions with some larger weights but many more weights set to zero. Thus L1 regularization leads to much sparser weight vectors, that is, far fewer features. Again, for both these types of regularization we generally ignore the bias term and only consider the other weights.

L1 和 L2 正则化都具有贝叶斯解释，即对

> Both L1 and L2 regularization have Bayesian interpretations as constraints on
权重应当呈现何种形态的先验施加约束。L1 正则化可以看作对权重施加拉普拉斯先验。L2 正则化对应于假设权重服从均值为 µ = 0 的高斯分布。在高斯分布或正态分布中，一个值离均值越远，其概率越低（按方差 σ 缩放）。通过对权重使用高斯先验，我们是在说权重偏好取值为 0。权重 θj 的高斯分布为

> the prior of how weights should look. L1 regularization can be viewed as a Laplace prior on the weights. L2 regularization corresponds to assuming that weights are distributed according to a Gaussian distribution with mean µ = 0. In a Gaussian or normal distribution, the further away a value is from the mean, the lower its probability (scaled by the variance σ). By using a Gaussian prior on the weights, we are saying that weights prefer to have the value 0. A Gaussian for a weight θj is
!

1 −(θj −µj)2
exp (4.54)
q 2σ2 2πσ2
如果我们对每个权重乘以一个作用于该权重的高斯先验，那么我们就相当于在最大化如下约束：

> If we multiply each weight by a Gaussian prior on the weight, we are thus maximizing the following constraint:

> j j

!

> m n

ˆθ = argmax Y Y 1 −(θ j −µj)2
P(y(i)|x(i))× exp (4.55)
q 2σ2 2πσ2
在对数空间下，令 µ = 0 并假设 2σ2 = 1，这对应于

> which in log space, with µ = 0, and assuming 2σ2 = 1, corresponds to
ˆθ = argmax X X
logP(y(i)|x(i))−α θ 2 (4.56)
其形式与式 4.51 相同。

> which is in the same form as Eq. 4.51.

> θ i=1 j=1 j j

> m n

> j

> θ i=1 j=1

## 4.15 进阶：推导梯度方程

> 4.15 Advanced: Deriving the Gradient Equation

本节给出逻辑回归中交叉熵损失函数 LCE 的梯度推导。我们先快速复习一些微积分知识。

> In this section we give the derivation of the gradient of the cross-entropy loss function LCE for logistic regression. Let’s start with some quick calculus refreshers.

首先，ln(x) 的导数：

> First, the derivative of ln(x):

dx ln(x) = 1 d (4.57)
x
其次，sigmoid 的（非常优雅的）导数：

> Second, the (very elegant) derivative of the sigmoid:

dσ(z)
= σ(z)(1−σ(z)) (4.58)
dz
最后是导数的链式法则。假设我们正在计算一个导数

> Finally, the chain rule of derivatives. Suppose we are computing the derivative

> `chain rule`（链式法则）

复合函数 f(x) = u(v(x)) 的导数。f(x) 的导数是 u(x) 关于 v(x) 的导数与 v(x) 关于 x 的导数的乘积：

> of a composite function f(x) = u(v(x)). The derivative of f(x) is the derivative of u(x) with respect to v(x) times the derivative of v(x) with respect to x:

d f dx = du dv · dv (4.59)
dx
首先，我们要知道损失函数关于单个权重的导数

> First, we want to know the derivative of the loss function with respect to a single
权重 w j（我们需要对每个权重以及偏置都计算它）：

> weight w j (we’ll need to compute it for each weight, and for the bias):

∂LCE ∂
= −[ylogσ(w ·x+b)+(1−y)log(1−σ(w ·x+b))]
∂w j ∂w j
∂
= − ylogσ(w ·x+b)+ ∂ (1−y)log[1−σ(w ·x+b)]
∂wj ∂wj (4.60)
接下来，利用链式法则，并借助 log 的导数：

> Next, using the chain rule, and relying on the derivative of log:

∂LCE y ∂ 1−y ∂
= − σ(w ·x+b)− [1−σ(w ·x+b)]
∂wj σ(w ·x+b) ∂w j 1−σ(w ·x+b) ∂wj (4.61)
整理各项：

> Rearranging terms:

∂LCE  y 1−y  ∂
= − σ(w ·x+b) − σ(w ·x+b)
∂w j 1−σ(w ·x+b) ∂wj
现在代入 sigmoid 的导数，并再次使用链式法则，我们最终得到式 4.62：

> And now plugging in the derivative of the sigmoid, and using the chain rule one more time, we end up with Eq. 4.62:

∂LCE  y−σ(w ·x+b)  σ(w ·x+b)[1−σ(w ·x+b)]∂(w ·x+b)∂wj = − σ(w ·x+b)[1−σ(w ·x+b)] ∂wj
y−σ(w ·x+b)
= − σ(w ·x+b)[1−σ(w ·x+b)]xj
σ(w ·x+b)[1−σ(w ·x+b)]
= −[y−σ(w ·x+b)]xj= [σ(w ·x+b)−y]xj (4.62)

## 4.16 小结

> 4.16 Summary

本章介绍了用于分类的逻辑回归模型。

> This chapter introduced the logistic regression model of classification.

- 逻辑回归是一种有监督机器学习分类器，它从输入中提取实值特征，将每个特征乘以一个权重，再求和，并将该和通过 sigmoid 函数以生成概率。最后使用阈值做出决策。
- 逻辑回归既可用于两个类别（例如正面和负面情感），也可用于多个类别（多项逻辑回归，例如用于多元文本分类、词性标注等）。
- 多项逻辑回归使用 softmax 函数来计算概率。
- 权重（向量 w 和偏置 b）通过一个必须被最小化的损失函数（如交叉熵损失）从带标签的训练集中学习得到。
- 最小化该损失函数是一个凸优化问题，可使用梯度下降等迭代算法来寻找最优权重。
- 使用正则化以避免过拟合。
- 逻辑回归也是最有用的分析工具之一，因为它能够透明地研究各个特征的重要性。

> Logistic regression is a supervised machine learning classifier that extracts real-valued features from the input, multiplies each by a weight, sums them, and passes the sum through a sigmoid function to generate a probability. A threshold is used to make a decision.
> Logistic regression can be used with two classes (e.g., positive and negative sentiment) or with multiple classes (multinomial logistic regression, for example for n-ary text classification, part-of-speech labeling, etc.).
> Multinomial logistic regression uses the softmax function to compute probabilities.
> The weights (vector w and bias b) are learned from a labeled training set via a loss function, such as the cross-entropy loss, that must be minimized.
> Minimizing this loss function is a convex optimization problem, and iterative algorithms like gradient descent are used to find the optimal weights.
> Regularization is used to avoid overfitting.
> Logistic regression is also one of the most useful analytic tools, because of its ability to transparently study the importance of individual features.

## 历史注记

> Historical Notes

逻辑回归是在统计学领域发展起来的，到 20 世纪 60 年代已被用于二值数据分析，并在医学中尤为常见（Cox, 1969）。从 20 世纪 70 年代末开始，它作为语言变异研究的形式化基础之一，在语言学中得到广泛使用（Sankoff and Labov, 1979）。

> Logistic regression was developed in the field of statistics, where it was used for the analysis of binary data by the 1960s, and was particularly common in medicine(Cox, 1969). Starting in the late 1970s it became widely used in linguistics as one of the formal foundations of the study of linguistic variation (Sankoff and Labov, 1979).

尽管如此，逻辑回归直到 20 世纪 90 年代才在自然语言处理中变得普遍，当时它似乎同时从两个方向出现。第一个来源是相邻的信息检索和语音处理领域，这两个领域都曾使用回归，也都为 NLP 提供了许多其他统计技术。事实上，逻辑回归用于文档路由的一个极早期应用，是最早使用（LSI）嵌入作为词表示的 NLP 应用之一（Sch¨utze et al., 1995）。

> Nonetheless, logistic regression didn’t become common in natural language processing until the 1990s, when it seems to have appeared simultaneously from two directions. The first source was the neighboring fields of information retrieval and speech processing, both of which had made use of regression, and both of which lent many other statistical techniques to NLP. Indeed a very early use of logistic regression for document routing was one of the first NLP applications to use (LSI) embeddings as word representations (Sch¨utze et al., 1995).

与此同时，在 20 世纪 90 年代初，逻辑回归在 IBM Research 以最大熵建模（maximum entropy modeling）或

> At the same time in the early 1990s logistic regression was developed and applied to NLP at IBM Research under the name maximum entropy modeling or

> `maximum entropy`（最大熵）

maxent 之名被开发并应用于 NLP（Berger et al., 1996），似乎独立于统计学文献。在这一名称下，它被应用于语言建模（Rosenfeld, 1996）、词性标注（Ratnaparkhi, 1996）、句法分析（Ratnaparkhi, 1997）、指代消解（Kehler, 1997b）和文本分类（Nigam et al., 1999）。

> maxent (Berger et al., 1996), seemingly independent of the statistical literature. Under that name it was applied to language modeling (Rosenfeld, 1996), part-of-speech tagging (Ratnaparkhi, 1996), parsing (Ratnaparkhi, 1997), coreference resolution(Kehler, 1997b), and text classification (Nigam et al., 1999).

有各种文献涵盖了多种文本分类

> There are a variety of sources covering the many kinds of text classification
任务。关于情感分析，参见 Pang and Lee (2008) 以及 Liu and Zhang (2012)。

> tasks. For sentiment analysis see Pang and Lee (2008), and Liu and Zhang (2012).

Stamatatos (2009) 综述了作者归属算法。关于语种识别，参见 Jauhiainen et al. (2019)；Jaech et al. (2016) 是一个重要的早期神经网络系统。新闻专线索引任务常被用作文本分类算法的测试用例，其基于 Reuters-21578 新闻专线文章集合。

> Stamatatos (2009) surveys authorship attribution algorithms. On language identification see Jauhiainen et al. (2019); Jaech et al. (2016) is an important early neural system. The task of newswire indexing was often used as a test case for text classification algorithms, based on the Reuters-21578 collection of newswire articles.

关于文本分类，参见 Manning et al. (2008) 以及 Aggarwal and Zhai (2012)；

> See Manning et al. (2008) and Aggarwal and Zhai (2012) on text classification;

一般的分类问题在机器学习教科书中有所涵盖（Hastie et al. 2001, Witten and Frank 2005, Bishop 2006, Murphy 2012）。

> classification in general is covered in machine learning textbooks (Hastie et al. 2001, Witten and Frank 2005, Bishop 2006, Murphy 2012).

用于计算统计显著性的非参数方法最早被使用于

> Non-parametric methods for computing statistical significance were used first in
NLP 中的 MUC 竞赛（Chinchor et al., 1993），甚至在更早的语音识别中（Gillick and Cox 1989, Bisani and Ney 2004）。我们对自助法的描述借鉴了 Berg-Kirkpatrick et al. (2012) 中的描述。近期工作关注的问题包括多个测试集和多种评价指标（Søgaard et al. 2014, Dror et al. 2017）。

> NLP in the MUC competition (Chinchor et al., 1993), and even earlier in speech recognition (Gillick and Cox 1989, Bisani and Ney 2004). Our description of the bootstrap draws on the description in Berg-Kirkpatrick et al. (2012). Recent work has focused on issues including multiple test sets and multiple metrics (Søgaard et al. 2014, Dror et al. 2017).

特征选择是一种去除不太可能具有良好泛化能力的特征的方法

> Feature selection is a method of removing features that are unlikely to generalize
。特征通常按其对于分类决策的信息量大小进行排序。一个非常常用的指标——信息增益，告诉我们多少比特的

> well. Features are generally ranked by how informative they are about the classification decision. A very common metric, information gain, tells us how many bits of

> `information gain`（信息增益）

信息，即该词的出现为我们猜测类别所提供的信息。其他特征选择指标包括 χ2、逐点互信息（pointwise mutual information）和 GINI 指数；比较参见 Yang and Pedersen (1997)，特征选择入门参见 Guyon and Elisseeff (2003)。

> information the presence of the word gives us for guessing the class. Other feature selection metrics include χ2, pointwise mutual information, and GINI index; see Yang and Pedersen (1997) for a comparison and Guyon and Elisseeff (2003) for an introduction to feature selection.

## 练习

> Exercises

4.1 为什么微平均精确率总是必须等于微平均

> 4.1 Why must the microaverage precision always be equal to the microaverage
召回率？

> recall?

4.2 一个垃圾邮件分类器在 1,000 封电子邮件上运行，其中 40 封是垃圾邮件。它将 30

> 4.2 A spam classifier is run on 1,000 emails, of which 40 are spam. It labels 30
封电子邮件标记为垃圾邮件，其中 24 封确实如此。计算准确率、精确率、召回率和 F1 值。然后计算一个将所有邮件都标记为非垃圾邮件的分类器的准确率。哪个指标最有用，为什么？

> emails as spam, 24 of which really are. Compute accuracy, precision, recall, and F1. Then compute the accuracy of a classifier that labels everything as not-spam. Which metric is most useful and why?

4.3 用一个负训练样本（y = 0，令 x = [2,5]）重做第 4.6.3 节的梯度下降步骤，使用相同的初始权重和 η = 0.1。报告新的 w1、w2、b，并验证 w2 的移动方向与该节末尾正文所预测的一致。

> 4.3 Redo the gradient-descent step of Section 4.6.3 with a negative training example (y = 0, let x = [2,5], same initial weights and η = 0.1. Report the new w1, w2, b, and verify that w2 has moved in the direction the text predicts at the end of the section.
