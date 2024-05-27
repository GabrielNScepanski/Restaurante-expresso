import os

restaurantes = [
    {"nome": "Boteco do Chef", "categoria": "Bar", "ativo": True},
    {"nome": "Comeu, Morreu", "categoria": "Lanchonete", "ativo": False},
    {"nome": "Laços de Comida", "categoria": "Restaurante", "ativo": True}
]

def voltar_ao_menu_principal():
    """
    Interrompe a execução da função atual e retorna ao menu principal.
    Input: Nenhum
    Output: Retorna ao menu principal
    """
    input("\nDigite uma tecla para voltar ao menu principal: \n")
    main()

def mostrar_subtitulo(texto):
    """
    Limpa o console e exibe um subtítulo.
    
    Input:
    texto (str): O texto do subtítulo a ser exibido.
    
    Output:
    Exibe o subtítulo no console.
    """
    os.system("clear")
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)

def desligar_app():
    """
    Finaliza a execução do aplicativo, exibindo uma mensagem de despedida.
    Input: Nenhum
    Output: Mensagem de despedida no console
    """
    mostrar_subtitulo("Finalizando o app")

def opcao_invalida():
    """
    Exibe uma mensagem de erro quando o usuário seleciona uma opção inválida e retorna ao menu principal.
    Input: Nenhum
    Output: Mensagem de erro no console
    """
    print("Opção inválida\n")
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    """
    Permite ao usuário cadastrar um novo restaurante no sistema. O restaurante é inicialmente inativo.
    
    Input:
    Nome e categoria do restaurante (digitados pelo usuário)
    
    Output:
    Mensagem de sucesso no console
    """
    os.system("clear")
    nome_do_restaurante = input("Digite o nome do novo restaurante: \n")
    os.system("clear")
    categoria_do_restaurante = input(f"Digite a categoria do restaurante {nome_do_restaurante}: \n")
    restaurantes.append({"nome": nome_do_restaurante, "categoria": categoria_do_restaurante, "ativo": False})
    print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    """
    Lista todos os restaurantes cadastrados no sistema, exibindo o nome, a categoria e o status de cada um.
    
    Input: Nenhum
    Output: Lista de restaurantes no console
    """
    os.system("clear")
    print(f"{'Nome do Restaurante'.ljust(22)} -- {'Categoria'.ljust(20)} -- {'Status'}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"].ljust(20)
        categoria = restaurante["categoria"].ljust(20)
        status = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f"- {nome_restaurante} -- {categoria} -- {status}")
    voltar_ao_menu_principal()

def ativar_restaurante():
    """
    Permite ao usuário alternar o estado de um restaurante entre ativo e inativo.
    
    Input:
    Nome do restaurante (digitado pelo usuário)
    
    Output:
    Mensagem de sucesso ou erro no console
    """
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
    """
    Exibe o nome do aplicativo no console.
    Input: Nenhum
    Output: Nome do aplicativo no console
    """
    print('''
🅡🅔🅢🅣🅐🅤🅡🅐🅝🅣🅔 🅔🅧🅟🅡🅔🅢🅢🅞
  🅖🅐🅑🅡🅘🅔🅛 🅝🅐🅢🅒🅘🅜🅔🅝🅣🅞
''')

def exibir_opcoes():
    """
    Exibe as opções disponíveis para o usuário no console.
    Input: Nenhum
    Output: Opções do menu no console
    """
    print("1 - Cadastrar um restaurante")
    print("2 - Listar restaurantes")
    print("3 - Ativar um restaurante")
    print("4 - Sair do programa\n")

def escolher_opcoes():
    """
    Permite ao usuário escolher uma opção do menu e executa a função correspondente.
    
    Input:
    Opção do menu (digitada pelo usuário)
    
    Output:
    Executa a função correspondente à opção escolhida
    """
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
    """
    Função principal que coordena as operações do programa.
    
    Input: Nenhum
    Output: Executa o programa
    """
    os.system("clear")
    nome_app()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == "__main__":
    main()
