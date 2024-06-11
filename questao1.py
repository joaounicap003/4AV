#função que vai retornar o inverso do número inteiro
def numero_reverso(n):
    transformar_n_em_string = str(n)
    string_invertida = transformar_n_em_string[::-1]
    return string_invertida

#dados de entrada
n = int(input("digite um número inteiro: "))

#saída de dados
print(numero_reverso(n))