n = int(input("Digite um número inteiro:: "))
i = 0
soma = 0
while n != 0:
   soma = soma + (n % 10)
   n = n // 10
print(soma)
