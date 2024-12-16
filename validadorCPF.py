"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

import re
import sys

print("Vamos verificar se o CPF digitado é válido.")
entrada = input("Digite o CPF: ")

# Recebendo o CPF, limpando usando o metodo replace
'''cpf = entrada \
    .replace(".", "")\
    .replace(" ", "")\
    .replace("-", "")'''

# Recebendo o CPF, limpando usando expressões regulares (re)
cpf = re.sub(
    r'[^0-9]',
    "",
    entrada
)

# verificando se o usuário passou números iguais
if cpf[0] * len(cpf) == cpf:
    print("CPF inválido")
    sys.exit()
    
# Reservando somente os nove primeiros dígitos que serão usados
cpf_nove = cpf[:9]

# criando um indice multiplicador
i = 10

# Variável que vai receber a soma
soma_cpf = 0

# for que vai percorrer os noves dígitos
for numero in cpf_nove:
    soma_cpf += int(numero) * i 
    i -= 1

# obtendo o resultado da divisão
decimo_digito = (soma_cpf * 10) % 11

# if ternario para saber qual será o 10 dígito.
decimo_digito = decimo_digito if decimo_digito <= 9 else 0


"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""


# Reservando somente os dez primeiros dígitos que serão usados
cpf_dez = cpf_nove + str(decimo_digito)

# criando um indice multiplicador
i = 11

# Variável que vai receber a soma
soma_cpf = 0

# for que vai percorrer os noves dígitos
for numero in cpf_dez:
    soma_cpf += int(numero) * i 
    i -= 1

# obtendo o resultado da divisão
digito_2 = (soma_cpf * 10) % 11

# if ternario para saber qual será o 10 dígito.
digito_2 = digito_2 if digito_2 <= 9 else 0

# motando o CPF para comparar
cpf_montado = cpf_dez + str(digito_2)

# verificando se é válido
if cpf_montado == cpf:
    print(f"O CPF {entrada} é válido")
else:
    print("CPF inválido")