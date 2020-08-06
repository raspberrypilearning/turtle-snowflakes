## 隨意地更改筆的顏色

到目前為止，您的烏龜在白底上繪製許多黑線， 是時候添加新色彩了！

- 要設置烏龜的顏色，將遊標移動到您命名烏龜指令的下方和迴圈之前，然後輸入以下內容：

```python
elsa.color("cyan")
```

**注意** ：“顏色”的拼寫在其他國家/地區有所不同。 在美國，它被拼寫為“color”，而在Python中，它必須以美語拼寫。

我選擇使用青色**cyan** ，而您可以使用下列的任何一個：

- 藍色 "blue"
- 紫紅色 "magenta"
- 灰色 "grey"
- 紫色 "purple"

您也可以更改背景視窗的顏色。 請在您剛剛編寫的代碼下方依照以下指令來設置背景顏色：

```python
turtle.Screen().bgcolor("blue")
```

![](images/colour.png)

有趣的是您可以為烏龜加上隨機的顏色，如此一來當您每次運行代碼時，都會得到不同的雪花。

- 首先您需要導入`random`函式庫：在`import turtle`下一行，輸入`import random` 。

- 接下來，將背景色從`"blue"`更改為`"grey"` 。

- 下一行，創建一個名為`colours`的變數來儲存要選擇的顏色列表，如下所示：
    
    ```python
    colours = ["cyan", "purple", "white", "blue"]
    ```

- 在螺旋迴圈的最後面，在`elsa.right(36)`下方 ，輸入：
    
    ```python
    elsa.color(random.choice(colours))  
    ```
    
    **注意** ：請確保此行已經縮排，好讓這段程式碼能在迴圈內被辨識。

- 儲存並執行程式碼以生成彩色的雪花！

![](images/colour-list.png)

--- collapse ---
---
title: 更多的顏色
---

您可以選擇更多顏色！ 查看[這個網站](https://wiki.tcl.tk/37701)一個完整的清單。

--- /collapse ---