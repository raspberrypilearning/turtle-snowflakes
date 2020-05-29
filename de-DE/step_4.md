## Wie man mit Python Turtle dreht

Deine Schildkröte bewegt sich bisher nur in eine Richtung. Dies ist eine gute Nachricht, wenn du eine gerade Linie zeichnen möchtest, aber um eine Form wie ein Quadrat zu zeichnen, muss sich deine Schildkröte drehen.

- Füge unter der Zeile `elsa.forward(100)` in deinem Python-Code hinzu:
    
    ```python
    elsa.right(90)
    ```
    
    **Hinweis:** Turtle verwendet Winkel in Grad. Es gibt 360 Grad in einem Kreis. Wie viele Grad hat der rechte Winkel eines Quadrats? Das stimmt: 90. Der Wert `90` innerhalb der Klammern in `elsa.right(90)` ist in Grad. Diese Linie sagte deinem Turtles, dass es sich um 90 Grad rechts drehen soll.

- Füge eine weitere Anweisung darunter hinzu, um deine Turtle um 100 vorwärts zu bewegen:
    
    ```python
    elsa.forward(100)
    ```

- Speichere und starte deinen Code, um zu sehen, was passiert.

Du bist auf dem Weg ein Quadrat zu erstellen! Was musst du deinem Code hinzufügen, um das Quadrat zu vervollständigen?

\--- hints \---

\--- hint \---

Füge den folgenden Code hinzu und führe dein Programm aus:

```python
elsa.right(90)
elsa.forward(100)
```

Was war das Ergebnis? Wie kann man die Form beenden, um ein Quadrat zu zeichnen?

\--- /hint \---

\--- /hints \---