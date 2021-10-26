# 原子文件可视化

下面，我们将介绍如何借助`LibCity`中的`VisHelper`对 [原子文件](../user_guide/data/atomic_files.md) 进行可视化。

## 准备原子文件

首先，只需将原子文件放在 `./raw_data` 文件夹，这与运行模型的准备工作相同。如果你不知道从哪里获取数据集，点击 [此处](./run_model.md) 获得更多信息。

## 运行可视化脚本

为简化用户操作，只有两个参数需要用户指定：

* `dataset`：数据集的名称
* `save_path`：可视化文件的保存目录，默认为`"./visualized_data/"`

脚本将自动检测`dataset`文件夹下的 `geo` 和 `dyna` 文件并将他们转化为[GeoJSON](https://geojson.org/)文件。 (**对于所有数据集，请确保 (1)`geo` 文件只有一个(2) 至少有一个文件具有`coordiantes`**。)

比如，你想使用**Seattle**数据集可视化路网匹配任务，你可以使用下面的命令

```shell
python visualize.py --dataset Seattle --save_path "./visualized_data"
```

以实现数据的类型转化。

`grid`类型数据集和`state`类型数据集可以通过相同的方式进行转化。 **注意：在`grid`类型数据集和`state`类型数据集中，`properties` (如`inflow` 和`outflow`) 是在所有时间上取平均得到的。**

## 可视化GeoJSON

[GeoJSON](https://geojson.org/) 是一种用于编码各种地理数据结构的格式，被大多数GIS工具所支持。在此，我们展示了我们使用[QGIS](https://www.qgis.org/en/site/)对**Seattle**数据集的可视化结果。

图中，红色线条代表**Seattle**的路网。黄色线条代表**Seattle**数据集中的GPS轨迹。

![](/_static/data_visualization1.png)

![](/_static/data_visualization2.png)

我们还展示了我们对交通速度数据集**METR_LA**的热图可视化。

![](/_static/data_visualization3.png)

