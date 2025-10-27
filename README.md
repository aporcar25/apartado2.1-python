# Ejercicios Lección 2 - Tipos Simples en Python

Este repositorio contiene los ejercicios del apartado 2.1 de la Lección 2.
Cada ejercicio tiene al menos dos commits: uno de inicio y otro final y un **tag** que marca la versión final.

---

## Índice de Ejercicios

| N° | Ejercicio | Descripción | Tag final |
|----|------------|-------------|------------|
| 1 | Perímetro y área del rectángulo | Calcula perímetro y área con base y altura dadas | `v1.0-ejer1` |
| 2 | Hipotenusa de triángulo rectángulo | Calcula hipotenusa con teorema de Pitágoras | `v1.0-ejer2` |
| 3 | Operaciones básicas | Suma, resta, multiplicación y división de dos números | `v1.0-ejer3` |
| 4 | Conversión Fahrenheit → Celsius | Convierte 212°F a °C | `v1.0-ejer4` |
| 5 | Media de tres números | Calcula la media aritmética de 3, 4 y 5 | `v1.0-ejer5` |
| 6 | Cadena mayúsculas y guiones | Convierte "hola mundo desde python" a mayúsculas y con guiones | `v1.0-ejer6` |
| 7 | Nombre en Title Case | Convierte "juan_perez_garcia" en "Juan Perez Garcia" | `v1.0-ejer7` |

---

## Algoritmos

### Ejercicio 1: Perímetro y área del rectángulo
1. Identificar base y altura.  
2. Calcular perímetro: `2 * (base + altura)` directamente en `print()`.  
3. Calcular área: `base * altura` directamente en `print()`.  

### Ejercicio 2: Hipotenusa
1. Identificar los catetos.  
2. Elevar cada cateto al cuadrado usando `**2`.  
3. Sumar los cuadrados y calcular raíz cuadrada con `**0.5`.  

### Ejercicio 3: Operaciones básicas
1. Identificar los dos números.  
2. Realizar suma, resta, multiplicación y división directamente dentro de `print()`.  

### Ejercicio 4: Conversión Fahrenheit → Celsius
1. Identificar el valor en Fahrenheit.  
2. Aplicar fórmula: `(F - 32) * 5 / 9` directamente en `print()`.  

### Ejercicio 5: Media de tres números
1. Identificar los tres números.  
2. Calcular media: `(num1 + num2 + num3) / 3` directamente en `print()`.  

### Ejercicio 6: Cadena mayúsculas y guiones
1. Tomar la cadena `"hola mundo desde python"`.  
2. Aplicar `upper()` para mayúsculas y `replace(" ", "-")` para guiones.  
3. Mostrar el resultado con `print()`.  

### Ejercicio 7: Nombre en Title Case
1. Tomar la cadena `"juan_perez_garcia"`.  
2. Reemplazar `_` por espacio con `replace("_", " ")`.  
3. Aplicar `title()` para poner inicial mayúscula en cada palabra.  
4. Mostrar el resultado con `print()`.  

---

## Control de versiones
Cada ejercicio sigue este flujo:

1. Commit inicial (`wip`) → archivo creado o con algo escrito escrito.  
2. Commit final (`feat`) → ejercicio terminado sin variables.  
3. Tag final → `v1.0-ejerX` para marcar versión estable.  

Todos los ejercicios están subidos a GitHub y etiquetados correctamente.
