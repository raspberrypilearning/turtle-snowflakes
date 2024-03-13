## How to turn with Python Turtle

Your turtle is only moving in one direction so far. This is good news if you want to draw a straight line, but to draw a shape such as a square, your turtle is going to have to turn.


--- task ---

Below the line `elsa.forward(100)` in your Python code, add a line to turn `elsa`.

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
elsa.forward(100)
elsa.right(90)

--- /code ---

--- /task ---

--- collapse ---

---
title: Degrees
---
Turtle uses angles in degrees. There are 360 degrees in a circle. How many degrees does the right angle of a square have? That's right: 90. The value `90` inside the brackets in `elsa.right(90)` is in degrees. So this line is telling your turtle to turn right by 90 degrees.
--- /collapse ---  

--- task ---

Add another instruction below to move your turtle forward by 100:  

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 4
line_highlights: 6
---
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
--- /code ---

Save and run your code to see what happens.

--- /task ---

You are on your way to creating a square! What do you need to add to your code in order to complete the square?

--- hints ---

--- hint ---

Try adding the following code and running you program:

```python
elsa.right(90)
elsa.forward(100)
```

What was the result? How can you finish the shape to draw a square?

--- /hint ---

--- /hints ---
