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
    
    **注意** ：別忘記縮排很重要。 確認所有的縮排都是正確的，否則您的程式碼不會運作！

- 在程式碼的最後一段**呼叫** (代表執行) 函式`branch`共八次， 您可以再藉由迴圈畫出雪花最終的形狀：
    
    ```python
    for i in range(8):
      branch()
      elsa.left(45)
    ```

- 在指令`elsa.color(random.choice(colours))`的開頭添加一個`#`符號來轉換成**註釋**， 這代表電腦會跳過那一行程式碼。 您可以刪除那一行，但您可能之後會想再啟用那一行來為您的雪花添加色彩。

- 儲存並執行您的程式，雪花應該出現在您眼前了！

![](images/snowflake2.png)