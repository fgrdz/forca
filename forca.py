import random
from os import system, name 

def limpa_tela():
    
    if name == 'nt':
        _= system('cls')
    else:
        _= system('clear')




def jogo():
    limpa_tela()

    
    print("\n***********************************")
    print("\nBem vindo ao jogo da forca")
    print("Advinhe a palavra abaixo")
    print("\n***********************************")

    palavras_possiveis = ['abacaxi', 'carro', 'bola', 'controle', 'casa', 'amor']
    palavra = random.choice(palavras_possiveis)

    letras_descobertas = ['_' for letra in palavra]
    
    chances = 6

    erradas = []

    

    while chances > 0:
        print(f"\n{letras_descobertas}")
        print(f"\nchances restantes: {chances}")
        print(f"\nLetras erradas: {erradas}")

        tentativa = input("Digite uma letra: ").lower()

        if tentativa in palavra:
            i = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[i] = letra
                i+=1
        else:
            chances -=1
            if tentativa in erradas:
                print("Você já tentou essa letra, tente outra")
            else:
                erradas.append(tentativa)
        if "_" not in letras_descobertas:
            print(f"Você acertou a palavra {palavra}")
            break
    if "_" in letras_descobertas:
        print(f"Você perdeu, a palavra era {palavra}")
        
if __name__ == "__main__":
    jogo()
    print("\n Programa finalizado")





        
