## Changing the pen colour randomly

So far the turtle has been drawing black lines on a white background. Now it's time to add colour!

- To set the colour of the turtle, move you're cursor below where you named your turtle and before your loops, and type in the following:

```python
elsa.color("cyan")
```

**Note**: The spelling of 'colour' is different in other countries. In the US, it is spelled 'color', and in Python it has to be spelled the American way to work.

I have chosen to use the colour **cyan**, but you can use any from this list:

- "kék"
- "bíborvörös"
- "grey"
- "purple"

You can also change the colour of the background window. To set the colour of the background, use this instruction below the code you've just written:

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