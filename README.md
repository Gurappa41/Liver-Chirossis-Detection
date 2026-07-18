# 🩺 Liver Cirrhosis Detection Using Deep Learning

A web-based deep learning application that predicts **Liver Cirrhosis** from ultrasound images using a **ResNet18** model. The application is built with **PyTorch** for model inference and **Flask** for the web interface, allowing users to upload liver ultrasound images and receive instant predictions.

---

## 📌 Overview

Liver cirrhosis is a chronic disease that causes irreversible liver damage. Early detection can improve treatment outcomes and patient care.

This project leverages **Deep Learning** and **Computer Vision** techniques to classify liver ultrasound images and provide fast, automated predictions through an easy-to-use web application.

---

## ✨ Features

- Upload liver ultrasound images.
- Deep learning-based prediction using ResNet18.
- User-friendly web interface built with Flask.
- Fast and accurate image classification.
- Responsive frontend using HTML, CSS, and JavaScript.
- Real-time prediction results.

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Flask
- Python

### Deep Learning
- PyTorch
- TorchVision
- ResNet18 (Transfer Learning)

### Libraries
- NumPy
- Pillow
- OpenCV
- Scikit-learn

---

## 📂 Project Structure

```
Liver-Cirrhosis-Detection/
│
├── backend/
│   ├── app.py
│   ├── models/
│   │   └── model.pth
│   └── requirements.txt
│
├── frontend/
│   ├── templates/
│   ├── static/
│
├── dataset/
│
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Liver-Cirrhosis-Detection.git

cd Liver-Cirrhosis-Detection
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 🧠 Model Information

- Architecture: **ResNet18**
- Framework: **PyTorch**
- Transfer Learning: Yes
- Image Classification
- Medical Ultrasound Image Analysis

---

## 📸 Application Workflow

1. Launch the Flask application.
2. Upload a liver ultrasound image.
3. The trained ResNet18 model processes the image.
4. The system predicts whether liver cirrhosis is detected.
5. The prediction result is displayed on the webpage.

---

## 🎯 Future Improvements

- Improve model accuracy with a larger dataset.
- Support multiple liver disease classifications.
- Deploy the application on a cloud platform.
- Add user authentication and patient history.
- Generate downloadable medical reports.

---

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Deep Learning with PyTorch
- Transfer Learning
- Image Classification
- Flask Web Development
- Computer Vision
- Model Integration
- Web Application Development
- Git & GitHub

---

## 👨‍💻 Author

**Avula Gurappa**

- GitHub: https://github.com/Gurappa41
- LinkedIn: https://linkedin.com/in/gurappa41

---

## ⭐ Support

If you found this project helpful, please consider giving it a **Star ⭐** on GitHub.

It motivates me to continue building and sharing more projects!
