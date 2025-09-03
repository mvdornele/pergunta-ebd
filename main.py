from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/pergunta")
def obter_perguntas():
    resposta = {
        # 👇 Estrutura futura com múltiplas perguntas separadas por categoria
        "perguntas": {
            "para_todos": [
                {
                    "texto": "1. Ao ler Apocalipse, capítulo 4, verso 7, identifique o significado profético das seguintes designações atribuidas ao Senhor Jesus na vidão de João- A- Semelhante a um Leão B- semelhamte a um Bezerro C- O rosto como Homem D-Semelhante a uma águia voando.",
                    "opcoes": [
                        "Leão → representa o Senhor Jesus como Rei soberano, aquele que reina com poder, autoridade e majestade sobre toda a criação.",    
                        "Bezerro → aponta para o sacrifício perfeito de Cristo, que se entregou em favor da Igreja, revelando obediência e serviço.",
                        "Homem → mostra o Jesus encarnado, que viveu como homem e se compadece das nossas fraquezas, sendo o intercessor fiel."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "2. Leia Hebreus, capítulo 11, verso 23 e responda, O que levou os pais de Moisés a não temerem faraó quando Moisés nasceu?.",
                    "opcoes": [
                        "Eles viram que Moisés era um menino formoso, separado por Deus, e reconheceram que havia um propósito especial na vida dele.",
                        "Agiram pela fé, confiando que Deus tinha um plano maior, e por isso não temeram o decreto de Faraó.",
                        "Tiveram coragem e confiança no Senhor, pois creram que a proteção divina era maior que a ordem do rei"
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
