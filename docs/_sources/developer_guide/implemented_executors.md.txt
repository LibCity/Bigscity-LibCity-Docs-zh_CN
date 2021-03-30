# Customize Executors

本文档用于介绍如何在`TrafficDL`下开发一个新的调度器。我们已经为以下几个任务开发了标准的Executor：

- Traffic Location Prediction
- Traffic Flow Prediction
- Traffic Speed Prediction
- On-Demand Service predition
- Travel Time prediction
- Traffic Accident prediction

如果模型的训练方法比较复杂，而且已经存在的Executor不能满足要求时，我们需要开发一个新的Executor。

`AbstractExecutor`类是所有调度器的基类，实现时，请继承此类。（当然，如果你继承已经实现的几个标准Executor子类，并在其基础上进行扩展也可以。）

`AbstractExecutor`类用于训练模型的接口是`train()`。

`AbstractExecutor`类用于评估模型的接口是`evaluate()`。

而`load_model()`和`save_model()`两个接口则分别用于模型的加载和保存。

约定：

- `train()`内部调用`_train_epoch()` 去完成每一轮的训练。
- `evaluate()`内部调用`_valid_epoch()` 去完成每一轮的验证。
- 训练过程的checkpoint等文件使用`tmp/`目录。
- `load_model()`和`save_model()`两个接口的模型缓存使用`cache/model_cache`目录。
- 评估结果使用`cache/evaluate_cache`目录。
- 训练完成后应该保存验证集误差最小的模型参数，并用这个模型进行评估。

所以可以这样实现`newexecutor.py`：

```python
from trafficdl.executor.abstract_executor import AbstractExecutor

class NewExecutor(AbstractExecutor):
    def __init__(self, config, model):
        self.evaluator = get_evaluator(config)
        pass

    def save_model(self, cache_name):
        pass

    def load_model(self, cache_name):
        pass

    def evaluate(self, test_dataloader):
        pass

    def train(self, train_dataloader, eval_dataloader):
        pass
```

接下来，只需要重写全部的接口即可。