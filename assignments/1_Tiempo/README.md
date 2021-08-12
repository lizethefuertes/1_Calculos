![Tec de Monterrey](../../images/logotecmty.png)
# Tiempo en horas, minutos y segundos
**Programas que requieren cálculos**

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python

def main():
  # Escribe tu código abajo de esta línea
  pass

if __name__ == '__main__':
    main()
```

La línea `#Escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

Escriba un programa que convierta un tiempo expresado en segundos al formato de horas, minutos y segundos. 
Considera que el valor del tiempo en segundos es proporcionado por el usuario. 
Solicite un tiempo en segundos y calcule la cantidad de horas, minutos y segundos.
Despliegue los resultados en pantalla. Variables utilizadas: tiempo, horas, minutos, 
segundos y residuo.

Casos de prueba:

**Entradas**
tiempo (entero) Tiempo en segundos

**Salida**
horas
minutos
segundos

Estos son algunos ejemplos de ejecución del programa. La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Introduce el tiempo: 8243
Horas: 2
Minutos: 17
Segundos: 23

Introduce el tiempo: 3521
Horas: 0
Minutos: 58
Segundos: 41

Introduce el tiempo: 5679
Horas: 1
Minutos: 34
Segundos: 39
```
**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento. No la vamos a necesitar para
este programa, pero es una buena práctica incluirla y quedará más
claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest` o `pytest --tb=short`,
subela a tu repositorio en GitHub, con el proceso de commit + push.
