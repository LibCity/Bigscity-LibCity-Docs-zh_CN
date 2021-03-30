Traffic State Prediction Evaluator
==================================

我们实现了若干种评估损失函数，以使得同一任务下的不同的模型可以在同样的标准下进行比较。

Evaluation Metrics
------------------

对于交通状态预测任务，本评估器实现了一系列评估指标：

=================== ================================= ====================================================================================
评估指标            评估指标(英文)                    公式
=================== ================================= ====================================================================================
平均绝对误差        MAE(Mean Absolute Error)          .. math:: MAE=\frac{1}{n}\sum_{i=1}^n|\hat{y_{i}}-y_i|
均方误差            MSE(Mean Squared Error)           .. math:: MSE=\frac{1}{n}\sum_{i=1}^n(\hat{y_{i}}-y_i)^2
均方根误差          RMSE(Rooted Mean Squared Error)   .. math:: RMSE=\sqrt{\frac{1}{n}\sum_{i=1}^n(\hat{y_{i}}-y_i)^2}
平均绝对百分比误差  MAPE(Mean Absolute Percent Error) .. math:: MAPE=\frac{1}{n}\sum_{i=1}^n|\frac{\hat{y_{i}}-y_i}{y_i}|*100\%
决定系数            R2(Coefficient of Determination)  .. math:: R^2=1-\frac{\sum_{i=1}^n(y_i-\hat{y_i})^2}{\sum_{i=1}^n(y_i-\bar{y})^2}
可释方差值          EVAR(Explained variance score)    .. math:: EVAR =1-\frac{Var(y_i-\hat{y_i})}{Var(y_i)}
=================== ================================= ====================================================================================

其中，真实值为\ :math:`y=\{y_1,y_2,...,y_n\}`\ ，预测值为\ :math:`\hat{y} = \{\hat{y_1}, \hat{y_2}, ..., \hat{y_n}\}`\ ，\ :math:`n`\ 为样本个数，均值\ :math:`\bar{y}=\frac{1}{n}\sum_{i=1}^ny_i`\ ，方差\ :math:`Var(y_i)=\frac{1}{n}\sum_{i=1}^n(y_{i}-\bar{y})^2`\ 。

Evaluation Settings
-------------------

下面是评估器所涉及到的一系列参数：

位置：trafficdl/config/evaluator/TrafficStateEvaluator.json

- ``metrics``\ ：指定评价指标数组，评估类的\ ``allowed_metrics``\ 表示该任务可以接受的指标类型，不能超出此范围。

- ``mode``\ ：评估模式，状态预测一般是多个时间步的预测，若设置为\ ``average``\ 表示计算前n个时间步平均的结果，设置成\ ``single``\ 则计算单独第n个时间步的评估结果。\ **目前的评估函数会返回所有时间步的结果**\ 。默认\ ``average``\ 。例如，总时间步长为3，则\ ``average``\ 模式返回[前1个时间步平均的loss，前2个时间步平均的loss，前3个步平均的loss]，\ ``single``\ 模式返回[第1个时间步的loss，第2个时间步的loss，第3个时间步的loss]。