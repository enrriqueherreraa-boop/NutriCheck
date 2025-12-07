from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "NutriCheck API funcionando correctamente."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    # Respuesta temporal (luego conectaremos ChatGPT)
    response = f"Recibido: {user_message}. Pronto te daré una respuesta inteligente."

    return jsonify({"reply": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
