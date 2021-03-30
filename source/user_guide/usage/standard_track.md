## 标准赛道

在交通大数据领域中，长期存在着评测数据集不统一、评测指标不统一、数据集预处理不统一等现象，导致了不同模型的性能可比性较差。因此本项目为了解决上述问题，为每个任务实现了一套标准流水线（赛道）。

标准赛道上，使用项目提供的原始数据集、标准数据模块（Data 模块）、标准评估模块（Evaluator 模块），从而约束不同模型使用相同的数据输入与评估指标，以提高评估结果的可比性。

下面对不同任务的标准数据输入格式与评估输入格式进行说明：

#### 轨迹下一跳预测

标准数据输入格式为类字典的 [Batch](../data/batch.md) 对象实例，该对象所具有的键名如下：

* `history_loc`：历史轨迹位置信息，`shape = (batch_size, history_len)`， `history_len` 为历史轨迹的长度。

* `history_tim`：历史轨迹时间信息，`shape = (batch_size, history_len)`。

* `current_loc`：表示当前轨迹位置信息，`shape = (batch_size, current_len)`， `current_len` 为历史轨迹的长度。

* `current_tim`：表示当前轨迹位置信息，`shape = (batch_size, current_len)`。

* `uid`：每条轨迹所属用户的 id，`shape = (batch_size)`。

* `target`：期望的下一跳位置，`shape = (batch_size) `。

标准评估输入格式为字典对象，该字典具有的键名如下：

* `uid`：每条输出所属的用户 id，`shape = (batch_size)`。
* `loc_true`：期望下一跳位置信息，`shape = (batch_size)`。
* `loc_pred`：模型预测输出，`shape = (batch_size, output_dim)`。 

#### 交通状态预测

根据交通数据的不同空间结构，交通状态数据一般可以用如下几种格式的张量进行表示：

- `（N,T,F）`的三维张量，`T`是时间长度，`F`是特征维度，`N`是传感器的个数。
- `（T,F,I,J）`的四维张量，`T`是时间长度，`F`是特征维度，`I,J`表示网格数据的行列索引。
- `（T,F,S,T）`的四维张量，`T`是时间长度，`F`是特征维度，`S,T`表示`od`数据的起点和终点的编号。
- `（T,F,SI,SJ,TI,TJ）`的六维张量，`T`是时间长度，`F`是特征维度，`SI,SJ,TI,TJ`表示网格结构的`od`数据的起点和终点的行列索引。

标准模型输入格式为类字典的 [Batch](../data/batch.md) 对象实例，该对象所具有的键名如下：

* `X`：模型输入的多维张量，`shape = (batch_size, T_in, space_dim, feature_dim)`，分别表示 batch 中的样本总数，输入时间窗的宽度，空间上的维度，数据特征维数。其中，空间上的维度可以是上文中的`N`或`I,J`或`S,T`或`SI,SJ,TI,TJ`。
* `y`：模型期望输出的多维张量，`shape = (batch_size, T_out, space_dim, feature_dim)`，分别表示 batch 中的样本总数，输出时间窗的宽度，空间上的维度，数据特征维数。其中，空间上的维度可以是上文中的`N`或`I,J`或`S,T`或`SI,SJ,TI,TJ`。
* `X_ext`：可选的外部数据，`shape = (batch_size, T_in, ext_dim)`，分别表示 batch 中的样本总数，输入时间窗的宽度，空间上的维度，外部数据特征维数。部分模型可能直接将`X_ext`融合到`X`中作为模型的输入。
* `y_ext`：可选的外部数据，`shape = (batch_size, T_out, ext_dim)`，分别表示 batch 中的样本总数，输出时间窗的宽度，空间上的维度，外部数据特征维数。

标准评估模块的输入格式为字典对象，该对象所具有的键名如下：

- `y_true`：真实值，格式同输入中的 `y`。
- `y_pred`：预测值，格式同输入中的 `y`。

