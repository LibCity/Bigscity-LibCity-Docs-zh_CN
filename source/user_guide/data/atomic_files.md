# 原子文件

定义如下几种原子文件：

| 文件名      | 内容                           | 示例                                        |
| ----------- | ------------------------------ | ------------------------------------------- |
| xxx.geo     | 存储地理实体属性信息。         | geo_id, type, coordinates                   |
| xxx.usr     | 存储交通使用者信息。           | usr_id, gender, birth_date                  |
| xxx.rel     | 存储实体间的关系信息，如路网。 | rel_id, type, origin_id, destination_id     |
| xxx.dyna    | 存储交通状态信息。             | dyna_id, type, time, entity_id, location_id |
| xxx.ext     | 存储外部信息，如天气、温度等。 | ext_id, time, properties                    |
| config.json | 用于补充描述各表信息。         |                                             |

注：对于不同的交通预测任务，可能用到不同的原子文件，同一个数据集不一定包含全部六种原子文件。

**`.geo`、`.usr`、 `.rel`、 `.dyna` 和 `.ext` 的格式类似 `csv` 文件， 即含有多列数据。**

如果在处理成原子文件的过程中，对任意一种id进行了重映射，**我们推荐从0开始编号**！

## Geo 表

Geo 表中一个元素由以下四部分组成：

**geo\_id、 type、 coordinates、 properties （多列）**。

*  geo\_id： 主键，唯一确定一个 geo 实体。 （如传感器， 经纬度点， 路段， 区域等的编号)
*  type： 表示该 geo 的类型。有 \[`Point`, `LineString`, `Polygon`\] 三种值。 这三种取值与 [Geojson](https://tools.ietf.org/html/rfc7946#section-1) 中的点线面一致。
*  coordinates：由 float 类型组成的数组或嵌套数组。 描述 geo 实体的位置信息，采用 [Geojson](https://tools.ietf.org/html/rfc7946#section-1) 的 coordinates 格式
*  properties： 描述该 geo 的属性信息，若有多个属性，可以使用不同的列名定义为多列数据，如 `POI_name`， `POI_type`。 （**对于网格数据，必有两列 `row_id` 和 `column_id` 属性表示网格的行列编号**。）


> 注： Geojson 的 coordinates 格式为： (**经度, 纬度**)
>
> *   Point： \[102.0, 0.5\]
>
> *   LineString： \[ \[102.0, 0.0\], \[103.0, 1.0\], \[104.0, 0.0\], \[105.0, 1.0\] \]
>
> *   Polygon： \[\[ \[100.0, 0.0\], \[101.0, 0.0\], \[101.0, 1.0\], \[100.0, 1.0\], \[100.0, 0.0\] \]\]

## Usr 表

Usr 表中一个元素由以下两部分组成：

**usr\_id， properties （多列）**。

*   usr\_id： 主键，唯一确定一个 usr 实体。

*   properties： 描述该 usr 实体的属性信息，若有多个属性，可以使用不同的列名定义为多列数据，如 `gender`，`birth_date`。


## Rel 表

Rel 表中一个元素由以下四个部分组成：

**rel\_id、 type、 origin\_id、 destination\_id、 properties（多列）**。

*   rel\_id： 主键，唯一确定一个实体间的关系。

*   type： 枚举类。取值为 \[`usr`，`geo`\]，表示该关系是基于 `geo` 还是 `usr`。

*   origin\_id： 关系起点方的 ID，为 Geo 表或 Usr 表中的一个。

*   destination\_id： 关系终点方的 ID，为 Geo 表或 Usr 表中的一个。

*   properties： 描述该关系所具有的属性信息。若有多个属性，可以使用不同的列名定义多列数据。


## Dyna 表

Dyna 表中一个元素由以下五部分组成：

**dyna\_id、 type、 time、 entity\_id（多列）、 properties（多列）**。

### 各列介绍

*   dyna\_id： 主键，唯一标识动态表中的一条记录。
*   type： 枚举类。一共有两种取值： `trajectory`（轨迹预测任务） 和 `state`（状态预测任务）。
*   time： 时间信息，采用 [ISO-8601 标准](https://www.iso.org/iso-8601-date-and-time-format.html) 中的日期时间组合表示法， 如： `2020-12-07T02:59:46Z`。
*   entity\_id： 描述该记录是基于哪一个实体观测产生的，就是 `geo` 或 `usr`的编号。
*   properties： 描述该条记录的属性信息，若有多个属性，可以使用不同的列名定义为多列数据，比如既有速度数据、又有流量数据。

### 详细说明

*   对于交通状态预测任务：
    *   格式为：*dyna\_id, state, time, entity\_id, properties*，**entity\_id** 可能有不同变化。
    *   对于传感器、路段、区域等实体来讲此列就是对应的编号， entity\_id 的列名为 \[**entity\_id**\]， 文件后缀名为 `.dyna`。
    *   对于网格结构的交通数据，entity\_id 变成2列，列名为 \[**row\_id, column\_id**\]，文件后缀名为 `.grid`。
    *   对于基于OD结构的交通数据，entity\_id 变成2列，列名为 \[**origin\_id, destination\_id**\]，文件后缀名为 `.od`。
    *   对于网格结合OD结构的交通数据，entity\_id 变成4列，列名为 \[**origin\_row\_id, origin\_column\_id, destination\_row\_id, destination\_column\_id**\]，文件后缀名为 `.gridod`。
    
*   对于轨迹相关任务: 
    
    轨迹数据包括GPS点轨迹、基于路段的轨迹（路网匹配后）、用户签到轨迹（基于POI的轨迹）。
    
    - GPS点轨迹
      - 格式为： ***dyna_id, type, time, entity_id, (traj_id), coordinates, properties***. 
      - **entity\_id**列的内容应为**usr\_id**，**traj_id**表示同一用户的多条轨迹的编号（从0开始），如果用户只有一条轨迹，则该列可以为空，**coordinates**列的内容为GPS点的纬度和经度。
    
    *   基于路段的轨迹
        *   格式为： ***dyna_id, type, time, entity_id, (traj_id), location, properties***. 
        *   **entity\_id**列的内容应为**usr\_id**，**traj_id**表示同一用户的多条轨迹的编号（从0开始），如果用户只有一条轨迹，则该列可以为空，**location**列的内容是**geo\_id**，指向geo表代表一个路段。
    *   基于POI的轨迹
        *   格式为： ***dyna_id, type, time, entity_id, (traj_id), location, properties***. 
        *   **entity\_id**列的内容应为**usr\_id**，**traj_id**表示同一用户的多条轨迹的编号（从0开始），如果用户只有一条轨迹，则该列可以为空，**location**列的内容是**geo\_id**，指向geo表代表一个POI。
    
    对于特定任务，轨迹下一个位置预测任务的输入基于POI点的轨迹，到达时间估计任务的输入为GPS点的轨迹或基于路段的轨迹，地图匹配任务的输入为GPS点的轨迹，输出的是基于路段的轨迹。

### 数据排列方式

- **Dyna表中，应该按照 <entity_id> 和 \<time\> 双关键字排列，即<entity_id>相同的记录放在一起并按照\<time\>排序。**
- **特别的，对于轨迹数据，同一用户 <entity_id> 的轨迹应先按 <traj_id> 排序，<traj_id> 相同者按照 \<time\> 排序。**

例如：

```
dyna_id,type,time,entity_id,traffic_speed
0,state,2012-03-01T00:00:00Z,773869,64.375
1,state,2012-03-01T00:05:00Z,773869,62.666666666666664
2,state,2012-03-01T00:10:00Z,773869,64.0
...
34270,state,2012-06-27T23:50:00Z,773869,66.75
34271,state,2012-06-27T23:55:00Z,773869,65.11111111111111
34272,state,2012-03-01T00:00:00Z,767541,67.625
34273,state,2012-03-01T00:05:00Z,767541,68.55555555555556
34274,state,2012-03-01T00:10:00Z,767541,63.75
...
68542,state,2012-06-27T23:50:00Z,767541,62.25
68543,state,2012-06-27T23:55:00Z,767541,66.88888888888889
68544,state,2012-03-01T00:00:00Z,767542,67.125
68545,state,2012-03-01T00:05:00Z,767542,65.44444444444444
...
```

```
dyna_id,type,time,entity_id,traj_id,coordinates,current_dis,current_state
0,trajectory,2014-08-03T18:29:00Z,810,0,"[104.115353,30.64392]",0.0,1.0
1,trajectory,2014-08-03T18:29:40Z,810,0,"[104.113091,30.642129]",0.294091467,1.0
2,trajectory,2014-08-03T18:30:20Z,810,0,"[104.110404,30.64393]",0.6199505718,1.0
3,trajectory,2014-08-03T18:31:00Z,810,0,"[104.108335,30.640667]",1.0332595142,1.0
...
21,trajectory,2014-08-03T18:53:23Z,810,0,"[104.076552,30.626844]",7.0811683597,0.0
22,trajectory,2014-08-03T18:13:00Z,810,1,"[104.106701,30.6916]",0.0,1.0
23,trajectory,2014-08-03T18:13:30Z,810,1,"[104.103889,30.688151]",0.4683813603,1.0
24,trajectory,2014-08-03T18:14:21Z,810,1,"[104.102828,30.68506]",0.8267467429,1.0
```

## Ext 表

Ext 表中一个元素由以下五部分组成：

**ext\_id、 time、 properties (multiple columns)**。

*   ext\_id：主键，唯一标识外部数据表中的一条记录。

*   time： 时间信息，采用 [ISO-8601 标准](https://www.iso.org/iso-8601-date-and-time-format.html) 中的日期时间组合表示法，如： `2020- 12-07T02:59:46Z`。

*   描述该条记录的属性信息，若有多个属性，可以使用不同的列名定义为多列数据，比如既有温度数据、又有湿度数据。


## 数据类型定义

需要在 config 文件中给出数据集中各列的数据类型定义，有助于后续的数据处理。

| 类型       | 说明                                  |
| ---------- | ------------------------------------- |
| geo_id     | 存在于 geo 表中的离散的有限的 ID      |
| usr_id     | 存在于 usr 表中的离散的有限的 ID      |
| rel_id     | 存在于 rel 表中的离散的有限的 ID      |
| time       | 符合 ISO-8601 标准的时间字符串        |
| coordinate | 符合 Geojosn 格式的坐标表示法的字符串 |
| num        | 实数类                                |
| enum       | 枚举类字符串                          |
| other      | 其余的均以字符串类型存储              |

## Config 文件

Config 文件用以补充描述上述五个表自身的信息， 以 `json` 形式保存并由 `geo`、 `usr`、 `rel`、 `dyna`、 `ext`、 `info` 六个键组成

*   `geo`、 `rel`、 `dyna`、 `ext`：

    包含一个 `including_types` 键， 以数组的形式描述该表中所具有的 `type` 值。 其后每个 `type` 作为键，描述该 `type` 下 `properties` 具有哪些键及其数据类型 。

*   `usr`：

    包含一个 `properties` 键，描述表中 `properties` 包含哪些键及其数据类型

*   `info`：

    **包含其他必要的数据集统计信息**，针对不同的交通预测任务，包含有不同的内容

    *   **对于交通状态预测任务：**

        * `geo_file`： `.geo` 文件的文件名， **字符串类型**， 默认为数据集名。

        * `rel_file`： `.rel` 文件的文件名， **字符串类型**， 默认为数据集名。

        * `data_files`： 数据文件的文件名 （例如 `.dyna`， `.grid`， `.gridod`）， **支持数组或字符串**，默认为数据集名。

        * `ext_file`： `.ext` 文件的文件名， **字符串类型**， 默认为数据集名。

        * `weight_col`： 从 `.rel` 文件中加载的列名， **支持只有一个元素的字符串数组或字符串**。不指定的话，如果 `.rel` 文件只有一列权重列，则没有问题，否则报错。

        * `data_col`： 从数据文件（如 `.dyna`， `.grid`， `.gridod`）加载的列名 ， **支持数组或字符串**，不指定则全部加载。

        * `ext_col`： 从外部数据文件中加载的列名， **支持数组或字符串**，不指定则全部加载。

        * `output_dim`： 指定模型输出的维度， **一般应该跟 `data_col`** 中指定的属性列名的数量相同。

        * `time_intervals`: 数据集时间片的长度，以秒为单位。

        * `init_weight_inf_or_zero`： 取值为 \[`inf` , `zero`\]。 加载 `.rel` 文件构建邻接矩阵时，初始化邻接矩阵为全INF (`inf`) 还是全0 (`zero`)， 默认为 `inf`。

        * `set_weight_link_or_dist`： 取值为 \[`link`, `dist`\]， 当加载 `.rel` 文件构建邻接矩阵时，使用文件中权重列中的原始值 (`dist`) 还是将之修订为全 01 的矩阵 (`link`)， 默认为 `dist`。 **\[注意： 如果 `.rel` 文件中只有相连的关系，没有不相连的关系，应该指定为 `link`\]**

        * `calculate_weight_adj`： 从 `.rel` 文件获取的邻接矩阵的权重是否需要进一步进行计算， **默认为 `False`**。 部分邻接矩阵在原始数据的基础上，进行了一些计算。目前的计算方法是带有阈值的高斯核方法： $$  w_{ij} = \exp \left(- \frac{d_{ij}^{2}}{\sigma^{2}}\right)$$

        * `weight_adj_epsilon`： 高斯核的阈值。 经过计算的权重如果小于该阈值，则变成0，即 $$  w_{ij}[w_{ij}<\epsilon]=0$$ 此参数依赖于参数 `calculate_weight_adj=True` 。
*   **对于轨迹下一跳预测任务：**
    
    *   `distance_upper`： POI点之间的最大距离。


样例如下：

```json
{
    "geo":{
        "including_types":[
            "Point"
        ],
        "Point":{
            "poi_name":"other"
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
