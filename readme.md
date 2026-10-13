# Automação de Cadastro de Produtos com Python

Script em Python que automatiza o cadastro de produtos em um sistema web. Ele abre o navegador, faz login no site, lê uma base de dados em CSV e preenche o formulário de cadastro, um produto por vez, simulando as ações de mouse e teclado de uma pessoa.

O projeto foi desenvolvido a partir do Intensivão de Python da Hashtag Treinamentos e utiliza o sistema de testes disponibilizado pelo curso:
https://dlp.hashtagtreinamentos.com/python/intensivao/login

## Visão geral

Cadastrar centenas de itens manualmente é uma tarefa repetitiva e sujeita a erros. Este projeto resolve esse problema automatizando todo o fluxo:

1. Abre o Google Chrome pelo menu iniciar do Windows.
2. Acessa a página de login do sistema.
3. Realiza o login com e-mail e senha.
4. Lê o arquivo `produtos.csv` com a biblioteca pandas.
5. Para cada linha do arquivo, preenche e envia o formulário de cadastro.

A base de exemplo contém 293 produtos, que são cadastrados em sequência sem intervenção manual.

## Tecnologias utilizadas

- Python 3
- [PyAutoGUI](https://pyautogui.readthedocs.io/): controle de mouse e teclado
- [pandas](https://pandas.pydata.org/): leitura e manipulação da base de dados

## Pré-requisitos

- Windows (o script abre o navegador pelo menu iniciar com a tecla `win`)
- Google Chrome instalado
- Python 3.8 ou superior
- Conta de acesso ao sistema de teste utilizado no projeto

## Instalação

Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/angelomoraes/Automacao-Cadastro-CSV.git
cd Automacao-Cadastro-CSV
```

Instale as dependências:

```bash
pip install pyautogui pandas
```

### Coordenadas do mouse

O script clica em posições fixas da tela para focar os campos do formulário. As coordenadas atuais foram calibradas para um monitor com resolução de 1360x768:

| Ação                                  | Coordenadas        |
|---------------------------------------|--------------------|
| Clique no campo de e-mail (login)     | `x=533, y=406`     |
| Clique no primeiro campo do cadastro  | `x=516, y=289`     |

Se a sua resolução ou o zoom do navegador forem diferentes, essas posições precisarão ser recalibradas. Para isso, use o `auxiliar.py`:

```bash
python auxiliar.py
```

Ao executar, você tem 3 segundos para posicionar o mouse sobre o ponto desejado na tela. O script imprime no terminal as coordenadas (x, y) daquela posição, que devem ser copiadas para o `main.py`.

### Tempos de espera

Os `time.sleep(3)` aguardam o carregamento das páginas. Em conexões mais lentas, aumente esse valor. A pausa global entre cada comando do PyAutoGUI está definida em `ag.PAUSE = 1` (1 segundo).

## Como executar

1. Feche janelas que possam atrapalhar e deixe a área de trabalho livre.
2. Confira se o arquivo `produtos.csv` está na mesma pasta do `main.py`.
3. Execute:

```bash
python main.py
```

4. Não mexa no mouse nem no teclado enquanto a automação estiver rodando, pois qualquer interferência pode desalinhar o preenchimento.

Para interromper a execução em caso de problema, mova o mouse rapidamente para o canto superior esquerdo da tela. O mecanismo de segurança (fail-safe) do PyAutoGUI irá encerrar o script. Você também pode usar `Ctrl + C` no terminal.

## Formato do arquivo CSV

O arquivo `produtos.csv` deve estar codificado em UTF-8 e conter as seguintes colunas:

| Coluna           | Tipo    | Descrição                                |
|------------------|---------|------------------------------------------|
| `codigo`         | Texto   | Código identificador do produto          |
| `marca`          | Texto   | Marca do produto                         |
| `tipo`           | Texto   | Tipo do produto                          |
| `categoria`      | Inteiro | Categoria do produto                     |
| `preco_unitario` | Decimal | Preço de venda unitário                  |
| `custo`          | Decimal | Custo do produto                         |
| `obs`            | Texto   | Observações (opcional, pode ficar vazio) |
