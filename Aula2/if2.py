# If extrutura de decisão
# Operadores de decisão
# == Igualdade
# != Diferente
# >= Maior ou igual
# > Maior
# <= Menor ou igual
# < Menor
# Valro 1 X Valor 2


# Operadores Logicos
# and = e
# or = ou
# Valor 1 X Valor 2 and Valor 2 X Valor 3


num1=0
num2=0
num3=0

num1= int(input("Introduza o 1 numero "))

num2= int(input("Introduza o 2 numero "))

num3= int(input("Introduza o 3 numero "))

if num1 > num2 and num2 > num3:  # num1 > num2 > num3
    print(f"O maior número é {num1}, o menor número é {num3}, e o numero do meio é {num2}")
elif num1 > num3 and num3 > num2:  # num1 > num3 > num2
    print(f"O maior número é {num1}, o menor número é {num2},e o numero do meio é {num3}" )
elif num2 > num1 and num1 > num3:  # num2 > num1 > num3
    print(f"O maior número é {num2}, o menor número é {num3}, e o numero do meio é {num1}")
elif num2 > num3 and num3 > num1:  # num2 > num3 > num1
    print(f"O maior número é {num2}, o menor número é {num1}, e o numero do meio é {num3}")
elif num3 > num1 and num1 > num2:  # num3 > num1 > num2
    print(f"O maior número é {num3}, o menor número é {num2}, e o numero do meio é {num1}")
elif num3 > num2 and num2 > num1:  # num3 > num2 > num1
    print(f"O maior número é {num3}, o menor número é {num1}, e o numero do meio é {num2}")
else:
    print("Alguns eram iguais")