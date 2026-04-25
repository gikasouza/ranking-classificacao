import csv
from datetime import datetime

candidatos = []

meu_nome = "Giovanna"
minha_nota = 62.5
meu_portugues = 8
minha_matematica = 6
meus_especificos = 11
minha_data = "29/06/2006"  # ⚠️ CONFIRMA SE É ESSA MESMO

with open("dados.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        candidatos.append({
            "nome": linha["nome"],
            "nota": float(linha["nota"]),
            "portugues": int(linha["portugues"]),
            "matematica": int(linha["matematica"]),
            "especificos": int(linha["especificos"]),
            "data": linha["data"]
        })

# adicionar você
candidatos.append({
    "nome": meu_nome,
    "nota": minha_nota,
    "portugues": meu_portugues,
    "matematica": minha_matematica,
    "especificos": meus_especificos,
    "data": minha_data
})

# ordenar (sem idade ainda)
candidatos.sort(key=lambda x: (
    -x["nota"],
    -x["especificos"],
    -x["portugues"],
    -x["matematica"]
))

# encontrar posição inicial
posicao = 0

for i, c in enumerate(candidatos, start=1):
    if c["nome"] == meu_nome:
        posicao = i
        print("Sua colocação (sem idade):", i)
        break

# pegar empatados
empatados = []

for c in candidatos:
    if (
        c["nota"] == minha_nota and
        c["especificos"] == meus_especificos and
        c["portugues"] == meu_portugues and
        c["matematica"] == minha_matematica
    ):
        empatados.append(c)

print("Total de empatados:", len(empatados))

# comparar idade
minha_data_dt = datetime.strptime(minha_data, "%d/%m/%Y")

mais_velhos = 0

for c in empatados:
    if c["nome"] == meu_nome:
        continue

    data_c = datetime.strptime(c["data"], "%d/%m/%Y")

    if data_c < minha_data_dt:
        mais_velhos += 1

print("Empatados mais velhos que você:", mais_velhos)

# calcular posição final
posicao_final = posicao + mais_velhos

print("Sua colocação FINAL:", posicao_final)
print("Pessoas na sua frente:", posicao_final - 1)