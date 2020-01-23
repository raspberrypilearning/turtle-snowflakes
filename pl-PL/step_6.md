## Creating spiral patterns

Enough squares! Let's create some different shapes and repeat them to make a snowflake-like spiral.

- Replace the code for your square with the following:
    
    ```python
    for i in range(2):
      elsa.forward(100)
      elsa.right(60)
      elsa.forward(100)
      elsa.right(120)
    ```
    
    This will draw a shape called a parallelogram. You can see what it looks like by saving and running your code.
    
    ![](images/parallelogram.png)

You can put loops inside of other loops. This is good news for us, as we can do this to easily make a drawing that looks like a snowflake.

- Above the line `for i in range(2):` for your parallelogram, type:
    
    ```python
            for i in range(10):
    ```
    
    How many times will this loop go round?

- Move your cursor to the line below your sequence of code, and press the space bar four times to **indent** the code you're about to write. Indentation in Python is very important to ensure that your code works as you expect! Now type:
    
    ```python
    elsa.right(36)
    ```

- Save and run your code to see what happens. You should see a drawing like this:
    
    ![](images/snowflake1.png)