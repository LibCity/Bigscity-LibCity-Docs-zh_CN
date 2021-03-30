Executor Introduction
======================

我们为每个任务提供一个标准的Executor，用来负责模型的训练、验证与评估。

如何你的模型不能够满足使用标准的Executor，你也可以为他设计单独的Executor。

用户可以通过修改执行器的参数设置，来调整训练的效果。

.. toctree::
   :maxdepth: 1

   executor/traffic_state_pred
   executor/traj_loc_pred

