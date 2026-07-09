const uploadBox = document.getElementById("uploadBox");
const fileInput = document.getElementById("imageInput");

// CLICK TO OPEN FILE EXPLORER
uploadBox.addEventListener("click", () => {
    fileInput.click();
});

// DRAG OVER EFFECT
uploadBox.addEventListener("dragover", (e) => {
    e.preventDefault();
    uploadBox.style.background = "#e3f2ff";
});

uploadBox.addEventListener("dragleave", () => {
    uploadBox.style.background = "white";
});

// DROP FILE SUPPORT
uploadBox.addEventListener("drop", (e) => {
    e.preventDefault();
    uploadBox.style.background = "white";

    const file = e.dataTransfer.files[0];
    fileInput.files = e.dataTransfer.files;
});


document.getElementById("predictBtn").addEventListener("click", async () => {

    const imgFile = document.getElementById("imageInput").files[0];
    if (!imgFile) {
        alert("Please upload an image!");
        return;
    }

    const formData = new FormData();
    formData.append("image", imgFile);

    const res = await fetch("/api/predict", {
        method: "POST",
        body: formData
    });
    const uploadBox = document.getElementById("uploadBox");
const imageInput = document.getElementById("imageInput");

// Click on box opens file dialog
uploadBox.addEventListener("click", () => imageInput.click());

// Drag & drop effects
uploadBox.addEventListener("dragover", (e) => {
    e.preventDefault();
    uploadBox.style.background = "#bc8ee4";
});

uploadBox.addEventListener("dragleave", () => {
    uploadBox.style.background = "white";
});

uploadBox.addEventListener("drop", (e) => {
    e.preventDefault();
    uploadBox.style.background = "white";

    const file = e.dataTransfer.files[0];
    imageInput.files = e.dataTransfer.files;
});

// Predict Logic (same as before)
document.getElementById("predictBtn").addEventListener("click", async () => {

    const imgFile = imageInput.files[0];
    if (!imgFile) return alert("Please upload an image!");

    const formData = new FormData();
    formData.append("image", imgFile);

    const res = await fetch("/api/predict", {
        method: "POST",
        body: formData
    });

    const data = await res.json();

    const box = document.getElementById("resultBox");
    const graph = document.getElementById("graphCanvas");

    box.classList.remove("hidden");

    if (data.success) {
        box.innerHTML = `
            <b>Diagnosis:</b> ${data.result.diagnosis}<br>
            <b>Confidence:</b> ${data.result.confidence}
        `;

        graph.classList.remove("hidden");

        const ctx = graph.getContext("2d");
        new Chart(ctx, {
            type: "bar",
            data: {
                labels: ["Confidence"],
                datasets: [{
                    label: "Prediction Confidence",
                    data: [data.result.confidence],
                    backgroundColor: ["#dfcf74"]
                }]
            },
            options: {
                scales: {
                    y: { min: 0, max: 1 }
                }
            }
        });
    }
});


    const data = await res.json();

    const box = document.getElementById("resultBox");
    const graph = document.getElementById("graphCanvas");

    box.classList.remove("hidden");

    if (data.success) {
        box.innerHTML = `
            <b>Prediction:</b> ${data.result.diagnosis}<br>
            <b>Confidence:</b> ${data.result.confidence}
        `;

        graph.classList.remove("hidden");

        const ctx = graph.getContext("2d");

        new Chart(ctx, {
            type: "bar",
            data: {
                labels: ["Confidence"],
                datasets: [{
                    label: "Prediction Confidence",
                    data: [data.result.confidence],
                    backgroundColor: ["#ed7bcb"]
                }]
            },
            options: {
                scales: {
                    y: { min: 0, max: 1 }
                }
            }
        });

    } else {
        box.innerHTML = "Error: " + data.error;
    }
});
