# Raw Data

## 人流轨迹数据集


### Foursquare

**Duration:** Apr. 12, 2012 ~ Feb. 16, 2013

**Link:** https://sites.google.com/site/yangdingqi/home/foursquare-dataset

**Description:**  Foursquare a location-based social networking website where users share their locations by checking-in.

### Foursquare: NYC Restaurant Rich Dataset

**Place:** New York, USA

**Duration:** Oct. 24, 2011 ~ Feb. 20, 2012

**Description:**  This dataset includes check-in, tip and tag data of restaurant venues in NYC.

### Foursquare: Global-scale Check-in Dataset

**Place:** 415 cities

**Duration:** Apr. 2012 ~ Sept. 2013

**Description:**  This dataset includes long-term (about 18 months from April 2012 to September 2013) global-scale check-in data collected from Foursquare.

### Foursquare: User Profile Dataset

**Place:** New York, USA and Tokyo, Japan

**Duration:** Apr. 2012 ~ Sept. 2013

**Description:**  This dataset includes some user profile data for privacy study (i. e., gender, friends, followers). The corresponding user check-in data can be found in the global-scale check-in dataset.

### Foursquare: Global-scale Check-in Dataset with User Social Networks

**Place:** 415 cities

**Duration:** Apr. 2012 ~ Jan. 2014

**Description:**  This dataset includes long-term (about 22 months from Apr. 2012 to Jan. 2014) global-scale check-in data collected from Foursquare, and also two snapshots of user social networks before and after the check-in data collection period. 

### Gowalla

**Place:** -

**Duration:** Feb. 2009 ~ Oct. 2010

**Link:** https://snap.stanford.edu/data/loc-gowalla.html

**Description:**  Gowalla is a location-based social networking website where users share their locations by checking-in,containing information of users, users' check-in time, users' latitude, longitude,users' location id.

### Brightkite

**Place:** -

**Duration:** Apr. 2008 ~ Oct. 2010

**Link:** http://snap.stanford.edu/data/loc-brightkite.html

**Description:** Brightkite is a location-based social networking website where users share their locations by checking-in,containing information of users, users' check-in time, users' latitude, longitude,users' location id.

### GeoLife-GPS

**Place:** Beijing, China (majority)

**Duration:** Aug. 2007 ~ Aug. 2012

**Link:** https://www.microsoft.com/en-us/research/publication/geolife-gps-trajectory-dataset-user-guide/

**Description:** The GPS track dataset was collected by 182 users from April 2007 to August 2012 and contains 17,621 tracks with a total distance of 1,292,951 km and a total duration of 50,176 hours. 91.5% of the tracks are recorded at high density, for example every 1 to 5 seconds or every 5 to 10 meters per point.

出行轨迹，基本就是user_ID，time ，lat，lon，location_id的格式

## 车辆轨迹数据集

### NYC-Bus

**Place:** New York, USA

**Duration:** Aug. 1, 2014 ~ Oct. 31, 2014

**Link:** http://web.mta.info/developers/MTA-Bus-Time-historical-data.html

**Description:** The NYC-Bus dataset contains MTA bus time historical data.

每条数据包含当前时间，公共汽车位置（经纬度），车辆ID，已行驶距离，公共汽车路线ID，下一站ID，到该站的距离

【本质上是不同时刻的公交车位置数据集】

### NYC-Taxi

**Place:** New York, USA

**Duration:** 2009 ~ present

**Link:** https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

**Description:** The NYC-Taxi dataset contains trajectories of different types of taxi collected by GPS for New York City from 2009 to 2020.

按行程ID组织数据（Per Trip），

黄色车：

上下车时间、上下车地点（经纬度）、行程距离、分项票价、费率类型、付款类型和司机报告的乘客数量

绿色车：

取车和还车时间、上下车地点（ID）、行程距离、分项票价、费率类型、付款类型和司机报告的乘客数量

FHV车：

上下车时间、上下车地点（ID）

### NYC-Bike

**Place:** New York, USA

**Duration:** Jun. 2013 ~ present

**Link:** https://www.citibikenyc.com/system-data

**Description:** The NYC-Bike dataset contains bike trajectories collected from NYC CitiBike system.

按行程ID组织数据（Per Trip），

旅程用时、起止时间、起止地点ID、起止地点Name、起止地点经纬度、车辆ID、用户类别、用户生日、用户性别

### BikeDC

**Place:** Washington, USA

**Duration:** Sept. 20, 2010 ~ Oct. 2020

**Link:** https://www.capitalbikeshare.com/system-data

**Description:** The BikeDC dataset describes the bike trails of the Washington Bicycle System, which includes 472 stops.

按行程ID组织数据（Per Trip），

起止时间、起止地点ID、起止地点Name、起止地点经纬度、车辆类型、车辆ID、用户类别

### BikeCHI

**Place:** Chicago, USA

**Duration:** Jun. 27, 2013 ~ 2018

**Link:** https://www.divvybikes.com/system-data

**Description:** The BikeCHI dataset shows the development of bike-sharing in Chicago from 2013 to 2018.

按行程ID组织数据（Per Trip），

起止时间、起止地点ID、起止地点Name、起止地点经纬度、车辆类型、车辆ID、用户类别

### AustinRide

**Place:** Austin, USA

**Duration:** Jun. 4, 2016 ~ Apr. 13, 2017

**Link:** https://data.world/ride-austin/ride-austin-june-6-april-13

**Description:** The AustinRide dataset contains Austin ride trajectories spans from August 1, 2016 to April 13, 2017, including over 1.4 million trips.

按行程ID组织数据（Per Trip），

旅程距离、起止时间、起止地点经纬度、车辆ID、用户ID等

### I-80

**Place:** San Francisco Bay, USA

**Duration:** Apr. 13, 2005

**Link:** https://www.fhwa.dot.gov/publications/research/operations/06137/index.cfm

**Description:** The I-80 dataset is 45 minutes long, and the vehicle trajectory data provides the precise location of each vehicle in the study area every tenth of a second.

按车辆ID组织数据，每隔一段时间记录一次车的位置，数据的每一行是车辆ID、车辆位置坐标、车辆的相关信息、车辆瞬时速度等

### T-Drive

**Place:** Beijing, China

**Duration:** Feb. 2, 2008 ~ Feb. 8, 2008

**Link:** https://www.microsoft.com/en-us/research/publication/t-drive-trajectory-data-sample/

**Description:** The T-Drive trajectory dataset sample containing the weekly trajectories of 10,357 Beijing taxis is about 15 million points, and the total distance of trajectories reaches 9 million kilometers.

按车辆ID组织数据，每隔一段时间记录一次车的位置，数据的每一行是车辆ID，时间，车辆位置经纬度

### Porto

**Place:** Porto, Portugal

**Duration:** Jul. 1, 2013 ~ Jun. 30, 2014

**Link:** https://archive.ics.uci.edu/ml/datasets/Taxi+Service+Trajectory+-+Prediction+Challenge%2C+ECML+PKDD+2015

**Description:** The Porto dataset describes trajectories performed by all the 442 taxis running in the city of Porto, in Portugal.

按行程ID组织数据（Per Trip），

每个Trip包含开始地点、开始时间、司机ID、一系列位置坐标：每隔一段时间记录一次车的位置（经纬度）

## 预处理过的车辆轨迹数据集

主要是将车辆轨迹数据集进行了空间切分、流量统计等预处理操作，将之转换成流量或者需求量数据。（主要是规则的网格划分）

### TaxiBJ

**Place:** Beijing, China

**Duration:** Jul. 1, 2013 ~ Oct. 30, 2013, Mar. 1, 2014 ~ Jun. 30, 2014, Mar. 1, 2015 ~ Jun. 30, 2015 and Nov. 1, 2015 ~ Apr. 10, 2016

**Link:** https://github.com/TolicWang/DeepST/issues/3

**Description:** The TaxiBJ dataset contains the taxicab GPS data, including crowd flow, meteorology and holiday information.

四维张量： [timeslots, inflow/outflow, grid_line_id, grid_column_id]，直接给出了inflow和outflow，只适合于流量预测

### NYCBike20140409

### NYCBike20160708

### NYCBike20160809

### NYCTaxi20140112

### NYCTaxi20150103

### NYCTaxi20160102

### T-Drive20150206

## 交通状况数据集

### METR-LA

**Place:** Los Angeles County, USA

**Duration:** Mar. 1, 2012 ~ Jun. 27, 2012

**Link:** https://github.com/liyaguang/DCRNN

**Description:** The METR-LA dataset collected in the highway by loop detectors, contains traffic speed data from 207 sensors.

列是时间，间隔为5min。行是sensor编号，提供文件表示sensor的经纬度。值是速度。

用sensor之间的距离矩阵代表路网（adjacency matrix、权重矩阵、代表节点的相似度）

### Los-loop

跟METR_LA稍有区别，把缺失值用线性插值的方式补充好了。

### SZ-Taxi

**Place:** Shenzhen, China

**Duration:** Jan. 1, 2015 ~ Jan. 31, 2015

**Link:** https://github.com/lehaifeng/T-GCN/tree/master/data

**Description:** The SZ-Taxi dataset contains the taxi trajectory of Shenzhen, including roads adjacency matrix and road traffic speed information.

DataFrame二维表的格式

列是时间，间隔为15min。行是sensor编号。值是速度。

提供adjacency matrix描述路网的结构（1或0，邻接与否）

### Loop Seattle

**Place:** Greater Seattle Area, China

**Duration:** over the entirely of 2015

**Link:** https://github.com/zhiyongc/Seattle-Loop-Data

**Description:** The Loop Seattle dataset is collected by the inductive loop detectors deployed on freeways (I-5, I-405, I-90, and SR-520) in Seattle area and contains traffic state data from 323 sensor stations.

列是时间，间隔为5min。行是sensor编号。值是速度。

提供adjacency matrix描述路网的结构（1或0，邻接与否）

### Q-Traffic

**Place:** Beijing, China

**Duration:** Apr. 1, 2017 ~ May 31, 2017

**Link:** https://github.com/JingqingZ/BaiduTraffic

**Description:** The Q-Traffic dataset contains three sub-datasets: query sub-dataset, traffic speed sub-dataset and road network sub-dataset.

- query sub-dataset

每条数据包括起始时间、起点经纬度、终点经纬度、预计的旅行时间

- traffic speed sub-dataset

数据收集的间隔为15min，每条数据为路段ID，时间戳 ([0, 5856))，速度(km/h)。

- road network sub-dataset

对于每个路段link，提供路段的起点（节点）和终点（节点），基于它们可以构建路网的拓扑、提供宽度，长度km，方向，限速和车道数信息。提供一个经纬度，不知道是起点还是终点。

### PEMS

**Place:** California, USA

**Duration:** 2001 ~ present

**Link:** http://pems.dot.ca.gov

**Description:** PEMS records California highway speed data, including time_hour, average_time, lane_points.

### PeMSD3

**Place:** District 3 of California, USA

**Duration:** Sept. 1, 2018 ~ Nov. 30, 2018

**Link:** https://github.com/Davidham3/STSGCN

**Description:** The PeMSD3 dataset includes 358 sensors and flow information.

DataFrame二维表的格式

列是时间，间隔为5min。行是sensor编号。值是flow。

也提供的numpy三维张量，时间间隔5min，三维（时间戳，sensor编号，flow）

用sensor之间的距离矩阵代表路网（adjacency matrix）

### PeMSD4

**Place:** San Francisco Bay Area, USA

**Duration:** Jan. 1, 2018 ~ Feb. 28, 2018

**Link:** https://github.com/Davidham3/ASTGCN/tree/master/data/PEMS04

**Description:** The PeMSD4 dataset describes the the speed flow occupancy information of California freeway and contains 3848 sensors on 29 roads.

提供的numpy三维张量，时间间隔5min，三维（时间戳，sensor编号，（flow, occupy, speed））

用sensor之间的距离矩阵代表路网（adjacency matrix）

### PEMSD7

**Place:** District 7 of California, USA

**Duration:** Jul. 1, 2016 ~ Aug. 31, 2016

**Link:** https://github.com/Davidham3/STSGCN

**Description:** The PeMSD7 dataset contains traffic flow information from 883 sensor stations.

提供的numpy三维张量，时间间隔5min，三维（时间戳，sensor编号，flow）

用sensor之间的距离矩阵代表路网（adjacency matrix）

### PeMSD8

**Place:** San Bernardino Area, USA

**Duration:** Jul. 1, 2016 ~ Aug. 31, 2016

**Link:** https://github.com/Davidham3/ASTGCN/tree/master/data/PEMS08

**Description:** The PeMSD8 dataset describes the speed occupancy of California freeways with data from 1979 sensors on 8 roads.

提供的numpy三维张量，时间间隔5min，三维（时间戳，sensor编号，（flow, occupy, speed））

用sensor之间的距离矩阵代表路网（adjacency matrix）

### PEMSD7(M)

**Place:** District 7 of California, USA

**Duration:** the weekdays of May and June of 2012

**Link:** https://github.com/Davidham3/STGCN/tree/master/datasets

**Description:** The PeMSD7(M) dataset describes highway speed information at 228 stations in the 7th District of California.

列是时间，间隔为5min。行是sensor编号。值是速度。

用sensor之间的距离矩阵代表路网（adjacency matrix）

### PeMSD-SF

**Place:** San Francisco Bay Area, USA

**Duration:** Jan. 1, 2008 ~ Mar. 30, 2009

**Link:** http://archive.ics.uci.edu/ml/datasets/PEMS-SF

**Description:** The PeMSD-SF dataset describes the occupancy rate, between 0 and 1, of different car lanes of San Francisco bay area freeways. 

Occupancy占有率数据集

### PEMS-BAY

**Place:** San Francisco Bay Area, USA

**Duration:** Jan. 1, 2017 ~ Jun. 30, 2017

**Link:** https://github.com/liyaguang/DCRNN

**Description:** The PeMS-BAY dataset contains 6 months of statistics on traffic speed, including 325 sensors.

列是时间，间隔为5min。行是sensor编号，提供文件表示sensor的经纬度。值是速度。

用sensor之间的距离矩阵代表路网（adjacency matrix、权重矩阵、代表节点的相似度）

### Beijing subway

### M_dense

### Rotterdam

### SHMetro

### HZMetro

### NYC Speed data

**Place:** New York, USA

**Duration:** Apr. 1, 2015 ~ present

**Link:** http://data.beta.nyc/dataset/nyc-real-time-traffic-speed-data-feed-archived

**Description:** The NYC Speed data contains speed data for New York City, including speed, travel time, status, etc.

按照道路ID组织数据，每一条数据包括道路ID、速度、时间、穿过道路的平均用时。

对于每个道路，提供文件描述一系列道路上sensor的经纬度位置、道路名称等。

Sequence of Lat/ Long points, describes locations of the sensor links

### HK

**Place:** Hong Kong, China

**Duration:** Dec. 28, 2015 ~ present

**Link:** https://data.gov.hk/en-data/dataset/hk-td-sm_1-traffic-speed-map

**Description:** The HK dataset contains average traffic speed of major roads in Hong Kong.

按照道路ID组织数据，每一条数据包括道路ID、道路区域、道路类型、道路状况等级、速度、时间。

时间间隔较短，可以得到每条道路，各个时间的速度信息。

对于每个路段link，提供文件描述起始站、终点站、以及相应的经纬度、道路类型。(基于它们可以构建路网的拓扑)

### ENG-HW

**Place:** British

**Duration:** 2006 ~ 2014

**Link:** http://tris.highwaysengland.co.uk/detail/trafficflowdata

**Description:** The ENG-HW dataset includes information on intercity road traffic between three UK cities recorded by the government from 2006 to 2014.

每个站点不同时间的流量数据

## 外部信息数据集

外部数据一般包括天气数据、路网结构数据、兴趣点（Point of Interest，POI）数据、事件数据、时间信息数据等数据。

- 气象条件：温度、湿度、风速、能见度和天气状态（晴/雨/风/多云等）
- 驾驶员ID：由于驾驶员的个人情况不同，预测会有一定的影响，因此有必要对驾驶员进行标记，此信息主要用于个人预测。
- 活动：包括各种节假日、交通管制、交通事故、体育赛事、音乐会等活动。
- 时间信息：星期几，一天中的时间片。

### NYC Accident data

**Place:** New York, USA

**Duration:** May 7, 2014 ~ present

**Link:** https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95

**Description:** The NYC Accident data Contains accidents data in NYC.

发生碰撞的日期、时间、经纬度、街道名、受伤人数、死亡人数、原因、车辆类型等

### Road network data (OpenStreetMap)

https://www.openstreetmap.org/

### Weather and events data

https://www.wunderground.com/

## 其他数据集

### BusCHI

**Place:** Chicago, USA

**Duration:** Aug. 2, 2011 ~ May 3, 2018

**Link:** https://data.cityofchicago.org/Transportation/Chicago-Traffic-Tracker-Historical-Congestion-Esti/77hq-huss/data

**Description:** The BusCHI dataset contains the historical estimated congestion for 1270 traffic segments.

交通拥堵状况数据集

### CTM

持续时间、请求数数据集

### HEAT

温度数据集

### AcousticPollution

声污染数据集

