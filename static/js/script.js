const baymaxVideo = document.getElementById("baymaxVideo");
const submitBtn = document.getElementById("submitBtn");
const contactDoctorBtn = document.getElementById("contactDoctorBtn");
const userInput = document.getElementById("userInput");
const responseBox = document.getElementById("response");

const doctorModal = document.getElementById("doctorModal");
const closeModal = document.querySelector(".close");
const doctorForm = document.getElementById("doctorForm");

// --------------- Baymax video state manager ---------------
function changeBaymaxState(file) {
  baymaxVideo.loop = file === "idle.mp4";
  baymaxVideo.src = `/static/videos/${file}`;
  baymaxVideo.load();
  baymaxVideo.play();

  if (file !== "idle.mp4") {
    baymaxVideo.onended = () => {
      changeBaymaxState("idle.mp4");
    };
  } else {
    baymaxVideo.onended = null;
  }
}

// --------------- Browser TTS (Speech) ---------------
function speakText(text) {
  if ("speechSynthesis" in window) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "en-US";
    utterance.rate = 1;
    utterance.pitch = 1;
    speechSynthesis.speak(utterance);
  } else {
    console.warn("Browser does not support speech synthesis.");
  }
}

// --------------- Send Chat Message ---------------
async function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;

  responseBox.innerText = "🤔 Thinking...";
  changeBaymaxState("thinking.mp4");

  try {
    const res = await fetch("/get_response", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    const data = await res.json();
    const botResponse = data.response;

    responseBox.innerText = "🗣️ " + botResponse;
    changeBaymaxState("speaking.mp4");
    speakText(botResponse);
    userInput.value = "";

  } catch (err) {
    console.error("Error fetching response:", err);
    responseBox.innerText = "⚠️ Failed to get response.";
    changeBaymaxState("idle.mp4");
  }
}

// --------------- Modal: Show Contact Doctor Form ---------------
if (contactDoctorBtn) {
  contactDoctorBtn.onclick = () => {
    doctorModal.style.display = "block";
  };
}

// --------------- Modal: Hide When Close Clicked ---------------
if (closeModal) {
  closeModal.onclick = () => {
    doctorModal.style.display = "none";
  };
}

// --------------- Handle Form Submission ---------------
if (doctorForm) {
  doctorForm.onsubmit = async (e) => {
    e.preventDefault();

    const formData = {
      name: document.getElementById("name").value.trim(),
      mobile: document.getElementById("mobile").value.trim(),
      email: document.getElementById("email").value.trim(),
      symptoms: document.getElementById("symptoms").value.trim(),
      city: document.getElementById("city").value.trim(),
      age: document.getElementById("age").value.trim(),
    };

    try {
      const res = await fetch("/contact_doctor", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      const result = await res.json();
      alert(result.message);
      doctorForm.reset();
      doctorModal.style.display = "none";
    } catch (err) {
      console.error("Error submitting contact form:", err);
      alert("❌ Failed to send message. Try again.");
    }
  };
}

// --------------- Enter Key to Submit Message ---------------
userInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

// --------------- Close Modal on Outside Click ---------------
window.onclick = function (event) {
  if (event.target == doctorModal) {
    doctorModal.style.display = "none";
  }
};

// --------------- Submit Button Click ---------------
submitBtn.onclick = sendMessage;
