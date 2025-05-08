from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/pergunta")
def obter_perguntas():
    resposta = {
        # 👇 Compatível com o app atual
        "pergunta": "2.Lendo Apocalipse, capítulo 3, verso 3a, comparado com 1 Samuel, capítulo 3, verso 10, quais as primeiras palavras que caracterizaram a Obra do Espírito Santo em nosso meio, como remanescentes de Sardes?",
        "opcoes": [
            "Não Ouvir a Palavra do Senhor e não Obedecer.",
            "As palavras Ouvir a Palavra do Senhor e Obedecer.",
            " A realização de uma grande Obra no nosso meio."
        ],

        # 👇 Estrutura futura com múltiplas perguntas separadas por categoria
        "perguntas": {
            "para_todos": [
                {
                    "texto": "2.Lendo Apocalipse, capítulo 3, verso 3a, comparado com 1 Samuel, capítulo 3, verso 10, quais as primeiras palavras que caracterizaram a Obra do Espírito Santo em nosso meio, como remanescentes de Sardes?",
                    "opcoes": [
                        "Não Ouvir a Palavra do Senhor e não Obedecer.",
                        "As palavras Ouvir a Palavra do Senhor e Obedecer.",
                        " A realização de uma grande Obra no nosso meio."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "5.Lendo Mateus, capítulo 13, verso 27, e Apocalipse, capítulo 2, verso 9a, o que representam: A) A boa semente, o trigo? B) A má semente, o joio?",
                    "opcoes": [
                        "A boa semente, o trigo, é a Palavra de Deus, que alimenta o coração do homem. A má semente, o joio, são os maus ensinos que vêm do mundo.",
                        "A boa semente representa os que seguem tradições religiosas, e o joio representa os que se afastaram da religião verdadeira.",
                        "A boa semente representa os anjos de Deus, e o joio representa os profetas do Antigo Testamento."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
