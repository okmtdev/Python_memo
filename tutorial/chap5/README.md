# 5章 データ構造

リスト`list`にはメソッドが提供されている

- list.append(x): 末尾にxを追加
- list.extend(iterable): 末尾に反復可能体iterableの全アイテムを追加する
- list.insert(i, x): 指定された位置にxを追加
- list.remove(x): xに等しい最初のアイテムを削除する
- list.pop([i]): 指定された位置のアイテムをリストから削除し、このアイテムを返す。indexが指定されないとリストの最後のアイテムをリストから削除する
- list.clear(): リストから全てのアイテムを削除する
- list.index(x[, start[, end]]): 値がxに等しい最初のアイテムのindexを返す
- list.count(x): リスト中のxの個数を返す
- list.sort(key=None, reverse=False): リストをインプレースでソートする
- list.reverse(): リストの要素をインプレースで逆順にする
- list.copy(): リストのシャローコピーを返す 

リストをスタックとして使う場合、スタックのトップにアイテムを積むにはappend()、スタックのトップからアイテムを取得するにはpop()

リストをキューとして使う場合、リストの末尾でappendやpopするのは高速だが、リストの先頭でのinsertやpopは低速なので、collections.dequeを使うべき

```
from collections import deque
queue = deque(["Eric", "John"])
queue.append("Terry")
queue.popleft()
queue # queue(["John", ""Terry])
```

リスト内包

```
squares = []
for x in range(10):
    squares.append(x**2)
```

以下のように書くと副作用無く書ける

```
squares = list(map(lambda x: x**2, range(10)))
```

別の書き方

```
squares = [x**2 for x in range(10)]
```

より簡潔で読みやすい

リスト内包には複合式や入れ子の関数を含むことができる

```
[str(round(pi, i)) for i in range(1, 6)]
```

入れ子のリスト内包


```
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
]
[[row[i] for row in matrix] for i in range(4)]
```

del文

```
del a[0]
```

pop()メソッドと違って値を返さない

変数やリストの丸ごと消去にも使える

```
del a
```

タプルとシーケンス

```

```

タプルは変更不可能、immutableなリストのこと

アイテム代入はサポートしていないが、可変オブジェクトは格納可能

```
# タプル・パッキング
t = 1, 2, 'hello!'
```

```
# シーケンス・アンパッキング
x, y, z = t
```

集合（set）

存在判定や重複エントリの排除

```
a = {'x', 'y', 'x', 'z'}
print(a)
{'x', 'y', 'z'}
```

集合演算もサポートしている

ディクショナリ

辞書内包

```
{x: x**2 for x in (2, 4, 6)}
```




