# 第 6 章 神经网络

### 章

> CHAPTER

# 6 神经网络

> 6 Neural Networks

“[M]achines 这类机器在单元数量很大时，能够表现出非常复杂的行为。”

> “[M]achines of this character can behave in a very complicated manner when the number of units is large.”

> Alan Turing（1948）《Intelligent Machines》，第 6 页
>
> *Alan Turing (1948) “Intelligent Machines”, page 6*

神经网络是语言处理中一种基础的计算工具，而且是一种非常古老的工具。它们之所以被称为「神经」网络，是因为其起源可以追溯到 McCulloch-Pitts 神经元（McCulloch and Pitts, 1943）——那是对生物神经元的一种简化模型，把它视为一种可以用命题逻辑刻画的计算元件。不过，语言处理中的现代用法已不再借助这些早期的生物学灵感。

> Neural networks are a fundamental computational tool for language processing, and a very old one. They are called neural because their origins lie in the McCulloch-Pitts neuron (McCulloch and Pitts, 1943), a simplified model of the biological neuron as a kind of computing element that could be described in terms of propositional logic. But the modern use in language processing no longer draws on these early biological inspirations.

相反，现代神经网络是由许多小型计算单元构成的网络，其中每个单元

> Instead, a modern neural network is a network of small computing units, each
都接收一个输入值向量，并产生一个输出值。本章介绍应用于分类任务的神经网络。我们要介绍的架构称为前馈网络，因为计算是从一层单元迭代地推进到下一层。现代神经网络的使用常被称为深度学习，因为现代网络往往很深（有很多层）。

> of which takes a vector of input values and produces a single output value. In this chapter we introduce the neural net applied to classification. The architecture we introduce is called a feedforward network because the computation proceeds iteratively from one layer of units to the next. The use of modern neural nets is often called deep learning, because modern networks are often deep (have many layers).

> `feedforward`（前馈）
>
> 释义：指计算沿网络单向逐层推进、层与层之间不存在循环连接的结构。

> `deep learning`（深度学习）
>
> 释义：指用含多个隐藏层的神经网络从数据中自动学习特征表示的机器学习方法。

神经网络与逻辑回归共用许多相同的数学工具。但

> Neural networks share much of the same mathematics as logistic regression. But
神经网络是比逻辑回归更强大的分类器，事实上可以证明，一个最小的神经网络（严格来说，是只含一个「隐藏层」的网络）能够学习任意函数。

> neural networks are a more powerful classifier than logistic regression, and indeed a minimal neural network (technically one with a single ‘hidden layer’) can be shown to learn any function.

神经网络分类器与逻辑回归还有另一处不同。在

> Neural net classifiers are different from logistic regression in another way. With
逻辑回归时，我们基于领域知识设计出许多丰富的特征模板，从而把回归分类器应用于许多不同的任务。而在使用神经网络时，更常见的做法是尽量避免大量使用人工设计的丰富特征，转而构建以原始词元为输入、并在学习分类的过程中学会归纳出特征的神经网络。我们在第 5 章已见过这类面向嵌入的表示学习的例子，等开始研究深度 transformer 网络时还会看到大量例子。非常深的网络尤其擅长表示学习。因此，对于数据充足、可以自动学习特征的任务，深度神经网络正是合适的工具。

> logistic regression, we applied the regression classifier to many different tasks by developing many rich kinds of feature templates based on domain knowledge. When working with neural networks, it is more common to avoid most uses of rich handderived features, instead building neural networks that take raw tokens as inputs and learn to induce features as part of the process of learning to classify. We saw examples of this kind of representation learning for embeddings in Chapter 5, and we’ll see lots of examples once we start studying deep transformer networks. Nets that are very deep are particularly good at representation learning. For that reason deep neural nets are the right tool for tasks that offer sufficient data to learn features automatically.

本章中，我们将介绍作为分类器的前馈网络，首先使用

> In this chapter we’ll introduce feedforward networks as classifiers, first with
人工构建的特征，然后使用我们在第 5 章研究过的嵌入。

> hand-built features, and then using the embeddings that we studied in Chapter 5.

在后续各章中，我们将介绍许多其他类型的神经模型，其中最重要的是 transformer 与注意力机制（第 7 章），此外还有循环神经网络（第 14 章）和卷积神经网络（第 16 章）。下一章我们将介绍神经大语言模型这一范式。

> In subsequent chapters we’ll introduce many other kinds of neural models, most importantly the transformer and attention (Chapter 7), but also recurrent neural networks (Chapter 14) and convolutional neural networks (Chapter 16). And in the next chapter we’ll introduce the paradigm of neural large language models.

## 6.1 单元

> 6.1 Units

神经网络的构建模块是单个计算单元。单元以一组实数为输入，对它们进行某种计算，并产生一个输出。

> The building block of a neural network is a single computational unit. A unit takes a set of real valued numbers as input, performs some computation on them, and produces an output.

从本质上说，神经单元是取其输入的加权和，并在和中额外加一项，称为偏置项。给定一组输入 x1...xn，一个单元具有

> At its heart, a neural unit is taking a weighted sum of its inputs, with one additional term in the sum called a bias term. Given a set of inputs x1...xn, a unit has

> `bias term`（偏置项）
>
> 释义：加权和之外额外加入的一个可学习常数，用于平移激活阈值与决策边界。

一组对应的权重 w1...wn 和一个偏置 b，因此加权和 z 可以表示为：

> a set of corresponding weights w1...wn and a bias b, so the weighted sum z can be represented as:

X
z = b+ wixi (6.1)
用向量记号来表达这个加权和往往更方便；回想线性代数可知，一个向量本质上只是一个数字的列表或数组。因此

> Often it’s more convenient to express this weighted sum using vector notation; recall from linear algebra that a vector is, at heart, just a list or array of numbers. Thus

> i

> `vector`（向量）
>
> 释义：由若干实数按固定顺序排列而成的列表，可看作高维空间中的一个点或有向线段。

我们将用权重向量 w、标量偏置 b 和输入向量 x 来讨论 z，并把那个求和替换为方便的点积：

> we’ll talk about z in terms of a weight vector w, a scalar bias b, and an input vector x, and we’ll replace the sum with the convenient dot product:

z = w ·x+b (6.2)
如式 6.2 所定义的，z 只是一个实数值。

> As defined in Eq. 6.2, z is just a real valued number.

最后，神经单元并不把 z（x 的线性函数）直接用作输出，而是

> Finally, instead of using z, a linear function of x, as the output, neural units
对 z 施加一个非线性函数 f。我们把这个函数的输出称为该单元的激活值，记为 a。由于我们只建模单个单元，该

> apply a non-linear function f to z. We will refer to the output of this function as the activation value for the unit, a. Since we are just modeling a single unit, the

> `activation`（激活）
>
> 释义：单元对输入的加权和施加非线性函数之后得到的输出值。

节点的激活值实际上就是网络的最终输出，我们一般将其称为 y。因此值 y 定义为：

> activation for the node is in fact the final output of the network, which we’ll generally call y. So the value y is defined as:

y = a = f(z)
下面我们将讨论三种常用的非线性函数 f（sigmoid 函数、tanh 函数，以及修正线性单元即 ReLU），但从教学角度考虑，先讲 sigmoid 函数更为方便，因为我们在第 4 章已经见过它：

> We’ll discuss three popular non-linear functions f below (the sigmoid, the tanh, and the rectified linear unit or ReLU) but it’s pedagogically convenient to start with the sigmoid function since we saw it in Chapter 4:

> `sigmoid`（sigmoid 函数）
>
> 释义：把任意实数压缩到 0 与 1 之间的 S 形非线性函数，其输出常被解释为概率。

1
y = σ(z) = (6.3)
1+e−z
sigmoid 函数（如图 6.1 所示）有许多优点；它把输出

> The sigmoid (shown in Fig. 6.1) has a number of advantages; it maps the output
映射到区间 (0,1)，这有助于把离群值压缩到接近 0 或 1。而且它是可微的，正如我们在 4.15 节所看到的，这对学习很有用。

> into the range (0,1), which is useful in squashing outliers toward 0 or 1. And it’s differentiable, which as we saw in Section 4.15 will be handy for learning.

![](images/06-neural-networks/fig_p2_0.png)

*图 6.1 sigmoid 函数接受一个实数值并将其映射到区间 (0,1)。它在 0 附近近似线性，但离群值会被压缩到接近 0 或 1。*
*Figure 6.1 The sigmoid function takes a real value and maps it to the range (0,1). It is nearly linear around 0 but outlier values get squashed toward 0 or 1.*

把式 6.2 代入式 6.3，就得到神经单元的输出：

> Substituting Eq. 6.2 into Eq. 6.3 gives us the output of a neural unit:

1
y = σ(w ·x+b) = (6.4)
1+exp(−(w ·x+b))
图 6.2 给出了一个基本神经单元的最终示意图。在这个例子中，该单元

> Fig. 6.2 shows a final schematic of a basic neural unit. In this example the unit
接收 3 个输入值 x1、x2 和 x3，计算加权和，把每个值分别乘以一个权重（依次为 w1、w2 和 w3），将它们与偏置项 b 相加，然后让所得的和通过 sigmoid 函数，最终得到一个介于 0 和 1 之间的数。

> takes 3 input values x1,x2, and x3, and computes a weighted sum, multiplying each value by a weight (w1, w2, and w3, respectively), adds them to a bias term b, and then passes the resulting sum through a sigmoid function to result in a number between 0 and 1.

![](images/06-neural-networks/fig_p3_0.png)

*图 6.2 一个神经单元，接收 3 个输入 x1、x2 和 x3（以及一个偏置 b，我们把它表示为一个被固定为 +1 的输入的权重），并产生输出 y。我们还引入了一些方便的中间变量：求和运算的输出 z，以及 sigmoid 的输出 a。在这种情况下，单元的输出 y 与 a 相同，但在更深的网络中，我们会保留 y 表示整个网络的最终输出，而让 a 表示单个节点的激活。*
*Figure 6.2 A neural unit, taking 3 inputs x1, x2, and x3 (and a bias b that we represent as a weight for an input clamped at +1) and producing an output y. We include some convenient intermediate variables: the output of the summation, z, and the output of the sigmoid, a. In this case the output of the unit y is the same as a, but in deeper networks we’ll reserve y to mean the final output of the entire network, leaving a as the activation of an individual node.*

我们来看一个例子，以获得直观的理解。假设我们有一个

> Let’s walk through an example just to get an intuition. Let’s suppose we have a
单元，其权重向量和偏置如下：

> unit with the following weight vector and bias:

w = [0.2,0.3,0.9]
b = 0.5
对于下面这个输入向量，该单元会给出什么结果：

> What would this unit do with the following input vector:

x = [0.5,0.6,0.1]
得到的输出 y 将是：

> The resulting output y would be:

1 1 1
y = σ(w ·x+b) = 1+e−(w·x+b) = 1+e−(.5∗.2+.6∗.3+.1∗.9+.5) = 1+e−0.87 = .70
在实践中，sigmoid 并不常被用作激活函数。一个与之非常相似但几乎总是更好的函数，是图 6.3a 所示的 tanh 函数；

> In practice, the sigmoid is not commonly used as an activation function. A function that is very similar but almost always better is the tanh function shown in Fig. 6.3a;

> `tanh`（tanh 函数）
>
> 释义：一种取值范围为 -1 到 +1 的激活函数，是 sigmoid 的变体，输出以 0 为中心，可平滑求导。

tanh 函数是 sigmoid 的一种变体，取值范围为 -1 到 +1：

> tanh is a variant of the sigmoid that ranges from -1 to +1:

y = tanh(z) = ez −e−z
ez +e−z (6.5)
最简单的激活函数，也许也是最常用的激活函数，是修正线性单元（rectified linear unit），又称 ReLU，如图 6.3b 所示。它就等于 z

> The simplest activation function, and perhaps the most commonly used, is the rectified linear unit, also called the ReLU, shown in Fig. 6.3b. It’s just the same as z

> `ReLU`（ReLU（修正线性单元））
>
> 释义：一种激活函数，输出取输入与 0 中的较大者，正区间为线性而负区间恒为 0。

在 z 为正时，否则为 0：

> when z is positive, and 0 otherwise:

y = ReLU(z) = max(z,0) (6.6)
这些激活函数具有不同的性质，使它们分别适用于不同的

> These activation functions have different properties that make them useful for differ-

![](images/06-neural-networks/fig_p4_0.png)

*图 6.3 tanh 函数与 ReLU 激活函数。*
*Figure 6.3 The tanh and ReLU activation functions.*

语言应用或网络架构。例如，tanh 函数具有平滑可微、能把离群值映射到均值附近的良好性质。另一方面，修正线性函数之所以具有良好的性质，是因为它非常接近线性。在 sigmoid 或 tanh 函数中，z 取很大值时得到的 y 是饱和的，即极其接近 1，并且具有

> ent language applications or network architectures. For example, the tanh function has the nice properties of being smoothly differentiable and mapping outlier values toward the mean. The rectifier function, on the other hand, has nice properties that result from it being very close to linear. In the sigmoid or tanh functions, very high values of z result in values of y that are saturated, i.e., extremely close to 1, and have

> `saturated`（饱和）
>
> 释义：指激活函数在高输入值处的输出趋于恒定、导数接近 0 的状态，会使误差信号难以回传。

非常接近 0 的导数。导数为 0 会给学习带来问题，因为正如我们将在 6.6 节看到的，我们通过把误差信号反向传播、逐层相乘网络中每一层的梯度（偏导数）来训练网络；接近 0 的梯度会使误差信号变得越来越小，直到它

> derivatives very close to 0. Zero derivatives cause problems for learning, because as we’ll see in Section 6.6, we’ll train networks by propagating an error signal backwards, multiplying gradients (partial derivatives) from each layer of the network; gradients that are almost 0 cause the error signal to get smaller and smaller until it is

> `vanishing gradient`（梯度消失）
>
> 释义：指反向传播时误差信号因逐层乘以接近 0 的梯度而不断衰减，导致浅层参数几乎得不到更新的现象。

小到无法用于训练，这一问题被称为梯度消失问题。

> too small to be used for training, a problem called the vanishing gradient problem.

修正线性函数不存在这个问题，因为当 z 取很大值时，ReLU 的导数是 1，而不是非常接近 0。

> Rectifiers don’t have this problem, since the derivative of ReLU for high values of z is 1 rather than very close to 0.

## 6.2 XOR 问题

> 6.2 The XOR problem

在神经网络历史的早期，人们就认识到，神经网络的能力——正如启发它的真实神经元一样——来自把这些单元组合成更大的网络。

> Early in the history of neural networks it was realized that the power of neural networks, as with the real neurons that inspired them, comes from combining these units into larger networks.

关于多层网络之必要性的最巧妙论证之一，是

> One of the most clever demonstrations of the need for multi-layer networks was
Minsky 和 Papert（1969）给出的证明：单个神经单元无法计算其输入的某些非常简单的函数。考虑计算两个输入的基本逻辑函数这一任务，例如 AND、OR 和 XOR。作为回顾，下面是这些函数的真值表：

> the proof by Minsky and Papert (1969) that a single neural unit cannot compute some very simple functions of its input. Consider the task of computing elementary logical functions of two inputs, like AND, OR, and XOR. As a reminder, here are the truth tables for those functions:

AND OR XOR

| y x1 x2 | y x1 x2 |
| --- | --- |

x1 x2 y x1 x2 y x1 x2 y
0 0 0 0 0 0 0 0 0 0 1 0 0 1 1 0 1 1 1 0 0 1 0 1 1 0 1 1 1 1 1 1 1 1 1 0
这个例子最初是为感知机给出的，感知机是一种非常简单的神经

> This example was first shown for the perceptron, which is a very simple neural

> `perceptron`（感知机）
>
> 释义：一种输出为 0 或 1 的简单神经单元，以阶跃函数作激活函数，只能实现线性可分的逻辑功能。

单元，其输出为二值，并以一个非常简单的阶跃函数作为非线性激活函数。感知机的输出 y 为 0 或 1，其计算方式如下（使用与式 6.2 相同的权重 w、输入 x 和偏置 b）：

> unit that has a binary output and has a very simple step function as its non-linear activation function. The output y of a perceptron is 0 or 1, and is computed as follows (using the same weight w, input x, and bias b as in Eq. 6.2):

 0, if w ·x+b ≤0
y = 1, if w ·x+b > 0 (6.7)
构建一个能够计算其二进制输入的逻辑 AND 和 OR 函数的感知机是很容易的，

> It’s very easy to build a perceptron that can compute the logical AND and OR
图 6.4 给出了所需的权重。

> functions of its binary inputs; Fig. 6.4 shows the necessary weights.

![](images/06-neural-networks/fig_p5_0.png)

*图 6.4 用于计算逻辑函数的感知机的权重 w 与偏置 b。输入记为 x1 和 x2，偏置表示为一个取值为 +1 的特殊节点，它与偏置权重 b 相乘。(a) 逻辑 AND，权重 w1 = 1、w2 = 1，偏置权重 b = −1。(b) 逻辑 OR，权重 w1 = 1、w2 = 1，偏置权重 b = 0。这些权重/偏置只是能够实现这些函数的无穷多组可能权重与偏置中的一组。*
*Figure 6.4 The weights w and bias b for perceptrons for computing logical functions. The inputs are shown as x1 and x2 and the bias as a special node with value +1 which is multiplied with the bias weight b. (a) logical AND, with weights w1 = 1 and w2 = 1 and bias weight b = −1. (b) logical OR, with weights w1 = 1 and w2 = 1 and bias weight b = 0. These weights/biases are just one from an infinite number of possible sets of weights and biases that would implement the functions.*

然而事实证明，不可能构建出一个感知机来计算

> It turns out, however, that it’s not possible to build a perceptron to compute
逻辑 XOR！（值得花一点时间试一试！）

> logical XOR! (It’s worth spending a moment to give it a try!)
这一重要结果背后的直觉，依赖于理解感知机是一个线性分类器。对于二维输入 x1 和 x2，感知机方程 w1x1 + w2x2 + b = 0 是一条直线的方程。（我们可以把它写成标准线性形式来看出这一点：x2 = (−w1/w2)x1 + (−b/w2)。）这条直线充当一个

> The intuition behind this important result relies on understanding that a perceptron is a linear classifier. For a two-dimensional input x1 and x2, the perceptron equation, w1x1 +w2x2 +b = 0 is the equation of a line. (We can see this by putting it in the standard linear format: x2 = (−w1/w2)x1 + (−b/w2).) This line acts as a

> `decision boundary`（决策边界）
>
> 释义：由权重和偏置确定的直线或超平面，它把输入空间划分为输出 0 与输出 1 两个区域。

二维空间中的决策边界，在此空间中，输出 0 被赋予所有

> decision boundary in two-dimensional space in which the output 0 is assigned to all
位于直线一侧的输入，而输出 1 则赋予位于直线另一侧的所有输入点。如果我们有超过 2 个输入，决策边界就变成超平面而不是直线，但其思想是相同的，即把空间划分为两个类别。

> inputs lying on one side of the line, and the output 1 to all input points lying on the other side of the line. If we had more than 2 inputs, the decision boundary becomes a hyperplane instead of a line, but the idea is the same, separating the space into two categories.

图 6.5 展示了可能的逻辑输入（00、01、10 和 11），以及分别由

> Fig. 6.5 shows the possible logical inputs (00, 01, 10, and 11) and the line drawn
AND 分类器和 OR 分类器的一组可能参数所画出的直线。请注意，根本无法画出一条直线来把 XOR 的正例（01 和 10）

> by one possible set of parameters for an AND and an OR classifier. Notice that there is simply no way to draw a line that separates the positive cases of XOR (01 and 10)

> `linearly separable`（线性可分）
>
> 释义：指存在一条直线或超平面能把正例与负例完全分开的性质，XOR 不具备该性质。

与负例（00 和 11）分开。我们说 XOR 不是一个线性可分的

> from the negative cases (00 and 11). We say that XOR is not a linearly separable
函数。当然，我们可以用曲线或某种其他函数来画出边界，但不能用一条直线。

> function. Of course we could draw a boundary with a curve, or some other function, but not a single line.

### 6.2.1 解决方案：神经网络

> 6.2.1 The solution: neural networks

虽然 XOR 函数无法由单个感知机计算，但它可以由感知机单元构成的分层网络来计算。不过，与其用简单感知机组成的网络来看这一点，不如按照 Goodfellow 等人（2016）的做法，看看如何用两层基于 ReLU 的单元来计算 XOR。图 6.6 展示了输入经两层神经单元处理的过程。中间层（称为

> While the XOR function cannot be calculated by a single perceptron, it can be calculated by a layered network of perceptron units. Rather than see this with networks of simple perceptrons, however, let’s see how to compute XOR using two layers of ReLU-based units following Goodfellow et al. (2016). Fig. 6.6 shows a figure with the input being processed by two layers of neural units. The middle layer (called

- 有两个单元，输出层（称为 y）有一个单元。图中给出了一组权重和偏置，使该网络能够正确地计算 XOR 函数。

> has two units, and the output layer (called y) has one unit. A set of weights and biases are shown that allows the network to correctly compute the XOR function.

让我们逐步看看输入 x = [0, 0] 时会发生什么。如果我们把每个

> Let’s walk through what happens with the input x = [0, 0]. If we multiply each
输入值乘以相应的权重、求和，然后加上偏置 b，就得到向量 [0, -1]；接着我们应用修正线性变换，使 h 层的输出为 [0, 0]。现在我们再次乘以权重、求和，并加上

> input value by the appropriate weight, sum, and then add the bias b, we get the vector[0, -1], and we then apply the rectified linear transformation to give the output of the h layer as [0, 0]. Now we once again multiply by the weights, sum, and add the

![](images/06-neural-networks/fig_p6_0.png)

*图 6.5 函数 AND、OR 和 XOR，横轴为输入 x1，纵轴为输入 x2。实心圆表示感知机输出为 1，空心圆表示感知机输出为 0。对于 XOR，无法画出一条直线将这两个类别正确分开。图形样式参照 Russell 和 Norvig（2002）。*
*Figure 6.5 The functions AND, OR, and XOR, represented with input x1 on the x-axis and input x2 on the y-axis. Filled circles represent perceptron outputs of 1, and white circles perceptron outputs of 0. There is no way to draw a line that correctly separates the two categories for XOR. Figure styled after Russell and Norvig(2002).*

![](images/06-neural-networks/fig_p6_1.png)

*图 6.6 参照 Goodfellow 等人（2016）的 XOR 解决方案。共有三个 ReLU 单元，分布在两层中；我们称它们为 h1、h2（h 表示“隐藏层”）和 y1。与之前一样，箭头上的数字表示每个单元的权重 w，我们把偏置 b 表示为取值固定为 +1 的单元上的一个权重，偏置权重/单元以灰色显示。*
*Figure 6.6 XOR solution after Goodfellow et al. (2016). There are three ReLU units, in two layers; we’ve called them h1, h2 (h for “hidden layer”) and y1. As before, the numbers on the arrows represent the weights w for each unit, and we represent the bias b as a weight on a unit clamped to +1, with the bias weights/units in gray.*

偏置（此处为 0），得到数值 0。读者应自行推导其余 3 组可能输入的运算，以确认结果 y 值对于输入 [0, 1] 和 [1, 0] 为 1，对于 [0, 0] 和 [1, 1] 为 0。

> bias (0 in this case) resulting in the value 0. The reader should work through the computation of the remaining 3 possible input pairs to see that the resulting y values are 1 for the inputs [0, 1] and [1, 0] and 0 for [0, 0] and [1, 1].

观察中间结果同样有启发意义，也就是两个

> It’s also instructive to look at the intermediate results, the outputs of the two
隐藏节点 h1 和 h2 的输出。我们在上一段中说明了输入 x = [0, 0] 的 h 向量为 [0, 0]。图 6.7b 给出了全部 4 个输入的 h 层取值。请注意，两个输入点 x = [0, 1] 和 x = [1, 0]（即 XOR 输出为 1 的两种情况）的隐藏表示被合并为单点 h = [1, 0]。这种合并使得线性地分开 XOR 的正例和负例变得容易。换言之，我们可以把网络的隐藏层视为形成了输入的一种表示。

> hidden nodes h1 and h2. We showed in the previous paragraph that the h vector for the inputs x = [0, 0] was [0, 0]. Fig. 6.7b shows the values of the h layer for all 4 inputs. Notice that hidden representations of the two input points x = [0, 1] and x = [1, 0] (the two cases with XOR output = 1) are merged to the single point h =[1, 0]. The merger makes it easy to linearly separate the positive and negative cases of XOR. In other words, we can view the hidden layer of the network as forming a representation of the input.

在这个例子中，我们只是直接指定了图 6.6 中的权重。但对于真实的例子，

> In this example we just stipulated the weights in Fig. 6.6. But for real examples
神经网络中的权重是使用第 6.6 节将要介绍的误差反向传播算法自动学习得到的。这意味着隐藏层将学会形成有用的表示。神经网络能够自动学习输入的有用表示，这一直觉是它的关键优势之一，我们将在后续章节中反复回到这一点。

> the weights for neural networks are learned automatically using the error backpropagation algorithm to be introduced in Section 6.6. That means the hidden layers will learn to form useful representations. This intuition, that neural networks can automatically learn useful representations of the input, is one of their key advantages, and one that we will return to again and again in later chapters.

![](images/06-neural-networks/fig_p7_0.png)

*图 6.7 隐藏层形成了输入的一种新表示。(b) 展示了隐藏层的表示 h，与 (a) 中原始输入表示 x 的对比。*
*Figure 6.7 The hidden layer forming a new representation of the input. (b) shows the representation of the hidden layer, h, compared to the original input representation x in (a).*

> 请注意，输入点 [0, 1] 已与输入点 [1, 0] 合并，使得线性地分开 XOR 的正例和负例成为可能。参照 Goodfellow 等人（2016）。
>
> *Notice that the input point [0, 1] has been collapsed with the input point [1, 0], making it possible to linearly separate the positive and negative cases of XOR. After Goodfellow et al.(2016).*

## 6.3 前馈神经网络

> 6.3 Feedforward Neural Networks

下面让我们略微更正式地介绍最简单的一种

> Let’s now walk through a slightly more formal presentation of the simplest kind of

> `feedforward network`（前馈网络）
>
> 释义：信息从输入层经隐藏层单向流向输出层、不包含循环连接的神经网络，是最基础的网络结构。

神经网络，即前馈网络。前馈网络是一种多层

> neural network, the feedforward network. A feedforward network is a multilayer
单元之间的连接不含环；每一层单元的输出都传递给更高一层的单元，没有任何输出被回传到更低的层。（第 14 章我们将介绍带环的网络，称为循环神经网络。）

> network in which the units are connected with no cycles; the outputs from units in each layer are passed to units in the next higher layer, and no outputs are passed back to lower layers. (In Chapter 14 we’ll introduce networks with cycles, called recurrent neural networks.)
由于历史原因，多层网络，尤其是前馈网络，

> For historical reasons multilayer networks, especially feedforward networks, are

> `multi-layer perceptrons MLP`（多层感知机（MLP））
>
> 释义：对多层前馈网络的一种通行叫法，其单元使用 ReLU、sigmoid 等非线性激活函数，与真正的感知机并不相同。

有时被称为多层感知机（multi-layer perceptrons，简称 MLP）；这是一个技术上的误称，

> sometimes called multi-layer perceptrons (or MLPs); this is a technical misnomer,
因为现代多层网络中的单元并不是感知机（感知机的

> since the units in modern multilayer networks aren’t perceptrons (perceptrons have a
激活函数是简单的阶跃函数，而现代网络由具有多种非线性特性的单元组成，例如 ReLU 和 sigmoid 函数），但这个名称在某个时候就固定下来了。

> simple step-function as their activation function, but modern networks are made up of units with many kinds of non-linearities like ReLUs and sigmoids), but at some point the name stuck.

简单的前馈网络有三类节点：输入单元、隐藏

> Simple feedforward networks have three kinds of nodes: input units, hidden
单元和输出单元。

> units, and output units.

图 6.8 给出了一幅示意图。输入层 x 是一个由简单标量值构成的向量，正如

> Fig. 6.8 shows a picture. The input layer x is a vector of simple scalar values just
我们在图 6.2 中所见。

> as we saw in Fig. 6.2.

神经网络的核心是由隐藏单元 hi 构成的隐藏层 h，

> The core of the neural network is the hidden layer h formed of hidden units hi,

> `hidden layer`（隐藏层）
>
> 释义：位于输入层与输出层之间的中间层，其中每个单元对输入做加权求和并施加非线性变换，从而形成输入的表示。

其中每个单元都是 6.1 节所述的神经单元，先对其输入取加权和，再施加一个非线性变换。在标准架构中，每一层都是全连接的，这意味着每一层中的每个单元都以

> each of which is a neural unit as described in Section 6.1, taking a weighted sum of its inputs and then applying a non-linearity. In the standard architecture, each layer is fully-connected, meaning that each unit in each layer takes as input the outputs

> `fully-connected`（全连接）
>
> 释义：相邻两层之间任意一对单元都存在连接，因而每个单元都把前一层所有单元的输出作为自己的输入。

前一层所有单元的输出作为输入，并且相邻两层之间的每一对单元之间都有一条连接。因此，每个隐藏单元都对所有输入单元求和。

> from all the units in the previous layer, and there is a link between every pair of units from two adjacent layers. Thus each hidden unit sums over all the input units.

回忆一下，单个隐藏单元的参数是一个权重向量和一个偏置。我们

> Recall that a single hidden unit has as parameters a weight vector and a bias. We
把每个单元 i 的权重向量和偏置合并为整个层的一个权重矩阵 W 和一个偏置向量 b，以此来表示整个隐藏层的参数（见图 6.8）。权重矩阵 W 的每个元素 W ji 表示从第 i 个输入单元 xi 到第 j 个隐藏单元 hj 这条连接的权重。

> represent the parameters for the entire hidden layer by combining the weight vector and bias for each unit i into a single weight matrix W and a single bias vector b for the whole layer (see Fig. 6.8). Each element W ji of the weight matrix W represents the weight of the connection from the ith input unit xi to the jth hidden unit hj.

用单个矩阵 W 表示整层的权重，其优势在于

> The advantage of using a single matrix W for the weights of the entire layer is
现在前馈网络的隐藏层计算可以非常

> that now the hidden layer computation for a feedforward network can be done very

![](images/06-neural-networks/fig_p8_0.png)

*图 6.8 一个简单的 2 层前馈网络，包含一个隐藏层、一个输出层和一个输入层（在数层数时通常不把输入层计入）。*
*Figure 6.8 A simple 2-layer feedforward network, with one hidden layer, one output layer, and one input layer (the input layer is usually not counted when enumerating layers).*

高效地用简单的矩阵运算完成。事实上，这个计算只有三步：用权重矩阵乘以输入向量 x，加上偏置向量 b，然后施加激活函数 g（例如上文定义的 sigmoid、tanh 或 ReLU 激活函数）。

> efficiently with simple matrix operations. In fact, the computation only has three steps: multiplying the weight matrix by the input vector x, adding the bias vector b, and applying the activation function g (such as the sigmoid, tanh, or ReLU activation function defined above).

因此，隐藏层的输出，即向量 h，如下所示（在本例中我们使用 sigmoid 函数 σ 作为激活函数）：

> The output of the hidden layer, the vector h, is thus the following (for this example we’ll use the sigmoid function σ as our activation function):

h = σ(Wx+b) (6.8)
请注意，这里我们是把 σ 函数作用于一个向量，而在式 6.3 中它作用于一个标量。因此我们允许 σ(·)，乃至任何激活函数 g(·)，按元素作用于向量，即 g[z1,z2,z3] = [g(z1),g(z2),g(z3)]。

> Notice that we’re applying the σ function here to a vector, while in Eq. 6.3 it was applied to a scalar. We’re thus allowing σ(·), and indeed any activation function g(·), to apply to a vector element-wise, so g[z1,z2,z3] = [g(z1),g(z2),g(z3)].

我们引入一些常量来表示这些向量

> Let’s introduce some constants to represent the dimensionalities of these vectors
和矩阵的维度。我们把输入层称为网络的第 0 层，并用 n0 表示输入的数量，于是 x 是维度为 n0 的实数向量，更形式化地写作 x ∈Rn0，即维度为 [n0 × 1] 的列向量。我们把隐藏层称为第 1 层，把输出层称为第 2 层。隐藏层的维度为 n1，因此 h ∈Rn1，同时 b ∈Rn1（因为每个隐藏单元可以取不同的偏置值）。而权重矩阵 W 的维度为 W ∈Rn1×n0，即 [n1 ×n0]。

> and matrices. We’ll refer to the input layer as layer 0 of the network, and have n0 represent the number of inputs, so x is a vector of real numbers of dimension n0, or more formally x ∈Rn0, a column vector of dimensionality [n0 × 1]. Let’s call the hidden layer layer 1 and the output layer layer 2. The hidden layer has dimensionality n1, so h ∈Rn1 and also b ∈Rn1 (since each hidden unit can take a different bias value). And the weight matrix W has dimensionality W ∈Rn1×n0, i.e.[n1 ×n0].

请花点时间确认，式 6.8 中的矩阵乘法会  Pn0 

> Take a moment to convince yourself that the matrix multiplication in Eq. 6.8 will  Pn0 
计算出每个 h j 的值为 σ i=1 Wjixi +b j 。

> compute the value of each h j as σ i=1 Wjixi +b j .

正如我们在 6.2 节所见，所得到的值 h（既取 hidden 之意，也取 hypothesis 之意）构成了输入的表示。输出层的作用是接收这个新的表示 h 并计算最终输出。这个输出可以是一个实数值，但在许多情况下网络的目标是做出某种分类决策，因此我们将聚焦于分类的情形。

> As we saw in Section 6.2, the resulting value h (for hidden but also for hypothesis) forms a representation of the input. The role of the output layer is to take this new representation h and compute a final output. This output could be a realvalued number, but in many cases the goal of the network is to make some sort of classification decision, and so we will focus on the case of classification.

如果我们做的是像情感分类这样的二分类任务，我们可能只有一个输出节点，其标量值 y 就是正面情感相对于负面情感的概率。如果我们做的是多项分类，例如标注词性，我们可能为每个可能的词性各设置一个输出节点，其输出值是该词性的概率，并且所有输出节点的值之和必须为 1。因此输出层是一个向量 y，它给出各输出节点上的概率分布。

> If we are doing a binary task like sentiment classification, we might have a single output node, and its scalar value y is the probability of positive versus negative sentiment. If we are doing multinomial classification, such as assigning a part-ofspeech tag, we might have one output node for each potential part-of-speech, whose output value is the probability of that part-of-speech, and the values of all the output nodes must sum to one. The output layer is thus a vector y that gives a probability distribution across the output nodes.

我们来看看这是如何发生的。与隐藏层一样，输出层也有一个权重

> Let’s see how this happens. Like the hidden layer, the output layer has a weight
矩阵（我们称它为 U），但有些模型在输出层不含偏置向量 b，因此在本例中我们为简化起见省去偏置向量。权重矩阵与其输入向量（h）相乘，产生中间输出 z：

> matrix (let’s call it U), but some models don’t include a bias vector b in the output layer, so we’ll simplify by eliminating the bias vector in this example. The weight matrix is multiplied by its input vector (h) to produce the intermediate output z:

z = Uh
共有 n2 个输出节点，因此 z ∈Rn2，权重矩阵 U 的维度为 U ∈Rn2×n1，元素 Ui j 是从隐藏层中的单元 j 到输出层中的单元 i 的权重。

> There are n2 output nodes, so z ∈Rn2, weight matrix U has dimensionality U ∈Rn2×n1, and element Ui j is the weight from unit j in the hidden layer to unit i in the output layer.

然而，z 不能作为分类器的输出，因为它是一个由实数值构成的

> However, z can’t be the output of the classifier, since it’s a vector of real-valued
向量，而分类所需要的是一个概率向量。有一个方便的函数可以把实数向量归一化，我们所说的归一化是指

> numbers, while what we need for classification is a vector of probabilities. There is a convenient function for normalizing a vector of real values, by which we mean

> `normalizing`（归一化）
>
> 释义：把一组实数转换成编码概率分布的向量，使所有数值都落在 0 与 1 之间且总和为 1。

把它转换为一个编码概率分布的向量（所有数值都位于 0 与 1 之间且总和为 1）：也就是我们在第 109 页见到的 softmax 函数

> converting it to a vector that encodes a probability distribution (all the numbers lie between 0 and 1 and sum to 1): the softmax function that we saw on page 109

> `softmax`
>
> 释义：把实数向量转换为概率分布的函数，输出各分量非负且总和为 1，常用于分类器的输出层。

（见第 4 章）。更一般地，对于任意维度为 d 的向量 z，softmax 定义为：

> of Chapter 4. More generally for any vector z of dimensionality d, the softmax is defined as:

exp(zi)
softmax(zi) = 1 ≤i ≤d (6.9)
Pd j=1 exp(z j)
因此，举例来说，给定一个向量

> Thus for example given a vector
z = [0.6,1.1,−1.5,1.2,3.2,−1.1], (6.10)
softmax 函数会把它归一化为一个概率分布（数值已四舍五入）：

> the softmax function will normalize it to a probability distribution (shown rounded):

softmax(z) = [0.055,0.090,0.0067,0.10,0.74,0.010] (6.11)
你可能还记得，在第 4 章多项逻辑回归的版本中，我们用 softmax 从一组实数值（由权重与特征相乘再求和得到）构造出一个概率分布。

> You may recall that we used softmax to create a probability distribution from a vector of real-valued numbers (computed from summing weights times features) in the multinomial version of logistic regression in Chapter 4.

这意味着，我们可以把带有一个隐藏层的神经网络分类器看作

> That means we can think of a neural network classifier with one hidden layer
它先构造出一个向量 h，即输入的隐藏层表示，然后针对网络在 h 中发展出的特征运行标准的多项逻辑回归。相比之下，第 4 章中的特征主要是通过特征模板手工设计的。因此，神经网络就像多项逻辑回归，只不过：(a) 它有许多层，因为深度神经网络就像一层接一层的逻辑回归分类器；(b) 这些中间层可以有许多种可选的激活函数（tanh 函数、ReLU（修正线性单元）、sigmoid 函数），而不只是 sigmoid 函数（不过为方便起见，我们仍继续用 σ 表示任意激活函数）；(c) 特征并非由特征模板构造，而是由网络先前各层自行导出特征的表示。

> as building a vector h which is a hidden layer representation of the input, and then running standard multinomial logistic regression on the features that the network develops in h. By contrast, in Chapter 4 the features were mainly designed by hand via feature templates. So a neural network is like multinomial logistic regression, but (a) with many layers, since a deep neural network is like layer after layer of logistic regression classifiers; (b) with those intermediate layers having many possible activation functions (tanh, ReLU, sigmoid) instead of just sigmoid (although we’ll continue to use σ for convenience to mean any activation function); (c) rather than forming the features by feature templates, the prior layers of the network induce the feature representations themselves.

下面是带单个隐藏层的前馈网络的最终公式，

> Here are the final equations for a feedforward network with a single hidden layer,
该网络接收输入向量 x，输出概率分布 y，并由权重矩阵 W 和 U 以及偏置向量 b 参数化：

> which takes an input vector x, outputs a probability distribution y, and is parameterized by weight matrices W and U and a bias vector b:

h = σ(Wx+b)
z = Uh
y = softmax(z) (6.12)
为便于记住所有变量的形状：x ∈ Rn0，h ∈ Rn1，b ∈ Rn1，W ∈ Rn1×n0，U ∈ Rn2×n1，输出向量 y ∈ Rn2。我们称这个网络为 2 层网络（在给层编号时，我们通常不把输入层计算在内，但会把输出层计算在内）。因此按这套术语，逻辑回归是一个 1 层网络。

> And just to remember the shapes of all our variables, x ∈Rn0, h ∈Rn1, b ∈Rn1, W ∈Rn1×n0, U ∈Rn2×n1, and the output vector y ∈Rn2. We’ll call this network a 2layer network (we traditionally don’t count the input layer when numbering layers, but do count the output layer). So by this terminology logistic regression is a 1-layer network.

### 6.3.1 前馈网络的更多细节

> 6.3.1 More details on feedforward networks

现在我们来约定一些记号，以便更容易讨论深度大于 2 的更深网络。我们用方括号中的上标表示层号，从输入层的 0 开始。因此 W[1] 表示（第一个）隐藏层的权重矩阵，b[1] 表示（第一个）隐藏层的偏置向量。nj 表示第 j 层的单元数。我们用 g(·) 表示激活函数，中间层通常采用 ReLU 或 tanh 函数，输出层则采用 softmax。我们用 a[i] 表示第 i 层的输出，用 z[i] 表示上一层输出、权重与偏置的组合 W[i]a[i−1] + b[i]。第 0 层用于输入，因此我们把输入 x 更一般地称为 a[0]。

> Let’s now set up some notation to make it easier to talk about deeper networks of depth more than 2. We’ll use superscripts in square brackets to mean layer numbers, starting at 0 for the input layer. So W[1] will mean the weight matrix for the(first) hidden layer, and b[1] will mean the bias vector for the (first) hidden layer. nj will mean the number of units at layer j. We’ll use g(·) to stand for the activation function, which will tend to be ReLU or tanh for intermediate layers and softmax for output layers. We’ll use a[i] to mean the output from layer i, and z[i] to mean the combination of previous layer output, weights and biases W[i]a[i−1] + b[i]. The 0th layer is for inputs, so we’ll refer to the inputs x more generally as a[0].

因此，我们可以把式 6.12 中的 2 层网络重新表示如下：

> Thus we can re-represent our 2-layer net from Eq. 6.12 as follows:

z[1] = W[1]a[0] +b[1] a[1] = g[1](z[1]) z[2] = W[2]a[1] +b[2] a[2] = g[2](z[2])ˆy = a[2]

(6.13)

注意，有了这套记号，每一层所做计算的公式都是相同的。因此，给定输入向量 a[0]，在 n 层前馈网络中计算前向步骤的算法就简单地是：

> Note that with this notation, the equations for the computation done at each layer are the same. The algorithm for computing the forward step in an n-layer feedforward network, given the input vector a[0] is thus simply:

> for i in 1,...,n z[i] = W[i]a[i−1] +b[i] a[i] = g[i](z[i])ˆy = a[n]

为紧接在最终 softmax 之前的那最后一组激活值取一个名字，往往很有用。

> It’s often useful to have a name for the final set of activations right before the final

因此，无论我们有多少层，通常都把最终向量 z[n] 中未归一化的值——即紧接在最终 softmax 之前的那个得分向量——称为 logits（见式 4.7）。

> softmax. So however many layers we have, we’ll generally call the unnormalized values in the final vector z[n], the vector of scores right before the final softmax, the logits (see Eq. 4.7).

> `logits`
>
> 释义：指输出层做归一化之前的那组未归一化得分，是最终向量 z[n] 的取值，经 softmax 后转成概率分布。

非线性激活函数的必要性　我们在神经网络中为每一层使用非线性激活函数的原因之一是：如果不这样做，得到的网络就完全等价于一个单层网络。我们来看看为什么会这样。设想这样一个纯线性层网络的前两层：

> The need for non-linear activation functions One of the reasons we use nonlinear activation functions for each layer in a neural network is that if we did not, the resulting network is exactly equivalent to a single-layer network. Let’s see why this is true. Imagine the first two layers of such a network of purely linear layers:

z[1] = W[1]x+b[1] z[2] = W[2]z[1] +b[2]
我们可以把网络所计算的函数改写为：

> We can rewrite the function that the network is computing as:

z[2] = W[2]z[1] +b[2]
= W[2](W[1]x+b[1])+b[2]= W[2]W[1]x+W[2]b[1] +b[2]
= W′x+b′ (6.14)
这一点可推广到任意层数。因此，如果没有非线性激活函数，多层网络就只是一个权重集合不同的单层网络在记号上的变体，我们也就失去了多层网络的全部表示能力。

> This generalizes to any number of layers. So without non-linear activation functions, a multilayer network is just a notational variant of a single layer network with a different set of weights, and we lose all the representational power of multilayer networks.

替换偏置单元　在描述网络时，我们有时会使用一种略微简化的记号，它表示完全相同的函数，却不显式引用偏置节点 b。取而代之的是，我们在每一层添加一个取值恒为 1 的哑节点 a0。这样，第 0 层即输入层会有一个哑节点 a[0] 0 = 1，第 1 层会有 a[1] 0 = 1，依此类推。这个哑节点仍然带有一个相关权重，该权重就代表偏置值 b。例如，我们不写成下面这样的等式

> Replacing the bias unit In describing networks, we will sometimes use a slightly simplified notation that represents exactly the same function without referring to an explicit bias node b. Instead, we add a dummy node a0 to each layer whose value will always be 1. Thus layer 0, the input layer, will have a dummy node a[0] 0 = 1, layer 1 will have a[1] 0 = 1, and so on. This dummy node still has an associated weight, and that weight represents the bias value b. For example instead of an equation like
h = σ(Wx+b) (6.15)
而是使用：

> we’ll use:

h = σ(Wx) (6.16)
但现在我们的向量 x 不再是具有 n0 个值：x = x1,...,xn0，而是具有 n0 +1 个值，其中新增了一个第 0 个哑值 x0 = 1：x = x0,...,xn0。并且，我们不再按如下方式计算每个 h j：

> But now instead of our vector x having n0 values: x = x1,...,xn0, it will have n0 +1 values, with a new 0th dummy value x0 = 1: x = x0,...,xn0. And instead of computing each h j as follows:

n0 ! X (6.17)
h j = σ Wji xi +b j ,
我们改用：

> we’ll instead use:

> i=1

n0 ! X (6.18)
h j = σ Wji xi ,
其中 Wj0 的值取代了原先的 b j。图 6.9 给出了可视化结果。

> where the value Wj0 replaces what had been b j. Fig. 6.9 shows a visualization.

> i=0

![](images/06-neural-networks/fig_p11_0.png)

*图 6.9 用 x0（b）替换偏置节点（如 a 所示）。*
*Figure 6.9 Replacing the bias node (shown in a) with x0 (b).*

在第 6.6 节讲解学习算法时，我们仍会把偏置表示为 b，

> We’ll continue showing the bias as b when we go over the learning algorithm
但在本书后续内容中，对于大多数图和部分公式，我们将使用这种不含显式偏置项的简化记法。

> in Section 6.6, but going forward in the book, for most figures and some equations we’ll use this simplified notation without explicit bias terms.

## 6.4 用于 NLP 的前馈网络：分类

> 6.4 Feedforward networks for NLP: Classification

让我们看看如何将前馈网络应用于 NLP 分类任务。在实践中，简单的前馈网络并不是我们做文本分类所采用的方式；对于真实应用，我们会使用更复杂的架构，例如第 9 章的 BERT 变换器。尽管如此，了解前馈网络文本分类器可以让我们引入一些关键思想，这些思想会在本书余下部分中发挥作用，包括嵌入矩阵、表示池化和表示学习等概念。

> Let’s see how to apply feedforward networks to NLP classification tasks. In practice, simple feedforward networks aren’t the way we do text classification; for real applications we would use more sophisticated architectures like the BERT transformers of Chapter 9. Nonetheless seeing a feedforward network text classifier will let us introduce key ideas that will play a role throughout the rest of the book, including the ideas of the embedding matrix, representation pooling, and representation learning.

但在介绍这些想法之前，让我们先从一个分类器开始，它只是

> But before introducing any of these ideas, let’s start with a classifier by making
对我们在第 4 章中看到的情感分类器做了最小的改动。与它们一样，我们将采用手工构建的特征，让这些特征通过分类器，并产生类别概率。唯一的区别在于，我们使用神经网络而不是逻辑回归作为分类器。

> only minimal change from the sentiment classifiers we saw in Chapter 4. Like them, we’ll take hand-built features, pass them through a classifier, and produce a class probability. The only difference is that we’ll use a neural network instead of logistic regression as the classifier.

### 6.4.1 使用手工构建特征的神经网络分类器

> 6.4.1 Neural net classifiers with hand-built features

让我们从一个简单的 2 层情感分类器开始：取第 4 章的逻辑回归分类器（它对应一个 1 层网络），再添加一个隐藏层。输入元素 xi 可以是图 4.2 那样的标量特征，例如 x1 = count(words ∈doc)，x2 = count(positive lexicon words ∈doc)，x3 = 1（如果 “no” ∈doc），等等，共 d 个特征。输出层的 ˆy 可以有两个节点（分别对应正面和负面），也可以有 3 个节点（正面、负面、中性），此时 ˆy1 将是正面情感的估计概率，ˆy2 是负面的概率，ˆy3 是中性的概率。由此得到的公式就与上面看到的 2 层网络相同（一如既往，我们继续用 σ 表示任意非线性，无论是 sigmoid 函数、ReLU 还是其他）。

> Let’s begin with a simple 2-layer sentiment classifier by taking our logistic regression classifier from Chapter 4, which corresponds to a 1-layer network, and just adding a hidden layer. The input element xi can be scalar features like those in Fig. 4.2, e.g., x1 = count(words ∈doc), x2 = count(positive lexicon words ∈doc), x3 = 1 if “no” ∈doc, and so on, for a total of d features. And the output layerˆy could have two nodes (one each for positive and negative), or 3 nodes (positive, negative, neutral), in which case ˆy1 would be the estimated probability of positive sentiment, ˆy2 the probability of negative and ˆy3 the probability of neutral. The resulting equations would be just what we saw above for a 2-layer network (as always, we’ll continue to use the σ to stand for any non-linearity, whether sigmoid, ReLU or other).

x = [x1,x2,...,xd]（每个 xi 都是一个手工设计的特征）

> x = [x1,x2,...,xd] (each xi is a hand-designed feature)
h = σ(Wx+b)
z = Uh
ˆy = softmax(z) (6.19)
图 6.10 给出了该架构的示意图。如前所述，在逻辑回归分类器中加入这个隐藏层，可以让网络表示特征之间的非线性交互。仅凭这一点就可能得到一个更好的情感分类器。

> Fig. 6.10 shows a sketch of this architecture. As we mentioned earlier, adding this hidden layer to our logistic regression classifier allows the network to represent the non-linear interactions between features. This alone might give us a better sentiment classifier.

![](images/06-neural-networks/fig_p12_0.png)

*图 6.10 使用传统手工构建特征的前馈网络情感分析*
*Figure 6.10 Feedforward network sentiment analysis using traditional hand-built features of the input text.*

### 6.4.2 向量化以实现并行推理

> 6.4.2 Vectorizing for parallelizing inference

式 6.19 展示了如何对一个样本 x 进行分类，但在实践中我们希望对包含 m 个样本的整个测试集高效地进行分类。我们通过对该过程进行向量化来实现这一点，正如在逻辑回归中所见；我们不使用 for 循环逐个处理样本，而是使用矩阵乘法一次完成整个测试集的计算。首先，我们把每个输入 x 的所有输入特征向量打包成一个输入矩阵 X，其中第 i 行是由输入样本 x(i) 的特征构成的行向量（即向量 x(i)）。如果输入特征向量的维度为 d，则 X 是一个形状为 [m×d] 的矩阵。

> While Eq. 6.19 shows how to classify a single example x, in practice we want to efficiently classify an entire test set of m examples. We do this by vectorizing the process, just as we saw with logistic regression; instead of using for-loops to go through each example, we’ll use matrix multiplication to do the entire computation of an entire test set at once. First, we pack all the input feature vectors for each input x into a single input matrix X, with each row i a row vector consisting of the features for input example x(i) (i.e., the vector x(i)). If the dimensionality of our input feature vector is d, X will be a matrix of shape [m×d].

由于我们现在把每个输入建模为行向量而不是列向量，

> Because we are now modeling each input as a row vector rather than a column
我们还需要稍微修改式 6.19。X 的形状为 [m×d]，W 的形状为 [dh ×d]，因此我们需要调整 X 与 W 相乘的顺序并转置 W，使它们正确相乘后得到形状为 [m×dh] 的矩阵 H。1

> vector, we also need to slightly modify Eq. 6.19. X is of shape [m×d] and W is of shape [dh ×d], so we’ll reorder how we multiply X and W and transpose W so they correctly multiply to yield a matrix H of shape [m×dh]. 1
式 6.19 中形状为 [1×dh] 的偏置向量 b 现在必须被复制

> The bias vector b from Eq. 6.19 of shape [1×dh] will now have to be replicated
成形状为 [m × dh] 的矩阵。我们还需要以类似方式调整下一步的顺序，并转置 U。最后，我们的输出矩阵 ˆY 的形状为 [m × 3]（更一般地是 [m × do]，其中 do 是输出类别数），输出矩阵 ˆY 的第 i 行由输出向量 ˆy(i) 构成。以下是计算整个测试集输出类别分布的最终公式：

> into a matrix of shape [m × dh]. We’ll need to similarly reorder the next step and transpose U. Finally, our output matrix ˆY will be of shape [m × 3] (or more generally [m × do], where do is the number of output classes), with each row i of our output matrix ˆY consisting of the output vector ˆy(i). Here are the final equations for computing the output class distribution for an entire test set:

H = σ(XW⊺+b) Z = HU⊺ˆY = softmax(Z) (6.20)
在本书中，我们有时会看到 WX + b 这样的顺序，有时会看到 XW + b。

> In this book, we’ll sometimes see orderings like WX + b and sometimes XW + b.

这就是为什么始终要十分留意任意给定公式中所涉及的权重矩阵的形状。

> That’s why it’s always important to be very aware of the shapes of your weight matrices participating in any given equation.

## 6.5 以嵌入作为神经网络分类器的输入

> 6.5 Embeddings as the input to neural net classifiers

虽然手工构建特征是设计分类器的传统方式，但 NLP 中大多数神经网络应用并不使用人工工程化的手工特征作为输入。相反，我们利用深度学习从数据中学习特征的能力，把词元表示为嵌入。本节中，我们将用第 5 章介绍过计算方法的静态 word2vec 或 GloVe 嵌入来表示每个词元。

> While hand-built features are a traditional way to design classifiers, most applications of neural networks for NLP don’t use hand-built human-engineered features as inputs. Instead, we draw on deep learning’s ability to learn features from the data by representing tokens as embeddings. For this section we’ll represent each token by its static word2vec or GloVe embeddings that we saw how to compute in Chapter 5.

所谓静态嵌入，是指每个词元都由一个固定的向量表示，我们只训练一次，然后把它放进一个大的词典中。当我们需要引用该词元时，就从词典中取出它的嵌入。

> By static embedding, we mean that each token is represented by a fixed vector that we train once, and then just put into a big dictionary. When we want to refer to that token, we grab its embedding out of the dictionary.

然而，当我们将神经模型应用于语言建模任务时（正如

> However when we apply neural models to the task of language modeling (as
我们将在第 7 章看到的那样），情况会更复杂，我们将使用一种更强大的嵌入，称为上下文嵌入。上下文嵌入在同一个词每次出现于不同上下文时都不相同。此外，我们会让网络把学习这些嵌入作为词预测任务的一部分。

> we’ll see in Chapter 7) the situation is more complex, and we’ll use a more powerful kind of embedding called a contextual embedding. Contextual embeddings are different for each time a word occurs in a different context. Furthermore, we’ll have the network learn these embeddings as part of the task of word prediction.

因此，让我们来探讨上面的文本分类任务，只不过使用静态嵌入

> So let’s explore the text classification domain above, but using static embeddings
作为特征，而不是手工设计的特征。让我们关注推理阶段，

> as features instead of the hand-designed features. Let’s focus on the inference stage,
其中我们已经为所有输入词元学习到了嵌入。嵌入是表示输入词元的 d 维向量。而存放这些

> in which we have already learned embeddings for all the input tokens. An embedding is a vector of dimension d that represents the input token. The dictionary of

> 矩阵 X 把每个输入表示为列向量而非行向量，使其形状为 [d ×m]。但
>
> *matrix X represent each input as a column vector instead of a row vector, making it of shape [d ×m]. But*

> `embedding matrix`（嵌入矩阵）
>
> 释义：把词表中每个词元映射为稠密向量的查找表，网络从中取出词元对应的向量作为输入。

静态嵌入的词典，就是嵌入矩阵

> static embeddings in which we store these embeddings is the embedding matrix

- 嵌入矩阵的每一行都把词表 V 中的每个词元表示为一个维度为 d 的（行）向量。由于 E 为词表中的 |V| 个词元各留一行，因此 E 的形状为 [|V|×d]。每当我们把嵌入用作神经 NLP 系统的输入时，这个嵌入矩阵 E 都会发挥作用，其中也包括我们将在随后几章介绍的基于 transformer 的大语言模型。

> Each row of the embedding matrix represents each token of the vocabulary V as a (row) vector of dimensionality d. Since E has a row for each of the |V| tokens in the vocabulary, E has shape [|V|×d]. This embedding matrix E plays a role whenever we are using embeddings as input to neural NLP systems, including in the transformer-based large language models we will introduce over the next chapters.

给定像 dessert was great 这样的输入词元串，我们先把这些词元

> Given an input token string like dessert was great we first convert the tokens
转换为词表索引（这些索引是在我们最初使用 BPE 或 SentencePiece 对输入分词时生成的）。因此，dessert was great 的表示可能是 w = [3,524,902]。接下来我们用索引从 E 中选出对应的行（第 3 行、第 524 行、第 902 行）。

> into vocabulary indices (these were created when we first tokenized the input using BPE or SentencePiece). So the representation of dessert was great might be w = [3,524,902]. Next we use indexing to select the corresponding rows from E(row 3, row 524, row 902).

理解从嵌入矩阵中选取词元嵌入的另一种方式，

> Another way to think about selecting token embeddings from the embedding
是把输入词元表示为形状为 [1 × |V|] 的独热向量，也就是说，词表中的每个词各占一个维度。回顾一下，在独热向量中，所有

> matrix is to represent input tokens as one-hot vectors of shape [1 × |V|], i.e., with one dimension for each word in the vocabulary. Recall that in a one-hot vector all

> `one-hot vector`（独热向量）
>
> 释义：只有一位为 1、其余为 0 的稀疏向量，用来指明词表中某个词所处的位置。

元素都为 0，只有一个例外，即维度对应词在词表中索引的那个元素，其值为 1。所以，如果词“dessert”在词表中的索引为 3，那么 x3 = 1，而对所有 i≠3 都有 xi = 0，如下所示：

> the elements are 0 except one, the element whose dimension is the word’s index in the vocabulary, which has value 1. So if the word “dessert” has index 3 in the vocabulary, x3 = 1, and xi = 0 ∀i̸ = 3, as shown here:

[0 0 1 0 0 0 0 ... 0 0 0 0] 1 2 3 4 5 6 7 ... ... |V|
用一个只有一个非零元素 xi = 1 的独热向量去乘，就等于

> Multiplying by a one-hot vector that has only one non-zero element xi = 1 simply
挑出词 i 对应的行向量，从而得到词 i 的嵌入，如图 6.11 所示。

> selects out the relevant row vector for word i, resulting in the embedding for word i, as depicted in Fig. 6.11.

![](images/06-neural-networks/fig_p14_1.png)

*图 6.11 用嵌入矩阵 E 乘以一个在第 3 位为 1 的独热向量，从而选出词 V3 的嵌入向量。*
*Figure 6.11 Selecting the embedding vector for word V3 by multiplying the embedding matrix E with a one-hot vector with a 1 in index 3.*

我们可以把这一思路推广开来，将整个输入词元序列表示为一个矩阵，

> We can extend this idea to represent the entire input token sequence as a matrix
该矩阵由独热向量组成，N 个输入位置各有一个，如图 6.12 所示。

> of one-hot vectors, one for each of the N input positions as shown in Fig. 6.12.

![](images/06-neural-networks/fig_p14_0.png)

*图 6.12 用与词元 id 序列 W 对应的独热矩阵乘以嵌入矩阵 E，从而选出该输入序列的嵌入矩阵。*
*Figure 6.12 Selecting the embedding matrix for the input sequence of token ids W by multiplying a one-hot matrix corresponding to W by the embedding matrix E.*

现在我们需要把这 N 个 [1×d] 嵌入构成的输入（代表一个含 N 个词元的窗口）归入单一类别（例如正面或负面）。

> We now need to classify this input of N [1×d] embeddings, representing a window of N tokens, into a single class (like positive or negative).

把嵌入传给分类器有两种常见方式：拼接

> There are two common ways to pass embeddings to a classifier: concatenation
和池化。第一种，我们可以取这个形状为 [N × d] 的输入，把所有输入向量拼接成一个形状为 [1 × dN] 的很长的向量来重塑它。然后把这个输入传给分类器，让它作出判定。这样能得到大量信息，代价是要使用一个相当大的网络。第二种，我们可以把这 N 个嵌入池化为单个嵌入，然后把这个池化后的单个嵌入传给分类器。池化得到的信息比原有全部嵌入所包含的信息要少，但优点是规模小、效率高，而且在那些我们不太在意原始词序的任务中特别有用。下面各举一例：情感任务采用池化，语言建模任务采用拼接。

> and pooling. First, we can take this input of shape [N × d] and reshape it by concatenating all the input vectors into one very long vector of shape [1 × dN]. Then we pass this input to our classifier and let it make its decision. This gives us lots of information, at the cost of using a pretty large network. Second, we can pool the N embeddings into a single embedding and then pass that single pooled embedding to the classifier. Pooling gives us less information than would have been present in all the original embeddings, but has the advantage of being small and efficient and is especially useful in tasks for which we don’t care as much about the original word order. Let’s give an example of each: pooling for the sentiment task, and concatenation for the language modeling task.

> `pool`（池化）
>
> 释义：把一组嵌入向量合并为单个向量的操作，常见形式有取平均或逐维取最大值。

为情感分析池化输入嵌入 我们先来看看池化如何用于情感分类任务。池化的直觉是：对情感而言，输入的确切位置（像 great 这样的词是第一个词还是第二个词？）不如词本身是什么重要。

> Pooling input embeddings for sentiment So let’s begin with seeing how pooling can work for the sentiment classification task. The intuition of pooling is that for sentiment, the exact position of the input (is some word like great the first word? the second word?) is less important than the identity of the word itself.

池化函数是一种把一组嵌入变成单个嵌入的方法。

> A pooling function is a way to turn a set of embeddings into a single embedding.

例如，对于含 N 个输入词/词元 w1,...,wN 的文本，我们要把

> For example, for a text with N input words/tokens w1,...,wN, we want to turn
这 N 个行嵌入 e(w1),...,e(wN)（每个维度均为 d）变成单个同样维度为 d 的嵌入。

> the N row embeddings e(w1),...,e(wN) (each of dimensionality d) into a single embedding also of dimensionality d.

池化的方式有多种。最简单的是平均池化：取平均，

> There are various ways to pool. The simplest is mean-pooling: taking the mean

> `mean-pooling`（平均池化）
>
> 释义：把一组嵌入逐维求算术平均，合成单个向量，不区分各词所处的位置。

即把各嵌入相加再除以 N：

> by summing the embeddings and then dividing by N:

> N

xmean = 1 X
e(wi) (6.21)
N
下面是这个分类器在采用平均池化时的方程：

> Here are the equations for this classifier assuming mean pooling:

> i=1

x = mean(e(w1),e(w2),...,e(wn))
h = σ(xW +b)
z = hU
ˆy = softmax(z) (6.22)
该架构如图 6.13 所示，图中也给出了所有相关矩阵的形状（注意我们现在使用的是行向量）。

> The architecture is sketched in Fig. 6.13, where we also give the shapes for all the relevant matrices (note that we’re using row vectors now).

池化还有许多其他选择，例如最大池化，在这种情况下，对

> There are many other options for pooling, like max-pooling, in which case for

> `max-pooling`（最大池化）
>
> 释义：在每个维度上取所有输入嵌入该维的最大值，合成单个向量。

每个维度，我们在所有输入上取逐元素最大值。一组 N 个向量的逐元素最大值是一个新向量，其第 k 个元素是这 N 个向量第 k 个元素中的最大值。

> each dimension we take the element-wise max over all the inputs. The element-wise max of a set of N vectors is a new vector whose kth element is the max of the kth elements of all the N vectors.

语言建模中输入嵌入的拼接　在情感分析中我们看到，给定一个包含 N 个输入词元的窗口作为输入，可以先把这些词元嵌入池化成单个嵌入向量，从而生成一个在三个类别（正面、负面或中性）上给出概率的输出向量。

> Concatenating input embeddings for language modeling For sentiment analysis we saw how to generate an output vector with probabilities over three classes: positive, negative, or neutral, given as input a window of N input tokens, by first pooling those token embeddings into a single embedding vector.

现在让我们来考虑语言建模：根据前面的

> Now let’s consider language modeling: predicting upcoming words from prior
词预测即将出现的词。在这项任务中，我们同样给定一个包含 N 个输入词元的窗口，但现在的任务是预测应当跟随在该窗口之后的下一词元。我们将勾勒一个简单的前馈神经语言模型，它借鉴了 Bengio 等人（2003）最先提出的算法。前馈语言模型引入了大规模语言建模的许多重要概念，我们将在第 7 章中再次讨论这些内容。

> words. In this task we are given the same window of N input tokens, but our task now is to predict the next token that should follow the window. We’ll sketch a simple feedforward neural language model, drawing on an algorithm first introduced by Bengio et al. (2003). The feedforward language model introduces many of the important concepts of large language modeling that we will return to in Chapter 7.

与第 3 章的 n-gram 语言模型相比，神经语言模型有许多优势。神经语言模型能够处理长得多的历史，能够在相似词的上下文之间更好地泛化，并且在词预测上准确得多。另一方面，神经网络语言模型更慢、更复杂、训练需要消耗大量能源，并且比 n-gram 模型更难解释，因此对于一些较小的任务，n-gram 语言模型仍然是合适的工具。

> Neural language models have many advantages over the n-gram language models of Chapter 3. Neural language models can handle much longer histories, can generalize better over contexts of similar words, and are far more accurate at wordprediction. On the other hand, neural net language models are slower, more complex, need vast amounts of energy to train, and are less interpretable than n-gram models, so for some smaller tasks an n-gram language model is still the right tool.

![](images/06-neural-networks/fig_p16_0.png)

*图 6.13 使用输入词的池化嵌入进行的前馈网络情感分析。在每个时间步，网络为每个上下文词计算一个 d 维嵌入（用一个独热向量乘以嵌入矩阵 E），并把得到的 N 个嵌入池化，得到一个表示上下文窗口的单一嵌入，作为层 x。*
*Figure 6.13 Feedforward network sentiment analysis using a pooled embedding of the input words. At each timestep the network computes a d-dimensional embedding for each context word (by multiplying a one-hot vector by the embedding matrix E), and pools the resulting N embeddings to get a single embedding that represents the context window as the layer x.*

前馈神经语言模型是一种前馈网络，它在时刻 t 把

> A feedforward neural language model is a feedforward network that takes as
若干前面词的表示（wt−1、wt−2 等）作为输入，并输出在可能的下一词上的概率分布。因此——与 n-gram 语言模型一样——前馈神经语言模型通过基于前面的 N−1 个词进行近似，来近似给定全部先前上下文时一个词的概率 P(wt|w1:t−1)：

> input at time t a representation of some number of previous words (wt−1,wt−2, etc.) and outputs a probability distribution over possible next words. Thus—like the ngram LM—the feedforward neural LM approximates the probability of a word given the entire prior context P(wt|w1:t−1) by approximating based on the N −1 previous words:

P(wt|w1,...,wt−1) ≈P(wt|wt−N+1,...,wt−1) (6.23)
在下面的例子中我们使用一个 4-gram 的示例，因此我们将展示一个用于估计概率 P(wt = i|wt−3,wt−2,wt−1) 的神经网络。

> In the following examples we’ll use a 4-gram example, so we’ll show a neural net to estimate the probability P(wt = i|wt−3,wt−2,wt−1).

神经语言模型用词的嵌入来表示这一先前上下文中的词，而不是像 n-gram 语言模型那样仅仅使用词的标识。

> Neural language models represent words in this prior context by their embeddings, rather than just by their word identity as used in n-gram language models.

使用嵌入使神经语言模型能够更好地泛化到未见过的数据。例如，假设我们在训练中见过下面这个句子：

> Using embeddings allows neural language models to generalize better to unseen data. For example, suppose we’ve seen this sentence in training:

我得确保这只猫有人喂。

> I have to make sure that the cat gets fed.

但从未见过 “gets fed” 这两个词出现在 “dog” 一词之后。我们的测试集有前缀 “I forgot to make sure that the dog gets”。下一个词是什么？n-gram 语言模型会在 “that the cat gets” 之后预测出 “fed”，但不会在 “that the dog gets” 之后这样做。而神经语言模型知道 “cat” 和 “dog” 有相似的嵌入，因而能够从 “cat” 的上下文泛化出去，即使见到的是 “dog”，也能给 “fed” 赋予足够高的概率。

> but have never seen the words “gets fed” after the word “dog”. Our test set has the prefix “I forgot to make sure that the dog gets”. What’s the next word? An n-gram language model will predict “fed” after “that the cat gets”, but not after “that the dog gets”. But a neural LM, knowing that “cat” and “dog” have similar embeddings, will be able to generalize from the “cat” context to assign a high enough probability to“fed” even after seeing “dog”.

![](images/06-neural-networks/fig_p17_0.png)

*图 6.14 前馈神经语言模型中的前向推理。在每个时间步 t，网络为 N = 3 个上下文词元中的每一个计算一个 d 维嵌入（用一个独热向量乘以嵌入矩阵 E），并把这三个嵌入拼接起来得到嵌入 e。该嵌入 e 乘以权重矩阵 W，然后逐元素施加激活函数得到隐藏层 h，h 再乘以另一个权重矩阵 U。softmax 层在每个输出节点 i 上预测下一词 wt 为词表词 Vi 的概率。这里把上下文窗口大小 N 画成 3 只是为了适合页面，而在实践中语言建模需要长得多的上下文。*
*Figure 6.14 Forward inference in a feedforward neural language model. At each timestep t the network computes a d-dimensional embedding for each of the N = 3 context tokens (by multiplying a one-hot vector by the embedding matrix E), and concatenates the three to get the embedding e. This embedding e is multiplied by weight matrix W and then an activation function is applied element-wise to produce the hidden layer h, which is then multiplied by another weight matrix U. A softmax layer predicts at each output node i the probability that the next word wt will be vocabulary word Vi. We show the context window size N as 3 just to fit on the page, but in practice language modeling requires a much longer context.*

这一预测任务需要一个给出 |V| 个概率的输出向量：

> This prediction task requires an output vector that expresses |V| probabilities:

即每个可能的下一词元对应一个概率值。词表可能有 60,000 到 300,000 个词元，所以语言建模任务的输出向量比 3 长得多。语言建模的另一个不同之处在于，我们不是把 N 个输入词元的嵌入池化成单个嵌入，而是把输入拼接成一个非常长的输入向量。要预测下一词元，知道每个前面的词元以及它们的先后顺序是有帮助的。

> one probability value for each possible next token. We might have a vocabulary between 60,000 and 300,000 tokens, so the output vector for the task of language modeling is much longer than 3. Another difference for language modeling is that instead of pooling the embeddings of the N input tokens to create a single embedding, we concatenate the inputs into one very long input vector. To predict the next token, it helps to know each of the preceding tokens and what order they were in.

图 6.14 展示了语言建模任务，为了适合页面，这里用很短的上下文

> Fig. 6.14 shows the language modeling task, sketched with a very short context
窗口 N = 3 来示意。这 3 个嵌入向量被拼接起来得到 e，即嵌入层。它乘以权重矩阵 W 得到隐藏层，再乘以另一个权重矩阵 U 得到输出层，输出层的 softmax 给出词上的概率分布。例如 y42，即输出节点 42 的值，是下一词 wt 为 V42 的概率，V42 是索引为 42 的词表词（在我们的例子中是词 ‘fish’）。

> window of N = 3 just to fit on the page. These 3 embedding vectors are concatenated to produce e, the embedding layer. This is multiplied by a weight matrix W to produce a hidden layer, and another weight matrix U to produce an output layer whose softmax gives a probability distribution over words. For example y42, the value of output node 42, is the probability of the next word wt being V42, the vocabulary word with index 42 (which is the word ‘fish’ in our example).

对于一个窗口大小为 3、给定每个输入上下文词的独热输入向量的简单前馈神经语言模型，其公式为：

> The equations for a simple feedforward neural language model with a window size of 3, given one-hot input vectors for each input context word, are:

e = [Ext−3;Ext−2;Ext−1] h = σ(We+b)
z = Uh
ˆy = softmax(z) (6.24)
注意我们用分号表示向量的拼接，因此我们通过拼接三个上下文向量各自的 3 个嵌入来构成嵌入层 e。

> Note that we use semicolons to mean concatenation of vectors, so we form the embedding layer e by concatenating the 3 embeddings for the three context vectors.

我们将在介绍

> We’ll return to this idea of using neural networks to do language modeling in
第 7 章 transformer 语言模型时，再回到用神经网络进行语言建模这一想法。

> Chapter 7 when we introduce transformer language models.

## 6.6 训练神经网络

> 6.6 Training Neural Nets

前馈神经网络是监督机器学习的一个实例，其中我们知道每个观测 x 对应的正确输出 y。系统通过式 6.13 产生的是 ˆy，即系统对真实 y 的估计。训练过程的目标是学习每一层 i 的参数 W[i] 和 b[i]，使每个训练观测的 ˆy 尽可能接近真实 y。

> A feedforward neural net is an instance of supervised machine learning in which we know the correct output y for each observation x. What the system produces, via Eq. 6.13, is ˆy, the system’s estimate of the true y. The goal of the training procedure is to learn parameters W[i] and b[i] for each layer i that make ˆy for each training observation as close as possible to the true y.

总的来说，我们做这一切所依据的，都是我们在第 4 章介绍的

> In general, we do all this by drawing on the methods we introduced in Chapter 4
逻辑回归方法，因此读者在继续之前应当对那一章比较熟悉。我们将在简单的通用网络上探讨该算法，而不是在为情感分析或语言建模设计的网络上探讨。

> for logistic regression, so the reader should be comfortable with that chapter before proceeding. We’ll explore the algorithm on simple generic networks rather than networks designed for sentiment or language modeling.

首先，我们需要一个损失函数来刻画系统

> First, we’ll need a loss function that models the distance between the system
输出与标准输出之间的距离，通常使用逻辑回归所用的损失函数，即交叉熵损失。

> output and the gold output, and it’s common to use the loss function used for logistic regression, the cross-entropy loss.

其次，为了找到使该损失函数最小的参数，我们将使用

> Second, to find the parameters that minimize this loss function, we’ll use the
第 4 章介绍的梯度下降优化算法。

> gradient descent optimization algorithm introduced in Chapter 4.

第三，梯度下降需要知道损失函数的梯度，即那个

> Third, gradient descent requires knowing the gradient of the loss function, the
包含损失函数对每个参数的偏导数的向量。在逻辑回归中，对于每个观测，我们可以直接计算损失函数关于某个 w 或 b 的导数。但对于神经网络，许多层中有数百万个参数，当损失挂在某个靠后得多的层上时，要计算第 1 层某个权重的偏导数就困难得多。我们如何把损失分摊到所有这些中间层上？答案就是被称为误差反向传播或反向微分的算法。

> vector that contains the partial derivative of the loss function with respect to each of the parameters. In logistic regression, for each observation we could directly compute the derivative of the loss function with respect to an individual w or b. But for neural networks, with millions of parameters in many layers, it’s much harder to see how to compute the partial derivative of some weight in layer 1 when the loss is attached to some much later layer. How do we partial out the loss over all those intermediate layers? The answer is the algorithm called error backpropagation or backward differentiation.

### 6.6.1 损失函数

> 6.6.1 Loss function

> `cross-entropy loss`（交叉熵损失）
>
> 释义：衡量模型输出的概率分布与真实标签分布之间差距的损失函数，逻辑回归和神经网络分类器都用它来指导参数学习。

神经网络中使用的交叉熵损失，与我们在

> The cross-entropy loss that is used in neural networks is the same one we saw for
逻辑回归中看到的那个是同一个。如果神经网络被用作二分类器，最后一层是 sigmoid 函数，那么损失函数就是我们在式 4.19 中看到的同一个逻辑回归损失：

> logistic regression. If the neural network is being used as a binary classifier, with the sigmoid at the final layer, the loss function is the same logistic regression loss we saw in Eq. 4.19:

LCE(ˆy,y) = −log p(y|x) = −[ylog ˆy+(1−y)log(1−ˆy)] (6.25)
如果我们用该网络划分 3 个或更多类别，那么损失函数

> If we are using the network to classify into 3 or more classes, the loss function is
与我们第 4 章第 112 页看到的多项式回归损失完全相同。为方便起见，这里简要重述一下。首先，当类别数超过 2 时，我们需要把 y 和 ˆy 都表示为向量。假设我们做的是硬分类，即只有一个类别是正确的。

> exactly the same as the loss for multinomial regression that we saw in Chapter 4 on page 112. Let’s briefly summarize the explanation here for convenience. First, when we have more than 2 classes we’ll need to represent both y and ˆy as vectors. Let’s assume we’re doing hard classification, where only one class is the correct one.

真实标签 y 则是一个含 K 个元素的向量，每个元素对应一个类别；若正确类别为 c，则 yc = 1，而 y 的其余元素均为 0。回想一下，这种一个值为 1、其余为 0 的向量称为独热向量。

> The true label y is then a vector with K elements, each corresponding to a class, with yc = 1 if the correct class is c, with all other elements of y being 0. Recall that a vector like this, with one value equal to 1 and the rest 0, is called a one-hot vector.

我们的分类器将产生一个含 K 个元素的估计向量 ˆy，其中每个元素 ˆyk 表示估计概率 p(yk = 1|x)。

> And our classifier will produce an estimate vector with K elements ˆy, each elementˆyk of which represents the estimated probability p(yk = 1|x).

对于单个样本 x，损失函数是 K 个

> The loss function for a single example x is the negative sum of the logs of the K
输出类别的对数之和的负值，其中每一项都按其概率 yk 加权：

> output classes, each weighted by their probability yk:

> K

X
LCE(ˆy,y) = − yk log ˆyk (6.26)
我们可以进一步简化这个等式；先用函数 1{} 重写该式，当括号中的条件成立时它取值为 1，否则取值为 0。这样就更容易看出，式 6.26 中求和各项除真实类别所对应的那一项（其 yk = 1）之外都为 0：

> We can simplify this equation further; let’s first rewrite the equation using the function 1{} which evaluates to 1 if the condition in the brackets is true and to 0 otherwise. This makes it more obvious that the terms in the sum in Eq. 6.26 will be 0 except for the term corresponding to the true class for which yk = 1:

> k=1

> K

X
LCE(ˆy,y) = − 1{yk = 1}log ˆyk
换言之，交叉熵损失就是正确类别所对应的输出概率的负对数，因此我们也把它称为负

> In other words, the cross-entropy loss is simply the negative log of the output probability corresponding to the correct class, and we therefore also call this the negative

> k=1

> `negative log likelihood loss`（负对数似然损失）
>
> 释义：多分类硬标签下与交叉熵损失等价的形式，其值是模型赋给正确类别的输出概率取对数后再取负所得。

对数似然损失：

> log likelihood loss:

LCE(ˆy,y) = −log ˆyc （其中 c 为正确类别） (6.27)

> LCE(ˆy,y) = −log ˆyc (where c is the correct class) (6.27)
代入式 6.9 中的 softmax 公式，其中 K 为类别数：

> Plugging in the softmax formula from Eq. 6.9, and with K the number of classes:

exp(zc)
LCE(ˆy,y) = −log （其中 c 为正确类别） (6.28)

> LCE(ˆy,y) = −log (where c is the correct class) (6.28)
PK j=1 exp(z j)
让我们把负对数概率看作损失函数。一个完美的分类器会给正确类别 i 赋予概率 1，而给所有错误类别赋予概率 0。这意味着 p(ˆyi) 越高（越接近 1），分类器就越好；p(ˆyi) 越低（越接近 0），分类器就越差。该概率的负对数是一个很理想的损失度量，因为它从 0（1 的负对数，无损失）一直变化到无穷大（0 的负对数，无穷大损失）。该损失函数还保证：当正确答案的概率被最大化时，所有错误答案的概率被最小化；由于它们之和为 1，正确答案概率的任何增加都是以错误答案的概率为代价的。

> Let’s think about the negative log probability as a loss function. A perfect classifier would assign the correct class i probability 1 and all the incorrect classes probability 0. That means the higher p(ˆyi) (the closer it is to 1), the better the classifier; p(ˆyi) is, and the lower it is (the closer it is to 0), the worse the classifier. The negative log of this probability is a beautiful loss metric since it goes from 0 (negative log of 1, no loss) to infinity (negative log of 0, infinite loss). This loss function also ensures that as probability of the correct answer is maximized, the probability of all the incorrect answers is minimized; since they all sum to one, any increase in the probability of the correct answer is coming at the expense of the incorrect answers.

输出向量 ˆy 的类别数 K 可小可大。也许

> The number K of classes of the output vector ˆy can be small or large. Perhaps
我们的任务是三分类情感分析，那么类别可能是正面、负面和中性。或者，如果我们的任务是判定一个词的词性（即它是名词、动词还是形容词等），那么 K 就是标记集中所有可能的词性（在我们第 18 章将定义的标记集中共有 17 个）。而如果我们的任务是语言建模，分类器要预测下一个词是什么，那么我们的类别集合就是词的集合，可能有 50,000 或 100,000 个。

> our task is 3-way sentiment, and then the classes might be positive, negative, and neutral. Or if our task is deciding the part of speech of a word (i.e., whether it is a noun or verb or adjective, etc.), then K is the set of possible parts of speech in our tagset (of which there are 17 in the tagset we will define in Chapter 18). And if our task is language modeling, and our classifier is trying to predict which word is next, then our set of classes is the set of words, which might be 50,000 or 100,000.

### 6.6.2 计算梯度

> 6.6.2 Computing the Gradient

我们如何计算这个损失函数的梯度？计算梯度需要求出损失函数对每个参数的偏导数。

> How do we compute the gradient of this loss function? Computing the gradient requires the partial derivative of the loss function with respect to each parameter.

对于只有一个权重层、输出为 sigmoid 的网络（也就是逻辑回归的情形），我们可以直接使用式 6.29 中用于逻辑回归的损失导数（其推导见第 4.15 节）：

> For a network with one weight layer and sigmoid output (which is what logistic regression is), we could simply use the derivative of the loss that we used for logistic regression in Eq. 6.29 (and derived in Section 4.15):

∂LCE(ˆy,y)
= (ˆy−y)xj
∂wj
= (σ(w ·x+b)−y)xj (6.29)
或者，对于只有一个权重层、输出为 softmax 的网络（即多项式逻辑回归），我们可以使用式 4.41 中 softmax 损失的导数，这里针对某个特定权重 wk 和输入 xi 给出

> Or for a network with one weight layer and softmax output (=multinomial logistic regression), we could use the derivative of the softmax loss from Eq. 4.41, shown for a particular weight wk and input xi
∂LCE(ˆy,y)
= −(yk −ˆyk)xi
∂wk,i
= −(yk −p(yk = 1|x))xi
!

exp(wk ·x+bk) (6.30)
= − yk − PK xi
j=1 exp(w j ·x+bj)
但这些导数只能为某一个权重层给出正确的更新：最后一层！

> But these derivatives only give correct updates for one weight layer: the last one!

对于深层网络，为每个权重计算梯度要复杂得多，因为我们要对出现在网络最早期层中的权重参数求导，而损失却只在网络的最后端计算。

> For deep networks, computing the gradients for each weight is much more complex, since we are computing the derivative with respect to weight parameters that appear all the way back in the very early layers of the network, even though the loss is computed only at the very end of the network.

解决这一梯度计算问题的算法称为误差反向传播（error backpropagation），简称 backprop（Rumelhart et al., 1986）。尽管反向传播最初是专门

> The solution to computing this gradient is an algorithm called error backpropagation or backprop (Rumelhart et al., 1986). While backprop was invented spe-

> `error back- propagation`（误差反向传播）
>
> 释义：从网络输出端的损失出发，利用链式法则把梯度逐层回传到前面各层，从而一次求得所有权重梯度的算法。

为神经网络而发明的，但它实际上与一个更通用的过程相同，后者称为反向微分（backward differentiation），它依赖于计算图这一概念。下一小节我们就来看它是如何工作的。

> cially for neural networks, it turns out to be the same as a more general procedure called backward differentiation, which depends on the notion of computation graphs. Let’s see how that works in the next subsection.

### 6.6.3 计算图

> 6.6.3 Computation Graphs

计算图是对计算某个数学表达式这一过程的表示，其中计算被分解为若干独立的运算，每个运算被建模为图中的一个节点。

> A computation graph is a representation of the process of computing a mathematical expression, in which the computation is broken down into separate operations, each of which is modeled as a node in a graph.

考虑计算函数 L(a,b,c) = c(a+2b)。如果我们把每一个

> Consider computing the function L(a,b,c) = c(a+2b). If we make each of the
加法与乘法运算都显式写出，并为中间输出取名字（d 和 e），那么得到的计算序列为：

> component addition and multiplication operations explicit, and add names (d and e) for the intermediate outputs, the resulting series of computations is:

d = 2∗b e = a+d L = c∗e
我们现在可以把它表示成一个图，每个运算对应一个节点，有向边表示每个运算的输出作为下一个运算的输入，如图 6.15 所示。计算图最简单的用途是在给定输入下计算函数的值。图中我们假设输入为 a = 3, b = 1, c = −2，并展示了前向传播计算得到结果 L(3,1,−2) = −10 的过程。在计算图的前向传播中，我们自左向右依次施加每个运算，把每次计算的输出作为下一个节点的输入。

> We can now represent this as a graph, with nodes for each operation, and directed edges showing the outputs from each operation as the inputs to the next, as in Fig. 6.15. The simplest use of computation graphs is to compute the value of the function with some given inputs. In the figure, we’ve assumed the inputs a = 3, b = 1, c = −2, and we’ve shown the result of the forward pass to compute the result L(3,1,−2) = −10. In the forward pass of a computation graph, we apply each operation left to right, passing the outputs of each computation as the input to the next node.

![](images/06-neural-networks/fig_p21_0.png)

*图 6.15 函数 L(a,b,c) = c(a+2b) 的计算图，输入节点的取值为 a = 3, b = 1, c = −2，图中展示了 L 的前向传播计算过程。*
*Figure 6.15 Computation graph for the function L(a,b,c) = c(a+2b), with values for input nodes a = 3, b = 1, c = −2, showing the forward pass computation of L.*

### 6.6.4 计算图上的反向微分

> 6.6.4 Backward differentiation on computation graphs

计算图的重要性来自反向传播过程，它用于计算权重更新所需的导数。在本例中，我们的目标是计算输出函数 L 对各个输入变量的导数，即 ∂L ∂a、∂L ∂b 和 ∂L ∂c。导数 ∂L ∂a 告诉我们 a 的微小变化对 L 有多大影响。

> The importance of the computation graph comes from the backward pass, which is used to compute the derivatives that we’ll need for the weight update. In this example our goal is to compute the derivative of the output function L with respect to each of the input variables, i.e., ∂L ∂a, ∂L ∂b, and ∂L ∂c . The derivative ∂L ∂a tells us how much a small change in a affects L.

反向微分利用微积分中的链式法则，因此我们先回顾一下它。假设我们要计算复合函数 f(x) = u(v(x)) 的导数。f(x) 的导数等于 u(x) 对 v(x) 的导数乘以 v(x) 对 x 的导数：

> Backwards differentiation makes use of the chain rule in calculus, so let’s remind ourselves of that. Suppose we are computing the derivative of a composite function f(x) = u(v(x)). The derivative of f(x) is the derivative of u(x) with respect to v(x) times the derivative of v(x) with respect to x:

> `chain rule`（链式法则）
>
> 释义：微积分中求复合函数导数的规则：把外层函数对内层函数的导数与内层函数的导数相乘，是反向传播逐层求梯度的依据。

d f dx = du dv · dv (6.31)
dx
链式法则可以推广到多于两个函数的情形。如果要计算复合函数 f(x) = u(v(w(x))) 的导数，则 f(x) 的导数为：

> The chain rule extends to more than two functions. If computing the derivative of a composite function f(x) = u(v(w(x))), the derivative of f(x) is:

d f dx = du dv · dv dw · dw (6.32)
dx
反向微分的直觉是把梯度从最后一个

> The intuition of backward differentiation is to pass gradients back from the final
节点回传到图中的所有节点。图 6.16 展示了在节点 e 处部分的反向计算。每个节点接收来自其右侧父节点传入的上游梯度，并对自己的每个输入计算局部梯度（即其输出对该输入的梯度），再用链式法则把两者相乘，得到要传给更早那个节点的下游梯度。

> node to all the nodes in the graph. Fig. 6.16 shows part of the backward computation at one node e. Each node takes an upstream gradient that is passed in from its parent node to the right, and for each of its inputs computes a local gradient (the gradient of its output with respect to its input), and uses the chain rule to multiply these two to compute a downstream gradient to be passed on to the next earlier node.

现在我们来计算所需的 3 个导数。由于在计算图中

> Let’s now compute the 3 derivatives we need. Since in the computation graph
L = ce，我们可以直接计算导数 ∂L ∂c：

> L = ce, we can directly compute the derivative ∂L ∂c :

∂L∂c = e (6.33)
对于另外两个导数，我们需要使用链式法则：

> For the other two, we’ll need to use the chain rule:

∂L ∂a = ∂L ∂e
∂e ∂a
∂L ∂b = ∂L ∂e ∂d
∂e ∂d ∂b

![](images/06-neural-networks/fig_p22_1.png)

*图 6.16 每个节点（如这里的 e）接收一个上游梯度，将其与局部梯度（即其输出对其输入的梯度）相乘，并利用链式法则计算出要传给前一个节点的下游梯度。如果一个节点有多个输入，它就可能对应多个局部梯度。*
*Figure 6.16 Each node (like e here) takes an upstream gradient, multiplies it by the local gradient (the gradient of its output with respect to its input), and uses the chain rule to compute a downstream gradient to be passed on to a prior node. A node may have multiple local gradients if it has multiple inputs.*

因此式 6.34 和式 6.33 需要五个中间导数：∂L ∂e、∂L ∂c、∂e ∂a、∂e ∂d，以及

> Eq. 6.34 and Eq. 6.33 thus require five intermediate derivatives: ∂L ∂e , ∂L ∂c , ∂e ∂a, ∂e ∂d , and
∂b，它们分别如下（这里用到了和的导数等于各导数之和这一事实）：

> ∂b, which are as follows (making use of the fact that the derivative of a sum is the sum of the derivatives):

> ∂d

∂L ∂e = c, ∂L
L = ce : ∂c = e
∂a = 1, ∂e ∂e
e = a+d : ∂d = 1
∂d
d = 2b : ∂b = 2
在反向传播过程中，我们沿图中的每条边从右到左计算这些偏导数，所用的方法与上面一样，都是链式法则。因此，我们首先从节点 L 开始计算下游梯度，即 ∂L ∂e 和 ∂L ∂c 。对于节点 e，我们把上游梯度 ∂L ∂e 与局部梯度（输出相对于输入的梯度）∂e ∂d 相乘，得到回传给节点 d 的输出：∂L ∂d 。

> In the backward pass, we compute each of these partials along each edge of the graph from right to left, using the chain rule just as we did above. Thus we begin by computing the downstream gradients from node L, which are ∂L ∂e and ∂L ∂c . For node e, we then multiply this upstream gradient ∂L ∂e by the local gradient (the gradient of the output with respect to the input), ∂e ∂d to get the output we send back to node d: ∂L ∂d .

依此类推，直到我们标注完整个图，一直标注到所有输入变量。

> And so on, until we have annotated the graph all the way to all the input variables.

前向传播过程恰好已经计算出了我们求这些导数所需的前向中间变量的值（如 d 和 e）。图 6.17 展示了反向传播过程。

> The forward pass conveniently already will have computed the values of the forward intermediate variables we need (like d and e) to compute these derivatives. Fig. 6.17 shows the backward pass.

![](images/06-neural-networks/fig_p22_0.png)

*图 6.17 函数 L(a,b,c) = c(a+2b) 的计算图，展示了反向传播的计算过程*
*Figure 6.17 Computation graph for the function L(a,b,c) = c(a+2b), showing the backward pass computation of ∂L ∂a , ∂L ∂b , and ∂L ∂c .*

神经网络的反向微分

> Backward differentiation for a neural network
当然，真实神经网络的计算图要复杂得多。

> Of course computation graphs for real neural networks are much more complex.

图 6.18 给出了一个 2 层神经网络的示例计算图，其中 n0 =2，n1 = 2，n2 = 1；这里假设是二分类任务，因此为简单起见使用 sigmoid 输出单元。该计算图所计算的函数为：

> Fig. 6.18 shows a sample computation graph for a 2-layer neural network with n0 =2, n1 = 2, and n2 = 1, assuming binary classification and hence using a sigmoid output unit for simplicity. The function that the computation graph is computing is:

z[1] = W[1]x+b[1] a[1] = ReLU(z[1]) z[2] = W[2]a[1] +b[2] a[2] = σ(z[2])ˆy = a[2]
对于反向传播过程，我们还需要计算损失 L。损失函数 (6.35)

> For the backward pass we’ll also need to compute the loss L. The loss function (6.35)
对于二分类 sigmoid 输出，由式 6.25 给出，其形式为

> for binary sigmoid output from Eq. 6.25 is
LCE(ˆy,y) = −[ylog ˆy+(1−y)log(1−ˆy)] (6.36)
我们的输出是 ˆy = a[2]，因此可以把它改写为

> Our output ˆy = a[2], so we can rephrase this as
h i
LCE(a[2],y) = − yloga[2] +(1−y)log(1−a[2]) (6.37)

![](images/06-neural-networks/fig_p23_0.png)

*图 6.18 一个简单 2 层神经网络（即 1 个隐藏层）的示例计算图，该网络有两个输入单元和 2 个隐藏单元。我们对记号作了少许调整，以避免在节点中写出冗长的公式，只标出所计算的函数及结果变量名。因此，节点 w[1] 11 右侧的 * 表示 w[1] 11 要与 x1 相乘，节点 z[1] = + 则表示 z[1] 的值由输入到该节点的三个节点求和得到（两个乘积项以及偏置项 b[1] i ）。*
*Figure 6.18 Sample computation graph for a simple 2-layer neural net (= 1 hidden layer) with two input units and 2 hidden units. We’ve adjusted the notation a bit to avoid long equations in the nodes by just mentioning the function that is being computed, and the resulting variable name. Thus the * to the right of node w[1] 11 means that w[1] 11 is to be multiplied by x1, and the node z[1] = + means that the value of z[1] is computed by summing the three nodes that feed into it (the two products, and the bias term b[1] i ).*

需要更新的权重（那些我们需要知道其损失函数偏导数的权重）

> The weights that need updating (those for which we need to know the partial
以青色显示。为了完成反向传播过程，我们需要知道图中所有函数的导数。我们在第 4.15 节已经看到 sigmoid 函数 σ 的导数：

> derivative of the loss function) are shown in teal. In order to do the backward pass, we’ll need to know the derivatives of all the functions in the graph. We already saw in Section 4.15 the derivative of the sigmoid σ:

dσ(z)
= σ(z)(1−σ(z))
dz 我们还需要其他各个激活函数的导数。tanh 函数的导数为：

> dz We’ll also need the derivatives of each of the other activation functions. The derivative of tanh is:

d tanh(z) = 1−tanh2(z) (6.39)
dz
ReLU（修正线性单元）的导数为2

> The derivative of the ReLU is2
 0 for z < 0 (6.40)
d ReLU(z)
dz = 1 for z ≥0
我们将给出计算的开头部分，即计算损失函数 L 关于 z 的导数 ∂L ∂z （其余计算留给读者作为练习）。根据链式法则：

> We’ll give the start of the computation, computing the derivative of the loss function L with respect to z, or ∂L ∂z (and leaving the rest of the computation as an exercise for the reader). By the chain rule:

∂L ∂z = ∂L ∂a[2] (6.41)
∂a[2] ∂z
因此我们先计算 ∂a[2] ，对式 6.37 求导，该式重写如下：

> So let’s first compute ∂a[2] , taking the derivative of Eq. 6.37, repeated here:

> ∂L

h i
LCE(a[2],y) = − yloga[2] +(1−y)log(1−a[2])
! !

∂L y∂log(a[2]) +(1−y)∂log(1−a[2])∂a[2] = − ∂a[2] ∂a[2]
 y 1  1 
= − +(1−y) 1−a[2] (−1)
a[2]
 y a[2] + y−1 (6.42)
= − 1−a[2]
接下来，根据 sigmoid 函数的导数：

> Next, by the derivative of the sigmoid:

∂a[2] = a[2](1−a[2])∂z
最后，我们可以使用链式法则：

> Finally, we can use the chain rule:

∂L ∂L ∂a[2]∂z = ∂a[2] ∂z
 y a[2] + y−1 a[2](1−a[2])
= − 1−a[2]= a[2] −y (6.43)
继续反向计算梯度（接下来让梯度经过 b[2] 1 和两个乘积节点，依此类推，一直回到所有蓝绿色的节点），这一步留给读者作为练习。

> Continuing the backward computation of the gradients (next by passing the gradients over b[2] 1 and the two product nodes, and so on, back to all the teal nodes), is left as an exercise for the reader.

### 6.6.5 关于学习的更多细节

> 6.6.5 More details on learning

神经网络中的优化是一个非凸优化问题，比逻辑回归的优化更为复杂；出于这一原因以及其他原因，要想成功学习有许多最佳实践。

> Optimization in neural networks is a non-convex optimization problem, more complex than for logistic regression, and for that and other reasons there are many best practices for successful learning.

对于逻辑回归，我们可以让所有权重和

> For logistic regression we can initialize gradient descent with all the weights and
偏置都取值为 0，以此初始化梯度下降。相比之下，在神经网络中，我们需要用小随机数来初始化权重。把输入值归一化为均值为 0、方差为单位方差，也很有帮助。

> biases having the value 0. In neural networks, by contrast, we need to initialize the weights with small random numbers. It’s also helpful to normalize the input values to have 0 mean and unit variance.

人们使用各种形式的正则化来防止过拟合。其中最重要的

> Various forms of regularization are used to prevent overfitting. One of the most
一种就是 dropout：在训练期间随机地丢弃网络中的一些单元及其连接

> important is dropout: randomly dropping some units and their connections from

> `dropout`
>
> 释义：训练时按概率随机把部分单元的输出置零并对其余输出重新归一化的正则化手段，用于抑制过拟合。

（Hinton 等 2012，Srivastava 等 2014）。在训练的每次迭代中（即每当我们更新参数时；如果使用小批量梯度下降，就是每个小批量），我们选定一个概率 p，对每个单元以概率 p 把它的输出替换为零（并对该层其余的输出重新归一化）。因此概率 p 是该算法的一个超参数。

> the network during training (Hinton et al. 2012, Srivastava et al. 2014). At each iteration of training (whenever we update parameters, i.e. each mini-batch if we are using mini-batch gradient descent), we choose a probability p and for each unit we replace its output with zero with probability p (and renormalize the rest of the outputs from that layer). Thus probability p is a hyperparameter of the algorithm.

这类超参数的调优同样重要。神经网络的

> Tuning of such hyperparameters is also important. The parameters of a neural

> `hyperparameter`（超参数）
>
> 释义：由算法设计者选定、在开发集上调优而非由梯度下降学到的量，如学习率、小批量大小、层数与激活函数等。

参数是权重 W 和偏置 b；它们通过梯度下降学习得到。

> network are the weights W and biases b; those are learned by gradient descent.

超参数是由算法设计者选择的量；其最优值是在开发集上调优得到的，而不是通过在训练集上用梯度下降学习得到的。超参数包括学习率 η、小批量大小、模型架构（层数、每层的隐藏节点数、激活函数的选择）、如何正则化等。梯度下降本身也有许多架构变体，例如 Adam（Kingma 和 Ba，2015）。

> The hyperparameters are things that are chosen by the algorithm designer; optimal values are tuned on a devset rather than by gradient descent learning on the training set. Hyperparameters include the learning rate η, the mini-batch size, the model architecture (the number of layers, the number of hidden nodes per layer, the choice of activation functions), how to regularize, and so on. Gradient descent itself also has many architectural variants such as Adam (Kingma and Ba, 2015).

最后，大多数现代神经网络都是借助计算图形式来构建的，这种形式使得在基于向量的 GPU（图形处理单元）上进行梯度计算和并行化既容易又自然。PyTorch（Paszke 等，2017）和 TensorFlow（Abadi 等，2015）是其中最流行的两个。有兴趣的读者可以查阅神经网络教科书以了解进一步的细节；本章末尾给出了一些建议。

> Finally, most modern neural networks are built using computation graph formalisms that make it easy and natural to do gradient computation and parallelization on vector-based GPUs (Graphic Processing Units). PyTorch (Paszke et al., 2017) and TensorFlow (Abadi et al., 2015) are two of the most popular. The interested reader should consult a neural network textbook for further details; some suggestions are at the end of the chapter.

## 6.7 小结

> 6.7 Summary

- 神经网络由神经单元构成。神经网络最初受生物神经元启发，如今它已是一种抽象的计算装置，而非生物模型。
- 每个神经单元把输入值乘以一个权重向量，加上偏置，然后应用非线性激活函数，如 sigmoid 函数、tanh 函数或修正线性单元。
- 在全连接前馈网络中，第 i 层的每个单元都与第 i+1 层的每个单元相连，并且不存在环路。
- 神经网络的能力来自较早的层能够学习到可供网络中较晚的层利用的表示。
- 神经网络通过梯度下降等优化算法进行训练。
- 误差反向传播，即计算图上的反向微分，用于计算一个网络损失函数的梯度。
- 神经语言模型使用神经网络作为概率分类器，在给定前 n 个词的条件下计算下一个词的概率。
- 神经语言模型可以使用预训练的嵌入，也可以在语言建模的过程中从零开始学习嵌入。

> Neural networks are built out of neural units. Originally inspired by biological neurons, neural networks are now an abstract computational device rather than a biological model.
> Each neural unit multiplies input values by a weight vector, adds a bias, and then applies a non-linear activation function like sigmoid, tanh, or rectified linear unit.
> In a fully-connected, feedforward network, each unit in layer i is connected to each unit in layer i+1, and there are no cycles.
> The power of neural networks comes from the ability of early layers to learn representations that can be utilized by later layers in the network.
> Neural networks are trained by optimization algorithms like gradient descent.
> Error backpropagation, backward differentiation on a computation graph, is used to compute the gradients of the loss function for a network.
> Neural language models use a neural network as a probabilistic classifier, to compute the probability of the next word given the previous n words.
> Neural language models can use pretrained embeddings, or can learn embeddings from scratch in the process of language modeling.

## 历史注记

> Historical Notes

神经网络的起源可追溯到 20 世纪 40 年代的 McCulloch-Pitts 神经元（McCulloch 和 Pitts，1943），它把生物神经元简化为一种可用命题逻辑来描述的计算元件。到 20 世纪 50 年代末和 60 年代初，若干实验室（包括康奈尔大学的 Frank Rosenblatt 和斯坦福大学的 Bernard Widrow）开展了神经网络研究；这一阶段促成了感知机的发展（Rosenblatt，1958），以及把阈值转换为偏置——这一记法我们至今仍在沿用（Widrow 和 Hoff，1960）。

> The origins of neural networks lie in the 1940s McCulloch-Pitts neuron (McCulloch and Pitts, 1943), a simplified model of the biological neuron as a kind of computing element that could be described in terms of propositional logic. By the late 1950s and early 1960s, a number of labs (including Frank Rosenblatt at Cornell and Bernard Widrow at Stanford) developed research into neural networks; this phase saw the development of the perceptron (Rosenblatt, 1958), and the transformation of the threshold into a bias, a notation we still use (Widrow and Hoff, 1960).

在人们证明单个感知机

> The field of neural networks declined after it was shown that a single perceptron
单元无法建模像 XOR 这样简单的函数之后，神经网络领域便衰落了（Minsky 和 Papert，1969）。

> unit was unable to model functions as simple as XOR (Minsky and Papert, 1969).

在接下来的二十年里虽然仍有少量工作继续，但该领域的重大复兴直到 20 世纪 80 年代才到来，当时像误差反向传播这样用于构建更深网络的实用工具开始普及（Rumelhart 等，1986）。20 世纪 80 年代发展出了各种各样的神经网络及相关架构，尤其是在心理学和认知科学的应用中（Rumelhart 和 McClelland 1986b，McClelland 和 Elman 1986，Rumelhart 和 McClelland 1986a，Elman 1990），当时人们常用连接主义或并行分布式处理这一说法（Feldman 和 Ballard 1982，Smolensky 1988）。这一时期发展出的许多原理和技术都是现代工作的基础，包括分布式表示（Hinton，1986）、循环网络（Elman，1990）以及用张量实现组合性（Smolensky，1990）等思想。

> While some small amount of work continued during the next two decades, a major revival for the field didn’t come until the 1980s, when practical tools for building deeper networks like error backpropagation became widespread (Rumelhart et al., 1986). During the 1980s a wide variety of neural network and related architectures were developed, particularly for applications in psychology and cognitive science (Rumelhart and McClelland 1986b, McClelland and Elman 1986, Rumelhart and McClelland 1986a, Elman 1990), for which the term connectionist or parallel distributed processing was often used (Feldman and Ballard 1982, Smolensky 1988). Many of the principles and techniques developed in this period are foundational to modern work, including the ideas of distributed representations (Hinton, 1986), recurrent networks (Elman, 1990), and the use of tensors for compositionality(Smolensky, 1990).

> `connectionist`（连接主义）
>
> 释义：20 世纪 80 年代对以大量简单单元的分布式计算来建模认知这一取向的称呼，也称并行分布式处理。

到 20 世纪 90 年代，规模更大的神经网络也开始应用于许多实际的语言处理任务，例如手写识别（LeCun 等 1989）和语音识别（Morgan 和 Bourlard 1990）。到 21 世纪初，计算机硬件的改进以及优化与训练技术的进步使得训练更大、更深的网络成为可能，由此产生了深度学习这一现代术语（Hinton 等 2006，Bengio 等 2007）。我们将在第 14 章和第 16 章介绍更多相关历史。

> By the 1990s larger neural networks began to be applied to many practical language processing tasks as well, like handwriting recognition (LeCun et al. 1989) and speech recognition (Morgan and Bourlard 1990). By the early 2000s, improvements in computer hardware and advances in optimization and training techniques made it possible to train even larger and deeper networks, leading to the modern term deep learning (Hinton et al. 2006, Bengio et al. 2007). We cover more related history in Chapter 14 and Chapter 16.

关于神经网络有许多优秀的著作，包括 Goodfellow

> There are a number of excellent books on neural networks, including Goodfellow
等（2016）与 Nielsen（2015）。

> et al. (2016) and Nielsen (2015).
