from time import sleep

def msg_confirmaçao_idade(possivel_idade):
    '''
    Função "def msg_confirmaçao_idade()": Exibe linha por linha de uma mensagem interativa, que pergunta se "A idade inserida está correta?", com o
    auxílio do método "sleep", da biblioteca "time".
    > Parâmetros: "possivel_idade";
    > :param possivel_idade: Recebe a possível idade inserida pelo usuário como argumento, exibindo-a para que o usuário tenha total convicção ao
    escolher entre confirmar a idade ou inserir a idade novamente;
    > Retorno: Sem retorno.
    '''

    sleep(1)
    print(f"=" * 50 + f"\nA idade de '{possivel_idade}' está correta?\n" + f"=" * 50 )
    sleep(0.7)
    print(f"\033[35m1-\033[m \033[34mSim\033[m")
    sleep(0.7)
    print("\033[35m2-\033[m \033[31mNão\033[m")
    sleep(0.7)
    print(f"-" * 50)
    sleep(0.7)

def msg_idade_com_erro():
    '''
    Função "def msg_idade_com_erro()": Exibe linha por linha de uma mensagem interativa, que informa que "A idade não pode conter letras, acentuações
    ou caracteres especiais, com o auxílio do método "sleep", da biblioteca "time".
    > Parâmetros: A função não recebe parâmetros;
    > Retorno: Sem retorno.
    '''

    sleep(1)
    print(f"=" * 50 + f"\n\033[31mA idade não pode conter letras, acentuações ou caracteres especiais.\033[m\n" + f"=" * 50)
    sleep(0.7)
    print(f"\033[35m1-\033[m \033[34mDigitar a Idade Novamente\033[m")
    sleep(0.7)
    print(f"\033[35m2-\033[m \033[31mNão Digitar a Idade Novamente\033[m")
    sleep(0.7)
    print(f"-" * 50)
    sleep(0.7)

def msg_nao_inserir_idade():
    '''
    Função "msg_nao_inserir_idade()": Exibe linha por linha de uma mensagem interativa, que pergunta se "Deseja não inserir a idade? Se confirmar",
    a pessoa ficará com uma idade de '0 anos'.", com o auxílio do método "sleep", da biblioteca "time".
    > Parâmetros: A função não recebe parâmetros;
    > Retorno: Sem retorno.
    '''

    sleep(1)
    print(f"=" * 50 + f"\nDeseja não inserir idade?\nSe confirmar, a pessoa ficará com uma idade de '0 anos'.\n" + f"=" * 50)
    sleep(0.7)
    print(f"\033[35m1-\033[m \033[34mDigitar a Idade\033[m")
    sleep(0.7)
    print(f"\033[35m2-\033[m \033[31mNão Digitar a Idade\033[m")
    sleep(0.7)
    print(f"-" * 50 )
    sleep(0.7)
