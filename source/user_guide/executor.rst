调度器简介
==========

我们为每个任务提供一个标准的调度器，负责模型的训练、验证和评估，用户可以通过修改执行器的参数设置来调整训练的效果。

如果您的模型对现有的标准 Executor 不满意，您还可以为其设计一个新的 Executor，详情请参考 :doc:`../developer_guide/implemented_executors`。

.. toctree::
   :maxdepth: 1

   executor/traffic_state_pred
   executor/traj_loc_pred

