# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-started')
def get_started():
    return render_template('get_started.html')

@app.route('/chat-assistant')
def chat_assistant():
    return render_template('chat_assistant.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)