from projeto import msg_de_interaçao
from .msg_interação_NomeIdade.msg_interação_nome import msg_confirmaçao_nome, msg_nome_com_erro, msg_nao_inserir_nome
from time import sleep

def nome_pessoa():
    '''
    Função "def nome_pessoa()": Verifica se o dado inserido pelo usuário pode ser um nome ou não, apenas permitindo que avance quando digitar um
    valor possível para um nome. Caso o valor possa ser considerado como um nome, a função verificará o dado e o formatá, deixando as primeiras
    letras de cada nome maiscúla, com exceção das primeiras letras das preposições "da", "de", "do", "das" e "dos". Após isso, o usário tera a opção
    de confirmar o nome ou inserir um novo dado.
    > Parâmetros: A função não recebe parâmetros;
    > Retorno: Retorna o nome verificado ou retorna "Desconhecido(a)", caso o usuário opte por não digitar nenhum dado;
    > :param return: nome_completo.
    '''

    while True:
        sleep(1)
        inserir_nome= str(input(f"=" * 50 + f"\nDigite um nome: ").strip().lower())
        nome_conferido= True

        if inserir_nome != "" or inserir_nome == " ":
            for conf in inserir_nome:
                if conf not in "aâãàáäbcçdeêèéëfghiîìíïjklmnoõôòóöpqrstuûúùüvwxyz ":
                    nome_conferido= False
                    break
        else:
            nome_conferido= False

        if nome_conferido:
            nome_completo= ""
            for conf in range(0, len(inserir_nome)):
                if inserir_nome[conf] != " ":
                    if conf == 0 or inserir_nome[conf-1] == " ":
                        if inserir_nome[conf] == "d" and (inserir_nome[conf+2] == " " or (inserir_nome[conf+3] == " " and inserir_nome[conf+2] == "s")):
                            nome_completo= nome_completo + inserir_nome[conf].lower()
                        else:
                            nome_completo= nome_completo + inserir_nome[conf].upper()
                    else:
                        nome_completo= nome_completo + inserir_nome[conf].lower()

                elif inserir_nome[conf-1] != " " and inserir_nome[conf] == " ":
                        nome_completo= nome_completo + inserir_nome[conf]
            
            while True:
                msg_confirmaçao_nome(nome_completo)
                confirmar_nome= str(input(f"=> ").strip().lower())

                if confirmar_nome == "1" or confirmar_nome == "2":
                    if confirmar_nome == "2":
                        sleep(1)
                        print(f"=" * 50 + f"\nPrepare-se para Digitar o Nome Novamente.")
                        msg_de_interaçao.msg_carregando()
                    break
                
                sleep(1)
                print(f"=" * 50 + f"\n\033[31mEssa opção não está disponível.\033[m")

            if confirmar_nome == "1":
                return nome_completo
        
        else:
            if inserir_nome == "":
                while True:
                    msg_nao_inserir_nome()
                    confirmar_sem_nome= str(input(f"=> ").strip().lower())

                    if confirmar_sem_nome == "1" or confirmar_sem_nome == "2":
                        if confirmar_sem_nome == "1":
                            sleep(1)
                            print(f"=" * 50 + f"\nPrepare-se para Digitar o Nome Novamente.")
                            msg_de_interaçao.msg_carregando()
                        break

                    sleep(1)
                    print(f"=" * 50 + f"\n\033[31mEssa opção não está disponível.\033[m")

                if confirmar_sem_nome == "2":
                    nome_completo= "Desconhecido(a)"
                    return nome_completo
                
            else:
                while True:
                    msg_nome_com_erro()
                    opções_de_erro= str(input(f"=> ").strip().lower())

                    if opções_de_erro == "1" or opções_de_erro == "2":
                        if opções_de_erro == "1":
                            sleep(1)
                            print(f"=" * 50 + f"\nPrepare-se para Digitar o Nome Novamente.")
                            msg_de_interaçao.msg_carregando()
                            break

                        elif opções_de_erro == "2":
                            while True:
                                msg_nao_inserir_nome()
                                confirmar_sem_nome= str(input(f"=> ").strip().lower())

                                if confirmar_sem_nome == "1" or confirmar_sem_nome == "2":
                                    if confirmar_sem_nome == "1":
                                        sleep(1)
                                        print(f"=" * 50 + f"\nPrepare-se para Digitar o Nome Novamente.")
                                        msg_de_interaçao.msg_carregando()
                                        break

                                    elif confirmar_sem_nome == "2":
                                        nome_completo= "Desconhecido(a)"
                                        return nome_completo

                                sleep(1)
                                print(f"=" * 50 + f"\n\033[31mEssa opção não está disponível.\033[m")
                            
                            if confirmar_sem_nome == "1":
                                break
                    else:
                        sleep(1)
                        print(f"=" * 50 + f"\n\033[31mEssa opção não está disponível.\033[m")
