from pymongo import MongoClient
from datetime import datetime, timedelta

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
    {'id': 41, 'gender': 'Female', 'age': 30, 'area': 'Tembisa', 'medical_condition': 'Diabetes', 'lat': -25.9964, 'lng': 28.2268, 'lng': 28.0895, 'date': datetime.now() - timedelta(days=41)},
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
