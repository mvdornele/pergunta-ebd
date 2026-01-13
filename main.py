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
                    "texto": "1.Lendo Levítico, capítulo 2, verso 1, identifique o sentido profético dos seguintes ingredientes básicos da oferta de manjares.",
                    "opcoes": [
                        "Flor de farinha:Representa a perfeição, pureza e humanidade sem pecado de Cristo .",    
                        "Azeite: Simboliza o Espírito Santo.",
                        "Incenso: Representa a oração, a intercessão e o bom perfume que sobe a Deus."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "3.Leia Hebreus, capítulo 11, versículo 6, e responda, O que devemos ter em nossos corações para agradar a Deus?",
                    "opcoes": [
                        "Fé em Deus",
                        "Crer que Deus existe.",
                        "Buscar a Deus com sinceridade."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
