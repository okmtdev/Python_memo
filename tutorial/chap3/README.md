# 3章 気楽な入門編

四則演算を試してみる

```python
python
Python 3.9.6 (default, Aug  4 2023, 13:19:08)
[Clang 13.1.6 (clang-1316.0.21.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5
1.6 # 除算は常に浮動小数点数を返す
>>> 17 / 3
5.666666666666667
>>> 17 // 3
5
>>> 17 % 3
2
>>> 5 * 3 + 2
17
>>> 5 ** 2
25
>>> 2 ** 7
128
>> 4 * 3.75 - 1
14.0 # 整数は浮動小数点数に変換される
```

対話モードでは最後に表示した式を変数「_」に代入してある

```python
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

シングルクォートを表示したい場合、`\`でエスケープするかダブルクォートを使う

逆に`\`を前置した文字が特殊文字として解釈されるのが嫌な時はraw文字列`r`を使えば良い

```python
>>> print('C:\some\name')
C:\some
ame
>>> print(r'C:\some\name')
C:\some\name
```

スライス操作もサポートされている


```python
>>> word = 'Python'
>>> word[0:2]
'Py'
>>> word[2:5]
'tho'
>>> word[2:]
'thon'
>>> word[:2]
'Py'
>>> word[-2:]
'on'
```

Pythonの文字列はimmutableなので改変できない

```python
word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

リスト操作を試してみる

```python
>>> squares = [1, 4, 9, 16, 25]
>>> squares[0]
1
>>> squares[-1]
25
>>> squares[-3:]
[9, 16, 25]
>>> squares + [36, 49]
[1, 4, 9, 16, 25, 36, 49]
>>> squares.append(65) # appendで追加ができる
>>> squares
[1, 4, 9, 16, 25, 65]
>>> squares[5] = 64 # リストはmutableなので要素を入れ替えることができる
>>> squares
[1, 4, 9, 16, 25, 64]
>>> len(squares) # 長さ
6
```

フィボナッチを試してみる

```python
>>> a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8
```