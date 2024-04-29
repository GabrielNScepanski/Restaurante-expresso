import os

restaurantes=[{"nome":"Comeu Morreu","Laços de Comida":"bar","Ativo": True},
            {"nome":"Comeu Morreu","Laços de Comida":"bar","Ativo": False},
            {"nome":"Comeu Morreu","Laços de Comida":"bar","Ativo": True}]

def desligar_app():
    os.system("clear")
    print("Desligando o app\n")

def opcao_invalida():
    print("Opção inválida\n")
    input("Digite uma tecla para voltar ao menu principal: ")
    os.system("clear")
    main()

def cadastrar_novo_restaurante():
    os.system("clear")
    nome_do_restaurante=input("digite o nome do novo restaurante: \n")
    restaurantes.append(nome_do_restaurante)
    print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    input("Digite uma tecla para voltar ao menu principal: ")
    os.system("clear")
    main()

def listar_restaurantes():
    os.system("clear")
    print("Restaurantes cadastrados:\n")
    for restaurante in restaurantes:
        neme_restaurante = restaurante["nome"]
        neme_restaurante = restaurante["categoria"]
        print(f"-{nome_restaurante}--{categoria}")
    input("\nDigite uma tecla para voltar ao menu principal: ")
    os.system("clear")
    main()    

def nome_app():
    print("""
    
    🇷​​​​​🇪​​​​​🇸​​​​​🇹​​​​​🇦​​​​​🇺​​​​​🇷​​​​​🇦​​​​​🇳​​​​​🇹​​​​​🇪​​​​​ 🇪​​​​​🇽​​​​​🇵​​​​​🇷​​​​​🇪​​​​​🇸​​​​​🇸​​​​​🇴​​​​
    
    
    ​""")

def exibir_opcoes():
    print("1-Cadastrar um restaurante")
    print("2-Listar restaurantes")
    print("3-Ativar um restaurante")
    print("4-Sair do programa\n")

def escolher_opcoes():
    try:
        escolha=int(input("Escolha uma opção: "))
        print("Você selecionou a opção:",escolha,"\n")
        if escolha == 1:
            cadastrar_novo_restaurante()
        elif escolha == 2:
            listar_restaurantes()
        elif escolha == 3:
            print("Você escolheu ativar um restaurante\n")
        elif escolha == 4:
            print("Você escolheu sair do programa\n")
            desligar_app()
        else:
            opcao_invalida()

    except:
        opcao_invalida()

def main():
    os.system("clear")
    nome_app()
    exibir_opcoes()
    escolher_opcoes()

if __name__=="__main__":
    main()