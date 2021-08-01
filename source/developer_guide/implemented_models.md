# 自定义Model

本文档用于介绍如何在`TrafficDL`下开发一个新模型。

## 创建新的Model类

首先，我们创建的新的模型应该继承`AbstractModel`或`AbstractTrafficStateModel`。注意，对于交通状态预测任务，请继承` AbstractTrafficStateModel`类，对于轨迹位置预测任务，请继承`AbstractModel`类。

这里我们以交通状态预测任务为例。我们想为交通速度预测任务开发一个名为`NewModel`的模型。

首先请在`libtraffic/model/traffic_speed_prediction/`目录下创建一个新的文件`NewModel.py`，并在该文件中写入以下代码。

```python
from libtraffic.model.abstract_traffic_state_model import AbstractTrafficStateModel

class NewModel(AbstractTrafficStateModel):
    def __init__(self, config, data_feature):
        pass
    
    def predict(self, batch):
        pass
    
    def calculate_loss(self, batch):
        pass
```

## 实现\_\_init\_\_()

然后我们需要实现`__init__()`方法，`__init__()`用于根据数据特征和配置信息来定义模型结构。

`__init__()`的输入参数是`config`和`data_feature`，其中`config`包含各种配置信息，包括模型参数等，`data_feature`包含建立我们模型的数据集的特征。

这里我们以一个简单的LSTM交通预测模型为例.你可以像这样定义`__init__()`。

```python
import torch
import torch.nn as nn
from logging import getLogger
from libtraffic.model.abstract_traffic_state_model import AbstractTrafficStateModel


class NewModel(AbstractTrafficStateModel):
    def __init__(self, config, data_feature):
        super().__init__(config, data_feature)
        # section 1: data_feature
        self._scaler = self.data_feature.get('scaler')
        self.num_nodes = self.data_feature.get('num_nodes', 1)
        self.feature_dim = self.data_feature.get('feature_dim', 1)
        self.output_dim = self.data_feature.get('output_dim', 1)
        self._logger = getLogger()
        # section 2: model config 
        self.input_window = config.get('input_window', 1)
        self.output_window = config.get('output_window', 1)
        self.device = config.get('device', torch.device('cpu'))
        self.hidden_size = config.get('hidden_size', 64)
        self.num_layers = config.get('num_layers', 1)
        self.dropout = config.get('dropout', 0)
        # section 3: model structure
        self.rnn = nn.LSTM(input_size=self.num_nodes * self.feature_dim, hidden_size=self.hidden_size,
                           num_layers=self.num_layers, dropout=self.dropout)
        self.fc = nn.Linear(self.hidden_size, self.num_nodes * self.output_dim)
```

在代码的第一部分，我们从`data_feature`中获取必要的参数，包括节点数（`num_nodes`）、数据输入尺寸（`feature_dim`）、输出尺寸（`output_dim`）和数据规范化对象（`scaler`），并初始化记录器。

在代码的第二部分，我们从配置中获取必要的参数，包括隐藏层尺寸（`hidden_size`）、网络层数（`num_layers`）、输入时间长度（`input_window`）、输出时间长度（`output_window`），等等。

在代码的第三部分，我们定义了模型结构，包括一个LSTM层和一个全连接层。

## 实现predict()

然后我们定义`predict()`方法，用来预测模型的结果。`predict()`的输入参数是`batch`，它是一个 [Batch](https://github.com/LibTraffic/Bigscity-LibTraffic-Docs-zh_CN/blob/master/source/user_guide/data/batch.md)类的对象。

`AbstractModel`和`AbstractTrafficStateModel`都继承自`torch.nn.Module`类。如果你熟悉Pytorch框架，你会发现这个函数与`torch.nn.Module`中的`forward()`函数类似。在大多数情况下，你可以在这个函数里面直接调用`forward()`函数来获得模型的输出。

这个函数的目的是，你可以在`forward()`函数计算的模型输出的基础上做一些额外的处理。例如，当`forward()`函数计算的是模型的单步预测结果，而你需要的是多步预测的结果，你可以使用`predict()`函数来实现。

例如，你可以这样定义`predict()`。

```python
class NewModel(AbstractTrafficStateModel):
    def forward(self, batch):
        src = batch['X'].clone()
        src = src.permute(1, 0, 2, 3)
        batch_size = src.shape[1]
        src = src.reshape(self.input_window, batch_size, self.num_nodes * self.feature_dim)
        outputs = []
        for i in range(self.output_window):
            out, _ = self.rnn(src)
            out = self.fc(out[-1])
            out = out.reshape(batch_size, self.num_nodes, self.output_dim)
            outputs.append(out.clone())
            src = torch.cat((src[1:, :, :], out.reshape(
                batch_size, self.num_nodes * self.feature_dim).unsqueeze(0)), dim=0)
        outputs = torch.stack(outputs)
        return outputs.permute(1, 0, 2, 3)

    def predict(self, batch):
        return self.forward(batch)
```

可以看出，`predict`函数直接调用`forward`函数，而在`forward`函数中，我们定义了模型的计算过程。这个模型使用LSTM进行多次预测，并将每次预测的输出作为下一个输入。这里我们假设输入数据维度和输出数据维度相等，即`feature_dim=output_dim`。

## 实现calcualte_loss()

最后，我们定义了`calculate_loss()`方法，`calculate_loss()`用于计算预测结果与地面实测值之间的损失。

`calculate_loss()`的输入参数是`batch`，它是一个[Batch](https://github.com/LibTraffic/Bigscity-LibTraffic-Docs-zh_CN/blob/master/source/user_guide/data/batch.md)类的对象。该方法返回一个用于反向传播的`Torch.Tensor`。

你可以自定义损失函数或者调用我们在`libtraffic/model/loss.py`文件中定义的损失函数。

例如，你可以像这样定义`calcualte_loss()`。

```python
from libtraffic.model import loss

class NewModel(AbstractTrafficStateModel):
    def calculate_loss(self, batch):
        y_true = batch['y']
        y_predicted = self.predict(batch)
        y_true = self._scaler.inverse_transform(y_true[..., :self.output_dim])
        y_predicted = self._scaler.inverse_transform(y_predicted[..., :self.output_dim])
        return loss.masked_mae_torch(y_predicted, y_true, 0)
```

这里我们直接调用了`loss.py`中定义的`loss.masked_mae_torch`函数，其功能是计算 MAE 损失。

现在我们已经完成了对模型结构的定义，还剩下一些简单的配置。

## 导入模型

添加模型后，你需要修改你的模型所属的任务文件夹中的`__init__.py`文件。在上面的例子中，你需要修改的文件是`libtraffic/model/traffic_speed_prediction/__init__.py`。

请添加这样的代码：

```python
from libtraffic.model.traffic_speed_prediction.NewModel import NewModel

__all__ = [
    "NewModel",
]
```

## 加入模型参数

最后，你需要修改一些相关的`config`文件。

- 首先，你需要修改`libtraffic/config/task_config.json`，它用于设置每个任务所支持的模型和数据集，并指定模型所使用的基本参数（数据模块、执行模块、评估模块）。

  例如，你可以添加如下代码，这意味着`NewModel`使用的数据模块类是`TrafficStatePointDataset`，执行模块类是`TrafficStateExecutor`，而评估模块类是`TrafficStateEvaluator`。

```json
{
    "traffic_state_pred": {
        "allowed_model": ["NewModel"],
        "allowed_dataset": [""],
        "NewModel": {
            "dataset_class": "TrafficStatePointDataset",
            "executor": "TrafficStateExecutor",
            "evaluator": "TrafficStateEvaluator"
        }
    }
}
```

- Second, you need to add a file in the `libtraffic/config/model/` directory to set the default parameters of your model. You can also set parameters of other modules which you want to cover as the parameters of the model module have the highest priority than other modules.

  For example, you can add this file `libtraffic/config/model/traffic_state_pred/NewModel.json` and add codes like the follows. You can see that in addition to the three parameters related to the model structure, we also define the number of training rounds(`max_epoch`), optimizer(`learner`), and learning rate(`learning_rate`) to cover the default execution configuration.

  第二，你需要在`libtraffic/config/model/目录下添加一个文件来设置你的模型的默认参数。你也可以设置你想覆盖的其他模块的参数，因为模型模块的参数比其他模块有最高的优先权。

  例如，你可以添加这个文件`libtraffic/config/model/traffic_state_pred/NewModel.json`并添加如下代码。你可以看到，除了与模型结构有关的三个参数外，我们还定义了训练轮数（`max_epoch`）、优化器（`learner`）和学习率（`learning_rate`），以涵盖默认的执行配置。

```json
{
  "hidden_size": 64,
  "num_layers": 1,
  "dropout": 0,

  "max_epoch": 100,
  "learner": "adam",
  "learning_rate": 0.001
}
```

**注意：配置的文件名和`allowed_model`列表中的值必须与你添加的模型的类名相同。**就像上面的`NewModel`。

现在你已经学会了如何添加一个新的模型，尝试用以下命令来运行这个模型！

```shell
python run_model.py --task traffic_state_pred --model NewModel --data
```

