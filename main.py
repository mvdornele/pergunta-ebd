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
                    "texto": "2.LendoApocalipse, capítulo 3, verso 9, qual a constatação que esses, da sinagoga de satanás,farão com a Igreja Fiel, em nossos dias?",
                    "opcoes": [
                        "Saberão que a Igreja Fiel é cheia do amor de Deus, pela ação do Espírito Santo,…eis que eu farei que venham, e adorem prostrados a teus pés, e saibam que eu te amo.",
                        "Reconhecerão que a Igreja Fiel é amada e guardada pelo Senhor, pois Ele mesmo manifesta Seu cuidado e presença nela.",
                        "Verão que a Igreja Fiel permanece firme na Palavra e na comunhão com Deus, sendo um testemunho vivo da obra do Espírito Santo neste tempo."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "4.Lendo Apocalipse, capítulo 3, verso 12, e I Timóteo, capítulo 3, verso 15, como a nossa família deve ser na casa do Senhor?",
                    "opcoes": [
                        "A nossa família deve ser firme como uma coluna na Casa do Senhor, sempre participando das escolas bíblicas, dos cultos e vivendo a verdade da Palavra de Deus",
                        "Nossa família deve ser exemplo de fidelidade e compromisso na Casa do Senhor, sustentando o testemunho da fé e da doutrina com amor e perseverança.",
                        "Nossa família deve viver em comunhão com a igreja, edificada na Palavra e no Espírito, sendo um pilar que fortalece a obra do Senhor em todas as suas atividades."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
