'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
'''

n = int(input (' informe quantos termos você quer monstrar: '))
t1 = 0
t2 = 1
print(f"{t1}, {t2}", end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f", {t3}", end='')
    t1 = t2
    t2 = t3
    cont +=1
print(' Fim')   