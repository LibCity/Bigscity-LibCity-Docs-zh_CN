# 安装和快速上手

## 安装LibTraffic

### 从源代码安装

LibTraffic目前可以从源代码安装。

请执行下列命令来获得源代码。

```
git clone https://github.com/LibTraffic/Bigscity-LibTraffic.git
cd Bigscity-LibTraffic
```

### 配置依赖

在获得了源代码后，我们可以配置环境。

我们的代码是基于Python 3.7版本和PyTorch 1.7.1版本。您可以点击[这里](https://pytorch.org/get-started/previous-versions/#v171)来了解如何安装PyTorch。例如，您的CUDA版本是10.2，您可以使用下列指令安装PyTorch。

Pip:

```
pip install torch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2
```

Conda:

```
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=10.2 -c pytorch
```

在安装PyTorch后，我们可以通过pip使用下列命令安装`LibTraffic`的所有依赖。

```
pip install -r requirements.txt
```

现在，我们就可以使用`LibTraffic`了，更多的细节可以看`Quick Start`一节。

值得注意的是，大多数模型依赖的包都记录在了`requirements.txt`中。除了以上需要的包，`STAGGCN`模型的实现需要依赖第三方库`torch-geometric`。如果您想运行这个模型，请参考[这里](https://github.com/rusty1s/pytorch_geometric)来根据您的环境安装这个包，并可以取消`libtraffic/model/traffic_speed_prediction/STAGGCN.py`第五行的注释。

## 快速上手

### 下载一个数据集

LibTraffic中使用的数据集是以一种统一的[原子文件](https://bigscity-libtraffic-docs.readthedocs.io/zh/latest/user_guide/data/atomic_files.html)格式存储的。

为了直接在`LibTraffic`中使用[原始数据集](https://bigscity-libtraffic-docs.readthedocs.io/zh/latest/user_guide/data/raw_data.html)，我们已经将所有这些数据集转换成了原子文件的格式，并提供了[转换工具](https://github.com/LibTraffic/Bigscity-LibTraffic-Datasets)。

您可以直接下载我们处理好的数据集。数据集链接是[百度网盘](https://pan.baidu.com/s/1qEfcXBO-QwZfiT0G3IYMpQ)（提取码：1231）或[Google Drive](https://drive.google.com/drive/folders/1g5v2Gq1tkOq8XO0HDCZ9nOTtRpB6-gPe?usp=sharing)。

在运行`LibTraffic`的模型前，请确保您至少下载了一个数据集，并把它放在了`Bigscity-LibTraffic/raw_data/dataset_name/*`目录下。

例如，如果您下载了METR_LA数据集，目录结构如下所示：

- `Bigscity-LibTraffic/raw_data/METR_LA/METR_LA.geo`
- `Bigscity-LibTraffic/raw_data/METR_LA/METR_LA.rel`
- `Bigscity-LibTraffic/raw_data/METR_LA/METR_LA.dyna`
- `Bigscity-LibTraffic/raw_data/METR_LA/config.json`

### 运行模型流水线

用于训练和评测一个模型的脚本`run_model.py`位于项目根目录中，它提供了一系列命令行参数，使用户可以调整运行参数配置。

当运行`run_model.py`时，您必须声明三个参数，分别是`task`、`dataset`和`model`。例如：

```
python run_model.py --task traffic_state_pred --model GRU --dataset METR_LA
```

这个脚本会在默认参数配置下，在METR_LA数据集上运行GRU模型，执行交通状态预测任务。

此外，这个脚本还支持输入下面的这些命令行参数，用于调整流水线的参数设置。

支持的参数有：

- `task`：要执行的任务名，包括`traffic_state_pred`和`traj_loc_pred`。默认为`traffic_state_pred`.
- `model`：要执行的模型名。默认为`GRU`。（[支持的模型](https://bigscity-libtraffic-docs.readthedocs.io/zh/latest/user_guide/model.html)）
- `dataset`：要执行的数据集。默认为`METR_LA`。（[支持的数据集](https://bigscity-libtraffic-docs.readthedocs.io/zh/latest/user_guide/data/raw_data.html)）
- `config_file`：用户自定义的配置文件名。默认为`None`。（[了解更多](https://bigscity-libtraffic-docs.readthedocs.io/zh/latest/user_guide/config_settings.html)）
- `saved_model`：是否保存训练好的模型。默认为`True`。
- `train`：如果模型已经预训练过了，是否要重新训练模型。默认为`True`。
- `batch_size`：训练集和验证集的批次大小。
- `train_rate`：训练集在整个数据集中所占的比例。（划分的顺序是训练集、验证集、测试集）
- `eval_rate`：验证集在整个数据集中所占的比例。
- `learning_rate`：学习率。不同的模型默认的学习率可能是不同的，请参考相关的配置文件了解更多细节。
- `max_epoch`：最大的训练轮数。默认值随模型变化而变化。
- `gpu`：是否使用GPU。默认为`True`。
- `gpu_id`：使用的GPU的ID。默认为`0`。