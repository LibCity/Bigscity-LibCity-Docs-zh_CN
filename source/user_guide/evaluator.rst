Evaluator Introduction
==========================

Considering the different output formats of models for different tasks, the framework implements different evaluators for different tasks and supports a variety of mainstream evaluation methods. The evaluation methods supported by different tasks are given below.

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
