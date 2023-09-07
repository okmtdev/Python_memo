# 付録A 用語

- 2to3: Python2.xコードをPython3.xコードに変換するツール。標準ライブラリにも存在する
- BDFL: Benevolent Dictator For Life。Pythonの作者
- CPyhton: Pythonの基準実装であり、python.orgで配布されているもののこと
- docstring: ドキュメンテーション文字列。クラス、関数、モジュールの最初の式として現れる文字列リテラル。`__doc__`属性
- EAFP: Easier to ask for forgiveness than permission
- `__future__`: 原稿インタープリタと互換性のない新しい言語機能を動かすのに使える擬似モジュール。`__future__`モジュールをインポートしてその変数を評価することにより、ある新機能が言語に導入された時期とデフォルトになる時期を知ることができる。
- f文字列: 頭にfのついた文字列リテラルはf文字列と呼ばれ、formatted string literalsの略となる
- global interpreter lock: Pythonバイトコードが同時に一つだけのスレッドで実行されることを保証するためにCPythonインタープリタが用いているメカニズム。
- IDLE: Intergrated Development Environment for Python（Python統合開発環境）。IDLEはPythonの標準ディストリビューション同梱のエディタとインタープリタによる基本的な環境
- lambda: 無名のインライン関数で単一の式により構成されコール時に評価される。lambda関数を生成する構文は「lambda [仮引数]: 式」となる
- LBYL: Look before you leap（転ばぬ先の杖）
- MRO: メソッド解決順
- PRP: Python Enhancement Proposal。