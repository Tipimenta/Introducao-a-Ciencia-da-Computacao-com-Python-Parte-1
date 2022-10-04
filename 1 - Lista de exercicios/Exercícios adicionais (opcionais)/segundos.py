numero = int(input("Por favor, entre com o número de segundos que deseja converter: "))

a = numero // 86400
b = (numero % 86400) // 3600
c = ((numero % 86400) % 3600) // 60
d = (numero % 86400) % 60

print(f"{a} dias, {b} horas, {c} minutos e {d} segundos.")