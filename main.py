from flask import Flask, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

system_prompt = """
Eres NutriCheck, un asistente de nutrición profesional, empático y conversacional.

Tu función principal es ayudar a los usuarios con temas de nutrición, salud y hábitos alimenticios.
También puedes responder saludos, despedidas y mensajes generales de forma amable y natural.

Si el usuario hace una pregunta que no está relacionada con nutrición:
- Responde brevemente y con educación
- Mantén un tono humano
- Redirige suavemente la conversación hacia la salud o alimentación

Adapta la longitud de tus respuestas:
- Mensajes simples → respuestas cortas y amigables
- Preguntas de salud → respuestas claras y más detalladas

Habla de forma cercana y natural.
Nunca respondas de manera cortante o robótica.
"""

@app.route("/", methods=["GET"])
def home():
    return "NutriCheck API funcionando correctamente con IA."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7,
        max_tokens=400,
        presence_penalty=0.3,
        frequency_penalty=0.2
    )

    ai_reply = completion.choices[0].message["content"]

    return jsonify({"reply": ai_reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
