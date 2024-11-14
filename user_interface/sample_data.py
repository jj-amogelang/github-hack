from pymongo import MongoClient
from datetime import datetime, timedelta
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import seaborn as sns

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
db = client['dumelahealth']
user_data_collection = db['user_data']  # Updated collection name

# Sample data
user_data = [
    {'id': 1, 'gender': 'Female', 'age': 40, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=1)},
    {'id': 2, 'gender': 'Female', 'age': 35, 'area': 'Soweto', 'medical_condition': 'Diabetes', 'lat': -26.2485, 'lng': 27.8540, 'date': datetime.now() - timedelta(days=1)},
    {'id': 3, 'gender': 'Female', 'age': 45, 'area': 'Tembisa', 'medical_condition': 'Asthma', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=1)},
    {'id': 4, 'gender': 'Female', 'age': 28, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=1)},
    {'id': 5, 'gender': 'Male', 'age': 36, 'area': 'Diepsloot', 'medical_condition': 'Respiratory Infection', 'lat': -25.9333, 'lng': 28.0125, 'date': datetime.now() - timedelta(days=2)},
    {'id': 6, 'gender': 'Male', 'age': 33, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=3)},
    {'id': 7, 'gender': 'Male', 'age': 38, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=3)},
    {'id': 8, 'gender': 'Female', 'age': 29, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=3)},
    {'id': 9, 'gender': 'Female', 'age': 31, 'area': 'Alexandra', 'medical_condition': 'Fever', 'lat': -26.1036, 'lng': 28.0895, 'date': datetime.now() - timedelta(days=3)},
    {'id': 10, 'gender': 'Female', 'age': 27, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=3)},
    {'id': 11, 'gender': 'Male', 'age': 50, 'area': 'Orange Farm', 'medical_condition': 'Hypertension', 'lat': -26.4833, 'lng': 27.8667, 'date': datetime.now() - timedelta(days=4)},
    {'id': 12, 'gender': 'Male', 'age': 42, 'area': 'Soweto', 'medical_condition': 'Asthma', 'lat': -26.2485, 'lng': 27.8540, 'date': datetime.now() - timedelta(days=4)},
    {'id': 13, 'gender': 'Male', 'age': 33, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=4)},
    {'id': 14, 'gender': 'Male', 'age': 26, 'area': 'Alexandra', 'medical_condition': 'Respiratory Infection', 'lat': -26.1036, 'lng': 28.0895, 'date': datetime.now() - timedelta(days=4)},
    {'id': 15, 'gender': 'Male', 'age': 48, 'area': 'Diepsloot', 'medical_condition': 'Fever', 'lat': -25.9333, 'lng': 28.0125, 'date': datetime.now() - timedelta(days=4)},
    {'id': 16, 'gender': 'Female', 'age': 39, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=4)},
    {'id': 17, 'gender': 'Male', 'age': 35, 'area': 'Soweto', 'medical_condition': 'Asthma', 'lat': -26.2485, 'lng': 27.8540, 'date': datetime.now() - timedelta(days=5)},
    {'id': 18, 'gender': 'Female', 'age': 30, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=5)},
    {'id': 19, 'gender': 'Male', 'age': 32, 'area': 'Alexandra', 'medical_condition': 'Respiratory Infection', 'lat': -26.1036, 'lng': 28.0895, 'date': datetime.now() - timedelta(days=5)},
    {'id': 20, 'gender': 'Female', 'age': 50, 'area': 'Diepsloot', 'medical_condition': 'Fever', 'lat': -25.9333, 'lng': 28.0125, 'date': datetime.now() - timedelta(days=6)},
    {'id': 21, 'gender': 'Female', 'age': 29, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=6)},
    {'id': 22, 'gender': 'Male', 'age': 41, 'area': 'Soweto', 'medical_condition': 'Asthma', 'lat': -26.2485, 'lng': 27.8540, 'date': datetime.now() - timedelta(days=6)},
    {'id': 23, 'gender': 'Female', 'age': 34, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=6)},
    {'id': 24, 'gender': 'Male', 'age': 37, 'area': 'Alexandra', 'medical_condition': 'Respiratory Infection', 'lat': -26.1036, 'lng': 28.0895, 'date': datetime.now() - timedelta(days=6)},
    {'id': 25, 'gender': 'Female', 'age': 28, 'area': 'Diepsloot', 'medical_condition': 'Fever', 'lat': -25.9333, 'lng': 28.0125, 'date': datetime.now() - timedelta(days=7)},
    {'id': 26, 'gender': 'Male', 'age': 45, 'area': 'Orange Farm', 'medical_condition': 'Hypertension', 'lat': -26.4833, 'lng': 27.8667, 'date': datetime.now() - timedelta(days=7)},
    {'id': 27, 'gender': 'Female', 'age': 36, 'area': 'Soweto', 'medical_condition': 'Asthma', 'lat': -26.2485, 'lng': 27.8540, 'date': datetime.now() - timedelta(days=7)},
    {'id': 28, 'gender': 'Male', 'age': 39, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=7)},
    {'id': 29, 'gender': 'Female', 'age': 31, 'area': 'Alexandra', 'medical_condition': 'Respiratory Infection', 'lat': -26.1036, 'lng': 28.0895, 'date': datetime.now() - timedelta(days=7)},
    {'id': 30, 'gender': 'Female', 'age': 36, 'area': 'Soweto', 'medical_condition': 'Asthma', 'lat': -26.2485, 'lng': 27.8540, 'date': datetime.now() - timedelta(days=10)},
    {'id': 31, 'gender': 'Male', 'age': 33, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'date': datetime.now() - timedelta(days=10)}
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

print(f"Active Cases by Condition: {active_cases}")
print(f"Cases by Gender and Age Groups: {cases_by_gender_age}")
print(f"Most Affected Areas: {most_affected_areas}")
print(f"Recent Activities: {recent_activities}")

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter data for the past 3 days
df_recent = df[df['date'] >= (datetime.now() - timedelta(days=3))]

# Group by date and medical condition, and count occurrences
df_grouped = df_recent.groupby([df['date'].dt.date, 'medical_condition']).size().reset_index(name='count')

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
future = model.make_future_dataframe(periods=7)  # Predict for the next 7 days
forecast = model.predict(future)

# Plot the forecast
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
model.plot(forecast)
plt.title('Diabetes Cases Forecast')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.show()

# Display the forecasted data
forecast_table = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(7)
forecast_table.columns = ['Date', 'Predicted Cases', 'Lower Bound', 'Upper Bound']
print(forecast_table.to_string(index=False))
