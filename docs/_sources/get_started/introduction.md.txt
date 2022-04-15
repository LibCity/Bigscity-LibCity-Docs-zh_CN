![](/_static/logo.png)

## 介绍

[主页](https://libcity.ai/)|[文档](https://bigscity-libcity-docs.readthedocs.io/zh_CN/latest/#)|[数据集](https://github.com/LibCity/Bigscity-LibCity-Datasets)|[论文列表](https://github.com/LibCity/Bigscity-LibCity-Paper)

LibCity 是一个统一、全面、可扩展的代码库，为交通预测领域的研究人员提供了一个可靠的实验工具和便捷的开发框架。 我们的库基于 PyTorch 实现，并将与交通预测相关的所有必要步骤或组件包含到系统的流水线中，使研究人员能够进行全面的对比实验。 我们的库将有助于交通预测领域的标准化和可复现性。

LibCity 目前支持以下任务：

* 交通状态预测
  * 交通流量预测
  * 交通速度预测
  * 交通需求预测
  * 起点-终点（OD）矩阵预测
  * 交通事故预测
* 轨迹下一跳预测
* 到达时间预测
* 路网匹配
* 路网表征学习

#### 特性

* **统一性**：LibCity 构建了一个系统的流水线以在一个统一的平台上实现、使用和评估交通预测模型。 我们设计了统一的时空数据存储格式、统一的模型实例化接口和标准的模型评估程序。
* **全面性**：复现覆盖 9 个交通预测任务的 60 个模型，形成了全面的模型库。 同时，LibCity 收集了 35 个不同来源的常用数据集，并实现了一系列常用的性能评估指标和策略。

* **可扩展性**：LibCity 实现了不同组件的模块化设计，允许用户灵活地加入自定义组件。 因此，新的研究人员可以在 LibCity 的支持下轻松开发新模型。

#### 总体框架

![](/_static/framework.png)

* **Configuration Module**：负责管理框架中涉及的所有参数。
* **Data Module**：负责加载数据集和数据预处理操作。
* **Model Module**：负责初始化基线模型或自定义模型。
* **Evaluation Module**：负责通过多个指标评估模型预测结果。
* **Execution Module**：负责模型训练和预测。

#### 引用

该工作已被ACM SIGSPATIAL 2021接收。如果您认为LibCity对您的科研工作有帮助，请引用我们的[论文](https://dl.acm.org/doi/10.1145/3474717.3483923)。

```
@inproceedings{10.1145/3474717.3483923,
  author = {Wang, Jingyuan and Jiang, Jiawei and Jiang, Wenjun and Li, Chao and Zhao, Wayne Xin},
  title = {LibCity: An Open Library for Traffic Prediction},
  year = {2021},
  isbn = {9781450386647},
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  url = {https://doi.org/10.1145/3474717.3483923},
  doi = {10.1145/3474717.3483923},
  booktitle = {Proceedings of the 29th International Conference on Advances in Geographic Information Systems},
  pages = {145–148},
  numpages = {4},
  keywords = {Spatial-temporal System, Reproducibility, Traffic Prediction},
  location = {Beijing, China},
  series = {SIGSPATIAL '21}
}
```

```
Jingyuan Wang, Jiawei Jiang, Wenjun Jiang, Chao Li, and Wayne Xin Zhao. 2021. LibCity: An Open Library for Traffic Prediction. In Proceedings of the 29th International Conference on Advances in Geographic Information Systems (SIGSPATIAL '21). Association for Computing Machinery, New York, NY, USA, 145–148. DOI:https://doi.org/10.1145/3474717.3483923
```

LibCity 主要由北航智慧城市兴趣小组 ([BIGSCITY](https://www.bigcity.ai/)) 开发和维护。 该库的核心开发人员是 [@aptx1231](https://github.com/aptx1231) 和 [@WenMellors](https://github.com/WenMellors)。

如果您遇到错误或有任何建议，请通过 [提交issue](https://github.com/LibCity/Bigscity-LibCity/issues) 的方式与我们联系。您也可以通过发送邮件的方式联系我们，邮箱为bigscity@126.com。
