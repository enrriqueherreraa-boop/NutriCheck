from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Creamos el cliente usando la clave que guardaste en Render
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/", methods=["GET"])
def home():
    return "NutriCheck API funcionando correctamente con IA."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    # Mandamos el mensaje del usuario a la IA
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=user_message
    )

    ai_reply = response.output_text

    return jsonify({"reply": ai_reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
