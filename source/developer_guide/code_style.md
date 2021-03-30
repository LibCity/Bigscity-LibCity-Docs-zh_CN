# Code Style

Every major open-source project has its own style guide: a set of conventions (sometimes arbitrary) about how to write code for that project. It is much easier to understand a large codebase when all the code in it is in a consistent style.

The code style of our project basically follows [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) ([Chinese version](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/contents/)). In order to better manage the quality of the code submitted by each co-developer, the project uses the python lint tool [flake8](https://flake8.pycqa.org/en/latest/) to find potential bugs and style problems in source code.

### Working with Flake8

Besides using flake8, the project also uses [pep8-naming](https://github.com/PyCQA/pep8-naming), a plugin for flake8, to check code naming style. Please install flake8 and pep8-naming according to `/requirements.txt`.

After installing flake8, we recommend you to integrate flake8 into Git pre-commit hook. For example, you can running following commands:

```shell
$ flake8 --install-hook git
$ git config --bool flake8.strict true
```

Now, whenever you create a git commit, flake8 will automatically check the code style of your commit and prevent you from submitting bad codes.

### Project Flake8 Configuration

Although the project basically follows the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html), we have made certain modifications to some uncomfortable specifications. The modifications we made will be recorded in detail, seeing below.

* `max-line-length`: We change the maximum line length from 80 characters to 120 characters.