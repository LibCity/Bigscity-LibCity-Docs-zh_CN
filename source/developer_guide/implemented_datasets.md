# 自定义Dataset

对于一个新的模型，如果没有合适的已实现数据集供使用，则需要设计一个新的数据集。本文档用于介绍如何在`LibCity`中开发一个新的数据集。

## 创建新的Dataset类

首先，我们创建的数据集应该继承自`AbstractDataset`或它的子类。

例如，若想为交通状态预测任务开发一个名为`NewDataset`的数据集，需要将代码写入`libcity/data/dataset/`目录下的`newdataset.py`文件中。

在如下代码中，我们的`NewDataset`继承了`AbstractDataset`类的子类`TrafficStatePointDataset`。

```python
from libcity.data.dataset import TrafficStatePointDataset

class NewDatasets(TrafficStatePointDataset):
    def __init__(self, config):
        super().__init__(config)
        pass
```

或者可以直接继承`AbstractDataset` 类，代码如下。

```python
from libcity.data.dataset import AbstractDataset

class NewDatasets(AbstractDataset):
    def __init__(self, config):
        pass
```

## 重写对应方法

`AbstractDataset`中的函数`get_data()`被用来分割数据，并获取3个数据加载器`train_dataloader`、`eval_dataloader`和`test_dataloader`。若想要获取数据加载器，需要调用函数`libcity.data.utils.generate_dataloader`来从输入数据的列表中获取，其中生成的数据加载器包含[Batch](../user_guide/data/batch.md)对象。

`AbstractDataset`中的函数`get_data_feature()`被用来返回一些数据集的特征，这些特征将被模型和执行器使用。

在`AbstractDataset`的子类中定义的其他接口将不在此描述。

如果没有合适的数据集类，那么你可以重写上面提到的相应接口。

### 样例 1

样例1用来演示如何直接继承`AbstractDataset`并重写函数`get_data_feature()`以返回我们想要的一些值。

```python
from libcity.data.dataset import AbstractDataset

class NewDatasets(AbstractDataset):
    def __init__(self, config):
        pass
    
    def get_data_feature(self):
        return {"scaler": self.scaler, "adj_mx": self.adj_mx,
                "num_nodes": self.num_nodes, "feature_dim": self.feature_dim,
                "output_dim": self.output_dim}
```

### 样例 2

样例2用来演示如何继承`AbstractDataset`的子类并重写其中的一个方法（`_load_rel`）。

```python
from libcity.data.dataset import TrafficStatePointDataset

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

样例3用来解释如何继承`AbstractDataset`的子类，并返回从原始数据文件转化而来的，含有不同键的`Batch`。具体来说，我们打算返回三个键值对，其中键包括：`X`，`Y`和`Z`。这只是一个例子，更多的细节，你可以参考`TrafficStateCPTDataset`，它有四个键的`Batch`。

```python
from libcity.data.dataset import TrafficStateDataset

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
        # Get dataloader by libcity.data.utils.generate_dataloader.
        self.train_dataloader, self.eval_dataloader, self.test_dataloader = \
            generate_dataloader(train_data, eval_data, test_data, self.feature_name,
                                self.batch_size, self.num_workers)
        # Return the dataloader
        return self.train_dataloader, self.eval_dataloader, self.test_dataloader
```