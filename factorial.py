def factorial(n):
    """
    Calcula el factorial de un número entero positivo.
    
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        numero = int(input("Ingresa un número entero para calcular su factorial: "))
        resultado = factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
        
    except ValueError:
        print("Ingresa un número entero positivo.")
