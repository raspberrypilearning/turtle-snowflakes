## Changement aléatoire de la couleur du stylo

Jusqu'à présent, la « tortue » a dessiné des lignes noires sur un fond blanc. Maintenant il est temps d'ajouter de la couleur !

- Pour définir la couleur de la « tortue », déplace ton curseur vers le bas où tu as nommé ta « tortue » et avant tes boucles, et tape ce qui suit :

```python
elsa.color("cyan")
```

**Note** : L'orthographe de « couleur » est différente dans les autres pays. Aux États-Unis, il est écrit « color », et en Python, il faut l'orthographier à la façon américaine pour fonctionner.

J'ai choisi d'utiliser la couleur **cyan**, mais tu peux en utiliser une dans cette liste :

- "blue"
- "magenta"
- "grey"
- "purple"

Tu peux également changer la couleur de la fenêtre de fond. Pour définir la couleur de l'arrière-plan, utilise cette instruction en-dessous le code que tu viens d'écrire :

```python
turtle.Screen().bgcolor("blue")
```

![](images/colour.png)

Pour le plaisir, tu peux ajouter une couleur aléatoire pour ta « tortue », de sorte que chaque fois que tu exécutes ton code, tu obtiens un flocon de neige légèrement différent.

- Tu devras d'abord importer la bibliothèque `random` : en-dessous `import turtle`, tape `import random`.

- Ensuite, change la couleur d'arrière-plan de `"blue"` à `"grey"`.

- Sous cette ligne, crée une variable appelée `colours` pour stocker une liste des couleurs à sélectionner, comme ceci :
    
    ```python
    colours = ["cyan", "purple", "white", "blue"]
    ```

- À la fin de la boucle en spirale, en-dessous `elsa.right(36)`, tape :
    
    ```python
    elsa.color(random.choice(colours))  
    ```
    
    **Note** : assure-toi que cette ligne est également indentée, afin que ton programme sache qu'il se trouve dans la boucle.

- Enregistre et exécute ton code pour un flocon de neige multicolore !

![](images/colour-list.png)

## \--- collapse \---

## title: Plus de couleurs

Il y a beaucoup plus de couleurs que tu peux choisir ! Jette un œil à [ce site web](https://wiki.tcl.tk/37701) pour une liste complète.

\--- /collapse \---