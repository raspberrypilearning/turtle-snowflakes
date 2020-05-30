## Cómo girar con Turtle en Python

Por ahora, tu tortuga solo puede moverse en una dirección. Si quieres que se mueva en línea recta, no hay problem. Pero si quieres dibujar una forma, por ejemplo, un cuadrado, necesitas que tu tortuga gire.

- Debajo de la línea ` elsa.forward (100) ` en tu código de Python agrega:
    
    ```python
    elsa.right(90)
    ```
    
    **Nota:** Turtle expresa los ángulos en grados. Hay 360 grados en un círculo. ¿Cuántos grados tiene el ángulo recto de un cuadrado? Así es: 90 grados. El valor `90` dentro de los paréntesis en `elsa.right(90)` representa los grados. Esta línea le dice a tu tortuga que debe girar 90 grados a la derecha.

- A continuación, agrega una instrucción para mover tu tortuga 100 píxeles hacia adelante:
    
    ```python
    elsa.forward(100)
    ```

- Guarda y ejecuta tu código para ver qué sucede.

¡Falta poco para completar el cuadrado! ¿Qué debes agregar a tu código para terminarlo?

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