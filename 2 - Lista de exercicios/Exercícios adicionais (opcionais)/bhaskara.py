import math

a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = (b ** 2) - 4 * a * c

if delta == 0:
    r1 = (-b + math.sqrt(delta))  / (2 * a)
    print(f"a raiz desta equação é {r1}")
elif delta < 0:
    print("esta equação não possui raízes reais")
else:
    r1 = (-b + math.sqrt(delta))  / (2 * a)
    r2 = (-b - math.sqrt(delta))  / (2 * a)
    if (r1 > r2):
        print(f"as raízes da equação são {r2} e {r1}")
    else:
        print(f"as raízes da equação são {r1} e {r2}")
