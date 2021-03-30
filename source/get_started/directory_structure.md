# Directory Structure

框架结构

- |-raw_data/

  存放处理好的原子文件

- |-test/

  存放测试脚本

- |-trafficdl/

  项目代码根目录

  - |-config/

    定义Config类，支持 command line、config file 等方式来修改我们预设的参数，预设的参数配置文件也放置于该文件夹下，分为 data、 model、evaluate、execute 四部分。【目前只支持直接配置config文件】

  - |-data/

    包含两部分 Dataset 与 DataLoader

    |-dataset/

    ​	负责加载原子文件并进行一些数据预处理操作，切分训练集、验证集、测试集。

    ​	AbstractDataset类定义两个接口：`get_data(self)`和`get_data_feature(self)`

    ​	针对每个任务定义继承自AbstractDataset的不同的Dataset子类进行相关操作。

    |-dataloader/

    ​	负责加载数据的dataloader类，使用pytorch原生的`torch.utils.data.DataLoader`。

    |-batch.py

    ​	定义统一的内部数据结构`Batch`类，用以表示模型的输入。从dataloader中取出的都是自定义的`Batch`类的对象，结构是字典形式{key=特征名，value=tensor}。

  - |-model/

    存放模型，AbstractModel类继承自`nn.Module`，实现接口`forward(self, batch)`，模型以`Batch`对象为输入。不同任务的模型存放在不同的子文件夹下，公用的损失函数、初始化方法、常用的layer统一存放。

  - |-evaluator/

    评估模块，`AbstractEvaluator`类，定义接口`collect(self, batch)`，`evaluate(self)`，`save_result(self, save_path, filename)`，`clear(self)`。

    不同的任务定义不同的评估模块，同一任务下的模型的评估方法相同。

  - |-executor/

    执行模块，`AbstractExecutor`类，定义接口`train(self, train_dataloader, eval_dataloader)`，`evaluate(self, test_dataloader)`，`load_model(self, cache_name)`，`save_model(self, cache_name)`。

    每个任务提供一个标准Executor，模型也可以拥有自己专属的 Executor。每个 Executor 负责训练、验证与评估。

  - |-pipeline/

    开放给用户使用的流水线函数，配置config，完成整个的训练验证和评估过程。详见后边样例。

  - |cache/

    存放缓存，分为model_cache/，data_cache/，evalute_cache

  - |-tmp/

    存放训练过程中的 checkpoint 等临时性文件

  - |-utils/

    存放一些通用的工具函数

  - |-log/

    存放训练过程中的log信息