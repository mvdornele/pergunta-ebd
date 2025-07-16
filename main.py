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
                    "texto": "2.Lendo Apocalipse, capítulo 3, verso 8a, comparado com Mateus, capítulo 13, versos 45 e 46,identifique o comportamento da igreja de Filadelfia. Faça a aplicação profética para a igreja dos nossos dias.",
                    "opcoes": [
                        "Jesus revelado à igreja como a pérola de grande valor.",    
                        "A igreja de Filadélfia persevera na Palavra e reconhece o valor incomparável de Jesus, entregando tudo por Ele.",
                        "A igreja de Filadélfia reconhece a porta aberta pela revelação de Jesus e não a rejeita, demonstrando fé e dependência espiritual."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "5.Lendo Mateus, capítulo 13, verso 47, junto com Mateus, capítulo 4, verso 19, o que isso quer dizer? A Rede, O Mar, Os Peixes?",
                    "opcoes": [
                        "A rede usada para falar de Jesus, O mar é o mundo, Os peixes são as pessoas que ouvem falar de Jesus.",
                        "A rede representa a pregação do Evangelho, o mar representa a humanidade perdida, e os peixes são os que serão alcançados pela Palavra.",
                        "A rede é o instrumento da salvação, o mar é o lugar de confusão e pecado, e os peixes são os que respondem ao chamado de Jesus."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
