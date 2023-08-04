# 2章 Pythonインタープリタの使い方

interpreterは`python`でpathが通っていればcommandひとつで起動できる

```
$ python
Python 3.9.6 (default, Aug  4 2023, 13:19:08)
[Clang 13.1.6 (clang-1316.0.21.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

primary prompt`>>>`が出ているときに`quit()`または`Ctrl + D`で終了(exit code 0)できる

`-c`でコマンド実行、`-m`でモジュール指定で起動

```
$ python -c 'print("aiueo")'
aiueo
```

デフォルトではPythonのソースファイルはUTF-8でエンコードしてあるものとして扱われる

デフォルト以外のエンコーディングを行う場合はソースコードの最初の行に特殊コメント行を追加すると

```python
# -*- coding: cp1252 -*-
```

shebangがある場合はshebang配下に記載する

```python
#!/usr/bin/env python3.9
# -*- coding: cp1252 -*-
```