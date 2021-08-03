# Parameter Tuning

与训练和评估模型相似，LibTraffic向研究者提供了一个脚本`hyper_tune.py`来自动搜索超参数。这个脚本是基于第三方开源库[Ray Tune](https://docs.ray.io/en/master/tune/index.html)的实现。

与`run_model.py`相同，`hyper_tune.py` 也提供了一系列命令行参数，允许使用者来调整实验配置。除了`run_model.py`提供的命令行指令参数，`hyper_tune.py`也支持了下列独有参数。

- `space_file`: 指定超参数搜索空间的配置文件，默认为`None`

- `scheduler`: 将在`ray.tune.run` 中使用的试验调度器， 默认值为 `FIFO`，目前, LibTraffic 支持 `FIFO`, `ASHA`,`MedianStoppingRule` (试验是从搜索空间中采样一次接着进行训练和评估）

- `search_alg`: 将被用在 `ray.tune.run`的搜索算法，默认值为 `BasicSearch`. 目前， LibTraffic支持 `BasicSearch`, `BayesOptSearch`, `HyperOpt`。 LibTraffic 将使用损失函数作为搜索指标。

- `num_samples`: 从超参数空间的取样次数，默认值为5

- `max_concurrent`: 同时运行试验的最大数，默认值为1

- `cpu_per_trial`: 每次试验所分配的cpu数量，默认值为1

- `gpu_per_trial`: 每次试验所分配的gpu数量，默认值为1

     `task, model, dataset, space_file` 这三个参数必须在命令行中指定。例如，你可以按照下方格式运行超参数调整
     
    ```shell
    python hyper_tune.py --task [task_name] --model=[model_name] --dataset=[dataset_name] --space_file=[file_name]
    ```
    
    

#### 空间文件

空间文件应该使用JSON文件格式储存。空间文件的内容是一个字典，其键为参数名，其值为空间描述变量。

空间描述变量由空间类型和该类型对应的约束参数组成。支持的空间类型及其对应的约束参数如下：

* `uniform`: 

    取样空间是均匀分布的实数空间

    * `lower`: 均匀分布的下限
    * `upper`: 均匀分布的上限

* `randn`: 取样空间是正态分布的实数空间

    * `mean`: 正态分布的数学期望。
    * `sd`: 正态分布的标准差。

* `randint`: 取样空间是均匀分布的整数空间

    * `lower`: 均匀分布的下限(inclusive)
    * `upper`: 均匀分布的上限 (exclusive)

* `choice`: 搜索空间是一组离散的分类变量的集合，超参数将从集合中随机选择。

    * `list`: 离散的分类变量的集合

* `grid_search`: 搜索空间是离散的分类变量。参数选择将采取网格搜索的方法，遍历所有可能的组合。

    * `list`: 离散的分类变量的集合

一个空间文件的例子如下:

```json
{
  "beta": {
    "type": "uniform",
    "lower": 0.1,
    "upper": 10.0
  },
  "learning_rate": {
    "type": "choice",
    "list": [0.01, 0.005, 0.001]
  }
}
```

