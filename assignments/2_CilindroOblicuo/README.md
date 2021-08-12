![Tec de Monterrey](../../images/logotecmty.png)
# Volúmen de un cilíndro recto de sección oblicua
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

Escriba un programa que calcule el volúmen (v) de un cilíndro recto de sección oblicua. 
Los valores dados por el usuario son el radio (r) y las alturas (h1 y h2) del cilíndro. 
El resultado obtenido (volumen) debe ser desplegado en la pantalla. 
Utiliza la constante math.pi de la librería math.

Casos de prueba:

**Entradas**
r   Radio (flotante) 
h1  Altura 1 (flotante)
h2  Altura 2 (flotante)

**Salida**
v   Volumen (flotante)

Estos son algunos ejemplos de ejecución del programa. La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Radio: 5
Altura 1: 2
Altura 2: 3
Volumen: 196.35

Radio: 2.5
Altura 1: 4.2
Altura 2: 8.6
Volumen: 125.66

Radio: 3.1
Altura 1: 5.7
Altura 2: 9.4
Volumen: 227.94
```
**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento. No la vamos a necesitar para
este programa, pero es una buena práctica incluirla y quedará más
claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest` o `pytest --tb=short`,
subela a tu repositorio en GitHub, con el proceso de commit + push.