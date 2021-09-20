# 安装LibCity

`LibCity`只能通过源代码安装。

请执行以下命令获取源代码。

```shell
git clone https://github.com/LibCity/Bigscity-LibCity
cd Bigscity-LibCity
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

在安装Pytorch后，您可以通过pip使用下面的命令安装LibCity的所有依赖项。

```shell
pip install -r requirements.txt
```

现在，您可以使用`LibCity`，更多细节请参考[快速入门](./quick_start.md)一节。
