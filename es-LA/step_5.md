## Usar bucles para crear formas

Para crear un cuadrado has repetido algunas líneas en el código. Esta no es la forma más eficaz de hacerlo. En lugar de escribir muchas líneas de código, es más fácil usar un bucle.

En vez de usar código como este para crear un cuadrado:

```python
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
```

Puedes escribir:

```python
for i in range(4):
  elsa.forward(100)
  elsa.right(90)
```

Pruébalo tu mismo y observa qué sucede cuando guardas y ejecuta tu código.

![](images/turtle-loop.png)