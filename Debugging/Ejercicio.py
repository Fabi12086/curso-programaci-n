def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)
    

def comparar_con_promedio(num, promedio):
    for num in numeros:
        if num > promedio:# en los if, elif y else siempre se colocan : al final
            print(f"{num} es mayor que el promedio.")
        elif num < promedio:
            print(f"{num} es menor que el promedio.")
        else:
            print(f"{num} es igual al promedio.")

# Pedir al usuario tres números
numeros = []
for i in range(3):
    num = int(input("Introduce un número: "))#Colocar un int para representar los números enteros
    numeros.append(num)

# Calcular el promedio
promedio = calcular_promedio(numeros)

# Comparar cada número con el promedio
comparar_con_promedio(numeros, promedio)