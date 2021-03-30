# Evaluation Introduction

我们实现了若干种评估损失函数，以使得同一任务下的不同的模型可以在同样的标准下进行比较。

## Evaluation Metrics

- MSE
- MAE
- RMSE
- MAPE
- MARE
- SMARE
- ACC
- top-k
- Recall
- Precision
- MAP
- AUC
- LogLoss

## Evaluation Settings

记录评估模块涉及到的相关参数

spilt_ratio：

数据集分割比例，默认为`[0.8, 0.1, 0.1]`。

