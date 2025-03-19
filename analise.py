import os
import pandas as pd
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Configurações do Azure
endpoint = "SEU_ENDPOINT_AQUI"  # Substitua pelo seu endpoint do Azure
key = "SUA_CHAVE_AQUI"  # Substitua pela sua chave de API

# Inicializa o cliente do Azure Language Studio
credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# Função para analisar o sentimento de uma sentença
def analyze_sentiment(text):
    try:
        response = client.analyze_sentiment([text])
        sentiment = response[0].sentiment
        return sentiment
    except Exception as e:
        print(f"Erro ao analisar o texto: {e}")
        return None

# Lê o arquivo CSV com as sentenças
def read_sentences(file_path):
    try:
        # Lê o arquivo CSV com pandas
        df = pd.read_csv(file_path)
        sentences = df['sentence'].tolist()  # Supondo que a coluna das sentenças seja 'sentence'
        return sentences
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        return []

# Caminho do arquivo CSV
file_path = 'inputs/sentences.csv'

# Lê as sentenças
sentences = read_sentences(file_path)

# Avalia o sentimento de cada sentença
if sentences:
    for sentence in sentences:
        sentiment = analyze_sentiment(sentence)
        print(f"Sentença: {sentence}")
        print(f"Sentimento: {sentiment}\n")
else:
    print("Não há sentenças para avaliar.")
