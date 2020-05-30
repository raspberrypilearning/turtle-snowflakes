## Crear patrones en espiral

¡Basta de cuadrados! Ahora vamos a crear otras formas y a repetirlas para hacer un espiral con forma de copo de nieve.

- Reemplaza el código de tu cuadrado con el siguiente:
    
    ```python
    for i in range(2):
      elsa.forward(100)
      elsa.right(60)
      elsa.forward(100)
      elsa.right(120)
    ```
    
    Esto dibujará una forma llamada paralelogramo. Puedes ver cómo se ve al guardar y ejecutar tu código.
    
    ![](images/parallelogram.png)

Puedes poner bucles dentro de otros bucles. Esta es una buena noticia para nosotros, ya que podemos usar esto para hacer fácilmente un dibujo que parezca un copo de nieve.

- Sobre la línea "`for i in range(2):`" de tu paralelogramo, escribe:
    
    ```python
    for i in range(10):
    ```
    
    ¿Cuántas veces se repetirá el bucle?

- Mueve el cursor a la línea debajo de tu secuencia de código y presiona la barra espaciadora cuatro veces para **dar indentación** al código que estás a punto de escribir. La indentación en Python es muy importante para asegurar que tu código funciona como esperas! Ahora escribe:
    
    ```python
    elsa.right(36)
    ```

- Guarda y ejecuta tu código para ver qué pasa. Deberías ver un dibujo como este:
    
    ![](images/snowflake1.png)