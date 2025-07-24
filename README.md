# 🤖 Virtual Baymax – AI Health Companion

Virtual Baymax is a personal health assistant inspired by Disney’s Baymax. It responds to user-reported symptoms using built-in medical treatment data, speaks replies aloud, and plays matching animations — all in a simple Flask web app.

---

## 📁 Folder Structure

baymax/
│
├── app.py # 🔥 Main Flask backend (chat logic)
├── requirements.txt # 📦 Python dependencies
├── README.md # 📘 This file
├── LICENSE
├── NOTICE
│
├── static/
│ ├── css/
│ │ └── styles.css # 🎨 UI styling
│ ├── js/
│ │ └── script.js # 💡 Handles TTS, video swapping, chat events
│ ├── videos/ # 🎬 Baymax animations (.mp4)
│ │ ├── idle.mp4
│ │ ├── thinking.mp4
│ │ └── speaking.mp4
│
├── templates/
│ └── index.html # 🖼️ Main HTML with video + chat UI
│
├── chatbot/
│ ├── treatment.py # 💊 Symptom → treatment mapping logic
│ ├── treatments.json # 📚 Symptom-treatment dataset
│ └── responder.py # 💬 Fallback chatbot logic (for casual Q&A)



---

## 🚀 Features

### 🎬 Baymax Animations
- Video-based responses using idle, thinking, and speaking animations
- Smooth transitions with autoplay and loop handling via JavaScript

### 💬 Symptom-Based Chat
- User enters symptoms like "fever", "nausea", "headache"
- Baymax suggests treatments based on a preloaded static database
- If no symptom is detected, fallback casual chatbot reply is used

### 🔊 Browser-Based Speech Output
- Uses the Web Speech API (no need for `pyttsx3`)
- Baymax speaks all responses aloud automatically

---

## 💻 Installation & Setup


### 1. Clone the Repository

```bash
git clone https://github.com/yourname/virtual_baymax.git
cd virtual_baymax


## 💻 Installation & Setup

1. **Clone the repository**

git clone https://github.com/yashwarulkar/virtual_baymax.git
cd virtual_baymax

2. **Install dependencies**

pip install -r requirements.txt
requirements.txt should include:
flask, opencv-python, deepface, pyttsx3, pydub, requests, beautifulsoup4, tensorflow, keras

3. Run the app

python app.py

4. Visit the interface

Open your browser to:
http://127.0.0.1:5000/

## 🖥️ Interface Overview

1. 🧠 Symptom detection via keyword match

2. 💊 Returns treatment options (medicines + non-medication suggestions)

3. 🗣️ Speaks out Baymax's response using browser TTS

4. 🎥 Plays relevant Baymax animation based on the conversation state

5. ⌨️ Chat interface with Enter key support

## ✅ To-Do / Future Plans

1. 🎙️ Add mic-to-text support (voice input)

2. 🧠 Integrate real AI (LLM, ChatGPT, etc.) in responder.py

3. 📚 Expand scraped database with treatments

4. 🧑‍⚕️ Store chat history or symptom logs

5. 🔐 Add user login for long-term health tracking

## 🙌 Credits

Created by Yash Warulkar
Inspired by Baymax from Big Hero 6