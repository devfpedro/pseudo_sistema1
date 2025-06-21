from projeto import msg_de_interaçao
from time import sleep
import shelve

def exibir_lista_pessoas():
    '''
    Função "def exibir_lista_pessoas()": Exibirá ordenadamente todos os nomes e idades das pessoas resgistradas no arquivo shelve.
    > Parâmetros: A função não recebe parâmetros;
    > Retorno: Sem retorno.
    '''

    with shelve.open("projeto/ação_opções/opção1/dados_pessoa/guardar_lista_pessoas/lista_pessoas") as lista_pessoas_registradas:
        if len(lista_pessoas_registradas) > 0:
            exibir_lista= lista_pessoas_registradas["pessoas_registradas"]
            sleep(1)
            print(f"=" * 50 + f"\n\033[1;34m" + f"Lista de Pessoas Registradas".center(50) + f"\n\033[m" + f"=" * 50)
            for pessoa in range(0, len(exibir_lista)):
                sleep(1)
                print(f"\033[33m{pessoa+1}° Pessoa:\033[m \033[1m{exibir_lista[pessoa]["pessoa_" + str(pessoa+1)]["nome"]}\033[m, com \033[1m{exibir_lista[pessoa]["pessoa_" + str(pessoa+1)]["idade"]}\033[m" + f"\n")
                sleep(1)
                print((f"-" * 50) if pessoa < (len(exibir_lista) - 1) else (f"-" * 22 + "{XXXX}" + f"-" * 22))
            sleep(1)
            print(f"=" * 50 + f"\nPrepare-se para Voltar ao Menu Principal.")
            msg_de_interaçao.msg_carregando()
        else:
            sleep(1)
            print(f"=" * 50 + f"\n\033[31mNenhuma pessoa foi registrada ainda.\033[m")
            sleep(1)
            print(f"=" * 50 + f"\nVoltando ao Menu Principal.")
            msg_de_interaçao.msg_carregando()
