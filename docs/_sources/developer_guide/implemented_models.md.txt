# Customize Models

本文档用于介绍如何在`TrafficDL`下开发一个新模型。

目前支持以下几个任务：

-  Traffic Location Prediction
-  Traffic Flow Prediction
-  Traffic Speed Prediction
-  On-Demand Service predition
-  Travel Time prediction
-  Traffic Accident prediction

开发模型：

`AbstractModel`类是所有模型的基类，实现模型时，请继承此类。

`AbstractModel`类继承自`torch.nn.Module`，实现接口`forward(self, batch)`，也就是说所有模型都以`Batch`类对象作为输入。

约定：

- 不同任务的模型存放在不同的子文件夹下，
- 公用的损失函数、初始化方法、常用的layer统一存放，

所以可以这样实现`newmodel.py`：

```python
from trafficdl.model.abstract_model import AbstractModel
class NewModel(AbstractModel):
    def __init__(self, config, data_feature):
        pass
     def forward(self, batch):
        pass
```

接下来需要实现`__init__()`方法：

该方法是参数是`config`和`data_feature`，其中`config`是配置文件，`data_feature`是构建模型所需要的数据集的相关特征。

接下来需要实现模型的核心内容以及相应的`forward`方法，注意`forward`方法以`Batch`类的对象为输入。

