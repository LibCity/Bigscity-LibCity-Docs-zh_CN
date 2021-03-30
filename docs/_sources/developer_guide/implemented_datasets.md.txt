# Customize Dataset

本文档用于介绍如何在`TrafficDL`下开发一个新的数据集类。

我们已经为以下几个任务开发了标准的Evaluator：

- Traffic Location Prediction
- Traffic Flow Prediction
- Traffic Speed Prediction
- On-Demand Service predition
- Travel Time prediction
- Traffic Accident prediction

`AbstractDataset`类是所有数据集的基类，实现数据集类时，请继承此类。

`AbstractDataset`类中接口：

- `get_data()`用于获取划分好的train_dataloader/eval_dataloader/test_dataloader，
- `get_data_feature()`用于返回一些数据集的特征供模型和调度器使用。

约定：

- Dataset类，负责加载原子文件并进行一些数据预处理操作，以及切分训练集、验证集、测试集。
- 处理好的数据集缓存到`cache/dataset_cache/`。
- `utils.generate_dataloader()`是实现好的切分数据集并返回dataloader，`get_data()`应该调用此函数。

所以可以这样实现`newdataset.py`：

```python
from trafficdl.data.dataset import AbstractDataset

class NewDatasets(AbstractDataset):
    def __init__(self, config):
        pass
    
    def get_data(self):
        pass
    
    def get_data_feature(self):
        pass
```

接下来，只需要重写全部的接口即可。