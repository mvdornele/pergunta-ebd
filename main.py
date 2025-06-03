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
                    "texto": "1.Lendo Apocalipse, capítulo 3, versos de 7 a 13, identifique as sete operações do Espírito de Deus em Filadélfia. Escolha um breve comentário sobre: A) Espírito do Senhor B) Espírito de Sabedoria C) Espírito de Inteligência",
                    "opcoes": [
                        "A) Espírito do Senhor (Essa operação revela a autoridade suprema de Jesus sobre a Igreja. Ele governa, abre e fecha portas espirituais, e conduz a Igreja segundo sua soberania).",
                        "B) Espírito de Sabedoria (A igreja de Filadélfia agiu com sabedoria ao valorizar a Palavra e o Nome do Senhor, mesmo em tempos de perseguição. A sabedoria do alto os fez entender o que realmente tinha valor espiritual).",
                        "C) Espírito de Inteligência ( A inteligência espiritual capacita o crente a discernir a vontade de Deus e agir com entendimento. Filadélfia entendeu o significado da "porta aberta" — uma oportunidade de serviço, comunhão e salvação — e seguiu com fé."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "3.Lendo Mateus, capítulo 13, versos 45 e 46, como a pérola de grande valor nos ajuda a entender o que o Espírito Santo nos mostra sobre Jesus?",
                    "opcoes": [
                        "O negociante achou uma pérola muito especial e ficou com ela. A igreja de Filadélfia entendeu que Jesus é muito especial. O Espírito Santo mostra que Jesus é precioso, como essa pérola.",
                        "Assim como o negociante vendeu tudo para adquirir a pérola, o Espírito Santo nos mostra que Jesus é tão valioso que vale a pena deixar tudo para segui-Lo.",
                        "A pérola é única, rara e perfeita — assim como Jesus. O Espírito Santo nos revela essa beleza e valor espiritual de Cristo, mostrando que Ele é o tesouro maior que Deus nos deu."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
