## Spiralförmige Muster erzeugen

Genug Quadrate! Lass' uns verschiedene Formen erstellen und sie wiederholen um eine schneeflockenähnliche Spirale zu erstellen.

- Ersetze den Code für dein Quadrat durch folgendes:
    
    ```python
    for i in range(2):
      elsa.forward(100)
      elsa.right(60)
      elsa.forward(100)
      elsa.right(120)
    ```
    
    Dies wird eine Form zeichnen, die ein Parallelogramm genannt wird. Du kannst sehen, wie es aussieht, indem du deinen Code speicherst und ausführst.
    
    ![](images/parallelogram.png)

Du kannst Schleifen in andere Schleifen legen. Dies sind gute Nachrichten für uns, da wir dies tun können, um auf einfache Weise eine Zeichnung zu erstellen, die wie eine Schneeflocke aussieht.

- Über der Zeile `for i in range(2):` für dein Parallelogramm, schreibe:
    
    ```python
    for i in range(10):
    ```
    
    Wie oft wird diese Schleife durchlaufen?

- Bewege deinen Cursor in die Zeile unter deinem Code und drücke die Leertaste viermal um den Code **einzurücken**, den du gerade schreibst. Einrückung in Python ist sehr wichtig, um sicherzustellen, dass dein Code funktioniert wie du es erwartest! Tippe nun:
    
    ```python
    elsa.right(36)
    ```

- Speichere und starte deinen Code, um zu sehen was passiert. Du solltest eine Zeichnung wie diese sehen:
    
    ![](images/snowflake1.png)