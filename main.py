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
                    "texto": "1.Lendo Apocalipse, capítulo 3, verso 10, destaque as figuras proféticas da Trindade.",
                    "opcoes": [
                        "O PAI -A Palavra - doutrina,O FILHO -A oração que Jesus fez por nós, O ESPÍRITO SANTO -levará a igreja antes da hora da grande Tribulação.",    
                        "O PAI – revelou o plano eterno de salvação, O FILHO –  O cumprimento da promessa de livramento, O ESPÍRITO SANTO - Quem prepara e conduz a igreja fiel ao arrebatamento.",
                        "O PAI – Quem, por sua fidelidade, sustenta o remanescente, O FILHO – O que cumpre a promessa do arrebatamento, O ESPÍRITO SANTO – É o selo e o penhor da promessa do livramento da igreja fiel."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "4.Lendo Apocalipse, capítulo 2, verso 14, e I Coríntios, capítulo 8, verso 4, como devemos agir com relação àquilo que é sacrificado a ídolos?",
                    "opcoes": [
                        "Devemos rejeitar qualquer prática que envolva o culto aos ídolos, porque sabemos que só há um Deus verdadeiro, e não podemos participar de coisas oferecidas ao que é falso.",
                        "Devemos nos afastar de tudo aquilo que é sacrificado a ídolos, porque adoramos somente ao nosso Deus",
                        "Devemos ser vigilantes e evitar o envolvimento com sacrifícios a ídolos, para não sermos tropeço aos irmãos na fé e não nos contaminarmos espiritualmente."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
