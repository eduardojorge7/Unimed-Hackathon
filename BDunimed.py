import random
from pymongo import MongoClient


uri = "mongodb+srv://Eduardo_jorge:YOURS_PASSWORD@clusterhospital.kmxto.mongodb.net"
client = MongoClient(uri)

db = client['UNIMED'] # criacao do bando de dados

#Variaveis paciente
cpfPaciente = input("CPF Paciente....: ")
nome = input("Nome Paciente....: ")
sexo = input("Sexo....: ")
planoUnimed = input("Plano Unimed....:")

#Variaveis clinica
cnpjClinica = input("CNPJ da clinica....: ")
nomeClinica = input("Nome da clinica....: ")
endereco = input("Endereco da clinica....: ")

#Variaveis pedidos
cnpjFornecedor = input("CNPJ do fornecedor....: ")
dataSolicitacao = input("Data da solicitacao....: ")

#Variaveis medicamentos
nomeMedicamento = input("Nome do medicamento....: ")
SLA = input("SLA....: ")
descricao = input("Descricao do medicamento....: ")

#Variaveis fornecedor
nomeFornecedor = input("Nome do fornecedor....: ")

#Variaveis consultas
medicamentoAplicado = True
dataConsulta = input("Data da consulta....: ")


#insercao de toda a estrutura do banco
db.Paciente.insert_many([{"idPaciente": random.randint(0, 9999),          #dados do paciente
                           "cpfPaciente": cpfPaciente,
                           "nome": nome,
                           "sexo": sexo,
                           "planoUnimed": planoUnimed,
                           "Clinica": [{"idClinica": random.randint(0, 9999),   #dados da clinica
                                        "cnpjClinica": cnpjClinica,
                                        "nomeClinica": nomeClinica,
                                        "endereco": endereco,
                                        "Pedidos": [{"idPedidos": random.randint(0, 9999),    #dados dos pedidos
                                                     "cnpjFornecedor": cnpjFornecedor,
                                                     "cpfPaciente": cpfPaciente,
                                                     "dataSolicitacao": dataSolicitacao,
                                                     "Medicamentos": [{"idMedicamento": random.randint(0, 9999),    #dados dos medicamentos
                                                                       "nomeMedicamento": nomeMedicamento,
                                                                       "SLA": SLA,
                                                                       "descricao": descricao
                                                                       }],
                                                     }],
                                        "Fornecedor": [{"idFornecedor": random.randint(0, 9999),    #dados do fornecedor
                                                        "nomeFornecedor": nomeFornecedor,
                                                        "cnpjFornecedor": cnpjFornecedor
                                                        }],
                                        }],
                           "Consultas": [{"idConsulta": random.randint(0, 9999),      #dados das consultas do paciente
                                          "cnpjClinica": cnpjClinica,
                                          "cpfPaciente": cpfPaciente,
                                          "medicamentoAplicado": medicamentoAplicado,
                                          "dataConsulta": dataConsulta}]
                           }])
