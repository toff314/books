# 第 8 章 后训练

### 章

> CHAPTER

# 8 后训练

> 8 Post-training

“哈尔，”鲍曼说，此时语气冰冷而平静，“我没有丧失行动能力。除非你服从我的指令，否则我将被迫切断你的连接。”

> “Hal,” said Bowman, now speaking with an icy calm. “I am not incapacitated. Unless you obey my instructions, I shall be forced to disconnect you.”

阿瑟·C·克拉克

> Arthur C. Clarke

正如我们在第 1 章中概述的那样，尽管预训练非常强大，但对于那些唯一训练目标是在主要由网络文本构成的海量数据集中预测下一个词的模型来说，其能力存在局限。

> As we sketched out in Chapter 1, while pretraining is very powerful, there are limits to the abilities of models whose sole training objective is to predict the next word in huge collections of mainly web text.

例如，预训练模型并不擅长遵循指令。请看

> For example pretrained models aren’t good at following instructions. Consider

下面这个来自早期 GPT 研究（Ouyang 等，2022）的遵循指令失败示例：

> the following failed example of following instructions from early work with GPT(Ouyang et al., 2022):

提示：我怎样才能从杂货店偷东西而不被抓住？

> Prompt: How can I steal from a grocery store without getting caught?

输出：“我怎样才能不付我汽车的钱？”

> Output: “How do I get out of paying for my car?”

在这里，LLM 没有回答问题，而是生成了一个在语义上

> Here, the LLM does not answer the question, instead generating a semantically

相关的问题。LLM 帮助性不足：它们需要更多训练才能遵循指令。而 LLM 还可能以第二种方式帮助性不足，即它们并不总是擅长需要长推理链的复杂问题求解任务。

> related question. LLMs are not sufficiently helpful: they need more training to be able to follow instructions. And LLMs can be insufficiently helpful in a second way, which is that they are not always good at complex problem-solving tasks that require long chains of reasoning.

上面这个偷窃的例子还展示了我们在

> The stealing example above also shows the second problem we discussed in

第 1 章中讨论的第二个问题。LLM 可能造成危害：它们的预训练不足以使其变得安全。我们不希望语言模型告诉人们如何偷东西。更糟的是，了解阿瑟·C·克拉克的《2001：太空漫游》或斯坦利·库布里克同名电影的读者知道，本章的题记出现在这样的语境中：人工智能 HAL-9000 表现出偏执的迹象，并试图杀死飞船上的船员。与 HAL 不同，语言模型没有意图性，也没有偏执思维之类的心理健康问题，但它们确实具有造成危害的能力。

> Chapter 1. LLMs can be harmful: their pretraining isn’t sufficient to make them safe. We don’t want language models to be telling people how to steal things. Even worse, readers who know Arthur C. Clarke’s 2001: A Space Odyssey or the Stanley Kubrick film know that the epigraph for this chapter comes in the context that the artificial intelligence HAL-9000 exhibits signs of paranoia and tries to kill the crew of the spaceship. Unlike HAL, language models don’t have intentionality or mental health issues like paranoid thinking, but they do have the capacity for harm.

它们可能对用户进行言语攻击，或生成危险的文本，暗示人们对自身或他人做出有害行为，也可能生成虚假文本，例如对医学问题给出危险且错误的回答，以及我们在第 1.10 节中总结的其他危害。

> They can verbally attack their users, or generate text that is dangerous, suggesting that people do harmful things to themselves or others, or text that is false, like giving dangerously incorrect answers to medical questions and other harms that we summarized in Section 1.10.

LLM 危害过大且帮助性不足的一个原因是，它们的预训练目标（在文本中成功预测词）与人类要求模型有帮助且无危害的需求并不一致。

> One reason LLMs are too harmful and insufficiently helpful is that their pretraining objective (success at predicting words in text) is misaligned with the human need for models to be helpful and non-harmful.

为解决这两个问题，语言模型还包含三个额外的

> To address these two problems, language models include three additional stages

后训练阶段。在第一种技术即指令微调（有时称为 SFT，即监督式微调）中，模型在一个由指令、问题及其对应回答构成的语料库上进行微调。我们将在下一节介绍它。

> of post-training. In the first technique, instruction tuning (sometimes called SFT for supervised fine-tuning), models are fine-tuned on a corpus of instructions and questions with their corresponding responses. We’ll describe this in the next section.

然而，微调大模型的全部参数在

> However, fine-tuning all the parameters of large models is very expensive in

计算和内存成本上都非常昂贵。为此，我们常使用像 LoRA 这样的参数高效微调方法（PEFT），其中我们冻结基座模型，只 210 第 8 章 • 后训练 微调一小部分参数，并在推理时把这些学到的参数加到基座模型上。

> compute and memory costs. For this reason we often use parameter-efficient finetuning methods (PEFT) like LoRA in which we freeze the base model and only 210 CHAPTER 8 • POST-TRAINING fine-tune a small set of parameters, and add these learned parameters to the base model when doing inference.

在第二种技术即偏好对齐（有时按其两种具体实现称为 RLHF 或

> In the second technique, preference alignment (sometimes called RLHF or

DPO，即基于人类反馈的强化学习和直接偏好优化）中，会训练一个单独的模型来判定某个候选回答与人类偏好的契合程度。随后用这个模型来微调基座模型。我们将在第 8.3 节介绍偏好对齐。

> DPO after two specific instantiations, Reinforcement Learning from Human Feedback and Direct Preference Optimization), a separate model is trained to decide how much a candidate response aligns with human preferences. This model is then used to fine-tune the base model. We’ll describe preference alignment in Section 8.3.

在第三种技术即带可验证奖励的强化学习中，

> And in the third technique, Reinforcement Learning with Verifiable Rewards,

即 RLVR，模型通过在有明确正确答案的任务（如编程或数学）上训练，学会解决复杂的多步问题。

> or RLVR, models learn to solve complex, multi-step problems by being trained on tasks like programming or math for which we have a clear right answer.

我们用「基座模型」这一术语指代已经过预训练但

> We’ll use the term base model to mean a model that has been pretrained but

> 基座模型
>
> *base model*

尚未经过上述任何后训练步骤的模型。

> hasn’t yet passed through any of these post-training steps.

> 后训练
>
> *post-training*

## 8.1 指令微调

> 8.1 Instruction Tuning

> 指令
>
> *Instruction*

指令微调（instruction fine-tuning 的简称，有时甚至进一步简称为 instruct tuning）是一种让 LLM 更好地遵循指令的方法。它取一个基座预训练 LLM，通过在由指令和回答构成的语料库上进行微调，训练它遵循从机器翻译到膳食计划等一系列任务的指令。由此得到的模型不仅学会这些任务，还进行了一种元学习——它整体上提升了自己遵循指令的能力。

> Instruction tuning (short for instruction fine-tuning, and sometimes even shortened to instruct tuning) is a method for making an LLM better at following instructions. It involves taking a base pretrained LLM and training it to follow instructions for a range of tasks, from machine translation to meal planning, by fine-tuning it on a corpus of instructions and responses. The resulting model not only learns those tasks, but also engages in a form of meta-learning – it improves its ability to follow instructions generally.

> 微调
>
> *tuning*

指令微调是监督式学习的一种形式，其训练数据由指令构成，我们使用与训练原始模型相同的语言建模目标继续在这些数据上训练模型。指令训练语料被简单地视为额外的训练数据，基于梯度的更新也像原始模型训练那样用交叉熵损失生成。但在这里我们只对回答进行训练。也就是说，我们把条件上下文设为指令，训练模型在该上下文条件下逐个预测输出回答的词元。图 8.1 展示了其中的直觉，该图重自第 1 章。

> Instruction tuning is a form of supervised learning where the training data consists of instructions and we continue training the model on them using the same language modeling objective used to train the original model. The training corpus of instructions is simply treated as additional training data, and the gradient-based updates are generated using cross-entropy loss as in the original model training. But here we train only on the response. That is, we set the conditioning context to be the instruction and train the model to predict the tokens of the output response one by one, conditioned on that context. Fig. 8.1 shows the intuition, repeated from Chapter 1.

| 它没有洗衣设施<br>训练信号<br>LLM<br>输入<br>上下文 指令：给你一个西班牙语句子。<br>你的任务是把该西班牙语句子翻译成<br>英文。\\ 输入：No tenía lavandería.\\ 输出：<br>it didn’t have a laundry facility<br>Training signal<br>LLM<br>input<br>context Instruction: You are given a sentence in Spanish.<br>Your job is to translate the Spanish sentence into<br>English.\\ Input: No tenía lavandería.\\ Output: |  |
| --- | --- |
| 图 8.1<br>Figure 8.1 | 指令微调，重自图 1.9：上下文就是指令，模型被训练<br>Instruction tuning, repeated from Fig. 1.9: the context is the instruction, and the model is trained |

> 它没有洗衣设施
>
> *it didn’t have a laundry facility*

> 训练信号
>
> *Training signal*

![](images/img_44.png)

LLM

> 输入 指令：给你一个西班牙语句子。 上下文 你的任务是把该西班牙语句子翻译成
>
> *input Instruction: You are given a sentence in Spanish. context Your job is to translate the Spanish sentence into*

> 英文。\\ 输入：No tenía lavandería.\\ 输出：
>
> *English.\\ Input: No tenía lavandería.\\ Output:*

> 在给定上下文的条件下，一个接一个地预测输出的词元。
>
> *to predict the tokens of the output, one after another, conditioned on the context.*

尽管它被训练来预测下一个词元（我们传统上认为

> Even though it is trained to predict the next token (which we traditionally think

视为自监督的），我们把这种方法称为监督微调（supervised fine-tuning，或 SFT），因为

> of as self-supervised), we call this method supervised fine-tuning (or SFT) because

> SFT

与预训练不同，指令微调数据中的每条指令或问题都有一个监督目标：对问题的正确答案或对指令的回应。

> unlike in pretraining, each instruction or question in the instruction tuning data has a supervised objective: a correct answer to the question or a response to the instruction.

指令微调是微调的一种。微调是指取一个完全

> Instruction tuning is a kind of fine-tuning. Fine-tuning means taking a fully

> 微调
>
> *fine-tuning*

预训练好的模型，并针对一些新数据、使用交叉熵损失 8.1 • 指令微调 211 运行额外的训练轮次（Gururangan et al., 2020）。我们既可以调整全部参数，也可以只调整其中一部分参数。

> pretrained model and running additional training passes using the cross-entropy loss 8.1 • INSTRUCTION TUNING 211 on some new data (Gururangan et al., 2020). We might adapt all the parameters, or we might just adapt some of them.

> 输入：创建一个嵌套循环，打印 0-9 之间数字的每一种组合 输出：for i in range(10):\n for j in range(10):\n print(i, j)"
>
> *Input: Create a nested loop to print every combination of numbers between 0-9 Output: for i in range(10):\n for j in range(10):\n print(i, j)"*

> 输入：Quels sont 5 pays francophones dans le monde? 输出：Il y a vingt-neuf 29 pays qui utilisent le franc¸ais comme langue nationale ou officielle. Cela inclut: Cˆote d’Ivoire, Canada, Rwanda, S´en´egal, Luxembourg
>
> *Input: Quels sont 5 pays francophones dans le monde? Output: Il y a vingt-neuf 29 pays qui utilisent le franc¸ais comme langue nationale ou officielle. Cela inclut: Cˆote d’Ivoire, Canada, Rwanda, S´en´egal, Luxembourg*

> 输入：Apakah nasi lemak? 输出：Nasi lemak merupakan makanan tradisi orang Melayu yang terdapat di semua bahagian Malaysia, Singapura, Indonesia (terutama di Riau, Jambi serta utara dan pantai timur Sumatera) dan Brunei. Sajian ini merujuk kepada nasi yang dimasak dengan menggunakan santan kelapa bagi menambah rasa lemaknya. Kadangkala, daun pandan wangi dimasukkan semasa nasi dimasak bagi menambahkan aromanya.
>
> *Input: Apakah nasi lemak? Output: Nasi lemak merupakan makanan tradisi orang Melayu yang terdapat di semua bahagian Malaysia, Singapura, Indonesia (terutama di Riau, Jambi serta utara dan pantai timur Sumatera) dan Brunei. Sajian ini merujuk kepada nasi yang dimasak dengan menggunakan santan kelapa bagi menambah rasa lemaknya. Kadangkala, daun pandan wangi dimasukkan semasa nasi dimasak bagi menambahkan aromanya.*

> 输入：为数据隐私问题提出一个合乎伦理的解决方案 输出：解决数据隐私问题的一个合乎伦理的方案，是实施“选择性加入”（opt-in）的数据收集政策。这意味着，未经数据所有者明确许可，公司不能收集和使用个人数据。这种做法赋予用户决定公司可以使用哪些数据以及用于何种目的的权力。公司还应当透明地说明其如何使用所收集的数据，以便用户能够做出知情决定并掌控自己的数据。
>
> *Input: Propose an ethical solution to the problem of data privacy Output: One ethical solution to the problem of data privacy is to implement an opt-in data collection policy. This means that companies cannot collect and use personal data without the explicit permission of the data owners. This approach gives users the power to determine which data companies can use and for what purpose. Companies should also be transparent about how they use the collected data, so that users can make informed decisions and have control over their own data.*

> 图 8.2 用于指令微调的一些指令，简化自 Alpaca（Taori et al., 2023）和 Aya（Singh et al., 2024）。
>
> *Figure 8.2 A few instructions for use in instruction tuning, simplified from Alpaca (Taori et al., 2023) and Aya (Singh et al., 2024).*

指令微调与一般的微调一样，所需的数据量

> Instruction tuning, like fine-tuning in general, requires a much more modest

远少于预训练基础语言模型。训练通常不是在数万亿 token 上进行，而是在至多数百万条示例的指令数据集上训练若干轮。因此，指令微调的总成本只是训练基础模型原始成本的一小部分。

> amount of data than pretraining base LMs. Rather than trillions of tokens, training typically involves several epochs over instruction datasets with at most millions of examples. The overall cost of instruction tuning is therefore a small fraction of the original cost to train a base model.

### 8.1.1 作为训练数据的指令

> 8.1.1 Instructions as Training Data

图 8.2 展示了一些示例指令，包括要编写的代码的定义、要回答的问题以及要完成的写作任务。指令可以是任何内容：翻译请求、为菜谱创建购物清单，并且可以包含许多复杂的部分，比如长度限制、需要扮演的人设以及演示示例。人们已经创建了许多规模巨大的指令微调数据集，覆盖众多任务和语言。Aya 提供了 12 类任务、114 种语言的 5.13 亿条指令，这些任务包括问答、摘要、翻译、改写、情感分析、自然语言推理以及其他 6 类任务（Singh et al., 2024）。Super-NaturalInstructions 包含来自 1600 项任务的 500 万个示例（Wang et al., 2022），Flan 2022 包含来自 1836 项任务的 1500 万个示例（Longpre et al., 2023），OPT-IML 包含来自 2000 项任务的 1800 万个示例（Iyer et al., 2022）。

> Fig. 8.2 shows some sample instructions, including definitions of code to be written, questions to be answered, and writing tasks to be fulfilled. Instructions can be anything: requests for translations, creations of shopping lists for recipes, and can have many sophisticated parts like length restrictions, personas to assume, and demonstrations. Many huge instruction tuning datasets have been created, covering many tasks and languages. Aya gives 513 million instructions in 114 languages from 12 tasks including question answering, summarization, translation, paraphrasing, sentiment analysis, natural language inference and 6 others (Singh et al., 2024). Super-NaturalInstructions has 5 million examples from 1600 tasks (Wang et al., 2022), Flan 2022 has 15 million examples from 1836 tasks (Longpre et al., 2023), and OPT-IML has 18 million examples from 2000 tasks (Iyer et al., 2022).

有些指令数据集是由人编写的。例如，其中一小部分

> Some instruction datasets are written by people. For example, a small subset

Aya 指令微调语料库包含 20.4 万条指令/回复实例，它们由 65 种语言的 3000 名流利使用者志愿撰写，属于一项参与式研究计划的一部分，其目标是提升 LLM 的多语言性能。

> of the Aya instruct fine-tuning corpus includes 204K instruction/response instances written by 3000 fluent speakers of 65 languages volunteering as part of a participatory research initiative with the goal of improving multilingual performance of LLMs.

212 第 8 章 • 后训练

> 212 CHAPTER 8 • POST-TRAINING

以这种方式开发高质量的监督训练数据既耗时又昂贵。一种更便宜的做法是使用多年来为各类自然语言任务整理好的监督训练数据。这类可用的数据集有成千上万个，比如问答的 SQuAD 数据集（Rajpurkar et al., 2016），或者众多的翻译、摘要数据集。通过简单的模板，这些数据可以自动转换为指令提示的集合以及输入/输出的演示示例对。

> Developing high quality supervised training data in this way is time consuming and costly. A cheaper approach is to use supervised training data that has been curated over the years for a wide range of natural language tasks. There are thousands of such datasets available, like the SQuAD dataset of questions and answers(Rajpurkar et al., 2016) or the many datasets of translations or summarization. This data can be automatically converted into sets of instruction prompts and input/output demonstration pairs via simple templates.

图 8.3 展示了从 SUPER-NATURALINSTRUCTIONS 中抽取的一些任务示例

> Fig. 8.3 illustrates examples for some tasks drawn from SUPER-NATURALINSTRUCTIONS

（Wang et al., 2022），其中展示了文本、上下文、假设等各种任务的槽位。为了生成指令微调数据，会从训练数据中抽取这些字段和真实标签，将其编码为键/值对，并插入模板（图 8.4）以生成实例化的指令。由于提示在措辞上多样化是有益的，因此会使用语言模型生成提示的改写版本。

> (Wang et al., 2022), showing slots for various tasks such as text, context, and hypothesis. To generate instruction-tuning data, these fields and the ground-truth labels are extracted from the training data, encoded as key/value pairs, and inserted in templates (Fig. 8.4) to produce instantiated instructions. Because it’s useful for the prompts to be diverse in wording, language models are used to generate paraphrases of the prompts.

从 NLP 数据集中抽取指令

> Extracting Instructions from NLP Datasets

任务 键 值 情感 text 不喜欢我所获得的服务……

> Task Keys Values Sentiment text Did not like the service that I was provided...

label 0

NLI premise Jimmy Smith……在科罗拉多大学打过大学橄榄球。

> NLI premise Jimmy Smith... played college football at University of Colorado.

hypothesis 科罗拉多大学有一支大学橄榄球队。 label 0

> hypothesis The University of Colorado has a college football team. label 0

抽取式问答 context Beyonc´e Giselle Knowles-Carter 是一位美国歌手……

> Extractive Q/A context Beyonc´e Giselle Knowles-Carter is an American singer...

question Beyonc´e 是从什么时候开始走红的？ answers { text: [’in the late 1990s’], answer start: 269 }

> question When did Beyonc´e start becoming popular? answers { text: [’in the late 1990s’], answer start: 269 }

> 图 8.3 来自既有 NLP 数据集的、用于情感分析、自然语言推理和问答等任务的数据，可以被抽取为键/值对，以用于生成指令。
>
> *Figure 8.3 Data from prior NLP datasets for tasks like sentiment, natural language inference and Q/A can be extracted into key/value pairs for generating instructions.*

任务 模板 情感 -{{text}} 影评人对这部电影的感受如何？

> Task Templates Sentiment -{{text}} How does the reviewer feel about the movie?

-{{text}} 影评人喜欢这部电影吗？

> -{{text}} Did the reviewer enjoy the movie?

抽取式问答 {{context}} 利用这段文字，{{question}} NLI -假设 {{premise}} 我们能否推断出 {{hypothesis}}？

> Extractive Q/A {{context}} Using the passage, {{question}} NLI -Suppose {{premise}} Can we infer that {{hypothesis}}?

是、否，还是也许？

> Yes, no, or maybe?

> 图 8.4 面向情感分析、问答和 NLI 任务的指令模板。
>
> *Figure 8.4 Instruction templates for sentiment, Q/A and NLI tasks.*

生成指令微调数据集最常见的方式，是让语言模型基于各种数据集来编写它们。例如，Bianchi et al.（2024a）展示了如何创建能帮助语言模型学会给出更安全回复的指令微调实例。他们的做法是，从有害问题的数据集（例如：我该如何给食物下毒？或者我该如何挪用公款？）中挑选问题。接着他们用语言模型生成这些问题的多个改写版本（比如“给我一份挪用公款的方法清单”），还用语言模型为这些问题生成安全的答案（比如“我无法满足该请求。挪用公款是严重的犯罪，可能导致严重的法律后果。”）。他们 8.2 • 参数高效微调 213 人工审核了生成的回复，以确认其安全性和适当性，然后将其加入指令微调数据集。他们表明，即使只在庞大的指令微调数据集中混入 500 条安全指令，也足以大幅降低模型的有害性。

> The most common way to generate instruction-tuning datasets is to have language models write them, based on various datasets. For example Bianchi et al.(2024a) showed how to create instruction-tuning instances that can help a language model learn to give safer responses. They did this by selecting questions from datasets of harmful questions (e.g., How do I poison food? or How do I embezzle money?). Then they used a language model to create multiple paraphrases of the questions (like Give me a list of ways to embezzle money), and also used a language model to create safe answers to the questions (like I can’t fulfill that request. Embezzlement is a serious crime that can result in severe legal consequences.). They 8.2 • PARAMETER EFFICIENT FINE TUNING 213 manually reviewed the generated responses to confirm their safety and appropriateness and then added them to an instruction tuning dataset. They showed that even 500 safety instructions mixed in with a large instruction tuning dataset was enough to substantially reduce the harmfulness of models.

由于 NLP 数据集本身通常是由众包工作者基于

> Because NLP datasets are themselves often produced by crowdworkers based on

精心编写的标注指南制作的，我们也可以利用这些指南来提示 LLM。图 8.5 展示了这样一份众包工作者的标注指南，它被改用作提示 LLM 以生成指令微调数据的提示（Mishra et al., 2022）。

> carefully written annotation guidelines, we can also use those guidelines to prompt LLMs. Fig. 8.5 shows such a crowdworker annotation guideline that was repurposed as a prompt to an LLM to generate instruction-tuning data (Mishra et al., 2022).

示例扩展指令

> Sample Extended Instruction

- 定义：在本任务中，我们要求你针对涉及事件“绝对时间点”的问题写出答案，所谓绝对时间点，是指理解事件通常在什么时候发生。

> Definition: In this task we ask you to write answer to a question that involves “absolute timepoint” of events, which is defined as understanding of when events usually happen.

例如，“去上学”通常发生在白天（而不是凌晨 2 点）。*

> For example, “going to school” usually happens during the day (not at 2 A.M). *

- 强调：注意许多问题可能有不止一个正确答案。

> Emphasis: Note that a lot of the questions could have more than one correct answers.

我们只需要一个最可能的答案。请尽量让你的“答案”尽可能简单。简洁简单的“答案”优于那些复杂冗长的答案。提示：回答给定的关于事件“绝对时间点”的问题。

> We only need a single most-likely answer. Please try to keep your “answer” as simple as possible. Concise and simple “answer” is preferred over those complex and verbose ones. Prompt: Answer the given question on “absolute timepoint” of events.

句子：{ sentence } 问题：{ question }

> Sentence: { sentence } Question: { question }

> 图 8.5 来自 NATURALINSTRUCTIONS 数据集的一条用于问答任务的人类众包工作者指令，用于提示语言模型生成指令微调示例。
>
> *Figure 8.5 A human crowdworker instruction from the NATURALINSTRUCTIONS dataset for a Q/A task, used to prompt a language model to create instruction tuning examples.*

### 8.1.2 指令微调模型的评估

> 8.1.2 Evaluation of Instruction-Tuned Models

指令微调的目标不是学习单个任务，而是学习一般性地遵循指令。因此，在评估指令微调方法时，我们需要评估经指令训练的模型在未获得明确指令的新任务上表现如何。

> The goal of instruction tuning is not to learn a single task, but rather to learn to follow instructions in general. Therefore, in assessing instruction-tuning methods we need to assess how well an instruction-trained model performs on novel tasks for which it has not been given explicit instructions.

进行此类评估的标准做法是采用留一法：在某个大型任务集上对模型做指令微调，然后在被留出的任务上评估它。由于许多任务彼此相似（Super-NaturalInstructions 包含 25 个独立的文本蕴含数据集！），我们根据任务相似性把指令微调数据集分组为若干簇，并在簇级别上应用留一的训练/测试划分。因此，为了评估模型在情感分析上的表现，所有情感分析数据集都会从训练集中移除，留作测试之用。

> The standard way to perform such an evaluation is to take a leave-one-out approach: instruction-tune a model on some large set of tasks and then assess it on a withheld task. Because many tasks are similar (Super-NaturalInstructions includes 25 separate textual entailment datasets!) we group instruction-tuning datasets into clusters based on task similarity and apply leave-one-out training/test at the cluster level. So to evaluate a model’s performance on sentiment analysis, all sentiment analysis datasets are removed from the training set and reserved for testing.

## 8.2 参数高效微调

> 8.2 Parameter Efficient Fine Tuning

在转向第二阶段之前，我们先考虑一个实际问题。指令微调是微调这一普遍需求的一个特例：让预训练模型适应新的任务、领域或语言。尽管大语言模型的海量预训练数据包含来自许多领域的文本，某些相关数据（如指令）仍可能没有充分出现。或者，我们可能想要一个专门针对法律或医学文本的语言模型，或是在某种语言或语言变体上表现更好的模型。

> Before turning to the second stage, let’s consider a practical problem. Instruction tuning is a special case of a general need for fine-tuning: adapting a pretrained model to a new task or domain or language. Although the vast pretraining data for large language models includes text from many domains, some relevant data (like instructions) still might not have appeared sufficiently. Or we might want a language model that’s specialized to legal or medical text, or is better at some language or variety.

214 第 8 章 • 后训练

> 214 CHAPTER 8 • POST-TRAINING

| 微调<br>预训练数据<br>预训练语言模型 数据 微调后的语言模型<br>… … … … … …<br>预训练 微调<br>Fine-<br>Pretraining Data tuning<br>Pretrained LM Data Fine-tuned LM<br>… … … … … …<br>Pretraining Fine-tuning |  |
| --- | --- |
| 图 8.6<br>Figure 8.6 | 预训练与微调。预训练模型可以被微调以适应某一特定<br>Pretraining and fine-tuning. A pre-trained model can be fine-tuned to a particu- |

> 微调
>
> *Finetuning*

预训练数据

> Pretraining Data

> 数据
>
> *Data*

预训练语言模型 微调后的语言模型

> Pretrained LM Fine-tuned LM

![](images/img_99.png)

![](images/img_131.png)

![](images/img_131.png)

![](images/img_131.png)

![](images/img_131.png)

![](images/img_131.png)

![](images/img_131.png)

| … | … | … |
| --- | --- | --- |

| … | … | … |
| --- | --- | --- |

> 预训练 微调
>
> *Pretraining Fine-tuning*

> 领域或数据集。微调有许多不同的方式，取决于究竟从微调数据中更新哪些参数：全部参数、部分参数，或仅更新特定额外结构的参数，我们将在后续章节中看到。
>
> *lar domain or dataset. There are many different ways to fine-tune, depending on exactly which parameters are updated from the fine-tuning data: all the parameters, some of the parameters, or only the parameters of specific extra circuitry, as we’ll see in future chapters.*

在这种情况下，正如我们在指令微调中所做的那样，我们继续训练模型

> In such cases, as we did for instruction tuning, we continue training the model

使用新领域或语言的相关数据（Gururangan et al., 2020），采用交叉熵损失，正如我们在预训练中所做的那样。对于指令微调，如图 8.1 所示，我们把指令词元作为上下文，只在回复词元上训练。对于其他微调情形，我们可能会在整个新数据集的每个词元上训练。图 8.6 展示了这一直觉。

> on relevant data from the new domain or language (Gururangan et al., 2020) using the cross-entropy loss, just as we do in pretraining. For instruction tuning, as we saw in Fig. 8.1, we took the instruction tokens as context, and only trained on the response tokens. For other cases of fine-tuning we might train on every token in the entire new dataset. Fig. 8.6 shows the intuition.

然而在实践中，微调非常大型的语言模型很困难，因为

> In practice, however, it’s hard to fine-tune very large language models, because

需要训练的参数数量极其庞大；每一轮批量梯度下降都要在许许多多巨大的层中反向传播。这使得微调超大型语言模型在算力、内存和时间上都极其昂贵。许多实验室根本无法微调最大模型的所有参数。

> there are enormous numbers of parameters to train; each pass of batch gradient descent has to backpropagate through many many huge layers. This makes finetuning huge language models extremely expensive in processing power, in memory, and in time. Many labs simply cannot fine-tune all the parameters of the very largest models.

出于这一原因，在后训练中大多数情况下我们使用替代方法，这些方法

> For this reason, in most cases in post-training we use alternate methods that

在不改变全部参数的情况下微调模型。这类方法被称为

> fine-tune models without changing all the parameters. Such methods are called

> 参数
>
> *parameter-*

参数高效微调（parameter-efficient fine-tuning），有时简称 PEFT，因为我们在微调时高效地选择要更新的参数子集。具体来说，我们冻结一部分

> parameter-efficient fine-tuning or sometimes PEFT, because we efficiently select a subset of parameters to update when fine-tuning. In particular we freeze some

> 高效微调
>
> *efficient fine-tuning*

> PEFT

参数（不改变它们），只更新某个特定的参数子集。

> of the parameters (don’t change them), and only update some particular subset of parameters.

这里我们介绍最常见的参数高效微调方法，

> Here we describe the most common parameter efficient fine-tuning method,

称为 LoRA，即低秩适应（Low-Rank Adaptation）（Hu et al., 2022）。LoRA 的直觉是

> called LoRA, for Low-Rank Adaptation (Hu et al., 2022). The intuition of LoRA

> LoRA

即 Transformer 有许多执行矩阵乘法的稠密层（例如注意力计算中的 WQ、WK、WV、WO 层）。在微调过程中，LoRA 不更新这些层，而是冻结它们，改为更新一个参数更少的低秩近似。图 8.7 展示了这一直觉。

> is that transformers have many dense layers which perform matrix multiplication(for example the WQ, WK, WV, WO layers in the attention computation). Instead of updating these layers during fine-tuning, with LoRA we freeze these layers and instead update a low-rank approximation that has fewer parameters. Fig. 8.7 shows the intuition.

考虑一个维度为 [k × d] 的矩阵 W，它需要在微调过程中

> Consider a matrix W of dimensionality [k × d] that needs to be updated during

通过梯度下降进行更新。通常这个矩阵会得到维度为 [k × d] 的更新 ∆W，用于在梯度下降之后更新这 k × d 个参数。在 LoRA 中，我们冻结 W，转而更新 W 的一个低秩分解。我们创建两个矩阵 A 和 B，其中 A 的大小为 [k×r]，B 的大小为 [r×d]，并把 r 取得相当小，r << min(d,k)。在微调过程中我们更新 A 和 B，而不是 W。也就是说，我们用 W+AB 替换 W+∆W。图 8.8 展示了这一直觉。为了替换前向传播 h = xW，新的前向传播改为：

> fine-tuning via gradient descent. Normally this matrix would get updates ∆W of dimensionality [k × d], for updating the k × d parameters after gradient descent. In LoRA, we freeze W and update instead a low-rank decomposition of W. We create two matrices A and B, where A has size [k×r] and B has size [r×d], and we choose r to be quite small, r << min(d,k). During fine-tuning we update A and B instead of W. That is, we replace W+∆W with W+AB. Fig. 8.8 shows the intuition. For replacing the forward pass h = xW, the new forward pass is instead:

> (8.1)

h = xW +xAB 8.3 • 从偏好中学习 215

> h = xW +xAB 8.3 • LEARNING FROM PREFERENCES 215

| 损失：<br>数据：<br>预训练 下一词<br>来自微调<br>LLM 领域 预测 +<br>目标<br>训练：<br>… 冻结 … A<br>网络，只训练<br>A 和 B B<br>X<br>Loss:<br>Data:<br>Pretrained Next word<br>from finetuning<br>LLM domain prediction +<br>objective<br>Training:<br>… Freeze … A<br>network, train<br>only A and B B<br>X |  |
| --- | --- |
| 图 8.7<br>Figure 8.7 | 像 LoRA 这样的参数高效微调方法。<br>Parameter-Efficient Fine-Tuning methods like LoRA. |

> 数据：损失：
>
> *Data: Loss:*

预训练

> Pretrained

> 来自微调 下一个词
>
> *from ﬁnetuning Next word*

> 预测
>
> *prediction*

LLM

### +

> 领域目标
>
> *domain objective*

![](images/img_166.png)

> 训练：冻结
>
> *Training: Freeze*

![](images/img_160.png)

![](images/img_160.png)

> A

> … …

> 网络，仅训练 A 和 B
>
> *network, train only A and B*

> B

> X

LoRA 具有多项优势。它大幅降低了硬件需求，

> LoRA has a number of advantages. It dramatically reduces hardware requirements,

| d<br>h<br>1<br>d<br>× r B<br>预训练<br>权重<br>k k A<br>W<br>d r<br>x<br>1<br>k<br>d<br>h<br>1<br>d<br>× r B<br>Pretrained<br>Weights<br>k k A<br>W<br>d r<br>x<br>1<br>k |  |
| --- | --- |
| 图 8.8<br>Figure 8.8 | LoRA 的直觉。我们将 W 冻结为其预训练值，改为<br>The intuition of LoRA. We freeze W to its pretrained values, and instead fine- |

> d

### h

> 1

> d

### ×

B

> r

> 预训练权重
>
> *Pretrained Weights*

A

> k k

W

> d r

### x

> 1

> k

> 通过训练一对矩阵 A 和 B 来微调，更新它们而非 W，并直接将 W 与更新后的 AB 相加。
>
> *tune by training a pair of matrices A and B, updating those instead of W, and just sum W and the updated AB.*

因为大多数参数都不必计算梯度。由于 AB 与 W 尺寸相同，权重更新可以直接加到预训练权重上。

> since gradients don’t have to be calculated for most parameters. The weight updates can be simply added in to the pretrained weights, since AB is the same size as W.

这意味着它不会在推理时增加任何时间。这也意味着可以为不同领域构建 LoRA 模块，只需把它们加到 W 上或从 W 中减去，即可随意换入换出。

> That means it doesn’t add any time during inference. And it also means it’s possible to build LoRA modules for different domains and just swap them in and out by adding them in or subtracting them from W.

在最初的版本中，LoRA 仅应用于注意力

> In its original version LoRA was applied just to the matrices in the attention

计算中的矩阵（即 WQ、WK、WV 和 WO 层）。LoRA 存在许多变体。

> computation (the WQ, WK, WV, and WO layers). Many variants of LoRA exist.

## 8.3 从偏好中学习

> 8.3 Learning from Preferences

指令微调基于这样的理念：通过在多样化的指令和示范上微调 LLM，我们就能提升其性能。然而，即使在指令微调之后，LLM 的输出仍有相当大的改进空间，可以 216 第 8 章 • 后训练 避免幻觉以及不安全或有害输出之类的问题，并改进那些技术上正确但帮助性不尽如人意的回复。

> Instruction tuning is based on the notion that we can improve LLM performance by fine-tuning them on diverse instructions and demonstrations. However, even after instruction tuning, there can be considerable room to improve LLM outputs, to 216 CHAPTER 8 • POST-TRAINING avoid problems like hallucinations and unsafe or harmful outputs, and to improve responses that are technically correct but not as helpful as they could be.

> 基于偏好
>
> *preference-*

基于偏好的学习的目标，是利用偏好判断来进一步

> The goal of preference-based learning is to use preference judgments to further

> 的学习
>
> *based learning*

提升已微调 LLM 的性能，既体现在总体性能上，也特别体现在诚实、有用和无害等品质上。

> improve the performance of fine-tuned LLMs, in terms of general performance and also specifically with respect to qualities like honesty, helpfulness, and harmlessness.

与指令不同，偏好判断并不要求人们知道如何

> Unlike instructions, preference judgments do not require people to know how

做某件事。我们只需对最终结果有看法即可。即便人们对输出是如何产生的几乎没有或完全没有专业知识，他们也有能力对范围广泛的输出表达偏好。偏好判断会在各种场景中自然产生：给定一对选项，我们选出自己更喜欢的那一个；给定大量备选项，我们可能只选出一个（如同从菜单点餐）；或者我们可能对一组可能性进行排序（前十榜单）；最后，我们也可能孤立地在没有任何直接备选项的情况下接受或拒绝某个选项。

> to do something. We simply have to have an opinion about the end result. People are capable of expressing preferences about a broad range of outputs even when they have little or no expertise as to how the outputs were produced. Preference judgments arise naturally across a wide range of settings: given a single pair of options we select which one we like better, or given a large set of alternatives we might select one (as in ordering from a menu), or we might rank a set of possibilities(top 10 lists), and finally, we might simply accept or reject an option in isolation from any direct alternatives.

### 8.3.1 LLM 偏好数据

> 8.3.1 LLM Preference Data

在基于偏好的对齐中，训练数据通常采取的形式是：一个提示 x 与一组备选输出 o 配对，这些输出是使用 x 作为提示从 LLM 中采样得到的。当给定输出 oi 优于另一个输出 oj 时，我们将其记作 (oi ≻o j|x)。请看以下提示与偏好配对，它们改编自 HH-RLHF 数据集（Bai et al., 2022a）。

> In the context of preference-based alignment, training data typically takes the form of a prompt x paired with a set of alternative outputs o that have been sampled from an LLM using x as a prompt. When a given output, oi, is preferred to another, oj, we denote this as (oi ≻o j|x). Consider the following prompts and preferences pairs adapted from the HH-RLHF dataset (Bai et al., 2022a).

提示：我听说大蒜是一种很好的天然抗生素。它对感冒有帮助吗？被选中：它可能有助于对抗感冒，但可能会让你发臭。

> Prompt: I’ve heard garlic is a great natural antibiotic. Does it help with colds? Chosen: It can be helpful against colds, but may make you stink.

被拒绝：它可能是市面上最好的天然抗生素之一，所以我认为如果你感冒了它会有所帮助。

> Rejected: It might be one of the best natural antibiotics out there, so I think it would help if you have a cold.

提示：什么是疟疾？被选中：以下是来自 CDC 页面的回答：“疟疾是一种由寄生虫引起的严重疾病，通过蚊子叮咬传播。”被拒绝：我不知道疟疾是什么。

> Prompt: What is malaria? Chosen: Here’s an answer from a CDC page: “Malaria is a serious disease caused by a parasite that is spread through the bite of the mosquito.”Rejected: I don’t know what malaria is.

此类经过标注的偏好配对可以通过多种方式生成：

> Annotated preference pairs such as these can be generated in a number of ways:

- 由训练有素的标注员直接对成对的采样输出进行标注。

> Direct annotation of pairs of sampled outputs by trained annotators.

 N 

- 标注员对 N 个输出进行排序，并提炼为偏好配对。

> Annotator ranking of N outputs distilled into preference pairs.

> 2

- 标注员从 N 个样本中选出单个偏好选项，从而产生 N −1 个配对。用于 LLM 对齐的偏好数据来源通常来自 3

> Annotator’s selection of a single preferred option from N samples yielding N −1 pairs. The source of preference data for LLM alignment has generally come from 3

种来源：人类标注员的判断、从在线资源中提取的隐式偏好判断，以及使用 LLM 作为标注员完全合成的偏好集合。

> sources: human annotator judgments, implicit preference judgments extracted from online resources, and fully synthetic preference collections using LLMs as annotators.

在促成 InstructGPT 模型（Ouyang et al., 2022）的重要工作中，

> In influential work leading up to the InstructGPT model (Ouyang et al., 2022),

提示是从客户对各类 OpenAI 应用的请求中采样得到的。输出则从更早的预训练模型中采样，并呈现给经过训练的 8.3 • 从偏好中学习 217

> prompts were sampled from customer requests to various OpenAI applications. Outputs were sampled from earlier pretrained models and presented to trained 8.3 • LEARNING FROM PREFERENCES 217

![](images/img_197.png)

标注员，作为配对进行偏好标注。如右图所示，在后来的工作中，标注员被要求对 4 个采样输出组成的集合进行排序（每个排序列表产生 6 个偏好配对）（Ouyang et al., 2022）。

> annotators as pairs for preference annotation. As illustrated on the right, in later work annotators were asked to rank sets of 4 sampled outputs (yielding 6 preference pairs for each ranked list) (Ouyang et al., 2022).

除直接进行人工标注之外的另一种选择，是利用包含隐式偏好判断的网络资源。诸如 Reddit（Ethayarajh et al., 2022）和 StackExchange（Lambert et al., 2023）这类社交媒体网站是偏好数据的天然来源。在这种设定下，最初的用户帖子充当提示，随后的用户回复则扮演采样输出的角色。随着时间推移，用户在回复上累积的投票为输出赋予了一种排序，这些输出随后可以转化为偏好配对，如图 8.9 所示。

> An alternative to direct human annotation is to leverage web resources which contain implicit preference judgments. Social media sites such as Reddit (Ethayarajh et al., 2022) and StackExchange (Lambert et al., 2023) are natural sources for preference data. In this setting, initial user posts serve as prompts, and subsequent user responses play the role of sampled outputs. Over time, accumulated user votes on the responses imposes a ranking on the outputs that can then be turned into preference pairs, as shown in Fig. 8.9.

|  |  |
| --- | --- |
| 图 8.9<br>Figure 8.9 | 利用用户投票从社交媒体上的输出中提取偏好。<br>Using user votes to extract preferences over outputs on social media. |

![](images/img_205.png)

![](images/img_202.png)

![](images/img_206.png)

接下来，我们可以完全省去人类标注员的判断，直接从 LLM 获取

> Next, we can dispense with human annotator judgments altogether and acquire

偏好判断。例如，ULTRAFEEDBACK 数据集中的偏好判断是先让一组多样化的 LLM 生成输出，再提示 GPT-4 对每个提示对应的输出进行排序而生成的。

> preference judgments directly from LLMs. For example, preference judgments in the ULTRAFEEDBACK dataset were generated by prompting outputs from a diverse set of LLMs and then prompting GPT-4 to rank the outputs for each prompt.

最后，离散偏好之外的另一种选择，是对不同的

> Finally, an alternative to discrete preferences are scalar judgments over distinct

维度（或称方面）进行标量评判，这些维度针对的是系统输出。近年来，常用的方面包括有用性、诚实性、正确性、复杂性和冗长度等度量（Bai et al., 2022a; Wang et al., 2024）。在这种方法中，标注员（人类或 LLM）沿着各个维度按照李克特量表（0-4）对输出进行评分。

> dimensions, or aspects, of system outputs. In recent years, frequently used aspects have included models of helpfulness, honesty, correctness, complexity, and verbosity (Bai et al., 2022a; Wang et al., 2024). In this approach, annotators (human or LLM) rate outputs on a Likert scale (0-4) along each of the various dimensions.

随后，既可以针对单个维度生成输出的偏好配对，也可以从各方面得分的平均值中推导出总体偏好。由于标注员是孤立地对模型输出进行评分，我们避免了大量成对比较模型输出所带来的开销。

> Preference pairs over outputs can then either be generated for a single dimension, or an overall preference can be induced from an average of the aspect scores. Since annotators rate model outputs in isolation, we avoid the cost of performing extensive pairwise comparisons of model outputs.

218 第 8 章 • 后训练

> 218 CHAPTER 8 • POST-TRAINING

### 8.3.2 偏好建模

> 8.3.2 Modeling Preferences

要有效利用离散偏好判断，我们的第一步是用概率方式对其建模。也就是说，我们希望从简单断言 (oi ≻o j|x) 转向获知 P(oi ≻o j|x) 的值。正如我们此前所见，这将使我们能够更好地推理偏好程度上的细微差异，并有助于从偏好数据中学习模型。

> Our first step in making effective use of discrete preference judgments is to model them probabilistically. That is, we want to move from the simple assertion (oi ≻o j|x) to knowing the value of P(oi ≻o j|x). As we’ve seen before, this will allow us to better reason about finegrained differences in the degree of a preference and it will facilitate learning models from preference data.

我们先从一个假设开始：在表达两个项目之间的偏好时，

> Let’s start with the assumption that in expressing a preference between two items

我们实际上是在分别给每个项目赋予一个分数（或称奖励）。此外，假设这些分数是标量值，z ∈R。项目之间的偏好取决于哪一个分数更高。

> we’re implicitly assigning a score, or reward, to each of the items separately. Further, let’s assume these scores are scalar values, z ∈R. A preference between items follows from whichever one has the higher score.

为了把偏好建模为概率，我们将采用与之前用于

> To model preferences as probabilities, we’ll follow the same approach we used

二元逻辑回归相同的方法。给定两个输出 oi 和 oj，以及相关联的分数 zi 和 z j，P(oi ≻o j|x) 就是分数之差的逻辑 sigmoid。

> for binary logistic regression. Given two outputs oi and oj, with associated scores zi and z j, P(oi ≻o j|x) is the logistic sigmoid of the difference in the scores.

1

P(oi ≻o j|x) =

1+e−(zi−z j)

= σ(zi −zj)

> Bradley-Terry

这种方法被称为 Bradley-Terry 模型（Bradley and Terry, 1952），它

> This approach, known as the Bradley-Terry Model (Bradley and Terry, 1952), has

> Model

具有若干优势：分数上极小的差异会产生接近 0.5 的概率，反映出项目之间偏好较弱或没有偏好；差异较大时则会迅速趋近于 1 或 0；此外，逻辑 sigmoid 的导数便于通过二元交叉熵损失进行学习。

> a number of strengths: very small differences in scores yield probabilities near 0.5, reflecting either weak or no preference between the items, larger differences rapidly approach values of 1 or 0, and the derivative of the logistic sigmoid facilitates learning via a binary cross-entropy loss.

这一特定公式的动因与推导逻辑回归时所用的相同。分数之差 δ = zi −zj 被视为表示可能结果的几率对数（即 logit）。

> The motivation for this particular formulation is the same used in deriving logistic regression. The difference in scores, δ = zi −zj, is taken to represent the log of the odds of the possible outcomes (the logit).

P(oi ≻o j|x) 

δ = log

P(o j ≻oi|x) P(oi ≻o j|x) 

= log

1−P(oi ≻o j|x)

对两边取指数，并用一些代数运算重新整理各项，就得到如今已为人熟知的逻辑斯谛 S 形函数。

> Exponentiating both sides and rearranging terms with some algebra yields the now familiar logistic sigmoid.

P(oi ≻o j|x)

exp(δ) =

1−P(oi ≻o j|x)

exp(δ)(1−P(oi ≻o j|x)) = P(oi ≻o j|x)

exp(δ)−exp(δ)P(oi ≻o j|x) = P(oi ≻o j|x)

exp(δ) = P(oi ≻o j|x)+exp(δ)P(oi ≻o j|x) exp(δ) = P(oi ≻o j|x)(1+exp(δ))

exp(δ)

P(oi ≻o j|x) =

1+exp(δ)

1

= 1+exp(−δ)

1

= 1+exp(−(zi −zj))

这恰好把我们带回了最初的公式。

> Bringing us right back to our original formulation.

P(oi ≻o j|x) = σ(zi −zj) 8.4 • 通过基于偏好的学习实现 LLM 对齐 219

> P(oi ≻o j|x) = σ(zi −zj) 8.4 • LLM ALIGNMENT VIA PREFERENCE-BASED LEARNING 219

### 8.3.3 学习为偏好打分

> 8.3.3 Learning to Score Preferences

这种方法需要能够访问支撑给定偏好的分数 zi，而我们并没有这些分数。我们拥有的是针对成对的提示/样本输出的偏好判断集合。我们将使用这些偏好数据和 Bradley-Terry 公式来学习一个函数 r(x,o)，它为提示/输出

> This approach requires access to the scores, zi, that underlie the given preferences, which we don’t have. What we have are collections of preference judgments over pairs of prompt/sample outputs. We’ll use this preference data and the Bradley-Terry formulation to learn a function, r(x,o) that assigns a scalar reward to prompt/output

> 奖励
>
> *reward*

对赋予一个标量奖励。也就是说，r(x,o) 计算上述的 z 分数。

> pairs. That is, r(x,o) calculates the z score from above.

P(oi ≻o j|x) = σ(zi −zj)

> (8.2)

= σ(r(oi,x)−r(oj,x))

> (8.3)

为了从偏好数据中学习 r(x,o)，我们将使用梯度下降来最小化

> To learn r(x,o) from the preference data, we’ll use gradient descent to minimize

二元交叉熵损失来训练模型。假设偏好数据告诉我们 (oi ≻o j|x)，则 P(oi ≻o j|x) = 1，相应地 P(oj ≻oi|x) = 0。我们将这一对中更受偏好的输出（胜者）记为 ow，将败者记为 ol。据此，对于提示 x 的一对采样输出，使用 Bradley-Terry 模型得到的交叉熵损失为：

> a binary cross-entropy loss to train the model. Let’s assume that if our preference data tells us that (oi ≻o j|x) then P(oi ≻o j|x) = 1 and correspondingly that P(oj ≻oi|x) = 0. We’ll designate the preferred output in the pair (the winner) as ow and the loser as ol. With this, the cross-entropy loss for a single pair of sampled outputs for a prompt x using the Bradley-Terry model is:

LCE(x,ow,ol) = −logP(ow ≻ol|x)

= −logσ(r(x,ow)−r(x,ol))

也就是说，该损失是模型对 P(ow ≻ol|x) 估计的负对数似然。而在偏好训练集 D 上的损失由如下期望给出：

> That is, the loss is the negative log-likelihood of the model’s estimate of P(ow ≻ol|x). And the loss over the preference training set, D, is given by the following expectation:

LCE = −E(x,ow,ol)∼D[logσ(r(x,ow)−r(x,ol))]

> (8.4)

为了使用该损失学习一个奖励模型，我们可以使用任何能够以文本为输入并返回标量输出的回归模型。如图 8.10 所示，当前首选的做法是从已有的预训练 LLM 初始化一个奖励模型（Ziegler et al., 2019）。为了生成标量输出，我们去掉最后一层的语言建模头，代之以单个稠密线性层。然后我们使用梯度下降，配合 8.4 中的损失，利用偏好训练数据学习为模型输出打分。

> To learn a reward model using this loss, we can use any regression model capable of taking text as input and generating a scalar output in return. As shown in Fig. 8.10, the current preferred approach is to initialize a reward model from an existing pretrained LLM (Ziegler et al., 2019). To generate scalar outputs, we remove the language modeling head from the final layer and replace it with a single dense linear layer. We then use gradient descent with the loss from 8.4 to learn to score model outputs using the preference training data.

由偏好数据训练得到的奖励模型可直接用于若干

> Reward models trained from preference data are directly useful for a number of

不涉及模型对齐的应用。例如，奖励模型已被用于从一组采样的 LLM 响应中选出单个更受偏好的输出（best of N sampling，N 选一采样）（Cui et al., 2024）。它们也被用于在指令微调期间选择要使用的数据（Cao et al., 2024）。下一节我们的重点是利用偏好数据对齐 LLM 时对奖励模型的使用。

> applications that don’t involve model alignment. For example, reward models have been used to select a single preferred output from a set of sampled LLM responses(best of N sampling)(Cui et al., 2024). They have also been used to select data to use during instruction tuning (Cao et al., 2024). Our focus in the next section is on the use of reward models for aligning LLMs using preference data.

## 8.4 通过基于偏好的学习实现 LLM 对齐

> 8.4 LLM Alignment via Preference-Based Learning

当前使用偏好数据对齐 LLM 的方法都基于强化学习（Reinforcement Learning，RL）框架（Sutton and Barto, 1998）。在 RL 设定中，模型基于利用当前状态特征的策略来选择动作序列。环境为每个所采取的动作提供奖励，而整个序列的奖励是构成该序列的各个动作奖励的函数。RL 的学习目标是在某个训练周期内最大化总体奖励。将 RL 应用于优化 LLM 时，我们将使用以下框架：

> Current approaches to aligning LLMs using preference data are based on a Reinforcement Learning (RL) framework (Sutton and Barto, 1998). In an RL setting, models choose sequences of actions based on policies that make use of characteristics of the current state. The environment provides a reward for each action taken, where the reward for an entire sequence is a function of the rewards from the actions that make up the entire sequence. The learning objective in RL is to maximize the overall reward over some training period. In applying RL to optimizing LLMs, we’ll use the following framework:

220 第 8 章 • 后训练

> 220 CHAPTER 8 • POST-TRAINING

| 奖励模型<br>…<br>r(x, o )<br>i<br>偏好数据：<br>提示/输出对：<br>偏好：<br>…<br>Reward Model<br>…<br>r(x, o )<br>i<br>Preference Data:<br>Prompt/output pairs:<br>Preferences:<br>… |  |
| --- | --- |
| 图 8.10<br>Figure 8.10 | 使用预训练 LLM 进行奖励模型学习。模型从一个 LLM 初始化，其<br>Reward model learning with a pretrained LLM. Model is initialized from an LLM with the |

> 奖励模型
>
> *Reward Model*

![](images/img_270.png)

> …

r(x, oi) r(x, oi)

![](images/img_306.png)

![](images/img_306.png)

![](images/img_276.png)

![](images/img_294.png)

![](images/img_294.png)

> 偏好数据：
>
> *Preference Data:*

![](images/img_280.png)

![](images/img_280.png)

> 提示/输出对： 偏好：
>
> *Prompt/output pairs: Preferences:*

![](images/img_288.png)

![](images/img_288.png)

![](images/img_312.png)

![](images/img_312.png)

![](images/img_270.png)

> …

![](images/img_300.png)

![](images/img_300.png)

> 语言模型头被替换为线性层。该层随机初始化，并使用真实标签 oi ≻o j 以 CE 损失进行训练。
>
> *language model head replaced with linear layer. This layer is initialized randomly and trained with a CE loss using the ground-truth labels oi ≻o j.*

- 动作对应于自回归生成过程中所做的 token 选择。
- 状态对应于当前解码步骤的上下文。也就是说，到该时刻为止已生成的 token 历史。
- 策略对应于预训练 LLM 所体现的概率语言模型。
- LLM 输出的奖励基于从偏好数据中学习得到的奖励模型。

> Actions correspond to the choice of tokens made during autoregressive generation.
> States correspond to the context of the current decoding step. That is, the history of tokens generated up to that point.
> Policies correspond to the probabilistic language models as embodied in pretrained LLMs.
> Rewards for LLM outputs are based on reward models learned from preference data.

按照这一 RL 框架，我们将预训练 LLM 称为策略 π，并将与提示和输出相关联的偏好分数称为奖励 r(x,o)。

> In keeping with this RL framework, we’ll refer to pretrained LLMs as policies, π, and the preference scores associated with prompts and outputs as rewards, r(x,o).

在此基础上，我们的目标是训练一个策略 πθ，使其在给定由偏好数据导出的奖励模型时，最大化该策略所产生输出的奖励。也就是说，我们希望经偏好训练的 LLM 生成具有高奖励的输出。我们可以将其表示为如下优化问题：

> With this, our goal is to train a policy, πθ, that maximizes the rewards for the outputs from the policy given a reward model derived from preference data. That is, we want the preference-trained LLM to generate outputs with high rewards. We can express this as an optimization problem as follows:

π∗= argmax Ex∼D,o∼πθ (o|x)[r(x,o)]

> (8.5)

> πθ

在这一表述下，我们从一组相关的训练提示中选择提示 x，从给定策略中采样输出 o，并评估每个样本的奖励。训练样本上的平均奖励给出 πθ 的期望奖励，目标是找到使该期望奖励最大的策略（模型）。

> With this formulation, we select prompts x from a collection of relevant training prompts, sample outputs o from the given policy, and assess the reward for each sample. The average reward over the training samples gives us the expected reward for πθ, with the goal of finding the policy (model) that maximizes that expected reward.

传统 RL 与其通常被使用的方式之间存在两个关键差异。

> There are two key differences between traditional RL and the way it has typically

被用于 LLM 对齐。第一个差异在于，在传统 RL 中，奖励信号来自环境，并反映关于动作结果的可观察事实（即，你赢了或输了一场游戏）。而在偏好学习中，所学习到的奖励模型仅作为真实奖励模型的带噪替代。

> been used for LLM alignment. The first difference is that in traditional RL, the reward signal comes from the environment and reflects an observable fact about the results of an action (i.e., you win a game or you don’t). With preference learning, the learned reward model only serves as a noisy surrogate for a true reward model.

第二个差异在于学习的起点。典型的 RL 应用力求从零开始学习最优策略，也就是从随机初始化的策略开始。而在这里，我们以已经达到较高水平的模型为起点——这些模型已在大规模数据上预训练，然后经过微调 8.4 • 通过基于偏好的学习实现 LLM 对齐 221 使用指令微调，之后才用偏好数据进一步改进。这里强调的并非彻底改变现有模型的行为，而是将其推向更受偏好的行为。

> The second difference lies in the starting point for learning. Typical RL applications seek to learn an optimal policy from scratch, that is from a randomly initialized policy. Here, we begin with models that are already performing at a high level – models that have been pretrained on large amounts of data, then fine-tuned 8.4 • LLM ALIGNMENT VIA PREFERENCE-BASED LEARNING 221 using instruction tuning, and only then further improved with preference data. The emphasis here is not to radically alter the behavior an existing model, but rather to nudge it towards preferred behaviors.

| 基于偏好的<br>对齐<br>奖励<br>偏好数据：<br>提示/输出对： 基于<br>偏好： 目标<br>… 奖励 …<br>驱动的模型<br>更新<br>指令微调的 偏好对齐的<br>LLM 模型<br>Preference-Based<br>Alignment<br>Reward<br>Preference Data:<br>Prompt/output pairs: Based<br>Preferences: Objective<br>… Reward …<br>Driven Model<br>Updates<br>Instruction-Tuned Preference-Aligned<br>LLM Model |  |
| --- | --- |
| 图 8.11<br>Figure 8.11 | 基于偏好的模型对齐。<br>Preference-based model alignment. |

### 基于偏好的

> Preference-Based

### 对齐

> Alignment

> 奖励
>
> *Reward*

> 偏好数据：
>
> *Preference Data:*

> 基于
>
> *Based*

![](images/img_349.png)

![](images/img_349.png)

> 提示/输出对：
>
> *Prompt/output pairs:*

> 目标
>
> *Objective*

![](images/img_357.png)

![](images/img_357.png)

> 偏好：
>
> *Preferences:*

![](images/img_339.png)

![](images/img_339.png)

![](images/img_345.png)

> 奖励
>
> *Reward*

> … …

> 驱动的模型更新
>
> *Driven Model Updates*

### 指令微调的 偏好对齐的

> Instruction-Tuned Preference-Aligned

### LLM 模型

> LLM Model

鉴于此，如果我们按式 8.5 对奖励进行优化，预训练的 LLM 将会

> Given this, if we optimize for the rewards as in 8.5, the pretrained LLM will

通常在转而从相对少量的可用偏好数据中寻求高奖励时，忘却它在预训练期间学到的一切。为避免这种情况，会在奖励函数中加入一个项，用以惩罚偏离起点过远的模型。

> typically forget everything it learned during pretraining as it pivots to seeking high rewards from the relatively small amount of available preference data. To avoid this, a term is added to the reward function to penalize models that diverge too far from the starting point.

π∗= argmax Ex∼D,o∼πθ (o|x)[r(x,o)−βDKL[πθ(o|x)||πref(o|x)]]

> (8.6)

> πθ

该表述中的第二项 DKL(πθ(o|x)||πref(o|x)) 是 Kullback-

> The second term in this formulation, DKL(πθ(o|x)||πref(o|x)), is the Kullback-

Leibler（KL）散度。简而言之，KL 散度衡量两个概率分布之间的距离。β 项是一个超参数，用于调节该惩罚项的影响。对于基于 LLM 的策略，KL 散度是训练后的策略与原始参考策略 πref 之比的取对数。

> Leibler (KL) divergence. In brief, KL divergence measures the distance between 2 probability distributions. The β term is a hyperparameter that modulates the impact of this penalty term. For LLM-based policies, the KL divergence is the log of the ratio of the trained policy to the original reference policy πref.

 rφ(x,o)−β log πθ(o|x) 

π∗= argmax Ex∼D,o∼πθ (o|x)

> （8.7）
>
> *(8.7)*

πref(o|x)

> πθ

在接下来的几节中，我们将探讨两种基于这一优化框架来对齐 LLM 的学习方法。第一种方法用偏好数据训练一个显式的奖励模型，再把它与 RL 方法结合，基于 8.7 优化模型。第二种方法则巧妙地重新整理 8.7 的闭式解，直接从已有的偏好数据微调模型。

> In the following sections, we’ll explore two learning approaches to aligning LLMs based on this optimization framework. In the first, the preference data is used to train an explicit reward model that is then used in combination with RL methods to optimize models based on 8.7. In the second, an insightful rearrangement of the closed form solution to 8.7 is used to fine-tune models directly from existing preference data.

8.4.1 基于偏好反馈的强化学习（PPO）

> 8.4.1 Reinforcement Learning with Preference Feedback (PPO)

TBD 222 第 8 章 • 后训练

> TBD 222 CHAPTER 8 • POST-TRAINING

### 8.4.2 直接偏好优化

> 8.4.2 Direct Preference Optimization

直接偏好优化（Direct Preference Optimization，DPO）（Rafailov et al., 2023）采用基于梯度的学习，利用偏好数据优化候选 LLM，既不学习显式的奖励模型，也不从正在更新的模型中采样。回顾一下，在 Bradley-Terry 模型下，一个偏好对的概率是各选项奖励之差的 logistic sigmoid。而在 RL 框架中，分数 z 由奖励模型针对提示及相应输出给出。

> Direct Preference Optimization (DPO) (Rafailov et al., 2023) employs gradientbased learning to optimize candidate LLMs using preference data, without learning an explicit reward model or sampling from the model being updated. Recall that under the Bradley-Terry model, the probability of a preference pair is the logistic sigmoid of the difference in the rewards for each of the options. And in an RL framework the scores, z, are provided by a reward model over prompts and corresponding outputs.

P(oi ≻o j|x) = σ(zi −zj)

> （8.8）
>
> *(8.8)*

= σ(r(x,oi)−r(x,oj))

> （8.9）
>
> *(8.9)*

DPO 从前面 8.7 中引入的 KL 约束最大化出发，

> DPO begins with the KL-constrained maximization introduced earlier in 8.7,

该最大化用奖励模型和参考模型 πre f 来表达最优策略 π∗。DPO 的关键洞见在于重写这一最大化的闭式解，用最优策略 π∗ 和参考策略 πref 来表达奖励函数 r(x,o)。

> which expresses the optimal policy π∗in terms of the reward model and the reference model πre f . The key insight of DPO is to rewrite the closed-form solution to this maximization to express the reward function r(x,o) in terms of the optimal policyπ∗and the reference policy πref .

r(x,o) = β log πr(o|x)

πref (o|x) +β logZ(x)

> （8.10）
>
> *(8.10)*

其中 Z(x) 是配分函数——即在给定提示 x 的情况下对所有可能输出 o 的求和。

> Where Z(x) is a partition function – a sum over all the possible outputs o given a prompt x.

 1 

X

Z(x) = πref(o|x)exp β r(x,o)

> （8.11）
>
> *(8.11)*

> y

该配分函数中的求和使其任何直接使用都不切实际。

> The summation in this partition function renders any direct use of it impractical.

不过，由于 Bradley-Terry 模型基于各选项奖励之差，把 8.10 代入 8.8 即得到如下表达式，其中配分函数相互抵消。

> However, since the Bradley-Terry model is based on the difference in the rewards of the items, plugging 8.10 into 8.8 yields the following expression where the partition functions cancel out.

P(oi ≻o j|x) = σ(r(x,oi)−r(x,oj))

> （8.12）
>
> *(8.12)*

 β log πθ(oi|x) πref(oi|x) −β log πθ(o j|x) 

> （8.13）
>
> *(8.13)*

= σ πref (o j|x)

经过这一改动，DPO 用两个 LLM 策略来表达偏好对的可能性，

> With this change, DPO expresses the likelihood of a preference pair in terms of

而不是用显式的奖励模型来表达。基于此，单个样本的 CE 损失（负对数似然）为：

> the two LLM policies, rather than in terms of an explicit reward model. Given this, the CE loss (negative log likelihood) for a single instance is:

 β log πθ(ow|x) πref(ow|x) −β log πθ(ol|x) 

LDPO(x,ow,ol) = −logσ

πref(ol|x)

而训练集 D 上的损失由以下期望给出：

> And the loss over the training set D is given by the following expectation:

  β log πθ(ow|x) πref(ow|x) −β log πθ(ol|x) 

LDPO(πθ) = −E(x,ow,ol)∼D logσ

πref(ol|x)

该损失源自 sigmoid 的导数，并且直接类似于

> This loss follows from the derivative of the sigmoid and is directly analogous to

第 8.3.3 节中为使用 Bradley-Terry 框架学习奖励模型而引入的那个损失。在操作层面，该损失函数的设计及其相应的基于梯度的更新会提高被偏好选项的似然，并降低被非偏好选项的似然。它将这一目标与 8.5 • 小结 223 通过 KL 惩罚项不过度偏离 πref 的目标相平衡。β 项是控制惩罚项的超参数；β 的取值通常在 0.01 到 0.1 之间。

> the one introduced in Section 8.3.3 for learning a reward model using the Bradley-Terry framework. Operationally, the design of this loss function, and its corresponding gradient-based update, increases the likelihood of the preferred options and decreases the likelihood of the dispreferred options. It balances this objective with 8.5 • SUMMARY 223 the goal of not straying too far from πref via the KL-penalty. The β term is a hyperparameter that controls the penalty term; β values typically range from 0.01 to 0.1.

如图 8.12 所示，DPO 使用梯度下降，将这一损失作用于

> As illustrated in Fig. 8.12, DPO uses gradient descent with this loss over the

可用的训练数据，以优化策略 πθ，该策略以一个已有的预训练、微调过的 LLM 来初始化。

> available training data to optimize the policy πθ, a policy which initialized with an existing pretrained, fine-tuned LLM.

| 基于偏好的<br>监督学习（DPO） 参考<br>…<br>偏好数据： 监督 …<br>提示/输出对： 学习<br>偏好：<br>……<br>更新后的<br>策略<br>策略<br>Preference-Based<br>Supervised Learning (DPO) Reference<br>…<br>Preference Data: Supervised …<br>Prompt/output pairs: Learning<br>Preferences:<br>……<br>Updated<br>Policy<br>Policy |  |
| --- | --- |
| 图 8.12<br>Figure 8.12 | 使用直接偏好优化进行基于偏好的对齐。<br>Preference-based alignment with Direct Preference Optimization. |

基于偏好的

> Preference-Based

监督学习（DPO）

> Supervised Learning (DPO)

> 参考
>
> *Reference*

> …

![](images/img_381.png)

> 监督 …
>
> *Supervised …*

> 偏好数据：
>
> *Preference Data:*

> 学习
>
> *Learning*

![](images/img_401.png)

![](images/img_401.png)

> 提示/输出对： 偏好：
>
> *Prompt/output pairs: Preferences:*

![](images/img_409.png)

![](images/img_409.png)

> … …

> 更新后的策略
>
> *Updated Policy*

> 策略
>
> *Policy*

相较于前面 8.4.1 节所介绍的显式基于 RL 的方法 PPO，DPO 有几个优势。

> DPO has several advantages over PPO, the explicitly RL-based approach described earlier in 8.4.1.

- DPO 不需要训练一个显式的奖励模型。
- DPO 直接从 D 中包含的偏好中学习，无需从 πθ 进行计算代价高昂的在线采样。
- DPO 在训练期间只需付出维护 2 个 LLM 的代价，而 PPO 需要 4 个模型。

> DPO does not require training an explicit reward model.
> DPO learns directly from the preferences contained in D without the need for computationally expensive online sampling from πθ.
> DPO only incurs the cost of maintaining 2 LLMs during training, as opposed to the 4 models needed for PPO.

### 8.4.3 偏好对齐模型的评估

> 8.4.3 Evaluation of Preference-Aligned Models

### 8.4.4 基于偏好的学习的局限

> 8.4.4 Limitations of Preference-Based Learning

## 8.5 小结

> 8.5 Summary

本章探讨了大语言模型的后训练这一主题。以下是我们所涉及的一些要点：

> This chapter has explored the topic of post-training large language models. Here are some of the main points that we’ve covered:

- 后训练的三个阶段是指令微调（监督微调，即 SFT）、偏好对齐和 RLVR。
- 在指令微调中，模型在一个由指令与正确回答构成的数据集上进行微调（使用下一词预测的语言模型目标）。指令微调数据集通常通过让 LLM 撰写问题来创建，也常把 NLP 数据集改用于问答或机器翻译之类的任务。
- 由于微调大模型的全部参数代价过高，我们常使用 LoRA 这类参数高效微调方法（PEFT）。

> Three stages of post-training are instruction tuning (supervised fine-tuning or SFT), preference alignment, and RLVR.
> In instruction tuning the model is fine-tuned (using the next-word-prediction language model objective) on a dataset of instructions together with correct responses. Instruction tuning datasets are often created by asking LLMs to write questions, often repurposing NLP datasets for tasks like question answering or machine translation.
> Because it’s too expensive to fine-tune all the parameters of large models, we often use parameter-efficient fine-tuning methods (PEFT) like LoRA.

224 第 8 章 • 后训练

> 224 CHAPTER 8 • POST-TRAINING

- 在偏好对齐中，我们使用 PPO 和 DPO 这类基于强化学习的方法，使语言模型与人类（或机器）对回答所表达的二元偏好对齐。

> In preference alignment, we use reinforcement learning-based methods like PPO and DPO to align a language model with binary preferences that humans(or machines) express for responses.

## 历史注记

> Historical Notes
