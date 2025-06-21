from .ação_opções.opção1.ação_opção1 import adicionar_pessoa
from .ação_opções.opção2.ação_opção2 import exibir_lista_pessoas
from .msg_de_interaçao import opçoes_menu_principal, msg_carregando, msg_erro_KeyboardInterrupt, msg_encerrar_programa, msg_agradecimento
from time import sleep
import shelve

def selecionar_opçao():
    '''
    Função "def selecionar_opcao()": Exibirá o Menu Principal e suas respectivas opções, permetindo que o usuário selecione o que deseja fazer. Caso
    o usuário digite um valor que não corresponda a nenhuma das opções, a função permitirá que o usuário selecione digite novamente. Após selecionar
    uma opção possível, a função verificará se o usuário deseja inserir uma nova pessoa à lista, ver a lista com todas as pessoas registradas ou sair
    do sistema. Dependendo da opçõa escolhida, a função importará os arquivos e funções necessários para executá-la.
    > Parâetros: A função não recebe parâmetros;
    > :param return: Sem retorno.
    '''

    while True:
        try:
            opçoes_menu_principal()
            escolher_opçao= str(input(f"=> ").strip().lower())
            
            if escolher_opçao == "1":
                adicionar_pessoa()
            elif escolher_opçao == "2":
                exibir_lista_pessoas()
            elif escolher_opçao == "3":
                while True:
                    msg_encerrar_programa()
                    confirmar_saida= str(input(f"=> ").strip().lower())
                    if confirmar_saida == "1" or confirmar_saida == "2":
                        if confirmar_saida == "1":
                            sleep(1)
                            print(f"=" * 50 + f"\nPrepare-se para Voltar ao Menu Principal.")
                            msg_carregando()
                        break
                    sleep(1)
                    print(f"=" * 50 + f"\n\033[31mEssa opção não está disponível.\033[m")

                if confirmar_saida == "2":
                    msg_agradecimento()
                    break
            else:
                sleep(1)
                print(f"=" * 50 + f"\n\033[31mEssa opção não está disponível.\033[m")

        except (KeyboardInterrupt):
            while True:
                msg_erro_KeyboardInterrupt()
                confirmar_nenhuma_info= str(input(f"=> ").strip().lower())

                if confirmar_nenhuma_info == "1" or confirmar_nenhuma_info == "2":
                    if confirmar_nenhuma_info == "1":
                        sleep(1)
                        print(f"=" * 50 + f"\nPrepare-se para Voltar ao Menu Principal.")
                        msg_carregando()
                    break

                sleep(1)
                print(f"=" * 50 + f"\n\033[31mEssa opção não está disponível.\033[m")
        
            if confirmar_nenhuma_info == "2":
                msg_agradecimento()
                break
