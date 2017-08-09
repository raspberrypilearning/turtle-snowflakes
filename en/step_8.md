## Using a function to draw a snowflake

Your parallelogram snowflake is cool, but it does not look as snowflake-like as it could. Let's fix that!

- For this drawing, we need to move the turtle from starting in the centre of the window. The `penup()` and `pendown()` instructions allow this to happen without drawing a line. It's like picking up a real pen from the paper and moving it somewhere else to start to write. Type the following instructions underneath the colours list:

  ```python
  elsa.penup()
  elsa.forward(90)
  elsa.left(45)
  elsa.pendown()
  ```
  
 1. Next, define a function by typing: 
 
  ```python
  def branch():
  ```
  
    *Note: The code to draw one branch of the snowflake will be stored inside this function, so that you can repeat it over and over to create an entire snowflake.*
  
  1. Remove the code for the parallelogram snowflake loops and replace it with:
  
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
  
  *Note: Remember that indentation is important. Make sure that you check your indentation is correct or your code might not work!*

- The last section of this code will call the snowflake function and repeat it eight times. You can use a loop in the same way as with the last snowflake:

  ```python
  for i in range(8):
      branch()
      elsa.left(45)
  ```    

- Use a `#` at the start of the `elsa.color(random.choice(colours))` instruction to turn it into a comment. This means that the computer will skip that line of code. You could delete the line, but you might want to use it to add colour to your snowflake later on.

- Save and run your code, and a snowflake should appear before your eyes! 

![](images/snowflake2.png)

