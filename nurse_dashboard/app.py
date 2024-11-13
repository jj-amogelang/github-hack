from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from collections import Counter

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client.dumelahealth
users_collection = db.users
user_data_collection = db.user_data  # Updated collection name

def get_user_data():
    user_data = user_data_collection.find({}, {'_id': 0, 'id': 1, 'gender': 1, 'age': 1, 'area': 1, 'medical_condition': 1})
    return list(user_data)

@app.route('/')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    username = session.get('username')
    return render_template('dashboard.html', username=username)

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
                return redirect(url_for('dashboard'))
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

@app.route('/api/geographic-data')
def geographic_data():
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

    data = user_data_collection.find(query, {'_id': 0, 'area': 1, 'medical_condition': 1, 'lat': 1, 'lng': 1})
    return jsonify(list(data))

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)