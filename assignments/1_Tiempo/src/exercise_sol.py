def main():
    tiempo = int(input("Introduce el tiempo: "))
    horas = tiempo // 3600
    print("Horas:", horas)
    residuo = tiempo % 3600
    #print("Residuo :", residuo)
    minutos = residuo // 60
    print("Minutos:", minutos)
    segundos = residuo % 60
    print("Segundos:", segundos)

if __name__ == '__main__':
    main()