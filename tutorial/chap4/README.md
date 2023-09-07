# 4章 制御構造ツール

if文

```
if 条件1:
    ~
elif 条件2:
    ~
elif 条件3:
    ~
else:
    ~
```

for文

```
>>> for w in ['cat', 'window', 'defenestrate']:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12
```

range()関数

```
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4

>>> for i in range(0, 10, 3):
...     print(i)
...
0
3
6
9
```

range()関数が返すオブジェクトはlistではなく、シーケンスのアイテムを連続的に返す反復可能体（iterable）というオブジェクト

以下のような使い方ができる

```
>>> sum(range(4))
6
>>> list(range(4))
[0, 1, 2, 3]
```

breakはforまたはwhileのループから抜ける

continueはループの残りを飛ばして次回の反復にいく

passは何もしない。構文的に文が必要だがプログラム的には何もする必要がないときに使う

以下のように最小のクラスを生成するのに使われたりもする

```
class MyEmptyClass:
    pass
```

関数定義の例をフィボナッチ級数の関数で示す

```
def fib(n)
    """nまでのフィボナッチ級数を表示する"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
```

```
>>> fib
<function fib at 10042ed0>
>>> f = fib 
>>> f(100)
0 1 1 2 3 5 8 13 21 34 55 89
```

引数のデフォルト値

```
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    ...
```

`ask_ok`は色々な呼び出し方ができる

```
ask_ok('aa')
ask_ok('aa', 2)
ask_ok('aa', 2, 'bb)
```

キーワード引数

```
def parrot(voltage, state='a stiff', action='voom'):
    ...
```

上記関数は必須の引数を一つ（voltage）、オプション引数を2つとる（state, action）

```
parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000, action='VOOOM')
```

仮引数の最後が`**名前`の形になっていると、この引数はディレクショナリを受け取る

このディクショナリには仮引数に対応するキーワードを除いた、全てのキーワード引数が入っている

また、キーワード引数の表示順序は関数のコール時に与えられた順序が保証される

任意引数のリスト

```
def concat(*args, sep="/"):
    return sep.join(args)
```

```
>>> concat("a", "b", "c")
'a/b/c'

>>> concat("a", "b", "c", sep=".")
'a.b.c'
```

`**演算子`を使えばディクショナリをキーワード引数にして直すことができる

```
def parrot(voltage, state='a stiff', action='voom'):
    ...
```

```
>>> d = {"voltage": "a", "state": "b", "action": "c"}
>>> parrot(**d)
```

lambda式

`lambda a, b: a+b`は2つの引数の和を返す関数

```
>>> def make_incrementor(n):
        return lambda x: x + n

>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```

小さな関数を引数として渡すときにも使える

```
>>> pairs = [{1, 'one'}, {2, 'two'}, {3, 'three'}]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[{1, 'one'}, {3, 'three'}, {2, 'two'}]
```

docstring

1行目はオブジェクトの目的の短い要約斗する

2行目は空行、3行目から使い方や副作用を記述するべき

`__doc__`を呼び出すと出力可能

関数注釈はユーザ定義関数で使われる型についての完全任意のメタデータ情報

`__annotations__`属性にディクショナリとして格納される



