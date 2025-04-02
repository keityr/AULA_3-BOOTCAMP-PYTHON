#Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham 
# valores positivos para quantidade e preço. Escreva um programa que verifique esses campos e imprima 
# "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

# quantidade = 30

# preco = -20


# if quantidade > 0 and preco > 0:
#     print("Dados Válidos")

# else:
#     print("Dados inválidos")

# Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. 
# Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:


# temperatura = 100

# if temperatura < 18:
#     temp = 'Baixa'

# elif temperatura  >= 18 and temperatura <= 26:
#     temp = 'Normal'

# elif temperatura > 26:
#     temp = 'Alta'

# print(f"A temperatura {temperatura}°C está {temp} ")


# Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. Dado um 
# registro de log em formato de dicionário como log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR',
#  'message': 'Falha na conexão'}, escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level'] == 'ERROR':
#     print(log['message'])

# Exercício 4: Validação de Dados de Entrada

# Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário
# tenha idade entre 18 e 65 anos e tenha fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.


# idade_usuario = 80
# email ="keity@gmail.com"

# if  not 18 <= idade_usuario <= 65:
#     print("Dados de usuário Inválidos!")

# elif "@" not in email and "." not in email:
#     print("Email inválido!") 

# else:
#     print("Dados de usuário válidos!")

# Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas.
# Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário 
# comercial (antes das 9h ou depois das 18h). Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, 
# verifique se ela é suspeita.

# transacao = {'valor': 12000, 'hora': 20}



# if transacao['valor'] >= 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
#     print("Valor incomum")

# else:
#     print("Transação normal")

# Measure some strings:
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))

# texto = "a raposa marrom salta sobre o preguiçoso preguiçoso"
# palavras = texto.split()
# contagem_palavras = {}


# for palavra in palavras:
#     if palavra  in contagem_palavras:
#         contagem_palavras[palavra] += 1
#     else:
#         contagem_palavras[palavra] = 1
# print(contagem_palavras)
# numeros = [10, 20, 30, 40, 50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# print(normalizados)

#(10 - 10) / (50 - 10) = 0 / 40

# numeros = range(1, 11)
# pares = [x for x in numeros if x % 2 == 0]

# print(pares)

# dados = []
# entrada = ""

# while entrada.lower() != "sim":
#     entrada = input("Quais frutas você deseja?")
#     if entrada.lower() != "sim":
#         dados.append(entrada)
# print("Frutas desejada: " ,dados)

# pagina_atual = 1
# paginas_totais = 5  # Simulação, na prática, isso viria da API

# while pagina_atual < paginas_totais:
#     print(f'Processando {pagina_atual} de {paginas_totais}')
#     pagina_atual += 1

# print("Todas as páginas foram processadas.")


# 14. Tentativas de Conexão
# Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.   


# tentativas_maximas = 5
# tentativa = 5

# while tentativa <=  tentativas_maximas:
#     print(f'Tentativa {tentativa} de {tentativas_maximas}')
#     if True:
#         print("Conexão obtida com sucesso!")
#         break
#     tentativa += 1
# else:
#     print("Conexão falhou após o máximo de tentativas")


# 15. Processamento de Dados com Condição de Parada
# Objetivo: Processar itens de uma lista até encontrar um valor específico que indica a parada.

# itens = [1, 2, 3, 4, 5 ,"parar"]
# i = 0

# while i < len(itens):
#     if itens [i] == "parar":
#         print("Parada encontrada")
#         break
#     print(f"Processando item: {itens[i]}")
#     i += 1

#   Peça ao usuário um número e mostre a tabuada desse número de 1 a 10.

# num = input("Insira um número: ")

# for numero in range(1, 11):
#     print(f'{num} x {numero} = {num * numero}')




