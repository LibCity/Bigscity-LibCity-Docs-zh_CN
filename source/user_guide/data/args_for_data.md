#Args for Data

下文描述数据集中涉及的相关参数。

##Traffic State Prediction DataSet

以下参数是在流量状态预测任务中用到的所有参数。

* `batch_size`: 培训和测试批次大小。默认为 `64`。

* `cache_dataset`: 是否保存处理后的数据集。默认为 `True`。

* `num_workers`: [Dataloader](https://pytorch.org/docs/stable/data.html?highlight=dataloader#torch.utils.data.DataLoader) 的参数。默认为 `0`。

* `pad_with_last_sample`: 当样本总数不能被 `batch_size` 整除时， 是否用最后一个元素填充最后一批。默认为`True`。

* `train_rate`: 训练集占全部数据集的比例。默认为 `0.7`。 （数据集划分顺序为训练集、测试集、验证集）

* `eval_rate`: 验证集的比例。默认为 `0.1`。

* `input_window`: 用于预测的前一批时间步的数目。流量预测通常使用过去多个时间步长的数据来预测未来的数据。默认为`12`。

* `output_window`: 预测的时间步的数目。具体来说，使用在 `input_window` 中的数据来预测 `output_window` 中的数据。 默认为 `12`。

* `load_external`: 是否加载外部数据(如天气数据)。默认为 `False`。

    *   `normal_external`: 是否规范化外部数据。默认为 `False`。

    *   `add_time_in_day`: 时间参数，添加一天中时间的辅助信息。默认为 `False`。 该参数依赖于参数 `load_external=True`。

    *   `add_day_in_week`: 时间参数，增加星期的辅助信息，默认为 `False`。 该参数依赖于参数 `load_external=True`。

* 一些参数从 `Dataset` 类的 `get_feature()` 方法获取：

    * `scaler`: 指定规范化方式， **需要在外部指定**. 在 \[`normal`, `standard`, `minmax01`, `minmax11`, `none`\]当中取值。默认为 `none`。

        *   `normal`: 除以最大值来进行规范化。

        *   `standard`: Z-score 规范化。

        *   `minmax01`: MinMax 规范化， 结果区间为 \[0, 1\]。

        *   `minmax11`: MinMax 规范化， 结果区间为 \[-1, 1\]。

        *   `none`: 不进行规范化。

    * `feature_dim*`: 交通数据特征维的大小，**不能在外部指定**，而是根据不同的数据集自动计算 。 外部数据和其他一些参数也可能影响这个维度的大小。

    * `adj_mx*`: 由流量数据构造的邻接矩阵，**不能从外部指定**，而是由 `.rel` 文件自动计算。 有关 `.rel` 文件的参数设置, 请查阅 [atomic files](./atmoic_files.md) 小节。

    * `num_nodes*`: 交通数据实体的数量，如传感器的数量、网格的数量等，**不能从外部指定**，而是根据不同的数据集自动计算。

    * `len_row*`: 网格数据的网格行数，**不能从外部指定**，而是根据不同的数据集自动计算。

    * `len_column*`: 网格数据的网格列数，**不能从外部指定**，而是根据不同的数据集自动计算。

    * `output_dim*`: 流量预测模型输出结果的特征维的大小，**需要在外部指定**。 其通常不等于 `feature_dim`， 因为输入数据可能包含外部特征，但模型的输出结果通常只包含有效的交通信息，而不含外部信息。 该参数通过数据集的 atomic file 设置, 请查阅 [atomic file](./atmoic_files.md) 小节。

* 其他非常用参数

    注: 一些交通预测模型通过接近度(closeness)/周期(period)/趋势(trend)进行建模来实现预测, 并使用 `len_closeness`/`len_period`/`len_trend` 数据作为历史数据进行预测，而不是上述 `input_window` 和 `output_window`, 所以有以下额外参数 are added:

    *   `points_per_hour`: 一个小时有多少个时间步长，例如，若数据集为5分钟一个时间步，那么它就是12。

    *   `len_closeness`: closeness 时间片序列的长度。

    *   `len_period`: period 时间片序列的长度。

    *   `len_trend`: trend 时间片序列的长度。

    *   `pad_forward_period`: period 对应位置的时间片向前扩展多少时间片。

    *   `pad_back_period`: period 对应位置的时间片向后扩展多少时间片。

    *   `pad_forward_trend`: trend 对应位置的时间片向前扩展多少时间片。

    *   `pad_back_trend`: trend 对应位置的时间片向后扩展多少时间片。

    *   `interval_period`: period 时间间隔的长度，一般为1，表示间隔一天。

    *   `interval_trend`: trend时间间隔的长度，一般为7，表示间隔一周。


    注: 从 `Dataset`类的`get_feature()` 方法当中获取的 `len_closeness`/`len_period`/`len_trend` 表示**这三段数据的实际长度**。 在返回值 `batch['X']` 中, 这三段数据按顺序拼接在一起。因此根据长度可以获得每一组数据。


### Trajectory Location Prediction DataSet