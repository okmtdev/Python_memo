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