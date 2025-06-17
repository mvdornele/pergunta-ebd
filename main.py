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
                    "texto": "1.Lendo Apocalipse, capítulo 3, verso 10, comparado com Apocalipse, capítulo 8, verso 13b, o que acontecerá com o mundo após o arrebatamento da igreja?",
                    "opcoes": [
                        "Deus permitirá que o mal atue com maior liberdade",
                        "Acontecerão os juízos da Grande Tribulação, ao toque das 3 últimas trombetas.",
                        "O mundo enfrentará a ira de Deus."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "3.Lendo Apocalipse, capítulo 3, versos 8b, comparado com Salmos, capítulo 119, verso 11, onde o filho que honra pai e mãe guarda a Palavra de Deus?",
                    "opcoes": [
                        "Ele guarda a Palavra de Deus no seu coração.",
                        "Ele guarda a Palavra no coração para não pecar contra o Senhor, mostrando temor e obediência.",
                        "Ele guarda a Palavra com fidelidade e amor, seguindo o caminho que o Senhor abriu diante dele."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
