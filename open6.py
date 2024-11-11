import fitz  # PyMuPDF
import requests
import json
import re
from senha import API_KEY

def extrair_texto_pdf(caminho_arquivo):
    texto_completo = ""
    with fitz.open(caminho_arquivo) as pdf:
        for pagina in pdf:
            texto_completo += pagina.get_text()
    return texto_completo

def usar_api_gpt_para_dados(texto):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_modelo = "gpt-3.5-turbo"

    body_mensagem = {
        "model": id_modelo,
        "messages": [
            {"role": "system", "content": "Você é um assistente que ajuda a identificar informações específicas em documentos de seguro."},
            {"role": "user", "content": "A partir do texto fornecido abaixo, identifique e extraia o Nome, CPF, RG e Endereço do segurado.\n\n" + texto}
        ]
    }

    response = requests.post(link, headers=headers, json=body_mensagem)

    if response.status_code == 200:
        resposta = response.json()
        conteudo = resposta['choices'][0]['message']['content'].strip()
        
        # Exibir a resposta para debug
        print("Conteúdo da resposta da API:", conteudo)
        
        # Processa o conteúdo retornado em formato de texto
        dados_extraidos = {
            "nome": extrair_campo("Nome", conteudo),
            "cpf": extrair_campo("CPF", conteudo),
            "rg": extrair_campo("RG", conteudo),
            "endereco": extrair_campo("Endereço", conteudo)
        }
        
        return dados_extraidos
    else:
        print("Erro na API:", response.status_code, response.text)
        return {"nome": "Não identificado", "cpf": "Não identificado", "rg": "Não identificado", "endereco": "Não identificado"}

def extrair_campo(label, texto):
    padrao = rf"{label}.*?:\s*(.*)"
    match = re.search(padrao, texto, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return "Não identificado"

arquivos_pdf = [
    r"C:\Users\Adolp\OneDrive\Área de Trabalho\Programação\Py\Projeto_SeguraData\arquivos\05.11.2025 - Lucila D Angelo Camacho Cecere - Proposta HDI - Placa FGB8732.pdf",
    r"C:\Users\Adolp\OneDrive\Área de Trabalho\Programação\Py\Projeto_SeguraData\arquivos\07.11.2025 - Debora Felipe Gama (Vinicius Sanches) - Proposta Allianz - Placa FJU9C07.pdf",
    r"C:\Users\Adolp\OneDrive\Área de Trabalho\Programação\Py\Projeto_SeguraData\arquivos\01.11.2025 - Alessandra Deutschmann - Proposta Porto Seguro Residencial - CEP 05684040 (Serzedello).pdf",
    r"C:\Users\Adolp\OneDrive\Área de Trabalho\Programação\Py\Projeto_SeguraData\arquivos\17.11.2025 - Condominio Edifico Parque - Proposta Tokio Marine Condominio - CEP 04601-030.pdf",
    r"C:\Users\Adolp\OneDrive\Área de Trabalho\Programação\Py\Projeto_SeguraData\arquivos\impressao.do.pdf"
]

resultados = []

for arquivo in arquivos_pdf:
    texto = extrair_texto_pdf(arquivo)
    dados_extraidos = usar_api_gpt_para_dados(texto)  # Chama a API para identificar os dados
    
    resultados.append({
        "arquivo": arquivo.split('\\')[-1],
        "nome": dados_extraidos.get("nome", "Não identificado"),
        "cpf": dados_extraidos.get("cpf", "Não identificado"),
        "rg": dados_extraidos.get("rg", "Não identificado"),
        "endereco": dados_extraidos.get("endereco", "Não identificado")
    })

with open("resultados_extracao.json", "w", encoding="utf-8") as f:
    json.dump(resultados, f, indent=4, ensure_ascii=False)

print("Arquivo JSON 'resultados_extracao.json' gerado com sucesso.")
