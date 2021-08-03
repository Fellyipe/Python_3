import random # importa uma biblioteca, um arquivo, etc

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3
    rodada = 1
    pontos = 1000

    print("Qual a dificuldade?")
    print("(1) fácil (2) médio (3) difícil")
    dificuldade = int(input("Defina o nível:"))

    if (dificuldade == 1):
        total_de_tentativas = 20
    elif (dificuldade == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número: ") # o input sempre devolve uma string
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100')
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou! Você fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
                pontos_perdidos = abs(chute - numero_secreto) # o abs() dá um número absoluto, como se fosse um módulo
                pontos = pontos - pontos_perdidos

                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute) # o abs() dá um número absoluto, como se fosse um módulo
                pontos = pontos - pontos_perdidos

                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
        rodada = rodada + 1

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
print("Deseja jogar novamente? (Digite 1 para SIM e 2 para NÃO)")
jogar_denovo = input()
if (jogar_denovo == '1'):
    jogar()