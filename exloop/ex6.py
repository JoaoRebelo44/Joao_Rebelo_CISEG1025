contador=0
num=2
primo=0
while contador < 10:
    primo = True
    
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    
    if primo:
        print(num)
        contador = contador + 1
    
    num = num + 1