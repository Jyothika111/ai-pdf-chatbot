

const API_URL = "http://127.0.0.1:8000";

// ======================= UPLOAD PDF =======================
async function uploadPDF() {
    const fileInput = document.getElementById("pdfFile");
    const uploadBtn = document.getElementById("uploadBtn");
    const status = document.getElementById("uploadStatus");
    const currentPDF = document.getElementById("currentPDF");

    if (fileInput.files.length === 0) {
        status.innerHTML = "❌ Please choose a PDF.";
        return;
    }

    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append("file", file);

    // Show processing
    uploadBtn.disabled = true;
    uploadBtn.innerText = "Processing...";
    status.innerHTML = "⏳ Uploading and processing your document...";

    try {
        const response = await fetch(`${API_URL}/upload`, {
            method: "POST",
            body: formData
        });

        const result = await response.json();

        if (response.ok) {
            status.innerHTML = "✅ PDF Uploaded Successfully!";
            currentPDF.innerHTML = `📄 Current Document: <b>${file.name}</b>`;
            fileInput.value = "";
        } else {
            status.innerHTML = `❌ ${result.detail || "Upload failed"}`;
        }

    } catch (error) {
        console.error(error);
        status.innerHTML = "❌ Cannot connect to backend.";
    }

    uploadBtn.disabled = false;
    uploadBtn.innerText = "Upload PDF";
}

// ======================= ASK QUESTION =======================
async function askQuestion() {
    const questionBox = document.getElementById("question");
    const chat = document.getElementById("chat");

    const question = questionBox.value.trim();
    if (!question) return;

    // User message
    chat.innerHTML += `
        <div class="user-message">${question}</div>
    `;

    // Thinking message
    chat.innerHTML += `
        <div class="bot-message" id="thinking">🤖 Thinking...</div>
    `;

    chat.scrollTop = chat.scrollHeight;
    questionBox.value = "";

    try {
        const response = await fetch(`${API_URL}/ask`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        const result = await response.json();

        document.getElementById("thinking").remove();

        chat.innerHTML += `
            <div class="bot-message">${result.answer}</div>
        `;

    } catch (error) {
        document.getElementById("thinking").remove();

        chat.innerHTML += `
            <div class="bot-message">❌ Error getting response from AI.</div>
        `;
    }

    chat.scrollTop = chat.scrollHeight;
}

// ======================= CLEAR CHAT =======================
function clearChat() {
    document.getElementById("chat").innerHTML = "";
}

// ======================= ENTER KEY =======================
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("question").addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            askQuestion();
        }
    });
});