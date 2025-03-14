import csv

# Projeto Prático Programação de Computadores | Professor: Jeofton Costa Melo
# Aluno: Gabriel Minga Pontes | RGM: 27881075
# Aluno: João Filipe Pereira Freitas | RGM: 28534000

ARQUIVO_CSV = "historico_escolar.csv"

def salvar_dados(alunos): # vai salvar todos os dados escritos no prompt no .csv
    with open(ARQUIVO_CSV, mode='w', newline='') as arquivo: # abre o arquivo para writing
        escritor = csv.writer(arquivo)
        escritor.writerow(["RGM", "Nome", "P. Nota", "S. Nota", "T. Nota", "Média", "Status"]) # cabeçalho
        escritor.writerows(alunos) # escreve com os dados dos alunos

def carregar_dados(): 
    try:
        with open(ARQUIVO_CSV, mode='r') as arquivo: # abre o arquivo CSV no modo de leitura reading
            leitor = csv.reader(arquivo) # cria um leitor CSV para ler o arquivo
            next(leitor) 
            return [linha for linha in leitor] # retorna todas as linhas do arquivo como uma lista de listas
    except FileNotFoundError: # se o arquivo não for encontrado, retorna uma lista vazia
        return []

def calcular_media(n1, n2, n3):
    media = round((n1 + n2 + n3) / 3, 2) # round 2 aredonda para 2 casas decimais
    status = "Aprovado" if media >= 6 else "Reprovado"
    return media, status

def cadastrar_aluno():
    rgm = input("RGM: ")
    nome = input("Nome: ")
    notas = [float(input(f"Nota {i+1}: ")) for i in range(3)] # loop para as 3 notas do aluno
    media, status = calcular_media(*notas)
    alunos.append([rgm, nome, *notas, media, status]) # adiciona as infos à lista de alunos
    salvar_dados(alunos)
    print("\nAluno cadastrado com sucesso!\n")

def listar_alunos(): # vai listar os alunos que foram ou não foram cadastrados, e mostrar seu histórico
    if not alunos: # se não houver nenhum, retorna vazio
        print("Nenhum aluno cadastrado!\n")
        return
    
    print("\nLista de Alunos:")
    print("RGM | Nome | Nota 1 | Nota 2 | Nota 3 | Média | Status") # cabeçalho
    for aluno in alunos: # vai rodar toda a lista de alunos
        print(" | ".join(map(str, aluno))) # exibe as infos
    print()

alunos = carregar_dados()
while True:
    print("1 - Cadastrar Aluno")
    print("2 - Listar Alunos")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        print("\nSaindo...\n")
        break
    else:
        print("\nOpção inválida!\n")
