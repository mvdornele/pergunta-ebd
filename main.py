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
                    "texto": "2.Ao comparar Apocalipse 22:5 com João 8:12, qual é a promessa para aquele que segue Jesus? Faça a relação profética.",
                    "opcoes": [
                        "Promessa de Luz Eterna: Em Apocalipse 22:5, está escrito que não haverá mais noite, e não necessitarão de lâmpada nem de luz do sol, porque o Senhor Deus os alumia.",    
                        "Promessa de Vida e Direção:Em João 8:12, Jesus promete que quem o segue terá a luz da vida, e em Apocalipse 22:5 essa vida é plena e eterna, pois os salvos reinarão para sempre com Deus.",
                        "Promessa de Reinado e Glória Eterna: Apocalipse 22:5 afirma que reinarão para todo o sempre, mostrando a vitória final dos que permaneceram fiéis à luz de Cristo."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "4.Leia Rute 2:2 e responda, O que Rute foi fazer no campo e o que aconteceu com ela?",
                    "opcoes": [
                        "Rute foi respigar espigas de trigo. Ela pediu permissão para ir aos campos e recolher as espigas que caíam durante a colheita, para que ela e Noemi tivessem alimento Rute 2:2.",
                        "Rute encontrou favor diante de Boaz.Enquanto trabalhava, Rute foi notada por Boaz, que era um homem justo e parente de Noemi. Ele tratou Rute com bondade e lhe concedeu proteção e provisão Rute 2:8-9.",
                        "Deus começou a mudar a história de Rute. A partir desse encontro, iniciou-se o plano de Deus para restaurar sua vida, resultando futuramente em seu casamento com Boaz e em sua inclusão na linhagem de Jesus Cristo Mateus 1:5."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
