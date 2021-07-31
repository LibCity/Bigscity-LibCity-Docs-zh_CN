## 基于[Sphinx](http://sphinx-doc.org/)的[项目文档](https://bigscity-libtraffic-docs.readthedocs.io/en/latest/)

两种部署的方式：

### [Read the Docs](https://readthedocs.org/)

更新方法：

每次将修改推送到Github后，Read the Docs会自动拉取最新的提交，自动编译生成最新版网站。

### [Github Page](https://pages.github.com/) [已被淘汰]

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

首先从Github拉取代码，目录为`Bigscity-LibTraffic-Docs/`。

需要修改的文件位于`source/`，编译输出的文件位于`build/`。

主页面文件是`source/index.rst`，此文件引用了`get_started/`，`user_guide/`，`developer_guide/`，`libtraffic/`四个目录下的内容，其中前三个目录分别放置Markdown文件。

`source/index.rst`的每一行例如`user_guide/config_settings`在网站的目录中显示为一行。

修改对应的Markdown文件以及主文件即可完成修改。

第四个目录`libtraffic/`则是代码API文档的目录，详见后文。

## 代码API文档自动生成

### 使用Github Page的部署方式 [已被淘汰]

此方法在本地完成编译，不需要将项目代码提交到项目文档仓库。

（1）保证文档目录`Bigscity-LibTraffic-Docs/`跟代码目录`Bigscity-LibTraffic/`处于平级目录

（2）设置conf.py

```python
sys.path.insert(0, os.path.abspath('../../Bigscity-LibTraffic/'))
```

（3）在`Bigscity-LibTraffic-Docs/`目录下执行如下命令：

```shell
sphinx-apidoc -o source/libtraffic/ -e -f ../Bigscity-LibTraffic/libtraffic/
python source/clear.py
make html
```

编译完成后，将`/build/html`目录下的文件复制到`/docs`目录下，上传到Github即可。

`make html`过程中可能提示一些代码注释的warning，需要后续制定代码注释规范以自动生成文档。

`make html`需要待生成API文档的代码的相关依赖项，本地配置起来比较简单。

### 使用Read the Docs的部署方式

此方法在远程完成编译，需要将项目代码提交到项目文档仓库，因此在目录`Bigscity-LibTraffic-Docs/libtraffic`中存储项目代码。

（1）设置conf.py

```python
sys.path.insert(0, os.path.abspath('../'))
```

（2）在`Bigscity-LibTraffic-Docs/`目录下执行如下命令：

```shell
sphinx-apidoc -o source/libtraffic/ -e -f ./libtraffic/
python source/clear.py
```

（3）最后直接把修改推送到Github即可，可以自动部署。

提示：最好先在本地编译（`make html`）看看输出结果的样子，可能会出现很多的warning。

### 代码注释规范

1. 使用[Google注释风格](https://www.sphinx.org.cn/usage/extensions/example_google.html?highlight=comments)。

2. Pycharms中可以修改默认设置，方法为Settings > Tools > Python Integrated Tools > Docstring format修改为Google。

3. 示例：

   ```python
   """一段基础的描述
   【空行】
   一段详细的描述
   【空行】
   Args:
       参数1名(参数类型): 参数1介绍
       参数2名(参数类型): 参数2介绍
       ...
   【空行】
   Returns: # 单返回值
       返回值类型: 返回值介绍
   
   Returns: # 多返回值
   	tuple: tuple contains:
   		返回值1的类型：返回值1的介绍
   		返回值2的类型：返回值2的介绍
   		...
   
   """
   ```

- 每一个部分都是可以省略的，可以只保留一段基础描述或详细描述。
- 注意各部分之间要有空行，Return的最后可以没有空行。

