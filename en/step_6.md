## Changing the pen colour randomly

So far the turtle has been drawing black lines on a white background. Now it's time to add colour!

--- task ---

Set the colour of the turtle.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 4
---
import turtle

elsa = turtle.Turtle()
elsa.color("cyan")

for i in range(10):
--- /code ---

--- /task ---

--- collapse ---

---
title: Color and Colour
---
The spelling of 'colour' is different in other countries. In the US, it is spelled 'color', and in Python it has to be spelled the American way to work.
--- /collapse ---


`cyan` is used in the example above, but you can use any from this list:

- "blue"
- "magenta"
- "grey"
- "purple"

--- task ---

Change the colour of the background window. To set the colour of the background.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 5
---
import turtle

elsa = turtle.Turtle()
elsa.color("cyan")
turtle.Screen().bgcolor("blue")

for i in range(10):
--- /code ---

![](images/colour.png)

--- /task ---


For fun you can add a random colour for your turtle, so that every time you run your code, you will get a slightly different snowflake. 

--- task ---

First you will need to import the `random` library: below `import turtle`, type `import random`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 2
---
import turtle
import random

elsa = turtle.Turtle()
elsa.color("cyan")
turtle.Screen().bgcolor("blue")

--- /code ---

--- /task ---


--- task ---

Next, change the background colour from `"blue"` to `"grey"`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 6
---
import turtle
import random

elsa = turtle.Turtle()
elsa.color("cyan")
turtle.Screen().bgcolor("grey")
--- /code ---

--- /task --- 

Create a list called `colours` to store colours to select from.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 5
---
import turtle
import random

elsa = turtle.Turtle()
colours = ["cyan", "purple", "white", "blue"]

elsa.color("cyan")
turtle.Screen().bgcolor("grey")
--- /code ---

--- task ---

At the end of the loop, below `elsa.right(36)`, choose a random colour

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 10
line_highlights: 17
---
for i in range(10):
    for i in range(2):
        elsa.forward(100)
        elsa.right(60)
        elsa.forward(100)
        elsa.right(120)
    elsa.right(36)
    elsa.color(random.choice(colours))
--- /code ---

**Note**: make sure this line is also indented, so that your program knows it's within the loop.

--- /task ---

--- task ---

Save and run your code for a multi-coloured snowflake!

![](images/colour-list.png)

--- /task ---


--- collapse ---
---
title: More colours
---

There are a lot more colours you can choose from! Have a look at [this website](https://wiki.tcl.tk/37701) for a complete list.

--- /collapse ---
