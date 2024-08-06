# Importando bibliotecas:

from datetime import datetime
from datetime import date
from tkinter import ttk
from tkinter import *
import emoji
import re
import os

def status_alistamento():

    while True: # Criando Laço de repetição infinito.

        # Inserindo o título do programa na tela:

        titulo = emoji.emojize(('\u2694\uFE0F:') + '  | ' + ('\U0001f530')) + '  ' + 'STATUS DE ALISTAMENTO MILITAR' + '  ' + emoji.emojize(('\U0001f530') + ' | ' + ('\u2694\uFE0F:'))  
        informativo = emoji.emojize('\U0001f6a8') + ' ' + 'ATENÇÃO!! - "ESTE SERVÇO É DESTINADO APENAS PARA CIDADÃOS BRASILEIROS DO SEXO MASCULINO"\nPara verificar sua situação perante as forças armadas brasileiras, insira seu nome e sua data de nascimento:'

        print(titulo)

        print(informativo)
            
        # Solicitando os dados do usuário e efetuando o tratamento dos dados inseridos::

        # Entrada e tratamento de "NOME":
        padrao_nome = re.compile(r'\w+[^0-9]+') # Cria o padrão aceito para a entrada de nome do usuário.
        nome_usuario = input('\nNOME: ').upper() # Solicita ao usuário o nome e converte todos os caracteres digitados para maiúsculo.
        teste_nome = re.fullmatch(padrao_nome, nome_usuario) # Efetua a verificação se o nome digitado pelo usuário corresponde com o padrão criado.

        while teste_nome == None or nome_usuario.isspace() == True: # Laço de repetição que irá continuar enquanto o teste comparativo entre o nome digitado e o padrão não for válido e ou se a entrada digitada pelo usuário for apenas espaços vazios.
            print('\nNome inválido!')
            nome_usuario = input('\nNOME: ').upper() # Solicita ao usuário o nome e converte todos os caracteres digitados para maiúsculo.
            teste_nome = re.fullmatch(padrao_nome, nome_usuario) # Efetua a verificação se o nome digitado pelo usuário corresponde com o padrão criado.

        # Entrada e tratamento de "DATA DE NASCIMENTO":
        padrao_data_nasc = re.compile(r'(0[1-9]{1}|1[0-9]{1}|2[0-9]{1}|3[0-1]{1}|[1-9]{1})[/](0[1-9]{1}|1[0-2]{1}|[1-9]{1})[/](1[0-9]{3}|2[0-9]{3})') # Cria o padrão aceito para entrada de data de nascimento do usuário.
        data_nascimento = input('\nDATA DE NASCIMENTO (00/00/0000): ') # Solicita ao usuário a data de nascimento.
        teste_data_nasc = re.fullmatch(padrao_data_nasc, data_nascimento) # Efetua a verificação se a data de nascimento digitada pelo usuário corresponde com o padrão criado.

        hoje = date.today() # Gera a data atual.
        while teste_data_nasc == None: # Laço de repetição que irá continuar enquanto o teste comparativo entre a data digitada e o padrão não for válido.
            print('\nData inválida!')
            data_nascimento = input('\nDATA DE NASCIMENTO (00/00/0000): ') # Solicita ao usuário a data de nascimento.
            teste_data_nasc = re.fullmatch(padrao_data_nasc, data_nascimento) # Efetua a verificação se a data de nascimento digitada pelo usuário corresponde com o padrão criado.

        data_teste = datetime.strptime(data_nascimento, '%d/%m/%Y').date() # Converte a data inserida pelo usuário, no formato string, para o formato de data passível de ser utilizada em cálculos.
        validacao_data = hoje - data_teste # Obtém a diferença, em dias, entre a data de nascimento digitada pelo usuário e data de hoje. 

        while validacao_data.days < 0: # Laço de repetição que irá continuar enquanto o resultado da diferença entre a data digitada e a data atual for negativo.
            print('\nData inválida!')
            data_nascimento = input('\nDATA DE NASCIMENTO (00/00/0000): ') # Solicita ao usuário a data de nascimento.
            teste_data_nasc = re.fullmatch(padrao_data_nasc, data_nascimento) # Efetua a verificação se a data de nascimento digitada pelo usuário corresponde com o padrão criado.
            data_teste = datetime.strptime(data_nascimento, '%d/%m/%Y').date() # Converte a data inserida pelo usuário, no formato string, para o formato de data passível de ser utilizada em cálculos.
            validacao_data = hoje - data_teste # Obtém a diferença, em dias, entre a data de nascimento digitada pelo usuário e data de hoje.

        # Entrada e tratamento da "SITUAÇÃO DO PAÍS":
        padrao_situacao_pais = re.compile(r'[s,n]{1}|[S,N]{1}') # Cria o padrão aceito para entrada da situação em que o país se encontra (Guerra ou Paz), a ser digitada pelo usuário.
        situacao_atual_pais = input('\nESTAMOS EM GUERRA? ("S" para sim / "N" para não): ').lower() # Solicita ao usuário a a letra correspondente a situação em que o país se encontra e converte o caracter digitado para minúsculo.
        teste_situacao_pais = re.fullmatch(padrao_situacao_pais, situacao_atual_pais) # Efetua a verificação se o caracter digitado pelo usuário corresponde com o padrão criado.

        while teste_situacao_pais == None: # Laço de repetição que irá continuar enquanto o teste comparativo entre o caracter digitado e o padrão não for válido.
            print('\nOpção inválida!')
            situacao_atual_pais = input('\nESTAMOS EM GUERRA? ("S" para sim / "N" para não): ').lower() # Solicita ao usuário a letra correspondente a situação em que o país se encontra e converte o caracter digitado para minúsculo.
            teste_situacao_pais = re.fullmatch(padrao_situacao_pais, situacao_atual_pais) # Efetua a verificação se o caracter digitado pelo usuário corresponde com o padrão criado.

        # Verificação da situação do país:
        guerra = None # Cria a variável guerra e não atribui nada a ela.

        if situacao_atual_pais == 's': # verifica se o caracter armazenado na variável é "s".
            guerra = True # Caso o caracter armazenado na variável seja "s", a variável guerra recebe True.
        else: # verifica se o caracter armazenado na variável é diferente de "s".
            guerra = False # Caso o caracter armazenado na variável não seja "s", a variável guerra recebe False.

        # Verificação de idade do usuário:
        idade = round((validacao_data.days / 365)//1) # Converte a data em dias para anos, obtém a parte inteira do idade e efetua o arredondamento para exibir apenas o número inteiro.
        verifica_idade = None # Cria a variável idade e não atribui nada a ela.

        if idade >= 17: # Verifica se o usuário tem 17 anos ou mais.
            verifica_idade = idade.is_integer() # Verifica se o usuário tem 17 anos completos ou se está prestes a fazer 18 anos, identificando se o número armazenado na variável idade é um número inteiro.

        # Verificação da situação do usuário de acordo com a situação do país:
        condicao = None # Cria a variável condicao e não atribui nada a ela.
        tempo_espera = None # Cria a variável tempo_espera e não atribui nada a ela.


        # Situação no caso do país estar em guerra declarada:
        if guerra == True: # Verifica se o conteúdo da variável guerra é igual a True.
            if idade < 17: # Verifica se a idade é menor que 17.
                condicao = 'NÃO PODERÁ SER CONVOCADO NESTE MOMENTO' # Armazena a frase em formato string na variável condicao.
                previsao_ano = (17 - idade) + hoje.year # Calcula o ano que o usuário irá completar 17 anos.
                mensagem_menor17_G = 'NÃO PODE SE ALISTAR VOLUNTARIAMENTE OU SER CONVOCADO NESTE MOMENTO' # Armazena a frase em formato string na variável mensagem_menor17_G.
                
                print(f'\n{nome_usuario}, você possui {idade} anos e {condicao}!')
                print(f'{mensagem_menor17_G}, aguarde até {previsao_ano} e procure a Junta de Serviço Militar da \
    sua região entre os meses de Janeiro a Junho.\n\n')
            
            else: # Verifica se a idade não é menor que 17.
                condicao = 'PODERÁ SER CONVOCADO A QUALQUER MOMENTO' # Armazena a frase em formato string na variável condicao.
                mensagem_maior_G = 'VOCÊ PODE PROCURAR A JUNTA DE SERVIÇO MILITAR DA SUA REGIÃO DE FORMA VOLUNTÁRIA \
    IMEDIATAMENTE OU AGUARDAR A CONVOCAÇÃO A PARTIR DOS MEIOS DE COMUNICAÇÃO OFICIAIS DAS FORÇAS \
    ARMADAS DO BRASIL' # Armazena a frase em formato string na variável mensagem_maior_G.
                
                print(f'\n{nome_usuario}, você possui {idade} anos e {condicao}!')
                print(f'{mensagem_maior_G}!\n\n')

        # Situação no caso do país não estar em paz (não está em guerra):
        else: # Verifica se o conteúdo da variável guerra é diferente de True.
            if idade < 17: # Verifica se a idade é menor que 17.
                condicao = 'NÃO PODERÁ SE ALISTAR NESTE MOMENTO' # Armazena a frase em formato string na variável condicao.
                previsao_ano_voluntario = (17 - idade) + hoje.year # Calcula o ano que o usuário irá completar 17 anos.
                previsao_ano_obrigatorio = (18 - idade) + hoje.year # Calcula o ano que o usuário irá completar 18 anos.
                mensagem_menor17 = 'NÃO PODE SE ALISTAR VOLUNTARIAMENTE OU SER CONVOCADO NESTE MOMENTO' # Armazena a frase em formato string na variável mensagem_menor17.
                print(f'\n{nome_usuario}, você possui {idade} anos e {condicao}!')
                
                print(f'{mensagem_menor17}, aguarde até {previsao_ano_voluntario} e procure a Junta de Serviço Militar \
    da sua região entre os meses de Janeiro a Junho, de forma voluntária ou aguarde \
    até {previsao_ano_obrigatorio} para se apresentar ao serviço militar obrigatório.\n\n')
            
            elif idade <= 18: # Verifica se a idade é menor ou igual a 18.
                if verifica_idade == True and idade < 18: # Verifica se o conteúdo armazenado na variável verifica_idade é igual a True e se o conteúdo da variável idade é menor que 18.
                    condicao = 'PODERÁ SE ALISTAR VOLUNTARIAMENTE NESTE MOMENTO' # Armazena a frase em formato string na variável condicao.
                    previsao_ano_obrigatorio = (18 - idade) + hoje.year # Calcula o ano que o usuário irá completar 18 anos.
                    print(f'\n{nome_usuario}, você possui {idade} anos e {condicao}!')
                    
                    print(f'Procure a Junta de Serviço Militar da sua região de forma voluntária imediatamente ou \
    aguarde até {previsao_ano_obrigatorio} para se apresentar ao serviço militar obrigatório de Janeiro a Junho.\n\n')
                
                else: # Verifica se o conteúdo armazenado na variável verifica_idade não é igual a True e se o conteúdo da variável idade não é menor que 18.
                    if (idade - 17) * 100 <= 45: # Obtém a parte decimal do número armazenado na variável idade, converte para inteiro e verifica se o número é menor ou igual a 45.
                        condicao = 'PODERÁ SE ALISTAR VOLUNTARIAMENTE NESTE MOMENTO' # Armazena a frase em formato string na variável condicao.
                        previsao_ano_obrigatorio = hoje.year + 1 # Calcula o ano que o usuário irá completar 18 anos.
                        print(f'\n{nome_usuario}, você possui {idade} anos e {condicao}!')
                        
                        print(f'Procure a Junta de Serviço Militar da sua região de forma voluntária imediatamente ou \
    aguarde até {previsao_ano_obrigatorio} para se apresentar ao serviço militar obrigatório de Janeiro a Junho.\n\n')
                    
                    else: # Verifica se o número obtido não é menor ou igual a 45.
                        condicao = 'SE AINDA NÃO SE ALISTOU, ESTÁ EM DÉBITO COM SUA PÁTRIA' # Armazena a frase em formato string na variável condicao.
                        print(f'\n{nome_usuario}, você possui {idade} anos e {condicao}!')
                        
                        print('PROCURE IMEDIATAMENTE A JUNTA DE SERVIÇO MILITAR DA SUA REGIÃO PARA SE APRESENTAR AO \
    SERVIÇO MILITAR OBRIGATÓRIO.')
                        
                        print('\nQuem estiver em débito com o Serviço Militar não poderá:')
                        
                        print('\n- Obter passaporte ou prorrogação de sua validade;')
                        
                        print('- Ingressar como funcionário, empregado ou associado em instituição, empresa ou \
    associação oficial, oficializada ou subvencionada;')
                        
                        print('- Assinar contrato com o Governo Federal, Estadual, dos Territórios ou Municípios;')      
                        
                        print('- Prestar exame ou matricular-se em qualquer estabelecimento de ensino;')
                        
                        print('- Obter carteira profissional, registro de diploma de profissões liberais, matrícula \
    ou inscrição para o exercício de qualquer função e licença de indústria e profissão;')
                        
                        print('- Inscrever-se em concurso para provimento de cargo público;')
                        
                        print('- Exercer, a qualquer título, sem distinção de categoria ou forma de pagamento, qualquer \
    função pública ou cargo público, eletivos ou de nomeação;')
                        
                        print('- E receber qualquer prêmio ou favor do Governo Federal, Estadual, dos Territórios ou \
    Municípios.\n\n')
                                
            elif idade > 18 and idade <= 45: # Verifica se a idade é menor que 18 e menor ou igual a 45.
                condicao = 'SE JÁ ESTIVER COMO RESERVISTA, PODERÁ SE ALISTAR VOLUNTARIAMENTE NESTE MOMENTO OU SER \
    CONVOCADO A QUALQUER MOMENTO EM CASO DE NECESSIDADE DAS FORÇAS ARMADAS OU GUERRA DECLARADA' # Armazena a frase em formato string na variável condicao.
                
                print(f'\n{nome_usuario}, você possui {idade} anos e {condicao}!')
            else:
                condicao = 'JÁ CUMPRIU SEU DEVER COM A PÁTRIA! NÃO PODERÁ SE ALISTAR OU SER CONVOCADO A QUALQUER \
    MOMENTO, COM EXCESSÃO EM CASO DE GUERRA DECLARADA' # Armazena a frase em formato string na variável condicao.
                
                print(f'\n{nome_usuario}, você possui {idade} anos e {condicao}!')

        # Verificação da Opção de saída do programa:
        padrao_saida = re.compile(r'[s,n]{1}|[S,N]{1}') # Cria o padrão aceito para entrada da opção a ser digitada pelo usuário.
        opcao_saida = input('\nDeseja realizar uma nova consulta? ("S" para sim / "N" para não): ').lower() # Solicita ao usuário a letra correspondente a opção e converte o caracter digitado para minúsculo.
        teste_opcao_saida = re.fullmatch(padrao_saida, opcao_saida) # Efetua a verificação se o caracter digitado pelo usuário corresponde com o padrão criado.

        while teste_opcao_saida == None: # Laço de repetição que irá continuar enquanto o teste comparativo entre o caracter digitado e o padrão não for válido.
            print('Opção inválida!')
            opcao_saida = input('\nDeseja realizar uma nova consulta? ("S" para sim / "N" para não): ').lower() # Solicita ao usuário a letra correspondente a opção e converte o caracter digitado para minúsculo.
            teste_opcao_saida = re.fullmatch(padrao_saida, opcao_saida) # Efetua a verificação se o caracter digitado pelo usuário corresponde com o padrão criado.

        if opcao_saida == 'n': # verifica se o caracter armazenado na variável é "n"
            break # Interrompe o laço de repetição infinito e encerra o programa.
            print('\nPrograma encerrado...\n\n') # Informa ao usuário que o programa foi encerrado.
        else: # verifica se o caracter armazenado na variável é diferente de "s".
            os.system('cls') # Efetua a limpeza da tela para reiniciar o programa.
            continue # Reinicia o laço de repetição infinito para reiniciar o progrma




janela_principal = Tk()

janela = ttk.Frame(janela_principal, padding= '3 3 12 12')
janela.grid(column=0, row=0, sticky=(N, S, E, W))
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1)

janela_principal.title(emoji.emojize(('\u2694\uFE0F') + '  | ' + ('\U0001f530')) + '  ' + 'STATUS DE ALISTAMENTO MILITAR' + '  ' + emoji.emojize(('\U0001f530') + ' | ' + ('\u2694\uFE0F')))

texto_alerta = emoji.emojize('\u26A0\uFE0F') + ' ' + 'ATENÇÃO!! - "ESTE SERVÇO É DESTINADO APENAS PARA CIDADÃOS BRASILEIROS DO SEXO MASCULINO"\nPara verificar sua situação perante as forças armadas brasileiras, insira seu nome e sua data de nascimento:'
informativo = Label(janela, text= texto_alerta)
informativo.grid (column=0, row=0, sticky=(W, E))

nome = ttk.Entry(janela, width=35)
nome.grid(column=0, row=2, sticky=W)
etiqueta_nome = Label(janela, text= 'NOME:')
etiqueta_nome.grid(column=0, row=1, sticky=W)

data_nascimento = ttk.Entry(janela, width=10)
data_nascimento.grid(column=0, row=4, sticky=W)
etiqueta_data_nascimento = Label(janela, text= 'DATA NASCIMENTO (DD/MM/AAAA):')
etiqueta_data_nascimento.grid(column=0,row=3, sticky=W)

opcao_gerra = ttk.Entry(janela, width=2)
opcao_gerra.grid(column=0, row=6, sticky=W)
etiqueta_opcao_guerra = Label(janela, text= 'ESTAMOS EM GUERRA? ("S" sim / "N" não):')
etiqueta_opcao_guerra.grid(column=0, row=5, sticky=W)

verificar_status = ttk.Button(janela, text= 'Verificar Status', command= status_alistamento)
verificar_status.grid(column=0, row=5, sticky=E)

reiniciar = ttk.Button(janela, text= 'Reiniciar Programa')
reiniciar.grid(column=0, row=6,sticky=E)

for child in janela.winfo_children():
    child.grid_configure(padx=1, pady=1)

nome.focus()
janela_principal.bind('<Return>', status_alistamento)
janela_principal.bind('<Escape>', )

janela_principal.mainloop()





informativo = emoji.emojize('\u26A0\uFE0F') + ' ' + 'ATENÇÃO!! - "ESTE SERVÇO É DESTINADO APENAS PARA CIDADÃOS BRASILEIROS DO SEXO MASCULINO"\nPara verificar sua situação perante as forças armadas brasileiras, insira seu nome e sua data de nascimento:'
