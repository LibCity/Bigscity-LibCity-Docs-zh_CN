# 安装LibTraffic

LibTraffic只能通过源代码安装。

请执行以下命令获取源代码。

```shell
git clone https://github.com/LibTraffic/Bigscity-LibTraffic
cd Bigscity-LibTraffic
```

获取源代码后，您可以配置环境。

我们的代码是基于Python 3.7版本和Pytorch 1.7.1版本。您可以点击[这里](https://pytorch.org/get-started/previous-versions/#v171)查看如何安装Pytorch。例如，如果您的CUDA版本是10.2，可以使用以下命令安装Pytorch。

Pip:

```shell
pip install torch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2
```

Conda:

```shell
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=10.2 -c pytorch
```

在安装Pytorch后，您可以通过pip使用下面的命令安装Libtraffic的所有依赖项。

```shell
pip install -r requirements.txt
```

现在，您可以使用LibTraffic，更多细节请参考[快速入门](./quick_start.md)一节。

值得注意的是，大多数模型依赖的包都记录在`requirements.txt`中。除了以上需要的包，`STAGGCN`模型的实现需要依赖第三方库`torch-geometric`。如果您想运行这个模型，请参考[这里](https://github.com/rusty1s/pytorch_geometric)来根据您的环境安装这个包，并取消`libtraffic/model/traffic_speed_prediction/STAGGCN.py`第五行的注释。