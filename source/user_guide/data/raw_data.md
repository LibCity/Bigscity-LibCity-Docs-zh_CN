# Raw Data

## 人流轨迹数据集

### Foursquare

**时期：** Apr. 12, 2012 ~ Feb. 16, 2013

**链接：** https://sites.google.com/site/yangdingqi/home/foursquare-dataset

**描述：** Foursquare 是一个基于地理位置的社交网站，用户通过签到来分享他们的地理位置。

### Foursquare: NYC Restaurant Rich Dataset

**地点：** New York, USA

**时期：** Oct. 24, 2011 ~ Feb. 20, 2012

**描述：** 这个数据集包括纽约餐厅地点的签到、小费和标签数据。

### Foursquare: Global-scale Check-in Dataset

**地点：** 415 个地点

**时期：** Apr. 2012 ~ Sept. 2013

**描述：** 该数据集包括从 Foursquare 收集的全球长期签到数据。

### Foursquare: User Profile Dataset

**地点：** New York, USA and Tokyo, Japan

**时期：** Apr. 2012 ~ Sept. 2013

**描述：** 该数据集包括一些用于隐私研究的用户资料(如性别、朋友、关注者)。相应的用户签到数据可以在全局签到数据集中找到。

### Foursquare: Global-scale Check-in Dataset with User Social Networks

**地点：** 415 个地点

**时期：** Apr. 2012 ~ Jan. 2014

**描述：** 该数据集包括从 Foursquare 收集的全球长期签到数据，以及签到数据收集期间前后用户社交网络的两张快照。

### Gowalla

**地点：** -

**时期：** Feb. 2009 ~ Oct. 2010

**链接：** https://snap.stanford.edu/data/loc-gowalla.html

**描述：** Gowalla 是一个以位置为基础的社交网站，用户通过签到分享自己的位置，包括用户信息、签到时间、用户纬度、经度、用户位置id。

### Brightkite

**地点：** -

**时期：** Apr. 2008 ~ Oct. 2010

**链接：** http://snap.stanford.edu/data/loc-brightkite.html

**描述：** Brightkite是一个基于位置的社交网站，用户通过签到分享自己的位置，包含用户信息、用户签到时间、用户纬度、经度、用户位置 id。

### GeoLife-GPS

**地点：** Beijing, China (主要)

**时期：** Aug. 2007 ~ Aug. 2012

**链接：** https://www.microsoft.com/en-us/research/publication/geolife-gps-trajectory-dataset-user-guide/

**描述：** 182名用户的GPS轨迹数据集，包含17621条轨迹，总距离为122951公里，总持续时间为50176小时。91.5%的轨迹是高密度记录（如每1 - 5秒或每点5 - 10米记录一次）

# Vehicle trajectory dataset

### NYC-Bus
**地点：** New York, USA

**时期：** Aug. 1, 2014 ~ Oct. 31, 2014

**链接：** http://web.mta.info/developers/MTA-Bus-Time-historical-data.html

**描述：** NYC-BUS 数据集包含 MTA 巴士的时间历史数据。

### NYC-Taxi
**地点：** New York, USA

**时期：** 2009 ~ present

**链接：** https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

**描述：** NYC-Taxi DataSet 包含由GPS收集的不同类型出租车的轨迹。

### NYC-Bike
**地点：** New York, USA

**时期：** Jun. 2013 ~ present

**链接：** https://www.citibikenyc.com/system-data

**描述：** NYC- bike 数据集包含从纽约市城市自行车系统收集的自行车轨迹。

### BikeDC
**地点：** Washington, USA

**时期：** Sept. 20, 2010 ~ Oct. 2020

**链接：** https://www.capitalbikeshare.com/system-data

**描述：** BikeDC 数据集描述了华盛顿自行车系统的自行车路径，其中包括472个站点。

### BikeCHI
**地点：** Chicago, USA

**时期：** Jun. 27, 2013 ~ 2018

**链接：** https://www.divvybikes.com/system-data

**描述：** BikeCHI 数据集显示了芝加哥从2013年到2018年共享单车的发展。

### AustinRide
**地点：** Austin, USA

**时期：** Jun. 4, 2016 ~ Apr. 13, 2017

**链接：** https://data.world/ride-austin/ride-austin-june-6-april-13

**描述：** AustinRide 数据集包含了从2016年8月1日到2017年4月13日的奥斯汀乘车轨迹，包括140多万次出行。

### I-80
**地点：** San Francisco Bay, USA

**时期：** Apr. 13, 2005

**链接：** https://www.fhwa.dot.gov/publications/research/operations/06137/index.cfm

**描述：** I-80 车辆轨迹数据数据集长达45分钟，包含研究区域内每辆车每十分之一秒的精确位置。

### T-Drive
**地点：** Beijing, China

**时期：** Feb. 2, 2008 ~ Feb. 8, 2008

**链接：** https://www.microsoft.com/en-us/research/publication/t-drive-trajectory-data-sample/

**描述：** T-Drive 轨迹数据集包含 10,357 辆北京出租车的每周轨迹。轨道的总距离达到了900万公里。

### Porto
**地点：** Porto, Portugal

**时期：** Jul. 1, 2013 ~ Jun. 30, 2014

**链接：** https://archive.ics.uci.edu/ml/datasets/Taxi+Service+Trajectory+-+Prediction+Challenge%2C+ECML+PKDD+2015

**描述：** 波尔图数据集描述了葡萄牙波尔图市所有 442 辆出租车的运行轨迹。

## 预处理车辆轨迹数据集

主要对车辆轨迹数据集进行空间分割、流量统计等预处理操作，并将其转换为流量或需求数据。(主要是基于网格)

### TaxiBJ
**地点：** Beijing, China

**时期：** Jul. 1, 2013 ~ Oct. 30, 2013, Mar. 1, 2014 ~ Jun. 30, 2014, Mar. 1, 2015 ~ Jun. 30, 2015 and Nov. 1, 2015 ~ Apr. 10, 2016

**链接：** https://github.com/TolicWang/DeepST/issues/3

**描述：** TaxiBJ 数据集包含出租车GPS数据，包括人流、气象和假期信息。

### NYCBike20140409
### NYCBike20160708
### NYCBike20160809
### NYCTaxi20140112
### NYCTaxi20150103
### NYCTaxi20160102
### T-Drive20150206
## Traffic condition dataset

### METR-LA
**地点：** Los Angeles County, USA

**时期：** Mar. 1, 2012 ~ Jun. 27, 2012

**链接：** https://github.com/liyaguang/DCRNN

**描述：** 由环路探测器在高速公路上收集，包含来自 207 个传感器的交通速度数据。

### Los-loop
描述：与METR LA略有不同，缺失值通过线性插值得到补充。

### SZ-Taxi
**地点：** Shenzhen, China

**时期：** Jan. 1, 2015 ~ Jan. 31, 2015

**链接：** https://github.com/lehaifeng/T-GCN/tree/master/data

**描述：** SZ-Taxi 数据集包含深圳市的出租车轨迹，包括道路邻接矩阵和道路交通速度信息。

### Loop Seattle
**地点：** Greater Seattle Area, China

**时期：** over the entirely of 2015

**链接：** https://github.com/zhiyongc/Seattle-Loop-Data

**描述：** Loop Seattle 数据集由部署在西雅图地区高速公路(I-5、I-405、I-90和SR-520)上的感应环路探测器收集，包含来自323个传感器站的交通状态数据。

### Q-Traffic
**地点：** Beijing, China

**时期：** Apr. 1, 2017 ~ May 31, 2017

**链接：** https://github.com/JingqingZ/BaiduTraffic

**描述：** Q-Traffic 数据集包含三个子数据集:查询子数据集、交通速度子数据集和路网子数据集。

### PEMS
**地点：** California, USA

**时期：** 2001 ~ present

**链接：** http://pems.dot.ca.gov

**描述：** PEMS 记录加利福尼亚高速公路的速度数据，包括时间小时，平均时间，车道点。

### PeMSD3
**地点：** District 3 of California, USA

**时期：** Sept. 1, 2018 ~ Nov. 30, 2018

**链接：** https://github.com/Davidham3/STSGCN

**描述：** PeMSD3 数据集包括 358 个传感器和流量信息。

### PeMSD4
**地点：** San Francisco Bay Area, USA

**时期：** Jan. 1, 2018 ~ Feb. 28, 2018

**链接：** https://github.com/Davidham3/ASTGCN/tree/master/data/PEMS04

**描述：** PeMSD4 数据集描述了加州高速公路的速度流量占用信息，包含29条道路上的3848个传感器。

### PEMSD7
**地点：** District 7 of California, USA

**时期：** Jul. 1, 2016 ~ Aug. 31, 2016

**链接：** https://github.com/Davidham3/STSGCN

**描述：** PeMSD7 数据集包含883个传感器站的交通流量信息。

### PeMSD8
**地点：** San Bernardino Area, USA

**时期：** Jul. 1, 2016 ~ Aug. 31, 2016

**链接：** https://github.com/Davidham3/ASTGCN/tree/master/data/PEMS08

**描述：** PeMSD8 数据集描述了加州高速公路的速度占用率，数据来自8条公路上的1979个传感器。

### PEMSD7(M)
**地点：** District 7 of California, USA

**时期：** the weekdays of May and June of 2012

**链接：** https://github.com/Davidham3/STGCN/tree/master/datasets

**描述：** PeMSD7(M) 数据集描述了加州第7区228个站点的高速公路速度信息。

### PeMSD-SF
**地点：** San Francisco Bay Area, USA

**时期：** Jan. 1, 2008 ~ Mar. 30, 2009

**链接：** http://archive.ics.uci.edu/ml/datasets/PEMS-SF

**描述：** PeMSD-SF数据集描述了旧金山湾区高速公路不同车道的占用率，在0到1之间。

### PEMS-BAY
**地点：** San Francisco Bay Area, USA

**时期：** Jan. 1, 2017 ~ Jun. 30, 2017

**链接：** https://github.com/liyaguang/DCRNN

**描述：** PEMS-BAY 数据集包含6个月的交通速度统计数据，包括325个传感器。

### Beijing subway
### M\_dense
### Rotterdam
### SHMetro
### HZMetro
### NYC Speed data
**地点：** New York, USA

**时期：** Apr. 1, 2015 ~ present

**链接：** http://data.beta.nyc/dataset/nyc-real-time-traffic-speed-data-feed-archived

**描述：** 纽约市速度数据包含纽约市的速度数据，包括速度、旅行时间、状态等。

LAT / LONG 点序列描述了传感器链路的位置

### HK
**地点：** Hong Kong, China

**时期：** Dec. 28, 2015 ~ present

**链接：** https://data.gov.hk/en-data/dataset/hk-td-sm\_1-traffic-speed-map

**描述：** HK 数据集包含香港主要道路的平均行车速度。

### ENG-HW
**地点：** British

**时期：** 2006 ~ 2014

**链接：** http://tris.highwaysengland.co.uk/detail/trafficflowdata

**描述：** ENG-HW 数据集包括政府从2006年到2014年记录的三个英国城市之间的城市间道路交通信息。

## 外部数据集

外部数据一般包括天气数据、路网结构数据、热点(point of interest, POI)数据、事件数据、时间信息数据等数据。

*   天气条件：温度，湿度，风速，可见性和天气状态（阳光、雨、风、阴云等）

*   司机 ID:因为司机的个人情况不同，预测会有一定的影响，所以有必要对司机进行标记。这些信息主要用于个人预测。

*   活动:包括各种节假日、交通管制、交通事故、体育赛事、音乐会等活动。

*   时间信息:星期的一天，一天的时间切片。 /p>


### NYC Accident data
**地点：** New York, USA

**时期：** May 7, 2014 ~ present

**链接：** https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95

**描述：** NYC Accident data 包含纽约市的事故数据.

### Road network data (OpenStreetMap)
**链接：** https://www.openstreetmap.org/

### Weather and events data
**链接：** https://www.wunderground.com/

## Others

### BusCHI
**地点：** Chicago, USA

**时期：** Aug. 2, 2011 ~ May 3, 2018

**链接：** https://data.cityofchicago.org/Transportation/Chicago-Traffic-Tracker-Historical-Congestion-Esti/77hq-huss/data

**描述：** BusCHI 数据集包含1270个流量段的历史估计拥堵度。

交通拥堵度数据集

### CTM
持续时间和请求数的数据集

### HEAT
温度数据集

### AcousticPollution
噪声数据集
