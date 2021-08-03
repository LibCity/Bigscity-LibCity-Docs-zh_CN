# 参数设置

实验参数配置由三方面决定：命令行传入的参数、用户定义的配置文件和框架默认的配置文件。由此，用户可以灵活地通过前两种方式调整实验的参数配置。

### 参数优先级

命令行参数>用户定义配置文件>模型所在模块默认参数>其它模块默认参数

**高优先级的参数会覆盖低优先级的同名参数。**

考虑到不同模型的最优训练参数并不一致，执行器默认训练参数也只能是固定值，我们做了将模型的最优训练参数存放在其默认配置文件、模型所在模块默认参数的优先级高于其它模块这两个决定，来解决该问题。

### 命令行参数

当用户在项目根目录运行脚本文件时，有些参数可以在命令行指定并修改。例如：

```shell
python run_model.py --task traj_loc_pred --model DeepMove --dataset foursquare_tky --gpu false --batch_size 15
```

不同的脚本文件允许传递不同的参数。更多细节参见[用法](./usage/run_model.md)。

也可使用`-h`选项得到帮助信息。例如：

```sh
> python run_model.py -h
usage: run_model.py [-h] [--task TASK] [--model MODEL] [--dataset DATASET]
                    [--config_file CONFIG_FILE] [--saved_model SAVED_MODEL]
                    [--train TRAIN] [--gpu GPU] [--batch_size BATCH_SIZE]
                    [--train_rate TRAIN_RATE] [--eval_rate EVAL_RATE]
                    [--learning_rate LEARNING_RATE] [--max_epoch MAX_EPOCH]
                    [--gpu_id GPU_ID]

optional arguments:
  -h, --help            show this help message and exit
  --task TASK           the name of task
  --model MODEL         the name of model
  --dataset DATASET     the name of dataset
  --config_file CONFIG_FILE
                        the file name of config file
  --saved_model SAVED_MODEL
                        whether save the trained model
  --train TRAIN         whether re-train model if the model is trained before
  --gpu GPU
  --batch_size BATCH_SIZE
  --train_rate TRAIN_RATE
  --eval_rate EVAL_RATE
  --learning_rate LEARNING_RATE
  --max_epoch MAX_EPOCH
  --gpu_id GPU_ID
```

### 用户定义配置文件

大多数命令行接受的参数是实验中经常传入的参数，比如`batch_size`。进一步来说，为了让用户能自如地修改各模块默认参数，本框架允许用户在命令行中传入用户定义配置文件的文件名，然后从该文件中读入参数配置。该文件应满足以下格式要求：

1. 用户定义配置文件应为**JSON**格式。
2. 该JSON文件应存储一个字典，其中键为**参数名**，值为应修改的**参数值**。
3. 文件应存放在**项目根目录**，文件名应由`--config_file`命令行参数指定。

例如：

```json
{
	"hidden_state_size": 50,
	"loc_embedding_size": 500
}
```

用户可通过自定义配置文件修改任何模块的默认配置。对修改具体的参数名而言，可参见每个模块的用户手册以获取更多信息。

### 默认配置

#### 模块默认配置

数据模块、执行器模块、评估模块和模型所在模块的配置分别位于以下目录中：

- `/libtraffic/config/data`
- `/libtraffic/config/executor`
- `/libtraffic/config/evaluator`
- `/libtraffic/config/model`

各目录中文件命名规则均为`类名.json`。例如，对交通状态预测的执行模块而言，默认参数文件名为`TrafficStateExecutor.json`。

#### 数据集配置文件

我们在数据集配置文件中存储了一些辅助信息，其存储路径为`/raw_data/数据集名字/config.json`。参见[原子文件](./data/atomic_files.md)一节获取更多信息。

#### 任务配置文件

任务配置文件用来记录各任务支持的模型与数据集列表，以及其下各模型默认的数据模块、执行器模块和评估模块类名，它们的存储路径为`/libtraffic/config/task_config.json`。

此处为任务配置文件一例：
```json
{
  "traffic_state_pred": {
    "allowed_model": ["DCRNN"],
    "allowed_dataset": ["METR_LA", "PEMS_BAY", "PEMSD3"],
    "DCRNN": {
        "dataset_class": "TrafficStatePointDataset",
        "executor": "DCRNNExecutor",
        "evaluator": "TrafficStateEvaluator"
    },
}
```

**增加新模块时，需要修改`libtraffic/config/task_config.json`。**

由以上配置文件，`DCRNN`使用的数据模块类为`TrafficStatePointDataset`，执行器模块为`DCRNNExecutor`，评估模块类为`TrafficStateEvaluator`。
