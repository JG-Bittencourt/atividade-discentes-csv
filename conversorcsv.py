import csv

def imprimir (alunos, matricula):
    n = 0
    while n < len(alunos) and alunos[n].matricula != matricula:
        n = n + 1
    
    if n == len(alunos):
        print("Erro! A matrícula informada não se encontra na nossa base de dados.")
    else: 
        print(f"MATRÍCULA: {alunos[n].matricula}\n"
        f"NOME: {alunos[n].nome}\n"
        f"ANO DE INGRESSO: {alunos[n].ano_ingresso}\n"
        f"PERÍODO DE INGRESSO: {alunos[n].periodo_ingresso}\n"
        f"TIPO DE DISCENTE: {alunos[n].tipo_discente}\n"
        f"STATUS: {alunos[n].status_discente}\n"
        f"NÍVEL DE ENSINO: {alunos[n].nivel_ensino}\n"
        f"CURSO: {alunos[n].nome_curso}\n"
        f"MODALIDADE: {alunos[n].modalidade_curso}\n"
        f"UNIDADE: {alunos[n].nome_unidade}\n"
        f"UNIDADE GESTORA: {alunos[n].nome_unidade_gestora}")


from dataclasses import dataclass

@dataclass
class Aluno:
    matricula: int
    nome:str
    ano_ingresso: int
    periodo_ingresso: int
    tipo_discente: str
    status_discente: str
    nivel_ensino: str
    nome_curso: str
    modalidade_curso: str
    nome_unidade: str
    nome_unidade_gestora: str

alunos = []

with open("C:/Users/POSITIVO/projetos/dis-csv-discentes-de-graduacao-de-2025_1.csv", encoding="UTF-8") as arquivocsv:

    if arquivocsv == None:
        print("=============================\nFalha ao carregar o arquivo\n=============================")
    else:
        print("=============================\nArquivo carregado com sucesso\n=============================") 

    leitor = csv.DictReader(arquivocsv,delimiter=",")

    for linha in leitor:
        aluno = Aluno(
            matricula=int(linha["matricula"]),
            nome=linha["nome_discente"],
            ano_ingresso=int(linha["ano_ingresso"]),
            periodo_ingresso=int(linha["periodo_ingresso"]),
            tipo_discente=linha["tipo_discente"],
            status_discente=linha["status_discente"],
            nivel_ensino=linha["nivel_ensino"],
            nome_curso=linha["nome_curso"],
            modalidade_curso=linha["modalidade_educacao"],
            nome_unidade=linha["nome_unidade"],
            nome_unidade_gestora=linha["nome_unidade_gestora"]
        )
        alunos.append(aluno)

matriculadiscente = int(input("Informe a matricula do discente para obtenção dos dados: "))
print("=========================================================================")
imprimir(alunos,matriculadiscente)