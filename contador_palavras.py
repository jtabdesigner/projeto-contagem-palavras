import csv
import string

# Abrindo o arquivo e lendo o conteúdo
with open("texto.txt", "r", encoding="utf-8") as file:
    conteudo = file.read()

# Removendo pontuações e convertendo o texto para minúsculas
conteudo = conteudo.translate(str.maketrans("", "", string.punctuation)).lower()

# Contando a frequência das palavras
palavras = conteudo.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

# Exibindo o resultado
print("Contagem de palavras:")
for palavra, contagem in contagem_palavras.items():
    print(f"{palavra}: {contagem}")

# Exportando o relatório para um arquivo CSV
with open("contagem_palavras.csv", "w", newline="") as csvfile:
    fieldnames = ['Palavra', 'Contagem']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Escreve o cabeçalho do CSV
    for palavra, contagem in contagem_palavras.items():
        writer.writerow({'Palavra': palavra, 'Contagem': contagem})

print("Relatório exportado para contagem_palavras.csv")