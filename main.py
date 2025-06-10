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
                    "texto": "1.Lendo Apocalipse, capítulo 3, versos 8 e 9, qual a diferença entre razão e revelação, considerando a operação do Espírito de Conhecimento ou Revelação?",
                    "opcoes": [
                        "A revelação é uma porta aberta pelo Senhor para entrar no mistério da salvação e discernir a verdade espiritual. A razão, por outro lado, limita-se ao entendimento natural, que confunde aparência com identidade verdadeira, como os que se diziam judeus mas não eram, por não terem a revelação da Obra do Senhor.",
                        "Revelação: pus diante de ti uma porta aberta. Revelação é da Obra Redentora. Razão: aos que dizem judeus e não são, mas mentem. Razão é da Obra Criadora.",
                        "A revelação vem por meio do Espírito, que abre a porta do entendimento espiritual e mostra o plano da salvação em Jesus (Obra Redentora). Já a razão humana julga pelas aparências e tradições (Obra Criadora), o que leva ao erro, como no caso dos que dizem que são judeus, mas mentem."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "4.Lendo Apocalipse, capítulo 3, verso 8b, o que aconteceu com a igreja de Filadelfia que, mesmo tendo pouca força, guardou a Palavra do Senhor?",
                    "opcoes": [
                        "A igreja de Filadélfia, embora fraca aos olhos humanos, foi fortalecida pelo Espírito de Deus para permanecer fiel. Ela não se rendeu à pressão externa e continuou anunciando Jesus como o único caminho de salvação.",
                        "Mesmo enfrentando limitações e provações, a igreja de Filadélfia permaneceu firme na fé, sustentada pelo Espírito Santo. Ela guardou a Palavra e não se envergonhou de proclamar o nome de Jesus, demonstrando total dependência do Senhor.",
                        "Ela não negou o nome de Jesus, mas confessou que Jesus é o único Salvador, pois o Espírito Santo a fortaleceu."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
