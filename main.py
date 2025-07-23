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
                    "texto": "3.Lendo Apocalipse, capítulo 3, versos 16 e 17, identifique as características da igreja de Laodiceia. Faça a aplicação profética para a igreja dos nossos dias.",
                    "opcoes": [
                        "Igreja morna, rica de bens materiais e pobre de bens espirituais.",    
                        "Uma igreja que não reconhece sua real condição espiritual.",
                        "Igreja indiferente espiritualmente, sem fervor nem compromisso verdadeiro com Deus."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "4.Lendo Apocalipse, capítulo 3, verso 14, identifique quem é o Senhor Jesus.",
                    "opcoes": [
                        "Jesus é aquele que confirma as promessas de Deus, digno de total confiança.",
                        "Jesus é o Amém, a testemunha fiel e verdadeira, o princípio da criação de Deus.",
                        "Jesus é o fundamento de toda a criação e o modelo perfeito de fidelidade ao Pai ."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
