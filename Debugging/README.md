# Debugging

_Propietario_: Fabiola Piedra Fallas

## Errores encontrados

En este código se econtraron en total dos errores los cuales fueron:

## _Error en la sintaxis_

Este fue el no colocarle los : al final de cada if, elif y else, por lo tanto para resolverlo lo que
se hizo fue colocarle estos : faltantes.
La forma correcta:

```
    if num > promedio:
```

La forma incorrecta:

```
    if num > promedio
```


## _Error lógico_

Este error fue el no colocar un int antes de hacer el input, ya que se necesita el int para representar los números enteros que el usuario ingrese a través del input, por lo tanto para resolverlo lo que se hizo fue colocar el int antes del input.
La forma correcta es:

```
    num = int(input("Introduce un número: "))
```

Y la forma incorrecta es:

```
    num = input("Introduce un número: ")
```