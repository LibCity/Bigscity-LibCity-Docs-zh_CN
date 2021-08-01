# 自定义Dataset类

本文档用于介绍如何在`TrafficDL`下开发一个新的数据集类。

## 已实现的Dataset类

已实现的Dataset类介绍如下

- `AbstractDataset`

  所有数据集的基类。**注意这是抽象类，不能直接使用**

- `TrajectoryDataset`

  所有轨迹位置预测任务的基类。

- `TrafficStateDataset`

  用于交通状态预测任务的基类之一。**注意这是抽象类，不能直接使用**。默认情况下，`input_window`的数据被用来预测`output_window`对应的数据。此类生成的[batch](https://github.com/LibTraffic/Bigscity-LibTraffic-Docs-zh_CN/blob/master/source/user_guide/data/batch.md)对象包含两个键，分别是`x`和`y`。此处的`input_window`和`output_window`是data的参数，点击[此处](https://github.com/LibTraffic/Bigscity-LibTraffic-Docs-zh_CN/blob/master/source/user_guide/data/args_for_data.md)查看细节。

- `TrafficStateCPTDataset`

  用于交通状态预测任务的另一个基类。**注意这是抽象类，不能直接使用。**一些交通预测模型通过对接近度/周期/趋势的建模来实现预测。默认情况下，`len_closeness`/`len_period`/`len_trend` 的数据被用来预测当前时刻的数据（单步预测）。此类生成的[batch](https://github.com/LibTraffic/Bigscity-LibTraffic-Docs-zh_CN/blob/master/source/user_guide/data/batch.md)对象包含4个键，分别是`X`，`y`，`X_ext`和`y_ext` 。此处的 `len_closeness`/`len_period`/`len_trend` 是data的参数, 点击[此处](https://github.com/LibTraffic/Bigscity-LibTraffic-Docs-zh_CN/blob/master/source/user_guide/data/args_for_data.md)查看细节。

- `TrafficStatePointDataset`

  一个继承了`TrafficStateDataset`的类，用于交通状态预测。只要这个数据集的空间维度是一维的，就可以用于基于点/基于段/基于区域的数据集。该类生成的[batch](https://github.com/LibTraffic/Bigscity-LibTraffic-Docs-zh_CN/blob/master/source/user_guide/data/batch.md)对象中的张量形状是3维的，即space_dim, time_dim, feature_dim。

- `TrafficStateGridDataset`

  一个继承了`TrafficStateDataset`的类，用于交通状态预测。该数据集适用于基于网格的数据集。这个类生成的[batch](https://github.com/LibTraffic/Bigscity-LibTraffic-Docs-zh_CN/blob/master/source/user_guide/data/batch.md)对象中的张量形状是3维还是4维取决于参数use_row_column。如果设置use_row_column=True，那么4个维度是grid_row_dim, grid_column_dim, time_dim, feature_dim。否则，3个维度是space_dim、time_dim、feature_dim，在这种情况下，网格被重新编号为一个维度。

- `TrafficStateGridOdDataset`

  一个继承了`TrafficStateDataset`的类，用于交通状态预测。该数据集用于基于网格的od数据集。这个类生成的[batch](https://github.com/LibTraffic/Bigscity-LibTraffic-Docs-zh_CN/blob/master/source/user_guide/data/batch.md)对象中的张量形状是4维还是6维取决于参数use_row_column。如果设置use_row_column=True，那么6个维度是origin_grid_row_dim, origin_grid_column_dim, destination_grid_row_dim, destination_grid_column_dim, time_dim, feature_dim。否则，4个维度是origin_dim, destination_dim, time_dim, feature_dim，在这种情况下，网格在一个维度上被重新编号。

- `STResNetDataset` and `ACFMDataset`

  继承了`TrafficStateDataset`的类，用于交通状态预测。

如果我们有一个新的模型，在没有合适的数据集类的情况下，我们需要设计一个新的数据集。

## 创建新的Dataset类

首先，我们应该从`AbstractDataset`或`AbstractDataset`的一个子类中创建一个新的数据集。

例如，我们想为交通状态预测任务开发一个名为`NewDataset`的数据集，并将代码写入`libtraffic/data/dataset/`目录中的`newdataset.py`。

这里我们继承了`AbstractDataset`类的子类`TrafficStatePointDataset`。

```python
from libtraffic.data.dataset import TrafficStatePointDataset

class NewDatasets(TrafficStatePointDataset):
    def __init__(self, config):
        super().__init__(config)
        pass
```

或者直接继承`AbstractDataset` 类。

```python
from libtraffic.data.dataset import AbstractDataset

class NewDatasets(AbstractDataset):
    def __init__(self, config):
        pass
```

## 重写对应方法

`AbstractDataset`中的函数`get_data()`用来获取被分割的3个数据加载器`train_dataloader`、`eval_dataloader`和`test_dataloader`。你需要调用函数`libtraffic.data.utils.generate_dataloader`来从输入数据的列表中获取数据加载器，其中生成的数据加载器包含批处理对象。

`AbstractDataset`中的函数`get_data_feature()`被用来返回一些数据集的特征，供模型和执行器使用。

在`AbstractDataset`的子类中定义的其他接口将不在此描述。

如果没有合适的数据集类，那么你可以重写上面提到的相应接口。

### 样例 1

这里我们解释一下如何直接继承`AbstractDataset`并重写函数`get_data_feature()`以返回我们想要的一些值。

```python
from libtraffic.data.dataset import AbstractDataset

class NewDatasets(AbstractDataset):
    def __init__(self, config):
        pass
    
    def get_data_feature(self):
        return {"scaler": self.scaler, "adj_mx": self.adj_mx,
                "num_nodes": self.num_nodes, "feature_dim": self.feature_dim,
                "output_dim": self.output_dim}
```

### 样例 2

这里我们解释一下如何继承`AbstractDataset`的子类并重写其中的一个方法。

```python
from libtraffic.data.dataset import TrafficStatePointDataset

class NewDatasets(TrafficStatePointDataset):
    def __init__(self, config):
        super().__init__(config)
        pass
    
    # We will rewrite this method which is used to calculate `self.adj_mx` based on the atmoic file `rel_file.rel`.
    def _load_rel(self):
        relfile = pd.read_csv(self.data_path + self.rel_file + '.rel')
        self.adj_mx = np.zeros((len(self.geo_ids), len(self.geo_ids)))
        self.adj_mx[:] = 1  # set all one
```

### 样例 3

这里我们解释如何继承`AbstractDataset`的子类，并从头开始返回含有不同键的batch。具体来说，我们打算返回三个键值对：X，Y和Z。这只是一个例子，更多的细节，你可以参考`TrafficStateCPTDataset`，它有四个键的批处理。

```python
from libtraffic.data.dataset import TrafficStateDataset

class NewDatasets(TrafficStateDataset):
    def __init__(self, config):
        super().__init__(config)
        # the origin code
        # self.feature_name = {'X': 'float', 'y': 'float'}
        # the modified code
        self.feature_name = {'X': 'float', 'Y': 'float', 'Z': 'int'}
        pass
    
    def get_data(self):
        # Load datset for the keys x,y,z, generate [x|y|z]_[train|val|test].
        # ... (implement it yourself)
        # Data normalization using self.scaler.
        # ... (implement it yourself)
        # Aggregate X, Y, Z into a list.
        # The i-th element in train_data(a list) is a tuple, consists of x_train[i], y_train[i] and z_train[i].
        train_data = list(zip(x_train, y_train, z_train))
        eval_data = list(zip(x_val, y_val, z_val))
        test_data = list(zip(x_test, y_test, z_test))
        # Get dataloader by libtraffic.data.utils.generate_dataloader.
        self.train_dataloader, self.eval_dataloader, self.test_dataloader = \
            generate_dataloader(train_data, eval_data, test_data, self.feature_name,
                                self.batch_size, self.num_workers)
        # Return the dataloader
        return self.train_dataloader, self.eval_dataloader, self.test_dataloader
```