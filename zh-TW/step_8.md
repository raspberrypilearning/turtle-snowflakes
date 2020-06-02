## 使用函數來繪製雪花

您用平行四邊形做的雪花很酷，但看起來還沒有雪花的樣子， 來修改一下！

為了完成雪花，我們需要先將烏龜從視窗的中心點移開， `penup()`和`pendown()`指令能讓我們無需畫線做到這一點，就像實際上在紙上提起筆尖並將筆移到其他位置開始書寫。

- 在`colours`清單之後輸入以下指令：
    
    ```python
    elsa.penup()
    elsa.forward(90)
    elsa.left(45)
    elsa.pendown()
    ```

讓我們寫一段程式碼畫出一部分的雪花，並儲存成一段**function**， 這樣子您就可以輕鬆地重複該函式並製作出完整的雪花了。

![分支](images/branch.PNG)

- 輸入以下程式碼來定義一個名為`branch`分支的函式：
    
    ```python
    def branch():
    ```

- 從迴圈中移除製作平行四邊形雪花的程式碼片段， 在`branch`函式內添加下列已縮排過的代碼：
    
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