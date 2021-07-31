## Reproduced Model List

#### Traffic Flow Prediction

* **AutoEncoder**: 

  This baseline model is implemented by ourselves, which uses an encoder to learn an embedded vector from data and then use a decoder to predict the future traffic state.

* **RNN(FC-RNN)**: 

  This baseline model is implemented by ourselves for traffic state prediction task based on RNN.

* **Seq2Seq**:  

  This baseline model is implemented by ourselves for traffic state prediction task based on Encoder-Decoder structure. We utilize the encode-decoder framework based on gated recurrent unit for multi-step prediction.

* **ST-ResNet**: 

  Spatio-Temporal Residual Networks, which is widely used in grid-based flow prediction task and models the spatio-temporal correlations by residual unit 

  > Junbo Zhang, Yu Zheng, and Dekang Qi. 2017. Deep Spatio-Temporal Residual Networks for Citywide Crowd Flows Prediction. In AAAI. AAAI Press, 1655–1661.

* **ACFM**: 

  Attentive Crowd Flow Machines, which is able to infer the evolution of the crowd flow by learning dynamic representations of temporally-varying data with an attention mechanism.

  > Lingbo Liu, Ruimao Zhang, Jiefeng Peng, Guanbin Li, Bowen Du, and Liang Lin.2018. Attentive Crowd Flow Machines. In ACM Multimedia. ACM, 1553–1561.

* **ASTGCN**: 

  Attention-based spatio-temporal graph convolutional network, which combines the spatial-temporal attention mechanism and the spatial-temporal convolution to capture the dynamic spatial-temporal characteristics.

  > Shengnan Guo, Youfang Lin, Ning Feng, Chao Song, and Huaiyu Wan. 2019.Attention Based Spatial-Temporal Graph Convolutional Networks for Traffic Flow Forecasting. In AAAI. AAAI Press, 922–929.

* **MSTGCN**: 

  A degraded version of ASTGCN, Multi-Component Spatial-Temporal Graph Convolution Networks (MSTGCN), which gets rid of the spatialtemporal attention.

  > Shengnan Guo, Youfang Lin, Ning Feng, Chao Song, and Huaiyu Wan. 2019.Attention Based Spatial-Temporal Graph Convolutional Networks for Traffic Flow Forecasting. In AAAI. AAAI Press, 922–929.

* **AGCRN**: 

  Adaptive Graph Convolutional Recurrent Network, which enhances the traditional graph convolution by adaptive modules and combines them into recurrent networks to capture fine-grained spatial and temporal correlations.

  > Lei Bai, Lina Yao, Can Li, Xianzhi Wang, and Can Wang. 2020. Adaptive Graph Convolutional Recurrent Network for Traffic Forecasting. In NeurIPS.

* **CONVGCN**: 

  Conv-GCN combines a graph convolutional network (GCN) and a three-dimensional (3D) convolutional
  neural network (3D CNN). The 3D CNN was used to innovatively integrate the inflow and outflow information as well as extract high-level correlations between three inflow/outflow patterns, and between stations located nearby and far away.

  > Jinlei Zhang, Feng Chen, Yinan Guo, and Xiaohong Li. 2020. Multi-graph convolutional network for short-term passenger flow forecasting in urban rail transit. IET Intell. Trans. Syst.14, 10 (2020), 1210–1217.

* **STDN**: 

  Spatial-Temporal Dynamic Network (STDN), in which a flow gating mechanism is introduced to learn the dynamic similarity between locations, and a periodically shifted attention mechanism is designed to handle long-term periodic temporal shifting. 

  > Huaxiu Yao, Xianfeng Tang, Hua Wei, Guanjie Zheng, and Zhenhui Li. 2019.Revisiting Spatial-Temporal Similarity: A Deep Learning Framework for Traffic Prediction. In AAAI. AAAI Press, 5668–5675.

* **STSGCN**: 

  Spatial-Temporal Synchronous Graph Convolutional Networks (STSGCN), for spatial-temporal network data forecasting. The model is able to effectively capture the complex localized spatial-temporal correlations through an elaborately designed spatial-temporal synchronous modeling mechanism.

  > Chao Song, Youfang Lin, Shengnan Guo, and Huaiyu Wan. 2020. Spatial-Temporal Synchronous Graph Convolutional Networks: A New Framework for Spatial-Temporal Network Data Forecasting. In AAAI. AAAI Press, 914–921.

* **ToGCN**: 

  Topological Graph Convolutional Network (ToGCN) followed with a Sequence-tosequence (Seq2Seq) framework to predict future traffic flow and density with temporal correlations.

  > Han Qiu, Qinkai Zheng, Mounira Msahli, Gerard Memmi, Meikang Qiu, and Jialiang Lu. 2020. Topological Graph Convolutional Network-Based Urban Traffic Flow and Density Prediction. IEEE Trans. Intell. Transp. Syst.(2020).

* **ResLSTM**: 

  ResLSTM is a deep learning architecture combining the residual network (ResNet), graph convolutional network (GCN), and long short-term memory (LSTM) (called “ResLSTM”) to forecast short-term passenger flow in urban rail transit on a network scale.

  > Jinlei Zhang, Feng Chen, Zhiyong Cui, Yinan Guo, and Yadi Zhu. 2020.  Deep learning architecture for short-term passenger flow forecasting in urban rail transit. IEEE Trans. Intell. Transp. Syst.(2020).

* **CRANN**: 

  CRANN is an interpretable attention-based neural network in which several modules are combined in order to capture key spatio-temporal time series components.

  > Rodrigo  de  Medrano  and  José  Luis  Aznarte.  2020.   A  Spatio-Temporal  Spot-Forecasting Framework forUrban Traffic Prediction. CoRR abs/2003.13977 (2020).

* **Multi-STGCnet**: 

  Multi-STGCnet contains three long short-term memory network (LSTM)-based modules as a temporal component and three spatial matrixes to extract spatial correlation of a target station as a spatial component.

  > Jiexia Ye, Juanjuan Zhao, Kejiang Ye, and Chengzhong Xu. 2020. Multi-STGCnet:A Graph Convolution Based Spatial-Temporal Framework for Subway PassengerFlow Forecasting. In IJCNN. IEEE, 1–8.

* **DGCN**: 

  DGCN is a novel dynamic graph convolution network for traffic forecasting, in which a latent network is introduced to extract spatial-temporal features for constructing the dynamic road network graph matrices adaptively.

  > Kan Guo, Yongli Hu, Zhen Qian, Yanfeng Sun, Junbin Gao, and Baocai Yin. 2020.Dynamic Graph Convolution Network for Traffic Forecasting Based on Latent Network of Laplace Matrix Estimation. IEEE Trans. Intell. Transp. Syst.(2020).

* **DSAN**: 

  Dynamic Switch-Attention Network (DSAN) with a novel Multi-Space Attention (MSA) mechanism, which dynamically extracts valuable information by applying selfattention over the noisy input and bridges each output directly.

  > Haoxing Lin, Rufan Bai, Weijia Jia, Xinyu Yang, and Yongjian You. 2020. Preserving Dynamic Attention for Long-Term Spatial-Temporal Prediction. In KDD. ACM,36–46.

* **STNN**: 

  STNN learns these dependencies through a structured latent dynamical component, while a decoder predicts the observations from the latent representations.

  > Ali Ziat, Edouard Delasalles, Ludovic Denoyer, and Patrick Gallinari. 2018. Spatio-Temporal Neural Networks for Space-Time Series Forecasting and Relations Discovery. CoRRabs/1804.08562 (2018).

#### Traffic Speed Prediction

* **AutoEncoder**: 

  This baseline model is implemented by ourselves, which uses an encoder to learn an embedded vector from data and then use a decoder to predict the future traffic state.

* **RNN(FC-RNN)**: 

  This baseline model is implemented by ourselves for traffic state prediction task based on RNN.

* **Seq2Seq**:  

  This baseline model is implemented by ourselves for traffic state prediction task based on Encoder-Decoder structure. We utilize the encode-decoder framework based on gated recurrent unit for multi-step prediction.

* **DCRNN**: 

  Diffusion Convolution Recurrent Neural Network, which captures the spatial dependency using graph convolution formulated by diffusion process and the temporal dependency using the encoder-decoder framework.

  > Yaguang Li, Rose Yu, Cyrus Shahabi, and Yan Liu. 2018. Diffusion Convolutional Recurrent Neural Network: Data-Driven Traffic Forecasting. In ICLR (Poster).OpenReview.net.

* **STGCN**:

  Spatial-Temporal Graph Convolutional Network, which combines graph convolutions and gated temporal convolution to capture spatial and temporal correlations. 

  > Bing Yu, Haoteng Yin, and Zhanxing Zhu. 2018. Spatio-Temporal Graph Convolutional Networks: A Deep Learning Framework for Traffic Forecasting. In IJCAI. ijcai.org, 3634–3640.

* **GWNET**: 

  Graph WaveNet, a spatial-temporal graph convolutional network integrating diffusion convolution with 1D dilated casual convolution to capture spatiotemporal dependencies.

  > Zonghan Wu, Shirui Pan, Guodong Long, Jing Jiang, and Chengqi Zhang. 2019.Graph Wave Net for Deep Spatial-Temporal Graph Modeling. In IJCAI. ijcai.org,1907–1913.

* **MTGNN**: 

  A graph neural network framework designed specifically for multivariate time series data, which combines graph convolutional network with mix-hop propagation layer and dilated inception layer to capture the spatial and temporal dependencies.

  > Zonghan Wu, Shirui Pan, Guodong Long, Jing Jiang, Xiaojun Chang, and Chengqi Zhang. 2020.  Connecting the Dots: Multivariate Time Series Forecasting with Graph Neural Networks. In KDD. ACM, 753–763.

* **TGCN**: 

  Temporal Graph Convolution Model, which is in combination with the graph convolutional network and gated recurrent unit to capture spatial and temporal correlations.

  > Ling Zhao, Yujiao Song, Chao Zhang, Yu Liu, Pu Wang, Tao Lin, Min Deng, and Haifeng Li. 2020. T-GCN: A Temporal Graph Convolutional Network for Traffic Prediction. IEEE Trans. Intell. Transp. Syst.21, 9 (2020), 3848–385.

* **TGCLSTM**: 

  Traffic Graph Convolutional Long Short-Term Memory Neural Network (TGC-LSTM), to learn the interactions between roadways in the traffic network and forecast the network-wide traffic state.

  > Zhiyong Cui, Kristian Henrickson, Ruimin Ke, and Yinhai Wang. 2020.  Traffic Graph Convolutional Recurrent Neural Network: A Deep Learning Frame work for Network-Scale Traffic Learning and Forecasting. IEEE Trans. Intell. Transp.Syst.21, 11 (2020), 4883–4894.

* **ATDM**: 

  ATDM is a model with the use of prior spatial knowledge. It is a convolution-based neural network for regression with their respective spatial agnostic versions.

  > Rodrigo de Medrano and José Luis Aznarte. 2020.  On the Inclusion of Spatial Information for Spatio-Temporal Neural Networks. CoRR abs/2007.07559 (2020).

* **GMAN**: 

  GMAN adapts an encoder-decoder architecture, where both the encoder and the decoder consist of multiple spatio-temporal attention blocks to model the impact of the spatio-temporal factors on traffic conditions.

  > Chuanpan Zheng, Xiaoliang Fan, Cheng Wang, and Jianzhong Qi. 2020. GMAN:A Graph Multi-Attention Network for Traffic Prediction. In AAAI. AAAI Press,1234–1241.

* **GTS**: 

  GTS is a learning the structure simultaneously with the GNN if the graph is unknown, and is a probabilistic graph model through optimizing the mean performance over the graph distribution.

  > Chao Shang, Jie Chen, and Jinbo Bi. 2021. Discrete Graph Structure Learning forForecasting Multiple Time Series. CoRR abs/2101.06861 (2021).

* **STAGGCN**: 

  STAGGCN exploits spatio-temporal correlation of urban traffic flow and construct a dynamic weighted graph by seeking both spatial neighbors and semantic neighbors of road nodes.

  > Bin Lu, Xiaoying Gan, Haiming Jin, Luoyi Fu, and Haisong Zhang. 2020.  Spa-tiotemporal Adaptive Gated Graph Convolution Network for Urban Traffic FlowForecasting. In CIKM. ACM, 1025–1034.

* **HGCN**: 

  Hierarchical Graph Convolution Networks (HGCN) for traffic forecasting by operating on both the micro and macro traffic graphs.

  > Kan Guo, Yongli Hu, Yanfeng Sun, Sean Qian, Junbin Gao, and Baocai Yin. 2021.Hierarchical Graph Convolution Networks for Traffic Forecasting. (2021).

* **ST-MGAT**: 

  Spatial-Temporal Multi-head Graph ATtention network (ST-MGAT), which build convolutions on the graph directly and consider the features of neighborhood nodes and the weights of the edges to generate new node representation.

  > Kelang Tian, Jingjie Guo, Kejiang Ye, and Cheng-Zhong Xu. 2020.  ST-MGAT:Spatial-Temporal Multi-Head Graph Attention Networks for Traffic Forecasting. In ICTAI. IEEE, 714–721.

* **DKFN**:  

  Deep Kalman Filtering Network (DKFN) to forecast the network-wide traffic state by modeling the self and neighbor dependencies as two streams, and their predictions are fused under the statistical theory and optimized through the Kalman filtering network.

  > Fanglan Chen, Zhiqian Chen, Subhodip Biswas, Shuo Lei, Naren Ramakrishnan,and Chang-Tien Lu. 2020. Graph Convolutional Networks with Kalman Filtering for Traffic Prediction. In SIGSPATIAL/GIS. ACM, 135–138.

#### On-Demand Service Prediction 

* **AutoEncoder**: 

  This baseline model is implemented by ourselves, which uses an encoder to learn an embedded vector from data and then use a decoder to predict the future traffic state.

* **RNN(FC-RNN)**: 

  This baseline model is implemented by ourselves for traffic state prediction task based on RNN.

* **Seq2Seq**:  

  This baseline model is implemented by ourselves for traffic state prediction task based on Encoder-Decoder structure. We utilize the encode-decoder framework based on gated recurrent unit for multi-step prediction.

* **DMVSTNET**: 

  Deep Multi-View Spatial-Temporal Network (DMVST-Net) framework to model both spatial and temporal relations. It consists of three views: temporal view, spatial view, and semantic view.

  > Huaxiu Yao, Fei Wu, Jintao Ke, Xianfeng Tang, Yitian Jia, Siyu Lu, Pinghua Gong, Jieping Ye, and Zhenhui Li. 2018. Deep Multi-View Spatial-Temporal Network for Taxi Demand Prediction. In AAAI. AAAI Press, 2588.

* **STG2Seq**: 

  STG2Seq is a model for multistep citywide passenger demand prediction based on a graph and use a hierarchical graph convolutional structure to capture both spatial and temporal correlations simultaneously.

  > Lei Bai, Lina Yao, Salil S. Kanhere, Xianzhi Wang, and Quan Z. Sheng. 2019. STG2Seq: Spatial-Temporal Graph to Sequence Model for Multi-step Passenger Demand Forecasting. In IJCAI. ijcai.org, 1981-1987.

* **CCRNN**: 

  CCRNN is a model to capture multi-level spatial dependence. The adjacency matrices in CGC were self-learned and varied from layer to layer. A layer-wise coupling mechanism was employed to bridge the upper-level graph structure with the lowerlevel one.

  > Junchen Ye, Leilei Sun, Bowen Du, Yanjie Fu, and Hui Xiong. 2021.  Coupled Layer-wise Graph Convolution for Transportation Demand Prediction. In AAAI. AAAI Press, 4617–4625.

#### Trajectory Next-Location Prediction

* **FPMC**:  

  This is a classical baseline model of sequence recommendation task. This model is often used as a baseline model in the early research period of trajectory prediction field.
	> Steffen Rendle, Christoph Freudenthaler, and Lars Schmidt-Thieme. 2010. Factorizing personalized Markov chains for next-basket recommendation. In WWW ACM, 811–820.

* **RNN**:
	This baseline model is implemented by ourselves.

* **ST-RNN**:
	This model focuses on introducing spatiotemporal transfer features into the hidden layer of RNN.
	> Qiang Liu, Shu Wu, Liang Wang, and Tieniu Tan. 2016. Predicting the Next Location: A Recurrent Model with Spatial and Temporal Contexts. In AAAI. AAAI Press, 194–200.

* **ATST-LSTM**:
	This model introduces the distance difference and time difference between the trajectory points into the LSTM, and uses a Attention mechanism.
	> Liwei Huang, Yutao Ma, Shibo Wang, and Yanbo Liu. 2019. An attention-based spatiotemporal lstm network for next poi recommendation. IEEE Transactions on Services Computing(2019).

* **SERM**：
	This model introduces the sematic information of the trajectory into the network.
	> Di Yao, Chao Zhang, Jian-Hui Huang, and Jingping Bi. 2017. SERM: A Recurrent Model for Next Location Prediction in Semantic Trajectories. In CIKM. ACM,2411–24.

* **DeepMove**: 
	This model uses the attention mechanism for the first time to combine historical trajectories with current trajectories for prediction.
	> Jie Feng, Yong Li, Chao Zhang, Funing Sun, Fanchao Meng, Ang Guo, and Depeng Jin. 2018. DeepMove: Predicting Human Mobility with Attentional Recurrent Networks. In WWW. ACM, 1459–1468.

* **HST-LSTM**:
	This model also introduces spatio-temporal transfer factors into LSTM, and uses an encoder-decoder structure for prediction.
	> Dejiang Kong and Fei Wu. 2018.  HST-LSTM: A Hierarchical Spatial-Temporal Long-Short Term Memory Network for Location Prediction. In IJCAI. ijcai.org,2341–2347.

* **LSTPM**:
	The model uses two special designed LSTMs to capture the user's long-term mobile preferences and short-term mobile preferences to jointly predition next location.
	> Ke Sun, Tieyun Qian, Tong Chen, Yile Liang, Quoc Viet Hung Nguyen, and HongzhiYin. 2020. Where to Go Next: Modeling Long- and Short-Term User Preferences for Point-of-Interest Recommendation. In AAAI. AAAI Press, 214-221.

* **GeoSAN**:
	The model uses a self-attention mechanism to realize the representation learning of POI, so as to make predictions based on the representation.
	> Defu Lian, Yongji Wu, Yong Ge, Xing Xie, and Enhong Chen. 2020. Geography-Aware Sequential Location Recommendation. In KDD. ACM, 2009–2019.

* **STAN**:
	The model uses a self-attention mechanism to capture spatio-temporal information to directly make predictions.
	> Yingtao Luo, Qiang Liu, and Zhaocheng Liu. 2021. STAN: Spatio-Temporal Attention Network for Next Location Recommendation. CoRR abs/2102.04095 (2021).

* **CARA**:
	The model focuses on using the attention mechanism to extract contextual information between trajectories for prediction.
	> Jarana Manotumruksa, Craig Macdonald, and Iadh Ounis. 2018.  A Contextual Attention Recurrent Architecture for Context-Aware Venue Recommendation. In SIGIR. ACM, 555–564.
