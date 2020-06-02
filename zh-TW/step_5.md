## 使用迴圈來創造形狀

為了創造一個正方形，您會需要重複執行某幾行程式碼， 這不是最有效的方式。 與其輸入好幾行重複的程式碼，不妨試試使用迴圈語法。

我們不用這段程式創造正方形：

```python
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
```

而是輸入：

```python
for i in range(4):
  elsa.forward(100)
  elsa.right(90)
```

試著自己動手做做看，並看看當您保存和執行程式碼時會發生什麼。

![](images/turtle-loop.png)