import pandas as pd
from pymongo import MongoClient
from datetime import datetime, timedelta
from prophet import Prophet

# Establish connection to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.dumelahealth
user_data_collection = db.user_data

# Sample data with 50 sets of data
user_data = [
    {'id': 1, 'gender': 'Male', 'age': 30, 'area': 'Alexandra', 'medical_condition': 'Respiratory Infection', 'lat': -26.1036, 'lng': 28.0895, 'date': datetime.now() - timedelta(days=1)},
    {'id': 2, 'gender': 'Female', 'age': 25, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=2)},
    {'id': 3, 'gender': 'Female', 'age': 40, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=3)},
    {'id': 4, 'gender': 'Female', 'age': 35, 'area': 'Soweto', 'medical_condition': 'Diabetes', 'lat': -26.2485, 'lng': 27.8540, 'date': datetime.now() - timedelta(days=4)},
    {'id': 5, 'gender': 'Female', 'age': 45, 'area': 'Tembisa', 'medical_condition': 'Asthma', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=5)},
    {'id': 6, 'gender': 'Female', 'age': 28, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=6)},
    {'id': 7, 'gender': 'Male', 'age': 36, 'area': 'Diepsloot', 'medical_condition': 'Respiratory Infection', 'lat': -25.9333, 'lng': 28.0125, 'date': datetime.now() - timedelta(days=7)},
    {'id': 8, 'gender': 'Male', 'age': 33, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=8)},
    {'id': 9, 'gender': 'Male', 'age': 38, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=9)},
    {'id': 10, 'gender': 'Female', 'age': 29, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=10)},
    {'id': 11, 'gender': 'Female', 'age': 31, 'area': 'Alexandra', 'medical_condition': 'Fever', 'lat': -26.1036, 'lng': 28.0895, 'date': datetime.now() - timedelta(days=11)},
    {'id': 12, 'gender': 'Female', 'age': 27, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=12)},
    {'id': 13, 'gender': 'Male', 'age': 50, 'area': 'Orange Farm', 'medical_condition': 'Hypertension', 'lat': -26.4833, 'lng': 27.8667, 'date': datetime.now() - timedelta(days=13)},
    {'id': 14, 'gender': 'Male', 'age': 42, 'area': 'Soweto', 'medical_condition': 'Asthma', 'lat': -26.2485, 'lng': 27.8540, 'date': datetime.now() - timedelta(days=14)},
    {'id': 15, 'gender': 'Male', 'age': 33, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=15)},
    {'id': 16, 'gender': 'Male', 'age': 26, 'area': 'Alexandra', 'medical_condition': 'Respiratory Infection', 'lat': -26.1036, 'lng': 28.0895, 'date': datetime.now() - timedelta(days=16)},
    {'id': 17, 'gender': 'Male', 'age': 48, 'area': 'Diepsloot', 'medical_condition': 'Fever', 'lat': -25.9333, 'lng': 28.0125, 'date': datetime.now() - timedelta(days=17)},
    {'id': 18, 'gender': 'Female', 'age': 39, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=18)},
    {'id': 19, 'gender': 'Male', 'age': 35, 'area': 'Soweto', 'medical_condition': 'Asthma', 'lat': -26.2485, 'lng': 27.8540, 'date': datetime.now() - timedelta(days=19)},
    {'id': 20, 'gender': 'Female', 'age': 30, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=20)},
    {'id': 21, 'gender': 'Male', 'age': 32, 'area': 'Alexandra', 'medical_condition': 'Respiratory Infection', 'lat': -26.1036, 'lng': 28.0895, 'date': datetime.now() - timedelta(days=21)},
    {'id': 22, 'gender': 'Female', 'age': 50, 'area': 'Diepsloot', 'medical_condition': 'Fever', 'lat': -25.9333, 'lng': 28.0125, 'date': datetime.now() - timedelta(days=22)},
    {'id': 23, 'gender': 'Female', 'age': 29, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=23)},
    {'id': 24, 'gender': 'Male', 'age': 41, 'area': 'Soweto', 'medical_condition': 'Asthma', 'lat': -26.2485, 'lng': 27.8540, 'date': datetime.now() - timedelta(days=24)},
    {'id': 25, 'gender': 'Female', 'age': 34, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=25)},
    {'id': 26, 'gender': 'Male', 'age': 37, 'area': 'Alexandra', 'medical_condition': 'Respiratory Infection', 'lat': -26.1036, 'lng': 28.0895, 'date': datetime.now() - timedelta(days=26)},
    {'id': 27, 'gender': 'Female', 'age': 28, 'area': 'Diepsloot', 'medical_condition': 'Fever', 'lat': -25.9333, 'lng': 28.0125, 'date': datetime.now() - timedelta(days=27)},
    {'id': 28, 'gender': 'Male', 'age': 45, 'area': 'Orange Farm', 'medical_condition': 'Hypertension', 'lat': -26.4833, 'lng': 27.8667, 'date': datetime.now() - timedelta(days=28)},
    {'id': 29, 'gender': 'Female', 'age': 36, 'area': 'Soweto', 'medical_condition': 'Asthma', 'lat': -26.2485, 'lng': 27.8540, 'date': datetime.now() - timedelta(days=29)},
    {'id': 30, 'gender': 'Male', 'age': 39, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=30)},
    {'id': 31, 'gender': 'Female', 'age': 31, 'area': 'Alexandra', 'medical_condition': 'Respiratory Infection', 'lat': -26.1036, 'lng': 28.0895, 'date': datetime.now() - timedelta(days=31)},
    {'id': 32, 'gender': 'Male', 'age': 29, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=32)},
    {'id': 33, 'gender': 'Female', 'age': 42, 'area': 'Orange Farm', 'medical_condition': 'Hypertension', 'lat': -26.4833, 'lng': 27.8667, 'date': datetime.now() - timedelta(days=33)},
    {'id': 34, 'gender': 'Male', 'age': 38, 'area': 'Soweto', 'medical_condition': 'Asthma', 'lat': -26.2485, 'lng': 27.8540, 'date': datetime.now() - timedelta(days=34)},
    {'id': 35, 'gender': 'Female', 'age': 33, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=35)},
    {'id': 36, 'gender': 'Male', 'age': 27, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=36)},
    {'id': 37, 'gender': 'Female', 'age': 26, 'area': 'Diepsloot', 'medical_condition': 'Fever', 'lat': -25.9333, 'lng': 28.0125, 'date': datetime.now() - timedelta(days=37)},
    {'id': 38, 'gender': 'Male', 'age': 44, 'area': 'Orange Farm', 'medical_condition': 'Hypertension', 'lat': -26.4833, 'lng': 27.8667, 'date': datetime.now() - timedelta(days=38)},
    {'id': 39, 'gender': 'Female', 'age': 35, 'area': 'Soweto', 'medical_condition': 'Asthma', 'lat': -26.2485, 'lng': 27.8540, 'date': datetime.now() - timedelta(days=39)},
    {'id': 40, 'gender': 'Male', 'age': 32, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=40)},
    {'id': 41, 'gender': 'Female', 'age': 30, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.0895, 'date': datetime.now() - timedelta(days=41)},
    {'id': 42, 'gender': 'Male', 'age': 28, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=42)},
    {'id': 43, 'gender': 'Female', 'age': 43, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=43)},
    {'id': 44, 'gender': 'Male', 'age': 37, 'area': 'Soweto', 'medical_condition': 'Asthma', 'lat': -26.2485, 'lng': 27.8540, 'date': datetime.now() - timedelta(days=44)},
    {'id': 45, 'gender': 'Female', 'age': 34, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=45)},
    {'id': 46, 'gender': 'Male', 'age': 31, 'area': 'Alexandra', 'medical_condition': 'Respiratory Infection', 'lat': -26.1036, 'lng': 28.0895, 'date': datetime.now() - timedelta(days=46)},
    {'id': 47, 'gender': 'Female', 'age': 27, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=47)},
    {'id': 48, 'gender': 'Male', 'age': 46, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=48)},
    {'id': 49, 'gender': 'Female', 'age': 36, 'area': 'Soweto', 'medical_condition': 'Asthma', 'lat': -26.2485, 'lng': 27.8540, 'date': datetime.now() - timedelta(days=49)},
    {'id': 50, 'gender': 'Male', 'age': 33, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=50)}
]

# Insert sample data into the collection
user_data_collection.insert_many(user_data)

print("Sample data inserted successfully.")

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

# Print the calculated metrics
print(f"Total Cases: {total_cases}")
print(f"Active Cases by Condition: {active_cases}")
print(f"Cases by Gender and Age Groups: {cases_by_gender_age}")
print(f"Most Affected Areas: {most_affected_areas}")
print(f"Recent Activities: {recent_activities}")

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Group by date and medical condition, and count occurrences
df_grouped = df.groupby([df['date'].dt.date, 'medical_condition']).size().reset_index(name='count')

# Pivot the DataFrame to have dates as index and medical conditions as columns
df_pivot = df_grouped.pivot(index='date', columns='medical_condition', values='count').fillna(0)

print(df_pivot.head())

# Prepare the data for Prophet
df_prophet = df_grouped[df_grouped['medical_condition'] == 'Diabetes'][['date', 'count']]
df_prophet.columns = ['ds', 'y']

# Initialize and train the model
model = Prophet()
model.fit(df_prophet)

# Make future predictions
future = model.make_future_dataframe(periods=30)  # Predict for the next 30 days
forecast = model.predict(future)

# Plot the forecast
fig = model.plot(forecast)
fig.show()
