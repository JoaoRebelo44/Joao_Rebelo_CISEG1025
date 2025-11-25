

num=0
i=0

for i in range(1,11):
 num= int(input(f"Insira o {i} numero "))
 if num%2==0:
  print(f"{num} é par")
 else:
  print(f"{num} é impar")