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
                    "texto": "1. Ao ler Apocalipse, capítulo 2, verso 1, identifique o significado profético de cada título dado ao Senhor Jesus. Faça a aplicação na vida da igreja a) Aquele que tem na sua destra as sete estrelas. b) Aquele que anda no meio dos sete castiçais de ouro.",
                    "opcoes": [
                        "A plena operação do Espírito Santo na igreja sob o governo do Senhor Jesus.",    
                        "A presença do Senhor Jesus na Igreja em todos os 7 períodos de sua existência.",
                        "A igreja deve reconhecer que toda autoridade espiritual provém de Cristo."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "3. Leia 1 Samuel, capítulo 17, verso 45, e responda: O que havia no coração de Davi quando foi lutar contra o gigante Golias?",
                    "opcoes": [
                        "A fé verdadeira. Davi confiava em Deus, que é o Senhor dos Exércitos.",
                        "A coragem que vem do Espírito de Deus.",
                        "O zelo pela honra do nome do Senhor."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
