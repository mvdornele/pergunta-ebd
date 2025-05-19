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
                    "texto": "4.Lendo Apocalipse, capítulo 3, verso 9, identifique a oposição que se levantou contra a fé no período profético de Filadelfia?",
                    "opcoes": [
                        "Grupos religiosos que ensinavam doutrinas erradas e tentavam impedir a ação do Espírito de Deus na Igreja.",
                        "Pessoas que se diziam do povo de Deus, mas rejeitavam a verdadeira revelação do Espírito Santo.",
                        "A teologia apóstata da Sinagoga de Satanás. (o anátema: Gálatas 1:8-9)."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "5.Em Apocalipse, capítulo 3, verso 7, Jesus é chamado de SANTO e VERDADEIRO. Comparando com 1 Pedro, capítulo 1, verso 15, e com Filipenses, capítulo 4, verso 8, como deve ser nossa maneira de viver?",
                    "opcoes": [
                        "Devemos viver de forma santa e verdadeira, como ensina a Bíblia.",
                        "Nossa vida deve refletir os valores que agradam a Deus: honestidade, pureza, justiça e fidelidade.",
                        "Devemos buscar ter atitudes puras e sinceras, seguindo o exemplo de Jesus em tudo o que fazemos."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
