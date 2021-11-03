交通轨迹预测评估模块
======================

评估指标
--------

对于轨迹下一跳预测任务，本评估器实现了一系列基于 TopK 的评估指标。

评估指标公式符号表

| 符号      | 含义                                                       |
| --------- | ---------------------------------------------------------- |
| $$N$$       | 测试集的大小                                               |
| $i$       | 第 $i$ 条测试数据                                          |
| $K$       | 取置信度前 $K$ 个预测输出进行评估                          |
| $T(i)$    | 第 $i$ 条测试数据中的真实下一跳位置                        |
| $R(i)$    | 模型对于第 $i$ 条测试数据预测结果中置信度前 $K$ 的位置集合 |
| $Hit(i)$  | 第 $i$ 条测试数据中预测命中的位置集合，即 $T(i) \cap R(i)$ |
| $Rank(i)$ | 第 $i$ 条测试数据中的 $T(i)$ 在 $R(i)$ 中的排名            |
| $|*|$     | 集合的取模运算符                                           |

使用上述符号，TopK 评估指标的计算公式为：

| 指标               | 公式                                                         |
| ------------------ | ------------------------------------------------------------ |
| 精准率             | $Precision@K=\frac{\sum_{i=1}^{N}|\operatorname{Hit}(i)|}{N \times K}$ |
| 召回率             | $Recall@K=\frac{\sum_{i=1}^{N}|\operatorname{Hit}(i)|}{N}$   |
| F1 分数            | $F 1 @ K=\frac{2 \times \text { Precision@ } \times \text { Recall@ } K}{\text { Precision } @+\text { Recall@ } K}$ |
| 平均倒数排名       | $M R R @ K=\frac{1}{N} \sum_{i=1}^{N} \frac{1}{\operatorname{Rank}(i)}$ |
| 归一化折损累计增益 | $NDCG@K=\frac{1}{N} \sum_{i=1}^{N} \frac{1}{\log _{2}(\operatorname{rank}(i)+1)}$ |

可以通过在用户自定义 Config 文件中加入 ``metrics`` 与 ``topk`` 两个参数，来控制本评估器使用哪些评估方法。

评估设置
--------

下面是评估器所涉及到的一系列参数：

位置：libcity/config/evaluator/TrajLocPredEvaluator.json

* ``metrics (list of string)``: 默认值为 ``["Recall"]``。可选参数为 ``["Precision", "Recall", "F1", "MRR", "MAP", "NDCG"]``。

* ``topk (int)``: 默认值为 ``1``。

