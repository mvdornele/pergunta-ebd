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
                    "texto": "2.Lendo Apocalipse, capítulo 3, verso 9, comparado Apocalipse, capítulo 2, verso 16, qual o recurso que o Senhor colocou na igreja em Filadelfia para combater a oposição do anátema?",
                    "opcoes": [
                        "A revelação da Palavra pelo Espírito Santo, que é o ensino verdadeiro vindo da boca do Senhor.",
                        "A doutrina pura transmitida pela espada do Espírito, que é a Palavra de Deus revelada à igreja fiel.",
                        "A espada da boca do Senhor, a Palavra revelada."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "6.No livro de Apocalipse, capítulo 3, verso 8, fala sobre uma porta aberta. No livro de João,capítulo 10, verso 9, quem é essa porta que nos salva?",
                    "opcoes": [
                        "Jesus é a porta pela qual entramos e somos salvos; quem entra por Ele encontra salvação, segurança e pastagem.",
                        "A porta é o próprio Senhor Jesus, que nos conduz à salvação e à vida eterna.",
                        "Jesus é a porta aberta. Ele nos salva e cuida de nós."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
