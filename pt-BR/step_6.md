## Criando padrões em espiral

Chega de quadrados! Vamos criar formas diferentes e repeti-las para fazer uma espiral semelhante a um floco de neve.

- Substitua o código do seu quadrado pelo seguinte:
    
    ```python
    for i in range(2):
      elsa.forward(100)
      elsa.right(60)
      elsa.forward(100)
      elsa.right(120)
    ```
    
    Isso vai desenhar uma forma chamada paralelogramo. Você pode ver como ele se parece ao salvar e executar o seu código.
    
    ![](images/parallelogram.png)

Você pode colocar laços dentro de outros laços. Isso é uma boa notícia para nós, pois podemos fazer isso para criar facilmente um desenho que se parece com um floco de neve.

- Acima da linha `for i in range(2):` para o seu paralelogramo, digite:
    
    ```python
    for i in range(10):
    ```
    
    Quantas vezes esse laço irá rodar?

- Mova seu cursor para a linha abaixo da sua sequência de código, e pressione a barra de espaço quatro vezes para **indentar** o código que você está prestes a escrever. A indentação em Python é muito importante para garantir que seu código funcione como você espera! Agora digite:
    
    ```python
    elsa.right(36)
    ```

- Salve e execute seu código para ver o que acontece. Você deve ver um desenho como este:
    
    ![](images/snowflake1.png)