## 复现模型列表

#### 基线模型

对于时间序列预测任务：

- **HA**:

  历史平均值，将历史流量建模为季节性过程，然后使用前几个季节的加权平均值作为预测值。

- **VAR**:

  向量自回归，这是一种常用的时间序列预测模型，用于捕捉多个变量随时间的关系。

- **SVR**:

  支持向量回归，它使用线性支持向量机进行回归任务。 SVR利用历史数据训练模型建立输入输出关系，然后进行预测。

- **ARIMA**

  带有卡尔曼滤波器的自回归综合移动平均模型。

对于交通速度、流量、需求预测任务：

* **AutoEncoder**

  本基线模型由我们实现，采用编码器从数据中学习嵌入向量后用解码器预测未来交通状况。

* **RNN（FC-RNN）**

  本基线模型由我们实现，预测交通状态，基于 RNN。

* **Seq2Seq**

  本基线模型由我们实现，基于编码器-解码器架构，预测交通状态。采用基于门控循环单元的编码器-解码器框架，进行多步预测。

- **FNN**

  该基线模型由我们自己实现，用于基于具有两个隐藏层和 L2 正则化的前馈神经网络的交通状态预测任务。

对于轨迹下一跳预测任务：

* **RNN**

  该基线模型由我们实现，使用 RNN 建模序列信息进行下一跳预测。

#### 交通流量预测

* **ST-ResNet**

  时空残差网络，广泛用于基于网格的流量预测任务，以残差单元建模时空关联。

  ```
  Junbo Zhang, Yu Zheng, and Dekang Qi. 2017. Deep Spatio-Temporal Residual Networks for Citywide Crowd Flows Prediction. In AAAI. AAAI Press, 1655–1661.
  ```

* **ACFM**

  注意力人群流量机，能推断人群流量，通过注意力机制学习随时间变化数据的动态表示。

  ```
  Lingbo Liu, Ruimao Zhang, Jiefeng Peng, Guanbin Li, Bowen Du, and Liang Lin.2018. Attentive Crowd Flow Machines. In ACM Multimedia. ACM, 1553–1561.
  ```

* **ASTGCN**

  基于注意力的时空图卷积网络，融合时空注意力机制与时空卷积捕捉动态时空特征。

  ```
  Shengnan Guo, Youfang Lin, Ning Feng, Chao Song, and Huaiyu Wan. 2019.Attention Based Spatial-Temporal Graph Convolutional Networks for Traffic Flow Forecasting. In AAAI. AAAI Press, 922–929.
  ```

* **MSTGCN**

  降级版的ASTGCN，称为多组件时空图卷积网络，去掉了原模型的时空注意力机制。

  ```
  Shengnan Guo, Youfang Lin, Ning Feng, Chao Song, and Huaiyu Wan. 2019.Attention Based Spatial-Temporal Graph Convolutional Networks for Traffic Flow Forecasting. In AAAI. AAAI Press, 922–929.
  ```

* **AGCRN**

  自适应图卷积循环网络，通过自适应模块增强传统图卷积，并组合成循环神经网络，以捕捉细粒度时空关联。

  ```
  Lei Bai, Lina Yao, Can Li, Xianzhi Wang, and Can Wang. 2020. Adaptive Graph Convolutional Recurrent Network for Traffic Forecasting. In NeurIPS.
  ```

* **CONVGCN**

  Conv-GCN 组合图卷积网络（GCN）与三维卷积神经网络（3D CNN）。三维卷积神经网络创新性地应用在集成入流与出流信息，以及提取入流/出流模式间与距离远近不同站点间的高层次关联两方面。

  ```
  Jinlei Zhang, Feng Chen, Yinan Guo, and Xiaohong Li. 2020. Multi-graph convolutional network for short-term passenger flow forecasting in urban rail transit. IET Intell. Trans. Syst.14, 10 (2020), 1210–1217.
  ```

* **STDN**

  时空动态网络（STDN）引入流门控机制以学习位置间的动态相似性，以及设计了周期轮换变动的注意力机制来把握长期、周期性的随时间的变换。

  ```
  Huaxiu Yao, Xianfeng Tang, Hua Wei, Guanjie Zheng, and Zhenhui Li. 2019.Revisiting Spatial-Temporal Similarity: A Deep Learning Framework for Traffic Prediction. In AAAI. AAAI Press, 5668–5675.
  ```

* **STSGCN**

  时空同步图卷积网络（STSGCN），致力于时空网络数据预测。通过精心设计的时空同步建模机制，该模型能够有效地提取复杂、局部化的时空关联。

  ```
  Chao Song, Youfang Lin, Shengnan Guo, and Huaiyu Wan. 2020. Spatial-Temporal Synchronous Graph Convolutional Networks: A New Framework for Spatial-Temporal Network Data Forecasting. In AAAI. AAAI Press, 914–921.
  ```

* **ToGCN**

  拓扑图卷积网络（ToGCN）后跟序列到序列（Seq2Seq）网络，以时间关联预测未来的交通流量与密度。

  ```
  Han Qiu, Qinkai Zheng, Mounira Msahli, Gerard Memmi, Meikang Qiu, and Jialiang Lu. 2020. Topological Graph Convolutional Network-Based Urban Traffic Flow and Density Prediction. IEEE Trans. Intell. Transp. Syst.(2020).
  ```

* **ResLSTM**

  ResLSTM是合并残差网络（ResNet），图卷积网络（GCN）和长短期记忆内存（LSTM）的深度学习架构，在交通网尺度预测城市轨道交通短期客流。

  ```
  Jinlei Zhang, Feng Chen, Zhiyong Cui, Yinan Guo, and Yadi Zhu. 2020.  Deep learning architecture for short-term passenger flow forecasting in urban rail transit. IEEE Trans. Intell. Transp. Syst.(2020).
  ```

* **CRANN**

  CRANN是可解释的、基于注意力的神经网络，其中多个模块组合以捕捉关键的时空时间序列部分。

  ```
  Rodrigo  de  Medrano  and  José  Luis  Aznarte.  2020.   A  Spatio-Temporal  Spot-Forecasting Framework forUrban Traffic Prediction. CoRR abs/2003.13977 (2020).
  ```

* **Multi-STGCnet**

  Multi-STGCnet含有三个作为时间组件的基于长短期记忆内存（LSTM）的模块和作为空间组件的三个用于提取目标站点空间关联的空间矩阵。

  ```
  Jiexia Ye, Juanjuan Zhao, Kejiang Ye, and Chengzhong Xu. 2020. Multi-STGCnet:A Graph Convolution Based Spatial-Temporal Framework for Subway PassengerFlow Forecasting. In IJCNN. IEEE, 1–8.
  ```

* **DGCN**

  DGCN是用于交通预测的创新性的图卷积网络，其中引入了潜在网络以提取时空特征，为了适应性地建构动态路网图矩阵。

  ```
  Kan Guo, Yongli Hu, Zhen Qian, Yanfeng Sun, Junbin Gao, and Baocai Yin. 2020.Dynamic Graph Convolution Network for Traffic Forecasting Based on Latent Network of Laplace Matrix Estimation. IEEE Trans. Intell. Transp. Syst.(2020).
  ```

* **DSAN**

  动态切换注意力网络（DSAN）含有创新性的多空间注意力机制（MSA），通过在带噪声的输入上应用自注意力动态提取有价值的信息，再将各输出直接拼接。

  ```
  Haoxing Lin, Rufan Bai, Weijia Jia, Xinyu Yang, and Yongjian You. 2020. Preserving Dynamic Attention for Long-Term Spatial-Temporal Prediction. In KDD. ACM,36–46.
  ```

* **STNN**

  STNN通过结构化隐动态组件学习这些依赖，然后一个解码器从隐表示中得到观测值。

  ```
  Ali Ziat, Edouard Delasalles, Ludovic Denoyer, and Patrick Gallinari. 2018. Spatio-Temporal Neural Networks for Space-Time Series Forecasting and Relations Discovery. CoRRabs/1804.08562 (2018).
  ```

#### 交通速度预测

* **DCRNN**

  扩散卷积循环神经网络，用由扩散过程形式化的图卷积捕捉时间依赖，并用编码器-解码器框架捕捉空间依赖。

  ```
  Yaguang Li, Rose Yu, Cyrus Shahabi, and Yan Liu. 2018. Diffusion Convolutional Recurrent Neural Network: Data-Driven Traffic Forecasting. In ICLR (Poster).OpenReview.net.
  ```

* **STGCN**

  时空图卷积网络，综合图卷积和门控时间卷积捕捉时空关联。

  ```
  Bing Yu, Haoteng Yin, and Zhanxing Zhu. 2018. Spatio-Temporal Graph Convolutional Networks: A Deep Learning Framework for Traffic Forecasting. In IJCAI. ijcai.org, 3634–3640.
  ```

* **GWNET**

  集成扩散卷积与一维空洞因果卷积捕捉时空依赖的时空图卷积网络。

  ```
  Zonghan Wu, Shirui Pan, Guodong Long, Jing Jiang, and Chengqi Zhang. 2019.Graph Wave Net for Deep Spatial-Temporal Graph Modeling. In IJCAI. ijcai.org,1907–1913.
  ```

* **MTGNN**

  专门为多变量时间序列数据设计的图神经网络框架，组合图卷积网络与混跳传播层、空洞复合卷积层捕捉时空依赖。

  ```
  Zonghan Wu, Shirui Pan, Guodong Long, Jing Jiang, Xiaojun Chang, and Chengqi Zhang. 2020.  Connecting the Dots: Multivariate Time Series Forecasting with Graph Neural Networks. In KDD. ACM, 753–763.
  ```

* **TGCN**

  时间图卷积模型，混合图卷积网络和门控循环单元捕捉时空关联。

  ```
  Ling Zhao, Yujiao Song, Chao Zhang, Yu Liu, Pu Wang, Tao Lin, Min Deng, and Haifeng Li. 2020. T-GCN: A Temporal Graph Convolutional Network for Traffic Prediction. IEEE Trans. Intell. Transp. Syst.21, 9 (2020), 3848–385.
  ```

* **TGCLSTM**

  交通图卷积长短期记忆内存神经网络（TGC-LSTM），能学习交通网络中路段之间的交互，以及预测全网络的交通状态。

  ```
  Zhiyong Cui, Kristian Henrickson, Ruimin Ke, and Yinhai Wang. 2020.  Traffic Graph Convolutional Recurrent Neural Network: A Deep Learning Frame work for Network-Scale Traffic Learning and Forecasting. IEEE Trans. Intell. Transp.Syst.21, 11 (2020), 4883–4894.
  ```

* **ATDM**

  ATDM是使用先验空间知识的模型。它是基于卷积、用于回归的神经网络，也有对应的空间不敏感版本。

  ```
  Rodrigo de Medrano and José Luis Aznarte. 2020.  On the Inclusion of Spatial Information for Spatio-Temporal Neural Networks. CoRR abs/2007.07559 (2020).
  ```

* **GMAN**

  GMAN采用编码器-解码器架构，编码器和解码器都由多个时空注意力块组成，来建模时空因素对交通状况的影响。

  ```
  Chuanpan Zheng, Xiaoliang Fan, Cheng Wang, and Jianzhong Qi. 2020. GMAN:A Graph Multi-Attention Network for Traffic Prediction. In AAAI. AAAI Press,1234–1241.
  ```

* **GTS**

  GTS是节点图未知时能够用GNN同时学习的模型，也是在图概率分布上优化期望性能的图概率模型。

  ```
  Chao Shang, Jie Chen, and Jinbo Bi. 2021. Discrete Graph Structure Learning forForecasting Multiple Time Series. CoRR abs/2101.06861 (2021).
  ```

* **STAGGCN**

  STAGGCN利用城市交通流量的时空关联，通过寻找道路节点的空间与语义邻居构建动态带权图。

  ```
  Bin Lu, Xiaoying Gan, Haiming Jin, Luoyi Fu, and Haisong Zhang. 2020.  Spa-tiotemporal Adaptive Gated Graph Convolution Network for Urban Traffic FlowForecasting. In CIKM. ACM, 1025–1034.
  ```

* **HGCN**

  结构化图卷积网络（HGCN）致力于交通预测，同时在宏观和微观交通图上进行。

  ```
  Kan Guo, Yongli Hu, Yanfeng Sun, Sean Qian, Junbin Gao, and Baocai Yin. 2021.Hierarchical Graph Convolution Networks for Traffic Forecasting. (2021).
  ```

* **ST-MGAT**

  时空多头图注意力机制网络（ST-MGAT），在图上直接建构卷积的同时，考虑邻居节点的特征和边权，生成新的节点表示。

  ```
  Kelang Tian, Jingjie Guo, Kejiang Ye, and Cheng-Zhong Xu. 2020.  ST-MGAT:Spatial-Temporal Multi-Head Graph Attention Networks for Traffic Forecasting. In ICTAI. IEEE, 714–721.
  ```

* **DKFN**

  深度卡曼滤波网络（DKFN）通过对自依赖和邻居依赖分别按照两序列进行建模，二者预测在统计学理论下融合，并经过卡曼滤波网络优化，来预测网络级别的交通状态。

  ```
  Fanglan Chen, Zhiqian Chen, Subhodip Biswas, Shuo Lei, Naren Ramakrishnan,and Chang-Tien Lu. 2020. Graph Convolutional Networks with Kalman Filtering for Traffic Prediction. In SIGSPATIAL/GIS. ACM, 135–138.
  ```

- **STTN**

  该模型使用时间和空间的Transformer结构进行交通预测。

  ```
  Xu, M., Dai, W., Liu, C., Gao, X., Lin, W., Qi, G. J., & Xiong, H. (2020). Spatial-temporal transformer networks for traffic flow forecasting. arXiv preprint arXiv:2001.02908.
  ```

#### 交通需求量预测

* **DMVSTNET**

  深度多视角时空网络（DVMST-Net）框架对时空关系进行建模。它由三个视角组成：时间视角、空间视角、语义视角。

  ```
  Huaxiu Yao, Fei Wu, Jintao Ke, Xianfeng Tang, Yitian Jia, Siyu Lu, Pinghua Gong, Jieping Ye, and Zhenhui Li. 2018. Deep Multi-View Spatial-Temporal Network for Taxi Demand Prediction. In AAAI. AAAI Press, 2588.
  ```

* **STG2Seq**

  STG2Seq是基于图的多步城市客流量预测模型，使用层次化图卷积的网络结构同时捕捉时空关联。

  ```
  Lei Bai, Lina Yao, Salil S. Kanhere, Xianzhi Wang, and Quan Z. Sheng. 2019. STG2Seq: Spatial-Temporal Graph to Sequence Model for Multi-step Passenger Demand Forecasting. In IJCAI. ijcai.org, 1981-1987.
  ```

* **CCRNN**

  CCRNN是捕捉多级别空间依赖的模型。CGC中的依赖矩阵是自学习的，每个层都有变化。应用按层的耦合机制桥接上层与下层的图结构。

  ```
  Junchen Ye, Leilei Sun, Bowen Du, Yanjie Fu, and Hui Xiong. 2021.  Coupled Layer-wise Graph Convolution for Transportation Demand Prediction. In AAAI. AAAI Press, 4617–4625.
  ```


#### OD矩阵预测

* **GEML**

  该模型使用图卷积神经网络捕获空间信息，p-Skip LSTM 捕获时间信息、以及多任务学习机制，预测每对出发-到达地点间的出租车流量。

  ```
  Wang, Yuandong & Yin, Hongzhi & Chen, Hongxu & Wo, Tianyu & xu, Jiudong & Zheng, Kai. (2019). Origin-Destination Matrix Prediction via Graph Convolution: a New Perspective of Passenger Demand Modeling. In KDD. ACM. 2019. 1227-1235
  ```

* **CSTN**

  该模型使用双视图卷积神经网络，捕获出发地、目的地两个视图上节点的空间信息，并使用 ConvLSTM 捕获时间信息，最后通过卷积捕获全局相关性。

  ```
  Liu, Lingbo & Qiu, Zhilin & Li, Guanbin & Wang, Qing & Ouyang, Wanli & Lin, Liang. (2019). Contextualized Spatial-Temporal Network for Taxi Origin-Destination Demand Prediction. In IEEE Transactions on Intelligent Transportation Systems. 2019. 3875-3887
  ```

#### 交通事故预测

- **GSNet**：

  该模型提出从时空地理和时空语义两个角度综合考虑交通事故风险，并设计了加权损失函数，更多关注高风险区域的样本信息，以解决零膨胀问题。

  ```
  Beibei Wang, Youfang Lin, Shengnan Guo, Huaiyu Wan. 2021. GSNet: Learning Spatial-Temporal Correlations from Geographical and Semantic Aspects for Traffic Accident Risk Forecasting. In AAAI. AAAI Press, 4402-4409. 
  ```

#### 轨迹下一跳预测

* **FPMC**

  经典下一跳预测基线模型。在下一跳预测领域研究早期，该模型经常作为基线模型使用。

  ```
  Steffen Rendle, Christoph Freudenthaler, and Lars Schmidt-Thieme. 2010. Factorizing personalized Markov chains for next-basket recommendation. In WWW ACM, 811–820.
  ```

* **ST-RNN**

  该模型聚焦于在RNN隐藏层引入时空转移特性。

  ```
  Qiang Liu, Shu Wu, Liang Wang, and Tieniu Tan. 2016. Predicting the Next Location: A Recurrent Model with Spatial and Temporal Contexts. In AAAI. AAAI Press, 194–200.
  ```

* **ATST-LSTM**

  该模型将轨迹点间的时间与距离差引入LSTM，并使用注意力机制。

  ```
  Liwei Huang, Yutao Ma, Shibo Wang, and Yanbo Liu. 2019. An attention-based spatiotemporal lstm network for next poi recommendation. IEEE Transactions on Services Computing(2019).
  ```

* **SERM**

  该模型在网络中引入轨迹的语义信息。

  ```
  Di Yao, Chao Zhang, Jian-Hui Huang, and Jingping Bi. 2017. SERM: A Recurrent Model for Next Location Prediction in Semantic Trajectories. In CIKM. ACM,2411–24.
  ```

* **DeepMove**

  该模型混合历史和当前的轨迹进行预测，在这方面第一次采用注意力机制。

  ```
  Jie Feng, Yong Li, Chao Zhang, Funing Sun, Fanchao Meng, Ang Guo, and Depeng Jin. 2018. DeepMove: Predicting Human Mobility with Attentional Recurrent Networks. In WWW. ACM, 1459–1468.
  ```

* **HST-LSTM**

  该模型也将时空转移因子引入LSTM，并采用编码器-解码器架构进行预测。

  ```
  Dejiang Kong and Fei Wu. 2018.  HST-LSTM: A Hierarchical Spatial-Temporal Long-Short Term Memory Network for Location Prediction. In IJCAI. ijcai.org,2341–2347.
  ```

* **LSTPM**

  该模型使用两个特别设计的LSTM捕捉用户长短期移动偏好，以联合二者预测下一位置。

  ```
  Ke Sun, Tieyun Qian, Tong Chen, Yile Liang, Quoc Viet Hung Nguyen, and HongzhiYin. 2020. Where to Go Next: Modeling Long- and Short-Term User Preferences for Point-of-Interest Recommendation. In AAAI. AAAI Press, 214-221.
  ```

* **GeoSAN**

  该模型使用自注意力机制实现某个关键点的表示学习，进而做到基于表征的预测。

  ```
  Defu Lian, Yongji Wu, Yong Ge, Xing Xie, and Enhong Chen. 2020. Geography-Aware Sequential Location Recommendation. In KDD. ACM, 2009–2019.
  ```

* **STAN**

  该模型采用自注意力机制捕捉时空信息来直接预测。

  ```
  Yingtao Luo, Qiang Liu, and Zhaocheng Liu. 2021. STAN: Spatio-Temporal Attention Network for Next Location Recommendation. CoRR abs/2102.04095 (2021).
  ```

* **CARA**

  该模型聚焦使用注意力机制提取轨迹间上下文信息来预测。

  ```
  Jarana Manotumruksa, Craig Macdonald, and Iadh Ounis. 2018.  A Contextual Attention Recurrent Architecture for Context-Aware Venue Recommendation. In SIGIR. ACM, 555–564.
  ```

#### 到达时间估计

* **DeepTTE**

  该模型是端到端的深度学习模型，直接预测整条路经所需的旅行时间；提出了地理卷积操作，通过将地理信息整合到传统的卷积中，用来捕捉空间相关性。

  ```
  Wang, D., Zhang, J., Cao, W., Li, J., & Zheng, Y. (2018). When Will You Arrive? Estimating Travel Time Based on Deep Neural Networks. Proceedings of the AAAI Conference on Artificial Intelligence, 32(1).
  ```

* **TTPNet**

  该模型基于张量分解和图接入，可以从历史轨迹有效捕捉旅行速度和路网表征，以及可以更好地预测旅行时间。

  ```
  Y. Shen, C. Jin and J. Hua, "TTPNet: A Neural Network for Travel Time Prediction Based on Tensor Decomposition and Graph Embedding," in IEEE Transactions on Knowledge and Data Engineering, doi: 10.1109/TKDE.2020.3038259.
  ```

#### 路网匹配

* **ST-Matching**

  该模型考虑了（1）道路网络的空间几何和拓扑结构，以及（2）轨迹的时间/速度约束，并专门为低采样率的GPS轨迹设计。

  ```
  Lou Y, Zhang C, Zheng Y, Wang W, Huang Y. Map-Matching for low-sampling-rate GPS trajectories. In: Proc. of the ACM-GIS.  2009. 352−361.
  ```

* **IVMM**

  该模型不仅考虑了GPS轨迹的空间和时间信息，而且还设计了一个基于投票的策略来模拟GPS点之间的加权相互影响。

  ```
  Yuan J, Zheng Y, Zhang C, Xie X, Sun JZ. An interactive-voting based map matching algorithm. In: Proc. of the MDM. 2010.  43−52. [doi: 10.1109/MDM.2010.14]
  ```

* **HMMM**

  该模型是一种新颖的、有原则的地图匹配算法，它使用隐马尔可夫模型（HMM）来寻找最可能的道路路线，该路线由有时间戳的经/纬度对序列代表。HMM优雅地考虑了测量噪声和道路网络的布局。

  ```
  Newson P, Krumm J. Hidden Markov map matching through noise and sparseness. In: Proc. of the ACM-GIS. 2009.  336−343. [doi: 10.1145/1653771.1653818]
  ```

#### 路网表征学习

- **ChebConv**

  该模型使用基于切比雪夫多项式近似的图卷积模型计算路网表征。

  ```
  Defferrard, M., Bresson, X., & Vandergheynst, P. (2016). Convolutional neural networks on graphs with fast localized spectral filtering. Advances in neural information processing systems, 29, 3844-3852.
  ```

- **LINE**

  适合大规模图结构的图嵌入模型，同时考虑一阶和二阶近似。

  ```
  Tang, J., Qu, M., Wang, M., Zhang, M., Yan, J., & Mei, Q. (2015, May). Line: Large-scale information network embedding. In Proceedings of the 24th international conference on world wide web (pp. 1067-1077).
  ```

