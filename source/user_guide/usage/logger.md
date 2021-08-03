# 使用 logger

本文档用于介绍如何在`LibTraffic`中使用统一的`Logger`来输出必要的辅助信息。**该logger能同时向标准输出和日志文件中输出信息。**

在入口文件`test_model.py`中，首先调用`utils.utils.get_logger()`实例化`Logger`对象。

```python
from libtraffic.utils import get_logger
logger = get_logger(config)
```

可以在想要用到`Logger`的文件中这样使用：

```python
from logging import getLogger
from libtraffic.model.abstract_model import AbstractModel

class NewModel(AbstractModel):
    def __init__(self, config, data_feature):
        self._logger = getLogger()
        
    def forward(self, batch):
        self._logger.info("hahhh")
```

