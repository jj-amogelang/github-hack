# app.py
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from ibm_watson import ApiException, LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
db = client['chat_assistant_db']
user_inputs_collection = db['user_inputs']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-started')
def get_started():
    return render_template('get_started.html')

@app.route('/chat-assistant')
def chat_assistant():
    return render_template('chat_assistant.html')

# Replace 'YOUR_API_KEY' and 'YOUR_URL' with the credentials from your IBM Watson NLU service
apikey = "IlVVJIRsM6D6cZeIHHUkjiaXAPOC-2AjpxpjgzQmVbxQ"
url = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/9aaf3279-dee8-434c-9fb2-488700a38341"

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-08-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

@app.route('/generate-text', methods=['POST'])
def generate_text():
    data = request.get_json()
    prompt = data['prompt']
    source_language = 'en'  # Replace with the source language code of your prompt (e.g., 'en' for English)
    target_language = 'en'  # Replace with the target language code for generating text (e.g., 'es' for Spanish)

    try:
        response = language_translator.translate(
            text=prompt,
            source=source_language,
            target=target_language
        ).get_result()
        
        generated_text = response['translations'][0]['translation']
        return jsonify({'generated_text': generated_text})
    
    except ApiException as e:
        return jsonify({'error': str(e)})
    
@app.route('/store-input', methods=['POST'])
def store_input():
    user_input = request.json
    user_inputs_collection.insert_one(user_input)
    return jsonify({"status": "success"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)