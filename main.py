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
                    "texto": "1.Ao ler Apocalipse, capitulo 13,verso8, quem sãos os adoradores do senhor jesus, cujo os nomes estão escritos no livro da Vida?.",
                    "opcoes": [
                        "são os que reconhecem Jesus como Senhor e O adoram; seus nomes estão escritos no Livro da Vida porque foram redimidos pela fé. Apoc. 13:8; Apoc. 21:27.",    
                        "aqueles que se arrependeram e foram purificados por Cristo; a Bíblia descreve os redimidos como os que "lavaram as suas vestes e as branquearam no sangue do Cordeiro". Apoc. 7:14.",
                        "os fiéis que permanecem em Cristo até o fim; a Escritura associa fidelidade perseverante à permanência no Livro da Vida Apoc. 3:5; Apoc. 2:10."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "3.Leia Lucas,capitulo 19, verso 5 a 6 e responde: O que Zaqueu fez quando Jesus disse que queria pousar na sua casa?",
                    "opcoes": [
                        "Apressou-se a descer da árvore. — Zaceu fez haste para descer quando Jesus disse que queria ficar em sua casa. Lc 19:5.",
                        "Recebeu Jesus em sua casa. — Ele abriu sua casa e hospedou Jesus. Lc 19:5.",
                        "Fez isso com alegria. — Lucas diz explicitamente que Zaceu o recebeu com alegria. Lc 19:6."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
