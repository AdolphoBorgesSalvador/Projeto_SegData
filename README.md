
# Projeto de Extração de Dados de Documentos PDF

Este projeto tem como objetivo extrair informações específicas (Nome, CPF, RG e Endereço) de documentos PDF relacionados a propostas de seguros utilizando a API do GPT-3.5 da OpenAI.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação utilizada.
- **PyMuPDF**: Biblioteca usada para manipular arquivos PDF e extrair seu conteúdo textual.
- **Requests**: Biblioteca para fazer requisições HTTP à API do OpenAI.
- **API OpenAI GPT-3.5**: Utilizada para processar o texto extraído dos PDFs e identificar os dados solicitados (Nome, CPF, RG e Endereço).

## Como Usar

### Requisitos

1. **Python 3.x**: Instale a versão mais recente do Python, se necessário.
2. **Bibliotecas**: Instale as dependências utilizando `pip`:

```bash
pip install fitz requests
```

3. **API Key**: Este código usa a API GPT-3.5 da OpenAI, portanto, você precisará de uma chave de API. Crie uma conta em [OpenAI](https://platform.openai.com/) e obtenha sua chave de API. Em seguida, crie um arquivo chamado `senha.py` com a seguinte variável:

```python
API_KEY = 'sua_chave_aqui'
```

### Estrutura do Projeto

```
Projeto_SeguraData/
│
├── arquivos/
│   ├── .pdf
│   ├── .pdf
│   └── ...
│
├── extrair_dados.py
├── senha.py
└── resultados_extracao.json
```

- **arquivos/**: Pasta onde os PDFs a serem processados devem ser armazenados.
- **extrair_dados.py**: Script principal para extração dos dados.
- **senha.py**: Arquivo que contém a chave da API da OpenAI.
- **resultados_extracao.json**: Arquivo de saída que contém os resultados extraídos de cada PDF.

### Como Executar

1. Coloque os PDFs que deseja processar na pasta `arquivos/`.
2. Execute o script `extrair_dados.py`:

```bash
python extrair_dados.py
```

3. O script vai gerar um arquivo `resultados_extracao.json` com os dados extraídos dos PDFs, contendo informações como Nome, CPF, RG e Endereço. Caso algum dado não seja encontrado, o valor será "Não identificado".

### Explicação do Código

- **extrair_texto_pdf**: Função que abre e lê o conteúdo textual de um arquivo PDF utilizando a biblioteca PyMuPDF.
- **usar_api_gpt_para_dados**: Função que envia o texto extraído para a API GPT-3.5 para processar e extrair informações relevantes (Nome, CPF, RG e Endereço).
- **extrair_campo**: Função auxiliar para extrair o valor correspondente a um campo específico do texto retornado pela API.
- **resultados**: Lista que armazena os dados extraídos de cada PDF processado.
- **resultados_extracao.json**: Arquivo gerado contendo os resultados da extração em formato JSON.

## Exemplo de Saída

A saída será um arquivo JSON semelhante ao seguinte:

```json
[
    {
        "arquivo":,
        "nome":,
        "cpf": ,
        "rg": ,
        "endereco":"
    },
    {
        "arquivo": ,
        "nome": ,
        "cpf": ,
        "rg": ,
        "endereco":
    },
    ...
]
```

## Possíveis Melhorias

- Melhorar a precisão da extração de dados, ajustando o modelo da API para identificar melhor os campos.
- Adicionar suporte para mais tipos de documentos e informações.
- Implementar tratamento de erros mais robusto para lidar com falhas na API ou nos arquivos PDF.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

