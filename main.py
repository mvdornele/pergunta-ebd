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
                    "texto": "1. Identifique a relação profética entre Apocalipse, capítulo 3, verso 16, e Mateus, capítulo 13,verso 48, quanto à operação do Espírito de Temor na igreja de Laodiceia",
                    "opcoes": [
                        "A relação profética está em uma igreja lançada fora do corpo, tal como os peixes ruins lançados fora do cesto. Uma igreja que perdeu o temor do Senhor. ",    
                        "A igreja de Laodiceia representa um grupo que perdeu o temor do Senhor, tornando-se indiferente espiritualmente, como os peixes ruins que são rejeitados no juízo final.",
                        "Assim como os peixes ruins foram lançados fora por não servirem ao propósito, a igreja morna de Laodiceia é rejeitada por ter perdido o zelo e o temor diante de Deus."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "3. Leia Provérbios, capítulo 1, verso 7 e Eclesiastes, capítulo 12, verso 13, e responda: O que o servo de Deus deve ter no coração desde o começo até o fim da sua vida?",
                    "opcoes": [
                        "O temor do Senhor deve estar presente em toda a caminhada do servo de Deus, desde o início até o fim.",
                        "O servo de Deus deve ter o temor do Senhor no coração.",
                        "Desde o começo da sua vida até o fim, o servo de Deus deve guardar no coração o temor e a obediência ao Senhor."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
