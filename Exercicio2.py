#Função para alterar os caracteres
def ConverterNome(nome):
    nome = nome.upper()
    print(nome)

#Tupla dos caracteres
    parCaracteres = (("A","@"),("E","&"),("I","!"),("O","#"),("U","*"))

    for caractere in parCaracteres:
        nome = nome.replace(caractere[0],caractere[1])
    print(nome)

def Main():
    nome = ConverterNome(input("Digite seu nome: "))

#Main
if __name__ == "__main__":
    Main()




