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
                    "texto": "2.Considerando as sete operações do Espírito de Deus, que lemos em Isaías, capítulo 11, verso 2, qual a designação do que a Igreja Fiel tem que fazer para estar alinhada com o Tempo do Breve?",
                    "opcoes": [
                        "A Igreja deve se fundamentar no estudo teológico e filosófico das Escrituras, como forma de alcançar a plenitude espiritual    .",
                        "A Igreja precisa aguardar passivamente o cumprimento das profecias, sem se envolver com revelações espirituais, pois tudo será esclarecido no arrebatamento.",
                        "A Igreja precisa viver a experiência com o Espírito de Revelação. Ela precisa estar preparada para viver os Mistérios. Ela não pode mais viver da razão, da teologia, da filosofia."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "4.Lendo Mateus, capítulo 13, versos 31 e 32, comparando com Mateus, capítulo 17, verso 20,como podemos ter as nossas orações respondidas?",
                    "opcoes": [
                        "As orações só são respondidas quando alcançamos uma fé perfeita, sem dúvidas ou falhas, pois Deus só ouve os que já estão espiritualmente maduros.",
                        "Se tivermos fé, mesmo que pequena como um grão de mostarda, podemos orar a Deus e seremos atendidos.",
                        "Para que as orações sejam atendidas, é necessário jejuar e repetir palavras com insistência, até convencer a Deus a agir."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
