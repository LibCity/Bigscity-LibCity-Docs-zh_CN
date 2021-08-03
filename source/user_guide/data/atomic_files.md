# Atomic Files

定义如下几种原子文件：

| 文件名      | 内容                           | 示例                                        |
| ----------- | ------------------------------ | ------------------------------------------- |
| xxx.geo     | 存储地理实体属性信息。         | geo_id, type, coordinates                   |
| xxx.usr     | 存储交通使用者信息。           | usr_id, gender, birth_date                  |
| xxx.rel     | 存储实体间的关系信息，如路网。 | rel_id, type, origin_id, destination_id     |
| xxx.dyna    | 存储交通状态信息。             | dyna_id, type, time, entity_id, location_id |
| xxx.ext     | 存储外部信息，如天气、温度等。 | ext_id, time, properties                    |
| config.json | 用于补充描述各表信息。         |                                             |

对于不同的交通预测任务，可能用到不同的原子文件，同一个数据集不一定包含全部6种原子文件。

`.geo`、`.rel`、`.dyna`、`.ext`的格式与`csv`文件类似，由多列数据构成。

## Geo 表

Geo 表中一个元素由以下四部分组成：geo_id, type, coordinates, properties(多列)。

1. geo_id: 主键，唯一确定一个 geo 实体。（传感器、经纬度点、路段、区域等的编号）
2. type：表示该 geo 的类型。一共有 “Point”、“LineString”、“Polygon” 三个值。此三值与 [Geojson](https://tools.ietf.org/html/rfc7946#section-1) 中的点线面一致。
3. coordinates：由 float 类型组成的数组或嵌套数组。描述 geo 实体的位置信息，采用 [Geojson](https://tools.ietf.org/html/rfc7946#section-1) 的 coordinates 格式。
4. properties：描述该 geo 的属性信息，若有多个属性，可以使用不同的列名定义为多列数据，如`POI_name`，`POI_type`。【对于网格数据，必有两列`row_id`和`column_id`属性表示网格的行列编号。】

> 注：Geojson的 coordinates 格式：
>
> - Point: [102.0, 0.5]
> - LineString: [ [102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0] ]
> - Polygon:  [[ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ]]

## Usr 表

Usr 表中一个元素由以下两部分组成：usr_id, properties(多列)。

1. usr_id：主键，唯一确定一个 usr 实体。

2. properties：描述该 usr 实体的属性信息，若有多个属性，可以使用不同的列名定义为多列数据，如 `gender`，`birth_date`。

## Rel 表

Rel 表中一个元素由以下四个部分组成：rel_id, type, origin_id, destination_id, properties(多列)。

1. rel_id：主键，唯一确定一个实体间的关系。
2. type：枚举类。一共有两种取值`usr`，`geo`。表示该关系是基于 `geo` 的还是基于 `usr` 的。
3. origin_id：关系起点方的 ID，为 Geo 表或 Usr 表中的一个。
4. destination_id：关系终点方的 ID，为 Geo 表或 Usr 表中的一个。
5. properties：描述该关系所具有的属性信息，如 `link_weight`可以表示邻接矩阵权重，若有多个属性，可以使用不同的列名定义为多列数据。

## Dyna 表

Dyna 表中一个元素由以下五部分组成：dyna_id, type, time, entity_id, properties(多列)。

- dyna_id：主键，唯一标识动态表中的一条记录。

- type：枚举类，一共有两种取值 `trajectory`（轨迹预测任务）、`state`（状态预测任务）。

- time：时间信息，采用 [ISO-8601标准](https://www.iso.org/iso-8601-date-and-time-format.html) 中的日期和时间的组合表示法，如：`2020-12-07T02:59:46Z`。

- entity_id：描述该记录是基于哪一个实体观测产生的，就是`geo`或者`usr`的编号。

   - 对于轨迹预测任务：

     格式为：dyna_id, trajectory, time, entity_id, location。其中**entity_id**列的内容应该是**usr_id**。

   - 对于状态预测任务：**entity_id**可能有不同的变化：

     对于传感器、路段、区域等实体来讲此列就是对应的编号，列名为**[entity_id]**，文件后缀名`.dyna`；

     对于网格结构的交通数据，列名为**[row_id, column_id]**，文件后缀名`.grid`；

     对于基于`od`结构的交通数据，列名为**[origin_id, destination_id]**，文件后缀名`.od`；

     对于网格结合`od`结构的交通数据，列名为**[origin_row_id, origin_column_id, destination_row_id, destination_column_id]**，文件后缀名`.gridod`；

- properties：描述该条记录的属性信息，若有多个属性，可以使用不同的列名定义为多列数据，比如既有速度数据、又有流量数据。

## Ext 表

Ext 表中一个元素由以下五部分组成：ext_id, time, properties(多列)。

1. ext_id：主键，唯一标识外部数据表中的一条记录。
2. time：时间信息，采用 [ISO-8601标准](https://www.iso.org/iso-8601-date-and-time-format.html) 中的日期和时间的组合表示法，如：`2020-12-07T02:59:46Z`。
3. properties：描述该条记录的属性信息，若有多个属性，可以使用不同的列名定义为多列数据，比如既有温度数据、又有湿度数据。

## 数据类型定义

需要在 config 文件中给出数据集中各列的数据类型定义，有助于后续的数据处理。

| 类型       | 说明                                  |
| ---------- | ------------------------------------- |
| geo_id     | 存在于 geo 表中的离散的有限的 ID      |
| usr_id     | 存在于 usr 表中的离散的有限的 ID      |
| rel_id     | 存在于 rel 表中的离散的有限的 ID      |
| time       | 符合 ISO-8601 标准的时间字符串        |
| coordinate | 符合 geojosn 格式的坐标表示法的字符串 |
| num        | 实数类                                |
| enum       | 枚举类字符串                          |
| other      | 其余的均以字符串类型存储              |

## Config 文件

 Config 文件用以补充描述上述四个表自身的信息，即各个表的 properties 字段具体含有的哪些属性。以 json 的格式存储，且由 `geo`、`usr`、`rel`、`dyna`、`ext`、`info` 六个键组成。

- 对于`geo`、`rel`、`dyna`、`ext`：

  包含一个 `including_types` 的键，以数组的形式描述该表中所具有的 `type` 值。其后每个 `type` 作为键，描述该 `type` 下 `properties` 具有哪些键以及其数据类型（`dyna` 表需要额外把 `entity_id` 也加以说明）。

- 对于`usr`：

  包含一个 `properties` 键，描述表中 `properties` 包含哪些键以及其数据类型。

- 对于`info`：

  **包含其他必要的数据集统计信息**，针对不同的交通预测任务，包含有不同的内容。

  - 交通状态预测任务包含的相关信息如下：
    - `geo_file`：`.geo`文件的文件名，**字符串类型**，默认为数据集名。
    - `rel_file`：`.rel`文件的文件名，**字符串类型**，默认为数据集名。
    - `data_files`：数据文件的文件名（例如`.dyna`、`.grid`、`.gridod`），**支持数组或字符串**，默认为数据集名。
    - `ext_file`：`.ext`文件的文件名，**字符串类型**，默认为数据集名。
    - `weight_col`：从`.rel`文件中加载的列名，**支持只有一个元素的字符串数组或字符串**，不指定的话如果`.rel`文件只有一列权重列，则没有问题，否则报错。
    - `data_col`：从数据文件`.dyna/.grid/.od/.gridod`中加载的列名，**支持数组或字符串**，不指定则全部加载。
    - `ext_col`：从`.ext`文件中加载的列名，**支持数组或字符串**，不指定则全部加载。
    - `output_dim`：指定模型输出的维度，**一般应该跟`data_col`中指定的属性列名的数量相同**。
    - `init_weight_inf_or_zero`：支持`inf`和`zero`，加载`.rel`文件构建邻接矩阵时，初始化邻接矩阵为全INF(`inf`)还是全0(`zero`)，默认为`inf`。
    - `set_weight_link_or_dist`：支持`link`和`dist`，加载`.rel`文件构建邻接矩阵时，使用文件中权重列中的原始值(`dist`)，还是将之修订为全01的矩阵(`link`)，默认为`dist`。【如果`.rel`文件中只有相连的关系，没有不相连的关系，应该指定为`link`】
    - `calculate_weight_adj`：从`.rel`文件获取的邻接矩阵的权重是否需要进一步进行计算，**默认False**，部分邻接矩阵在原始数据的基础上，进行了一些计算。目前的计算方法是带有阈值的高斯核方法：$$  w_{ij} = \exp \left(- \frac{d_{ij}^{2}}{\sigma^{2}}\right)$$，$\sigma$ 是方差。
    - `weight_adj_epsilon`：高斯核的阈值，经过计算的权重如果小于该阈值，则变成0，即 $$  w_{ij}[w_{ij}<\epsilon]=0​$$，此参数依赖于参数`calculate_weight_adj=True`。
  - 轨迹下一跳预测任务包含的相关信息如下：

样例如下：

```json
{
    "geo":{
        "including_types":[
            "Point"
        ],
        "Point":{
            "poi_name":"other",
        }
    },
    "usr":{
        "properties":{
            "user_type":"enum",
            "birth_year":"time",
            "gender":"enum"
        }
    },
    "rel":{
        "including_types":[
            "geo"
        ],
        "geo":{
            "link_weight":"num"
        }
    },
    "dyna":{
        "including_types":[
            "state"
        ],
        "state":{
            "entity_id":"geo_id",
            "traffic_speed":"num"
        }
    },
    "grid":{
        "including_types":[
            "state"
        ],
        "state":{
            "row_id": 15,
            "column_id": 5,
            "traffic_speed":"num"
        }
    },
    "od":{
        "including_types":[
            "state"
        ],
        "state":{
            "origin_id":"geo_id",
            "destination_id":"geo_id",
            "traffic_speed":"num"
        }
    },
    "gridod":{
        "including_types":[
            "state"
        ],
        "state":{
            "origin_row_id": 15,
            "origin_column_id": 5,
            "destination_row_id": 15,
            "destination_column_id": 5,
            "traffic_speed":"num"
        }
    },
    "info": {
        "data_col": [
          "inflow",
          "outflow"
        ],
        "ext_col": [
          "Temperature"
        ],
        "data_files": [
          "TAXIBJ2013"
        ],
        "geo_file": "TAXIBJ",
        "ext_file": "TAXIBJ",
        "output_dim": 2,
        "init_weight_inf_or_zero": "inf",
        "set_weight_link_or_dist": "dist",
        "calculate_weight_adj": false,
        "weight_adj_epsilon": 0.1
  	}
}
```