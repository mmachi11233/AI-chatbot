from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API Key (Replace with your actual key)
OPENAI_API_KEY = "SECRET KEY"
openai.api_key = OPENAI_API_KEY

# Store chat history (can be replaced with a database)
chat_history = []

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Append user message to chat history
    chat_history.append({"role": "user", "content": user_input})

    # Limit history to last 5 exchanges
    if len(chat_history) > 10:
        chat_history.pop(0)

    # Get AI response
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful AI assistant."}] + chat_history,
    )

    ai_response = response["choices"][0]["message"]["content"]

    # Append AI response to chat history
    chat_history.append({"role": "assistant", "content": ai_response})

    return jsonify({"reply": ai_response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
