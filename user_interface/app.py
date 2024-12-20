# app.py
from flask import Flask, render_template, jsonify, request, redirect, url_for, session, flash
from pymongo import MongoClient
from ibm_watson import ApiException, LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from collections import Counter
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
db = client['dumelahealth']
user_inputs_collection = db['user_inputs']
users_collection = db['users']
user_data_collection = db['user_data']  # Updated collection name

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-started')
def get_started():
    return render_template('get_started.html')

@app.route('/dashboard')
def dashboard_view():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    # Fetch data from MongoDB
    data = list(user_data_collection.find({}, {'_id': 0, 'date': 1, 'medical_condition': 1, 'gender': 1, 'age': 1, 'area': 1}))

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Total number of cases reported
    total_cases = len(df)

    # Number of active cases by condition
    active_cases = df['medical_condition'].value_counts().to_dict()

    # Cases by gender and age groups
    cases_by_gender_age = df.groupby(['gender', pd.cut(df['age'], bins=[0, 18, 35, 50, 100])]).size().unstack(fill_value=0).to_dict()

    # Most affected areas
    most_affected_areas = df['area'].value_counts().to_dict()

    # Recent activity (for demonstration purposes, we'll just use the last 5 entries)
    recent_activities = df.tail(5).to_dict(orient='records')

    username = session.get('username')
    return render_template('dashboard.html', username=username, total_cases=total_cases, active_cases=active_cases, cases_by_gender_age=cases_by_gender_age, most_affected_areas=most_affected_areas, recent_activities=recent_activities)

@app.route('/chat-assistant')
def chat_assistant():
    return render_template('chat_assistant.html')

@app.route('/geographic')
def geographic():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('geographic.html')

@app.route('/user-data')
def user_data():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    users = get_user_data()
    return render_template('user_data.html', users=users)

@app.route('/ai-insights')
def ai_insights():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('ai_insights.html')

@app.route('/notifications')
def notifications():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('notifications.html')

@app.route('/image-analysis')
def image_analysis():
    return render_template('image_analysis.html')

@app.route('/analyze-image', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return redirect(request.url)
    
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Perform image analysis (placeholder logic)
        result = "Potential diagnosis: Example Skin Condition"
        
        return render_template('image_analysis.html', result=result)

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

@app.route('/api/store-user-data', methods=['POST'])
def store_user_data():
    data = request.json
    print('Received data:', data)  # Debugging log
    user_inputs_collection.insert_one({
        'id': data['id'],
        'gender': data['gender'],
        'age': data['age'],
        'area': data['area'],
        'medical_condition': data['medical_condition'],
        'longitude': data['longitude'],
        'latitude': data['latitude'],
        'date': datetime.fromisoformat(data['date'])
    })
    return jsonify({'message': 'Your data has been stored successfully.'})

def get_user_data():
    user_data = user_data_collection.find({}, {'_id': 0, 'id': 1, 'gender': 1, 'age': 1, 'area': 1, 'medical_condition': 1})
    return list(user_data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users_collection.find_one({'username': username})
        if user:
            if check_password_hash(user['password'], password):
                session['logged_in'] = True
                session['username'] = username
                return redirect(url_for('dashboard_view'))
            else:
                flash('Invalid password')
        else:
            flash('Invalid username')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        users_collection.insert_one({
            'username': username,
            'email': email,
            'password': hashed_password
        })
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/api/top-affected-regions')
def top_affected_regions():
    time_period = request.args.get('time_period', 'daily')
    condition = request.args.get('condition', 'all')

    query = {}
    if condition != 'all':
        query['medical_condition'] = condition

    if time_period == 'daily':
        start_date = datetime.now() - timedelta(days=1)
    elif time_period == 'weekly':
        start_date = datetime.now() - timedelta(weeks=1)

    query['date'] = {'$gte': start_date}

    data = user_data_collection.find(query, {'_id': 0, 'area': 1, 'medical_condition': 1})
    counter = Counter((item['area'], item['medical_condition']) for item in data)
    top_regions = [{'area': area, 'medical_condition': condition, 'count': count} for (area, condition), count in counter.items()]
    top_regions.sort(key=lambda x: x['count'], reverse=True)
    return jsonify(top_regions)


@app.route('/api/conditions_by_region', methods=['GET'])
def get_conditions_by_region():
    pipeline = [
        {
            '$group': {
                '_id': {
                    'region': '$area',
                    'medical_condition': '$medical_condition',
                    'lat': '$lat',
                    'lng': '$lng'
                },
                'count': {'$sum': 1}
            }
        },
        {
            '$sort': {'count': -1}
        }
    ]
    result = user_data_collection.aggregate(pipeline)
    data = []
    for doc in result:
        data.append({
            'region': doc['_id']['region'],
            'medical_condition': doc['_id']['medical_condition'],
            'lat': doc['_id']['lat'],
            'lng': doc['_id']['lng'],
            'count': doc['count']
        })
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
