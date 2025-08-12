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
                    "texto": "1. Lendo Apocalipse, capítulo 3, versos 17 e 18, identifique a relação entre as seguintes características da igreja de Laodiceia e os conselhos do Senhor Jesus. Faça a aplicação profética",
                    "opcoes": [
                        "Batismo com o Espírito Santo, discernimento espiritual e experiência de salvação — a igreja de Laodiceia carece desses três aspectos, vivendo na força humana, sem santidade e misturada com o mundo.",    
                        "Falta à igreja de Laodiceia poder espiritual, clareza para distinguir o santo do profano e vida transformada pelo sangue de Jesus.",
                        "A igreja de Laodiceia vive sem o poder do Espírito Santo, sem discernimento e sem comunhão verdadeira com Deus, conformando-se com o mundo."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "2. Leia 1 Samuel, capítulo 16, verso 7b e Atos, capítulo 13, verso 22b, e responda: Por que Deus escolheu Davi para ser rei de Israel?",
                    "opcoes": [
                        "Porque Davi tinha um coração obediente a Deus.",
                        "Porque Davi tinha um coração segundo o coração de Deus.",
                        "Porque Davi fazia a vontade de Deus em todas as coisas."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
