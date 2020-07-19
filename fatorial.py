# valor = int(input('Entre com um número para saber o fatorial:'))
# fatorial = 1
# while (valor > 1):
#  fatorial = fatorial * valor
#  valor = valor - 1
# print('O fatorial é {}.'.format(fatorial))

# leia o valor de n
n = int(input("Digite um número inteiro não-negativo:"))

# inicializações
i = 1  # contador
n_fat = 1

# calcule n!
while i <= n:
    n_fat = n_fat * i
    i = i + 1

print(n_fat)
