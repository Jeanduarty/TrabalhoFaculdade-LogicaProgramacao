from random import randint

#Função para validar se é um número
def ValidarNumero(mensagem):
    ok = False
    while not ok:
        try:
            numero = int(input(mensagem))
            ok = True
        except ValueError:
            print("Digite apenas números")
    return numero

#Função para pegar os dados e criar uma nova inscrição dentro dicionario
def NovaInscricao():
    inscricao = {}
    inscricao["voucher"] = randint(100,400)
    inscricao["nome"] = input("Digite seu nome: ")
    inscricao["email"] = input("Digite o seu email: ")
    inscricao["telefone"] = ValidarNumero("Digite o seu telefone: ")
    inscricao["curso"] = input("Digite o seu curso: ")
    return inscricao

#função para visualizar as inscrições
def VisualizarInscricoes(inscricoesLista):
    print(f"{'-' * 12} Lista de Inscritos {'-' * 12}")
    for indice,inscricao in enumerate(inscricoesLista):
        print(f"{'*' * 12} Inscrição {indice + 1}{'*' * 12}")
        for chave,valor in inscricao.items():
            print(f" {chave} : {valor}")
    return

#Main: Adiciona a inscrição que está no dicionario dentro de um array/lista
def Main():
    inscricoesLista = []
    menuLista = ["Nova inscrição","Visualizar inscrições","Encerrar"]
    ok = False
    while not ok:
        print(f"\n{'-' * 12} Menu {'-' * 12}")
        for indice,menu in enumerate(menuLista):
            print(f"{indice + 1} - {menu}")

        opcaoMenu = ValidarNumero("Escolha uma opção: ")
        if opcaoMenu == 1:
            inscricoesLista.append(NovaInscricao())
        elif opcaoMenu == 2:
            VisualizarInscricoes(inscricoesLista)
        elif opcaoMenu == 3:
            print("Encerrando...")
            ok = True
        else:
            print("Apenas números entre 1 e 3!")
    return

if __name__ == "__main__":
    Main()