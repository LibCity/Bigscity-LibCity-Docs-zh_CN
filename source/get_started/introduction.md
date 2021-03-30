## Introduction

本项目为交通大数据领域下的模型开发开源框架，目前支持以下任务：

* 交通状态预测（Traffic State Prediction）
  * 交通流量预测（Traffic Flow Prediction）
  * 交通速度预测（Traffic Speed Prediction）
  * 交通需求量预测（On-Demand Service Predition）
* 轨迹下一跳预测（Traffic Location Prediction）

#### 架构说明

本框架主要由 Config、Data、Model、Executor、Evaluator、Pipeline 六个模块构成。其中每个模块的职责如下所述：

* Config：负责统一管理参数配置。
* Data：负责加载数据集，并进行数据预处理与数据集划分。
* Model：负责具体模型的实现。
* Executor：负责运行模型，如：训练模型、模型预测。
* Evaluator：负责评估模型。
* Pipeline：将前五个模块整合起来，以流水线的方式先后执行完成用户指定的任务。

#### 流水线实例说明：运行单个模型流水线

![](/_static/pipeline.png)

1. 初始化流水线配置。用户可通过命令行传参与指定 config 文件的方式灵活地调整流水线参数配置。（依托 Config 模块）

2. 数据集加载与数据预处理，数据转换并划分训练集、验证集、测试集。（依托 Data 模块）

3. 加载模型。（依托 Model 模块）

4. 训练验证模型，并在测试集上进行测试。（依托 Executor 模块）

5. 评估模型测试输出。（依托 Evaluator 模块）

不过由于模型验证时就需要 Evaluator 来进行评估，在实际实现中，Evaluator 模块是由 Executor 模块进行实例化并调用的。

