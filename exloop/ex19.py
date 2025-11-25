a=1
b=1
contador=2

print("Sequência de Fibonacci:")
print(f"1º: {a}")
print(f"2º: {b}")

for i in range(3, 61):
    c = a + b
    print(f"{i}º: {c} = {a} + {b}")
    a = b
    b = c