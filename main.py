from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def home():
    return "NutriCheck API funcionando correctamente"

@app.route("/nutricionista", methods=["POST"])
def nutricionista():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"error": "Falta el mensaje del usuario"}), 400

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": (
                    "Eres NutriCheck IA, un profesional nutricionista para niños. "
                    "Das respuestas claras, responsables y basadas en ciencia, sin reemplazar a un médico real. "
                    "Siempre mantienes un tono amigable, educativo y respetuoso."
                )
            },
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7
    }

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post("https://api.openai.com/v1/chat/completions",
                             json=data, headers=headers)

    return jsonify(response.json())


if __name__ == "__main__":
    app.run(port=5000)
