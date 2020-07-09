## Como virar com Python Turtle

Sua tartaruga está se movendo apenas em uma direção até agora. Esta é uma boa notícia se você quiser desenhar uma linha reta, mas para desenhar uma forma como um quadrado, sua tartaruga terá que virar.

- Abaixo da linha ` elsa.forward (100) ` no seu código Python, adicione:
    
    ```python
    elsa.right(90)
    ```
    
    **Nota:** Turtle usa ângulos em graus. Existem 360 graus em um círculo. Quantos graus tem o ângulo reto de um quadrado? É isso mesmo: 90. O valor `90` dentro dos parênteses em `elsa.right(90)` está em graus. Então esta linha está dizendo à sua tartaruga para virar 90 graus à direita.

- Adicione outra instrução abaixo para mover sua tartaruga para frente em 100:
    
    ```python
    elsa.forward(100)
    ```

- Salve e execute seu código para ver o que acontece.

Você está a caminho de criar um quadrado! O que você precisa adicionar ao seu código para completar o quadrado?

\--- hints \---

\--- hint \---

Tente adicionar o seguinte código e executar seu programa:

```python
elsa.right(90)
elsa.forward(100)
```

Qual foi o resultado? Como você pode terminar a forma para desenhar um quadrado?

\--- /hint \---

\--- /hints \---