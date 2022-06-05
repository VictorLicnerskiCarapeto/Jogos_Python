import forca
import adivinhacao

print("********************************")
print("Escolha o seu jogo!")
print("********************************")

print("(1) Forca (2) Advinhação")

jogo = int(input("Qual jogo?\n"))
if(jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando advinhação")
    adivinhacao.jogar()