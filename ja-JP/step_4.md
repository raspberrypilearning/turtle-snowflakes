## Pythonタートルの向きを変える方法

タートルは今のところ一方向にしか動いていません。 直線を描きたい場合は、これは良いニュースです。でも、正方形のような形を描くにはタートルの向きを変える必要があります。

- Pythonコードの`elsa.forward(100)`の下に以下を追加します。
    
    ```python
    elsa.right(90)
    ```
    
    **注意：**タートルは度単位の角度を使用します。 円は一周360度です。 正方形の直角は何度ですか？ That's right: 90. The value `90` inside the brackets in `elsa.right(90)` is in degrees. So this line is telling your turtle to turn right by 90 degrees.

- Add another instruction below to move your turtle forward by 100:
    
    ```python
    elsa.forward(100)
    ```

- Save and run your code to see what happens.

You are on your way to creating a square! What do you need to add to your code in order to complete the square?

\--- hints \---

\--- hint \---

Try adding the following code and running you program:

```python
elsa.right(90)
elsa.forward(100)
```

What was the result? How can you finish the shape to draw a square?

\--- /hint \---

\--- /hints \---