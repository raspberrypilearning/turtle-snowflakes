## 関数を使って雪の結晶を描く

平行四辺形を使った雪の結晶はクールですが、本当の雪の結晶のようには見えません。 修正しましょう！

この描画方法では、タートルがウィンドウの中心から動き出すようにする必要があります。 `penup()`および`pendown()`命令を使えば、本物のペンを紙から持ち上げてどこか別の場所に移動して書き始めるように、線を引くことなく移動することができます。

- `colours`リストの下に次の命令を入力します：
    
    ```python
    elsa.penup()
    elsa.forward(90)
    elsa.left(45)
    elsa.pendown()
    ```

雪の結晶の枝を一本描くコードを書いて**関数**の中に入れましょう。 そうすれば、これを繰り返して使うことで、完全な雪の結晶を作成できます。

![branch](images/branch.PNG)

- Define a function called `branch` by typing:
    
    ```python
    def branch():
    ```

- Remove the code for the parallelogram snowflake loops. Add the following code indented inside the `branch` function:
    
    ```python
    for i in range(3):
        for i in range(3):
            elsa.forward(30)
            elsa.backward(30)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(30)
        elsa.left(45)
    elsa.right(90)
    elsa.forward(90)
    ```
    
    **Note**: Remember that indentation is important. Make sure to check that all your indentation is correct, otherwise your code won't work!

- Write a final section of code to **call** the `branch` function (which means to run it) eight times. You can use a loop again as for your last snowflake:
    
    ```python
    for i in range(8):
      branch()
      elsa.left(45)
    ```

- Put a `#` at the start of the `elsa.color(random.choice(colours))` instruction to turn it into a **comment**. This means that the computer will skip that line of code. You could delete the line, but you might want to use it to add colour to your snowflake later on.

- Save and run your code, and a snowflake should appear before your eyes!

![](images/snowflake2.png)