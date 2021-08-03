# Batch

`Batch` 类是由 `DataLoader` 加载并输入到预测模型中的**内部数据表示**。

**从数据流的 `Dataloader` 取出的对象都是 `Batch` 类的对象。**

`Batch` 类是基于 `python.dict`实现的抽象数据结构。 其构成键值对结构，以特征名为键, 以特征名对应的张量(`torch.Tensor`)为值。值包含一个 `batch` 或 `mini-batch` 的全部数据.

因此，您可以使用以下方法来获得相应的值：

loc \= batch\['current\_loc'\]
tim \= batch\['current\_tim'\]

**`Batch` 类统一了模型的输入格式，框架得以实现通用的训练、预测执行器类和标准模型抽象类。**