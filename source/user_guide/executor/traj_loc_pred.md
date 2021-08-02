# Trajectory Location Prediction Executor

## Executor Setting

* `gpu`：是否是用gpu训练，**默认True**
* `gpu_id`：指定使用的gpu的id，**默认0**
* `learning_rate`: 学习率，**默认0.0005**
* `L2`: torch优化器的L2范数，**默认0.00001**
* `max_epoch`: 训练最大轮数，**默认1**
* `lr_step`: torch学习率下降的轮数，即经过lr_step轮后还没改进时则下降学习率，**默认2**
* `lr_decay`: torch每次学习率下降的比例，**默认0.1**
* `clip`: 梯度裁剪中，梯度的最大范数，**默认5.0**
* `schedule_threshold`: torch scheduler的门限值，**默认0.001**
* `verbose`: 输出结果前的训练次数，**默认10**

