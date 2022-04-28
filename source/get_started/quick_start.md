# 快速入门

## 下载一个数据集

LibCity中使用的数据集以一种名为[原子文件](../user_guide/data/atomic_files.md)的统一数据存储格式存储。

为了直接在`LibCity`中使用[原始数据集](../user_guide/data/raw_data.md)，我们已经将所有这些数据集转换成了原子文件的格式，并提供了[转换工具](https://github.com/LibCity/Bigscity-LibCity-Datasets)。

您可以直接下载我们处理好的数据集。数据集链接是[百度网盘](https://pan.baidu.com/s/1qEfcXBO-QwZfiT0G3IYMpQ)（提取码：1231）或[Google Drive](https://drive.google.com/drive/folders/1g5v2Gq1tkOq8XO0HDCZ9nOTtRpB6-gPe?usp=sharing)。

在运行LibCity的模型前，请确保您至少下载了一个数据集，并把它放在了`Bigscity-LibCity/raw_data/dataset_name/*`目录下。

例如，如果您下载了METR_LA数据集，目录结构如下所示：

- `Bigscity-LibCity/raw_data/METR_LA/METR_LA.geo`
- `Bigscity-LibCity/raw_data/METR_LA/METR_LA.rel`
- `Bigscity-LibCity/raw_data/METR_LA/METR_LA.dyna`
- `Bigscity-LibCity/raw_data/METR_LA/config.json`

## 运行模型流水线

用于训练和评测一个模型的脚本`run_model.py`位于项目根目录中，它提供了一系列命令行参数，使用户可以调整运行参数配置。

当运行`run_model.py`时，您必须声明以下三个参数，分别是`task`、`dataset`和`model`。例如：

```
python run_model.py --task traffic_state_pred --model GRU --dataset METR_LA
```

这个脚本会在默认参数配置下，在METR_LA数据集上运行GRU模型，执行交通状态预测任务。

**目前我们已经在 [文档](../user_guide/data/dataset_for_task) 发布了数据集、模型和任务之间的对应关系表格供用户参考。**

此外，这个脚本还支持输入下面的这些命令行参数，用于调整流水线的参数设置。

支持的参数有：

- `task`：要执行的任务名，包括`traffic_state_pred`，`traj_loc_pred`，`eta`，`map_matching`，`road_representation`。默认为`traffic_state_pred`。
- `model`：要执行的模型名。默认为`GRU`。（[支持的模型](../user_guide/model)）
- `dataset`：要执行的数据集。默认为`METR_LA`。（[支持的数据集](../user_guide/data/raw_data.md)）
- `config_file`：用户自定义的配置文件名。默认为`None`。（[了解更多](../user_guide/config_settings.md)）
- `saved_model`：是否保存训练好的模型。默认为`True`。
- `train`：如果模型已经预训练过了，是否要重新训练模型。默认为`True`。
- `batch_size`：训练集和验证集的批次大小。
- `train_rate`：训练集在整个数据集中所占的比例。（划分的顺序是训练集、验证集、测试集）。
- `eval_rate`：验证集在整个数据集中所占的比例。
- `learning_rate`：学习率。默认值因模型而异。
- `max_epoch`：最大的训练轮数。默认值因模型而异。
- `gpu`：是否使用GPU。默认为`True`。
- `gpu_id`：使用的GPU的ID。默认为`0`。

## TensorBoard Visualization

在模型训练过程中，LibCity 会记录每个 epoch 的损失，并支持 tensorboard 可视化。

模型运行一次后，可以使用以下命令进行可视化：

```shell
tensorboard --logdir 'libcity/cache'
```

```
TensorFlow installation not found - running with reduced feature set.
Serving TensorBoard on localhost; to expose to the network, use a proxy or pass --bind_all
TensorBoard 2.4.1 at http://localhost:6006/ (Press CTRL+C to quit)
```

在浏览器中访问这个地址（http://localhost:6006/）可以看到可视化的结果。

![](/_static/tensorboard.png)

