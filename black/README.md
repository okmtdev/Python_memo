 # Black

Black is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters.

Pythonのコードを自動的に成形してくれるツBlack は、妥協のない Python コード フォーマッタです。これを使用すると、手動フォーマットの細部に対する制御を譲渡することに同意したことになります。その代わりに、Black は速度、決定性、およびフォーマットに関する pycodestyle の煩わしさからの自由を提供します。より重要な事柄のために時間と精神的エネルギーを節約できます。

競合ツール: autopep8, yapf, Pylint

[black](https://github.com/psf/black)

Black is already successfully used by many projects, small and big.

Black はすでに大小を問わず多くのプロジェクトでうまく使用されています。

To get started right away with sensible defaults:

適切なデフォルトを指定してすぐに開始するには:

 ```
$ black {source_file_or_directory}
```

You can run Black as a package if running it as a script doesn't work:

Blackをスクリプトとして実行できない場合は、パッケージとして実行できます。

```
$ python -m black {source_file_or_directory}
```