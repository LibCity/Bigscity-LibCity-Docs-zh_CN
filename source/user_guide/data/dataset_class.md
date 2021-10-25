# 已实现的Dataset类

已实现的Dataset类的功能介绍如下

- `AbstractDataset`

  所有数据集的基类。**注意这是抽象类，不能直接使用**

- `TrajectoryDataset`

  所有轨迹位置预测任务的基类。

- `TrafficStateDataset`

  用于交通状态预测任务的基类之一。**注意这是抽象类，不能直接使用**。默认情况下，`input_window`的数据被用来预测`output_window`对应的数据。此类生成的[Batch](../user_guide/data/batch.md) 对象包含两个键，分别是`X`和`y`。此处的`input_window`和`output_window`是data的参数，点击[此处](../user_guide/data/args_for_data.md)查看细节。

- `TrafficStateCPTDataset`

  用于交通状态预测任务的另一个基类。**注意这是抽象类，不能直接使用**。一些交通预测模型通过对接近度/周期/趋势的建模来实现预测。默认情况下，`len_closeness`/`len_period`/`len_trend` 的数据被用来预测当前时刻的数据（单步预测）。此类生成的[Batch](../user_guide/data/batch.md)对象包含4个键，分别是`X`，`y`，`X_ext`和`y_ext` 。此处的 `len_closeness`/`len_period`/`len_trend` 是data的参数, 点击[此处](../user_guide/data/args_for_data.md)查看细节。

- `TrafficStatePointDataset`

  一个继承了`TrafficStateDataset`的类，用于交通状态预测，该类适用于空间维度是一维的数据集（即基于点/基于段/基于区域的数据集）。该类生成的[Batch](../user_guide/data/batch.md)对象中的张量形状是3维的，即`space_dim`, `time_dim`, `feature_dim`（空间维度、时间维度、特征维度）。

- `TrafficStateGridDataset`

  一个继承了`TrafficStateDataset`的类，用于交通状态预测，该类适用于基于网格的数据集。这个类生成的[Batch](../user_guide/data/batch.md)对象中的张量形状是3维还是4维取决于参数`use_row_column`。如果设置`use_row_column=True`，那么4个维度是`grid_row_dim`, `grid_column_dim`, `time_dim`, `feature_dim`（网格行数、网格列数、时间维度、特征维度）。否则，3个维度是`space_dim`、`time_dim`、`feature_dim`（空间维度、时间维度、特征维度），在这种情况下，网格被重新编号为一维的。

- `TrafficStateOdDataset`

  一个继承了`TrafficStateDataset`的类，用于交通状态预测，该类适用于基于OD的数据集，即起点和终点。这个类生成的[Batch](../user_guide/data/batch.md)对象中的张量形状是4维的，即`origin_dim`, `destination_dim`, `time_dim`, `feature_dim`（起点维度、终点维度，时间维度、特征维度）。

- `TrafficStateGridOdDataset`

  一个继承了`TrafficStateDataset`的类，用于交通状态预测，该类适用于基于网格的OD数据集。这个类生成的[Batch](../user_guide/data/batch.md)对象中的张量形状是4维或6维，取决于参数`use_row_column`。如果设置`use_row_column=True`，那么张量拥有6个维度，分别是`origin_grid_row_dim`, `origin_grid_column_dim`, `destination_grid_row_dim`, `destination_grid_column_dim`, `time_dim`, `feature_dim`（起点网格行数、起点网格列数、终点网格行数、终点网格列数、时间维度、特征维度）。否则，张量拥有4个维度，分别是`origin_dim`, `destination_dim`, `time_dim`, `feature_dim`（起点空间维度、终点空间维度、时间维度、特征维度），在这种情况下，二维网格被重新编号为一维的。
  
- `MapMatchingDataset`

  所有地图匹配任务的基类。该类生成一个包含3个键的字典：`rd_nwk`, `trajectory`和`route`，分别代表路网、GPS样本的轨迹和真实轨迹。如果`delta_time=True`，`trajectory`将包括一个`time`列，表示轨迹时间读秒。`delta_time`是数据集的参数，详见[此处](../data/args_for_data.md)。标准数据输入的介绍见[此处](../usage/standard_track.md)。

