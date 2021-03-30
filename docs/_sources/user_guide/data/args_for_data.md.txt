# Args for Data

下边介绍数据集涉及的相关参数。

## Traffic State Prediction DataSet

下述参数为交通状态预测任务中所用到的全部参数：

- `batch_size`：批次大小

- `cache_dataset`：是否保存经过`Dataset`类处理好的数据集，**默认True**

- `num_workers`： `Dataloader`类的参数，**这个参数用本地CPU跑，应该设为0**

- `pad_with_last_sample`：总样本数跟`batch_size`除不尽的时候，是否用最后一个元素补齐最后一个batch，**默认True**

- `train_rate`：训练集所占比例

- `eval_rate`：验证集所占比例，划分顺序是【训练集，验证集，测试集】，从前到后的顺序按比例划分

- `input_window`：预测使用的过去时间步的长度，**交通预测一般使用过去一段时间（即多个时间步的数据对未来数据进行预测）**

- `output_window`：预测未来的时间步的长度，**交通预测一般是多步预测，即预测未来多个时间步的交通状况**

- `load_external`：是否加载外部数据（如天气数据），**默认False**

  - `normal_external`：是否对外部数据进行归一化处理，**默认False**
  - `add_time_in_day`：时间参数，增加时间片属于一天中的哪个时刻的辅助信息，**默认False**，依赖于参数`load_external=True`。
  - `add_day_in_week`：时间参数，增加时间片属于一周中的哪一天的辅助信息，**默认False**，依赖于参数`load_external=True`。

- 从`Dataset`类的`get_feature()`函数中获取的部分参数：

  - `scaler`：指定归一化方法，**需要从外部指定**，目前支持`normal`、`standard`、`minmax01`、`minmax11`、`none`，默认`none`。
    - `normal`：除以最大值
    - `standard`：Z-score归一化
    - `minmax01`：MinMax归一化 结果区间[0, 1]
    - `minmax11`：MinMax归一化 结果区间[-1, 1]
    - `none`：不归一化
  - `feature_dim*`：交通数据特征维度的大小，**不能从外部指定**，而是根据不同数据集自动计算得到的，外部数据的存在和其他的一些参数也可能会影响这个维度的大小。
  - `adj_mx*`：交通数据构建的邻接矩阵，**不能从外部指定**，从`.rel`文件中计算出来的。与`.rel`文件相关的参数设置请参见[原子文件](./atmoic_files.md)一节。
  - `num_nodes*`：交通数据实体的个数，例如传感器的数目、网格的数目，**不能从外部指定**，而是根据不同数据集自动计算得到的。
  - `len_row*`：网格数据的网格行数，**不能从外部指定**，而是根据不同数据集自动计算得到的。
  - `len_column*`：网格数据的网格列数，**不能从外部指定**，而是根据不同数据集自动计算得到的。
  - `output_dim*`：交通预测模型输出的预测结果的特征维度的大小，**需要从外部指定**，即预测模型的预测目标。一般不等于`feature_dim`，因为输入数据可能包含了外部特征，但是模型输出的结果一般只包含有效的交通状况信息，而不包含外部信息。该参数由数据集原子文件中的config文件所指定，请参见[原子文件](./atmoic_files.md)一节。

- 其他不通用的参数

  注：部分交通预测模型通过对接近度(closeness)/周期(period)/趋势(trend)进行建模实现交通预测，默认使用`len_closeness`/`len_period`/`len_trend`的数据作为历史数据进行预测，取代了上文中的参数`input_window`和`output_window`，因此多出了下述若干参数：

  - `points_per_hour`：一小时有几个时间步，例如数据集是5min一个时间步，则为12

  - `len_closeness`：closeness时间片序列的长度
  - `len_period`：period时间片序列的长度
  - `len_trend`：trend时间片序列的长度
  - `pad_forward_period`：period对应位置的时间片向前扩展多少时间片
  - `pad_back_period`：period对应位置的时间片向后扩展多少时间片
  - `pad_forward_trend`：trend对应位置的时间片向前扩展多少时间片
  - `pad_back_trend`：trend对应位置的时间片向后扩展多少时间片
  - `interval_period`：period时间间隔的长度，一般为1，表示间隔一天
  - `interval_trend`：trend时间间隔的长度，一般为7，表示间隔一周

  注：从`Dataset`类的`get_feature()`函数中获取到的`len_closeness`/`len_period`/`len_trend`表示这三段数据的实际长度，因为返回的输入结果`batch[‘X’]`中将这三段数据按顺序拼接到了一起，根据长度可以获取逐段对应的数据。

## Trajectory Location Prediction DataSet