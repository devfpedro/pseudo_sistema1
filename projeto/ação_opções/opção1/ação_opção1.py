from .dados_pessoa import idade_pessoa, nome_pessoa
from .msg_interaçao_Primeira_Digitaçao import msg_primeiraDigitaçao_nome
from .msg_interaçao_Primeira_Digitaçao import msg_primeiraDigitação_idade
from projeto import msg_de_interaçao
from time import sleep
import shelve

def adicionar_pessoa():
    '''
    Função "def adicionar_pessoas()": Importará as funções responsáveis por verificar e salvar os dados inseridos pelo usuário. Após o usuário
    digitar e confirmar o nome e a idade de uma pessoa, a função salvará esses dados em um arquivo shelve. Caso os dados inseridos sejam os 
    primeiros, a função criará uma lista vázia no arquivo shelve, evitando possíveis erros ao atribuir os novos dados e atualizar o arquivo.
    > Parâmetros: A função não recebe parâmetros;
    > Retorno: Sem retorno.
    '''

    msg_primeiraDigitaçao_nome.msg_primeiro_nome()
    inserir_nome= nome_pessoa.nome_pessoa()
    msg_primeiraDigitação_idade.msg_primeira_idade()
    inserir_idade= idade_pessoa.idade_pessoa()

    with shelve.open("projeto/ação_opções/opção1/dados_pessoa/guardar_lista_pessoas/lista_pessoas") as lista_pessoas_registradas:
        nova_pessoa= {"nome": inserir_nome, "idade": inserir_idade}
        quant_pessoas_registradas= len(lista_pessoas_registradas)
        if len(lista_pessoas_registradas) == 0:
            lista_pessoas_registradas["pessoas_registradas"]= []
        registrar_pessoa= lista_pessoas_registradas["pessoas_registradas"]
        if len(registrar_pessoa) == 0:
            registrar_pessoa.append({"pessoa_1": nova_pessoa})
        else:
            registrar_pessoa.append({"pessoa_" + (str(len(registrar_pessoa) + 1)): nova_pessoa})
        lista_pessoas_registradas["pessoas_registradas"]= registrar_pessoa
        sleep(1)
        print((f"=" * 50 + f"\n\033[34mNova pessoa registrada com sucesso!\033[m") if len(lista_pessoas_registradas["pessoas_registradas"]) > quant_pessoas_registradas else (f"=" * 50 + f"\nNenhuma pessoa foi adicionada."))
        sleep(1)
        print(f"=" * 50 + f"\nPrepare-se para Voltar ao Menu Principal.")
        msg_de_interaçao.msg_carregando()
