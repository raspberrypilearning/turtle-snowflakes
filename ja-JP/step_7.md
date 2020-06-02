## ペンの色をランダムに変更する

これまでのところ、タートルは白い背景に黒い線を描いていました。 色を追加する時が来ました！

- タートルの色を設定するには、タートルに名前を付けた行の下、ループの前にカーソルを移動して次のように入力します：

```python
elsa.color("cyan")
```

**注意**：「colour」（色）のつづり方は国によって違います。 アメリカでは「color」とつづられており、Pythonではアメリカ式につづらなければなりません。

私は**cyan**（青緑色）を選択しましたが、以下のどの色でも使用することができます：

- 「blue」（青色）
- 「magenta」（赤紫色）
- 「grey」（灰色）
- 「purple」（紫色）

ウィンドウの背景色を変更することもできます。 背景色を設定するには、今書いたコードの下にこの命令を入力します：

```python
turtle.Screen().bgcolor("blue")
```

![](images/colour.png)

タートルの色をランダムに追加して楽しむこともできます。 コードを実行するたびに少しずつ違う雪の結晶ができます：

- First you will need to import the `random` library: below `import turtle`, type `import random`.

- Next, change the background colour from `"blue"` to `"grey"`.

- Below that line, create a variable called `colours` to store a list of the colours to select from, like this:
    
    ```python
    colours = ["cyan", "purple", "white", "blue"]
    ```

- At the end of the spiral loop, below `elsa.right(36)`, type:
    
    ```python
    elsa.color(random.choice(colours))  
    ```
    
    **Note**: make sure this line is also indented, so that your program knows it's within the loop.

- Save and run your code for a multi-coloured snowflake!

![](images/colour-list.png)

## \--- collapse \---

## title: More colours

There are a lot more colours you can choose from! Have a look at [this website](https://wiki.tcl.tk/37701) for a complete list.

\--- /collapse \---