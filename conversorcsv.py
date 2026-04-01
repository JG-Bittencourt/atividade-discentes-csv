import csv
from dataclasses import dataclass

#CRIAÇÃO DA ESTRUTURA ALUNO 
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

#FUNÇÃO PARA UPAR ARQUIVO CSV
def uparquivo():   
    arquivo = input("Informe o caminho do arquivo csv: ")

    try:
        with open(arquivo, encoding="UTF-8") as arquivocsv:
            alunos = []
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
                
            return alunos
    except:
        print("=============================\nFalha ao carregar o arquivo\n=============================")


#FUNÇÃO PARA IMPRESSÃO DOS DADOS, PARÂMETRO DE BUSCA = MATRÍCULA
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

#FUNÇÃO SALVAR COMO TEXTO
def savetxt (alunos):

    try:
        with open ("arqconvert.txt","w", encoding="UTF-8") as arquivotxt:
            for aluno in alunos:
                print(f"MATRÍCULA: {aluno.matricula}\n"
                f"NOME: {aluno.nome}\n"
                f"ANO DE INGRESSO: {aluno.ano_ingresso}\n"
                f"PERÍODO DE INGRESSO: {aluno.periodo_ingresso}\n"
                f"TIPO DE DISCENTE: {aluno.tipo_discente}\n"
                f"STATUS: {aluno.status_discente}\n"
                f"NÍVEL DE ENSINO: {aluno.nivel_ensino}\n"
                f"CURSO: {aluno.nome_curso}\n"
                f"MODALIDADE: {aluno.modalidade_curso}\n"
                f"UNIDADE: {aluno.nome_unidade}\n"
                f"UNIDADE GESTORA: {aluno.nome_unidade_gestora}\n", file = arquivotxt)

        print ("Arquivo txt salvo com sucesso.")

    except:
        print("Erro ao salvar o arquivo.")

def main():

    alunos = None

    while True:
        option = int(input("============================================================\n"
                        "Informe o n° da opção desejada:\n"
                        "1 - Carregar arquivo csv.\n"
                        "2 - Exibir dados de Aluno através da matrícula.\n"
                        "3 - Salvar arquivo como txt.\n"
                        "4 - Sair\n"
                        "============================================================\n"))
        if option == 1:
            alunos = uparquivo()

        elif option == 2:
            if alunos is not None:
                matriculadiscente = int(input("Informe a matricula do discente para obtenção dos dados: "))
                print("=========================================================================")
                imprimir(alunos,matriculadiscente) 
            else:
                print ("Carregue o arquivo primeiro!")
        
        elif option == 3:
            if alunos is not None:
                savetxt(alunos)
            else:
                print ("Carregue o arquivo primeiro!")   

        elif option == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

main()
