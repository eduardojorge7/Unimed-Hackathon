import random
from pymongo import MongoClient

uri = "mongodb+srv://Eduardo_jorge:YOURS_PASSWORD@clusterhospital.kmxto.mongodb.net"
client = MongoClient(uri)

db = client['UNIMED']

#schema

############### ADICIONAR NOVO PACIENTE ###############
novoPaciente = {
    "idPaciente": random.randint(0, 9999),
    "cpfPaciente": 39609001922,
    "nome": 'Eduardo Jorge',
    "sexo": "M",
    "planoUnimed": "Classico",
    "Clinica": [{"idClinica": random.randint(0, 9999),
                 "cnpjClinica": "61.412.110/0001-55",
                 "nomeClinica": "ABC Exames",
                 "endereco": "Rua Jasmim, 810",
                 "Pedidos": [{"idPedidos": random.randint(0, 9999),
                              "cnpjFornecedor": "13.840.709/0001-47",
                              "cpfPaciente": 39609001922,
                              "dataSolicitacao": "25/06/2000",
                              "Medicamentos": [{"idMedicamento": random.randint(0, 9999),
                                                "nomeMedicamento": "Dipirona, 3mg",
                                                "SLA": 10,
                                                "descricao": "10 comprimidos"
                                                }],
                              }],
                 "Fornecedor": [{"idFornecedor": random.randint(0, 9999),
                                 "nomeFornecedor": "XYZ fornecedores",
                                 "cnpjFornecedor": "13.840.709/0001-47"
                                 }],
                 }],
    "Consultas": [{"idConsulta": random.randint(0, 9999),
                   "cnpjClinica": "61.412.110/0001-55",
                   "cpfPaciente": 39609001922,
                   "medicamentoAplicado": True,
                   "dataConsulta": "26/06/2022"}]

}

db.Paciente.insert_one(novoPaciente)

############### INSERIR +1 CLINICA ###############
novaClinica = {
    "idClinica": random.randint(0, 9999),
    "cnpjClinica": "28.425.652/0001-97",
    "nomeClinica": "Clinica Amor Saude",
    "endereco": "Av. Brasil, 2066",
    "Pedidos": [{"idPedidos": random.randint(0, 9999),
                 "cnpjFornecedor": "13.840.709/0001-47",
                 "cpfPaciente": 39609001922,
                 "dataSolicitacao": "22/05/2022",
                 "Medicamentos": [{"idMedicamento": random.randint(0, 9999),
                                   "nomeMedicamento": "Rivotril 5mg",
                                   "SLA": 5,
                                   "descricao": "gotas"
                                   }],
                 }]
    }


db.Paciente.update_one(
   { "idPaciente": 1043 },
   { '$push': { "Clinica": novaClinica } })


############### INSERIR +1 PEDIDO ###############
novoPedido = {
    "idPedidos": random.randint(0, 9999),
     "cnpjFornecedor": "13.840.709/0001-47",
     "cpfPaciente": 39609001922,
     "dataSolicitacao": "22/06/2022",
     "Medicamentos": [{"idMedicamento": random.randint(0, 9999),
                       "nomeMedicamento": "toxina botulinica",
                       "SLA": 5,
                       "descricao": "frasco"
                       }]
    }

db.Paciente.update_one(
   { "idPaciente": 1043 },
   { '$push': { "Pedidos": novoPedido } })


############### INSERIR +1 FORNECEDOR ###############
novoFornecedor = {
    "idFornecedor": random.randint(0, 9999),
    "nomeFornecedor": "XYZ fornecedores",
    "cnpjFornecedor": "13.840.709/0001-47"
}

db.Paciente.update_one(
   { "idPaciente": 1043 },
   { '$push': { "Fornecedor": novoFornecedor } })


############### INSERIR +1 FORNECEDOR ###############
novaConsulta = {
    "idConsulta": random.randint(0, 9999),
    "cnpjClinica": "28.425.652/0001-97",
    "cpfPaciente": 39609001922,
    "medicamentoAplicado": "Toxina botulinica",
    "dataConsulta": "24/06/2022"
}

db.Paciente.update_one(
   { "idPaciente": 1043 },
   { '$push': { "Consultas": novaConsulta } })
