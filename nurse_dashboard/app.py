from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/geographic')
def geographic():
    return render_template('geographic.html')

@app.route('/user-data')
def user_data():
    return render_template('user_data.html')

@app.route('/ai-insights')
def ai_insights():
    return render_template('ai_insights.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')  


if __name__ == '__main__':
    app.run(debug=True, port=5000)