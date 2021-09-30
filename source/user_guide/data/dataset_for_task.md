# 数据集适用的任务

In this section, we introduce to you the correspondence between our provided [standard datasets](https://drive.google.com/drive/folders/1g5v2Gq1tkOq8XO0HDCZ9nOTtRpB6-gPe?usp=sharing) and tasks. It is worth noting that some datasets can only support some models in a certain task.

在本节中，我们向您介绍我们提供的[标准数据集](https://drive.google.com/drive/folders/1g5v2Gq1tkOq8XO0HDCZ9nOTtRpB6-gPe?usp=sharing) 和任务之间的对应关系。 值得注意的是，某些数据集只能支持某个任务中的某些模型。

| 任务           | 数据集                                                       | 支持的模型                                                   | 备注                                                         |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 交通流量预测   | **TAXIBJ**, PORTO, NYCTAXI_GRID, NYCBIKE, AUSTINRIDE, BIKEDC, BIKECHI, **NYCBike20140409**, **NYCBike20160708**, **NYCBike20160809**, **NYCTaxi20140112**, **NYCTaxi20150103**, **NYCTaxi20160102**, **T_DRIVE20150206**, T_DRIVE_SMALL | ACFM, STResNet, DSAN, ACFMCommon, STResNetCommon             | 基于网格的数据                                               |
|                | **PEMSD3**, **PeMSD4**, **PeMSD7**, **PeMSD8**, BEIJING_SUBWAY, M_DENSE, SHMETRO, HZMETRO, NYCTAXI_DYNA | AGCRN, ASTGCNCommon, MSTGCNCommon, STSGCN, CONVGCNCommon, ToGCN, MultiSTGCnetCommon, STNN, ASTGCN, MSTGCN, CONVGCN, DGCN, ResLSTM, MultiSTGCnet | 基于传感器点的数据                                           |
|                | **TAXIBJ**, PORTO, NYCTAXI_GRID, NYCBIKE, AUSTINRIDE, BIKEDC, BIKECHI, **NYCBike20140409**, **NYCBike20160708**, **NYCBike20160809**, **NYCTaxi20140112**, **NYCTaxi20150103**, **NYCTaxi20160102**, **T_DRIVE20150206**, T_DRIVE_SMALL | AGCRN, ASTGCNCommon, MSTGCNCommon, STSGCN, CONVGCNCommon, ToGCN, MultiSTGCnetCommon, STNN, ASTGCN, MSTGCN, CONVGCN, DGCN, ResLSTM, MultiSTGCnet | 需要简单的修改以用于网格数据， **见 Note 3.**                |
|                | **M_DENSE**                                                  | CRANN                                                        | 需要`.ext` 文件                                              |
|                | **NYCBike20160708**, **NYCTaxi20150103**                     | STDN                                                         | 需要`.gridod` 文件                                           |
| 交通速度预测   | **METR_LA**, **LOS_LOOP**, **PeMSD4**, **PeMSD8**, **PEMSD7(M)**, **PEMS_BAY**, LOS_LOOP_SMALL, SZ_TAXI, LOOP_SEATTLE, Q_TRAFFIC, ROTTERDAM | DCRNN, STGCN, GWNET, MTGNN, STMGAT, TGCN, ATDM, HGCN, DKFN, STTN, GTS, GMAN, STAGGCN, TGCLSTM | 基于传感器点的数据                                           |
|                | **LOOP_SEATTLE**                                             | TGCLSTM                                                      | **见Note 2.**                                                |
| 交通需求预测   | **TAXIBJ**, PORTO, NYCTAXI_GRID, NYCBIKE, AUSTINRIDE, BIKEDC, BIKECHI, **NYCBike20140409**, **NYCBike20160708**, **NYCBike20160809**, **NYCTaxi20140112**, **NYCTaxi20150103**, **NYCTaxi20160102**, **T_DRIVE20150206**, T_DRIVE_SMALL | DMVSTNet                                                     | 基于网格的数据                                               |
|                | **PEMSD3**, **PeMSD4**, **PeMSD7**, **PeMSD8**, BEIJING_SUBWAY, M_DENSE, SHMETRO, HZMETRO, NYCTAXI_DYNA | CCRNN, STG2Seq                                               | 基于传感器点的数据                                           |
|                | **TAXIBJ**, PORTO, NYCTAXI_GRID, NYCBIKE, AUSTINRIDE, BIKEDC, BIKECHI, **NYCBike20140409**, **NYCBike20160708**, **NYCBike20160809**, **NYCTaxi20140112**, **NYCTaxi20150103**, **NYCTaxi20160102**, **T_DRIVE20150206**, T_DRIVE_SMALL | CCRNN, STG2Seq                                               | Need **simple modification**   for grid based dataset. **See Note 3.** |
| OD矩阵预测     | **NYCTAXI_OD**                                               | GEML                                                         | 基于OD的数据                                                 |
| 轨迹下一跳预测 | **Gowalla**, BrightKite                                      | FPMC, RNN, ST-RNN, ATST-LSTM, DeepMove, HST-LSTM, LSTPM, STAN | 轨迹数据                                                     |
|                | **Fousquare**, Instagram                                     | FPMC, RNN, ST-RNN, ATST-LSTM, DeepMove, HST-LSTM, LSTPM, GeoSAN, STAN, SERM, CARA | 轨迹数据                                                     |
| 路网匹配       | **Seattle**, global                                          | STMatching, IVMM                                             | 轨迹数据                                                     |

## Note

1.加粗的数据集是我们推荐的数据集。

2.对于`TGCLSTM`，需要将`dataset_class`设置为`TrafficStatePointDataset`。 否则，默认的`dataset_class=TGCLSTMDataset` 只适用于数据集`LOOP_SEATTLE`。

3.以下是如何将用于基于点的数据的模型泛化为基于网格的数据。

（1）如果模型使用的数据集类是`TrafficStatePointDataset`，如`AGCRN`、`ASTGCNCommon`、`CCRNN`等，可以直接在`task_file.json`中将`dataset_class`设为`TrafficStateGridDataset`或通过自定义配置文件（`--config_file`）设置。 然后将 `TrafficStateGridDataset` 的参数 `use_row_column` 设置为 `False`。

（2）如果模型使用的数据集类是`TrafficStatePointDataset`的子类，如`ASTGCNDataset`、`CONVGCNDataset`、`STG2SeqDataset`等，可以修改数据集类的文件，使其继承`TrafficStateGridDataset` 取代当前的`TrafficStatePointDataset`。 然后将函数`__init__()`中的参数`use_row_column`设置为`False`。

样例：

修改前：

```python
from libcity.data.dataset import TrafficStatePointDataset
class STG2SeqDataset(TrafficStatePointDataset):
    def __init__(self, config):
        super().__init__(config)
        pass
```

修改后：

```python
from libcity.data.dataset import TrafficStateGridDataset
class STG2SeqDataset(TrafficStateGridDataset):
    def __init__(self, config):
        super().__init__(config)
        self.use_row_column = False
        pass
```

