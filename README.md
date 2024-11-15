# Projeto Contagem de Palavras

Este é um projeto em Python que realiza a contagem de palavras em um arquivo de texto. O objetivo é ler o conteúdo do arquivo, contar a frequência de cada palavra e exibir um relatório com as contagens.

## Objetivo

- Criar um script em Python que leia um arquivo de texto.
- Conte a frequência de cada palavra.
- Exiba a contagem de palavras na tela.
- Exporte a contagem de palavras para um arquivo CSV para análise posterior.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

projeto_contagem_palavras/
│
├── contador_palavras.py   # Script principal que realiza a contagem de palavras
├── texto.txt              # Arquivo de exemplo com conteúdo para contagem de palavras
├── contagem_palavras.csv  # Relatório gerado com a contagem de palavras em formato CSV
└── README.md              # Este arquivo


## Como Usar

1. Clone este repositório para o seu computador:
2. Abra o arquivo `texto.txt` e adicione o texto que deseja analisar.
3. Execute o script Python:
4. O script exibirá a contagem das palavras no terminal.
5. O arquivo contagem_palavras.csv será gerado no mesmo diretório, contendo a lista de palavras e suas contagens.

## Como Funciona

- O arquivo contador_palavras.py abre o arquivo texto.txt, lê seu conteúdo e remove pontuações.
- O texto é convertido para minúsculas para garantir que palavras iguais sejam contadas corretamente.
- A contagem de palavras é exibida no terminal.
- O script também gera um arquivo CSV chamado contagem_palavras.csv, que contém as palavras e suas respectivas contagens.

## Exemplo de Saída

Ao executar o script, a saída será algo como:

Contagem de palavras:

certificação: 1
business: 1
intelligence: 1
foundation: 1
...
Relatório exportado para contagem_palavras.csv

## Tecnologias Utilizadas

- Python 3.x

## Contribuindo

Se você quiser contribuir para este projeto, fique à vontade para abrir um "pull request" com melhorias!

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).