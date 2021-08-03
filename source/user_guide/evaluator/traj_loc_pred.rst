交通轨迹预测评估器
================

评估指标
--------

对于轨迹下一跳预测任务，本评估器实现了一系列基于 TopK 的评估指标：

* Precision@K
  
  - R(u) 为根据用户在训练集上的行为给用户作出的预测列表。
  
  - T(u) 为用户在测试集上的行为列表。
  
  - 准确率 \ :math:`Precision=\frac{\sum_{u}|R(u)\bigcap T(u)|}{\sum_{u}|R(u)|}`\。

* Recall@K

  * 召回率 \ :math:`Recall=\frac{\sum_{u}|R(u)\bigcap T(u)|}{\sum_{u}|T(u)|}`\

  * 对于交通轨迹预测，下一跳仅有一个ground-truth，因此 \ :math:`Precision=\frac{Recall}{topk}`\。

* F1-score@K

  * \ :math:`F1=\frac{2*Recall*Precision}{Recall+Precision}`\

* MRR(Mean Reciprocal Rank)@K

  * rank(u) 为该用户预测列表第一个ground-truth所在排列位置。

  * \ :math:`MRR=\sum_u\frac{1}{rank(u)}`\

* MAP(Mean Average Precision)@K

  * \ :math:`Precision=f(Recall)`\

  * AP(Average Precision)：\ :math:`\int_0^1f(r)\text{d}r`\，不同召回率下的准确率平均值。

  * 对于交通轨迹预测，下一跳仅有一个ground-truth，即召回率为 1，准确率为 \ :math:`\frac{1}{rank}`\，因此\ :math:`AP_u=\frac{1}{rank(u)}`\。

  * \ :math:`MAP=\frac{\sum_{u\in U}AP_u}{|T(u)|}`\

* NDCG(Normalized Discounted Cumulative Gain)@K

  * CG(Cumulative Gain)：\ :math:`\sum_u{rel(u)}`\，其中 rel(u) 表示相关性分数，\ :math:`rel\in\{0,1\}`\。
  
  * DCG(Discounted Cumulative Gain)：\ :math:`\sum_u \frac{rel(u)}{\log_2(rank(u)+1)}`\，考虑排序顺序的因素，对排名靠后的物品进行折损。
  
  * NDCG：\ :math:`\frac{DCG}{IDCG}`\，对 DCG 归一化，IDCG 为理想情况下最大的 DCG 值，实现中为 1。

可以通过在用户自定义 Config 文件中加入 ``metrics`` 与 ``topk`` 两个参数，来控制本评估器使用哪些评估方法。

评估设置
--------

* ``metrics (list of string)``: 默认值为 ``["Recall"]``。可选参数为 ``["Precision", "Recall", "F1", "MRR", "MAP", "NDCG"]``。

* ``topk (int)``: 默认值为 ``1``。

