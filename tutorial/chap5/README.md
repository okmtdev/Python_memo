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

