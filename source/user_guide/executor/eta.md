# 到达时间估计调度模块

本调度器类主要负责完成所有到达时间估计模型的训练和评估过程。

## 调度模块参数

下面主要介绍此调度器类所能够接收的参数：

- `max_epoch`：训练总轮数，初值由模型设定。
- `epoch`：起始训练的轮数，如果大于0，会先从`./libcity/cache/model_cache`加载该epoch的模型（缓存文件名为[模型名\_数据集名\_epoch+轮数.tar]），然后继续完成接下来的训练或评估。
- `learner`：优化器[optimizer](https://pytorch.org/docs/stable/optim.html#module-torch.optim)的类别（字符串），目前支持`adam`、`sgd`、`adagrad`、`rmsprop`、`sparse_adam`，**默认'adam'**。
  - `learning_rate`：optimizer的参数，学习率，**默认0.01**。
  - `weight_decay`：optimizer的参数，**默认0.0**。
  - `lr_epsilon`：optimizer的参数，**默认1e-8**。
  - `lr_beta1`： optimizer的参数，**默认0.9**。
  - `lr_beta2`： optimizer的参数，**默认0.999**。
  - `lr_alpha`： optimizer的参数，**默认0.99**。
  - `lr_momentum`： optimizer的参数，**默认0**。
- `lr_decay`：是否是用[lr_scheduler](https://pytorch.org/docs/stable/optim.html#how-to-adjust-learning-rate)，**默认False**。
  - `lr_scheduler`：[lr_scheduler](https://pytorch.org/docs/stable/optim.html#how-to-adjust-learning-rate)的类别，目前支持`MultiStepLR`、`StepLR`、`ExponentialLR`、`CosineAnnealingLR`、`LambdaLR`以及`ReduceLROnPlateau`。
    - `lr_decay_ratio`：`MultiStepLR`、`StepLR`、`ExponentialLR`、`ReduceLROnPlateau`的参数。
    - `steps`：`MultiStepLR`的参数。
    - `step_size`：`StepLR`的参数。
    - `lr_lambda`：`LambdaLR`的参数【**此参数需要指定为一个函数，目前基于json的配置文件不支持**】。
    - `lr_T_max`：`CosineAnnealingLR`的参数。
    - `lr_eta_min`：`CosineAnnealingLR`的参数。
    - `lr_patience`： `ReduceLROnPlateau`的参数。
    - `lr_threshold`：`ReduceLROnPlateau`的参数。
- `clip_grad_norm`：是否是用[clip_grad_norm_](https://pytorch.org/docs/stable/generated/torch.nn.utils.clip_grad_norm_.html)，**默认False**（`torch.nn.utils.clip_grad_norm_`）。
  - `max_grad_norm`：[clip_grad_norm_](https://pytorch.org/docs/stable/generated/torch.nn.utils.clip_grad_norm_.html)的参数。
- `use_early_stop`：是否是用早停机制，**默认False。**
  - `patience`：早停机制的轮数，每当验证集误差>最小验证误差，则累计1，反之则清0从头累计，累计到`patience`次就结束训练。
- `train_loss`： 训练时使用的损失函数（字符串）。目前支持`mae`、`mape`、`mse`、`rmse`、`masked_mae`、`masked_mape`、`masked_mse`、`masked_rmse`、`r2`、`evar`。
- `log_level`：log的级别设置，默认为`INFO`，超过`INFO`级别的log都将被输出，具体参考第三方库logging。
  - `log_every`：训练过程中用log记录过程的频次。
- `saved_model`：是否保存训练过程中的model，**默认True。**
- `gpu`：是否是用gpu训练，**默认True。**
  - `gpu_id`：指定使用的gpu的id，**默认0**。
  - `device*`：不能从外部指定，由参数`gpu`和`gpu_id`共同确定，在模型的代码中，使用`config['device']`即可取得，不需要使用参数`gpu`和`gpu_id`。

