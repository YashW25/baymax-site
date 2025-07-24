from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
from chatbot.treatment import get_treatment_for_input
from chatbot.responder import generate_response as fallback_response

app = Flask(__name__)

# ------------------ Mail Configuration ------------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'yashwarulkar25@gmail.com'       # ✅ Your email
app.config['MAIL_PASSWORD'] = 'Yash@123'                        # ✅ App password (not Gmail password!)
app.config['MAIL_DEFAULT_SENDER'] = 'yashwarulkar25@gmail.com' # ✅ Sender address

mail = Mail(app)

# ------------------ Routes ------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.json
    message = data.get("message", "").strip()
    print(f"\n📝 User said: {message}")

    response_text = get_treatment_for_input(message)
    if not response_text:
        response_text = fallback_response(message)

    print(f"🤖 Baymax replied: {response_text}")
    return jsonify({"response": response_text})


@app.route("/contact_doctor", methods=["POST"])
def contact_doctor():
    data = request.get_json()
    name = data.get("name")
    mobile = data.get("mobile")
    email = data.get("email")
    symptoms = data.get("symptoms")
    city = data.get("city")
    age = data.get("age")

    msg_body = f"""
    👨‍⚕️ New Doctor Contact Request:

    Name: {name}
    Mobile: {mobile}
    Email: {email}
    City: {city}
    Age: {age}
    Symptoms: {symptoms}
    """

    try:
        msg = Message("Baymax: New Patient Request", recipients=['your_doctor_email@example.com'])
        msg.body = msg_body
        mail.send(msg)
        return jsonify({"message": "✅ Your request has been sent to a doctor!"})
    except Exception as e:
        print(f"❌ Mail send failed: {e}")
        return jsonify({"message": "❌ Failed to send your request. Please try again later."}), 500

# ------------------ Run Server ------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
