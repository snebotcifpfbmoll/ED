# P06E14:
# Desarrolla un programa junto con tu compañero, apoyándote en la “metodología pair programming” que tenga las siguientes características:
# While
print("Calculadora Fibonacci")
iteraciones = int(input("Introduce el numero de valores que quieres: "))
num_1 = 0
num_2 = 1

print("%d, %d, " % (num_1, num_2), end="")
while iteraciones > 2:
    resultado = num_1 + num_2
    print(resultado, end="")

    if iteraciones > 3:
        print(end=", ")

    num_1 = num_2
    num_2 = resultado
    iteraciones -= 1
print("")

# For
iteraciones = int(input("Introduce el numero de valores que quieres: "))

num_1 = 0
num_2 = 1

print("%d, %d, " % (num_1, num_2), end="")
for i in range(iteraciones - 2):
    resultado = num_1 + num_2
    print(resultado, end="")

    if i < iteraciones - 3:
        print(end=", ")

    num_1 = num_2
    num_2 = resultado
print("")

# Reflexion:
# En adecuacion, el for es mas apropiado para este caso puesto que es una secuencia a la que el usuario fija la cantidad de veces que se repetira la misma, si bien el while puede utilizarse para la misma funcion agregando una variable auxiliar, este es mas apropiado para un entorno en el que se desconozca la cantidad de veces que se repetira la secuencia.
# Don Serafin Nebot Ginard y Don Daniel Alfredo Apesteguia Timoner ©
