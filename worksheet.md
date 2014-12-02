# Draw a Snowflake with Code

Let's create a beautiful landscape of snowflakes using python turtle. Along the way you will learn how to think in seuqneces, use loops to repeat a sequence, use the random module, and how to use functions.

## Step 1: How to draw with python turtle

1. To begin you will need to open the Python 3 programming environment **IDLE3**. You can do this by selecting it from the **Main Menu** with your mouse. 
1. Then click on **File** and **New Window** to open a blank text editor window to write your code into. 
1. Save your empty file by clicking on **File**, **Save As** and naming it `snowflake.py`.
1. To begin using turtle in python you need to import the turtle library. At the top of the text editor window type `import turtle`. 
1. Next a command is needed to create the window which will display your turtle drawings `turtle.Screen()`. To save having to type it out every time you need the command you can store it as a **variable**:

  ```python
  wn = turtle.Screen()
  ```
  *Note: There is a capital letter used here for Screen. It is important to get uppercase and lowercase syntax correct in python in order for your code to work.*
  
1. Time to give your turtle a name, you can use a variable to do this. I'm naming my turtle Elsa but you can name yours whatever you like.

  ```python
  elsa = turtle.Turtle()
  ```

1. Now you can tell your turtle what to do. For example, to move forward 100. Give it a go.

  ```python
  elsa.forward(100)
  ```

1. To complete your first turtle program, add `wn.exitonclick()` so that the turtle window will stay open so you can see your drawing for as long as you like. It will only close when you click on the `x` in the top right hand corner of the window with your mouse.    

  ```python
  wn.exitonclick()
  ```
1. Click on **File** and **Save** and then click on **Run** and **Run Module** to run your first turtle program. What happens?

  ![](images/import-turtle.png)

## Step 2: How to turn with python turtle

Your turtle is pointing in one direction, which is good news if you want to draw a line, but it is time to think about drawing a shape like a square!

1. Underneath the line `elsa.forward(100)` in your python code, add:

  ```python
  elsa.right(90)
  ```
  *Note: Turtle uses angles in degrees. There are 360 degrees in a circle. How many are in a right angle of a square? That's right, 90. The value 90 inside the brackets in `elsa.right(90)` is in degrees. So this line is telling your turtle to turn right by 90 degrees.*
  
1. Add another instruction underneath to move your tutle forward by 100.   

  ```python
  elsa.forward(100)
  ```
1. Save and run your code to see what happens.

1. You are on your way to creating a square. What do you need to add to your code in order to complete the square?

## Step 3: Using loops to create shapes

To create a square, you have repeated some lines of code. It is not the most efficent way of doing it. Instead of typing out many lines of code it makes more sense to use a loop.

Instead of code to create a square like this:
  
  ```python
  elsa.forward(100)
  elsa.right(90)
  elsa.forward(100)
  elsa.right(90)
  elsa.forward(100)
  elsa.right(90)
  elsa.forward(100)
  ```
You can type:
  
  ```python
  for i in range(4):
      elsa.forward(100)
      elsa.right(90)
  ```
Try it yourself and see what happens when you save and run your code.
  
  ![](images/turtle-loop.png)

## Step 4: Creating spiral patterns
Don't be a square! Let's create some different shapes and repeat them to make a snowflake like spiral.

1. Replace the code for your square with the following:

  ```python
  for i in range(2):
      elsa.forward(100)
      elsa.right(60)
      elsa.forward(100)
      elsa.right(120)
  ```
  It will draw a shape called a parallelogram. You can see what it looks like by saving and running your code.
  
  ![](images/parallelogram.png)

## Step 5: Changing the pen colour randomly


## Step 6: Using a function to draw a snowflake


## Step 7: Creating a window of snowflakes
