#Função para validar se é um número
def ValidarNumero(mensagem):
    ok = False
    while not ok:
        try:
            numeroLimpo = int(input(mensagem))
            ok = True
        except ValueError:
            print("Digite apenas números.")
    return numeroLimpo

#Função para printar o resultado final
def PrintMensagem(nome,idade,opcaoEnsino):
    ensinos = ["Ensino Infantil","Ensino Fundamental I","Ensino Fundamental II","Ensino Médio"]
    print(f"{nome} tem {idade} anos e está no {ensinos[opcaoEnsino]}.")

def Main():
#"ok" é uma variável flag
    ok = False
    while not ok:
#Dados de entrada
        print ("Ru do aluno: 2343706")
        nome = input("Nome da criança: ")
        idade = ValidarNumero("Idade: ")

#if para definir o ensino do usuario
        if (idade <= 0):
            print("idade invalida refaça o teste")
        elif(idade < 6):
            PrintMensagem(nome,idade,0)
        elif(idade < 11 ):
            PrintMensagem(nome,idade,1)
        elif(idade < 15):
            PrintMensagem(nome,idade,2)
        else:
            PrintMensagem(nome,idade,3)
#Continuar ou não.
        continuar = ValidarNumero("Deseja continuar?\n 0 - Não // 1 - Sim ")
        if (continuar == 1):
            print("")
        else:
            ok = True

if __name__ == "__main__":
    Main()
