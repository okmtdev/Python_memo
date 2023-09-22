# pyproject.toml

https://peps.python.org/pep-0621/


- pyproject.toml は PEP で提案されているパッケージのビルドに必要なデータを定義するファイルのフォーマット
  - setup.py や setup.cfg の機能を代替し、setuptools 以外のビルドツールを指定できるファイルとして提案
- ツールの設定を書くファイルとして pyproject.toml に対応するケースが増えつつある
- pyproject.toml がプロジェクト管理においてどのような役割を持つのかはそのプロジェクトが採用しているツール次第
- 状況に合わせてpyproject.tomlを使うべきか判断をしていくしかない


Example

```
[project]
name = "spam"
version = "2020.0.0"
description = "Lovely Spam! Wonderful Spam!"
readme = "README.rst"
requires-python = ">=3.8"
license = {file = "LICENSE.txt"}
keywords = ["egg", "bacon", "sausage", "tomatoes", "Lobster Thermidor"]
authors = [
  {email = "hi@pradyunsg.me"},
  {name = "Tzu-ping Chung"}
]
maintainers = [
  {name = "Brett Cannon", email = "brett@python.org"}
]
classifiers = [
  "Development Status :: 4 - Beta",
  "Programming Language :: Python"
]

dependencies = [
  "httpx",
  "gidgethub[httpx]>4.0.0",
  "django>2.1; os_name != 'nt'",
  "django>2.0; os_name == 'nt'"
]

[project.optional-dependencies]
test = [
  "pytest < 5.0.0",
  "pytest-cov[all]"
]

[project.urls]
homepage = "https://example.com"
documentation = "https://readthedocs.org"
repository = "https://github.com"
changelog = "https://github.com/me/spam/blob/master/CHANGELOG.md"

[project.scripts]
spam-cli = "spam:main_cli"

[project.gui-scripts]
spam-gui = "spam:main_gui"

[project.entry-points."spam.magical"]
tomatoes = "spam:main_tomatoes"
```


https://tech.515hikaru.net/post/2019-11-23-pyproject/