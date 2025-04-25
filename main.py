from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

pergunta = {
    "pergunta": "Você participou da EBD esta semana?",
    "opcoes": ["Sim", "Não", "Participei Online"]
}

@app.route("/pergunta")
def get_pergunta():
    return jsonify(pergunta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
