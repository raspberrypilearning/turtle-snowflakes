## Випадкова зміна кольору ручки

Поки що "черепаха" малювала чорні лінії на білому фоні. Настав час додати кольору!

- Щоб задати колір, перемісти свій курсор між рядком, де ти давав (-ла) ім’я своїй "черепасі" і циклами, а потім введи наступне:

```python
elsa.color("cyan")
```

**Примітка**: написання слова "colour" (колір) відрізняється в різних англомовних країнах. В США воно пишеться як "color", і в Python воно теж має писатися по-американськи.

Ми вибрали колір **cyan** (блакитний), але ти можеш вибрати будь-який із наступного списку:

- "blue" (синій)
- "magenta" (фіолетово-рожевий)
- "grey" (сірий)
- "purple" (пурпурний)

Також ти можеш змінити колір тла. To set the colour of the background, use this instruction below the code you've just written:

```python
turtle.Screen().bgcolor("blue")
```

![](images/colour.png)

For fun you can add a random colour for your turtle, so that every time you run your code, you will get a slightly different snowflake.

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