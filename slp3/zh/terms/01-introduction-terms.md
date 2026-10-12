# 第 1 章 · 页边术语标注对照表

原文左侧边注（术语置顶标注）逐条对齐：**原词 → 译名**，并给出它标注的正文片段（据原文）。

| # | 页 | 原词（原文边注） | 译名 | 标注的正文（原文） |
|---|---|---|---|---|
| 1 | p1 | `NLP` | NLP | The field has many names corresponding to its many facets, including natural lan |
| 2 | p3 | `language model` | 语言模型 | A language model is a computational system that can predict the next word |
| 3 | p4 | `tokens` | token | words. This was a simplification. In fact, language models use tokens as their |
| 4 | p5 | `BPE` | BPE | there are 27 tokens for only 12 words. The word Ist contains two tokens, the wor |
| 5 | p5 | `large language model` | 大型语言模型 | So what then is a large language model or LLM? We use the term to refer to |
| 6 | p5 | `LLM` | LLM | language models built from various neural network architectures (Chapter 6), par |
| 7 | p5 | `parameters` | 参数 | in terms of parameters. A parameter is a single real-valued number that is train |
| 8 | p5 | `weights` | 权重 | in a neural network and used for computation (specifically the parameters are ma |
| 9 | p5 | `biases` | 偏置 | of parameters are in the name of the model, like Llama 3.1 405B, which has 405 |
| 10 | p5 | `scaling laws` | 缩放定律 | model size (the number of parameters), training dataset size (in tokens), and th |
| 11 | p7 | `pretraining` | 预训练 | can learn this knowledge of language, knowledge of concepts, and knowledge of th |
| 12 | p7 | `prompts` | 提示 | You all have used prompts, text strings that a user issues to a language model t |
| 13 | p7 | `conditional generation` | 条件生成 | generation because we are generating tokens whose probability conditioned on |
| 14 | p8 | `Shannon game` | 香农游戏 | by computer scientist Claude Shannon (Shannon, 1951) and psychologists George Mi |
| 15 | p9 | `neural network` | 神经网络 | Neural networks are the fundamental computational tool for language processing.  |
| 16 | p9 | `weights` | 权重 | A neural network can be specified by its weights, which are the set of values |
| 17 | p9 | `open-weight` | 开放权重 | in all the computing units. We often distinguish between two classes of models:  |
| 18 | p9 | `proprietary` | 专有 | allowing anyone to run the model on their own machines, and closed-weight or pro |
| 19 | p9 | `embedding` | 嵌入 | Embeddings are the way we approximate meaning in neural networks. An embedding i |
| 20 | p11 | `connectionist` | 联结主义 | the field moved back toward statistical and neural models, beginning various tim |
| 21 | p12 | `generative AI` | 生成式 AI | — |
| 22 | p12 | `parsing` | 句法分析 | Detecting these syntactic dependency relationships (Chapter 20) a task called pa |
| 23 | p12 | `interpretability` | 可解释性 | Interpretability helps us understand how LLMs work by uncovering the model’s |
| 24 | p13 | `common` | 共同 | language models and users. Let’s consider a third kind of linguistic structure r |
| 25 | p13 | `ground` | 基础 | language models and users. Let’s consider a third kind of linguistic structure r |
| 26 | p13 | `grounding` | 建立共识 | (Clark, 1996). People do this by grounding, which means linguistically signaling |
| 27 | p13 | `clarification` | 澄清 | understanding or lack of understanding. For example if a person doesn’t understa |
| 28 | p13 | `computational linguistics` | 计算语言学 | questions about language itself, a research area called computational linguistic |
| 29 | p15 | `common crawl` | common crawl | While we don’t know the details of how closed, proprietary large language models |
| 30 | p16 | `instruction tuning` | 指令微调 | We fix this problem via the second stage of training, instruction tuning (short |
| 31 | p17 | `preference alignment` | 偏好对齐 | The next stage of training, preference alignment attempts to improve the perform |
| 32 | p19 | `RLVR` | RLVR | As with preference tuning, training from verifiable data is based on a reinforce |
| 33 | p19 | `inference` | 推理 | Inference means running the model and generating text. At inference, we prompt a |
| 34 | p19 | `prompt` | 提示词 | model and conditionally generate text. |
| 35 | p19 | `engineering demonstrations few-shot` | 工程、示范、少样本 | complex tasks, it often helps to include a few labeled examples, demonstrations, |
| 36 | p19 | `zero-shot` | 零样本 | contrasted with zero-shot prompting which means instructions that don’t include |
| 37 | p20 | `system prompt` | 系统提示 | Large language models generally have a system prompt, a single text prompt |
| 38 | p20 | `test-time` | 测试时 | Prompts can also be used in more sophisticated ways in a method called testtime  |
| 39 | p20 | `chain-of- compute` | 思维链 计算 | Prompts can also be used in more sophisticated ways in a method called testtime  |
| 40 | p20 | `thought` | 思维 | attacks difficult reasoning tasks by encouraging the language model to break the |
| 41 | p21 | `temperature` | 温度 | Each token becomes an embedding. Each of these indices (27, 17360, and so on) is |
| 42 | p22 | `in-context learning` | 上下文内学习 | the weights in-context learning. |
| 43 | p22 | `agent` | 智能体 | An agent is an LLM that has the power to autonomously act in the world, by calli |
| 44 | p22 | `ReAct` | ReAct | Let’s sketch one popular agent architecture called ReAct (Yao et al., 2023). In |
| 45 | p23 | `accuracy` | 准确率 | The most common thing to measure is the accuracy or correctness of a system. If |
| 46 | p23 | `test set` | 测试集 | We can measure accuracy in this way by creating a test set of questions or other |
| 47 | p23 | `benchmarks` | 基准（benchmarks） | benchmarks. Many of them involve asking systems to answer factual questions |
| 48 | p24 | `MMLU` | MMLU | — |
| 49 | p24 | `data` | 数据 | Evaluating LLMs via public benchmarks like these can suffer from the problem |
| 50 | p24 | `contamination` | 污染 | of data contamination, the name for the situation where a test dataset makes its |
| 51 | p25 | `perplexity` | 困惑度（perplexity） | for”. The language model in Fig. 1.2 predicts the most likely next word to be “a |
| 52 | p26 | `LLM-as-a- judge` | LLM 作为评判者 | LLMs, a paradigm called LLM-as-a-judge. This has an additional benefit for tasks |
| 53 | p26 | `proxy metric` | 代理指标 | Before the advent of LLMs, for tasks like MT or summarization without a unique r |
| 54 | p27 | `AI safety` | AI 安全 | Studying potential harms in LLMs and related models, and learning how to mitigat |
| 55 | p27 | `alignment` | 对齐 | develop methods to address safety issues is often called alignment, or sometimes |
| 56 | p27 | `value alignment` | 价值对齐 | alignment. Alignment is the goal of getting |
| 57 | p27 | `de-skilling` | 去技能化 | known as de-skilling, in which using models for a task leads people to become |
| 58 | p27 | `sycophantic` | 谄媚性 | Language models can be sycophantic, excessively agreeing with, flattering, or |
| 59 | p28 | `existential risk` | 存在性风险 | A final issue is the problem of existential risk: sufficiently advanced language |
| 60 | p28 | `prompt` | 提示词 | Many of these problems are exacerbated for LLM agents. For example malicious |
| 61 | p28 | `injection` | 注入 | actors can perform prompt injection, where they insert malicious commands into |
| 62 | p28 | `sociotechnical` | 社会技术 | Mitigating harms As should be clear from the above discussion, LLM design is a s |
| 63 | p28 | `value sensitive design` | 价值敏感设计 | — |
| 64 | p29 | `IRB` | IRB | — |
| 65 | p29 | `constitutional AI` | 宪法式 AI | Another direction is constitutional AI (Bai et al., 2022b), in which we write a |
| 66 | p29 | `red teaming` | 红队测试 | red teaming, in which a security team attempts to attack its own system. |
| 67 | p29 | `hallucinate` | 产生幻觉 | that simply makes factually wrong claims. For example, LLMs can hallucinate, |
| 68 | p29 | `overconfident calibrated` | 过度自信、校准 | LLMs can be overconfident, using very certain language (“definitely”) even |
| 69 | p29 | `anthropomor- phism` | 拟人化 | prompt, guess, think, deceive. This is anthropomorphism: assigning human traits, |
| 70 | p29 | `intentional stance` | 意向立场 | we call the intentional stance (Dennett, 2009): interpreting an entity like lang |

共 70 条。
