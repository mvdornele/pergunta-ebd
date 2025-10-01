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
                    "texto": "1.Ao ler Apocalipse, capítulo 6, verso 2, o que representa na história da Igreja o cavalo branco, que saiu vitorioso para vencer?.",
                    "opcoes": [
                        "O cavalo branco simboliza a pureza e a vitória do Evangelho anunciado pela Igreja primitiva.",    
                        "O que está montado no cavalo branco aponta para Cristo, que venceu o pecado e a morte e continua conduzindo a Igreja em triunfo.",
                        "Representa a Igreja no início da sua jornada, cheia do Espírito Santo, pregando com autoridade e alcançando vitória espiritual sobre o mundo."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "4.Leia Marcos, capítulo 1, versículo 17, e responda: O que é ser “pescador de homens”?.",
                    "opcoes": [
                        "Ser pescador de homens é anunciar o Evangelho para que pessoas sejam salvas.",
                        "Significa obedecer à voz de Jesus, deixando interesses pessoais para cumprir a missão dele.",
                        "Ser pescador de homens é ser instrumento de Deus para tirar pessoas das trevas e conduzi-las à vida eterna."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
