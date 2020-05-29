## Die Stiftfarbe zufällig ändern

Bisher hat dein Turtle schwarze Linien auf einem weißen Hintergrund gezeichnet. Jetzt ist es Zeit Farbe hinzuzufügen!

- Um die Farbe des Turtles zu bestimmen, bewege deinen Cursor unter die Stelle, wo du dein Turtle und deine Schleifen benannt hast und gib folgendes ein:

```python
elsa.color("cyan")
```

**Hinweis**: Die Schreibweise von 'colour' ist in anderen Ländern unterschiedlich. In den USA heißt es "color" und in Python muss es wie die amerikanische Art geschrieben werden, damit es funktioniert.

Ich habe die Farbe **cyan** gewählt, aber du kannst eine andere von dieser Liste verwenden:

- "blue"
- "magenta"
- "grey"
- "purple"

Du kannst auch die Farbe des Hintergrundfensters ändern. Um die Hintergrundfarbe festzulegen, verwende diese Anweisung unter dem Code, den du gerade geschrieben hast:

```python
turtle.Screen().bgcolor("blue")
```

![](images/colour.png)

Zum Spaß kannst du eine zufällige Farbe für dein Turtle hinzufügen, so dass du bei jedem Programmstart eine etwas andere Schneeflocke bekommst.

- Zuerst musst du die `random` Bibliothek importieren: unter `import turtle`, musst du `import random` eingeben.

- Ändere als nächstes die Hintergrundfarbe von `"blue"` auf `"grey"`.

- Erstelle unterhalb dieser Zeile eine Variable namens `Farben` um eine Liste der auszuwählenden Farben zu speichern:
    
    ```python
    colours = ["cyan", "purple", "white", "blue"]
    ```

- Am Ende der Spiralschleife unter `elsa.right(36)`, tippe:
    
    ```python
    elsa.color(random.choice(colours))  
    ```
    
    **Hinweis**: Stelle sicher, dass diese Zeile auch eingerückt ist, damit dein Programm weiß, dass es sich innerhalb der Schleife befindet.

- Speichere und starte deinen Code für eine bunte Schneeflocke!

![](images/colour-list.png)

## \--- collapse \---

## title: Weitere Farben

Es gibt noch viel mehr Farben, aus denen du wählen kannst! Schau dir [diese Website](https://wiki.tcl.tk/37701) an, um eine vollständige Liste zu erhalten.

\--- /collapse \---