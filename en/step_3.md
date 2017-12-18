## How to draw with Python Turtle

+ Open the blank Python template trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Type the following into the window that appears:

    ![screenshot](images/me-hi.png)

    The line `#!/bin/python3` just tells Trinket that we're using Python 3 (the latest version).
    
+ To begin using Turtle in Python you need to import the Turtle library. At the top of the text editor window type `import turtle`. 

+ Next, a command is needed to create the window which will display your turtle drawings: `turtle.Screen()`. To save having to type it out every time you need the command, you can store it as a **variable**:

  ```python
  wn = turtle.Screen()
  ```
  
  Note: There is a capital letter used here for Screen. It is important to get uppercase and lowercase syntax correct in Python in order for your code to work.
  
+ Time to give your turtle a name; you can use a variable to do this. I'm naming my turtle Elsa but you can name yours whatever you like.

  ```python
  elsa = turtle.Turtle()
  ```

+ Now you can tell your turtle what to do; for example, to move forward 100. Give it a go.

  ```python
  elsa.forward(100)
  ```
  
+ Click on **Run** to run your first turtle program. What happens?

  ![](images/import-turtle.png)

__You don't need a Trinket account to save your projects!__

If you don't have a Trinket account, click the down arrow and then click **Link**. This will give you a link that you can save and come back to later. You'll need to do this every time you make changes, as the link will change!

![screenshot](images/me-link.png)

If you have a Trinket account, you can click **Remix** to save your own copy of the trinket.

![screenshot](images/me-remix.png)
