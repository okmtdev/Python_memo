# Ruff

静的コード解析ツール、フォーマッター


https://gihyo.jp/article/2023/03/monthly-python-2303

```
rye run ruff app/database.py
app/database.py:1:1: I001 [*] Import block is un-sorted or un-formatted
Found 1 error.
[*] 1 potentially fixable with the --fix option.
```

```
rye run ruff app/database.py --fix
Found 1 error (1 fixed, 0 remaining).
```