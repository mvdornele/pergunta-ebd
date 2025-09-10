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
                    "texto": "1.Ao ler Apocalipse, Capitulo 5, versos 5 e 6, identifique a relação profética entre três designações atribuidas ao senhor jesus na visão de João. Faça aplicação na vida da Igreja.,
                    "opcoes": [
                        "O Leão da tribo de Juda: Mostra que Jesus é o Rei vitorioso, que reina sobre todas as coisas e dá à igreja segurança diante das lutas espirituais.",    
                        "A raiz de Davi: Ensina que toda a esperança e governo espiritual da igreja estão firmados em Cristo, o verdadeiro Rei prometido, que sustenta e conduz o Seu povo.",
                        "O Cordeiro, como havendo sido morto: Mostra que a vitória da igreja está no sangue do Cordeiro. Ele é a base da nossa salvação, adoração e comunhão eterna com Deus."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "2.Leia Êxodo, capítulo 3, verso 4, e responda: O que Moisés respondeu quando Deus o chamou?.",
                    "opcoes": [
                        "Disponibilidade – Moisés mostrou-se pronto para ouvir a voz de Deus.",
                        "Entrega – Ao dizer “Eis-me aqui”, ele reconheceu que sua vida estava nas mãos do Senhor.",
                        "Chamado – Foi o início de sua missão como libertador do povo de Israel."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
