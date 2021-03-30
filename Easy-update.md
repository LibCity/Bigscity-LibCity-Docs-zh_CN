## 基于[Sphinx](http://sphinx-doc.org/)的项目文档

两种部署的方式：

### [Read the Docs](https://readthedocs.org/)

访问：https://bigscity-trafficdl-docs.readthedocs.io/zh_CN/latest/

更新方法：

每次将修改推送到Github后，Read the Docs会自动拉取最新的提交，自动编译生成最新版网站。

缺点：

部署后的网页有广告；自动拉取比较慢，经常编译失败；为代码生成文档功能部分页面显示失败，应该需要修改requirements.txt的内容，还有些依赖需要使用conf.py配置。

### [Github Page](https://pages.github.com/)

访问：https://aptx1231.github.io/Bigscity-TrafficDL-Docs/

更新方法：

每次修改后，需要在本地手动`make html`以得到最新版网页内容，输出内容存储于`/build`目录，之后将`/build/html/`目录下的内容复制到`docs/`目录下，之后将`docs/`目录下的内容也要提交到Github，之后Github Page会自动将`docs/`目录下的内容更新到网站上，注意需要配置`docs/`目录下的`.nojekyll`文件。

## Sphinx使用教程

安装：

```shell
pip install Sphinx==3.3.1
pip install sphinx_rtd_theme        # 安装网页样式
pip install sphinx-markdown-tables  # 支持表格显示
pip install recommonmark            # 支持Markdown显示
```

> 注意版本号，不要使用3.4及以上，影响搜索功能。

编译命令

```shell
make clean  # 清除build目录
make html   # 生成html
```

内置的扩展，详见[参考](https://www.sphinx.org.cn/usage/extensions/index.html#built-in-extensions)：

- sphinx.ext.autodoc        生成API文档
- sphinx.ext.viewcode      显示到源代码的链接
- sphinx.ext.todo              支持TODO
- sphinx.ext.napoleon      支持NumPy和Google风格的文档字符串
- sphinx.ext.doctest          测试文档中的代码片段
- sphinx.ext.autosummary        生成autodoc摘要
- sphinx.ext.githubpages            支持Github Page，生成`.nojekyll`文件。
- sphinx.ext.mathjax                    支持数学公式
- sphinx.ext.intersphinx              链接到其他项目的文档

修改方式

首先从Github拉取代码，目录为`Bigscity-TrafficDL-Docs/`。

需要修改的文件位于`source/`，编译输出的文件位于`build/`。

主页面文件是`source/index.rst`，此文件引用了`get_started/`，`user_guide/`，`developer_guide/`，`trafficdl/`四个目录下的内容，其中前三个目录分别放置Markdown文件。

`source/index.rst`的每一行例如`user_guide/config_settings`在网站中显示为一个可折叠的行，Markdown内部的标题用于折叠内容，`source/index.rst`的`:caption:`表示标题，显示为蓝色。

修改对应的Markdown文件以及主文件即可完成修改。

第四个目录`trafficdl/`则是代码API文档的目录，详见后文。

## 代码API文档自动生成

将代码中用三个双引号包裹的注释内容转换成代码文档，层次分明。

### 使用Github Page的部署方式

> 首先保证文档目录Bigscity-TrafficDL-Docs/跟代码目录Bigscity-TrafficDL/处于平级目录

当代码发生修改后，使用如下步骤修改API文档：

在`Bigscity-TrafficDL-Docs/`目录下执行如下命令：

```shell
sphinx-apidoc -o source/trafficdl/ -e -f ../Bigscity-TrafficDL/trafficdl/
python source/clear.py
make html
```

编译完成后，将`/build/html`目录下的文件复制到`/docs`目录下，上传到Github即可。

`make html`过程中可能提示一些代码注释的warning，需要后续制定代码注释规范以自动生成文档。

`make html`需要待生成API文档的代码的相关依赖项，本地配置起来比较简单。

### 使用Read the Docs的部署方式

此功能部署之后暂时不可用，需要配置依赖。