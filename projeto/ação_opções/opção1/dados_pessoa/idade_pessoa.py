from projeto import msg_de_interaçao
from .msg_interação_NomeIdade.msg_interação_idade import msg_nao_inserir_idade, msg_idade_com_erro, msg_confirmaçao_idade
from time import sleep

def idade_pessoa():
    '''
    Função "def idade_pessoa()": Verifica se o dado inserido pelo usuário pode ser uma idade ou não, apenas permitindo que avance quando digitar um
    valor possível para uma idade. Caso o valor possa ser considerado como uma idade, o usuário terá a opção de confirmar a idade ou inserir um novo
    dado.
    > Parâmetros: A função não recebe parâmetros;
    > Retorno: Retorna a idade verificada, junto de "ano" ou "anos", dependendo se for 1 ou qualquer outro número, respectivamente, ou retorna "0
    anos", caso o usuário opte por não digitar nenhum valor ao inserir um valor que não pode ser considerado uma idade, optou por não inserir um
    valor novamente;
    > :param return: inserir_idade.
    '''

    while True:
        sleep(1)
        print(f"=" * 50 )
        sleep(0.7)
        inserir_idade= str(input(f"Digite uma idade: ").strip().lower())
        idade_conferida= True

        if inserir_idade != "":
            for conf in inserir_idade:
                if conf not in "0123456789":
                    idade_conferida= False
                    break
        else:
            idade_conferida= False
        
        if idade_conferida:
            inserir_idade= (inserir_idade + " ano") if inserir_idade == "1" else (inserir_idade + " anos")

            while True:
                msg_confirmaçao_idade(inserir_idade)
                confirmar_idade= str(input(f"=> ").strip().lower())

                if confirmar_idade == "1" or confirmar_idade == "2":
                    if confirmar_idade == "2":
                        sleep(1)
                        print(f"=" * 50 + f"\nPrepare-se para Digitar a Idade Novamente.")
                        msg_de_interaçao.msg_carregando()
                    break

                sleep(1)
                print(f"=" * 50 + f"\n\033[31mEssa opção não está disponível.\033[m")
            
            if confirmar_idade == "1":
                return inserir_idade
        
        else:
            if inserir_idade == "":
                while True:
                    msg_nao_inserir_idade()
                    confirmar_sem_idade= str(input(f"=> ").strip().lower())

                    if confirmar_sem_idade == "1" or confirmar_sem_idade == "2":
                        if confirmar_sem_idade == "1":
                            sleep(1)
                            print(f"=" * 50 + f"\nPrepare-se para Digitar a Idade Novamente.")
                            msg_de_interaçao.msg_carregando()
                        break

                    sleep(1)
                    print(f"=" * 50 + f"\n\033[31mEssa opção não está disponível.\033[m")
                    
                if confirmar_sem_idade == "2":
                    inserir_idade= "0 anos"
                    return inserir_idade
                
            else:
                while True:
                    msg_idade_com_erro()
                    opções_de_erro= str(input(f"=> ").strip().lower())

                    if opções_de_erro == "1" or opções_de_erro == "2":
                        if opções_de_erro == "1":
                            sleep(1)
                            print(f"=" * 50 + f"\n\033[31mPrepare-se para Digitar a Idade Novamente.\033[m")
                            msg_de_interaçao.msg_carregando()
                            break

                        elif opções_de_erro == "2":
                            while True:
                                msg_nao_inserir_idade()
                                confirmar_sem_idade= str(input(f"=> ").strip().lower())

                                if confirmar_sem_idade == "1" or confirmar_sem_idade == "2":
                                    if confirmar_sem_idade == "1":
                                        sleep(1)
                                        print(f"=" * 50 + f"\nPrepare-se para Digitar a Idade Novamente.")
                                        msg_de_interaçao.msg_carregando()
                                        break

                                    elif confirmar_sem_idade == "2":
                                        inserir_idade= "0 anos"
                                        return inserir_idade
                                else:
                                    sleep(1)
                                    print(f"=" * 50 + f"\n\033[31mEssa opção não está disponível.\033[m")
                            
                            if confirmar_sem_idade == "1":
                                break

                    else:
                        sleep(1)
                        print(f"=" * 50 + f"\n\033[31mEssa opção não está disponivel.\033[m")
