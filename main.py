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
                    "texto": "2.Ao ler Apocalipse, capítulo 19, versos 7 e 8, identifique o sentido profético das vestes da Igreja que já está pronta como a esposa do Cordeiro.",
                    "opcoes": [
                        "Representam o estado espiritual daqueles que foram lavados e purificados pelo sangue de Jesus, conforme está escrito.Apocalipse 22:14",    
                        "Elas não são fruto de mérito humano, mas resultado da obediência e fidelidade à Palavra de Deus, conforme o próprio versículo declara.Apocalipse 19:8",
                        "A Igreja adornada com vestes puras e resplandecentes é símbolo de que está pronta para as Bodas do Cordeiro — um povo separado, fiel e revestido da graça do Senhor.Apocalipse 19:7"
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "4.Leia João, capítulo 14, verso 3, e responda: O que Jesus fará quando Ele voltar?",
                    "opcoes": [
                        "Ele prometeu voltar para levar consigo aqueles que creram n’Ele e guardaram Sua Palavra. João 14:3",
                        "O retorno de Cristo marca o cumprimento da promessa da vida eterna ao lado do Pai. 1 Tessalonicenses 4:17",
                        "Na Sua vinda, Ele dará a coroa da vida aos que permaneceram firmes na fé. Apocalipse 22:12"
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
