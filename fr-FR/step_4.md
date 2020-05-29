## Comment tourner avec Turtle de Python

Ta « tortue » ne va que dans une direction jusqu'à présent. C'est une bonne nouvelle si tu veux tracer une ligne droite, mais pour dessiner une forme comme un carré, ta « tortue » devra tourner.

- Sous la ligne `elsa.forward(100)` dans ton code Python, ajoute :
    
    ```python
    elsa.right(90)
    ```
    
    **Note :** La tortue utilise des angles en degrés. Il y a 360 degrés dans un cercle. Combien de degrés a l'angle droit d'un carré ? C'est correct : 90. La valeur `90` entre parenthèses dans `elsa.right(90)` est en degrés. Cette ligne dit donc à ta « tortue » de tourner à droite de 90 degrés.

- Ajoute une autre instruction en-dessous pour avancer ta « tortue » de 100 :
    
    ```python
    elsa.forward(100)
    ```

- Enregistre et exécute ton code pour voir ce qui se passe.

Tu es sur le point de créer un carré ! Qu'est-ce que tu dois ajouter à ton code pour compléter le carré ?

\--- hints \---

\--- hint \---

Essaie d'ajouter le code suivant et exécute ton programme :

```python
elsa.right(90)
elsa.forward(100)
```

Quel en a été le résultat ? Comment peux-tu finir la forme pour dessiner un carré ?

\--- /hint \---

\--- /hints \---