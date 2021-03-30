# Batch

`Batch`类是由`DataLoader`加载并输入到预测模型中的**内部数据表示形式**。

**从数据流的`Dataloader`中取出的对象都是`Batch`类的对象。**

`Batch`类是基于`python.dict`实现的抽象数据结构，其构成`key-value`的结构，其中`key`是模型输入的特征名，`value`是对应特征的张量（`torch.Tensor`），其包含一个`batch`或`mini-batch`的全部数据。

所以可以使用如下的方式来获取相应的值：

```python
loc = batch['current_loc']
tim = batch['current_tim']
```

**`Batch`类的存在，统一了模型的输入格式，框架得以实现通用的训练、预测执行器类和标准模型抽象类。**

