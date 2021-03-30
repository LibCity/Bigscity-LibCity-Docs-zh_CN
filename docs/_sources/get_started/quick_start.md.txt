# Quick Start

#### 运行单个模型

框架根目录下提供运行单个模型的脚本 run_model.py，并提供一系列命令行参数以允许用户能够调整流水线参数配置。命令行运行示例：

```sh
python run_model.py --task traj_loc_pred --model DeepMove --dataset foursquare_tky
```

本脚本所支持的命令行参数：

- `task`：所要执行的任务名，包括`traj_loc_pred`和`traffic_state_pred`，默认为`traj_loc_pred`。
- `model`：所要运行的模型名，应是`trafficdl/model/`目录下各Model类名中的一个，默认为`DeepMove`。
- `dataset`：所要运行的数据集，默认为 `foursquare_tky`。
- `config_file`：用户指定 config 文件名，默认为 `None`，详见[配置设置](../user_guide/config_settings.md)一节。
- `saved_model`：是否保存训练的模型结果，默认为 `True`。
- `train`：当模型已被训练时是否要重新训练，默认为 `True`。
- `batch_size`：单次输入的 Batch 大小。
- `train_rate`：训练集所占比例，如`0.6`，划分顺序是【训练集，验证集，测试集】。
- `eval_rate`：验证集所占比例，如`0.2`，划分顺序是【训练集，验证集，测试集】。
- `learning_rate`：优化器的学习率。
- `max_epoch`：训练的最大轮次。
- `gpu`：是否是用GPU，默认为 `True`。
- `gpu_id`：指定使用的GPU的id，默认为`0`。

