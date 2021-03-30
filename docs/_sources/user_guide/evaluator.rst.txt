Evaluator Introduction
==========================

考虑到不同的任务的模型输出格式不同。因此对于不同的任务，框架实现了不同的评估器，并支持多种主流评估方法。下面给出不同任务所支持的评估方法。

============================== ==============================
Task Name                      Supported Metrics
============================== ==============================
Trajectory Location prediction TopK
Traffic Flow Prediction        MAE、MSE、RMSE、MAPE、R2、EVAR
Traffic Speed Prediction       MAE、MSE、RMSE、MAPE、R2、EVAR
On-Demand Service predition    MAE、MSE、RMSE、MAPE、R2、EVAR
============================== ==============================

.. toctree::
   :maxdepth: 1

   evaluator/traffic_state_pred
   evaluator/traj_loc_pred
