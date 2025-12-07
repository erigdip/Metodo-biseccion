import numpy as np
import matplotlib.pyplot as plt
import math

# Configuración del entorno matemático
funciones_permitidas = {
    'sen': np.sin, #Seno
    'cos': np.cos, #Coseno
    'tan': np.tan, #Tangente
    'asin': np.arcsin, #Arco Seno
    'acos': np.arccos, #Arco Coseno
    'atan': np.arctan, #Arco Tangente
    'sqrt': np.sqrt, #Raíz Cuadrada
    'exp': np.exp, #Exponencial
    'log': np.log, #Logaritmo Natural
    'log10': np.log10, #Logaritmo Base 10
    'pi': np.pi, #Constante Pi
    'e': np.e, #Constante de Euler
    'abs': np.abs #Valor Absoluto
}

def obtener_funcion_usuario(): # Entrada y Evaluación de la Función
    print("--- Calculadora de Raíces (Método Bisección) ---")
    print("Instrucciones: Use 'x' como variable. Ejemplos: 'sen(x)', 'x**2 - 4'")
    expr_str = input("Ingrese la función f(x): ").lower()
    
    def funcion_evaluada(val_x): # Evaluación Segura de la Función
        contexto = funciones_permitidas.copy() # Copia del entorno permitido
        contexto['x'] = val_x # Asignación del valor de x
        return eval(expr_str, {"__builtins__": None}, contexto) # Evaluación Segura
    
    return funcion_evaluada, expr_str # Retorna la función y su representación en texto

# Algoritmo de Bisección con tolerancia y máximo de iteraciones
def biseccion_con_iteraciones(f, a, b, tol_error, max_iter): # Bisección con Criterios de Parada
    fa = f(a) # Evaluación en a
    fb = f(b) # Evaluación en b
    
    if fa * fb >= 0: # Verificación del Cambio de Signo
        print("\nLa función no cambia de signo en el intervalo [a, b].")
        return None
    
    print("\n--- Iteraciones del Método de Bisección ---")
    # Encabezado con columna de Error
    print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "Iter.", "a", "b", "c (raiz)", "f(c)", "Error (%)")) # Formato de Impresión
    print("-" * 90) # Línea Separadora
    
    c_old = None # Para guardar la raíz de la iteración anterior
    
    for i in range(max_iter): # Iteración Principal
        c = (a + b) / 2.0 # Cálculo del Punto Medio
        fc = f(c) # Evaluación en el Punto Medio
        
        # Cálculo del Error Relativo Porcentual
        error_actual = 100.0 # Valor inicial alto
        if i > 0 and c != 0: # Evitar división por cero
            error_actual = abs((c - c_old) / c) * 100 # Cálculo del Error
        
        # Formato para imprimir (Muestra '----' en la primera iteración para el error)
        str_error = f"{error_actual:.6f}" if i > 0 else "----"
        
        print("{:<5} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15}".format(
            i + 1, a, b, c, fc, str_error)) # Impresión de Resultados con el formato adecuado

        # Condición de Parada 1: Raíz Exacta (Prioridad Absoluta)
        if fc == 0:
            print("-" * 90)
            print(f"La raíz exacta fue encontrada en la iteración número {i + 1}.")
            return c

        # Condición de Parada 2: Tolerancia del Error
        if i > 0 and error_actual < tol_error: # Verificación del Error
            print("-" * 90)
            print(f"Criterio de tolerancia ({tol_error}%) alcanzado en la iteración número {i + 1}.")
            return c
        
        # Actualización de variables para siguiente ciclo
        c_old = c 
        
        if fa * fc < 0: # Si el cambio de signo está en [a, c]
            b = c # Actualiza b
        else: # Si el cambio de signo está en [c, b]
            a = c # Actualiza a
            fa = fc # Actualiza fa

    print("-" * 90)
    print(f"Se alcanzó el número máximo de iteraciones ({max_iter}) sin cumplir la tolerancia.")
    return c

# Bloque Principal
try:
    funcion, texto_funcion = obtener_funcion_usuario() # Obtención de la Función
    
    # Entradas numéricas con validación básica
    a_str = input("Ingrese el límite inferior (a): ")
    b_str = input("Ingrese el límite superior (b): ")
    
    contexto_limites = {"__builtins__": None} # Entorno Seguro
    contexto_limites.update(funciones_permitidas) # Añadir funciones permitidas
    a = float(eval(a_str, contexto_limites)) # Evaluación Segura de a
    b = float(eval(b_str, contexto_limites)) # Evaluación Segura de b
    
    if a >= b: 
        raise ValueError("El límite 'a' debe ser menor que 'b'.")

    # Entradas para tolerancia y número máximo de iteraciones
    iter_str = input("Ingrese número máximo de iteraciones: ")
    tol_str = input("Ingrese error deseado en porcentaje (ej. 1 para 1%): ")
    
    max_iter_user = int(iter_str)
    tol_error_user = float(tol_str)

except Exception as e: 
    print(f"Error en la entrada de datos: {e}")
    exit()

# Ejecución del Método de Bisección
print(f"\nBuscando raíz para f(x) = {texto_funcion} en [{a}, {b}]")
raiz = biseccion_con_iteraciones(funcion, a, b, tol_error_user, max_iter_user)

if raiz is not None: # Si se encontró una raíz
    print(f"\n>>> Resultado final: x ≈ {raiz:.8f}")
    y_raiz = funcion(raiz)

    # Graficación de la Función y la Raíz Encontrada
    margen = (b - a) * 0.5 if (b - a) != 0 else 1
    x_vals = np.linspace(a - margen, b + margen, 400)
    
    y_vals = []
    try:
        y_vals = funcion(x_vals)
    except:
        y_vals = np.array([funcion(v) if np.isfinite(v) else np.nan for v in x_vals])

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {texto_funcion}', color='#1f77b4')
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='gray', ls='--')
    plt.axvline(a, color='green', ls='--', label='a')
    plt.axvline(b, color='purple', ls='--', label='b')
    plt.plot(raiz, y_raiz, 'ro', label=f'Raíz: {raiz:.5f}', zorder=5)
    
    # Ajuste visual para evitar gráficos infinitos
    y_visibles = y_vals[np.isfinite(y_vals)]
    if len(y_visibles) > 0:
        rango = np.max(y_visibles) - np.min(y_visibles)
        plt.ylim(np.min(y_visibles) - 0.1*rango, np.max(y_visibles) + 0.1*rango)
    
    plt.title("Método de Bisección")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.show()