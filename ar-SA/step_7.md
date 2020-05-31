## تغيير لون القلم عشوائياً

حتى الآن ، كانت السلحفاة ترسم خطوطًا سوداء على خلفية بيضاء. الآن حان الوقت لإضافة لون!

- لتعيين لون السلحفاة ، حرك مؤشر الماوس الى السطر الذي قمت بتسمية سلحفاتك وقبل التعليمة البرمجية تكرار، واكتب ما يلي:

```python
elsa.color("cyan")
```

**ملاحظة**: يختلف تهجئة "اللون colour" في البلدان الأخرى. في الولايات المتحدة ، تم تهجئتها بـ'color' ، وفي Python يجب أن يتم تهجئة بالطريقة الأمريكية لتعمل.

لقد اخترت استخدام اللون الازرق الفاتح **cyan**، ولكن يمكنك استخدام أي لون من هذه القائمة:

- "blue"
- "magenta"
- "grey"
- "purple"

يمكنك أيضا تغيير لون نافذة الخلفية. لتعيين لون الخلفية، استخدم هذه التعليمات أسفل التعليمات البرمجية التي كتبتها للتو:

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