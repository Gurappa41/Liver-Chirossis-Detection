import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import json
import os
import io

# ----------------------------
# PATHS
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pth")
CLASS_MAP_PATH = os.path.join(BASE_DIR, "models", "class_map.json")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ----------------------------
# LOAD CLASS MAP
# ----------------------------
with open(CLASS_MAP_PATH, "r") as f:
    class_map = json.load(f)

# Convert keys to int
class_map = {int(k): v for k, v in class_map.items()}

num_classes = len(class_map)

# ----------------------------
# LOAD MODEL (No warnings)
# ----------------------------
# We do NOT use pretrained weights for inference
model = models.resnet18(weights=None)

# Replace final FC layer to match training configuration
model.fc = nn.Linear(model.fc.in_features, num_classes)

# Load trained model weights
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))

# Set model to evaluation mode
model.eval()
model.to(device)

# ----------------------------
# IMAGE TRANSFORM PIPELINE
# ----------------------------
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# ----------------------------
# FRIENDLY LABEL MAP
# ----------------------------
friendly = {
    "f0": "No Fibrosis (F0)",
    "f1": "Mild Fibrosis (F1)",
    "f2": "Moderate Fibrosis (F2)",
    "f3": "Severe Fibrosis (F3)",
    "f4": "Cirrhosis (F4)"
}

# ----------------------------
# PREDICTION FUNCTION
# ----------------------------
def predict_from_bytes(file_bytes):
    img = Image.open(io.BytesIO(file_bytes)).convert("RGB")

    # Apply transforms
    img = transform(img).unsqueeze(0).to(device)

    # Forward pass
    with torch.no_grad():
        logits = model(img)
        probs = torch.softmax(logits, dim=1)
        confidence, pred_idx = torch.max(probs, dim=1)

    # Get class label
    label = class_map[pred_idx.item()]
    confidence = round(confidence.item(), 3)

    diagnosis = friendly.get(label, label)

    return {
        "label": label,
        "diagnosis": diagnosis,
        "confidence": confidence
    }
