import os, re


# Modelos de roteadores suportados pela automação
def roteadores():
    print("1 - Archer C50, Archer C20, WR849N, WR949N, WR940N, WR840N, WR845N",
    "2 - Archer C7, Archer C50, Archer C20, WR845N",
    "3 (Em manutenção) - Archer C7, Archer C6, AX50, AX10, Archer C60", sep='\n')


def menu():
    print('---------------------------- MENU DE AUTOMAÇÃO ----------------------------------')
    print("Começaremos agora o processo de configuração do seu roteador!")
    print("Mas antes, preciso saber algumas informações bem básicas, ok?")
    print("Iremos trabalhar apenas com tp-link por agora :)")
 
    print()

    print("Qual opção contém o modelo do seu roteador?")
    print("Essa informação pode ser encontrada na parte de baixo do mesmo.")
    roteadores()
    model = int(input("Por favor, digite o número correspondente: "))
    while model < 1 or model > 4:
        print("\nOpção inválida!\nQual opção contém o modelo do seu roteador?")
        roteadores()
        model = int(input("Por favor, digite novamente o número correspondente: "))
    
    # Pegando a informação se é cabo ou wifi para pegaro IP de acordo com a configuração
    print("\nSeu computador está conectado no cabo ou no wifi?\n1 - Cabo\n2 - Wifi")
    wifi = int(input("Por favor, digite o número correspondente: "))
    while wifi < 1 or wifi > 2:
        print("\nOpção inválida!\nSeu computador está conectado no cabo ou no wifi?\n1 - Cabo\n2 - Wifi")
        wifi = int(input("Por favor, digite novamente o número correspondente: "))
    
    os.system("cls") or None

    print('---------------------------- MENU DE AUTOMAÇÃO ----------------------------------')
    print("Você sabe o login e a senha do seu roteador?",
    "Na maioria dos casos, a senha e o login estão na parte de baixo dele.",
    "Caso não saiba e também não haja nenhuma informação no roteador, não tem problema!"
    "Iremos tentar configurar assim mesmo com senhas padrões.", sep='\n')
    if model == 3:
        print("\nÉ necessário inserir o e-mail cadastrado, onde esse servirá como login!")
        loginBox = input("Digite seu e-mail: ")
        regex = r'^[a-zA-Z0-9._-]+@([a-z0-9]+)(.[a-z]{2,3})+$'
        while not re.search(regex, loginBox):
            print("\nFormato inválido!")
            loginBox = input("Por favor, digite novamente seu e-mail: ")
    else:
        print("\nMuitas vezes existe somente uma senha, mas caso tenha login, digite abaixo.\nSe não souber, deixe em branco e aperte ENTER!")
        loginBox = input("Digite seu login: ")
        if not loginBox:
            loginBox = None

    print("\nSe não souber a senha, deixe em branco e aperte ENTER.\nPodemos tentar com senhas padrões!")
    passwordBox = input("Digite sua senha: ")
    if not passwordBox:
        passwordBox = None

    os.system("cls") or None

    print('---------------------------- MENU DE AUTOMAÇÃO ----------------------------------')
    print("Agora digite o nome e a senha que você quer no seu Wi-Fi!")
    ssid, senhaW = input("Digite o nome: "), input("Digite a senha: ")
    while(len(ssid) < 2):
        ssid = input("\nO nome deve ter, no mínimo, 2 caracteres!\nDigite o nome novamente: ")
    while (len(senhaW) < 8):
        senhaW = input("\nA senha deve ter, no mínimo, 8 caracteres!\nDigite a senha novamente: ")

    os.system("cls") or None

    print('---------------------------- MENU DE AUTOMAÇÃO ----------------------------------')
    if loginBox == None and passwordBox == None:
        print("Iremos tentar o processo com as senhas padrões!")    
    
    return [loginBox, passwordBox, wifi, ssid, senhaW, str(model)]
