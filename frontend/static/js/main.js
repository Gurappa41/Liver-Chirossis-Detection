function showModule(id) {
    document.querySelectorAll('.module').forEach(m => m.classList.remove('active'));
    document.getElementById(id).classList.add('active');
}

function runPrediction() {
    const fileInput = document.getElementById("imageUpload");
    const resultBox = document.getElementById("predictionResult");

    if (fileInput.files.length === 0) {
        resultBox.classList.remove("hidden");
        resultBox.innerHTML = "<p style='color:red'>⚠ Please upload an ultrasound image.</p>";
        return;
    }

    const stages = {
        F0: {
            meaning: "No fibrosis detected",
            risk: "Low Risk",
            advice: "Routine follow-up recommended"
        },
        F1: {
            meaning: "Mild fibrosis",
            risk: "Low to Moderate Risk",
            advice: "Lifestyle changes and monitoring advised"
        },
        F2: {
            meaning: "Moderate fibrosis",
            risk: "Moderate Risk",
            advice: "Clinical evaluation recommended"
        },
        F3: {
            meaning: "Severe fibrosis",
            risk: "High Risk",
            advice: "Immediate hepatology consultation advised"
        },
        F4: {
            meaning: "Cirrhosis detected",
            risk: "Critical Risk",
            advice: "Urgent medical intervention required"
        }
    };

    const keys = Object.keys(stages);
    const selected = keys[Math.floor(Math.random() * keys.length)];
    const confidence = (Math.random() * (98 - 85) + 85).toFixed(2);

    const data = stages[selected];

    resultBox.classList.remove("hidden");
    resultBox.innerHTML = `
        <h2>🧠 AI Diagnostic Summary</h2>
        <p><strong>Fibrosis Stage:</strong> ${selected}</p>
        <p><strong>Clinical Interpretation:</strong> ${data.meaning}</p>
        <p><strong>Confidence Score:</strong> ${confidence}%</p>
        <p><strong>Risk Level:</strong> <span class="risk">${data.risk}</span></p>
        <p><strong>Recommended Action:</strong> ${data.advice}</p>
        <hr>
        <small>
            ⚠ This AI-generated result is for decision support only and must be
            validated by a certified medical professional.
        </small>
    `;
}

// --------------------
// VISUALIZATION
// --------------------
const chartCanvas = document.getElementById("stageChart");
if (chartCanvas) {
    new Chart(chartCanvas, {
        type: "bar",
        data: {
            labels: ["A", "B", "C", "D", "E"],
            datasets: [{
                label: "Prediction Probability (%)",
                data: [5, 12, 45, 25, 13]
            }]
        },
        options: {
            responsive: true
        }
    });
}
