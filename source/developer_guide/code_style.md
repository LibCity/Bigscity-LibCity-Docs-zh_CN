# 代码风格

每个主流开源项目都有其自己的风格指南：关于如何为该项目编写代码的一组约定。当所有代码都采用统一的风格时，更加容易理解大型代码库。

我们的代码风格基本遵循了 [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)（[Chinese version](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/contents/)）。为了更好的管理各合作开发者提交的代码质量，这个项目使用python lint工具[flake8](https://flake8.pycqa.org/en/latest/)来查找潜在的bug和源代码中的风格问题。



### 使用Flake8

除了使用flake8，项目也使用了[pep8-naming](https://github.com/PyCQA/pep8-naming)，一种flake8的插件来检查代码命名风格，请根据requirements.txt安装flake8和pep8-naming库。

在安装了flake8后，我们建议您将flake8集成到Git pre-commit hook中使用。例如，您可以运行下列指令：

```shell
$ flake8 --install-hook git
$ git config --bool flake8.strict true
```

现在，每当您git commit时，flake8都将自动检查您commit的代码风格和并防止您submit错误代码。 



### 项目Flake8配置

虽然这个项目基本遵循了[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)，但我们已经针对一些不合适的规范做出了某些修改。我们做的修改将被详细记录，请见下方。

- `max-line-length`：我们将最大行长度从80个字符更改为120个字符。

