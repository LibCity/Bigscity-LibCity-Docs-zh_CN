# 使用 run_model

框架的根目录中提供了用于训练和评估单个模型的脚本`run_model.py` ，并提供了一系列命令行参数，允许用户调整运行参数配置。

运行`run_model.py`时，必须指定以下三个参数，即`task`、`dataset`和`model`。也就是:

```sh
python run_model.py --task=[task_name] --model=[model_name] --dataset=[dataset_name]
```

此外，该脚本支持输入以下命令行参数来调整流水线的参数设置。

支持参数:

- `task`：要执行的任务的名称，包括`traffic_state_pred` 和`traj_loc_pred`。默认为 `traffic_state_pred`。
- `model`：要执行的模型的名称。默认为 `GRU`。([支持的模型](../model))
- `dataset`：要执行的数据集。默认为 `METR_LA`。（[支持的数据集](../data/raw_data.md)）
- `config_file`：用户定义配置文件的名称。默认为 `None`。([查看更多](../config_settings.md))
- `saved_model`：是否保存训练好的模型。默认为 `True`。
- `train`：如果模型已经过预训练，是否对模型进行再训练。默认为 `True`。
- `batch_size`：训练和评估的批次大小。
- `train_rate`：训练集占总数据集的比例。(划分顺序为训练集、验证集、测试集)
- `eval_rate`：验证集的比例。
- `learning_rate`：学习率。默认值因模型而异。
- `max_epoch`：最大训练轮次。默认值因模型而异。
- `gpu`：是否使用 GPU. 默认为 `True`。
- `gpu_id`：所使用GPU的id。默认为`0`。

