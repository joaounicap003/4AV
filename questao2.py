#função para calcular a quantidade de digitos do número inteiro
def quantidade_de_digitos(n):
    transformar_n_em_string = str(n)
    ler_a_quantidade_de_digitos_da_string = len(transformar_n_em_string)
    return ler_a_quantidade_de_digitos_da_string
    
#dados de entrada
n = int(input("digite um número inteiro: "))

#saída de dados
print(quantidade_de_digitos(n))