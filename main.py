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
                    "texto": "1.Ao ler Apocalipse 19:13, qual é a relação entre as vestes de Jesus, que estão salpicadas de sangue, e o Seu nome, A Palavra de Deus?.",
                    "opcoes": [
                        "As vestes salpicadas de sangue simbolizam o sacrifício de Jesus na cruz, através do qual Ele redimiu a humanidade. Esse sangue representa o preço pago pela salvação, confirmando que A Palavra de Deus se fez carne e se entregou por amor (João 1:14).",    
                        "O sangue em Suas vestes também indica o juízo de Deus sobre o pecado. Jesus, como a Palavra de Deus, executa justiça divina e vence o mal o sangue representa a vitória sobre os inimigos espirituais (Isaías 63:2-3).",
                        "O título A Palavra de Deus revela que Jesus é a manifestação viva da vontade e do poder de Deus. Suas vestes salpicadas de sangue mostram que essa Palavra não é apenas falada, mas cumprida com autoridade e sacrifício, revelando tanto graça quanto juízo."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "4.Leia Rute 1:16 e responda: Qual foi a escolha de Rute Quando Noemi descidiu voltar para Belem?",
                    "opcoes": [
                        "Rute escolheu permanecer ao lado de Noemi, recusando-se a deixá-la mesmo diante das dificuldades.",
                        "Ela decidiu deixar sua terra natal, Moabe, para acompanhar Noemi e viver em Belém, demonstrando amor e lealdade.",
                        "Rute escolheu servir ao Deus de Israel, declarando: O teu povo é o meu povo, e o teu Deus é o meu Deus, revelando sua fé e compromisso com o Senhor."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
