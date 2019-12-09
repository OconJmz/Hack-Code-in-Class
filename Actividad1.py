"""
Nombre: SolucionEjercicio.py
Objetivo: Resolver ejercicio 1
Autor: Antonio Valencia Delgadillo 
Fecha: 30 de octubre de 2019
"""
def main():
    a = int(input("Ingresa sueldo de trabajador:"))
    if int(a)< 1000:
        sueldo= ((a*.15)+a)
        print(str(sueldo)+ " nuevo sueldo")
    else:
        sueldo= ((a*.12)+a)
        print(str(sueldo)+ " nuevo sueldo")
    print("Adios..")
        
if __name__ == "__main__":
    main()