# 自定义Executor类

本文档用于介绍如何在`TrafficDL`下开发一个新的executor。

对于一个新的模型，如果训练方法复杂，而现有的执行器不能用于训练和评估，那么我们就需要开发一个新的执行器。

## 创建新的Executor类

首先，我们创建的新executor应该继承自`AbstractExecutoror`。

例如，我们想为交通状态预测任务开发一个名为`NewExecutor`的执行器，并将代码写入`libtraffic/executor/`目录下的`newexecutor.py`。

```python
from libtraffic.executor.abstract_executor import AbstractExecutor

class NewExecutor(AbstractExecutor):
    def __init__(self, config, model):
        self.evaluator = get_evaluator(config)
        pass
```

## 重写对应的方法

用于训练模型的函数是`train()`，它将调用`_train_epoch()`来训练模型。

用来评估模型的函数是`evaluate()`，它将调用`_valid_epoch()`来评估该模型。

剩下的两个接口`load_model()`和`save_model()`分别用来加载和保存模型。

如果开发的模型需要更复杂的训练或评估方法，那么你可以重写上述接口。

```python
from libtraffic.executor.abstract_executor import AbstractExecutor

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