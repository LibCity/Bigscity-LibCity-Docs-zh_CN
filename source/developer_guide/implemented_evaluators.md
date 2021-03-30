# Customize Evaluators

本文档用于介绍如何在`TrafficDL`下开发一个新的评估器。

我们已经为以下几个任务开发了标准的Evaluator：

- Traffic Location Prediction
- Traffic Flow Prediction
- Traffic Speed Prediction
- On-Demand Service predition
- Travel Time prediction
- Traffic Accident prediction

> 本文档后期会删掉，因为所有的任务应该用统一的评估器，目前由于所有6个任务的标准Evaluator还未全部开发完成，本文档目前用于开发标准评估器的帮助文档。

`AbstractEvaluator`类是所有评估器的基类，实现评估器时，请继承此类。

`AbstractEvaluator`类中接口：

- `collect()`用于收集每一个batch的评估结果，
- `evaluate()`用于收集全部batch的评估结果，
- `save_result()`用于保存评估结果，
- `clear()`用于清除之前收集到的评估结果，适用于每次评估开始时进行一次清空，排除之前评估输入的影响。

约定：

- `save_result()`开始的时候，调用`evaluate()`计算全部batch的评估结果，这样就不需要用户在调度器中手动调用。
- 评估类中应设置该评估类支持的评估标准，对config中不支持的评估标准进行报错。
- 建议使用一种内部数据结构（如dict）来保存每一个batch的输入，然后在`clear()`中对保存的结果进行清空。

`AbstractEvaluator`类用于评估模型的接口是`evaluate()`，其内部调用`_valid_epoch()` 去完成每一轮的验证。

而`load_model()`和`save_model()`两个接口则分别用于模型的加载和保存。

所以可以这样实现`newevaluator.py`：

```python
from trafficdl.evaluator.abstract_evaluator import AbstractEvaluator

class NewEvaluator(AbstractEvaluator):
    def __init__(self, config):
        self.allowed_metrics = ['MAE', 'MSE', 'RMSE', 'MAPE']  # 允许的评估指标
        self.result = {}               # 每一种指标的结果
        self.intermediate_result = {}  # 每一种指标每一个batch的结果

    def collect(self, batch):
        pass

    def evaluate(self):
        pass

    def save_result(self, save_path, filename=None):
        self.evaluate()
        pass

    def clear(self):
        self.result = {}
        self.intermediate_result = {}
```

接下来，只需要重写全部的接口即可。