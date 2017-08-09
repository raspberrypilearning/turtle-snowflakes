## How to draw with Python Turtle

- To begin, you will need to open the Python 3 programming environment **IDLE3**. You can do this by selecting it from the **Main Menu** with your mouse. 
- Then click on **File** and **New Window** to open a blank text editor window to write your code in. 
- Save your empty file by clicking on **File**, **Save As** and naming it `snowflake.py`.
- To begin using Turtle in Python you need to import the Turtle library. At the top of the text editor window type `import turtle`. 
- Next, a command is needed to create the window which will display your turtle drawings: `turtle.Screen()`. To save having to type it out every time you need the command, you can store it as a **variable**:

  ```python
  wn = turtle.Screen()
  ```
  
  *Note: There is a capital letter used here for Screen. It is important to get uppercase and lowercase syntax correct in Python in order for your code to work.*
  
- Time to give your turtle a name; you can use a variable to do this. I'm naming my turtle Elsa but you can name yours whatever you like.

  ```python
  elsa = turtle.Turtle()
  ```

- Now you can tell your turtle what to do; for example, to move forward 100. Give it a go.

  ```python
  elsa.forward(100)
  ```

- To complete your first turtle program, add `wn.exitonclick()`; this means that the turtle window will stay open so you can see your drawing for as long as you like. It will only close when you click on the `x` in the top right hand corner of the window with your mouse.    

  ```python
  wn.exitonclick()
  ```
  
- Click on **File** and **Save**, and then click on **Run** and **Run Module** to run your first turtle program. What happens?

  ![](images/import-turtle.png)

