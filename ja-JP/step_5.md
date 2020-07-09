## ループを使って図形を作成する

正方形を作成するのに、何行かコードを繰り返しました。 これは、最も効率的な方法ではありません。 コードを何行も入力する代わりに、ループを使用する方が簡単です。

次のような正方形を作成するコードの代わりに：

```python
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
```

次のように入力します：

```python
for i in range(4):
  elsa.forward(100)
  elsa.right(90)
```

プログラムを保存して実行するとどうなるか、自分でやって確かめてください。

![](images/turtle-loop.png)