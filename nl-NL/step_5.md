## Lussen gebruiken om vormen te maken

Om een vierkant te maken, heb je enkele regels code herhaald. Dit is niet de meest efficiënte manier om dit te doen. In plaats van veel regels code te typen, is het gemakkelijker om een lus te gebruiken.

In plaats van code om een vierkant zo te maken:

```python
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
```

Kun je typen:

```python
for i in range(4):
  elsa.forward(100)
  elsa.right(90)
```

Probeer het zelf en kijk wat er gebeurt als je je code opslaat en uitvoert.

![](images/turtle-loop.png)