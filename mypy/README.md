# mypy

動的型付け言語Pythonでの型チェックライブラリ

```
$ pip install mypy
```

型ヒント

```
num:int
num:int = 100
```

```
def cal_total(num: int) -> int:
    return 200 * num
```

```
num_list: list[int] = [2, 5, 10]
```

実行方法

```
$ mypy プログラムファイル名
```