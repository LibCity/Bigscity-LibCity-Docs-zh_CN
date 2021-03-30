# Config Settings

本框架通过三种方式确定实验的最终配置：用户命令行传参、用户自定义 config 文件、各模块默认参数配置。用户可以通过前两种方式灵活地调整实验的参数配置。

其优先级为：命令行参数>用户自定义配置文件>模型模块的默认参数>其余模块的默认参数，**高优先级的参数会覆盖低优先级的同名参数**。

## 命令行传参

当用户运行项目根目录下的脚本文件时，可以通过命令行指定修改一些参数，如：

```shell
python run_model.py --task traj_loc_pred --model DeepMove --dataset foursquare_tky --gpu false --batch_size 15
```

**具体所允许传入的参数因不同脚本而异**，可以参见 [Usage](./usage.md) 中详细的介绍了项目根目录下可执行的脚本文件，对于脚本`run_model.py`所支持的全部命令行参数如下：

- `task`：任务名，包括`traj_loc_pred`和`traffic_state_pred`
- `model`：模型名，应是`trafficdl/model/`目录下各Model类名中的一个
- `dataset`：数据集名
- `config_file`：自定义config文件名，参见下文
- `saved_model`：是否保存训练过程中的model
- `train`：如果模型被训练过，是否重新训练，**默认True**
- `batch_size`：批次大小
- `train_rate`：训练集所占比例，划分顺序是【训练集，验证集，测试集】
- `eval_rate`：验证集所占比例，划分顺序是【训练集，验证集，测试集】
- `learning_rate`：学习率
- `max_epoch`：训练总轮数
- `gpu`：是否是用GPU，**默认True**
- `gpu_id`：指定使用的GPU的id，**默认0**

也可以使用 `-h` 以获取帮助信息，例如：

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

## 自定义 config 文件

命令行允许传递的参数多为实验中常见通过的参数，如 `batch_size`。但为了使得用户能够随意修改各模块的默认参数，框架还提供通过命令行指定 config 文件名的方式，从用户自定义的配置文件中读入参数配置。用户自定义的 config 文件应满足如下格式要求：

1. 用户自定义 config 文件应为 **JSON** 文件。
2. JSON 文件中存放一个字典，其键为**参数名**，值为所要修改的**参数值**。
3. **该文件应放置在项目根目录，并通过`--config_file`的方式指定其文件名。**

示例：

```json
{
	"hidden_state_size": 50,
	"loc_embedding_size": 500
}
```

用户可以通过自定义 config 文件修改任意模块的默认参数，具体的参数名可以前往各模块的章节了解更多信息。

## 默认参数

### 模块默认参数

所有四个模块都具有默认参数，数据模块、执行模块、评估模块、模型模块的默认配置分别位于以下四个目录

- `trafficdl/config/data`
- `trafficdl/config/executor`
- `trafficdl/config/evaluator`
- `trafficdl/config/model`

每个目录下文件命名规则为`类名.json`，例如对于交通状态预测的执行模块，其默认的配置参数文件为`TrafficStateExecutor.json`。

### 数据集默认参数

数据集的默认参数位于目录`raw_data/DataSet_Name/config.json`，其具体内容请参考[原子文件](./data/atmoic_files.md) 章节。

**上述默认参数中，模型模块的优先级最高！**

### 任务默认参数

各任务的默认参数位于`trafficdl/config/task_config.json`文件中，此文件记录各类任务所能支持的全部模型和全部数据集的范围，以及各模型的以下三个参数：

- `dataset_class`：数据集类的类名，应是`trafficdl/data/dataset`目录下各Dataset类名中的一个
- `executor`：调度类的类名，应是`trafficdl/executor/`目录下各Executor类名中的一个
- `evaluator`：评估类的类名，应是`trafficdl/evaluator/`目录下各Evaluator类名中的一个

这样一来，可以完成不同模型所使用的不同Dataset类、Executor类、Evaluator类的默认配置。

**增加模型时需要修改`trafficdl/config/task_config.json`文件。**