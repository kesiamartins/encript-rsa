from random import choice, randint, sample, randrange
from math import pi, sqrt as r2
from datetime import datetime
from sys import exit
import os
import shutil
from getpass import getuser, getpass
from platform import system
import json
import numpy as np
# import jsonpickle as Njson

ascii_table = {
    "32":" ",
    "33":"!",
    "34":'"',
    "35":"#",
    "36":"$",
    "37":"%",
    "38":"&",
    "39":"'",
    "40":"(",
    "41":")",
    "42":"*",
    "43":"+",
    "44":",",
    "45":"-",
    "46":".",
    "47":"/",
    "48":"0",
    "49":"1",
    "50":"2",
    "51":"3",
    "52":"4",
    "53":"5",
    "54":"6",
    "55":"7",
    "56":"8",
    "57":"9",
    "58":":",
    "59":";",
    "60":"<",
    "61":"=",
    "62":">",
    "63":"?",
    "64":"@",
    "65":"A",
    "66":"B",
    "67":"C",
    "68":"D", 
    "69":"E",
    "70":"F",
    "71":"G",
    "72":"H",
    "73":"I",
    "74":"J",
    "75":"K",
    "76":"L",
    "77":"M",
    "78":"N",
    "79":"O",
    "80":"P",
    "81":"Q",
    "82":"R",
    "83":"S",
    "84":"T",
    "85":"U",
    "86":"V",
    "87":"W",
    "88":"X",
    "89":"Y",
    "90":"Z",
    "91":"[",
    "92":"\\",
    "93":"]",
    "94":"^",
    "95":"_",
    "96":"`",
    "97":"a",
    "98":"b",
    "99":"c",
    "100":"d",
    "101":"e",
    "102":"f",
    "103":"g",
    "104":"h",
    "105":"i",
    "106":"j",
    "107":"k",
    "108":"l",
    "109":"m",
    "110":"n",
    "111":"o",
    "112":"p",
    "113":"q",
    "114":"r",
    "115":"s",
    "116":"t",
    "117":"u",
    "118":"v",
    "119":"w",
    "120":"x",
    "121":"y",
    "122":"z",
    "123":"{",
    "124":"|",
    "125":"}",
    "126":"~",
    # "127":"00",
    "128":"Ç",
    "129":"ü",
    "130":"é",
    "131":"â",
    "132":"ä",
    "133":"à",
    "134":"å",
    "135":"ç",
    "136":"ê",
    "137":"ë",
    "138":"è",
    "139":"ï",
    "140":"î",
    "141":"ì",
    "142":"Ä",
    "143":"Å",
    "144":"É",
    "145":"æ",
    "146":"Æ",
    "147":"ô",
    "148":"ö",
    "149":"ò",
    "150":"û",
    "151":"ù",
    "152":"ÿ",
    "153":"Ö",
    "154":"Ü",
    "155":"ø",
    "156":"£",
    "157":"Ø",
    "158":"×",
    "159":"ƒ",
    "160":"á",
    "161":"í",
    "162":"ó",
    "163":"ú",
    "164":"ñ",
    "165":"Ñ",
    "166":"ª",
    "167":"º",
    "168":"¿",
    "169":"®",
    "170":"¬",
    "171":"½",
    "172":"¼",
    "173":"¡",
    "174":"«",
    "175":"»",
    "176":"░",
    "177":"▒",
    "178":"▓",
    "179":"│",
    "180":"┤",
    "181":"Á",
    "182":"Â",
    "183":"À",
    "184":"©",
    "185":"╣",
    "186":"║",
    "187":"╗",
    "188":"╝",
    "189":"¢",
    "190":"¥",
    "191":"┐",
    "192":"└",
    "193":"┴",
    "194":"┬",
    "195":"├",
    "196":"─",
    "197":"┼",
    "198":"ã",
    "199":"Ã",
    "200":"╚",
    "201":"╔",
    "202":"╩",
    "203":"╦",
    "204":"╠",
    "205":"═",
    "206":"╬",
    "207":"¤",
    "208":"ð",
    "209":"Ð",
    "210":"Ê",
    "211":"Ë",
    "212":"È",
    "213":"ı",
    "214":"Í",
    "215":"Î",
    "216":"Ï",
    "217":"┘",
    "218":"┌",
    "219":"█",
    "220":"▄",
    "221":"¦",
    "222":"Ì",
    "223":"Ó",
    "224":"ß",
    "225":"Ô",
    "226":"Ò",
    "227":"õ",
    "228":"Õ",
    "229":"µ",
    "230":"þ",
    "231":"Þ",
    "232":"Ú",
    "233":"Û",
    "234":"Ù",
    "235":"Ù",
    "236":"ý",
    "237":"Ý",
    "238":"¯",
    "239":"´",
    # "240":" ",
    "241":"±",
    "242":"‗",
    "243":"¾",
    "244":"¶",
    "245":"§",
    "246":"÷",
    "247":"¸",
    "248":"°",
    "249":"¨",
    "250":"·",
    "251":"¹",
    "252":"³",
    "253":"²",
    "254":"■"
    # "255":" "
}

# Achar os números primos:
def primos():
    primos = []
    for x in range(10, 300):
        cont = 0
        for y in range(1, x+1):
            if x % y == 0:
                cont+=1
        if cont <= 2:
            primos.append(x)
    return primos

# Ler o banco de dados:
def checkDB():

    # Nome do banco:
    db_File = "users.txt"

    # Pega o path atual:
    origin_Path = os.getcwd()

    # Verifica se existe um diretório; Se não é criado:
    if ( not os.path.isdir('banco') ):
        os.mkdir('banco')

    # Entra no diretório do banco:
    os.chdir('banco')

    # Verifica se existe o arquivo do banco; Se não é criado:
    if ( not os.path.isfile(db_File) ):
        f = open(db_File, mode='w', encoding="utf8")
        f.close()
    
    # Lemos o arquivo do banco:
    db = open(db_File, mode='r', encoding="utf8")
    data = db.read()
    db.close()

    # Voltamos para o path original:
    os.chdir(origin_Path)

    # Retornamos os dados:
    return data

# Achar um usuário do banco:
def listDB(field):
    data_JSON = checkDB()
    data_DICT = json.loads(data_JSON)

    r = []

    for index, fields in data_DICT.items():
        for attr, value in fields.items():
            if ( attr == field ):
                r.append([field, value])

    return r

# Listar os membros para mandar mensagem:
def listMembers(_user):

    # Pegamos os dados do arquivo do banco:
    data_JSON = checkDB()

    # Transformamos o JSON do banco em DICT:
    data_DICT = json.loads(data_JSON)

    # Criação de variáveis:
        # list_members -> DICT que contém: { 'ID' : 'NOME' };
        # members      -> DICT que contém todas as chaves;
    list_members = {}
    members = {}
    
    # Pegamos o ID 
    id_user = int
    for index, fields in _user.items():
        id_user = index

    # Printamos a lista de usuários cadastrados no banco, removend o própio usuário logado:
    cont = 1
    turn = False
    for index, fields in data_DICT.items():
        for attr, value in fields.items():
            if ( attr == "name" ):
                if ( index != id_user ):
                    print(f"-----> {cont} : {value}")
                    list_members[str(cont)] = value
                    members[str(index)] = fields
                else :
                    if ( id_user == "1" ):
                        cont = 0
                    else:
                        turn = True
        if ( turn == True ):
            turn = False
        else: 
            cont += 1
    print(f"-----> {len(data_DICT)} : Apenas para mim")

    # Retorna as variáveis:
    return list_members, members

# Verifica se é membro:
def isMember():
    print('Bem vindo ao programa\n')

    print('Já é membro ?\n--> 1 : Sim\n--> 2 : Não\n--> 3 : Sair\n')
    member = input('--> ')

    # Menu:
    looping = 0
    while ( looping == 0 ):
        if ( member == '1'):
            looping = 1
            res = login()
            break
        elif ( member == '2' ):
            looping = 1
            res = register()
            break
        elif ( member == '3' ):
            clear()
            print('\nGoodbye *-*')
            exit()
        clear()
        print('Bem vindo ao programa\n')
        print('Já é membro ?\n--> 1 : Sim\n--> 2 : Não\n--> 3 : Sair\n')
        member = input('--> ')

    # Retorna a resposta da opção escolhida:
        # Se for um DICT ou um INT;
    return res

# Menu interno do programa:
def opening(user):
    clear()
    
    # Printa o nome do usuário:
    for index_user, attr_user in user.items():
        print(f"Bem Vindo: {attr_user['name']}")

    print('*** O que deseja fazer? ***\n')
    print('-----> 1 - Ler Mensagem:')
    print('-----> 2 - Escrever Mensagem:')
    print('-----> 3 - Créditos:')
    print('-----> 4 - Logoff:')
    print('-----> Qualquer tecla para sair...\n')
    
    response = input("--------> ")

    # Escolha do usuário, passando como parâmetro os dados de quem fez login:
    if ( response == '1' ):
        return read(user)
    elif ( response == '2' ):
        return write(user)
    elif ( response == '3' ):
        return credit(user)
    elif ( response == '4' ):
        clear()
        return main()
    else:
        clear()
        print('\nGoodbye *-*')
        exit()

# Tela de login:
def login():
    clear()
    print('*** LOGIN ***\n')

    print("Digite seu login:")
    name = input("--------> ")
    print("Digite sua senha:")
    passw = input("--------> ")

    # Variáveis que utilizaremos neste escopo:
        # guest -> DICT com os dados de quem fará o login;
        # defined -> Bool para verificação dos dados em relação ao banco;
    guest = {}
    defined = False 

    # Acessamos o banco:
    data_JSON = checkDB()
    
    # Se não existir dados no banco, retornamos para o menu principal;
    if ( len(data_JSON) == 0 ):
        return 0

    # Senão, convertemos o dado do banco que está em JSON, para DICT:
    data_DICT = json.loads(data_JSON)

    # Check dos dados inserios com o banco de dados:
    for i, val in data_DICT.items():
        # Se o login e senha forem correspondente aos dados do banco:
            # defined = True
        if ( val["name"] == name and val["password"] == passw ):
            guest[i] = val
            defined = True

    # De acordo com o Bool criado:
        # Se os dados inseridos não estiverem no banco corretamente:
            # É retornado um INT;
    if ( defined == False ):
        return 0
    # Se os dados inseridos forem compatíveis com o banco:
        # É retornado um DICT;
    else:
        return guest

# Tela de registro:
def register():
    clear()

    # Pegamos o Path atual:
    origin_Path = os.getcwd()

    print('*** REGISTER ***\n')

    print("Você quer fazer um registro?\n\n--> 1 : Sim\n--> 2 : Voltar ao Menu\n--> Qualquer Tecla para sair\n")
    q = input("--------> ")

    # Menu de Registro:
    # Se o input for igual a '1'
    if ( q == "1" ):
        clear()

        # Um banco de números primos, gerado através da função:
        privateKeys = np.array([11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293])
        
        print('*** REGISTER ***\n')
        print("Digite seu login: ")
        name = input("--------> ")

        # Importamos o banco de dados:
        data_JSON = checkDB()

        # Se contém algum dado do banco:
        if ( len(data_JSON) > 0 ):

            # Transforma o JSON em DICT:
            data_DICT = json.loads(data_JSON)
            
            # Verificação se existe algum nome igual ao do banco:
            checkName = False
            while ( checkName == False ):
                checkName = True
                # Laço FOR para acessar o ATTR do DICT chamado 'name':
                # Se o nome digitado pelo usuário for igual ao do banco:
                    # Validação feita se o nome for igual independente do tipo de letra (UPPER ou LOWER);
                    # Continuamos no laço WHILE;
                for i, field in data_DICT.items():
                    for j, val in field.items():

                        _thisName = name
                        _nameUpper = _thisName.upper()
                        _nameLower = _thisName.lower()
                        _thisNameDB = val
                        _nameDBUpper = _thisNameDB.upper()
                        _nameDBLower = _thisNameDB.lower()

                        if ( name == val or
                            _nameUpper == _nameDBUpper or
                            _nameLower == _nameDBLower ):
                            checkName = False
                if ( checkName == True ):
                    break
                clear()
                print('*** REGISTER ***\n')
                print("Digite um login válido.")
                name = input("Name --> ")

        # Se não existir um nome igual ao do banco, passamos para as próximas etapas:

        print("\nDigite uma senha: ")
        passw = input("--------> ")
        
        # Se existe algum dado guardado no banco:
            # Se existir, pegamos o tamanho dos dados e somamos + 1, para gerar o ID automático;
        if ( len(data_JSON) > 0 ):
            user_Id = len(data_DICT) + 1
        # Se não existir, criamos um DICT e definimos o primeiro ID que será inserido do banco como 1;
        else :
            data_DICT = {}
            user_Id = 1

        # Pegamos os números primos aleatóriamente:
        # Primeira chave privada:
        privateKeyA = choice(privateKeys)

        # Segunda chave privada:
        privateKeyB = choice(privateKeys)
        # Enquanto o KeyB for igual ao KeyA, pegamos aleatóriamente outro número para KeyB
        while ( privateKeyA == privateKeyB ):
            privateKeyB = choice(privateKeys)

        # Geramos a primeira chave pública:
        publicKeyAB = privateKeyA * privateKeyB

        # Geramos o número Totiente / Phi de Euler de publicKeyAB:
        fiAB = (privateKeyA - 1) * (privateKeyB - 1)

        # Chave pública E:
            # Regra para achar o número: 1 > E < fiAB;
            # O número E tem que ser Coprimo de fiAB, ou seja, o MDC de X e fiAB precisa ser APENAS 1;
        # Variável que começará a achar o número E:
        increm = 2
        # Pegamos o resto do MDC entre 2 e fiAB:
        rMDC = searchNumE(increm, fiAB)
        # Enquanto o resto do MDC for maior que 1 ( Utilizaremos esse WHILE para achar um número COPRIMO de fiAB ):
        while ( rMDC > 1 ):
            # Incremento: Antes era 2. Se entramos nesse WHILE é pq é maior que 1; Então incrementamos:
            increm += 1
            rMDC = searchNumE(increm, fiAB)

        # Quando o resto do MDC de increm e fiAB for igual 1, achamos o nossa outra chave pública E com increm:
        publicKeyE = increm

        # Geramos a chave inversa:
        for x in range(fiAB):
            if ( (x*publicKeyE)%fiAB == 1 ):
                privateInverse = x

        # Criamos um DICT de todos os dados gerados:
        data_DICT[str(user_Id)] = {"name":name, "password":passw, "privateKeyA":str(privateKeyA), "privateKeyB":str(privateKeyB), "publicKeyAB":str(publicKeyAB), "fiAB":str(fiAB), "publicKeyE":str(publicKeyE), "privateInverse":str(privateInverse)}

        # Entramos na pasta do banco e adicionamos os dados:
        os.chdir('banco')
        db = open('users.txt', 'w')
        data_JSON = json.dumps(data_DICT, ensure_ascii=False, indent=4, separators=(',', ': '))
        db.write(data_JSON)
        db.close()

        # Voltamos para a pasta do executável:
        os.chdir(origin_Path)

        # Retornamos o DICT que contém o ID e todos os valores:
        for _i_db, _attr_db in data_DICT.items():
            if ( _i_db == str(user_Id) ):
                return {_i_db : _attr_db }

    # Se o input for igual a '2'
    elif ( q == "2" ):
        clear()
        main()

    # Encerramos o programa:
    else:
        print('Programa Encerrado!')
        exit()

# Função MDC (Máximo Divisor Comum):
def searchNumE(increment, fiAB):
    r = increment % fiAB
    if ( r==0 ):
        return r
    else:
        while ( r != 0 ):
            increment = fiAB
            fiAB = r
            r = increment % fiAB
        return fiAB

# Função para encripitar:
def encripty(decimal, publicKeyE, publicKeyAB):
    decimal = int(decimal)
    publicKeyE = int(publicKeyE)
    publicKeyAB = int(publicKeyAB)

    result = ((decimal**publicKeyE) % publicKeyAB)
    return str(result)

# Função para decripitar:
def decripty(encripty, privateInverse, publicKeyAB):
    encripty = int(encripty)
    privateInverse = int(privateInverse)
    publicKeyAB = int(publicKeyAB)

    result = ((encripty**privateInverse) % publicKeyAB)
    return str(result)

# Tela de Créditos:
def credit(user):
    clear()

    # Printa o nome do usuário:
    for index_user, attr_user in user.items():
        print(f"Bem Vindo: {attr_user['name']}")

    print('*** CRÉDITOS ***\n')
    grupo = [
        ["Gustavo Pereira do Amor Divino", "N508612"],
        ["Ian Cozachevici de Jesus", "N503530"],
        ["Jennifer Satirio Lima Santos", "N51608-9"]
    ]
    for alunos in grupo:
        for order, aluno in enumerate(alunos):
            if ( order == 0 ):
                print(f"==> Nome: {aluno}")
            elif ( order == 1 ):
                print(f"==> R.A: {aluno}")
        print("<---------------------->")
    
    input('-----> Digite algo para continuar... ')

    clear()
    # Printa o nome do usuário:
    for index_user, attr_user in user.items():
        print(f"Bem Vindo: {attr_user['name']}")

    print('*** O que deseja fazer? ***\n')
    print('-----> 1 - Voltar ao Menu de Opções:')
    print('-----> 2 - Logoff:')
    print('-----> Qualquer tecla para sair...\n')

    response = input("--------> ")

    # Menu:
    if ( response == '1' ):
        return opening(user)
    elif ( response == '2' ):
        clear()
        return main()
    else:
        clear()
        print('\nGoodbye *-*')
        exit()

# Ler mensagens:
def read(_user):
    
    # Guardo os dados do usuário logado no dict:
    this_user = {}
    for id_user, fields in _user.items():
        this_user = fields

    # Path do executável:
    origin_Path = os.getcwd()

    # Check da pasta mensagens;
        # Se não existir, criamos.
    if ( not os.path.isdir('msgs') ):
        os.mkdir('msgs')

    # Entrando na pasta mensagens:
    os.chdir('msgs')

    # Path da pasta mensagens:
    msg_Path = os.getcwd()

    # Se não existir a pasta do usuários de mensagens:
    if ( not os.path.isdir(this_user['name']) ):
        # Menu:
        clear()
        print('*** READ ***\n')
        print('Não há mensagens para você...\n')
        print('*** O que deseja fazer? ***\n')
        input('Digite algo para voltar ao menu de opções: ')

        # Voltamos para o path do executável:
        os.chdir(origin_Path)
        opening(_user)
    
    # Entrando na pasta mensagens do usuário:
    os.chdir(this_user['name'])

    # Path da pasta do Usuário de mensagens:
    user_path = os.getcwd()

    # Check da mensagem selecionada:
    iteration = False
    while ( iteration == False ):
        clear()
        print('*** READ ***\n')
        print("--------> Lista de arquivos:\n")

        # Variável que iremos adicionar o nome dos arquivos:
        files_dict = {}

        # Listamos os arquivos e adicionamos no DICT:
        for index, files in enumerate(os.listdir('.')):
            files_dict[index+1] = files
            print(f"--> {index+1} : {files}")

        print("\nDigite o arquivo desejado: ")
        # Variável do arquivo selecionado;
        file = input("--------> ")

        # Pequena validação dos espaços em branco:
        if ( file == '' or file == ' '):
            file = 0
        file = int(file)

        # Verificação do número digitado:
        for i in range(1, len(os.listdir('.'))+1):
            if ( file == i ):
                iteration = True
                break
        
    
    # Verificamos no DICT criado dos arquivos:
        # Se o número digitado pra ler for igual ao DICT criado dos arquivos:
            # Pegamos o nome completo do arquivo e guardamos na variável f_name;
    for index, files in files_dict.items():
        if ( index == file ) : 
            f_name = files

    # Variáveis para ler a
    encript = []
    decript = []
    return_ascii = []

    # Lendo o arquivo com o nome desejado:
    f_read = open(f_name, mode="r", encoding="utf8")
    for x in f_read.readlines():
        # Retirando as quebras de linhas:
        r = x.rstrip('\n')
        # Retirando os espaços de #
        r = x.split('#')
        # Adicionando no array:
        encript.append(r)
    f_read.close()

    # Decripita a Mensagem:
    for frase in encript:
        frase_decript_To_Me = []
        # Chamada da função, passando como parâmetro ( NºdaLetra, ChaveInversa, ChavePublicaAB ):
        for letter in frase:
            to_me = decripty(letter, this_user['privateInverse'], this_user['publicKeyAB'])
            # Passo o resultado para a lista criada:
            frase_decript_To_Me.append(to_me)
        # Passo o vetor do valor para outra lista:
        decript.append(frase_decript_To_Me)

    # Converte os valores ASCII para Caracteres:
    for value in decript:
        ascii_by_letter_To_Me = []
        for uni_value in value:
            for decimal, char in ascii_table.items():
                # Se o valor decripitado for igual ao decimal do banco ASCII, adicionamos em uma lista
                if ( uni_value == decimal ):
                    ascii_by_letter_To_Me.append(char)
        # Quando a frase estiver toda convertida, tratamos o vetor para adicionar um única frase em um índice da lista
        return_ascii.append(''.join(ascii_by_letter_To_Me))


    # Resultado da mensagem:
    retorno = False
    while ( retorno == False ):
        clear()

        # Print da mensagem decripitada: 
        print('\n-------> MESSAGE: <-------')
        for response in return_ascii:
            print(response)
        print('\n-------> END: MESSAGE <-------')

        # Menu:
        print('\n*** O que deseja fazer? ***\n')
        print('-----> 1 - Ler mensagens:')
        print('-----> 2 - Voltar a menu de opções:')
        choice = input("--> ")
        
        if ( choice == '1' ):
            retorno = True
            os.chdir(origin_Path)
            read(_user)
            break
        elif ( choice == '2' ):
            retorno = True
            os.chdir(origin_Path)
            opening(_user)
            break
    
# Escrever mensagens:
def write(_user):

    # Só podemos escrever algum arquivos se tivemos PELO MENOS UM dado no banco:

    # Variáveis para pegar a data e horário antes de escrever a mensagem:
    now = datetime.now()
    year = now.strftime('%Y')
    month = now.strftime('%B')
    day = now.strftime('%d')
    hour = now.strftime('%H')
    minute = now.strftime('%M')
    second = now.strftime('%S')
    dateToday = '-'.join([hour, minute, second, year, month, day])

    # Conexão com o banco:
    data_JSON = checkDB()

    # Convertendo o JSON em DICT:
    data_DICT = json.loads(data_JSON)

    # Path do executável:
    origin_Path = os.getcwd()
    
    # Se não existir o diretórito msgs, criamos:
    if ( not os.path.isdir('msgs') ):
        os.mkdir('msgs')
    
    # Pegando os campos do usuário logado e criação da variável Sketch (rascunho):
    sketch = False
    this_user = {}
    for id_user, fields in _user.items():
        this_user = fields

    # Validação do número digitado:
    iteration = False
    while ( iteration == False ):
        clear()
        print('*** WRITE ***\n')
        print("--------> Lista de usuários:\n")

        # Listando os usuários disponíveis no banco para mandar a mensagem, passando como parâmetro o usuário logado:
        result_members = listMembers(_user)
        # Guardando a lista de usuários:
        list_members = result_members[0]
        # Guardando as chaves dos respectivos usuários:
        members = result_members[1]

        print("\nDigite o usuário: ")
        who = input("--------> ")

        # Pequena validação dos espaços em branco:
        if ( who == '' or who == ' '):
            who = 0
        who = int(who)

        # Verificando se o número digitado consta na lista de membros, tirando o número zero e adicionando o próprio usuários -> len(list_members)+2
        for i in range(1, len(list_members)+2):
            if ( who == i ):
                iteration = True
                break
    
    # Validando se o usuário escolheu ele mesmo:
    if ( len(list_members)+1 == who ):
        for id_user, fields in _user.items():
            sketch = True
            who = fields
    # Validando se foi outra pessoa:
    else :
        # Verificação do nome em relação ao numero da lista:
        for choose, fields in list_members.items():
            if ( who == int(choose) ):
                who = fields
        # Verificação do campo das chaves em relação ao nome:
        for user_id, fields in members.items():
            if ( fields["name"] == who ):
                who = fields
    
    # Entrando na pasta mensagens:
    os.chdir('msgs')
    
    # Path das Mensagens:
    path_msgs = os.getcwd()
    
    
    # Criação da pasta do usuário, se ainda não estiver criado:
    if ( not os.path.isdir(f"{this_user['name']}") ):
        os.mkdir(f"{this_user['name']}")
    # Criação da pasta do destinatário e validando se foi apenas pra ele mesmo:
        # Se ele escolheu ele mesmo, a pasta não é criada. Se for diferente dele, criaremos a pasta desta pessoa, se ainda não estiver criada;
    if ( not os.path.isdir(f"{who['name']}") and sketch == False ):
        os.mkdir(f"{who['name']}")

    # Entrando na pasta do usuário:
    os.chdir(f"{this_user['name']}")
    # Path da pasta do usuário:
    path_user = os.getcwd()

    # Retornando ao path das Mensagens:
    os.chdir(path_msgs)

    # Entrando e pegando o path da pasta do destinátario, lembrando que só fará isto se for para uma pessoa do banco, diferente dele mesmo:
    if ( sketch == False ):
        os.chdir(f"{who['name']}")
        path_who = os.getcwd()

    # Retornando ao path das Mensagens:
    os.chdir(path_msgs)

    # Preparação para escrever a mensagem:
    clear()
    # Variável de saída do texto:
    out = "out"
    # Variável do texto:
    txt = []
    
    # Laço WHILE para escrever a mensagem:
    print('*** Escreva sua mensagem ***\n')
    print("-----> Para encerrar sua mensagem, na próxima linha digite: 'out' \n")
    loop = 0
    while ( loop == 0):
        msg = input('--> ')
        if (out in msg):
            loop = 1
            break
        txt.append(msg)

    # Variáveis para encripitar:
    encript_To_Who = []
    encript_To_Me = []

    # Converte o texto digitado em ASCII e Encripita:
    for frase in txt[:]:
        frase_encripty_To_Who = []
        frase_encripty_To_Me = []
        for letter in frase:
            for decimal, char in ascii_table.items():
                if ( letter == char ):
                    # Função encripty;
                    to_who = encripty(decimal, who['publicKeyE'], who['publicKeyAB'])
                    to_me = encripty(decimal, this_user['publicKeyE'], this_user['publicKeyAB'])
                    frase_encripty_To_Who.append(to_who)
                    frase_encripty_To_Me.append(to_me)
        encript_To_Who.append(frase_encripty_To_Who)
        encript_To_Me.append(frase_encripty_To_Me)

    
    # Ajustando para gravar a mensagem:
        # Aqui criamos as novas variáveis, antes de gravar no arquivo;
        # Cada letra será separado por '#'
        # Cada frase, está em sua respectiva ordem:
    encript_To_Who_New = []
    encript_To_Me_New = []
    for x in encript_To_Who:
        r = "#".join(x)
        encript_To_Who_New.append(r)
    for y in encript_To_Me:
        r = "#".join(y)
        encript_To_Me_New.append(r)
    
    # Nome do arquivo será a data e hora do momento:
    name_file_user = dateToday+".txt"
    
    # Criando o arquivos:
    f_user = open(name_file_user, mode="w", encoding="utf8")
    for frase in encript_To_Me_New:
        f_user.write(frase)
        f_user.write('\n')
    f_user.close()
    # Movemos o arquivo para a pasta do usuário:
    shutil.copy2(name_file_user, path_user)
    # Removendo o arquivo no diretório msgs:
    os.remove(name_file_user)

    # Se não for rascunho, fazemos o mesmo procedimento:
    if ( sketch == False ):
        # Criando o arquivos:
        f_user = open(name_file_user, mode="w", encoding="utf8")
        for frase in encript_To_Who_New:
            f_user.write(frase)
            f_user.write('\n')
        f_user.close()
        # Movemos o arquivo para a pasta do usuário:
        shutil.copy2(name_file_user, path_who)
        # Removendo o arquivo no diretório msgs:
        os.remove(name_file_user)

    # Menu
    # Verificando o que devemos fazer após a operação:
    retorno = False
    while ( retorno == False ):
        clear()
        print('*** O que deseja fazer? ***\n')
        print('-----> 1 - Enviar novamente uma mensagem:')
        print('-----> 2 - Voltar a menu de opções:')
        choice = input("--> ")
        
        if ( choice == '1' ):
            retorno = True
            os.chdir(origin_Path)
            write(_user)
            break
        elif ( choice == '2' ):
            retorno = True
            os.chdir(origin_Path)
            opening(_user)
            break
        
# Função para limpar a tela:
def clear():
    return os.system('cls')


# Início do programa:
def main():

    # Verifica se é membro:
    res = isMember()
    # Verifica se é um DICT:
        # Se for, chama a função do menu interno, com os dados de quem fez login:
    if ( isinstance(res, dict) ):
        opening(res)
    # Se for um INT:
        # Retorna pra função principal, main();
    elif ( isinstance(res, int) ):
        clear()
        main()
            
    return 0
    exit()

# Chamada do programa:
main()