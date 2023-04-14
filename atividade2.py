 
num = int(input("Digite um número inteiro: "))


a, b = 0, 1


while b <= num:
   
    if b == num:
        print("O número", num, "pertence à sequência de Fibonacci.")
        break
    a, b = b, a + b
else:
    print("O número", num, "não pertence à sequência de Fibonacci.")
