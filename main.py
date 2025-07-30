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
                    "texto": "3.Lendo Apocalipse, capítulo 3, verso 20, o que temos que fazer para o Senhor Jesus habitar em nosso coração?",
                    "opcoes": [
                        "Ouvir a voz do Senhor Jesus e abrir o coração para Ele entrar e fazer morada em nossa vida.",    
                        "Estar atentos à voz do Senhor e responder ao Seu chamado com obediência e fé, permitindo que Ele transforme nosso interior.",
                        "Receber Jesus com sinceridade, entregando nossa vida a Ele e permitindo que Sua presença guie nossos pensamentos e atitudes."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "4.Lendo Apocalipse, capítulo 3, verso 20, o que temos que fazer para Jesus morar no nosso coração?",
                    "opcoes": [
                        "Estar atentos à voz do Senhor e responder ao Seu chamado com obediência e fé, permitindo que Ele transforme nosso interior.",
                        "Ouvir Jesus. Abrir o coração para Jesus entrar e morar",
                        "Receber Jesus com sinceridade, entregando nossa vida a Ele e permitindo que Sua presença guie nossos pensamentos e atitudes."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
