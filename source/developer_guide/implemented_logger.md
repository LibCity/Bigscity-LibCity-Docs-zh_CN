# Logger

本文档用于介绍如何在`TrafficDL`中使用统一的`Logger`。

首先在入口文件`test_moel.py`中调用`utils.utils.get_logger()`以实例化`Logger`对象。

```python
from trafficdl.utils import get_logger
logger = get_logger(config)
```

在想要使用`Logger`的文件中`from logging import getLogger`，之后`self.logger=getLogger()`即可。

例如在`newmodel.py`中

```python
from logging import getLogger
from trafficdl.model.abstract_model import AbstractModel

class NewModel(AbstractModel):
    def __init__(self, config, data_feature):
        self._logger = getLogger()
        
    def forward(self, batch):
        self._logger.info("hahhh")
```

使用方法：

`self._logger.info()`传入一个字符串即可。

