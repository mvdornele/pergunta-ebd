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
                    "texto": "1.Ao ler Apocalipse, capítulo 1, verso 8 e capítulo 22, verso 13, identifique a relação profética da designação de Jesus como EU SOU, no evangelho de João, nas seguintes expressões:.",
                    "opcoes": [
                        "EU SOU o pão da vida.– João 6:48: Relaciona-se a Jesus como o princípio e o fim (Ap 1:8), pois Ele é quem sustenta a vida eterna.Assim como o pão físico alimenta o corpo, Jesus é o alimento espiritual que dá vida eterna",    
                        "EU SOU a luz do mundo.– João 8:12: Relaciona-se a Jesus como a luz que guia na eternidade (Ap 22:13). Ele é a luz que dissipa as trevas do pecado e conduz o seu povo até a Canaã Celestial.",
                        "EU SOU o bom Pastor.– João 10:11: Relaciona-se a Jesus como o que é, que era e que há de vir (Ap 1:8), pois Ele cuida das suas ovelhas em todo tempo, deu a sua vida por elas e as conduzirá até a vida eterna."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "2.Leia, Êxodo capitulo 14, verso 13 e 14a, e responda: Quem batalhou pelo povo de Israel e batalha por nós para nos tirar deste mundo e nos levar para a Canaã Celestial?.",
                    "opcoes": [
                        "O Senhor Deus.",
                        "Jesus Cristo.",
                        "O Espírito Santo."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
