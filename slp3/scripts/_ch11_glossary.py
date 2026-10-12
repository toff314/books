"""把第 11 章统一术语表写入每个 chunk 的 glossary 字段（跨分片强制一致）。

约定沿用 _ch09_glossary.py：同一术语在全章只用同一译名；
专名（人名/系统名/数据集名）保留原文。
"""
import glob
import json

GLOSSARY = {
    # —— 检索基础 ——
    "information retrieval": "信息检索",
    "IR": "信息检索",
    "ad hoc retrieval": "即席检索",
    "retrieval": "检索",
    "retriever": "检索器",
    "document": "文档",
    "query": "查询",
    "collection": "文档集合",
    "corpus": "语料库",
    "search engine": "搜索引擎",
    "web search": "网络搜索",
    "web search term": "网络搜索词",
    "ranked retrieval": "排序检索",
    "rank": "排名",
    "ranking": "排序",
    "relevance": "相关性",
    "relevant": "相关的",
    "landmark": "地标",
    # —— 向量空间模型 ——
    "vector space model": "向量空间模型",
    "bag of words": "词袋",
    "bag-of-words": "词袋",
    "term-document matrix": "词项-文档矩阵",
    "document vector": "文档向量",
    "query vector": "查询向量",
    "count vector": "计数向量",
    "sparse vector": "稀疏向量",
    "dense vector": "稠密向量",
    "term": "词项",
    "term weight": "词项权重",
    "term weighting": "词项加权",
    "term frequency": "词频",
    "vocabulary": "词表",
    "dimension": "维度",
    "dot product": "点积",
    "cosine": "余弦",
    "similarity": "相似度",
    "normalization": "归一化",
    # —— 加权与索引 ——
    "tf-idf": "tf-idf",
    "BM25": "BM25",
    "Okapi": "Okapi",
    "document frequency": "文档频率",
    "inverse document frequency": "逆文档频率",
    "idf": "idf",
    "df": "df",
    "stop list": "停用词表",
    "stop word": "停用词",
    "stopword": "停用词",
    "inverted index": "倒排索引",
    "postings": "倒排记录",
    "postings list": "倒排列表",
    "index": "索引",
    # —— 评测 ——
    "precision": "精确率",
    "recall": "召回率",
    "precision-recall curve": "精确率-召回率曲线",
    "interpolated precision": "插值精确率",
    "average precision": "平均精确率",
    "mean average precision": "平均精确率均值",
    "MAP": "MAP",
    "F1": "F1",
    "exact match": "精确匹配",
    "gold": "标准答案",
    "ground truth": "标准答案",
    # —— 稠密检索 ——
    "dense retrieval": "稠密检索",
    "sparse retrieval": "稀疏检索",
    "embedding": "嵌入",
    "token": "词元",
    "encoder": "编码器",
    "decoder": "解码器",
    "bi-encoder": "双编码器",
    "cross-encoder": "交叉编码器",
    "dual encoder": "双编码器",
    "passage": "段落",
    "chunk": "文本块",
    "late interaction": "后期交互",
    "MaxSim": "MaxSim",
    "ColBERT": "ColBERT",
    "Faiss": "Faiss",
    "ANN": "近似最近邻",
    "attention": "注意力",
    "self-attention": "自注意力",
    "fine-tuning": "微调",
    "pretraining": "预训练",
    "pre-training": "预训练",
    "softmax": "softmax",
    "logits": "logits",
    # —— RAG ——
    "retrieval-augmented generation": "检索增强生成",
    "RAG": "RAG",
    "generator": "生成器",
    "reader": "阅读器",
    "hallucination": "幻觉",
    "hallucinate": "产生幻觉",
    "calibrated": "经过校准的",
    "factoid questions": "事实型问题",
    "knowledge citations": "知识引证",
    "open book": "开卷",
    "closed book": "闭卷",
    "reading comprehension": "阅读理解",
    "question answering": "问答",
    "QA": "问答",
    "open-domain QA": "开放域问答",
    "prompt": "提示",
    "LLM": "大语言模型",
    "LLMs": "大语言模型",
    "large language model": "大语言模型",
    "language model": "语言模型",
    "in-context learning": "上下文学习",
    "zero-shot": "零样本",
    "few-shot": "少样本",
    # —— 专名（保留原文）——
    "BERT": "BERT",
    "CLS": "CLS",
    "[SEP]": "[SEP]",
    "Natural Questions": "Natural Questions",
    "MS MARCO": "MS MARCO",
    "TyDi QA": "TyDi QA",
    "MMLU": "MMLU",
    "LUNAR": "LUNAR",
    "Jeopardy!": "Jeopardy!",
    "Wikipedia": "维基百科",
    "Shakespeare": "莎士比亚",
    "Khattab": "Khattab",
    "Zaharia": "Zaharia",
    "Karpukhin": "Karpukhin",
    "Rajpurkar": "Rajpurkar",
    "et al.": "等",
}


def main() -> None:
    files = sorted(glob.glob("build/11-retrieval-based-models/chunks/*.json"))
    for f in files:
        with open(f, encoding="utf-8") as fh:
            c = json.load(fh)
        c["glossary"] = GLOSSARY
        with open(f, "w", encoding="utf-8") as fh:
            json.dump(c, fh, ensure_ascii=False, indent=1)
        print(f"{f}: glossary={len(c['glossary'])} items={len(c['items'])}")


if __name__ == "__main__":
    main()
