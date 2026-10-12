# 第 6 章 神经网络

### 章

> CHAPTER

# 6 神经网络

> 6 Neural Networks

“这类机器在单元数量很大时，能够表现出极其复杂的行为。”

> “[M]achines of this character can behave in a very complicated manner when the number of units is large.”

> 艾伦·图灵（Alan Turing，1948）《智能机器》（Intelligent Machines），第 6 页
>
> *Alan Turing (1948) “Intelligent Machines”, page 6*

神经网络是语言处理的一种基础计算工具，而且是一种非常古老的工具。它们之所以被称为神经（neural）网络，是因为其起源在于 McCulloch-Pitts 神经元（McCulloch and Pitts, 1943）——它是生物神经元的一种简化模型，把神经元视为某种可以用命题逻辑描述的计算元件。但它在语言处理中的现代用法已不再借鉴这些早期的生物学灵感。

> Neural networks are a fundamental computational tool for language processing, and a very old one. They are called neural because their origins lie in the McCulloch-Pitts neuron (McCulloch and Pitts, 1943), a simplified model of the biological neuron as a kind of computing element that could be described in terms of propositional logic. But the modern use in language processing no longer draws on these early biological inspirations.

相反，现代神经网络是由小型计算单元构成的网络，其中每个

> Instead, a modern neural network is a network of small computing units, each

单元接收一个输入值向量，并产生单个输出值。本章我们介绍应用于分类的神经网络。我们介绍的架构称为前馈网络（feedforward network），因为计算是从一层单元迭代地推进到下一层。现代神经网络的使用常被称为深度学习（deep learning），因为现代网络往往很深（有很多层）。

> of which takes a vector of input values and produces a single output value. In this chapter we introduce the neural net applied to classification. The architecture we introduce is called a feedforward network because the computation proceeds iteratively from one layer of units to the next. The use of modern neural nets is often called deep learning, because modern networks are often deep (have many layers).

> 前馈
>
> *feedforward*

> 深度学习
>
> *deep learning*

神经网络与逻辑回归共用许多相同的数学工具。但

> Neural networks share much of the same mathematics as logistic regression. But

神经网络是比逻辑回归更强大的分类器，事实上可以证明，一个极小的神经网络（严格地说，是只有一个“隐藏层”的神经网络）能够学习任意函数。

> neural networks are a more powerful classifier than logistic regression, and indeed a minimal neural network (technically one with a single ‘hidden layer’) can be shown to learn any function.

神经网络分类器与逻辑回归还有另一处不同。在

> Neural net classifiers are different from logistic regression in another way. With

逻辑回归中，我们基于领域知识开发出许多种丰富的特征模板，从而把回归分类器应用到许多不同的任务上。而在使用神经网络时，更常见的做法是避免大多数对丰富的人工设计特征的使用，转而构建以原始 token 为输入、并在学习分类的过程中学会诱导出特征的神经网络。我们在第 5 章已经看到过这种用于嵌入的表示学习的例子，等我们开始研究深度 transformer 网络时，还会看到大量例子。非常深的网络尤其擅长表示学习。因此，对于有足够数据来自动学习特征的任务，深度神经网络是合适的工具。

> logistic regression, we applied the regression classifier to many different tasks by developing many rich kinds of feature templates based on domain knowledge. When working with neural networks, it is more common to avoid most uses of rich handderived features, instead building neural networks that take raw tokens as inputs and learn to induce features as part of the process of learning to classify. We saw examples of this kind of representation learning for embeddings in Chapter 5, and we’ll see lots of examples once we start studying deep transformer networks. Nets that are very deep are particularly good at representation learning. For that reason deep neural nets are the right tool for tasks that offer sufficient data to learn features automatically.

本章我们将介绍作为分类器的前馈网络，首先使用

> In this chapter we’ll introduce feedforward networks as classifiers, first with

人工构建的特征，然后使用我们在第 5 章研究过的嵌入。

> hand-built features, and then using the embeddings that we studied in Chapter 5.

在后续各章中，我们将介绍许多其他类型的神经模型，最重要的是 transformer 与注意力机制（第 7 章），此外还有循环神经网络（第 14 章）和卷积神经网络（第 16 章）。而在下一章，我们将介绍神经大语言模型这一范式。

> In subsequent chapters we’ll introduce many other kinds of neural models, most importantly the transformer and attention (Chapter 7), but also recurrent neural networks (Chapter 14) and convolutional neural networks (Chapter 16). And in the next chapter we’ll introduce the paradigm of neural large language models.

152 第 6 章 • 神经网络

> 152 CHAPTER 6 • NEURAL NETWORKS

## 6.1 单元

> 6.1 Units

神经网络的构建模块是单个计算单元。一个单元接收一组实数值作为输入，对它们进行某种计算，并产生一个输出。

> The building block of a neural network is a single computational unit. A unit takes a set of real valued numbers as input, performs some computation on them, and produces an output.

从本质上说，神经单元是在对其输入求加权和，并在和中多加一项，称为偏置项（bias term）。给定一组输入 x1...xn，一个单元有

> At its heart, a neural unit is taking a weighted sum of its inputs, with one additional term in the sum called a bias term. Given a set of inputs x1...xn, a unit has

> 偏置项
>
> *bias term*

一组对应的权重 w1...wn 和一个偏置 b，因此加权和 z 可以表示为：

> a set of corresponding weights w1...wn and a bias b, so the weighted sum z can be represented as:

X

z = b+ wixi (6.1)

> i

用向量记法来表达这个加权和通常更方便；回忆线性代数可知，向量本质上只是一个数的列表或数组。因此

> Often it’s more convenient to express this weighted sum using vector notation; recall from linear algebra that a vector is, at heart, just a list or array of numbers. Thus

> 向量
>
> *vector*

我们将用权重向量 w、标量偏置 b 和输入向量 x 来讨论 z，并把求和替换为方便的向量点积：

> we’ll talk about z in terms of a weight vector w, a scalar bias b, and an input vector x, and we’ll replace the sum with the convenient dot product:

z = w ·x+b (6.2)

如式 6.2 所定义，z 只是一个实数值。

> As defined in Eq. 6.2, z is just a real valued number.

最后，神经单元不是把 z 这个 x 的线性函数作为输出，而是

> Finally, instead of using z, a linear function of x, as the output, neural units

对 z 施加一个非线性函数 f。我们把该函数的输出称为该单元的激活值（activation value），记作 a。由于我们只是在建模单个单元，该

> apply a non-linear function f to z. We will refer to the output of this function as the activation value for the unit, a. Since we are just modeling a single unit, the

> 激活
>
> *activation*

节点的激活实际上就是网络的最终输出，我们通常称之为 y。因此值 y 定义为：

> activation for the node is in fact the final output of the network, which we’ll generally call y. So the value y is defined as:

y = a = f(z)

下文我们将讨论三种常用的非线性函数 f（sigmoid、tanh，以及修正线性单元或 ReLU），但从教学角度更方便的是从 sigmoid 函数开始，因为我们在第 4 章已经见过它：

> We’ll discuss three popular non-linear functions f below (the sigmoid, the tanh, and the rectified linear unit or ReLU) but it’s pedagogically convenient to start with the sigmoid function since we saw it in Chapter 4:

> sigmoid

1

y = σ(z) = (6.3)

1+e−z

sigmoid（如图 6.1 所示）有许多优点；它把输出

> The sigmoid (shown in Fig. 6.1) has a number of advantages; it maps the output

映射到区间 (0,1) 内，这有助于把异常值压缩向 0 或 1。而且它是可导的，正如我们在第 4.15 节所见，这对学习很有帮助。

> into the range (0,1), which is useful in squashing outliers toward 0 or 1. And it’s differentiable, which as we saw in Section 4.15 will be handy for learning.

|  |  |
| --- | --- |
| 图 6.1<br>Figure 6.1 | sigmoid 函数接受一个实数值，并将其映射到区间 (0,1)。它<br>The sigmoid function takes a real value and maps it to the range (0,1). It is |

![](images/img_57.png)

> 在 0 附近近似线性，但异常值会被压缩向 0 或 1。
>
> *nearly linear around 0 but outlier values get squashed toward 0 or 1.*

把式 6.2 代入式 6.3，就得到神经单元的输出：

> Substituting Eq. 6.2 into Eq. 6.3 gives us the output of a neural unit:

6.1 • 单元 153

> 6.1 • UNITS 153

1

y = σ(w ·x+b) = (6.4)

1+exp(−(w ·x+b))

图 6.2 给出了一个基本神经单元的最终示意图。在这个例子中，该单元

> Fig. 6.2 shows a final schematic of a basic neural unit. In this example the unit

接收 3 个输入值 x1、x2 和 x3，并计算加权和，即把每个值分别乘以一个权重（依次为 w1、w2 和 w3），将它们与偏置项 b 相加，然后把所得的和通过 sigmoid 函数，得到一个介于 0 和 1 之间的数。

> takes 3 input values x1,x2, and x3, and computes a weighted sum, multiplying each value by a weight (w1, w2, and w3, respectively), adds them to a bias term b, and then passes the resulting sum through a sigmoid function to result in a number between 0 and 1.

| x<br>1 w 1<br>x w 2 ∑ z σ a y<br>2<br>w<br>3<br>x b<br>3<br>+1 |  |
| --- | --- |
| 图 6.2<br>Figure 6.2 | 一个神经单元，接收 3 个输入 x 1、x 2 和 x （以及一个偏置 b，我们把它表示为<br>3<br>A neural unit, taking 3 inputs x 1, x 2, and x (and a bias b that we represent as a<br>3 |

x1

> w1

> w2

z a

![](images/img_87.png)

### σ ∑

x2 y

> w3

x3

> b

> +1

> 图 6.2 一个神经单元，接收 3 个输入 x1、x2 和 x3（以及一个偏置 b，我们把它表示为取值固定在 +1 的输入的权重），并产生输出 y。我们引入了一些方便的中间变量：求和的结果 z，以及 sigmoid 的输出 a。在此情形下，单元的输出 y 与 a 相同，但在更深的网络中，我们会用 y 表示整个网络的最终输出，而把 a 留作单个节点的激活值。
>
> *Figure 6.2 A neural unit, taking 3 inputs x1, x2, and x3 (and a bias b that we represent as a weight for an input clamped at +1) and producing an output y. We include some convenient intermediate variables: the output of the summation, z, and the output of the sigmoid, a. In this case the output of the unit y is the same as a, but in deeper networks we’ll reserve y to mean the final output of the entire network, leaving a as the activation of an individual node.*

让我们看一个例子，以获得直观理解。假设我们有一个

> Let’s walk through an example just to get an intuition. Let’s suppose we have a

具有如下权重向量和偏置的单元：

> unit with the following weight vector and bias:

w = [0.2,0.3,0.9]

b = 0.5

这个单元对下面这个输入向量会给出什么结果：

> What would this unit do with the following input vector:

x = [0.5,0.6,0.1]

得到的输出 y 将是：

> The resulting output y would be:

1 1 1

y = σ(w ·x+b) = 1+e−(w·x+b) = 1+e−(.5∗.2+.6∗.3+.1∗.9+.5) = 1+e−0.87 = .70

在实践中，sigmoid 并不常被用作激活函数。一个与之非常相似、但几乎总是更好的函数是图 6.3a 所示的 tanh 函数；

> In practice, the sigmoid is not commonly used as an activation function. A function that is very similar but almost always better is the tanh function shown in Fig. 6.3a;

> tanh

tanh 是 sigmoid 的一个变体，取值范围从 -1 到 +1：

> tanh is a variant of the sigmoid that ranges from -1 to +1:

y = tanh(z) = ez −e−z

ez +e−z (6.5)

最简单、也许也是最常用的激活函数是修正线性单元（rectified linear unit），也称为 ReLU，如图 6.3b 所示。当 z 为正时，它就和 z 一样，

> The simplest activation function, and perhaps the most commonly used, is the rectified linear unit, also called the ReLU, shown in Fig. 6.3b. It’s just the same as z

> ReLU

否则为 0：

> when z is positive, and 0 otherwise:

y = ReLU(z) = max(z,0) (6.6)

这些激活函数具有不同的性质，使它们适用于不同 154 第 6 章 • 神经网络

> These activation functions have different properties that make them useful for differ- 154 CHAPTER 6 • NEURAL NETWORKS

| (a) (b) |  |
| --- | --- |
| 图 6.3<br>Figure 6.3 | tanh 与 ReLU 激活函数。<br>The tanh and ReLU activation functions. |

![](images/img_99.png)

![](images/img_101.png)

(a) (b)

的语言应用或网络架构。例如，tanh 函数具有良好的性质：它可平滑求导，并能把离群值映射到均值附近。而整流函数则具有良好的性质，这些性质源于它非常接近线性。在 sigmoid 或 tanh 函数中，z 的取值很高时会使 y 的取值饱和，即极其接近 1，并且其

> ent language applications or network architectures. For example, the tanh function has the nice properties of being smoothly differentiable and mapping outlier values toward the mean. The rectifier function, on the other hand, has nice properties that result from it being very close to linear. In the sigmoid or tanh functions, very high values of z result in values of y that are saturated, i.e., extremely close to 1, and have

> 饱和
>
> *saturated*

导数非常接近 0。零导数会给学习带来问题，因为正如我们将在 6.6 节看到的，我们训练网络的方式是反向传播误差信号，将网络各层的梯度（偏导数）相乘；几乎为 0 的梯度会使误差信号越来越小，直到它

> derivatives very close to 0. Zero derivatives cause problems for learning, because as we’ll see in Section 6.6, we’ll train networks by propagating an error signal backwards, multiplying gradients (partial derivatives) from each layer of the network; gradients that are almost 0 cause the error signal to get smaller and smaller until it is

> 消失
>
> *vanishing*

小到无法用于训练，这一问题被称为梯度消失问题。

> too small to be used for training, a problem called the vanishing gradient problem.

> 梯度
>
> *gradient*

整流函数不存在这个问题，因为当 z 取值较高时，ReLU 的导数是 1，而不是非常接近 0。

> Rectifiers don’t have this problem, since the derivative of ReLU for high values of z is 1 rather than very close to 0.

## 6.2 XOR 问题

> 6.2 The XOR problem

在神经网络发展的早期，人们就认识到，神经网络的强大能力与启发它们的真实神经元一样，来自将这些单元组合成更大的网络。

> Early in the history of neural networks it was realized that the power of neural networks, as with the real neurons that inspired them, comes from combining these units into larger networks.

对多层网络必要性最巧妙的论证之一，是

> One of the most clever demonstrations of the need for multi-layer networks was

Minsky 和 Papert（1969）给出的证明：单个神经单元无法计算其输入的某些非常简单的函数。考虑计算两个输入的基本逻辑函数这一任务，例如 AND、OR 和 XOR。作为提示，以下是这些函数的真值表：

> the proof by Minsky and Papert (1969) that a single neural unit cannot compute some very simple functions of its input. Consider the task of computing elementary logical functions of two inputs, like AND, OR, and XOR. As a reminder, here are the truth tables for those functions:

AND OR XOR

| y x1 x2 | y x1 x2 |
| --- | --- |

x1 x2 y x1 x2 y x1 x2 y

0 0 0 0 0 0 0 0 0 0 1 0 0 1 1 0 1 1 1 0 0 1 0 1 1 0 1 1 1 1 1 1 1 1 1 0

这个例子最初是针对感知机提出的，感知机是一种非常简单的神经

> This example was first shown for the perceptron, which is a very simple neural

> 感知机
>
> *perceptron*

单元，它具有二值输出，并以一个非常简单的阶跃函数作为其非线性激活函数。感知机的输出 y 为 0 或 1，其计算方式如下（使用与式 6.2 相同的权重 w、输入 x 和偏置 b）：

> unit that has a binary output and has a very simple step function as its non-linear activation function. The output y of a perceptron is 0 or 1, and is computed as follows (using the same weight w, input x, and bias b as in Eq. 6.2):

6.2 • XOR 问题 155

> 6.2 • THE XOR PROBLEM 155

 0, 若 w ·x+b ≤0

>  0, if w ·x+b ≤0

y = 1, 若 w ·x+b > 0 (6.7)

> y = 1, if w ·x+b > 0 (6.7)

很容易构建一个能够计算逻辑 AND 和 OR

> It’s very easy to build a perceptron that can compute the logical AND and OR

函数的感知机，这些函数作用于它的二进制输入；图 6.4 给出了所需的权重。

> functions of its binary inputs; Fig. 6.4 shows the necessary weights.

| x x<br>1 1<br>1 1<br>x 1 x 1<br>2 2<br>-1 0<br>+1 +1<br>(a) (b) |  |
| --- | --- |
| 图 6.4<br>Figure 6.4 | 用于计算逻辑函数的感知机的权重 w 和偏置 b。其中<br>The weights w and bias b for perceptrons for computing logical functions. The |

x1 x1

1 1

x2 x2

1 1

-1 0

+1 +1

(a) (b)

> 输入表示为 x1 和 x2，偏置表示为一个取值为 +1 的特殊节点，它与偏置权重 b 相乘。(a) 逻辑 AND，权重 w1 = 1、w2 = 1，偏置权重 b = −1。(b) 逻辑 OR，权重 w1 = 1、w2 = 1，偏置权重 b = 0。这些权重/偏置只是能够实现这些函数的无穷多组可能权重与偏置中的一组。
>
> *inputs are shown as x1 and x2 and the bias as a special node with value +1 which is multiplied with the bias weight b. (a) logical AND, with weights w1 = 1 and w2 = 1 and bias weight b = −1. (b) logical OR, with weights w1 = 1 and w2 = 1 and bias weight b = 0. These weights/biases are just one from an infinite number of possible sets of weights and biases that would implement the functions.*

然而事实证明，无法构建一个感知机来计算

> It turns out, however, that it’s not possible to build a perceptron to compute

逻辑 XOR！（值得花一点时间亲自试一试！）

> logical XOR! (It’s worth spending a moment to give it a try!)

这一重要结论背后的直观理解，依赖于认识到感知机是一个线性分类器。对于二维输入 x1 和 x2，感知机方程 w1x1 +w2x2 +b = 0 是一条直线的方程。（将其写成标准线性形式即可看出：x2 = (−w1/w2)x1 + (−b/w2)。）这条直线充当一条

> The intuition behind this important result relies on understanding that a perceptron is a linear classifier. For a two-dimensional input x1 and x2, the perceptron equation, w1x1 +w2x2 +b = 0 is the equation of a line. (We can see this by putting it in the standard linear format: x2 = (−w1/w2)x1 + (−b/w2).) This line acts as a

> 决策
>
> *decision*

二维空间中的决策边界，其中输出 0 赋予所有

> decision boundary in two-dimensional space in which the output 0 is assigned to all

> 边界
>
> *boundary*

位于直线一侧的输入，而输出 1 赋予位于直线另一侧的所有输入点。如果输入多于 2 个，决策边界就变成超平面而非直线，但思路是相同的：把空间划分为两个类别。

> inputs lying on one side of the line, and the output 1 to all input points lying on the other side of the line. If we had more than 2 inputs, the decision boundary becomes a hyperplane instead of a line, but the idea is the same, separating the space into two categories.

图 6.5 展示了可能的逻辑输入（00、01、10 和 11），以及所画出的直线

> Fig. 6.5 shows the possible logical inputs (00, 01, 10, and 11) and the line drawn

它由 AND 分类器和 OR 分类器的某一组可能参数确定。注意，根本无法画出一条直线把 XOR 的正例（01 和 10）

> by one possible set of parameters for an AND and an OR classifier. Notice that there is simply no way to draw a line that separates the positive cases of XOR (01 and 10)

> 线性地
>
> *linearly*

与负例（00 和 11）分开。我们说 XOR 不是一个线性可分的

> from the negative cases (00 and 11). We say that XOR is not a linearly separable

> 可分
>
> *separable*

函数。当然，我们可以用一条曲线或其他某种函数来画出边界，但不能用一条直线。

> function. Of course we could draw a boundary with a curve, or some other function, but not a single line.

### 6.2.1 解决方案：神经网络

> 6.2.1 The solution: neural networks

虽然 XOR 函数无法由单个感知机计算，但可以由感知机单元组成的分层网络来计算。不过，与其用简单感知机组成的网络来看这一点，不如按照 Goodfellow 等人（2016）的做法，看看如何使用两层基于 ReLU 的单元来计算 XOR。图 6.6 展示了一个由两层神经单元处理输入的示意图。中间层（称为

> While the XOR function cannot be calculated by a single perceptron, it can be calculated by a layered network of perceptron units. Rather than see this with networks of simple perceptrons, however, let’s see how to compute XOR using two layers of ReLU-based units following Goodfellow et al. (2016). Fig. 6.6 shows a figure with the input being processed by two layers of neural units. The middle layer (called

- 有两个单元，输出层（称为 y）有一个单元。图中给出了一组权重和偏置，使网络能够正确计算 XOR 函数。

> has two units, and the output layer (called y) has one unit. A set of weights and biases are shown that allows the network to correctly compute the XOR function.

让我们逐步看一下输入 x = [0, 0] 时会发生什么。如果把每个

> Let’s walk through what happens with the input x = [0, 0]. If we multiply each

输入值乘以相应的权重、求和，再加上偏置 b，就得到向量 [0, -1]，然后应用修正线性变换，得到 h 层的输出为 [0, 0]。现在我们再次乘以权重、求和，再加上 156 第 6 章 • 神经网络

> input value by the appropriate weight, sum, and then add the bias b, we get the vector[0, -1], and we then apply the rectified linear transformation to give the output of the h layer as [0, 0]. Now we once again multiply by the weights, sum, and add the 156 CHAPTER 6 • NEURAL NETWORKS

| x x x<br>2 2 2<br>1 1 1<br>?<br>0 0 0<br>x x x<br>1 1 1<br>0 1 0 1 0 1<br>a) x1 AND x2 b) x1 OR x2 c) x1 XOR x2<br>x x x<br>2 2 2<br>1 1 1<br>?<br>0 0 0<br>x x x<br>1 1 1<br>0 1 0 1 0 1<br>a) x AND x b) x OR x c) x XOR x<br>1 2 1 2 1 2 |  |
| --- | --- |
| 图 6.5<br>Figure 6.5 | AND、OR 和 XOR 函数，横轴表示输入 x1，纵轴表示输入 x2<br>The functions AND, OR, and XOR, represented with input x on the x-axis and input x on the<br>1 2 |

x2 x2 x2

1 1 1

?

0 x1 0 x1 0 x1 0 1 0 1 0 1

- x1 AND x2 b) x1 OR x2 c) x1 XOR x2

> 图 6.5 AND、OR 和 XOR 函数，横轴为输入 x1，纵轴为输入 x2。实心圆表示感知机输出 1，空心圆表示感知机输出 0。对于 XOR，无法画出能正确分开两个类别的直线。图形风格参照 Russell 和 Norvig（2002）。
>
> *Figure 6.5 The functions AND, OR, and XOR, represented with input x1 on the x-axis and input x2 on the y-axis. Filled circles represent perceptron outputs of 1, and white circles perceptron outputs of 0. There is no way to draw a line that correctly separates the two categories for XOR. Figure styled after Russell and Norvig(2002).*

| x 1 h<br>1 1<br>1<br>1<br>y<br>1<br>1<br>-2<br>x<br>2 1 h 2 0<br>0<br>-1<br>+1 +1 |  |
| --- | --- |
| 图 6.6<br>Figure 6.6 | Goodfellow 等人（2016）给出的 XOR 解决方案。共有三个 ReLU 单元，位于<br>XOR solution after Goodfellow et al. (2016). There are three ReLU units, in |

### x1

> 1 h1 1 1

> y1

> 1 -2

### x2

> 1 h2 0 0-1

+1 +1

> 两层；我们把它们称为 h1、h2（h 表示“隐藏层”）和 y1。与之前一样，箭头上的数字表示每个单元的权重 w，而偏置 b 表示为固定为 +1 的单元上的权重，偏置权重/单元以灰色表示。
>
> *two layers; we’ve called them h1, h2 (h for “hidden layer”) and y1. As before, the numbers on the arrows represent the weights w for each unit, and we represent the bias b as a weight on a unit clamped to +1, with the bias weights/units in gray.*

偏置（此处为 0），得到数值 0。读者应自行计算其余 3 种可能的输入对，以验证所得 y 值对输入 [0, 1] 和 [1, 0] 为 1，对 [0, 0] 和 [1, 1] 为 0。

> bias (0 in this case) resulting in the value 0. The reader should work through the computation of the remaining 3 possible input pairs to see that the resulting y values are 1 for the inputs [0, 1] and [1, 0] and 0 for [0, 0] and [1, 1].

考察中间结果，即两个隐藏节点 h1 和 h2 的输出，也很有启发。

> It’s also instructive to look at the intermediate results, the outputs of the two

上一段中我们已说明，输入 x = [0, 0] 对应的 h 向量为 [0, 0]。图 6.7b 给出了全部 4 种输入下 h 层的取值。注意，两个输入点 x = [0, 1] 和 x = [1, 0]（即 XOR 输出 = 1 的两种情况）的隐藏表示被合并为同一点 h = [1, 0]。这一合并使得线性分开 XOR 的正例与负例变得容易。换句话说，我们可以把网络的隐藏层视为在构造输入的一种表示。

> hidden nodes h1 and h2. We showed in the previous paragraph that the h vector for the inputs x = [0, 0] was [0, 0]. Fig. 6.7b shows the values of the h layer for all 4 inputs. Notice that hidden representations of the two input points x = [0, 1] and x = [1, 0] (the two cases with XOR output = 1) are merged to the single point h =[1, 0]. The merger makes it easy to linearly separate the positive and negative cases of XOR. In other words, we can view the hidden layer of the network as forming a representation of the input.

在这个例子中，我们只是直接指定了图 6.6 中的权重。但对于真实的例子，

> In this example we just stipulated the weights in Fig. 6.6. But for real examples

神经网络的权重是使用第 6.6 节将要介绍的误差反向传播算法自动学习得到的。这意味着隐藏层会学习形成有用的表示。这种直觉——神经网络能够自动学习输入的有用表示——是它们的关键优势之一，我们将在后续章节中反复回到这一点。

> the weights for neural networks are learned automatically using the error backpropagation algorithm to be introduced in Section 6.6. That means the hidden layers will learn to form useful representations. This intuition, that neural networks can automatically learn useful representations of the input, is one of their key advantages, and one that we will return to again and again in later chapters.

6.3 • 前馈神经网络 157

> 6.3 • FEEDFORWARD NEURAL NETWORKS 157

| x 2 h 2<br>1 1<br>0 0<br>x<br>1 h<br>0 1 0 1 2 1<br>a) 原始的 x 空间 b) 新的（线性可分的）h 空间<br>x 2 h 2<br>1 1<br>0 0<br>x<br>1 h<br>0 1 0 1 2 1<br>a) The original x space b) The new (linearly separable) h space |  |
| --- | --- |
| 图 6.7<br>Figure 6.7 | 隐藏层形成输入的一种新表示。（b）展示了<br>The hidden layer forming a new representation of the input. (b) shows the |

x2 h2

1 1

0 x1 0 0 1 h1

0 1 2

- 原始的 x 空间 b) 新的（线性可分的）h 空间

> The original x space b) The new (linearly separable) h space

> 隐藏层 h 的表示，与 (a) 中原始输入表示 x 的对比。
>
> *representation of the hidden layer, h, compared to the original input representation x in (a).*

> 注意，输入点 [0, 1] 与输入点 [1, 0] 已被合并，从而使 XOR 的正例与负例可以被线性分离。改编自 Goodfellow et al.(2016)。
>
> *Notice that the input point [0, 1] has been collapsed with the input point [1, 0], making it possible to linearly separate the positive and negative cases of XOR. After Goodfellow et al.(2016).*

## 6.3 前馈神经网络

> 6.3 Feedforward Neural Networks

现在让我们稍更正式地介绍最简单的一种

> Let’s now walk through a slightly more formal presentation of the simplest kind of

> 前馈
>
> *feedforward*

神经网络——前馈网络。前馈网络是一种多层

> neural network, the feedforward network. A feedforward network is a multilayer

> 网络
>
> *network*

网络，其中的单元之间没有环状连接；每一层单元的输出传递到更高一层的单元，而没有任何输出回传到更低的层。（在第 14 章我们将介绍带环的网络，称为循环神经网络。）

> network in which the units are connected with no cycles; the outputs from units in each layer are passed to units in the next higher layer, and no outputs are passed back to lower layers. (In Chapter 14 we’ll introduce networks with cycles, called recurrent neural networks.)

由于历史原因，多层网络，尤其是前馈网络，

> For historical reasons multilayer networks, especially feedforward networks, are

> 多层
>
> *multi-layer*

有时被称为多层感知机（multi-layer perceptrons，MLP）；这在术语上其实是个误称，

> sometimes called multi-layer perceptrons (or MLPs); this is a technical misnomer,

> 感知机
>
> *perceptrons*

因为现代多层网络中的单元并不是感知机（感知机以

> since the units in modern multilayer networks aren’t perceptrons (perceptrons have a

> MLP

简单的阶跃函数作为激活函数，而现代网络是由具有多种非线性（如 ReLU 和 sigmoid）的单元组成的），但这一名称最终还是沿用下来了。

> simple step-function as their activation function, but modern networks are made up of units with many kinds of non-linearities like ReLUs and sigmoids), but at some point the name stuck.

简单的前馈网络有三类节点：输入单元、隐藏

> Simple feedforward networks have three kinds of nodes: input units, hidden

单元和输出单元。

> units, and output units.

图 6.8 展示了这样一幅图。输入层 x 是一个由简单标量值构成的向量，正如

> Fig. 6.8 shows a picture. The input layer x is a vector of simple scalar values just

我们在图 6.2 中所见的那样。

> as we saw in Fig. 6.2.

神经网络的核心是由隐藏单元 hi 构成的隐藏层 h，

> The core of the neural network is the hidden layer h formed of hidden units hi,

> 隐藏层
>
> *hidden layer*

其中每个隐藏单元都是 6.1 节所述的神经单元，先计算其输入的加权和，然后施加一个非线性函数。在标准架构中，每一层都是全连接的，也就是说每一层中的每个单元都把

> each of which is a neural unit as described in Section 6.1, taking a weighted sum of its inputs and then applying a non-linearity. In the standard architecture, each layer is fully-connected, meaning that each unit in each layer takes as input the outputs

> 全连接
>
> *fully-connected*

上一层所有单元的输出作为输入，并且相邻两层的每一对单元之间都有一条连接。因此每个隐藏单元都对所有输入单元求和。

> from all the units in the previous layer, and there is a link between every pair of units from two adjacent layers. Thus each hidden unit sums over all the input units.

回忆一下，单个隐藏单元的参数是一个权重向量和一个偏置。我们

> Recall that a single hidden unit has as parameters a weight vector and a bias. We

把每个单元 i 的权重向量和偏置合并为整个层的单一权重矩阵 W 和单一偏置向量 b，以此表示整个隐藏层的参数（见图 6.8）。权重矩阵 W 的每个元素 W ji 表示从第 i 个输入单元 xi 到第 j 个隐藏单元 hj 的连接的权重。

> represent the parameters for the entire hidden layer by combining the weight vector and bias for each unit i into a single weight matrix W and a single bias vector b for the whole layer (see Fig. 6.8). Each element W ji of the weight matrix W represents the weight of the connection from the ith input unit xi to the jth hidden unit hj.

对整个层的权重使用单一矩阵 W 的好处在于，

> The advantage of using a single matrix W for the weights of the entire layer is

现在前馈网络的隐藏层计算可以非常 158 第 6 章 • 神经网络

> that now the hidden layer computation for a feedforward network can be done very 158 CHAPTER 6 • NEURAL NETWORKS

| W U<br>x<br>1 y<br>1<br>h<br>1<br>h<br>x 2 y<br>2 2<br>h<br>3 …<br>…<br>…<br>x<br>n h<br>0 n<br>1<br>y<br>b n<br>+1 2<br>输入层 隐藏层 输出层<br>W U<br>x<br>1 y<br>1<br>h<br>1<br>h<br>x 2 y<br>2 2<br>h<br>3 …<br>…<br>…<br>x<br>n h<br>0 n<br>1<br>y<br>b n<br>+1 2<br>input layer hidden layer output layer |  |
| --- | --- |
| 图 6.8<br>Figure 6.8 | 一个简单的 2 层前馈网络，含一个隐藏层、一个输出层，<br>A simple 2-layer feedforward network, with one hidden layer, one output layer, |

### W U x1 y1

### h1 x2 h2 y2

### h3 … … …

### xn0 hn1

### yn2 b

### +1

> 输入层 隐藏层 输出层
>
> *input layer hidden layer output layer*

> 以及一个输入层（在计算层数时通常不把输入层计入）。
>
> *and one input layer (the input layer is usually not counted when enumerating layers).*

高效地用简单的矩阵运算完成。事实上，该计算只有三个步骤：用权重矩阵乘以输入向量 x，加上偏置向量 b，然后施加激活函数 g（例如上文定义的 sigmoid、tanh 或 ReLU 激活函数）。

> efficiently with simple matrix operations. In fact, the computation only has three steps: multiplying the weight matrix by the input vector x, adding the bias vector b, and applying the activation function g (such as the sigmoid, tanh, or ReLU activation function defined above).

因此，隐藏层的输出，即向量 h，如下所示（在本例中，我们将使用 sigmoid 函数 σ 作为激活函数）：

> The output of the hidden layer, the vector h, is thus the following (for this example we’ll use the sigmoid function σ as our activation function):

> (6.8)

h = σ(Wx+b)

注意，这里我们把 σ 函数应用于一个向量，而在式 6.3 中它是应用于一个标量。因此我们允许 σ(·)，乃至任何激活函数 g(·)，逐元素地作用于向量，于是 g[z1,z2,z3] = [g(z1),g(z2),g(z3)]。

> Notice that we’re applying the σ function here to a vector, while in Eq. 6.3 it was applied to a scalar. We’re thus allowing σ(·), and indeed any activation function g(·), to apply to a vector element-wise, so g[z1,z2,z3] = [g(z1),g(z2),g(z3)].

下面引入一些常量来表示这些向量

> Let’s introduce some constants to represent the dimensionalities of these vectors

与矩阵的维度。我们把输入层称为网络的第 0 层，并用 n0 表示输入的个数，因此 x 是一个维度为 n0 的实数向量，更正式地说 x ∈Rn0，即一个维度为 [n0 × 1] 的列向量。我们把隐藏层称为第 1 层，把输出层称为第 2 层。隐藏层的维度为 n1，因此 h ∈Rn1，并且 b ∈Rn1（因为每个隐藏单元可以取不同的偏置值）。而权重矩阵 W 的维度为 W ∈Rn1×n0，即 [n1 ×n0]。

> and matrices. We’ll refer to the input layer as layer 0 of the network, and have n0 represent the number of inputs, so x is a vector of real numbers of dimension n0, or more formally x ∈Rn0, a column vector of dimensionality [n0 × 1]. Let’s call the hidden layer layer 1 and the output layer layer 2. The hidden layer has dimensionality n1, so h ∈Rn1 and also b ∈Rn1 (since each hidden unit can take a different bias value). And the weight matrix W has dimensionality W ∈Rn1×n0, i.e.[n1 ×n0].

花点时间确认一下，式 6.8 中的矩阵乘法将  Pn0 

> Take a moment to convince yourself that the matrix multiplication in Eq. 6.8 will  Pn0 

计算出每个 h j 的值，即 σ i=1 Wjixi +b j 。

> compute the value of each h j as σ i=1 Wjixi +b j .

正如我们在 6.2 节所见，得到的值 h（既取自 hidden，也取自 hypothesis）构成了输入的一种表示。输出层的作用是接收这一新的表示 h 并计算最终输出。这个输出可以是一个实数值，但在许多情况下，网络的目标是做出某种分类决策，因此我们将重点关注分类的情形。

> As we saw in Section 6.2, the resulting value h (for hidden but also for hypothesis) forms a representation of the input. The role of the output layer is to take this new representation h and compute a final output. This output could be a realvalued number, but in many cases the goal of the network is to make some sort of classification decision, and so we will focus on the case of classification.

如果我们做的是二分类任务，例如情感分类，我们可能只有一个输出节点，其标量值 y 是正面情感相对于负面情感的概率。如果我们做的是多项分类，例如标注词性，我们可能为每个可能的词性设置一个输出节点，其输出值是该词性的概率，并且所有输出节点的值之和必须为 1。因此输出层是一个向量 y，它给出在所有输出节点上的概率分布。

> If we are doing a binary task like sentiment classification, we might have a single output node, and its scalar value y is the probability of positive versus negative sentiment. If we are doing multinomial classification, such as assigning a part-ofspeech tag, we might have one output node for each potential part-of-speech, whose output value is the probability of that part-of-speech, and the values of all the output nodes must sum to one. The output layer is thus a vector y that gives a probability distribution across the output nodes.

6.3 • 前馈神经网络 159

> 6.3 • FEEDFORWARD NEURAL NETWORKS 159

我们来看看这是如何发生的。与隐藏层一样，输出层也有一个权重

> Let’s see how this happens. Like the hidden layer, the output layer has a weight

矩阵（我们称它为 U），但有些模型在输出层不包含偏置向量 b，因此在本例中我们做简化处理，去掉偏置向量。权重矩阵与其输入向量（h）相乘，得到中间输出 z：

> matrix (let’s call it U), but some models don’t include a bias vector b in the output layer, so we’ll simplify by eliminating the bias vector in this example. The weight matrix is multiplied by its input vector (h) to produce the intermediate output z:

z = Uh

共有 n2 个输出节点，因此 z ∈Rn2，权重矩阵 U 的维度为 U ∈Rn2×n1，元素 Ui j 是从隐藏层第 j 个单元到输出层第 i 个单元的权重。

> There are n2 output nodes, so z ∈Rn2, weight matrix U has dimensionality U ∈Rn2×n1, and element Ui j is the weight from unit j in the hidden layer to unit i in the output layer.

然而，z 不能作为分类器的输出，因为它是实数值

> However, z can’t be the output of the classifier, since it’s a vector of real-valued

构成的向量，而分类所需要的却是概率向量。有一个方便的函数可以对实数向量进行归一化，我们所说的归一化是指

> numbers, while what we need for classification is a vector of probabilities. There is a convenient function for normalizing a vector of real values, by which we mean

> 归一化
>
> *normalizing*

把它转换为一个编码概率分布的向量（所有数值都介于 0 和 1 之间且总和为 1）：即我们在第 109 页看到的 softmax 函数

> converting it to a vector that encodes a probability distribution (all the numbers lie between 0 and 1 and sum to 1): the softmax function that we saw on page 109

> softmax

，见第 4 章。更一般地，对于任意维度为 d 的向量 z，softmax 定义为：

> of Chapter 4. More generally for any vector z of dimensionality d, the softmax is defined as:

exp(zi)

softmax(zi) = 1 ≤i ≤d

> (6.9)

Pd j=1 exp(z j)

因此，例如给定一个向量

> Thus for example given a vector

z = [0.6,1.1,−1.5,1.2,3.2,−1.1]，

> z = [0.6,1.1,−1.5,1.2,3.2,−1.1],

> (6.10)

softmax 函数会把它归一化为一个概率分布（四舍五入后显示）：

> the softmax function will normalize it to a probability distribution (shown rounded):

softmax(z) = [0.055,0.090,0.0067,0.10,0.74,0.010]

> (6.11)

你可能记得，在第 4 章的多项逻辑回归中，我们使用 softmax 从一个实数值向量（由权重与特征相乘再求和得到）构造概率分布。

> You may recall that we used softmax to create a probability distribution from a vector of real-valued numbers (computed from summing weights times features) in the multinomial version of logistic regression in Chapter 4.

这意味着，我们可以把具有一个隐藏层的神经网络分类器看作

> That means we can think of a neural network classifier with one hidden layer

先构建一个向量 h，作为输入的隐藏层表示，然后对网络在 h 中形成的特征运行标准的多项逻辑回归。相比之下，在第 4 章中特征主要是通过特征模板手工设计的。因此，神经网络就像多项逻辑回归，只不过：(a) 它有许多层，因为深度神经网络就像一层接一层的逻辑回归分类器；(b) 这些中间层有许多可能的激活函数（tanh、ReLU、sigmoid），而不只是 sigmoid（不过为方便起见，我们将继续用 σ 表示任意激活函数）；(c) 特征不是通过特征模板形成的，而是由网络的前面各层自行诱导出特征表示。

> as building a vector h which is a hidden layer representation of the input, and then running standard multinomial logistic regression on the features that the network develops in h. By contrast, in Chapter 4 the features were mainly designed by hand via feature templates. So a neural network is like multinomial logistic regression, but (a) with many layers, since a deep neural network is like layer after layer of logistic regression classifiers; (b) with those intermediate layers having many possible activation functions (tanh, ReLU, sigmoid) instead of just sigmoid (although we’ll continue to use σ for convenience to mean any activation function); (c) rather than forming the features by feature templates, the prior layers of the network induce the feature representations themselves.

以下是具有单个隐藏层的前馈网络的最终方程，

> Here are the final equations for a feedforward network with a single hidden layer,

它以输入向量 x 为输入，输出概率分布 y，并由权重矩阵 W 和 U 以及偏置向量 b 参数化：

> which takes an input vector x, outputs a probability distribution y, and is parameterized by weight matrices W and U and a bias vector b:

h = σ(Wx+b)

z = Uh

y = softmax(z)

> (6.12)

再顺便记住所有变量的形状：x ∈Rn0，h ∈Rn1，b ∈Rn1，W ∈Rn1×n0，U ∈Rn2×n1，输出向量 y ∈Rn2。我们把这种网络称为 2 层网络（按惯例，层数编号时不计输入层，但计输出层）。因此按这一术语，逻辑回归就是一个 1 层网络。

> And just to remember the shapes of all our variables, x ∈Rn0, h ∈Rn1, b ∈Rn1, W ∈Rn1×n0, U ∈Rn2×n1, and the output vector y ∈Rn2. We’ll call this network a 2layer network (we traditionally don’t count the input layer when numbering layers, but do count the output layer). So by this terminology logistic regression is a 1-layer network.

160 第 6 章 • 神经网络

> 160 CHAPTER 6 • NEURAL NETWORKS

### 6.3.1 前馈网络的更多细节

> 6.3.1 More details on feedforward networks

现在让我们建立一些记号，以便更容易地讨论深度超过 2 的更深网络。我们用方括号中的上标表示层编号，输入层从 0 开始。因此 W[1] 表示（第一个）隐藏层的权重矩阵，b[1] 表示（第一个）隐藏层的偏置向量。nj 表示第 j 层的单元数。我们用 g(·) 表示激活函数，中间层通常使用 ReLU 或 tanh，输出层使用 softmax。我们用 a[i] 表示第 i 层的输出，用 z[i] 表示上一层输出、权重和偏置的组合 W[i]a[i−1] + b[i]。第 0 层用于输入，因此我们更一般地把输入 x 称作 a[0]。

> Let’s now set up some notation to make it easier to talk about deeper networks of depth more than 2. We’ll use superscripts in square brackets to mean layer numbers, starting at 0 for the input layer. So W[1] will mean the weight matrix for the(first) hidden layer, and b[1] will mean the bias vector for the (first) hidden layer. nj will mean the number of units at layer j. We’ll use g(·) to stand for the activation function, which will tend to be ReLU or tanh for intermediate layers and softmax for output layers. We’ll use a[i] to mean the output from layer i, and z[i] to mean the combination of previous layer output, weights and biases W[i]a[i−1] + b[i]. The 0th layer is for inputs, so we’ll refer to the inputs x more generally as a[0].

因此我们可以把式 6.12 中的 2 层网络重新表示如下：

> Thus we can re-represent our 2-layer net from Eq. 6.12 as follows:

z[1] = W[1]a[0] +b[1] a[1] = g[1](z[1]) z[2] = W[2]a[1] +b[2] a[2] = g[2](z[2])ˆy = a[2]

> (6.13)

注意，使用这种记号后，每一层所做计算的方程都相同。因此，给定输入向量 a[0]，在 n 层前馈网络中计算前向步骤的算法就很简单：

> Note that with this notation, the equations for the computation done at each layer are the same. The algorithm for computing the forward step in an n-layer feedforward network, given the input vector a[0] is thus simply:

> for i in 1,...,n z[i] = W[i]a[i−1] +b[i] a[i] = g[i](z[i])ˆy = a[n]

为最终 softmax 之前的那组最终激活值取一个名字，往往是有用的。

> It’s often useful to have a name for the final set of activations right before the final

因此无论我们有多少层，我们一般把最终向量 z[n] 中未归一化的值，即最终 softmax 之前的分数向量，称为 logits（见式 4.7）。

> softmax. So however many layers we have, we’ll generally call the unnormalized values in the final vector z[n], the vector of scores right before the final softmax, the logits (see Eq. 4.7).

> logits

非线性激活函数的必要性 我们在神经网络的每一层使用非线性激活函数的原因之一是，如果不这样做，所得到的网络就完全等价于单层网络。让我们看看为什么这是对的。设想这样一个纯线性层网络中前两层：

> The need for non-linear activation functions One of the reasons we use nonlinear activation functions for each layer in a neural network is that if we did not, the resulting network is exactly equivalent to a single-layer network. Let’s see why this is true. Imagine the first two layers of such a network of purely linear layers:

z[1] = W[1]x+b[1] z[2] = W[2]z[1] +b[2]

我们可以把该网络所计算的函数改写为：

> We can rewrite the function that the network is computing as:

z[2] = W[2]z[1] +b[2]

= W[2](W[1]x+b[1])+b[2]= W[2]W[1]x+W[2]b[1] +b[2]

= W′x+b′

> (6.14)

这一点可以推广到任意层数。因此，如果没有非线性激活函数，多层网络就只是权重集合不同的单层网络在记号上的一个变体，我们也就失去了多层网络的全部表示能力。

> This generalizes to any number of layers. So without non-linear activation functions, a multilayer network is just a notational variant of a single layer network with a different set of weights, and we lose all the representational power of multilayer networks.

6.4 • 面向 NLP 的前馈网络：分类 161

> 6.4 • FEEDFORWARD NETWORKS FOR NLP: CLASSIFICATION 161

替换偏置单元 在描述网络时，我们有时会使用一种略微简化的记号，它表示完全相同的函数，但不提及显式的偏置节点 b。取而代之，我们给每一层添加一个哑节点 a0，其值始终为 1。于是第 0 层即输入层将有一个哑节点 a[0] 0 = 1，第 1 层将有一个 a[1] 0 = 1，依此类推。这个哑节点仍然带有一个关联权重，该权重就代表偏置值 b。例如，我们不再使用像

> Replacing the bias unit In describing networks, we will sometimes use a slightly simplified notation that represents exactly the same function without referring to an explicit bias node b. Instead, we add a dummy node a0 to each layer whose value will always be 1. Thus layer 0, the input layer, will have a dummy node a[0] 0 = 1, layer 1 will have a[1] 0 = 1, and so on. This dummy node still has an associated weight, and that weight represents the bias value b. For example instead of an equation like

> (6.15)

h = σ(Wx+b)

这样的方程，而是使用：

> we’ll use:

> (6.16)

h = σ(Wx)

但现在我们的向量 x 不再有 n0 个值：x = x1,...,xn0，而是有 n0 +1 个值，新增一个第 0 个哑值 x0 = 1：x = x0,...,xn0。并且我们不再按如下方式计算每个 h j：

> But now instead of our vector x having n0 values: x = x1,...,xn0, it will have n0 +1 values, with a new 0th dummy value x0 = 1: x = x0,...,xn0. And instead of computing each h j as follows:

n0 ! X

> (6.17)

h j = σ Wji xi +b j ,

> i=1

而是使用：

> we’ll instead use:

n0 ! X

> (6.18)

h j = σ Wji xi ,

> i=0

其中 Wj0 的值取代了原来 b j 的位置。图 6.9 给出了一种可视化。

> where the value Wj0 replaces what had been b j. Fig. 6.9 shows a visualization.

| W U<br>W U<br>h<br>x 1 y x =1<br>1 1 0 y<br>h 1<br>1<br>h<br>x 2 2 y 2 x 1 h 2 y<br>h 2<br>3 …<br>h<br>x 3 2 … …<br>…<br>x …<br>n h 0 n …<br>1 y h<br>+1 b n 2 x n n 1 y n<br>0 2<br>(a) (b) |  |
| --- | --- |
| 图 6.9<br>Figure 6.9 | 把偏置节点（如 (a) 中所示）替换为 x（(b)）。<br>0<br>Replacing the bias node (shown in a) with x (b).<br>0 |

### W U W U

### x1 h1 y1 x0=1

### h1 y1

### x2 h2

### y2 x1 h2 y2

### h3 … x2 h3

### … … … …

### xn0 hn1

### … yn2 hn1

### b +1 xn0 yn2

(a) (b)

> 图 6.9 将偏置节点（如 (a) 所示）替换为 x0（b）。
>
> *Figure 6.9 Replacing the bias node (shown in a) with x0 (b).*

在讲解学习算法时，我们仍将继续把偏置表示为 b，

> We’ll continue showing the bias as b when we go over the learning algorithm

即第 6.6 节；但在本书后续内容中，对于大多数图和部分公式，我们将使用这种不带显式偏置项的简化记法。

> in Section 6.6, but going forward in the book, for most figures and some equations we’ll use this simplified notation without explicit bias terms.

## 6.4 用于 NLP 的前馈网络：分类

> 6.4 Feedforward networks for NLP: Classification

让我们看看如何将前馈网络应用于 NLP 分类任务。在实践中，简单的前馈网络并不是我们做文本分类的方式；对于真实应用，我们会使用更复杂的架构，比如第 9 章的 BERT transformers 162 第 6 章 • 神经网络。尽管如此，观察一个前馈网络的文本分类器，可以让我们引入一些将在本书余下部分发挥作用的关键思想，包括嵌入矩阵、表示池化和表示学习等思想。

> Let’s see how to apply feedforward networks to NLP classification tasks. In practice, simple feedforward networks aren’t the way we do text classification; for real applications we would use more sophisticated architectures like the BERT transformers 162 CHAPTER 6 • NEURAL NETWORKS of Chapter 9. Nonetheless seeing a feedforward network text classifier will let us introduce key ideas that will play a role throughout the rest of the book, including the ideas of the embedding matrix, representation pooling, and representation learning.

但在引入这些思想中的任何一个之前，让我们先从一个分类器开始，其做法是

> But before introducing any of these ideas, let’s start with a classifier by making

对第 4 章中看到的情感分类器只做最小的改动。与它们一样，我们将采用手工构建的特征，把它们送入分类器，并产生一个类别概率。唯一的区别是，我们将使用神经网络而不是逻辑回归作为分类器。

> only minimal change from the sentiment classifiers we saw in Chapter 4. Like them, we’ll take hand-built features, pass them through a classifier, and produce a class probability. The only difference is that we’ll use a neural network instead of logistic regression as the classifier.

### 6.4.1 使用手工构建特征的神经网络分类器

> 6.4.1 Neural net classifiers with hand-built features

让我们从一个简单的 2 层情感分类器开始：取第 4 章中我们的逻辑回归分类器（它对应于一个 1 层网络），只是增加一个隐藏层。输入元素 xi 可以是像图 4.2 中那样的标量特征，例如 x1 = count(words ∈doc)、x2 = count(positive lexicon words ∈doc)、x3 = 1 若 “no” ∈doc，等等，总共 d 个特征。而输出层 ˆy 可以有两个节点（分别对应正面和负面），也可以有 3 个节点（正面、负面、中性），此时 ˆy1 就是正面情感的概率估计，ˆy2 是负面的概率，ˆy3 是中性的概率。由此得到的公式正是我们在上文看到的 2 层网络公式（一如既往，我们将继续用 σ 表示任意非线性函数，无论是 sigmoid、ReLU 还是其他）。

> Let’s begin with a simple 2-layer sentiment classifier by taking our logistic regression classifier from Chapter 4, which corresponds to a 1-layer network, and just adding a hidden layer. The input element xi can be scalar features like those in Fig. 4.2, e.g., x1 = count(words ∈doc), x2 = count(positive lexicon words ∈doc), x3 = 1 if “no” ∈doc, and so on, for a total of d features. And the output layerˆy could have two nodes (one each for positive and negative), or 3 nodes (positive, negative, neutral), in which case ˆy1 would be the estimated probability of positive sentiment, ˆy2 the probability of negative and ˆy3 the probability of neutral. The resulting equations would be just what we saw above for a 2-layer network (as always, we’ll continue to use the σ to stand for any non-linearity, whether sigmoid, ReLU or other).

x = [x1,x2,...,xd]（每个 xi 都是一个手工设计的特征）

> x = [x1,x2,...,xd] (each xi is a hand-designed feature)

h = σ(Wx+b)

z = Uh

ˆy = softmax(z)

> (6.19)

图 6.10 给出了这种架构的示意图。正如我们之前提到的，把这一隐藏层加入我们的逻辑回归分类器，使网络能够表示特征之间的非线性交互。仅凭这一点，就可能让我们得到一个更好的情感分类器。

> Fig. 6.10 shows a sketch of this architecture. As we mentioned earlier, adding this hidden layer to our logistic regression classifier allows the network to represent the non-linear interactions between features. This alone might give us a better sentiment classifier.

| h1<br>dessert 词数 x<br>=3 1 y^ p(+)<br>h2 1<br>正面词典 x<br>was words = 1 2 h3 y^ 2 p(-)<br>great “no” 的计数 x y^ 3 p(neut) …<br>3<br>= 0<br>h<br>dh<br>输入词 x W U y<br>h<br>[d⨉1] [d h⨉d] [3⨉d h] [3⨉1]<br>[d h⨉1]<br>输入层 隐藏层 输出层<br>d=3 特征 softmax<br>h1<br>dessert wordcount x<br>=3 1 y^ p(+)<br>h2 1<br>positive lexicon x<br>was words = 1 2 h3 y^ 2 p(-)<br>great count of “no” x y^ 3 p(neut) …<br>3<br>= 0<br>h<br>dh<br>Input words x W U y<br>h<br>[d⨉1] [d h⨉d] [3⨉d h] [3⨉1]<br>[d h⨉1]<br>Input layer Hidden layer Output layer<br>d=3 features softmax |  |
| --- | --- |
| 图 6.10<br>Figure 6.10 | 使用传统手工构建特征的前馈网络情感分析<br>Feedforward network sentiment analysis using traditional hand-built features |

> h1

> 词数
>
> *wordcount*

> dessert x1

> ^

> =3

> y1 p(+)

> h2

> 正面词典
>
> *positive lexicon*

> was x2 ^

> y2 p(-)

> words = 1

> h3

> y3 ^

…

> p(中性)
>
> *p(neut)*

> “no” 的计数
>
> *count of “no”*

> great x3

> = 0 hdh

### x W U y

> 输入词
>
> *Input words*

### h

> [d⨉1] [dh⨉d] [dh⨉1] [3⨉dh] [3⨉1] 输入层 隐藏层 输出层 d=3 特征 softmax
>
> *[d⨉1] [dh⨉d] [dh⨉1] [3⨉dh] [3⨉1] Input layer Hidden layer Output layer d=3 features softmax*

> 输入文本的。
>
> *of the input text.*

6.5 • 作为神经网络分类器输入的词嵌入 163

> 6.5 • EMBEDDINGS AS THE INPUT TO NEURAL NET CLASSIFIERS 163

### 6.4.2 向量化以实现并行推断

> 6.4.2 Vectorizing for parallelizing inference

虽然式 6.19 展示了如何对单个样本 x 进行分类，但在实践中我们希望高效地对由 m 个样本组成的整个测试集进行分类。我们通过将这一过程向量化来实现，正如在逻辑回归中看到的那样；不再使用 for 循环逐个遍历样本，而是用矩阵乘法一次性完成整个测试集的全部计算。首先，我们把每个输入 x 的所有输入特征向量打包进单个输入矩阵 X，其中第 i 行是一个行向量，由输入样本 x(i) 的特征构成（即向量 x(i)）。如果输入特征向量的维度为 d，那么 X 是形状为 [m×d] 的矩阵。

> While Eq. 6.19 shows how to classify a single example x, in practice we want to efficiently classify an entire test set of m examples. We do this by vectorizing the process, just as we saw with logistic regression; instead of using for-loops to go through each example, we’ll use matrix multiplication to do the entire computation of an entire test set at once. First, we pack all the input feature vectors for each input x into a single input matrix X, with each row i a row vector consisting of the features for input example x(i) (i.e., the vector x(i)). If the dimensionality of our input feature vector is d, X will be a matrix of shape [m×d].

由于我们现在把每个输入建模为行向量而非列

> Because we are now modeling each input as a row vector rather than a column

向量，我们还需要对式 6.19 稍作修改。X 的形状为 [m×d]，W 的形状为 [dh ×d]，因此我们要调整 X 与 W 相乘的顺序，并对 W 转置，使它们正确相乘，得到形状为 [m×dh] 的矩阵 H。1

> vector, we also need to slightly modify Eq. 6.19. X is of shape [m×d] and W is of shape [dh ×d], so we’ll reorder how we multiply X and W and transpose W so they correctly multiply to yield a matrix H of shape [m×dh]. 1

式 6.19 中形状为 [1×dh] 的偏置向量 b 现在必须复制

> The bias vector b from Eq. 6.19 of shape [1×dh] will now have to be replicated

成形状为 [m × dh] 的矩阵。我们还需要类似地调整下一步的顺序，并对 U 转置。最后，我们的输出矩阵 ˆY 的形状为 [m × 3]（更一般地是 [m × do]，其中 do 是输出类别数），输出矩阵 ˆY 的第 i 行由输出向量 ˆy(i) 构成。下面是对整个测试集计算输出类别分布的最终公式：

> into a matrix of shape [m × dh]. We’ll need to similarly reorder the next step and transpose U. Finally, our output matrix ˆY will be of shape [m × 3] (or more generally [m × do], where do is the number of output classes), with each row i of our output matrix ˆY consisting of the output vector ˆy(i). Here are the final equations for computing the output class distribution for an entire test set:

H = σ(XW⊺+b) Z = HU⊺ˆY = softmax(Z)

> (6.20)

在本书中，我们有时会看到 WX + b 这样的顺序，有时会看到 XW + b。

> In this book, we’ll sometimes see orderings like WX + b and sometimes XW + b.

这就是为什么始终要非常清楚参与任何给定公式的权重矩阵的形状。

> That’s why it’s always important to be very aware of the shapes of your weight matrices participating in any given equation.

## 6.5 作为神经网络分类器输入的词嵌入

> 6.5 Embeddings as the input to neural net classifiers

手工构建的特征是设计分类器的传统方式，但 NLP 中大多数神经网络应用并不使用人工设计的手工特征作为输入。相反，我们借助深度学习从数据中学习特征的能力，把词元表示为嵌入。在本节中，我们用第 5 章介绍过如何计算的静态 word2vec 或 GloVe 嵌入来表示每个词元。

> While hand-built features are a traditional way to design classifiers, most applications of neural networks for NLP don’t use hand-built human-engineered features as inputs. Instead, we draw on deep learning’s ability to learn features from the data by representing tokens as embeddings. For this section we’ll represent each token by its static word2vec or GloVe embeddings that we saw how to compute in Chapter 5.

所谓静态嵌入，是指每个词元由一个固定的向量表示，我们只需训练一次，然后把它放进一个大字典中即可。当我们想要引用该词元时，就从字典中取出它的嵌入。

> By static embedding, we mean that each token is represented by a fixed vector that we train once, and then just put into a big dictionary. When we want to refer to that token, we grab its embedding out of the dictionary.

然而，当我们将神经模型应用于语言建模任务时（正如

> However when we apply neural models to the task of language modeling (as

我们将在第 7 章看到的那样），情况会更加复杂，我们将使用一种更强大的嵌入，称为上下文嵌入。同一个词每次出现在不同上下文中时，其上下文嵌入都不相同。此外，我们会让网络在词预测任务中一并学习这些嵌入。

> we’ll see in Chapter 7) the situation is more complex, and we’ll use a more powerful kind of embedding called a contextual embedding. Contextual embeddings are different for each time a word occurs in a different context. Furthermore, we’ll have the network learn these embeddings as part of the task of word prediction.

那么，让我们仍然考察上面的文本分类领域，但改用静态嵌入

> So let’s explore the text classification domain above, but using static embeddings

作为特征，而不是人工设计的特征。我们聚焦于推断阶段，

> as features instead of the hand-designed features. Let’s focus on the inference stage,

> 1

> 注意，如果我们改为让输入矩阵 X 把每个输入表示为列向量而非行向量，使其形状为 [d ×m]，那么我们本可以保持乘积的原有顺序。但在神经网络模型中，把输入表示为行向量既方便又常见。
>
> *Note that we could have kept the original order of our products if we had instead made our input matrix X represent each input as a column vector instead of a row vector, making it of shape [d ×m]. But representing inputs as row vectors is convenient and common in neural network models.*

164 第 6 章 • 神经网络

> 164 CHAPTER 6 • NEURAL NETWORKS

在其中我们已经为所有输入词元学习到了嵌入。嵌入是一个维度为 d 的向量，用于表示输入词元。存储

> in which we have already learned embeddings for all the input tokens. An embedding is a vector of dimension d that represents the input token. The dictionary of

> 嵌入
>
> *embedding*

这些嵌入的静态嵌入字典就是嵌入矩阵

> static embeddings in which we store these embeddings is the embedding matrix

> 矩阵
>
> *matrix*

- 嵌入矩阵的每一行把词汇表 V 中的每个词元表示为维度为 d 的（行）向量。由于 E 为词汇表中的 |V| 个词元各保留一行，因此 E 的形状为 [|V|×d]。每当我们把嵌入用作神经 NLP 系统的输入时，这个嵌入矩阵 E 都会发挥作用，包括我们将在接下来几章介绍的基于 Transformer 的大语言模型。

> Each row of the embedding matrix represents each token of the vocabulary V as a (row) vector of dimensionality d. Since E has a row for each of the |V| tokens in the vocabulary, E has shape [|V|×d]. This embedding matrix E plays a role whenever we are using embeddings as input to neural NLP systems, including in the transformer-based large language models we will introduce over the next chapters.

给定像 dessert was great 这样的输入词元串，我们首先把这些词元

> Given an input token string like dessert was great we first convert the tokens

转换为词汇表索引（这些索引是在我们最初使用 BPE 或 SentencePiece 对输入分词时创建的）。因此 dessert was great 的表示可能是 w = [3,524,902]。接着我们用索引从 E 中选出相应的行（第 3 行、第 524 行、第 902 行）。

> into vocabulary indices (these were created when we first tokenized the input using BPE or SentencePiece). So the representation of dessert was great might be w = [3,524,902]. Next we use indexing to select the corresponding rows from E(row 3, row 524, row 902).

从嵌入矩阵中选取词元嵌入的另一种思考方式

> Another way to think about selecting token embeddings from the embedding

是把输入词元表示为形状为 [1 × |V|] 的独热向量，即词汇表中每个词对应一个维度。回顾一下，在独热向量中，所有

> matrix is to represent input tokens as one-hot vectors of shape [1 × |V|], i.e., with one dimension for each word in the vocabulary. Recall that in a one-hot vector all

> 独热向量
>
> *one-hot vector*

除一个元素外，其余元素均为 0；那个维度正是该词在词表中索引的元素取值为 1。因此，如果单词“dessert”在词表中的索引为 3，则 x3 = 1，且对所有 i̸ = 3 有 xi = 0，如下所示：

> the elements are 0 except one, the element whose dimension is the word’s index in the vocabulary, which has value 1. So if the word “dessert” has index 3 in the vocabulary, x3 = 1, and xi = 0 ∀i̸ = 3, as shown here:

[0 0 1 0 0 0 0 ... 0 0 0 0] 1 2 3 4 5 6 7 ... ... |V|

乘以一个只有一个非零元素 xi = 1 的独热向量，只是

> Multiplying by a one-hot vector that has only one non-zero element xi = 1 simply

选出单词 i 对应的行向量，从而得到单词 i 的嵌入，如图 6.11 所示。

> selects out the relevant row vector for word i, resulting in the embedding for word i, as depicted in Fig. 6.11.

| d<br>3<br>3 \|V\| d<br>1 0 0 1 0 0 0 0 … 0 0 0 0 ✕ E = 1<br>\|V\| |  |
| --- | --- |
| 图 6.11<br>Figure 6.11 | 通过将嵌入相乘来选择单词 V3 的嵌入向量<br>Selecting the embedding vector for word V by multiplying the embedding<br>3 |

> d

> 3 |V| 3 d

### = ✕ E

| 0 0 | 1 | 0 0 0 0 … 0 0 0 0 |
| --- | --- | --- |

> 0 0 1 0 0 0 0 … 0 0 0 0

> |V|

> 图 6.11 通过将嵌入矩阵 E 与一个在第 3 个索引处为 1 的独热向量相乘，来选择单词 V3 的嵌入向量。
>
> *Figure 6.11 Selecting the embedding vector for word V3 by multiplying the embedding matrix E with a one-hot vector with a 1 in index 3.*

我们可以扩展这一思路，把整个输入 token 序列表示为一个矩阵

> We can extend this idea to represent the entire input token sequence as a matrix

该矩阵由独热向量组成，对应 N 个输入位置中的每一个，如图 6.12 所示。

> of one-hot vectors, one for each of the N input positions as shown in Fig. 6.12.

| d<br>\|V\| d<br>0 0 1 0 0 0 0 … 0 0 0 0<br>0 0 0 0 0 0 0 … 0 0 1 0 ✕ E =<br>1 0 0 0 0 0 0 … 0 0 0 0<br>… N<br>N 0 0 0 0 1 0 0 … 0 0 0 0 \|V\| |  |
| --- | --- |
| 图 6.12<br>Figure 6.12 | 通过相乘来选择输入 token id 序列 W 的嵌入矩阵<br>Selecting the embedding matrix for the input sequence of token ids W by mul- |

> d

> |V| d

| 0 0 | 1 | 0 0 0 0 … 0 0 0 0 |  |  |
| --- | --- | --- | --- | --- |
| 0 0 0 0 0 0 0 … 0 0 |  |  | 1 | 0 |
| 1 0 | 0 0 0 0 0 … 0 0 0 0 |  |  |  |

> 0 0 1 0 0 0 0 … 0 0 0 0

### =

> 0 0 0 0 0 0 0 … 0 0 1 0

### ✕ E

> 1 0 0 0 0 0 0 … 0 0 0 0

> … N

> N

| 0 0 0 0 | 1 | 0 0 … 0 0 0 0 |
| --- | --- | --- |

> 0 0 0 0 1 0 0 … 0 0 0 0

|V|

> 将 W 对应的独热矩阵与嵌入矩阵 E 相乘。
>
> *tiplying a one-hot matrix corresponding to W by the embedding matrix E.*

现在我们需要把这个由 N 个 [1×d] 嵌入组成的输入（代表一个包含 N 个 token 的窗口）分类为单个类别（例如正面或负面）。

> We now need to classify this input of N [1×d] embeddings, representing a window of N tokens, into a single class (like positive or negative).

把嵌入传给分类器有两种常见方式：拼接

> There are two common ways to pass embeddings to a classifier: concatenation

和池化。第一种方式是，取这个形状为 [N × d] 的输入，通过把所有输入向量拼接成一个形状为 [1 × dN] 的很长的向量来重塑它。然后 6.5 • 以嵌入作为神经网络分类器的输入 165 我们把这个输入传给分类器，让它做出判断。这为我们提供了大量信息，代价是要使用一个相当大的网络。第二种方式是，我们可以把

> and pooling. First, we can take this input of shape [N × d] and reshape it by concatenating all the input vectors into one very long vector of shape [1 × dN]. Then 6.5 • EMBEDDINGS AS THE INPUT TO NEURAL NET CLASSIFIERS 165 we pass this input to our classifier and let it make its decision. This gives us lots of information, at the cost of using a pretty large network. Second, we can pool the

> 池化
>
> *pool*

这 N 个嵌入汇聚成单个嵌入，然后把这个池化后的单一嵌入传给分类器。与所有原始嵌入本可包含的信息相比，池化给我们的信息更少，但优点是规模小、效率高，而且在那些不太在意原始词序的任务中特别有用。下面各举一个例子：情感任务用池化，语言建模任务用拼接。

> N embeddings into a single embedding and then pass that single pooled embedding to the classifier. Pooling gives us less information than would have been present in all the original embeddings, but has the advantage of being small and efficient and is especially useful in tasks for which we don’t care as much about the original word order. Let’s give an example of each: pooling for the sentiment task, and concatenation for the language modeling task.

为情感任务池化输入嵌入 那么我们先来看看池化如何用于情感分类任务。池化的直觉是：对于情感而言，输入的确切位置（像 great 这样的词是第一个词？还是第二个词？）不如词本身的身份重要。

> Pooling input embeddings for sentiment So let’s begin with seeing how pooling can work for the sentiment classification task. The intuition of pooling is that for sentiment, the exact position of the input (is some word like great the first word? the second word?) is less important than the identity of the word itself.

池化函数是一种把一组嵌入变成单个嵌入的方法。

> A pooling function is a way to turn a set of embeddings into a single embedding.

例如，对于包含 N 个输入词/token w1,...,wN 的文本，我们希望把

> For example, for a text with N input words/tokens w1,...,wN, we want to turn

这 N 个行嵌入 e(w1),...,e(wN)（每个维度为 d）变成单个维度同样为 d 的嵌入。

> the N row embeddings e(w1),...,e(wN) (each of dimensionality d) into a single embedding also of dimensionality d.

池化的方式有多种。最简单的是均值池化：即取均值

> There are various ways to pool. The simplest is mean-pooling: taking the mean

> 均值池化
>
> *mean-pooling*

先将嵌入求和，再除以 N：

> by summing the embeddings and then dividing by N:

> N

xmean = 1 X

e(wi)

> (6.21)

N

> i=1

以下是假设采用均值池化时该分类器的方程：

> Here are the equations for this classifier assuming mean pooling:

x = mean(e(w1),e(w2),...,e(wn))

h = σ(xW +b)

z = hU

ˆy = softmax(z)

> (6.22)

图 6.13 画出了该架构，其中也给出了所有相关矩阵的形状（注意，现在我们使用的是行向量）。

> The architecture is sketched in Fig. 6.13, where we also give the shapes for all the relevant matrices (note that we’re using row vectors now).

池化还有许多其他选择，例如最大池化（max-pooling），此时对于

> There are many other options for pooling, like max-pooling, in which case for

> 最大池化（max-pooling）
>
> *max-pooling*

每个维度，我们对所有输入取逐元素最大值。一组 N 个向量的逐元素最大值是一个新向量，其第 k 个元素是所有 N 个向量的第 k 个元素中的最大值。

> each dimension we take the element-wise max over all the inputs. The element-wise max of a set of N vectors is a new vector whose kth element is the max of the kth elements of all the N vectors.

为语言建模拼接输入嵌入 在情感分析中，我们看到了如何生成一个给出三个类别（正面、负面或中性）概率的输出向量：以 N 个输入词元的窗口为输入，先把这些词元嵌入池化为单个嵌入向量。

> Concatenating input embeddings for language modeling For sentiment analysis we saw how to generate an output vector with probabilities over three classes: positive, negative, or neutral, given as input a window of N input tokens, by first pooling those token embeddings into a single embedding vector.

现在让我们考虑语言建模：根据之前的

> Now let’s consider language modeling: predicting upcoming words from prior

词来预测即将出现的词。在这项任务中，我们同样得到 N 个输入词元的窗口，但现在的任务是预测应接在该窗口之后的下一词元。我们将借鉴 Bengio et al. (2003) 首次提出的算法，勾勒一个简单的前馈神经语言模型。前馈语言模型引入了大语言建模的许多重要概念，我们将在第 7 章再次讨论这些概念。

> words. In this task we are given the same window of N input tokens, but our task now is to predict the next token that should follow the window. We’ll sketch a simple feedforward neural language model, drawing on an algorithm first introduced by Bengio et al. (2003). The feedforward language model introduces many of the important concepts of large language modeling that we will return to in Chapter 7.

与第 3 章的 n-gram 语言模型相比，神经语言模型有许多优势。神经语言模型能够处理长得多的历史，能在相似词的上下文之间更好地泛化，并且在词语预测上准确得多。另一方面，神经网络语言模型更慢、更复杂，训练需要消耗大量能量，且可解释性不如 n-gram 模型，因此在一些较小的任务上，n-gram 语言模型仍是合适的工具。

> Neural language models have many advantages over the n-gram language models of Chapter 3. Neural language models can handle much longer histories, can generalize better over contexts of similar words, and are far more accurate at wordprediction. On the other hand, neural net language models are slower, more complex, need vast amounts of energy to train, and are less interpretable than n-gram models, so for some smaller tasks an n-gram language model is still the right tool.

166 第 6 章 • 神经网络

> 166 CHAPTER 6 • NEURAL NETWORKS

| p(+) p(-) p(neut) 输出概率<br>y y y y ^ ^ ^<br>1 2 3 [1⨉3] 输出层 softmax<br>[d h⨉3] 权重<br>U<br>h h h … h h [1⨉d h] 隐藏层<br>1 2 3 dh<br>W[d⨉d h] 权重<br>x<br>[1⨉d] 输入层<br>池化嵌入<br>+ 池化<br>“dessert” 的嵌入<br>“was” 的嵌入 N⨉d 个嵌入<br>“great” 的嵌入<br>E E E \|V\|⨉d E 矩阵<br>所有词共享<br>1 3 \|V\|<br>1 524 \|V\|<br>1 902 \|V\| N⨉\|V\| 个 one-hot 向量<br>0 0 1 00<br>0 0 01 00<br>“dessert” = V 3 “was” = V 524 “0 g0 rea0 t” 1 = V00<br>902<br>dessert was great 输入词<br>p(+) p(-) p(neut) Output probabilities<br>y y y y ^ ^ ^<br>1 2 3 [1⨉3] Output layer softmax<br>[d h⨉3] weights<br>U<br>h h h … h h [1⨉d h] Hidden layer<br>1 2 3 dh<br>W[d⨉d h] weights<br>x<br>[1⨉d] Input layer<br>pooled embedding<br>+ pooling<br>embedding for “dessert”<br>embedding for “was” N⨉d embeddings<br>embedding for “great”<br>E E E \|V\|⨉d E matrix<br>shared across words<br>1 3 \|V\|<br>1 524 \|V\|<br>1 902 \|V\| N⨉\|V\| one-hot vectors<br>0 0 1 00<br>0 0 01 00<br>“dessert” = V 3 “was” = V 524 “0 g0 rea0 t” 1 = V00<br>902<br>dessert was great Input words |  |
| --- | --- |
| 图 6.13<br>Figure 6.13 | 使用输入词的池化嵌入的前馈网络情感分析。在每个<br>Feedforward network sentiment analysis using a pooled embedding of the input words. At each |

p(+) p(-) p(neut)

输出概率

> Output probabilities

### ^ ^

^

### y2 y3

### y y1

> [1⨉3]

输出层 softmax

> Output layer softmax

> [dh⨉3]

权重

> weights

### U h …

> [1⨉dh]

隐藏层

> Hidden layer

> h1 h2 h3

hdh

### W

> [d⨉dh]

权重

> weights

### x

输入层

> Input layer

> [1⨉d]

池化后的嵌入

> pooled embedding

池化

> pooling

> +

> “dessert”的嵌入
>
> *embedding for “dessert”*

> “was”的嵌入
>
> *embedding for “was”*

> N⨉d

> 嵌入
>
> *embeddings*

> “great”的嵌入
>
> *embedding for “great”*

### E E E

> E 矩阵
>
> *E matrix*

> |V|⨉d

> 在所有词之间共享
>
> *shared across words*

> 1 3 |V|

> 1 524 |V|

> N⨉|V|

> 1 902 |V|

> 独热向量
>
> *one-hot vectors*

> 0 0 1 0 0

> 0 0 0 1 0 0

> 0 0 0 1 0 0

| “desse | rt” = V<br>3 |
| --- | --- |

> “dessert” = V3 “was” = V524

> “great” = V902

dessert was great

输入词

> Input words

> 时间步，网络为每个上下文词计算一个 d 维嵌入（做法是用独热向量乘以嵌入矩阵 E），并把得到的 N 个嵌入池化，从而得到一个表示上下文窗口的单一嵌入，作为 x 层。
>
> *timestep the network computes a d-dimensional embedding for each context word (by multiplying a one-hot vector by the embedding matrix E), and pools the resulting N embeddings to get a single embedding that represents the context window as the layer x.*

前馈神经语言模型是一种前馈网络，它把

> A feedforward neural language model is a feedforward network that takes as

时刻 t 时前若干个词（wt−1、wt−2 等）的表示作为输入，并输出在可能的下一个词上的概率分布。因此——与 n-gram 语言模型一样——前馈神经语言模型通过基于前 N −1 个词作近似，来近似给定整个先前上下文时某个词的概率 P(wt|w1:t−1)：

> input at time t a representation of some number of previous words (wt−1,wt−2, etc.) and outputs a probability distribution over possible next words. Thus—like the ngram LM—the feedforward neural LM approximates the probability of a word given the entire prior context P(wt|w1:t−1) by approximating based on the N −1 previous words:

P(wt|w1,...,wt−1) ≈P(wt|wt−N+1,...,wt−1)

> (6.23)

在下面的例子中，我们将使用一个 4-gram 的例子，展示一个用来估计概率 P(wt = i|wt−3,wt−2,wt−1) 的神经网络。

> In the following examples we’ll use a 4-gram example, so we’ll show a neural net to estimate the probability P(wt = i|wt−3,wt−2,wt−1).

神经语言模型用嵌入来表示这一先前上下文中的词，而不像 n-gram 语言模型那样仅用词的身份来表示。

> Neural language models represent words in this prior context by their embeddings, rather than just by their word identity as used in n-gram language models.

使用嵌入使神经语言模型能更好地泛化到未见过的数据。例如，假设我们在训练中见过这个句子：

> Using embeddings allows neural language models to generalize better to unseen data. For example, suppose we’ve seen this sentence in training:

I have to make sure that the cat gets fed.

但从未见过“dog”一词后面出现“gets fed”。我们的测试集有前缀“I forgot to make sure that the dog gets”。下一个词是什么？n-gram 语言模型会在“that the cat gets”之后预测出“fed”，但不会在“that the dog gets”之后预测出它。而神经语言模型知道“cat”和“dog”有相似的嵌入，因此 6.5 • 作为神经网络分类器输入的嵌入 167 能够从“cat”的上下文泛化，从而即使在见到“dog”之后也能为“fed”赋予足够高的概率。

> but have never seen the words “gets fed” after the word “dog”. Our test set has the prefix “I forgot to make sure that the dog gets”. What’s the next word? An n-gram language model will predict “fed” after “that the cat gets”, but not after “that the dog gets”. But a neural LM, knowing that “cat” and “dog” have similar embeddings, will 6.5 • EMBEDDINGS AS THE INPUT TO NEURAL NET CLASSIFIERS 167 be able to generalize from the “cat” context to assign a high enough probability to“fed” even after seeing “dog”.

| p(w=aardvark\|w ,w ,w ) p(w=do\|…) p(w=fish\|…) p(w=zebra\|…)<br>t t-3 t-2 t-1 t t t<br>输出层 y y^ 1 … y^ 34 … y^ 42 … ^y 35102… y^ \|V\| 1⨉\|V\|<br>softmax<br>U<br>d h⨉\|V\|<br>隐藏层 h h 1 h 2 h 3 … h dh 1⨉d h<br>W Nd⨉d h<br>嵌入层 e 1⨉Nd<br>E 被共享 E E E<br>\|V\|⨉d<br>跨所有词<br>1 35 \|V\| 1 992 \|V\| 1 451 \|V\|<br>输入层 N⨉\|V\|<br>独热 0 0 1 00 0 0 01 00 0 0 0 1 00<br>向量 “for” = V 35 “all” = V 992 “the” = V 451<br>...<br>… and thanks for all the ? …<br>wt-3 wt-2 wt-1 wt<br>p(w=aardvark\|w ,w ,w ) p(w=do\|…) p(w=fish\|…) p(w=zebra\|…)<br>t t-3 t-2 t-1 t t t<br>output layer y y^ 1 … y^ 34 … y^ 42 … ^y 35102… y^ \|V\| 1⨉\|V\|<br>softmax<br>U<br>d h⨉\|V\|<br>hidden layer h h 1 h 2 h 3 … h dh 1⨉d h<br>W Nd⨉d h<br>embedding layer e 1⨉Nd<br>E is shared E E E<br>\|V\|⨉d<br>across words<br>1 35 \|V\| 1 992 \|V\| 1 451 \|V\|<br>Input layer N⨉\|V\|<br>one-hot 0 0 1 00 0 0 01 00 0 0 0 1 00<br>vectors “for” = V 35 “all” = V 992 “the” = V 451<br>...<br>… and thanks for all the ? …<br>wt-3 wt-2 wt-1 wt |  |
| --- | --- |
| 图 6.14<br>Figure 6.14 | 前馈神经语言模型中的前向推断。在每个时间步<br>Forward inference in a feedforward neural language model. At each timestep |

> p(wt=aardvark|wt-3,wt-2,wt-1) p(wt=do|…) p(wt=fish|…) p(wt=zebra|…)

^ ^ ^ ^ ^

| y^ … y^ … y^ … ^y<br>1 34 42 35102 | … y^<br>\|V\| |
| --- | --- |

… … … …

y1 y34 y42 y35102 y|V|

> 输出层 y 1⨉|V|softmax
>
> *output layer y 1⨉|V|softmax*

### U

> dh⨉|V|

…

> h2 h3 1⨉dh

> hdh

> h1

> 隐藏层 h
>
> *hidden layer h*

### W

> Nd⨉dh

> 嵌入层 e 1⨉Nd
>
> *embedding layer e 1⨉Nd*

> E 是共享的
>
> *E is shared*

### E E E

> 跨各个词 |V|⨉d
>
> *across words |V|⨉d*

> 1 35 |V| 1 992 |V| 1 451 |V|

> 输入层 N⨉|V|
>
> *Input layer N⨉|V|*

> 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0

> one-hot 向量 “for” = V35 “all” = V992 “the” = V451
>
> *one-hot vectors “for” = V35 “all” = V992 “the” = V451*

| ..<br>and | thanks | for | all | the | ? |
| --- | --- | --- | --- | --- | --- |

> ...

> and thanks for all the ?

> … …

> wt-3 wt-2 wt-1 wt

> t 网络为 N = 3 个上下文词元（context token）中的每一个计算 d 维嵌入（做法是把 one-hot 向量与嵌入矩阵 E 相乘），然后把这三个嵌入拼接起来得到嵌入 e。该嵌入 e 与权重矩阵 W 相乘，再逐元素应用激活函数，得到隐藏层 h，h 接着与另一个权重矩阵 U 相乘。softmax 层在每个输出节点 i 上预测下一个词 wt 是词汇表词 Vi 的概率。我们把上下文窗口大小 N 显示为 3 只是为了能放进页面，但实际的语言建模需要长得多的上下文。
>
> *t the network computes a d-dimensional embedding for each of the N = 3 context tokens (by multiplying a one-hot vector by the embedding matrix E), and concatenates the three to get the embedding e. This embedding e is multiplied by weight matrix W and then an activation function is applied element-wise to produce the hidden layer h, which is then multiplied by another weight matrix U. A softmax layer predicts at each output node i the probability that the next word wt will be vocabulary word Vi. We show the context window size N as 3 just to fit on the page, but in practice language modeling requires a much longer context.*

这个预测任务需要一个能表达 |V| 个概率的输出向量：

> This prediction task requires an output vector that expresses |V| probabilities:

即每个可能的下一个词元对应一个概率值。我们的词汇表可能包含 60,000 到 300,000 个词元，因此语言建模任务的输出向量远长于 3。语言建模的另一个不同之处在于：我们不是把 N 个输入词元的嵌入池化为单个嵌入，而是把各输入拼接成一个很长的输入向量。要预测下一个词元，知道前面每个词元以及它们的先后顺序是有帮助的。

> one probability value for each possible next token. We might have a vocabulary between 60,000 and 300,000 tokens, so the output vector for the task of language modeling is much longer than 3. Another difference for language modeling is that instead of pooling the embeddings of the N input tokens to create a single embedding, we concatenate the inputs into one very long input vector. To predict the next token, it helps to know each of the preceding tokens and what order they were in.

图 6.14 展示了语言建模任务，其中画出的上下文非常短

> Fig. 6.14 shows the language modeling task, sketched with a very short context

窗口仅为 N = 3，只是为了让图能放进页面。这 3 个嵌入向量被拼接起来得到嵌入层 e。e 与权重矩阵 W 相乘得到隐藏层，再与另一个权重矩阵 U 相乘得到输出层，输出层的 softmax 给出词上的概率分布。例如 y42，即输出节点 42 的值，是下一个词 wt 为 V42 的概率，V42 是索引为 42 的那个词汇表词（在我们的例子中就是词 ‘fish’）。

> window of N = 3 just to fit on the page. These 3 embedding vectors are concatenated to produce e, the embedding layer. This is multiplied by a weight matrix W to produce a hidden layer, and another weight matrix U to produce an output layer whose softmax gives a probability distribution over words. For example y42, the value of output node 42, is the probability of the next word wt being V42, the vocabulary word with index 42 (which is the word ‘fish’ in our example).

对于一个窗口 168 第 6 章 • 神经网络 大小为 3 的简单前馈神经语言模型，在给定每个输入上下文词的 one-hot 输入向量时，其方程为：

> The equations for a simple feedforward neural language model with a window 168 CHAPTER 6 • NEURAL NETWORKS size of 3, given one-hot input vectors for each input context word, are:

e = [Ext−3;Ext−2;Ext−1] h = σ(We+b)

z = Uh

ˆy = softmax(z)

> (6.24)

注意，我们用分号表示向量的拼接，因此我们把三个上下文向量的 3 个嵌入拼接起来，形成嵌入层 e。

> Note that we use semicolons to mean concatenation of vectors, so we form the embedding layer e by concatenating the 3 embeddings for the three context vectors.

我们将在后文再回到用神经网络进行语言建模这一想法

> We’ll return to this idea of using neural networks to do language modeling in

第 7 章中我们介绍 transformer 语言模型时。

> Chapter 7 when we introduce transformer language models.

## 6.6 训练神经网络

> 6.6 Training Neural Nets

前馈神经网络是有监督机器学习的一个实例，其中我们知道每个观测 x 的正确输出 y。系统通过式 6.13 所产生的是 ˆy，即系统对真实 y 的估计。训练过程的目标是为每一层 i 学习参数 W[i] 和 b[i]，使每个训练观测的 ˆy 尽可能接近真实 y。

> A feedforward neural net is an instance of supervised machine learning in which we know the correct output y for each observation x. What the system produces, via Eq. 6.13, is ˆy, the system’s estimate of the true y. The goal of the training procedure is to learn parameters W[i] and b[i] for each layer i that make ˆy for each training observation as close as possible to the true y.

一般来说，我们做这一切都借鉴了我们在第 4 章中介绍的方法

> In general, we do all this by drawing on the methods we introduced in Chapter 4

即用于逻辑回归的方法，因此在继续阅读之前，读者应当熟悉那一章。我们将在简单的通用网络上探索该算法，而不是在为情感分析或语言建模设计的网络上。

> for logistic regression, so the reader should be comfortable with that chapter before proceeding. We’ll explore the algorithm on simple generic networks rather than networks designed for sentiment or language modeling.

首先，我们需要一个损失函数，用来建模系统

> First, we’ll need a loss function that models the distance between the system

输出与金标准输出之间的距离，通常使用逻辑回归所用的损失函数，即交叉熵损失。

> output and the gold output, and it’s common to use the loss function used for logistic regression, the cross-entropy loss.

其次，为了找到使该损失函数最小的参数，我们将使用

> Second, to find the parameters that minimize this loss function, we’ll use the

第 4 章中介绍的梯度下降优化算法。

> gradient descent optimization algorithm introduced in Chapter 4.

第三，梯度下降需要知道损失函数的梯度，即

> Third, gradient descent requires knowing the gradient of the loss function, the

包含损失函数对每个参数的偏导数的向量。在逻辑回归中，对于每个观测，我们可以直接计算损失函数对单个 w 或 b 的导数。但对于神经网络，许多层中包含数百万个参数，当损失附着在靠后得多的某一层时，要看出如何计算第 1 层某个权重的偏导数就困难得多。我们如何将损失分摊到所有这些中间层？答案就是称为误差反向传播或反向微分的算法。

> vector that contains the partial derivative of the loss function with respect to each of the parameters. In logistic regression, for each observation we could directly compute the derivative of the loss function with respect to an individual w or b. But for neural networks, with millions of parameters in many layers, it’s much harder to see how to compute the partial derivative of some weight in layer 1 when the loss is attached to some much later layer. How do we partial out the loss over all those intermediate layers? The answer is the algorithm called error backpropagation or backward differentiation.

### 6.6.1 损失函数

> 6.6.1 Loss function

> 交叉熵
>
> *cross-entropy*

神经网络中使用的交叉熵损失与我们在

> The cross-entropy loss that is used in neural networks is the same one we saw for

> 损失
>
> *loss*

逻辑回归中看到的损失相同。如果神经网络被用作二分类器，并在最后一层使用 sigmoid，那么损失函数与我们在式 4.19 中看到的逻辑回归损失相同：

> logistic regression. If the neural network is being used as a binary classifier, with the sigmoid at the final layer, the loss function is the same logistic regression loss we saw in Eq. 4.19:

LCE(ˆy,y) = −log p(y|x) = −[ylog ˆy+(1−y)log(1−ˆy)]

> (6.25)

如果我们使用该网络进行 3 个或更多类别的分类，那么损失函数

> If we are using the network to classify into 3 or more classes, the loss function is

与我们在第 4 章中看到的多项式回归损失完全相同，参见 6.6 • 训练神经网络 169，第 112 页。为方便起见，这里简要总结一下该处的解释。首先，当类别多于 2 个时，我们需要将 y 和 ˆy 都表示为向量。假设我们做的是硬分类，即只有一个类别是正确的。

> exactly the same as the loss for multinomial regression that we saw in Chapter 4 on 6.6 • TRAINING NEURAL NETS 169 page 112. Let’s briefly summarize the explanation here for convenience. First, when we have more than 2 classes we’ll need to represent both y and ˆy as vectors. Let’s assume we’re doing hard classification, where only one class is the correct one.

真实标签 y 则是一个具有 K 个元素的向量，每个元素对应一个类别，如果正确类别是 c，则 yc = 1，而 y 的所有其他元素都为 0。回忆一下，像这样一个值为 1、其余为 0 的向量称为独热向量。

> The true label y is then a vector with K elements, each corresponding to a class, with yc = 1 if the correct class is c, with all other elements of y being 0. Recall that a vector like this, with one value equal to 1 and the rest 0, is called a one-hot vector.

而我们的分类器将产生一个具有 K 个元素的估计向量 ˆy，其中每个元素 ˆyk 都表示估计概率 p(yk = 1|x)。

> And our classifier will produce an estimate vector with K elements ˆy, each elementˆyk of which represents the estimated probability p(yk = 1|x).

单个样本 x 的损失函数是 K 个

> The loss function for a single example x is the negative sum of the logs of the K

输出类别的对数之和的负值，每项按其概率 yk 加权：

> output classes, each weighted by their probability yk:

> K

X

LCE(ˆy,y) = − yk log ˆyk

> (6.26)

> k=1

我们可以进一步简化这个方程；让我们首先用函数 1{} 重写该方程，当括号中的条件为真时它取值为 1，否则取值为 0。这更明显地表明，式 6.26 中求和里的各项除对应于真实类别（yk = 1）的那一项之外都将为 0：

> We can simplify this equation further; let’s first rewrite the equation using the function 1{} which evaluates to 1 if the condition in the brackets is true and to 0 otherwise. This makes it more obvious that the terms in the sum in Eq. 6.26 will be 0 except for the term corresponding to the true class for which yk = 1:

> K

X

LCE(ˆy,y) = − 1{yk = 1}log ˆyk

> k=1

换言之，交叉熵损失就是对应于正确类别的输出概率的负对数，因此我们也把它称为负

> In other words, the cross-entropy loss is simply the negative log of the output probability corresponding to the correct class, and we therefore also call this the negative

> 负对数
>
> *negative log*

对数似然损失：

> log likelihood loss:

> 似然损失
>
> *likelihood loss*

LCE(ˆy,y) = −log ˆyc（其中 c 是正确类别）

> LCE(ˆy,y) = −log ˆyc (where c is the correct class)

> (6.27)

代入式 6.9 中的 softmax 公式，并设 K 为类别数：

> Plugging in the softmax formula from Eq. 6.9, and with K the number of classes:

exp(zc)

LCE(ˆy,y) = −log（其中 c 是正确类别）

> LCE(ˆy,y) = −log (where c is the correct class)

> (6.28)

PK j=1 exp(z j)

让我们把负对数概率视为一种损失函数。一个完美的分类器会给正确类别 i 分配概率 1，给所有错误类别分配概率 0。这意味着 p(ˆyi) 越高（越接近 1），分类器就越好；p(ˆyi) 越低（越接近 0），分类器就越差。该概率的负对数是一个很好的损失度量，因为它从 0（1 的负对数，没有损失）变化到无穷（0 的负对数，损失无穷）。这一损失函数还保证：当正确答案的概率被最大化时，所有错误答案的概率被最小化；由于它们之和为 1，正确答案概率的任何增加都是以牺牲错误答案为代价的。

> Let’s think about the negative log probability as a loss function. A perfect classifier would assign the correct class i probability 1 and all the incorrect classes probability 0. That means the higher p(ˆyi) (the closer it is to 1), the better the classifier; p(ˆyi) is, and the lower it is (the closer it is to 0), the worse the classifier. The negative log of this probability is a beautiful loss metric since it goes from 0 (negative log of 1, no loss) to infinity (negative log of 0, infinite loss). This loss function also ensures that as probability of the correct answer is maximized, the probability of all the incorrect answers is minimized; since they all sum to one, any increase in the probability of the correct answer is coming at the expense of the incorrect answers.

输出向量 ˆy 的类别数 K 可小可大。也许

> The number K of classes of the output vector ˆy can be small or large. Perhaps

我们的任务是三分类情感分析，那么类别可能是正面、负面和中性。或者，如果我们的任务是判定一个词的词性（即它是名词还是动词或形容词等），那么 K 就是我们的标记集中可能的词性集合（在我们将于第 18 章定义的标记集中有 17 个）。而如果我们的任务是语言建模，分类器试图预测下一个词是哪个，那么我们的类别集合就是词的集合，可能有 50,000 或 100,000 个。

> our task is 3-way sentiment, and then the classes might be positive, negative, and neutral. Or if our task is deciding the part of speech of a word (i.e., whether it is a noun or verb or adjective, etc.), then K is the set of possible parts of speech in our tagset (of which there are 17 in the tagset we will define in Chapter 18). And if our task is language modeling, and our classifier is trying to predict which word is next, then our set of classes is the set of words, which might be 50,000 or 100,000.

170 第 6 章 • 神经网络

> 170 CHAPTER 6 • NEURAL NETWORKS

### 6.6.2 计算梯度

> 6.6.2 Computing the Gradient

我们如何计算这一损失函数的梯度？计算梯度需要求损失函数对每个参数的偏导数。

> How do we compute the gradient of this loss function? Computing the gradient requires the partial derivative of the loss function with respect to each parameter.

对于只有一个权重层和 sigmoid 输出的网络（也就是逻辑回归），我们可以直接使用式 6.29 中逻辑回归所用的损失导数（该式在 4.15 节推导）：

> For a network with one weight layer and sigmoid output (which is what logistic regression is), we could simply use the derivative of the loss that we used for logistic regression in Eq. 6.29 (and derived in Section 4.15):

∂LCE(ˆy,y)

= (ˆy−y)xj

∂wj

= (σ(w ·x+b)−y)xj

> (6.29)

或者对于只有一个权重层和 softmax 输出的网络（即多项逻辑回归），我们可以使用式 4.41 中 softmax 损失的导数，这里针对某个特定的权重 wk 和输入 xi 给出

> Or for a network with one weight layer and softmax output (=multinomial logistic regression), we could use the derivative of the softmax loss from Eq. 4.41, shown for a particular weight wk and input xi

∂LCE(ˆy,y)

= −(yk −ˆyk)xi

∂wk,i

= −(yk −p(yk = 1|x))xi

!

exp(wk ·x+bk)

> (6.30)

= − yk − PK xi

j=1 exp(w j ·x+bj)

但这些导数只能为一个权重层给出正确的更新：也就是最后一个权重层！

> But these derivatives only give correct updates for one weight layer: the last one!

对于深层网络，计算每个权重的梯度要复杂得多，因为我们要对一直回溯到网络最早期层中出现的权重参数求导，而损失却只在网络的最末端计算。

> For deep networks, computing the gradients for each weight is much more complex, since we are computing the derivative with respect to weight parameters that appear all the way back in the very early layers of the network, even though the loss is computed only at the very end of the network.

计算这一梯度的解决方案是一种称为误差反向传播（error backpropagation）或反向传播（backprop）的算法（Rumelhart et al., 1986）。虽然反向传播最初是专门

> The solution to computing this gradient is an algorithm called error backpropagation or backprop (Rumelhart et al., 1986). While backprop was invented spe-

> 误差反向
>
> *error back-*

> 传播
>
> *propagation*

为神经网络而发明的，但它最终被证明与一种更通用的、称为反向微分（backward differentiation）的过程相同，后者依赖于计算图的概念。我们在下一小节看看它是如何工作的。

> cially for neural networks, it turns out to be the same as a more general procedure called backward differentiation, which depends on the notion of computation graphs. Let’s see how that works in the next subsection.

### 6.6.3 计算图

> 6.6.3 Computation Graphs

计算图是对计算数学表达式的过程的表示，其中计算被分解为一个个独立的运算，每个运算被建模为图中的一个节点。

> A computation graph is a representation of the process of computing a mathematical expression, in which the computation is broken down into separate operations, each of which is modeled as a node in a graph.

考虑计算函数 L(a,b,c) = c(a+2b)。如果我们把其中的每个

> Consider computing the function L(a,b,c) = c(a+2b). If we make each of the

加法与乘法分量运算都显式写出，并为中间输出命名（d 和 e），得到的计算序列为：

> component addition and multiplication operations explicit, and add names (d and e) for the intermediate outputs, the resulting series of computations is:

d = 2∗b e = a+d L = c∗e

现在我们可以把它表示为一个图，每个运算对应一个节点，有向边表示每个运算的输出作为下一个运算的输入，如图 6.15 所示。计算图最简单的用途是在给定某些输入的情况下计算函数的值。在图中，我们假设输入为 a = 3、b = 1、c = −2，并展示了前向传播用于计算结果 L(3,1,−2) = −10 的过程。在计算图的前向传播中，我们自左向右依次应用每个 6.6 • 训练神经网络 171 运算，把每次计算的输出作为下一个节点的输入。

> We can now represent this as a graph, with nodes for each operation, and directed edges showing the outputs from each operation as the inputs to the next, as in Fig. 6.15. The simplest use of computation graphs is to compute the value of the function with some given inputs. In the figure, we’ve assumed the inputs a = 3, b = 1, c = −2, and we’ve shown the result of the forward pass to compute the result L(3,1,−2) = −10. In the forward pass of a computation graph, we apply each 6.6 • TRAINING NEURAL NETS 171 operation left to right, passing the outputs of each computation as the input to the next node.

| 前向传播<br>a=3<br>a<br>e=5<br>e=a+d<br>d=2<br>b=1<br>b d = 2b L=ce L=-10<br>c=-2<br>c<br>forward pass<br>a=3<br>a<br>e=5<br>e=a+d<br>d=2<br>b=1<br>b d = 2b L=ce L=-10<br>c=-2<br>c |  |
| --- | --- |
| 图 6.15<br>Figure 6.15 | 函数 L(a,b,c) = c(a+2b) 的计算图，并给出了各输入的值<br>Computation graph for the function L(a,b,c) = c(a+2b), with values for input |

前向传播

> forward pass

a a=3

e=a+d e=5

d=2

b=1 L=ce L=-10 b d = 2b

c=-2

c

> 节点 a = 3、b = 1、c = −2，展示 L 的前向传播计算。
>
> *nodes a = 3, b = 1, c = −2, showing the forward pass computation of L.*

### 6.6.4 计算图上的反向微分

> 6.6.4 Backward differentiation on computation graphs

计算图的重要性来自反向传播，它用于计算权重更新所需的导数。在本例中，我们的目标是计算输出函数 L 对每个输入变量的导数，即 ∂L ∂a、∂L ∂b 和 ∂L ∂c。导数 ∂L ∂a 告诉我们 a 的微小变化对 L 的影响有多大。

> The importance of the computation graph comes from the backward pass, which is used to compute the derivatives that we’ll need for the weight update. In this example our goal is to compute the derivative of the output function L with respect to each of the input variables, i.e., ∂L ∂a, ∂L ∂b, and ∂L ∂c . The derivative ∂L ∂a tells us how much a small change in a affects L.

反向微分利用了微积分中的链式法则，因此我们先回顾一下。假设我们要计算复合函数 f(x) = u(v(x)) 的导数。f(x) 的导数等于 u(x) 对 v(x) 的导数乘以 v(x) 对 x 的导数：

> Backwards differentiation makes use of the chain rule in calculus, so let’s remind ourselves of that. Suppose we are computing the derivative of a composite function f(x) = u(v(x)). The derivative of f(x) is the derivative of u(x) with respect to v(x) times the derivative of v(x) with respect to x:

> 链式法则
>
> *chain rule*

d f dx = du dv · dv

> (6.31)

dx

链式法则可以推广到两个以上的函数。如果计算复合函数 f(x) = u(v(w(x))) 的导数，则 f(x) 的导数为：

> The chain rule extends to more than two functions. If computing the derivative of a composite function f(x) = u(v(w(x))), the derivative of f(x) is:

d f dx = du dv · dv dw · dw

> (6.32)

dx

反向微分的直观含义是把梯度从最末

> The intuition of backward differentiation is to pass gradients back from the final

节点反向传给图中的所有节点。图 6.16 展示了在节点 e 处进行的部分反向计算。每个节点接收一个由其右侧父节点传入的上游梯度，并对其每个输入计算一个局部梯度（即其输出对其输入的梯度），然后利用链式法则将两者相乘，计算出一个要传递给更早一个节点的下游梯度。

> node to all the nodes in the graph. Fig. 6.16 shows part of the backward computation at one node e. Each node takes an upstream gradient that is passed in from its parent node to the right, and for each of its inputs computes a local gradient (the gradient of its output with respect to its input), and uses the chain rule to multiply these two to compute a downstream gradient to be passed on to the next earlier node.

现在让我们来计算所需的 3 个导数。由于在计算图中

> Let’s now compute the 3 derivatives we need. Since in the computation graph

L = ce，我们可以直接计算导数 ∂L ∂c：

> L = ce, we can directly compute the derivative ∂L ∂c :

∂L∂c = e

> (6.33)

对于另外两个，我们需要使用链式法则：

> For the other two, we’ll need to use the chain rule:

∂L ∂a = ∂L ∂e

∂e ∂a

∂L ∂b = ∂L ∂e ∂d

> (6.34)

∂e ∂d ∂b 172 第 6 章 • 神经网络

> ∂e ∂d ∂b 172 CHAPTER 6 • NEURAL NETWORKS

| d e<br>d e L<br>∂L ∂L ∂e ∂e ∂L<br>=<br>∂d ∂e ∂d ∂d ∂e<br>下游 局部 上游<br>梯度 梯度 梯度<br>d e<br>d e L<br>∂L ∂L ∂e ∂e ∂L<br>=<br>∂d ∂e ∂d ∂d ∂e<br>downstream local upstream<br>gradient gradient gradient |  |
| --- | --- |
| 图 6.16<br>Figure 6.16 | 每个节点（如这里的 e）接收一个上游梯度，将其与局部<br>Each node (like e here) takes an upstream gradient, multiplies it by the local |

> d e

d e L

> ∂L ∂L ∂e ∂e ∂L= ∂d ∂e∂d ∂e ∂d

> 下游 局部 上游 梯度 梯度 梯度
>
> *downstream local upstream gradient gradient gradient*

> 梯度（即其输出对其输入的梯度），并使用链式法则计算一个要传递给前一个节点的下游梯度。如果一个节点有多个输入，它就可能拥有多个局部梯度。
>
> *gradient (the gradient of its output with respect to its input), and uses the chain rule to compute a downstream gradient to be passed on to a prior node. A node may have multiple local gradients if it has multiple inputs.*

因此，式 6.34 和式 6.33 需要五个中间导数：∂L ∂e、∂L ∂c、∂e ∂a、∂e ∂d 以及

> Eq. 6.34 and Eq. 6.33 thus require five intermediate derivatives: ∂L ∂e , ∂L ∂c , ∂e ∂a, ∂e ∂d , and

> ∂d

∂b，它们具体如下（利用和的导数等于导数之和这一事实）：

> ∂b, which are as follows (making use of the fact that the derivative of a sum is the sum of the derivatives):

∂L ∂e = c, ∂L

L = ce : ∂c = e

∂a = 1, ∂e ∂e

e = a+d : ∂d = 1

∂d

d = 2b : ∂b = 2

在反向传播中，我们像上文那样使用链式法则，沿图的每条边从右到左计算这些偏导数。因此，我们首先计算来自节点 L 的下游梯度，即 ∂L ∂e 和 ∂L ∂c 。对于节点 e，我们随后将这个上游梯度 ∂L ∂e 与局部梯度（输出关于输入的梯度）∂e ∂d 相乘，得到传回节点 d 的结果：∂L ∂d 。

> In the backward pass, we compute each of these partials along each edge of the graph from right to left, using the chain rule just as we did above. Thus we begin by computing the downstream gradients from node L, which are ∂L ∂e and ∂L ∂c . For node e, we then multiply this upstream gradient ∂L ∂e by the local gradient (the gradient of the output with respect to the input), ∂e ∂d to get the output we send back to node d: ∂L ∂d .

依此类推，直到我们为图中所有输入变量都完成标注。

> And so on, until we have annotated the graph all the way to all the input variables.

前向传播恰好已经计算出了我们计算这些导数所需的前向中间变量的值（如 d 和 e）。图 6.17 展示了反向传播。

> The forward pass conveniently already will have computed the values of the forward intermediate variables we need (like d and e) to compute these derivatives. Fig. 6.17 shows the backward pass.

|  |  |
| --- | --- |
| a=3<br>a<br>∂L ∂L∂e<br>= =-2<br>∂a ∂e ∂a e=d+a e=5<br>d=2<br>b=1<br>∂e ∂e<br>b d = 2b ∂L =∂L∂e =-2 ∂a =1 ∂d =1 ∂ ∂L e =-2 L=ce L=-10<br>∂L ∂L∂d ∂d ∂d ∂e ∂d<br>= =-4 =2 ∂L<br>∂b ∂d ∂b ∂b =-2<br>∂e<br>c=-2 ∂L<br>=5<br>∂c<br>∂L<br>c =5 反向传播<br>∂c<br>a=3<br>a<br>∂L ∂L∂e<br>= =-2<br>∂a ∂e ∂a e=d+a e=5<br>d=2<br>b=1<br>∂e ∂e<br>b d = 2b ∂L =∂L∂e =-2 ∂a =1 ∂d =1 ∂ ∂L e =-2 L=ce L=-10<br>∂L ∂L∂d ∂d ∂d ∂e ∂d<br>= =-4 =2 ∂L<br>∂b ∂d ∂b ∂b =-2<br>∂e<br>c=-2 ∂L<br>=5<br>∂c<br>∂L<br>c =5 backward pass<br>∂c |  |
|  |  |
| 图 6.17<br>Figure 6.17 | 函数 L(a,b,c) = c(a+2b) 的计算图，展示反向传播的计算<br>Computation graph for the function L(a,b,c) = c(a+2b), showing the backward pass computa- |

a=3

a

> ∂L = ∂L ∂e =-2∂a ∂e ∂a

e=d+a e=5

d=2

b=1

> ∂e =1 ∂e =1 ∂L =-2

b d = 2b

> ∂a ∂d

L=-10

> ∂L ∂L ∂e

L=ce

> = =-2 ∂e

> ∂L ∂L ∂d ∂d =2 ∂d ∂e ∂d= =-4 ∂L =-2∂b ∂d ∂b ∂b ∂e

c=-2

> ∂L =5∂c

∂L=5 反向传播

> ∂L=5 backward pass

c ∂c

> …… ∂L ∂a 、∂L ∂b 和 ∂L ∂c 的计算。
>
> *tion of ∂L ∂a , ∂L ∂b , and ∂L ∂c .*

6.6 • 训练神经网络 173

> 6.6 • TRAINING NEURAL NETS 173

神经网络的反向微分

> Backward differentiation for a neural network

当然，真实神经网络的计算图要复杂得多。

> Of course computation graphs for real neural networks are much more complex.

图 6.18 展示了一个 2 层神经网络的示例计算图，其中 n0 =2、n1 = 2、n2 = 1，假设为二分类任务，因此为简单起见使用 sigmoid 输出单元。该计算图所计算的函数为：

> Fig. 6.18 shows a sample computation graph for a 2-layer neural network with n0 =2, n1 = 2, and n2 = 1, assuming binary classification and hence using a sigmoid output unit for simplicity. The function that the computation graph is computing is:

z[1] = W[1]x+b[1] a[1] = ReLU(z[1]) z[2] = W[2]a[1] +b[2] a[2] = σ(z[2])ˆy = a[2]

> (6.35)

对于反向传播，我们还需要计算损失 L。损失函数

> For the backward pass we’ll also need to compute the loss L. The loss function

对于二分类 sigmoid 输出，由式 6.25 给出，即

> for binary sigmoid output from Eq. 6.25 is

LCE(ˆy,y) = −[ylog ˆy+(1−y)log(1−ˆy)]

> (6.36)

我们的输出为 ˆy = a[2]，因此可以将其改写为

> Our output ˆy = a[2], so we can rephrase this as

h i

LCE(a[2],y) = − yloga[2] +(1−y)log(1−a[2])

> (6.37)

| [1]<br>w<br>11 *<br>[1]<br>w<br>12 z[1] = a[1] =<br>* 1 1<br>+ ReLU<br>x<br>1<br>*<br>[1]<br>b [2]<br>x 1 w 1[ 12] z + = a[2] = σ L (a[2] ,y)<br>2<br>*<br>*<br>[1] [2]<br>w [1] [1] w<br>21 * z 2 = a 2 = 12<br>+ ReLU<br>[1]<br>w [2]<br>22 b<br>1<br>[1]<br>b<br>2 | [1]<br>w<br>11 *<br>[1]<br>w<br>12 z[1] = a[1] =<br>* 1 1<br>+ ReLU<br>x<br>1<br>*<br>[1]<br>b [2]<br>x 1 w 1[ 12] z + = a[2] = σ L (a[2] ,y)<br>2<br>*<br>*<br>[1] [2]<br>w [1] [1] w<br>21 * z 2 = a 2 = 12<br>+ ReLU<br>[1]<br>w [2]<br>22 b<br>1<br>[1]<br>b<br>2 |
| --- | --- |
| 图 6.18<br>Figure 6.18 | 一个简单 2 层神经网络（= 1 个隐藏层）在有两个输入单元时的示例计算图<br>Sample computation graph for a simple 2-layer neural net (= 1 hidden layer) with two input units |

> w[1]

> 11

> *

> w[1]

> z[1] = a[1] =

> 12

> 1

> *

> 1

> + ReLU

> x1

> b[1] *

> z[2] =

> 1

### a[2] = σ

> w[2] L (a[2],y)

> x2 11 +

> *

> *

> w[1] z[1] = a[1] = w[2]

> 12

> 21

> *

> 2 2

> w[1] + ReLU

> b[2]

> 22 1

> b[1]

> 2

> 以及 2 个隐藏单元。我们略微调整了记号，节点中只提及正在计算的函数以及所得的变量名，以避免出现冗长的公式。因此，节点 w[1] 11 右侧的 * 表示 w[1] 11 要与 x1 相乘，而节点 z[1] = + 表示 z[1] 的值是通过对输入它的三个节点求和计算得到的（两个乘积项以及偏置项 b[1] i ）。
>
> *and 2 hidden units. We’ve adjusted the notation a bit to avoid long equations in the nodes by just mentioning the function that is being computed, and the resulting variable name. Thus the * to the right of node w[1] 11 means that w[1] 11 is to be multiplied by x1, and the node z[1] = + means that the value of z[1] is computed by summing the three nodes that feed into it (the two products, and the bias term b[1] i ).*

需要更新的权重（即那些我们需要求损失函数偏

> The weights that need updating (those for which we need to know the partial

导数的权重）以青色显示。为了进行反向传播，我们需要知道图中所有函数的导数。我们已经在 4.15 节看到过 sigmoid σ 的导数：

> derivative of the loss function) are shown in teal. In order to do the backward pass, we’ll need to know the derivatives of all the functions in the graph. We already saw in Section 4.15 the derivative of the sigmoid σ:

dσ(z)

= σ(z)(1−σ(z))

> (6.38)

dz 174 第 6 章 • 神经网络 我们还需要其他每个激活函数的导数。tanh 的导数为：

> dz 174 CHAPTER 6 • NEURAL NETWORKS We’ll also need the derivatives of each of the other activation functions. The derivative of tanh is:

d tanh(z) = 1−tanh2(z)

> (6.39)

dz

ReLU 的导数为2

> The derivative of the ReLU is2

 0，当 z < 0 时

>  0 for z < 0

d ReLU(z)

> (6.40)

dz = 1，当 z ≥0 时

> dz = 1 for z ≥0

我们将给出计算的开头部分，即计算损失函数 L 关于 z 的导数，也就是 ∂L ∂z（其余计算留作读者的练习）。根据链式法则：

> We’ll give the start of the computation, computing the derivative of the loss function L with respect to z, or ∂L ∂z (and leaving the rest of the computation as an exercise for the reader). By the chain rule:

∂L ∂z = ∂L ∂a[2]

> (6.41)

∂a[2] ∂z

> ∂L

因此我们先计算 ∂a[2]，即对式 6.37 求导，该式在此重述如下：

> So let’s first compute ∂a[2] , taking the derivative of Eq. 6.37, repeated here:

h i

LCE(a[2],y) = − yloga[2] +(1−y)log(1−a[2])

! !

∂L y∂log(a[2]) +(1−y)∂log(1−a[2])∂a[2] = − ∂a[2] ∂a[2]

 y 1  1 

= − +(1−y) 1−a[2] (−1)

a[2]

 y a[2] + y−1

> (6.42)

= − 1−a[2]

接下来，根据 sigmoid 的导数：

> Next, by the derivative of the sigmoid:

∂a[2] = a[2](1−a[2])∂z

最后，我们可以使用链式法则：

> Finally, we can use the chain rule:

∂L ∂L ∂a[2]∂z = ∂a[2] ∂z

 y a[2] + y−1 a[2](1−a[2])

= − 1−a[2]= a[2] −y

> (6.43)

继续梯度的反向计算（接下来把梯度经过 b[2] 1 和两个乘积节点依次向后传递，直到回到所有青色节点），留作读者的练习。

> Continuing the backward computation of the gradients (next by passing the gradients over b[2] 1 and the two product nodes, and so on, back to all the teal nodes), is left as an exercise for the reader.

### 6.6.5 关于学习的更多细节

> 6.6.5 More details on learning

神经网络中的优化是一个非凸优化问题，比逻辑回归中的优化更为复杂，由于这一原因以及其他原因，成功学习存在许多最佳实践。

> Optimization in neural networks is a non-convex optimization problem, more complex than for logistic regression, and for that and other reasons there are many best practices for successful learning.

> 2

> 在 z = 0 这一点上该导数实际上未定义，但按惯例我们将其视为 1。
>
> *The derivative is actually undefined at the point z = 0, but by convention we treat it as 1.*

6.7 • 小结 175

> 6.7 • SUMMARY 175

对于逻辑回归，我们可以把所有权重和

> For logistic regression we can initialize gradient descent with all the weights and

偏置都取值为 0 来初始化梯度下降。相比之下，在神经网络中，我们需要用小随机数来初始化权重。把输入值归一化为均值为 0、方差为单位方差也很有帮助。

> biases having the value 0. In neural networks, by contrast, we need to initialize the weights with small random numbers. It’s also helpful to normalize the input values to have 0 mean and unit variance.

人们使用各种形式的正则化来防止过拟合。其中最

> Various forms of regularization are used to prevent overfitting. One of the most

重要的是 dropout：随机丢弃一些单元及其连接，从

> important is dropout: randomly dropping some units and their connections from

> dropout（丢弃法）
>
> *dropout*

训练期间的网络（Hinton et al. 2012, Srivastava et al. 2014）。在训练的每一次迭代中（每当我们更新参数时，即如果使用小批量梯度下降，则每个小批量），我们选定一个概率 p，并对每个单元以概率 p 将其输出替换为零（并重新归一化该层其余的输出）。因此概率 p 是该算法的一个超参数。

> the network during training (Hinton et al. 2012, Srivastava et al. 2014). At each iteration of training (whenever we update parameters, i.e. each mini-batch if we are using mini-batch gradient descent), we choose a probability p and for each unit we replace its output with zero with probability p (and renormalize the rest of the outputs from that layer). Thus probability p is a hyperparameter of the algorithm.

此类超参数的调优也很重要。神经网络的

> Tuning of such hyperparameters is also important. The parameters of a neural

> 超参数
>
> *hyperparameter*

参数是权重 W 和偏置 b；它们通过梯度下降学习得到。

> network are the weights W and biases b; those are learned by gradient descent.

超参数是由算法设计者选择的；其最优值在开发集上调优得到，而不是靠在训练集上通过梯度下降学习得到。超参数包括学习率 η、小批量大小、模型架构（层数、每层隐藏节点数、激活函数的选择）、如何正则化等。梯度下降本身也有许多架构变体，例如 Adam（Kingma and Ba, 2015）。

> The hyperparameters are things that are chosen by the algorithm designer; optimal values are tuned on a devset rather than by gradient descent learning on the training set. Hyperparameters include the learning rate η, the mini-batch size, the model architecture (the number of layers, the number of hidden nodes per layer, the choice of activation functions), how to regularize, and so on. Gradient descent itself also has many architectural variants such as Adam (Kingma and Ba, 2015).

最后，大多数现代神经网络都是借助计算图形式化方法构建的，这类方法使得在基于向量的 GPU（图形处理器，Graphic Processing Units）上进行梯度计算和并行化变得简单而自然。PyTorch（Paszke et al., 2017）和 TensorFlow（Abadi et al., 2015）是其中最流行的两个。有兴趣的读者应查阅神经网络教材以了解更多细节；本章末尾给出了一些建议。

> Finally, most modern neural networks are built using computation graph formalisms that make it easy and natural to do gradient computation and parallelization on vector-based GPUs (Graphic Processing Units). PyTorch (Paszke et al., 2017) and TensorFlow (Abadi et al., 2015) are two of the most popular. The interested reader should consult a neural network textbook for further details; some suggestions are at the end of the chapter.

## 6.7 小结

> 6.7 Summary

- 神经网络由神经单元构成。它最初受生物神经元启发，如今神经网络已成为一种抽象的计算装置，而不再是生物学模型。
- 每个神经单元将输入值与一个权重向量相乘，加上偏置，然后施加一个非线性激活函数，如 sigmoid、tanh 或修正线性单元。
- 在完全连接的前馈网络中，第 i 层的每个单元都与第 i+1 层的每个单元相连，且不存在环路。
- 神经网络的能力来源于较早的层能够学习到可供网络中较晚的层利用的表示。
- 神经网络通过梯度下降等优化算法进行训练。
- 误差反向传播，即计算图上的反向求导，用于计算网络损失函数的梯度。
- 神经语言模型将神经网络用作概率分类器，以计算给定前 n 个词时下一个词的概率。
- 神经语言模型可以使用预训练的词嵌入，也可以在语言建模过程中从零开始学习词嵌入。

> Neural networks are built out of neural units. Originally inspired by biological neurons, neural networks are now an abstract computational device rather than a biological model.
> Each neural unit multiplies input values by a weight vector, adds a bias, and then applies a non-linear activation function like sigmoid, tanh, or rectified linear unit.
> In a fully-connected, feedforward network, each unit in layer i is connected to each unit in layer i+1, and there are no cycles.
> The power of neural networks comes from the ability of early layers to learn representations that can be utilized by later layers in the network.
> Neural networks are trained by optimization algorithms like gradient descent.
> Error backpropagation, backward differentiation on a computation graph, is used to compute the gradients of the loss function for a network.
> Neural language models use a neural network as a probabilistic classifier, to compute the probability of the next word given the previous n words.
> Neural language models can use pretrained embeddings, or can learn embeddings from scratch in the process of language modeling.

176 第 6 章 • 神经网络

> 176 CHAPTER 6 • NEURAL NETWORKS

## 历史注记

> Historical Notes

神经网络的起源可追溯到 20 世纪 40 年代的 McCulloch-Pitts 神经元（McCulloch and Pitts, 1943），它是生物神经元的一种简化模型，被视作一种可用命题逻辑描述的计算元件。到 20 世纪 50 年代末和 60 年代初，若干实验室（包括康奈尔的 Frank Rosenblatt 和斯坦福的 Bernard Widrow）开展了神经网络研究；这一阶段出现了感知机（perceptron）（Rosenblatt, 1958），并将阈值转变为偏置，这一记号我们至今仍在使用（Widrow and Hoff, 1960）。

> The origins of neural networks lie in the 1940s McCulloch-Pitts neuron (McCulloch and Pitts, 1943), a simplified model of the biological neuron as a kind of computing element that could be described in terms of propositional logic. By the late 1950s and early 1960s, a number of labs (including Frank Rosenblatt at Cornell and Bernard Widrow at Stanford) developed research into neural networks; this phase saw the development of the perceptron (Rosenblatt, 1958), and the transformation of the threshold into a bias, a notation we still use (Widrow and Hoff, 1960).

神经网络领域走向衰落，是在人们证明单个感知机

> The field of neural networks declined after it was shown that a single perceptron

单元无法对像 XOR 这样简单的函数建模之后（Minsky and Papert, 1969）。

> unit was unable to model functions as simple as XOR (Minsky and Papert, 1969).

尽管在此后的二十年中仍有少量工作继续进行，该领域的重大复兴直到 20 世纪 80 年代才出现，当时构建更深网络的实用工具（如误差反向传播）开始广泛使用（Rumelhart et al., 1986）。在 20 世纪 80 年代，出现了各式各样的神经网络及相关架构，特别是在心理学和认知科学的应用中（Rumelhart and McClelland 1986b, McClelland and Elman 1986, Rumelhart and McClelland 1986a, Elman 1990），当时常用联结主义或并行分布式处理这一术语（Feldman and Ballard 1982, Smolensky 1988）。这一时期发展出的许多原理和技术都是现代工作的基础，包括分布式表示（Hinton, 1986）、循环网络（Elman, 1990）以及用张量实现组合性（Smolensky, 1990）等思想。

> While some small amount of work continued during the next two decades, a major revival for the field didn’t come until the 1980s, when practical tools for building deeper networks like error backpropagation became widespread (Rumelhart et al., 1986). During the 1980s a wide variety of neural network and related architectures were developed, particularly for applications in psychology and cognitive science (Rumelhart and McClelland 1986b, McClelland and Elman 1986, Rumelhart and McClelland 1986a, Elman 1990), for which the term connectionist or parallel distributed processing was often used (Feldman and Ballard 1982, Smolensky 1988). Many of the principles and techniques developed in this period are foundational to modern work, including the ideas of distributed representations (Hinton, 1986), recurrent networks (Elman, 1990), and the use of tensors for compositionality(Smolensky, 1990).

> 联结主义
>
> *connectionist*

到 20 世纪 90 年代，更大的神经网络也开始被应用于许多实际的语言处理任务，例如手写识别（LeCun et al. 1989）和语音识别（Morgan and Bourlard 1990）。到 21 世纪初，计算机硬件的改进以及优化和训练技术的进步，使得训练更大、更深的网络成为可能，由此产生了现代的深度学习这一术语（Hinton et al. 2006, Bengio et al. 2007）。我们在第 14 章和第 16 章会介绍更多相关的历史。

> By the 1990s larger neural networks began to be applied to many practical language processing tasks as well, like handwriting recognition (LeCun et al. 1989) and speech recognition (Morgan and Bourlard 1990). By the early 2000s, improvements in computer hardware and advances in optimization and training techniques made it possible to train even larger and deeper networks, leading to the modern term deep learning (Hinton et al. 2006, Bengio et al. 2007). We cover more related history in Chapter 14 and Chapter 16.

关于神经网络有许多优秀的著作，包括 Goodfellow

> There are a number of excellent books on neural networks, including Goodfellow

et al. (2016) 和 Nielsen (2015)。

> et al. (2016) and Nielsen (2015).
