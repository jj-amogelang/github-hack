// List of severe conditions 
const severeConditions = [
    "Respiratory Infection",
    "Diabetes",
    "Asthma",
    "Hypertension"
];

const areaCoordinates = {
    "tembisa": { "lng": 28.2184, "lat": -25.9964 },
    "orange farm": { "lng": 27.8576, "lat": -26.4833 },
    "soweto": { "lng": 27.8540, "lat": -26.2485 },
    "alexandra": { "lng": 28.1000, "lat": -26.1036 },
    "diepsloot": { "lng": 28.0126, "lat": -25.9333 }
};

let chatStep = 0; // Track steps in the booking process
let gender, age, area; // Declare variables to store user input

function sendMessage() {
    const userInput = document.getElementById("user-input").value.toLowerCase().trim();
    document.getElementById("chat").innerHTML += `<div><b>User:</b> ${userInput}</div>`;
    document.getElementById("user-input").value = ""; // Clear input field

    console.log(`chatStep: ${chatStep}, userInput: ${userInput}`); // Debugging log

    if (chatStep === 0) {
        // Check for severe conditions
        const isSevere = severeConditions.some(condition => userInput.includes(condition.toLowerCase()));
        
        console.log(`isSevere: ${isSevere}`); // Debugging log

        if (isSevere) {
            document.getElementById("chat").innerHTML += `<div><b>Chat Assistant:</b> Would you like to book a mobile clinic consultation?</div>`;
            chatStep = 1; // Move to booking process
        } else {
            document.getElementById("chat").innerHTML += `<div><b>Chat Assistant:</b> Could you please describe your condition or type 'help' for more assistance.</div>`;
        }
    } else if (chatStep === 1) {
        // User's response to booking consultation
        if (userInput === "yes") {
            document.getElementById("chat").innerHTML += `<div><b>Chat Assistant:</b> Could you please specify your gender?</div>`;
            chatStep = 2; // Move to ask for gender
        } else {
            document.getElementById("chat").innerHTML += `<div><b>Chat Assistant:</b> Let us know if there's anything else you need help with.</div>`;
            chatStep = 0; // Reset to initial state
        }
    } else if (chatStep === 2) {
        // Get user's gender
        gender = userInput; // Store gender
        document.getElementById("chat").innerHTML += `<div><b>Chat Assistant:</b> Thank you. Now, could you please provide your age?</div>`;
        chatStep = 3; // Move to ask for age
        return; // Exit to wait for age input
    } else if (chatStep === 3) {
        // Get user's age
        age = userInput; // Store age
        document.getElementById("chat").innerHTML += `<div><b>Chat Assistant:</b> Great. Please select your area: Tembisa, Orange Farm, Soweto, Alexandra, or Diepsloot.</div>`;
        chatStep = 4; // Move to ask for area
        return; // Exit to wait for area input
    } else if (chatStep === 4) {
        // Get user's area
        area = userInput; // Store area
        if (["tembisa", "orange farm", "soweto", "alexandra", "diepsloot"].includes(area)) {
            document.getElementById("chat").innerHTML += `<div><b>Chat Assistant:</b> Lastly, please describe your medical condition briefly.</div>`;
            chatStep = 5; // Move to ask for medical condition description
            return; // Exit to wait for medical condition input
        } else {
            document.getElementById("chat").innerHTML += `<div><b>Chat Assistant:</b> Please select a valid area from Tembisa, Orange Farm, Soweto, Alexandra, or Diepsloot.</div>`;
        }
    } else if (chatStep === 5) {
        // Get medical condition description and check if it’s a severe condition
        const medicalCondition = userInput; // Store medical condition
        const isSevereCondition = severeConditions.some(condition => medicalCondition.includes(condition.toLowerCase()));
        
        // Prepare data to send to the server
        const userData = {
            id: new Date().getTime(), // Generate a unique ID based on the current timestamp
            gender: gender,
            age: age,
            area: area,
            medical_condition: medicalCondition,
            longitude: areaCoordinates[area].lng,
            latitude: areaCoordinates[area].lat,
            date: new Date().toISOString() // Add the current date and time
        };

        console.log('Sending data to server:', userData); // Debugging log

        // Send data to the server
        fetch('/api/store-user-data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userData)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Server response:', data); // Debugging log
            document.getElementById("chat").innerHTML += `<div><b>Chat Assistant:</b> ${data.message}</div>`;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById("chat").innerHTML += `<div><b>Chat Assistant:</b> There was an error storing your data. Please try again later.</div>`;
        });

        if (isSevereCondition) {
            document.getElementById("chat").innerHTML += `<div><b>Chat Assistant:</b> Thank you for providing your details. We will prioritize your consultation request based on your condition. A representative will contact you soon.</div>`;
        } else {
            document.getElementById("chat").innerHTML += `<div><b>Chat Assistant:</b> Thank you. Your details have been noted. We will proceed with the regular process for consultation.</div>`;
        }
        chatStep = 0; // Reset to initial state after completing the flow
    }
}