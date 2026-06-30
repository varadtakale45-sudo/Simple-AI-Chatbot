from flask import Flask, render_template, request, jsonify
import random
import datetime

app = Flask(__name__)

responses = {
    "greeting": [
        "Hello! 👋",
        "Hi there!",
        "Hey! How can I help?"
    ],
    "python": [
        "Python is a powerful programming language."
    ],
    "ai": [
        "AI stands for Artificial Intelligence."
    ],
    "flask": [
        "Flask is a lightweight Python web framework."
    ],
    "bye": [
        "Goodbye! 👋",
        "See you soon!"
    ]
}


def chatbot(message):
    msg = message.lower()

    if any(word in msg for word in ["hi", "hello", "hey"]):
        return random.choice(responses["greeting"])

    elif "python" in msg:
        return random.choice(responses["python"])

    elif "ai" in msg:
        return random.choice(responses["ai"])

    elif "flask" in msg:
        return random.choice(responses["flask"])

    elif "time" in msg:
        return "Current Time: " + datetime.datetime.now().strftime("%I:%M %p")

    elif "date" in msg:
        return "Today's Date: " + str(datetime.date.today())

    elif "name" in msg:
        return "I'm your AI Chatbot."

    elif "bye" in msg:
        return random.choice(responses["bye"])

    else:
        return "Sorry, I don't understand that yet."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    message = request.json["message"]
    reply = chatbot(message)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)