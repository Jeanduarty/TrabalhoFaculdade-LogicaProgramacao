def AlocarBixo(bixo,quartosOcupados):
    i = False
    while not i:
        inputSujo = input("Em qual posição deseja alocar o {}?".format(bixo))
        try:
            pos = int(inputSujo)
            if (pos in quartosOcupados):
                print("Quarto indisponíveil.\nInsira outro quarto")
                continue
            elif (pos <= 0 or pos > 8):
                print("Número não correspondente a um quarto.\nTente novamente!")
                continue
            else:
                quartosOcupados.append(pos)
                i = True
        except:
            print("Digite apenas números!")
    return quartosOcupados

def Fase1():
    print(" ||Bem vindo a fase 1||")
    print("Na Fase 1, o jogador deve alocar o RATO e o GATO na seguinte matriz que representa os quartos:")
    print("['*', '*', '-', 'G']\n['R', '-', '*', '*']")

    quartosIndisponiveis = [1, 2, 4, 5, 7, 8]
    bixosAlocar = ["RATO","GATO"]

    for bixo in bixosAlocar:
        quartosIndisponiveis = AlocarBixo(bixo,quartosIndisponiveis)


def teste():
    ensinos = {"ensinoInfantil":list(range(1,6)),"ensinofundamental1":list(range(6,11)),
               "ensinoFundamental2":list(range(11,15))}

    idade = int(input("Digite: "))
    if idade in ensinos.items():
        print("10")


def teste2(idade):
    ensinos = {list(range(1,6)):"Ensino Infantil",list(range(6,11)):"Ensino Fundamental I",
               list(range(11,15)):"Ensino Fundamental II"}
    if idade in ensinos:
        print("sim")

def executar():
    return

def teste123():
    i = 10
    while (i<= 100):
        i+=1
        print(i)




if __name__ == "__main__":
    teste123()

