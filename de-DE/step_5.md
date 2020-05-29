## Schleifen benutzen um Formen zu erzeugen

Um ein Quadrat zu erstellen, hast du einige Zeilen Code wiederholt. Das ist nicht die effizienteste Methode. Anstatt viele Codezeilen einzugeben, ist es einfacher, eine Schleife zu verwenden.

Anstelle von Code, um ein Quadrat wie folgt zu erstellen:

```python
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
```

Du kannst tippen:

```python
for i in range(4):
  elsa.forward(100)
  elsa.right(90)
```

Probiere es selbst aus und sieh, was passiert, wenn du deinen Code speicherst und ausführst.

![](images/turtle-loop.png)