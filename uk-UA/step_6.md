## Створення візерунків для сніжинок

Досить квадратів! Давай намалюємо якісь інші фігури і повторюватимемо їх, щоб вийшла сніжинка.

- Заміни код для квадрата наступним:
    
    ```python
    for i in range(2):
      elsa.forward(100)
      elsa.right(60)
      elsa.forward(100)
      elsa.right(120)
    ```
    
    Так ти намалюєш фігуру, що називається паралелограм. Ти можеш побачити, як вона виглядає, якщо збережеш і запустиш код.
    
    ![](images/parallelogram.png)

Можна розміщувати цикли всередині інших циклів. Це нам підходить, тому що ми можемо це використати, щоб намалювати сніжинку.

- Над рядком `for i in range(2):` для паралелограма, введи:
    
    ```python
    for i in range(10):
    ```
    
    Скільки разів виконується цей цикл?

- Move your cursor to the line below your sequence of code, and press the space bar four times to **indent** the code you're about to write. Indentation in Python is very important to ensure that your code works as you expect! Now type:
    
    ```python
    elsa.right(36)
    ```

- Save and run your code to see what happens. You should see a drawing like this:
    
    ![](images/snowflake1.png)