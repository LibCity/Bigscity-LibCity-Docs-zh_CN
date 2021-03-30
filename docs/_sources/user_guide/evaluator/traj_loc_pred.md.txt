# Trajectory Location Prediction Evaluator

## Evaluation Metrics

对于轨迹下一跳预测任务，本评估器实现了一系列基于 TopK 的评估指标：

* Precision@K
* Recall@K
* F1-score@K
* MRR@K
* MAP@K
* NDCG@K

可以通过在用户自定义 Config 文件中加入 `metrics` 与 `topk` 两个参数，来控制本评估器使用哪些评估方法。

## Evaluation Settings

* `metrics (list of string)`: 默认值为 `["Recall"]`。可选参数为 `["Precision", "Recall", "F1", "MRR", "MAP", "NDCG"]`。
* `topk (int)`: 默认值为 `1`。

