# Traffic State Prediction Executor

本调度器类主要负责完成所有交通状态预测（交通速度、流量、需求量）模型的训练和评估过程。

## Executor Settings

下面主要介绍此调度器类所能够接收的参数：

- `max_epoch`：训练总轮数
- `epoch`：起始训练的轮数，如果大于0，会**先从'./trafficdl/cache/model_cache'加载该epoch的模型（缓存文件名为[模型名\_数据集名\_epoch+轮数.tar]）**，然后继续完成接下来的训练或评估。
- `learner`：优化器optimizer的类别，目前支持`adam`、`sgd`、`adagrad`、`rmsprop`、`sparse_adam`。
  - `learning_rate`：optimizer的参数，学习率
  - `weight_decay`：Adam optimizer的参数
  - `lr_epsilon`：Adam optimizer的参数
- `lr_decay`：是否是用lr_scheduler，**默认False**
  - `lr_scheduler`：lr_scheduler的类别，目前支持`MultiStepLR`、`StepLR`、`ExponentialLR`、`CosineAnnealingLR`、`LambdaLR`。
    - `lr_decay_ratio`：`MultiStepLR`、`StepLR`、`ExponentialLR`的参数
    - `steps`：`MultiStepLR`的参数
    - `step_size`：`StepLR`的参数
    - `lr_lambda`：`LambdaLR`的参数【**此参数需要指定为一个函数，目前基于json的配置文件不支持**】
    - `lr_T_max`：`CosineAnnealingLR`的参数
    - `lr_eta_min`：`CosineAnnealingLR`的参数
- `clip_grad_norm`：是否是用clip_grad_norm\_，**默认False**（`torch.nn.utils.clip_grad_norm_`）
  - `max_grad_norm`：clip_grad_norm_的参数
- `use_early_stop`：是否是用早停机制，**默认False**
  - `patience`：早停机制的轮数，每当验证集误差>最小验证误差，则累计1，反之则清0从头累计，累计到`patience`次就结束训练
- `log_level`：log的级别设置，默认为`INFO`，超过`INFO`级别的log都将被输出，具体参考第三方库logging
  - `log_every`：训练过程中用log记录过程的频次
- `saved_model`：是否保存训练过程中的model，**默认True**
- `gpu`：是否是用gpu训练，**默认True**
  - `gpu_id`：指定使用的gpu的id，**默认0**
  - `device*`：不能从外部指定，由参数`gpu`和`gpu_id`共同确定，在模型的代码中，使用`config['device']`即可取得，不需要使用参数`gpu`和`gpu_id`。

