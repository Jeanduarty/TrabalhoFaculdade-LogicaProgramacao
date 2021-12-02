#Função para validar se é um número
def ValidarNumero(mensagem):
    ok = False
    while not ok:
        try:
            numero = int(input(mensagem))
            ok = True
        except ValueError:
            print("Digite apenas números.")
    return numero

#Função para receber a posição do "bixo" e adiona-lo no array/lista e no final retornar a lista adicionado com a
# posição do player.(Também tem algumas validações)
def AlocarBixo(bixo,quartosIndisponiveis):
    ok = False
    while not ok:
        posicao = ValidarNumero((f"Em qual posição deseja alocar o {bixo}?"))
        if (posicao in quartosIndisponiveis):
            print("Quarto indisponíveil.\nInsira outro quarto")
        elif (posicao <= 0 or posicao > 8):
            print("Número não correspondente a um quarto.\nTente novamente!")
        else:
            quartosIndisponiveis.append(posicao)
            ok = True
    return quartosIndisponiveis

def Fase1():
    print("Especificando posição:\n[1,2,3,4]\n[5,6,7,8]\n")
    print(" ||Bem vindo a fase 1||")
    print("Na Fase 1, o jogador deve alocar o RATO e o GATO na seguinte matriz que representa os quartos:")
    print("['*', '*', '-', 'G']\n['R', '-', '*', '*']")
#Array pré-definido das posições indisponiveis
    quartosIndisponiveis = [1, 2, 4, 5, 7, 8]
    bixosAlocar = ["RATO","GATO"]

#for dos "bixos" para alocar nessa fase
    for bixo in bixosAlocar:
        quartosIndisponiveis = AlocarBixo(bixo,quartosIndisponiveis)
#Condição de derrota
    perdeu = quartosIndisponiveis[-1] == 6
    return perdeu

def Fase2():
    print(" ||Bem vindo a fase 2||")
    print("Na Fase 2, o jogador deve alocar o CÃO, CÃO, OSSO na seguinte matriz que representa os quartos:")
    print("['-', '*', '*', '*']\n['*', 'C', '-', '-']")
#Array pré-definido das posições indisponiveis
    quartosIndisponiveis = [2, 3, 4, 5, 6]
    bixosAlocar = ["CÃO","CÃO","OSSO"]

#for dos "bixos" para alocar nessa fase
    for bixo in bixosAlocar:
        quartosIndisponiveis = AlocarBixo(bixo,quartosIndisponiveis)
#Condição de derrota
    perdeu = quartosIndisponiveis[-1] != 1
    return perdeu

def Fase3():
    print(" ||Bem vindo a fase 3||")
    print("Na Fase 3, o jogador deve alocar o GATO, RATO, OSSO na seguinte matriz que representa os quartos:")
    print("['-', '*', '*', '*']\n['_', 'G', '-', '*']")
#Array pré-definido das posições indisponiveis
    quartosIndisponiveis = [2, 3, 4, 6, 8]
    bixosAlocar = ["GATO","RATO","OSSO"]

#for dos "bixos" para alocar nessa fase
    for bixo in bixosAlocar:
        quartosIndisponiveis = AlocarBixo(bixo,quartosIndisponiveis)
#Condição de derrota
    perdeu = (quartosIndisponiveis[-3] == 5 or quartosIndisponiveis[-2] != 1)
    return perdeu

def Fase4():
    print(" ||Bem vindo a fase 4||")
    print("Na Fase 4, o jogador deve alocar o QUEIJO, QUEIJO, OSSO na seguinte matriz que representa os quartos:")
    print("['-', '_', '_', '*']\n['_', 'R', '*', '*']")
#Array pré-definido das posições indisponiveis
    quartosIndisponiveis = [4, 5, 6, 7, 8]
    bixosAlocar = ["QUEIJO","QUEIJO","OSSO"]

#for dos "bixos" para alocar nessa fase
    for bixo in bixosAlocar:
        quartosIndisponiveis = AlocarBixo(bixo,quartosIndisponiveis)
#Condição de derrota
    perdeu = quartosIndisponiveis[-1] != 2
    return perdeu

def Main():
    perdeu = Fase1()
    if not perdeu:
        print("Parabéns! Você avançou pra Fase 2.\n")
        perdeu = Fase2()
    if not perdeu:
        print("Parabéns! Você avançou pra Fase 3.\n")
        perdeu = Fase3()
    if not perdeu:
        print("Parabéns! Você está na ultima Fase.\n")
        perdeu = Fase4()
    if not perdeu:
        print("PARABÉNS!!! Você é Fera!!")
    else:
        print("Você perdeu!\nObrigado por participar")
    return

if __name__ == "__main__":
    Main()