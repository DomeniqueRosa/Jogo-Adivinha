import os
import random


def verifica_par(numeroAleatorio):

    if(numeroAleatorio % 2 == 0):           # Op de mod, usada para verificar se é par
        print("O número correto é par.")
    else:
        print("O número correto é ímpar.")


def dicas(numeroJogador, numeroAleatorio):
    if(numeroJogador < numeroAleatorio):
        print("O número correto é maior.")
    else:
        print(" O número correto é menor.")

  
def verificarNumero( numeroJogador,  numeroAleatorio):
    if(numeroJogador == numeroAleatorio):
        print("Parabéns você acertou! :)")
    else:
        print("Ainda não é o número correto :(")
        dicas(numeroJogador, numeroAleatorio)

              
def nivelDificuldade():

    print("Nivel 1: 3 TENTATIVAS")
    print("Nivel 2: 4 TENTATIVAS")
    print("Nivel 3: 6 TENTATIVAS")
    nivel = int(input("Qual nivel gostaria de jogar: "))

    if(nivel == 1):
        qtdTentativas = 3
        numeroAleatorio = random.randint(1,10)

    if(nivel == 2):
        qtdTentativas = 4
        numeroAleatorio = random.randint(1,100)

    if(nivel == 3):
        qtdTentativas = 6
        numeroAleatorio = random.randint(1,1000)
    
    return qtdTentativas, numeroAleatorio


def inicio():
    os.system('cls')      # Função usada para limpar tela
    
    i = 1
    chute = 0
    numeroAleatorio = 0
    qtdTentativas, numeroAleatorio = nivelDificuldade()  #

    print("Número aleatorio: ", numeroAleatorio)

    while i <= qtdTentativas and chute != numeroAleatorio:
        print("=" * 35)
        chute = int(input(f"Chute nº {i} Qual seu chute: "))
        print("-" * 35)

        if (i == 3): verifica_par(numeroAleatorio)      # Dica se esta na tentativa número 3
        verificarNumero(chute, numeroAleatorio)         # Função usada para verificar se o número esta correto
        i = i + 1
    
    print("=" * 35)
    print(f"Número correto é: {numeroAleatorio}")
    print("=" * 35)


#Main
try:
 inicio()
except BaseException:
    print("Reencie o programa ")

        
