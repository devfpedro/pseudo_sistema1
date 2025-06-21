from time import sleep

def msg_primeiro_nome():
    '''
    Função "def msg_confirmaçao_nome()": Exibe linha por linha de uma mensagem interativa, que informa "Prepare-se para Digitar o Nome.", com o
    auxílio do método "sleep", da biblioteca "time".
    > Parâmetros: A função não recebe parâmetros;
    > Retorno: Sem retorno.
    '''

    sleep(1)
    print(f"=" * 50)
    sleep(0.7)
    print(f"Prepara-se para Digitar o Nome.")
    sleep(0.7)
    print(f"=" * 50)
    sleep(0.7)
    print(f"Carregando", end= "")
    sleep(0.7)
    print(f".", end= "")
    sleep(0.7)
    print(f".", end= "")
    sleep(0.7)
    print(f".")
