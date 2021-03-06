# 数据流

本文件介绍数据模块整体的数据流。

*   原始数据 Raw Data

    原始的开源数据集，针对每一种支持的原始数据集，我们提供脚本以将其转化为 [原子文件](./atomic_files.md)。

*   原子文件 Atomic Files

    不同交通预测任务的基础输入元素，用于构建 Dataset 类。

*   数据集 Dataset

    针对每一类交通预测任务制定了不同的 `Dataset` 类，负责读取原子文件并进行一些数据预处理操作。详情请参考[这里](./dataset_class.md)。

*   数据加载器 DataLoader

    `Dataloader` 负责加载数据， 使用 `Pytorch` 原生的 `torch.utils.data.DataLoader` ，负责将数据以内部数据表示结构 [Batch](./batch.md) 类的形式返回给模型使用。