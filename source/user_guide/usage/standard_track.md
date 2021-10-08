# 标准赛道

在交通大数据领域，长期存在数据集评价标准不一致，评估指标不一致和数据集预处理过程不一致等现象，导致了不同模型的可比性较差。因此，为了解决上述问题，本项目为每个任务实现了一套标准的pipeline(track)。

在标准赛道上，项目提供的原始数据集，标准数据模块(Data module)和标准评估模块(Evaluator module)通过使用相同的数据输入与评估指标来限制不同的模型，以提高评估结果的可比性。

不同任务的标准数据输入格式和评估输入格式解释如下：

## 交通状态预测

根据交通数据空间结构的不同，交通状态数据一般可以用以下格式的张量表示：

- 一个形如`(N,T,F)`的三维tensor， `T`是时间长度 ， `F` 是特征维度， `N` 传感器数量。
- 一个形如为`(T,F,I,J)`的四维tensor， `T`是时间长度 ， `F` 是特征维度，  `I,J`表示网格数据的行和列索引。
- 一个形如`(T,F,S,T)`的四维tensor， `T`是时间长度 ， `F` 是特征维度，  `S,T` 表示`od`数据的出发地id和目的地id。
- 一个形如`(T,F,SI,SJ,TI,TJ)`的六维tensor， `T`是时间长度 ，`F` 是特征维度，`SI,SJ,TI,TJ` 表示`grid-od`数据出发地和目的地的行索引和列索引。

标准数据输入格式类字典的[Batch](../data/batch.md)对象实例，对象的key名如下：

* `X`：模型输入的多维度tensor，`shape = (batch_size, T_in, space_dim, feature_dim)`， 每个维度表示batch中的样本总数，输入时间窗口的宽度，空间维度和数据特征维度。尤其是，空间维度可以是如上所述的`N` or `I, J` or `S, T` or `SI, SJ, TI, TJ` 。
* `y`：模型期望输出的多维度tensor，`shape = (batch_size, T_out, space_dim, feature_dim)`, 每个维度表示batch中的样本总数，输出时间窗口的宽度，空间维度和数据特征维度。在这些中，空间维度可以是如上所述的`N` or `I, J` or `S, T` or `SI, SJ, TI, TJ` 。
* `X_ext`： 可选的外部数据， `shape = (batch_size, T_in, ext_dim)`，每个维度表示batch中的样本总数，输入时间窗口的宽度，空间维度和外部数据特征维度。**尤其是，一些模型可能直接将`X_ext`合并入`X`作为模型的输入**。
* `y_ext`：可选的外部数据O，`shape = (batch_size, T_out, ext_dim)`，每个维度表示batch中的样本总数，输出时间窗口的宽度，空间维度和外部数据特征维度。

标准评价输入格式是一个字典对象，并且这个字典有下列key名：

- `y_true`：真实值，格式与输入的`y`相同。
- `y_pred`：预测值，格式与输入的`y`相同。

## 轨迹位置预测

标准数据输入格式是类字典的[Batch](../data/batch.md)对象实例。该对象的key名如下：

- `history_loc`：历史轨迹位置信息，`shape = (batch_size, history_len)`，`history_len` 是历史轨迹的长度。
- `history_tim`：历史轨迹时间信息，`shape = (batch_size, history_len)`。
- `current_loc`：当前轨迹位置信息，`shape = (batch_size, current_len)`，`current_len` 是当前轨迹长度。
- `current_tim`：当前轨迹时间信息，`shape = (batch_size, current_len)`。
- `uid`：每个轨迹的用户的id，`shape = (batch_size)`。
- `target`：期望下一跳的位置，`shape = (batch_size) `。

标准评价输入格式是类字典对象，字典的key名如下：

- `uid`： 每个轨迹使用者的id， `shape = (batch_size)`。
- `loc_true`：预期下一跳的位置， `shape = (batch_size)`。
- `loc_pred`：模型预测输出，`shape = (batch_size, output_dim)`。

## 路网匹配

标准的数据输入格式是一个字典。这个对象的key名如下：

* `trajectory`：是所有轨迹的一个字典，它的key是`usr_id`。每一个 `usr_id` 对应一个`numpy.ndarray`，表示从连续运动的对象上采样得到的按时间顺序排列的空间点序列，其列名为`columns=(index,longitude,latitude,time)`或者`columns=(index,longitude,latitude)`.
* `rd_nwk`： 一个具有类型`networkx.classes.digraph.DiGraph`的路网数据。
* `route`：一个由`rel_id`组成的`numpy.ndarray` 对象，`shape=(num_road,)`，代表真实路径

标准的评价输入格式是一个字典。这个对象的key名如下：

* `result`：一个由`rel_id` 组成的 `numpy.ndarray`对象， `shape=(num_sample,)`，代表匹配的结果。`num_sample`是轨迹数据中GPS采样点的数量

* `route`：见标准的数据输入格式中的描述

* `rd_nwk`：见标准的数据输入格式中的描述

  