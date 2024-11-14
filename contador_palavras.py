# Abrindo o arquivo e lendo o conteúdo
with open("texto.txt", "r") as file:
    conteudo = file.read()

# Removendo pontuações e convertendo o texto para minúsculas
import string
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