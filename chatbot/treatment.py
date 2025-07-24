import json
import os
from chatbot.responder import generate_response  # fallback if no matching symptom

def load_treatments_data():
    """Load treatments data from JSON file"""
    path = os.path.join(os.path.dirname(__file__), "treatments.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("❌ Error loading treatments.json:", e)
        return {}

def extract_keywords(user_input, treatments_data):
    """Find matching symptoms in user input"""
    input_lower = user_input.lower()
    return [symptom for symptom in treatments_data.keys() if symptom.lower() in input_lower]

def format_treatment_response(keywords, treatments_data):
    """Format the treatment information into a readable response"""

    # Emergency symptoms list
    emergencies = {
        "chest pain", "suicidal ideation", "shortness of breath",
        "hematemesis", "melena", "vaginal bleeding in late pregnancy",
        "amaurosis fugax", "paralysis", "bradypnea"
    }

    # Check for emergencies
    found_emergencies = [s for s in keywords if s in emergencies]
    if found_emergencies:
        return (
            "🚨 **EMERGENCY WARNING** 🚨\n"
            f"Detected symptom(s): {', '.join(found_emergencies)}\n"
            "➡️ Please seek **immediate medical attention**.\n"
            "Call emergency services or visit the nearest hospital.\n"
        )

    # Compile treatment details
    treatment_sections = []
    general_advice = [
        "Rest and hydration are often helpful",
        "Monitor symptoms for worsening",
        "Consult a healthcare provider if symptoms persist"
    ]

    for keyword in keywords:
        if keyword in treatments_data:
            treatments = treatments_data[keyword]
            section = f"▪️ **For {keyword.capitalize()}**:\n"

            # Medications
            meds = treatments.get("medications", [])
            if meds:
                section += "  - Medications:\n" + "".join(f"    • {m}\n" for m in meds)

            # Other treatments
            others = treatments.get("other", [])
            if others:
                section += "  - Other Treatments:\n" + "".join(f"    • {o}\n" for o in others)

            if not meds and not others:
                section += "  - No specific treatments found.\n"

            treatment_sections.append(section)

    if treatment_sections:
        return (
            "🩺 **Treatment Recommendations**:\n\n" +
            "\n".join(treatment_sections) +
            "\nℹ️ **General Advice**:\n" +
            "\n".join(f"- {tip}" for tip in general_advice) +
            "\n\n⚠️ *Disclaimer: This is general information and not a substitute for professional medical advice.*"
        )
    else:
        return generate_response(" ".join(keywords))  # fallback

def get_treatment_for_input(user_input):
    """Main entry point to get treatment or fallback to responder"""
    treatments_data = load_treatments_data()
    if not treatments_data:
        return generate_response(user_input)

    keywords = extract_keywords(user_input, treatments_data)
    if not keywords:
        return generate_response(user_input)

    return format_treatment_response(keywords, treatments_data)
