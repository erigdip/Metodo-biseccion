# Calculadora de Raíces con el Método de Bisección

Este es un script en Python que implementa el método de bisección para encontrar las raíces de una función matemática proporcionada por el usuario. El programa muestra una tabla detallada de las iteraciones y genera una gráfica de la función con la raíz encontrada.

## Características

- **Cálculo de raíces**: Utiliza el método numérico de bisección.
- **Entrada de funciones dinámicas**: Permite al usuario ingresar funciones matemáticas como una cadena de texto (ej. `x**3 - x - 2`).
- **Visualización de iteraciones**: Imprime una tabla en la consola que muestra el progreso del algoritmo en cada paso, incluyendo el intervalo, la raíz aproximada y el error relativo porcentual.
- **Graficación**: Genera una gráfica utilizando `matplotlib` que muestra la función, los límites del intervalo inicial (`a` y `b`) y la raíz encontrada.
- **Condiciones de parada**: El algoritmo se detiene cuando se alcanza la tolerancia de error deseada o el número máximo de iteraciones.

## Requisitos

Asegúrate de tener Python 3 instalado. Las siguientes bibliotecas son necesarias:

- **NumPy**: Para cálculos numéricos y matemáticos.
- **Matplotlib**: Para la generación de la gráfica.

## Instalación

1.  **Clona o descarga el repositorio.**

2.  **Crea un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    ```

3.  **Activa el entorno virtual:**
    - En Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - En macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## ¿Cómo usarlo?

1.  Ejecuta el script desde tu terminal:
    ```bash
    python biseccion.py
    ```

2.  Sigue las instrucciones en la consola para ingresar:
    - La función `f(x)` (usando `x` como variable).
    - El límite inferior del intervalo (`a`).
    - El límite superior del intervalo (`b`).
    - El número máximo de iteraciones.
    - El porcentaje de error de tolerancia.

El programa mostrará la tabla de iteraciones y, al finalizar, abrirá una ventana con la gráfica de la función y la raíz calculada.
