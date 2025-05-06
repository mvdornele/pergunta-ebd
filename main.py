from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

pergunta = {
    "pergunta": "Lendo Apocalipse, capítulo 3, verso 3a, comparado com 1 Samuel, capítulo 3, verso 10, quais as primeiras palavras que caracterizaram a Obra do Espírito Santo em nosso meio, como remanescentes de Sardes? ",
    "opcoes": ["Não Ouvir a Palavra do Senhor e não Obedecer.", "As palavras Ouvir a Palavra do Senhor e Obedecer.", " A realização de uma grande Obra no nosso meio."]
}

@app.route("/pergunta")
def get_pergunta():
    return jsonify(pergunta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
