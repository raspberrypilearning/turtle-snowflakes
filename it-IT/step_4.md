## Come ruotare con Python Turtle

La tua tartaruga si è mosso solo in una direzione finora. Questa è una buona cosa se vuoi disegnare una linea retta, ma per disegnare una forma come un quadrato, la tua tartaruga dovrà poter ruotare.

- Sotto la riga `elsa.forward (100)` nel tuo codice Python, aggiungi:
    
    ```python
    elsa.right(90)
    ```
    
    **Nota:** La tartaruga usa angoli in gradi. Ci sono 360 gradi in una circonferenza. Quanti gradi ha l'angolo retto di un quadrato? Esatto: 90. Il valore `90` all'interno delle parentesi in `elsa.right(90)` è in gradi. Quindi questa linea sta dicendo alla tartaruga di girare a destra di 90 gradi.

- Aggiungi un'altra istruzione qui sotto per spostare la tartaruga in avanti di 100:
    
    ```python
    elsa.forward(100)
    ```

- Salva ed esegui il tuo codice per vedere cosa succede.

Stai per creare un quadrato! Cosa devi aggiungere al tuo codice per completare il quadrato?

--- hints ---


--- hint ---

Prova ad aggiungere il seguente codice ed esegui il programma:

```python
elsa.right(90)
elsa.forward(100)
```

Qual è stato il risultato? Come si può finire la forma per disegnare un quadrato?

--- /hint ---

--- /hints ---