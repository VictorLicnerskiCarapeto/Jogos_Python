import random

def jogar():
    print("********************************")
    print("Bem vindo no jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificulodade ?")
    print("Nível 1 - fácil(20 tentativas)", "Nível 2 - Médio(10 tentativas)",
          "Nível 3 - Dífícil(5 tentativas)", sep="\n")

    nivel = int(input("Escolha um nível: "))
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for tentativa_atual in range(1, total_tentativas + 1):
        print(f"Tentativa {tentativa_atual} de {total_tentativas}")
        # entrada
        chute = input("Digite um número entre 1 e 100: ")
        chute_int = int(chute)
        acertou = numero_secreto == chute_int

        if (chute_int < 1 or chute_int > 100):
            print("Invalido!!")
            continue

        # tratamento
        maior = chute_int > numero_secreto
        menor = chute_int < numero_secreto
        print("Voce digitou", chute)
        if (acertou):
            print(f"Você acertou! e fez {pontos} pontos!")
            break
        else:
            if (maior):
                print("Você errou!! \nSeu chute foi maior que o número secreto.")
                if (tentativa_atual == total_tentativas):
                    print(f"O número secreto era {numero_secreto}. Você fez {pontos}")
            elif (menor):
                print("Você errou!! \nSeu chute foi menor que o número secreto.")
                if (tentativa_atual == total_tentativas):
                    print(f"O número secreto era {numero_secreto}. Você fez {pontos}")

            pontos_perdidos = abs(numero_secreto - chute_int)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")
if(__name__ == "__main__"):
    jogar()
