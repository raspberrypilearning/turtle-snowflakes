## ループを使って図形を作成する

正方形を作成するのに、何行かコードを繰り返しました。 これは、最も効率的な方法ではありません。 コードを何行も入力するかわりに、ループを使用する方が簡単です。

正方形を作成する次のようなコード：

```python
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
```

You can type:

```python
for i in range(4):
  elsa.forward(100)
  elsa.right(90)
```

Try it yourself, and see what happens when you save and run your code.

![](images/turtle-loop.png)