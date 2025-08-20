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
                    "texto": "1.Em Apocalipse, capitulo 1, verso 4, o senhor Jesus e apresentado como; ...aquele que é, e que era, e que há de vir.... Identifique o sentido profético desta expressão e o que ela representa para a sua vida espiritual.",
                    "opcoes": [
                        "O sentido profético desta expressão mostra a eternidade e a imutabilidade do Senhor Jesus. Ele é o mesmo ontem, hoje e para sempre, o que dá segurança à nossa fé.Para minha vida espiritual, isso representa confiança",    
                        "Aquele que é, que era e que há de vir, revela que o Senhor Jesus está presente em toda a história: Ele já atuava no passado, governa o presente e virá em glória no futuro.",
                        "O sentido profético mostra que Jesus é o Senhor do tempo e da eternidade. Ele transcende passado, presente e futuro, e anuncia Sua volta gloriosa. Para minha vida espiritual, isso representa esperança."
                    ]
                }
            ],
            "para_cias": [
                {
                    "texto": "4. Leia 1º Samuel, capítulo 16, verso 18 e responda: Davi dava um bom testemunho? Quais as caracteristicas que o identificavam?",
                    "opcoes": [
                        "Sim, Davi dava um bom testemunho. Ele era descrito como valente, forte e homem de guerra, além de tocar bem a harpa. Essas características mostravam que ele tinha coragem, habilidade e dedicação em tudo o que fazia.",
                        "Davi dava um bom testemunho porque era conhecido como homem cuidadoso nas palavras e de boa aparência, além de ter o Senhor com ele. Isso mostra que seu testemunho não estava apenas em suas capacidades, mas principalmente na presença de Deus em sua vida.",
                        "As características que identificavam Davi eram: sabedoria, coragem, habilidade musical, prudência no falar e a presença do Espírito do Senhor em sua vida. Isso fazia dele alguém diferenciado, que inspirava confiança e demonstrava fidelidade a Deus."
                    ]
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
