import random

RESPONSES = {
    "hello": [
        "Hello, I am Baymax, your personal healthcare companion.",
        "Hi there! How can I assist you today?",
        "Greetings! I'm Baymax. How are you feeling?"
    ],
    "pain": [
        "Can you describe your pain on a scale of 1 to 10?",
        "I'm here to help. Where is the pain located?",
        "Let me record that. What type of pain are you experiencing?"
    ],
    "headache": [
        "Headaches are common. Have you hydrated today?",
        "I recommend rest and drinking water. Would you like me to search for treatments?",
        "Noted. Would you like to see remedies or consult a doctor?"
    ],
    "thank you": [
        "You're welcome. I will always be with you.",
        "No problem. Stay healthy!",
        "Happy to help!"
    ],
    "bye": [
        "Goodbye. I hope you feel better soon.",
        "Take care, and remember: I am always here.",
        "Bye-bye! Don't forget to exercise and stay hydrated."
    ]
}

DEFAULT_RESPONSES = [
    "I'm not sure I understand. Could you rephrase that?",
    "Hmm... I’ll look into that. Can you be more specific?",
    "Interesting! Let me check that further."
]

def generate_response(user_input):
    user_input = user_input.lower()
    for keyword in RESPONSES:
        if keyword in user_input:
            return random.choice(RESPONSES[keyword])
    return random.choice(DEFAULT_RESPONSES)
