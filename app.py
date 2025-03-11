from flask import Flask, request, jsonify
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Load the frontend

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    bot_response = f"I understand: {user_input}"  # Dummy response
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)

import openai
import mysql.connector
import bcrypt

app = Flask(__name__)

# OpenAI API Key
openai.api_key = "your_openai_api_key"

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aatma123#",
    database="chatbot_db"
)
cursor = db.cursor()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    
    # OpenAI Chatbot Response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    
    bot_response = response['choices'][0]['message']['content']

    # Store conversation in MySQL
    cursor.execute("INSERT INTO chat_logs (user_message, bot_response) VALUES (%s, %s)", (user_input, bot_response))
    db.commit()
    
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
