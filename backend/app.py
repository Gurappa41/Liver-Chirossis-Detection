# backend/app.py

import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from predict_utils import predict_from_bytes

# ---------------------------------------
# UPLOAD FOLDER SETUP
# ---------------------------------------
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXT = {"png", "jpg", "jpeg"}

# ---------------------------------------
# FLASK APP SETUP
# ---------------------------------------
app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "..", "frontend", "templates"),
    static_folder=os.path.join(os.path.dirname(__file__), "..", "frontend", "static")
)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB limit


# ---------------------------------------
# VALIDATE FILE EXTENSIONS
# ---------------------------------------
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXT


# ---------------------------------------
# HOME PAGE (LANDING PAGE)
# ---------------------------------------
@app.route("/")
def index():
    return render_template("index.html")


# ---------------------------------------
# PREDICT PAGE (FORM + FILE UPLOAD PAGE)
# ---------------------------------------
@app.route("/predict.html")
def predict_page():
    return render_template("predict.html")


# ---------------------------------------
# IMAGE UPLOAD - PREDICT API
# ---------------------------------------
@app.route("/api/predict", methods=["POST"])
def api_predict():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    f = request.files["image"]

    if f.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    if f and allowed_file(f.filename):
        filename = secure_filename(f.filename)
        save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        f.save(save_path)

        # Run model prediction
        with open(save_path, "rb") as img_file:
            result = predict_from_bytes(img_file.read())

        return jsonify({
            "success": True,
            "result": result
        }), 200

    return jsonify({"error": "Invalid file type"}), 400


# ---------------------------------------
# REGISTRATION + OPTIONAL IMAGE PREDICTION
# ---------------------------------------
@app.route("/api/predict_registration", methods=["POST"])
def api_predict_registration():

    name = request.form.get("name", "")
    age = request.form.get("age", "")
    gender = request.form.get("gender", "")

    # If an image is included → run prediction
    if "image" in request.files and request.files["image"].filename != "":
        f = request.files["image"]

        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            f.save(save_path)

            with open(save_path, "rb") as img_file:
                result = predict_from_bytes(img_file.read())

            return jsonify({
                "success": True,
                "form": {"name": name, "age": age, "gender": gender},
                "result": result
            }), 200

        return jsonify({"error": "Invalid file format"}), 400

    # If NO image uploaded → return only form data
    return jsonify({
        "success": True,
        "form": {"name": name, "age": age, "gender": gender},
        "result": None,
        "message": "No image provided. Upload an image to get prediction."
    }), 200


# ---------------------------------------
# RUN FLASK SERVER
# ---------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
