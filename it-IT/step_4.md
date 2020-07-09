## Come ruotare con Python Turtle

La tua tartaruga si è mosso solo in una direzione finora. Questa è una buona cosa se vuoi disegnare una linea retta, ma per disegnare una forma come un quadrato, la tua tartaruga dovrà poter ruotare.

- Sotto la riga `elsa.forward (100)` nel tuo codice Python, aggiungi:
    
    ```python
    elsa.right(90)
    ```
    
    **Nota:** La tartaruga usa angoli in gradi. Ci sono 360 gradi in una circonferenza. Quanti gradi ha l'angolo retto di un quadrato? Esatto: 90. Il valore `90` all'interno delle parentesi in `elsa.right(90)` è in gradi. Quindi questa linea sta dicendo alla tartaruga di girare a destra di 90 gradi.

- Add another instruction below to move your turtle forward by 100:
    
    ```python
    elsa.forward(100)
    ```

- Save and run your code to see what happens.

You are on your way to creating a square! What do you need to add to your code in order to complete the square?

\--- hints \---

\--- hint \---

Try adding the following code and running you program:

```python
elsa.right(90)
elsa.forward(100)
```

What was the result? How can you finish the shape to draw a square?

\--- /hint \---

\--- /hints \---