import math

def main():
    r = float(input("Radio: "))
    h1 = float(input("Altura 1: "))
    h2 = float(input("Altura 2: "))
    v = (math.pi*math.pow(r,2)*(h1+h2))/2 
    print("Volumen: %.2f" % v)

if __name__ == '__main__':
    main()