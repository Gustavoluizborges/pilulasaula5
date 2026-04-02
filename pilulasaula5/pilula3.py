def verificarValores():
    anterior = float(input('Leitura 1: '))
    crescente = True
    
    for i in range(4):
        atual = float(input(f'Leitura: {i+2}: '))
        if atual <= anterior:
            crescente = False
        anterior = atual
    return True

#main
if(verificarValores()):
    print('Crescente')
else:
    print('Instável')