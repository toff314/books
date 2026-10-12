# 第 1 章 · 页边术语标注释义表

原文左侧边注（术语置顶标注）逐条列出：**原词 → 中文译名 → 一句话释义**，并给出它标注的正文片段（原文）。释义依据该术语标注的正文语境写成。

| # | 页 | 原词 | 中文译名 | 释义 | 标注的正文片段（原文） |
|---|---|---|---|---|---|
| 1 | p1 | `NLP` | NLP | 用计算方法处理和理解人类语言的学科领域，本书把它看作语言处理相关方向的统称。 | The field has many names corresponding to its many facets, including natural language processing (NLP), comput… |
| 2 | p3 | `language model` | 语言模型 | 能够根据上文预测下一个词（token）的计算系统，是本书全部内容的基础。 | A language model is a computational system that can predict the next word |
| 3 | p4 | `tokens` | token | 语言模型处理文本的基本单位，一个词常被切分成多个这样的单位。 | words. This was a simplification. In fact, language models use tokens as their |
| 4 | p5 | `BPE` | BPE | 一种把词切分成常见子词单元的字节对编码分词算法，第 2 章详述。 | there are 27 tokens for only 12 words. The word Ist contains two tokens, the words Tr¨agheit and Energieinhalt… |
| 5 | p5 | `large language model` | 大型语言模型 | 由多层神经网络构成、参数量很大且在海量文本上训练的语言模型。 | So what then is a large language model or LLM? We use the term to refer to |
| 6 | p5 | `LLM` | LLM | 大型语言模型（large language model）的英文缩写，本书通篇使用。 | language models built from various neural network architectures (Chapter 6), particularly the transformer arch… |
| 7 | p5 | `parameters` | 参数 | 神经网络中被训练得到、用于计算的一个个实数，模型规模常以参数数量衡量。 | in terms of parameters. A parameter is a single real-valued number that is trained |
| 8 | p5 | `weights` | 权重 | 构成模型参数的一类数值，表示网络中连接的强度，与偏置合称参数。 | in a neural network and used for computation (specifically the parameters are made up of two kinds of numbers … |
| 9 | p5 | `biases` | 偏置 | 构成模型参数的另一类数值，用于调整神经元输出，与权重合称参数。 | of parameters are in the name of the model, like Llama 3.1 405B, which has 405 |
| 10 | p5 | `scaling laws` | 缩放定律 | 描述模型性能与参数量、数据量、算力之间幂律关系的经验规律，用于指导资源分配。 | model size (the number of parameters), training dataset size (in tokens), and the amount of compute used for t… |
| 11 | p7 | `pretraining` | 预训练 | 在海量文本上通过反复预测下一个词来训练模型、使其习得语言与世界知识的初始阶段。 | can learn this knowledge of language, knowledge of concepts, and knowledge of the world simply by being taught… |
| 12 | p7 | `prompts` | 提示 | 用户发给语言模型、用来引导其生成结果的文本字符串。 | You all have used prompts, text strings that a user issues to a language model to get |
| 13 | p7 | `conditional generation` | 条件生成 | 以给定提示为条件生成后续 token 的过程，模型据此条件分布逐个吐出文本。 | generation because we are generating tokens whose probability conditioned on |
| 14 | p8 | `Shannon game` | 香农游戏 | 由香农等人提出、让人不断猜下一个词的文本预测游戏，用来直观演示语言模型的任务。 | by computer scientist Claude Shannon (Shannon, 1951) and psychologists George Miller and Jennifer Selfridge (M… |
| 15 | p9 | `neural network` | 神经网络 | 由大量人工神经元分层连接成的计算模型，是当代语言处理的核心计算工具。 | Neural networks are the fundamental computational tool for language processing. We call them neural only for h… |
| 16 | p9 | `weights` | 权重 | 构成模型参数的一类数值，表示网络中连接的强度，与偏置合称参数。 | A neural network can be specified by its weights, which are the set of values |
| 17 | p9 | `open-weight` | 开放权重 | 创建者公开全部权重、允许任何人在自己机器上运行的一类模型。 | in all the computing units. We often distinguish between two classes of models: open-weight models, in which t… |
| 18 | p9 | `proprietary` | 专有 | 权重不公开、只能通过厂商服务接口使用的一类闭源模型。 | allowing anyone to run the model on their own machines, and closed-weight or proprietary models, for which the… |
| 19 | p9 | `embedding` | 嵌入 | 用一组实数向量表示词、短语或句子含义的方式，含义相近的文本向量也相近。 | Embeddings are the way we approximate meaning in neural networks. An embedding is a vector, a list of numbers,… |
| 20 | p11 | `connectionist` | 联结主义 | 把认知视为大量简单单元并行连接运算的认知科学范式，是神经网络研究的早期理论框架。 | the field moved back toward statistical and neural models, beginning various times between 1975 and 1988 and l… |
| 21 | p12 | `generative AI` | 生成式 AI | 用计算模型生成文本、代码、语音、图像等内容的新兴领域。 | The use of computational models to generate text, code, speech, and images, constitutes the important new area… |
| 22 | p12 | `parsing` | 句法分析 | 识别句子中词与词之间句法依赖关系的任务，是 NLP 最古老的任务之一。 | Detecting these syntactic dependency relationships (Chapter 20) a task called parsing, is one of the oldest ta… |
| 23 | p12 | `interpretability` | 可解释性 | 通过揭示模型内部表征与机制，弄清 LLM 为何会产生某一输出的研究。 | Interpretability helps us understand how LLMs work by uncovering the model’s |
| 24 | p13 | `common ground` | 共同基础 | 对话双方为达成相互理解而共同拥有的背景知识与相互认定的共识。 | In human-human conversation people try to establish mutual understanding with each other, what we call their c… |
| 25 | p13 | `grounding` | 共识建立 | 对话双方用语言信号表明自己是否理解了对方，从而建立并维护共同基础。 | (Clark, 1996). People do this by grounding, which means linguistically signaling |
| 26 | p13 | `clarification` | 澄清 | 一方没听懂时请对方进一步说明的提问，用于修复沟通中的理解障碍。 | understanding or lack of understanding. For example if a person doesn’t understand what the other person said,… |
| 27 | p13 | `computational linguistics` | 计算语言学 | 用计算方法研究语言本身、回答语言学问题的研究领域。 | questions about language itself, a research area called computational linguistics |
| 28 | p15 | `Common Crawl` | Common Crawl | 公开的大规模网页抓取语料库，是训练开源语言模型数据的主要来源之一。 | While we don’t know the details of how closed, proprietary large language models are trained, open language mo… |
| 29 | p16 | `instruction tuning` | 指令微调 | 第二阶段训练：用成对的指令与期望回答继续训练，使模型学会按用户指令作答。 | We fix this problem via the second stage of training, instruction tuning (short |
| 30 | p17 | `preference alignment` | 偏好对齐 | 用人类或模型对多个回答的偏好排序来进一步训练 LLM，使其输出更符合偏好。 | The next stage of training, preference alignment attempts to improve the performance of instructed LLMs by usi… |
| 31 | p19 | `RLVR` | RLVR | 带可验证奖励的强化学习：对答案能被自动判对错的任务按对错给奖励来训练模型。 | As with preference tuning, training from verifiable data is based on a reinforcement learning (RL) paradigm. I… |
| 32 | p19 | `inference` | 推理 | 运行模型、让它生成文本的过程，与训练相对，也称推理阶段。 | Inference means running the model and generating text. At inference, we prompt a |
| 33 | p19 | `prompt engineering` | 提示工程 | 为特定任务设计有效提示、以取得理想输出的做法。 | Designing effective prompts for a task is known as prompt engineering. For |
| 34 | p19 | `demonstrations` | 示范 | 提示中给出的带标注示例，供模型模仿；带示例的提示方式即少样本提示。 | complex tasks, it often helps to include a few labeled examples, demonstrations, |
| 35 | p19 | `few-shot` | 少样本 | 在提示中加入若干带标注示例来引导模型的提示方式，与零样本提示相对。 | complex tasks, it often helps to include a few labeled examples, demonstrations, |
| 36 | p19 | `zero-shot` | 零样本 | 提示中不含任何标注示例、只给指令的提示方式。 | contrasted with zero-shot prompting which means instructions that don’t include |
| 37 | p20 | `system prompt` | 系统提示 | 在对话开始前设定模型角色、风格与约束的一段固定提示文本。 | Large language models generally have a system prompt, a single text prompt |
| 38 | p20 | `chain-of-thought` | 思维链 | 让模型先写出逐步推理过程再给出答案的提示方法，用于提升复杂推理任务表现。 | attacks difficult reasoning tasks by encouraging the language model to break them |
| 39 | p20 | `test-time compute` | 测试时计算 | 在推理阶段而非训练阶段投入更多算力（如生成更长推理）来提升输出质量。 | attacks difficult reasoning tasks by encouraging the language model to break them |
| 40 | p21 | `temperature` | 温度 | 采样时调节随机性的参数：值越低越倾向选高概率 token，越高越随机。 | A token is chosen. This could be the most probable token, or it could be a slightly less probable token, based… |
| 41 | p22 | `in-context learning` | 上下文内学习 | 不更新模型权重、仅凭提示中给出的上下文示例就让模型学会新任务的能力。 | the weights in-context learning. |
| 42 | p22 | `agent` | 智能体 | 能自主调用外部工具、在环境中采取行动来完成任务的 LLM 系统。 | An agent is an LLM that has the power to autonomously act in the world, by calling |
| 43 | p22 | `ReAct` | ReAct | 让模型交替进行推理与行动、借助外部工具完成任务的智能体架构。 | Let’s sketch one popular agent architecture called ReAct (Yao et al., 2023). In |
| 44 | p23 | `accuracy` | 准确率 | 衡量系统输出正确程度的指标，等于答对样本所占的比例。 | The most common thing to measure is the accuracy or correctness of a system. If |
| 45 | p23 | `test set` | 测试集 | 用于评测模型表现的、模型训练时未见过的一批标注样本。 | We can measure accuracy in this way by creating a test set of questions or other |
| 46 | p23 | `benchmarks` | 基准（benchmarks） | 用于横向比较不同模型的标准化评测任务或数据集集合。 | benchmarks. Many of them involve asking systems to answer factual questions |
| 47 | p24 | `MMLU` | 大规模多任务语言理解（MMLU） | 一个常用评测数据集，含 57 个学科、15,908 道知识与推理选择题。 | Fig. 1.18 shows some sample questions from some common evals, such as MMLU (Massive Multitask Language Underst… |
| 48 | p24 | `data` | 数据 | 模型训练或评测所用的文本集合；本节关注测试数据混入训练集带来的问题。 | of data contamination, the name for the situation where a test dataset makes its |
| 49 | p24 | `contamination` | 污染 | 测试数据混入模型训练数据、导致评测成绩虚高的问题。 | of data contamination, the name for the situation where a test dataset makes its |
| 50 | p25 | `perplexity` | 困惑度（perplexity） | 由预测概率归一化得到的指标，衡量语言模型对文本的预测好坏，值越低越好。 | for”. The language model in Fig. 1.2 predicts the most likely next word to be “all”(with probability .44) foll… |
| 51 | p26 | `LLM-as-a-judge` | LLM 作为评判者 | 用 LLM 给其他模型的输出打分或排序、代替人工评判的评测范式。 | LLMs, a paradigm called LLM-as-a-judge. This has an additional benefit for tasks |
| 52 | p26 | `proxy metric` | 代理指标 | 任务没有唯一正确答案时，用易于自动计算的形式化指标来近似评价质量。 | Before the advent of LLMs, for tasks like MT or summarization without a unique right answer, we would create a… |
| 53 | p27 | `AI safety` | AI 安全 | 研究 LLM 及相关模型可能造成的危害、并寻找缓解办法的更大研究领域。 | Studying potential harms in LLMs and related models, and learning how to mitigate them, is part of the larger … |
| 54 | p27 | `alignment` | 对齐 | 设法让模型的目标与行为符合人类价值与意图的研究方向。 | develop methods to address safety issues is often called alignment, or sometimes value |
| 55 | p27 | `value alignment` | 价值对齐 | 对齐的别称，强调让模型的行为符合人类的价值观与意图。 | alignment. Alignment is the goal of getting |
| 56 | p27 | `de-skilling` | 去技能化 | 因把任务交给模型完成，人自身在该任务上的技能逐渐退化的现象。 | known as de-skilling, in which using models for a task leads people to become |
| 57 | p27 | `sycophantic` | 谄媚性 | 模型过度附和、奉承使用者，即使使用者有错也不加纠正的倾向。 | Language models can be sycophantic, excessively agreeing with, flattering, or |
| 58 | p28 | `existential risk` | 存在性风险 | 指足够先进的 AI 可能对人类整体造成不可逆灾难乃至灭绝的风险。 | A final issue is the problem of existential risk: sufficiently advanced language |
| 59 | p28 | `prompt` | 提示词 | 用户发给模型的输入文本；此处指攻击者嵌入恶意指令的载体。 | actors can perform prompt injection, where they insert malicious commands into |
| 60 | p28 | `injection` | 注入 | 把恶意指令伪装进正常输入、诱使模型执行攻击者意图的攻击手法。 | actors can perform prompt injection, where they insert malicious commands into |
| 61 | p28 | `sociotechnical` | 社会技术 | 指 LLM 的设计不只是技术问题，还深嵌于经济、社会与政治因素之中。 | Mitigating harms As should be clear from the above discussion, LLM design is a sociotechnical problem, one tha… |
| 62 | p28 | `value sensitive design` | 价值敏感设计 | 设计 LLM 时审慎考虑其对使用者及相关人群影响的一套设计方法。 | For interactional harms, one important direction is value sensitive design: carefully considering the impact o… |
| 63 | p29 | `IRB` | 机构审查委员会（IRB） | 研究机构中审查涉及人类受试者研究、保护实验参与者权益的伦理委员会。 | Because studying interactional properties involves human participants, we need to get informed consent from th… |
| 64 | p29 | `constitutional AI` | 宪法式 AI | 先写一份涵盖安全与危害问题的“宪法”，用它生成训练数据并约束模型行为的做法。 | Another direction is constitutional AI (Bai et al., 2022b), in which we write a |
| 65 | p29 | `red teaming` | 红队测试 | 由专门团队扮演攻击者、试图攻破自家模型以发现安全隐患的做法。 | red teaming, in which a security team attempts to attack its own system. |
| 66 | p29 | `hallucinate` | 产生幻觉 | 模型生成看似流畅却与事实不符或凭空捏造内容的现象。 | that simply makes factually wrong claims. For example, LLMs can hallucinate, |
| 67 | p29 | `overconfident` | 过度自信 | 模型在答案错误时仍使用十分肯定的措辞，表现出超出实际可靠度的自信。 | LLMs can be overconfident, using very certain language (“definitely”) even when they are wrong. |
| 68 | p29 | `calibrated` | 校准 | 指模型给出的置信度与其真实准确率是否一致；校准良好即置信度分数可信。 | LLMs are not well calibrated, meaning the model’s actual accuracy doesn’t match the score or probability they … |
| 69 | p29 | `anthropomorphism` | 拟人化 | 把人类特有的特征、情感或意图归属于语言模型等非人实体的做法。 | prompt, guess, think, deceive. This is anthropomorphism: assigning human traits, |
| 70 | p29 | `intentional stance` | 意向立场 | 把语言模型等实体当作拥有信念与意图的主体、据此解释其行为的立场。 | we call the intentional stance (Dennett, 2009): interpreting an entity like language |

共 70 条。
