#função para calcular o maior número
def maior(*numero):
    maior_elemento = numero[0]
    for i in range(len(numero)):
        if numero[i] > maior_elemento:
            maior_elemento = numero[i]
#saída de dados
    
    print(maior_elemento)

#entrada de dados
maior(1, 3, 5, 7)
maior(11, 33)
maior(-1, -2)