from time import sleep

def msg_confirmaçao_nome(possivel_nome):
    '''
    Função "def msg_confirmaçao_nome()": Exibe linha por linha de uma mensagem interativa, que pergunta se "O nome '{o nome inserido pelo usuário
    ficará aqui}' está correto?", com o auxílio do método "sleep", da biblioteca "time".
    > Parâmetros: "possivel_nome";
    > :param possivel_nome: Recebe o possível nome inseriro pelo usuário, exibindo-o para que o usuário tenha total convicção ao escolher entre
    confirmar o nome ou digitar o nome novamente;
    > Retorno: Sem retorno.
    '''

    sleep(1)
    print(f"=" * 50 + f"\n\033[33mO nome '{possivel_nome}' está correto?\033[m\n" + f"=" * 50)
    sleep(0.7)
    print(f"\033[35m1-\033[m \033[34mSim\033[m")
    sleep(0.7)
    print(f"\033[35m2-\033[m \033[31mNão\033[m")
    sleep(0.7)
    print(f"-" * 50)
    sleep(0.7)

def msg_nome_com_erro():
    '''
    Função "def msg_nome_com_erro()": Exibe linha por linha de uma mensagem interativa, que informa que "O nome não pode conter números ou
    caracteres especiais.", com o auxílio do método "sleep", da biblioteca "time".
    > Parâmetros: a função não recebe parâmetros;
    > Retorno: Sem retorno.
    '''

    sleep(1)
    print(f"=" * 50 + f"\n\033[31mO nome não pode conter números ou caracteres especiais.\033[m\n" + f"=" * 50)
    sleep(0.7)
    print(f"\033[35m1-\033[m \033[34mDigitar o Nome Novamente\033[m")
    sleep(0.7)
    print(f"\033[35m2- \033[31mNão Digitar o Nome Novamente\033[m")
    sleep(0.7)
    print(f"-" * 50)
    sleep(0.7)

def msg_nao_inserir_nome():
    '''
    Função "def msg_nao_inserir_nome()": Exibe linha por linha de uma mensagem interativa, que pergunta se "Deseja não inserir nome? Se confirmar, a
    pessoa não será identificada.", com o auxílio do método "sleep", da biblioteca "time".
    > Parâmetros: a função não recebe parâmetros;
    > Retorno: Sem retorno.
    '''

    sleep(1)
    print(f"=" * 50 + f"\nDeseja não inserir nome?\nSe confirmar, a pessoa não será identificada.\n" + f"=" * 50)
    sleep(0.7)
    print(f"\033[35m1-\033[m \033[34mDigitar o Nome\033[m")
    sleep(0.7)
    print(f"\033[35m2-\033[m \033[31mNão Digitar o Nome\033[m")
    sleep(0.7)
    print(f"-" * 50)
    sleep(0.7)
