## Utiliser des boucles pour créer des formes

Pour créer un carré, tu as répété quelques lignes de code. Ce n'est pas la manière la plus efficace de le faire. Au lieu de taper plusieurs lignes de code, il est plus facile d'utiliser une boucle.

Au lieu du code pour créer un carré comme ceci :

```python
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
elsa.right(90)
elsa.forward(100)
```

Tu peux taper :

```python
for i in range(4):
  elsa.forward(100)
  elsa.right(90)
```

Essaie-le toi-même, et vois ce qui se passe lorsque tu enregistres et exécutes ton code.

![](images/turtle-loop.png)