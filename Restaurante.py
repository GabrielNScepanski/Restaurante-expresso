import os


restaurantes = [
    {"nome": "Boteco do Chef", "categoria": "Bar", "ativo": True},
    {"nome": "Comeu, Morreu", "categoria": "Lanchonete", "ativo": False},
    {"nome": "Laços de Comida", "categoria": "Restaurante", "ativo": True}
]


def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal: \n")
    main()


def mostrar_subtitulo(texto):
    os.system("clear")
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)


def desligar_app():
    mostrar_subtitulo("Finalizando o app")


def opcao_invalida():
    print("Opção inválida\n")
    voltar_ao_menu_principal()


def cadastrar_novo_restaurante():
    os.system("clear")
    nome_do_restaurante = input("Digite o nome do novo restaurante: \n")
    os.system("clear")
    categoria_do_restaurante = input(f"Digite a categoria do restaurante {nome_do_restaurante}: \n")
    restaurantes.append({"nome": nome_do_restaurante, "categoria": categoria_do_restaurante, "ativo": False})
    print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()


def listar_restaurantes():
    os.system("clear")
    print(f"{'Nome do Restaurante'.ljust(22)} -- {'Categoria'.ljust(20)} -- {'Status'}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"].ljust(20)
        categoria = restaurante["categoria"].ljust(20)
        status = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f"- {nome_restaurante} -- {categoria} -- {status}")
    voltar_ao_menu_principal()


def ativar_restaurante():
    mostrar_subtitulo("Alternando o estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso!"
            print(mensagem)
            break

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")
    voltar_ao_menu_principal()


def nome_app():
    print('''
🅡🅔🅢🅣🅐🅤🅡🅐🅝🅣🅔 🅔🅧🅟🅡🅔🅢🅢🅞
''')


def exibir_opcoes():
    print("1 - Cadastrar um restaurante")
    print("2 - Listar restaurantes")
    print("3 - Ativar um restaurante")
    print("4 - Sair do programa\n")


def escolher_opcoes():
    try:
        escolha = int(input("Escolha uma opção: "))
        print("Você selecionou a opção:", escolha, "\n")
        if escolha == 1:
            cadastrar_novo_restaurante()
        elif escolha == 2:
            listar_restaurantes()
        elif escolha == 3:
            ativar_restaurante()
        elif escolha == 4:
            desligar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    os.system("clear")
    nome_app()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == "__main__":
    main()
