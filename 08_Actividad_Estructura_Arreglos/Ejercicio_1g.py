fibonacci = [0, 1]

for i in range(2, 10):
    valor = fibonacci[i-1] + fibonacci[i-2]
    
    fibonacci.append(valor)


for i in range(0, len(fibonacci)):
    print(fibonacci[i])