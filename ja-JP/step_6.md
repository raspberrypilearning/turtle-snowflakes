## うずまき模様（もよう）を作成する

正方形はもう十分です！ いくつかの異なる形を作成し、それらを繰り返して雪の結晶のようなうずまきを作りましょう。

- 正方形を描くコードを以下に置き換えてください。
    
    ```python
    for i in range(2):
      elsa.forward(100)
      elsa.right(60)
      elsa.forward(100)
      elsa.right(120)
    ```
    
    これは平行四辺形と呼ばれる形を描画します。 コードを保存して実行することで、どのように見えるかを確認できます。
    
    ![](images/parallelogram.png)

You can put loops inside of other loops. This is good news for us, as we can do this to easily make a drawing that looks like a snowflake.

- Above the line `for i in range(2):` for your parallelogram, type:
    
    ```python
    for i in range(10):
    ```
    
    How many times will this loop go round?

- Move your cursor to the line below your sequence of code, and press the space bar four times to **indent** the code you're about to write. Indentation in Python is very important to ensure that your code works as you expect! Now type:
    
    ```python
    elsa.right(36)
    ```

- Save and run your code to see what happens. You should see a drawing like this:
    
    ![](images/snowflake1.png)