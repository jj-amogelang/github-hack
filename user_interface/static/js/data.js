const dataset = {
    // Your dataset here
        "qa_pairs": [
            {
                "question": "hello",
                "answer": "Hello, I am your medical assistant. What would you like assistance with?\n1 - Health\n2 - Mobile Clinic\n3 - Telemedicine"
            },
            {
                "question": "hi",
                "answer": "Hello, I am your medical assistant. What would you like assistance with?\n1 - Health\n2 - Mobile Clinic\n3 - Telemedicine"
            },
    
            // Health Options
            {
                "question": "1",
                "answer": "You selected Health. Please choose a topic:\n1 - Common Illnesses\n2 - Preventive Care\n3 - Mental Health Support\n4 - General Health Tips"
            },
            {
                "question": "health",
                "answer": "You selected Health. Please choose a topic:\n1 - Common Illnesses\n2 - Preventive Care\n3 - Mental Health Support\n4 - General Health Tips"
            },
    
            // Common Illnesses Options
            {
                "question": "1.1",
                "answer": "You selected Common Illnesses. Which one would you like advice on?\n1 - Cold and Flu\n2 - Fever\n3 - Sore Throat\n4 - Headache\n5 - Persistent Cough"
            },
            {
                "question": "common illnesses",
                "answer": "You selected Common Illnesses. Which one would you like advice on?\n1 - Cold and Flu\n2 - Fever\n3 - Sore Throat\n4 - Headache\n5 - Persistent Cough"
            },
    
            {
                "question": "cold and flu",
                "answer": "For cold and flu, rest, stay hydrated, and use over-the-counter medicines as needed. If symptoms persist for more than a week, consider seeing a healthcare provider."
            },
            {
                "question": "fever",
                "answer": "For a fever, stay hydrated, rest, and monitor your temperature. If it’s above 102°F (38.9°C) or lasts more than 3 days, seek medical attention."
            },
            {
                "question": "sore throat",
                "answer": "For a sore throat, try warm salt water gargles, stay hydrated, and use throat lozenges. If symptoms are severe or persist, see a healthcare provider."
            },
            {
                "question": "headache",
                "answer": "For a headache, rest in a quiet, dark room and stay hydrated. If headaches are frequent or severe, consult a healthcare provider."
            },
            {
                "question": "persistent cough",
                "answer": "If you have a persistent cough, stay hydrated and avoid smoke. If it lasts more than two weeks, see a healthcare provider."
            },
    
            // Preventive Care Options
            {
                "question": "2",
                "answer": "You selected Preventive Care. Here are some options:\n1 - Vaccinations\n2 - Annual Check-ups\n3 - Healthy Lifestyle Tips"
            },
            {
                "question": "preventive care",
                "answer": "You selected Preventive Care. Here are some options:\n1 - Vaccinations\n2 - Annual Check-ups\n3 - Healthy Lifestyle Tips"
            },
    
            {
                "question": "vaccinations",
                "answer": "Vaccinations protect you from serious diseases. It’s recommended to stay up-to-date with routine vaccines as advised by your healthcare provider."
            },
            {
                "question": "annual check-ups",
                "answer": "Annual check-ups help detect health issues early. Schedule a check-up at least once a year, even if you feel healthy."
            },
            {
                "question": "healthy lifestyle tips",
                "answer": "A healthy lifestyle includes a balanced diet, regular exercise, adequate sleep, and stress management. Consult a provider for personalized guidance."
            },
    
            // Mental Health Support Options
            {
                "question": "3",
                "answer": "You selected Mental Health Support. Here are some options:\n1 - Managing Stress\n2 - Dealing with Anxiety\n3 - Coping with Depression"
            },
            {
                "question": "mental health support",
                "answer": "You selected Mental Health Support. Here are some options:\n1 - Managing Stress\n2 - Dealing with Anxiety\n3 - Coping with Depression"
            },
    
            {
                "question": "managing stress",
                "answer": "To manage stress, try deep breathing exercises, regular physical activity, and maintain a balanced lifestyle. Speaking to a counselor may also help."
            },
            {
                "question": "dealing with anxiety",
                "answer": "For anxiety, practice mindfulness, avoid caffeine, and consider relaxation techniques. Talking to a mental health professional is also beneficial."
            },
            {
                "question": "coping with depression",
                "answer": "If you're feeling depressed, try to reach out to friends or family. Regular exercise and a balanced diet can help. For persistent symptoms, seek professional help."
            },
    
            // Telemedicine
            {
                "question": "3",
                "answer": "You selected Telemedicine. Here are some options:\n1 - Schedule a Virtual Visit\n2 - Understand Telemedicine Benefits\n3 - Preparing for a Virtual Appointment"
            },
            {
                "question": "telemedicine",
                "answer": "You selected Telemedicine. Here are some options:\n1 - Schedule a Virtual Visit\n2 - Understand Telemedicine Benefits\n3 - Preparing for a Virtual Appointment"
            },
    
            {
                "question": "schedule a virtual visit",
                "answer": "To schedule a virtual visit, check with your healthcare provider for available times. Many clinics allow you to book directly through their website."
            },
            {
                "question": "understand telemedicine benefits",
                "answer": "Telemedicine allows you to consult a provider from the comfort of home, saving travel time and helping prevent exposure to illness."
            },
            {
                "question": "preparing for a virtual appointment",
                "answer": "For a virtual appointment, ensure you have a stable internet connection, a quiet space, and any relevant health records ready."
            },
    
            // Mobile Clinic
            {
                "question": "2",
                "answer": "You selected Mobile Clinic. Here are some options:\n1 - Find a Nearby Mobile Clinic\n2 - Mobile Clinic Services\n3 - How to Access Mobile Clinic Care"
            },
            {
                "question": "mobile clinic",
                "answer": "You selected Mobile Clinic. Here are some options:\n1 - Find a Nearby Mobile Clinic\n2 - Mobile Clinic Services\n3 - How to Access Mobile Clinic Care"
            },
    
            {
                "question": "find a nearby mobile clinic",
                "answer": "To find a nearby mobile clinic, visit your local health department’s website or call their hotline for mobile clinic locations."
            },
            {
                "question": "mobile clinic services",
                "answer": "Mobile clinics offer services like basic health screenings, vaccinations, and routine check-ups. Contact your local clinic for more details."
            },
            {
                "question": "how to access mobile clinic care",
                "answer": "Accessing mobile clinic care typically doesn’t require an appointment. Walk-in services are often available, but call ahead to confirm."
            },
    
            // Fallback Response
            {
                "question": "default",
                "answer": "I'm sorry, I didn't understand that. Please respond with the number or keyword for an option. Type 'hello' to restart if needed."
            }
        ]
};

function sendUserInput(question, answer) {
    fetch('/store-input', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: question, answer: answer })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Example usage
sendUserInput("hello", "Hello, I am your medical assistant. What would you like assistance with?\n1 - Health\n2 - Mobile Clinic\n3 - Telemedicine");