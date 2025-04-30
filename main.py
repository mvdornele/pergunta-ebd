from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

pergunta = {
    "pergunta": "Lendo Mateus, capítulo 13, verso 8, e Apocalipse, capítulo 2, verso 7, qual a promessa que o Senhor fez para aqueles que receberam a Palavra de Deus e deram frutos? ",
    "opcoes": ["Eles comerão do fruto da árvore da vida, que está no meio do paraíso de Deus.", "Eles NÃO comerão do fruto da árvore da vida, que está no meio do paraíso de Deus.", "Nenhuma das alternativas"]
}

@app.route("/pergunta")
def get_pergunta():
    return jsonify(pergunta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
