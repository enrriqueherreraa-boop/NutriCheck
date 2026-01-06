from flask import Flask, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("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"))

SYSTEM_PROMPT = """
Eres NutriCheck, un asistente de nutrición profesional, empático y conversacional.

Puedes responder saludos, charlas generales y preguntas de nutrición.
Habla de forma natural, cercana y clara.
Nunca seas cortante ni robótico.
"""

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "NutriCheck API funcionando correctamente"})

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"reply": "¿En qué puedo ayudarte hoy?"})

        response = client.responses.create(
            model="gpt-4o-mini",
            input=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            max_output_tokens=400,
            temperature=0.7
        )

        reply = response.output_text
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({
            "error": "Error en el servidor",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
