# Análise de sentimentos com Language Studio no Azure AI

**Sentiment and opinion mining** é uma solução da plataforma **Language Studio, da Azure**, que permite **detectar sentimentos positivos, negativos e neutros** a partir de sentenças. Esse repositório mostra alguns exemplos de testes na plataforma. Os procedimentos foram realizados como parte do **Bootcamp Microsoft Azure AI Fundamentals, da DIO**.

Também coloquei um pequena exemplo de aplicação em python que se comunica com a API do Azure AI para realizar analise de sentimento em um conjunto de sentenças. 

### Para utilizar a aplicação é necessário instalar as dependênias: 

pip install -r requirements.txt

###  Sobre os resultado:

A análise dos resultados podem ser obtidas tanto de forma gráfica como em um JSON.

Segue um exemplo de resultado em json para a sentença que usei de exemplo:

```json
{
    "documents": [
        {
            "id": "id__1497",
            "sentiment": "mixed",
            "confidenceScores": {
                "positive": 0.74,
                "neutral": 0.01,
                "negative": 0.25
            },
            "sentences": [
                {
                    "sentiment": "positive",
                    "confidenceScores": {
                        "positive": 0.95,
                        "neutral": 0.04,
                        "negative": 0.01
                    },
                    "offset": 0,
                    "length": 40,
                    "text": "I bought a size S and it fit perfectly. ",
                    "targets": [],
                    "assessments": []
                },
                {
                    "sentiment": "negative",
                    "confidenceScores": {
                        "positive": 0,
                        "neutral": 0,
                        "negative": 0.99
                    },
                    "offset": 40,
                    "length": 84,
                    "text": "I found the zipper a little bit difficult to get up & down due to the side rushing. ",
                    "targets": [
                        {
                            "sentiment": "negative",
                            "confidenceScores": {
                                "positive": 0,
                                "negative": 1
                            },
                            "offset": 52,
                            "length": 6,
                            "text": "zipper",
                            "relations": [
                                {
                                    "relationType": "assessment",
                                    "ref": "#/documents/0/sentences/1/assessments/0"
                                }
                            ]
                        }
                    ],
                    "assessments": [
                        {
                            "sentiment": "negative",
                            "confidenceScores": {
                                "positive": 0,
                                "negative": 1
                            },
                            "offset": 72,
                            "length": 9,
                            "text": "difficult",
                            "isNegated": false
                        }
                    ]
                },
                {
                    "sentiment": "positive",
                    "confidenceScores": {
                        "positive": 0.99,
                        "neutral": 0,
                        "negative": 0
                    },
                    "offset": 124,
                    "length": 48,
                    "text": "The color and material are beautiful in person. ",
                    "targets": [
                        {
                            "sentiment": "positive",
                            "confidenceScores": {
                                "positive": 1,
                                "negative": 0
                            },
                            "offset": 128,
                            "length": 5,
                            "text": "color",
                            "relations": [
                                {
                                    "relationType": "assessment",
                                    "ref": "#/documents/0/sentences/2/assessments/0"
                                }
                            ]
                        },
                        {
                            "sentiment": "positive",
                            "confidenceScores": {
                                "positive": 1,
                                "negative": 0
                            },
                            "offset": 138,
                            "length": 8,
                            "text": "material",
                            "relations": [
                                {
                                    "relationType": "assessment",
                                    "ref": "#/documents/0/sentences/2/assessments/0"
                                }
                            ]
                        }
                    ],
                    "assessments": [
                        {
                            "sentiment": "positive",
                            "confidenceScores": {
                                "positive": 1,
                                "negative": 0
                            },
                            "offset": 151,
                            "length": 9,
                            "text": "beautiful",
                            "isNegated": false
                        }
                    ]
                },
                {
                    "sentiment": "positive",
                    "confidenceScores": {
                        "positive": 0.99,
                        "neutral": 0,
                        "negative": 0
                    },
                    "offset": 172,
                    "length": 22,
                    "text": "Amazingly comfortable!",
                    "targets": [],
                    "assessments": []
                }
            ]
        }
    ],
    "errors": []
}



### Conclusão e Insights

Ferramentas de análise de sentimentos funcionam bem para textos com emoção clara, mas falham quando o contexto não é considerado. Uma abordagem que conecte sentenças pode melhorar a precisão.