import os
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, models, transforms
from torch.utils.data import DataLoader
import json

# ---------------------------
# PATH SETUP
# ---------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "..", "..", "dataset")
MODEL_DIR = os.path.join(BASE_DIR, "..", "models")
os.makedirs(MODEL_DIR, exist_ok=True)


def main():
    # ---------------------------
    # IMAGE TRANSFORMS
    # ---------------------------
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    dataset = datasets.ImageFolder(DATASET_DIR, transform=transform)
    dataloader = DataLoader(dataset, batch_size=16, shuffle=True)

    num_classes = len(dataset.classes)
    class_map = {i: cls for i, cls in enumerate(dataset.classes)}

    # Save class label mapping
    with open(os.path.join(MODEL_DIR, "class_map.json"), "w") as f:
        json.dump(class_map, f)

    # ---------------------------
    # LOAD RESNET18 WITH NEW SYNTAX (no warning)
    # ---------------------------
    weights = models.ResNet18_Weights.DEFAULT
    model = models.resnet18(weights=weights)

    # Replace final FC layer for our number of classes
    model.fc = nn.Linear(model.fc.in_features, num_classes)

    # Device selection
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    # Loss and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.0001)

    print("\n==============================")
    print("       Training Started       ")
    print("==============================\n")

    # ---------------------------
    # TRAINING LOOP (5 EPOCHS)
    # ---------------------------
    for epoch in range(5):
        model.train()
        running_loss = 0.0

        for images, labels in dataloader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)

            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

        print(f"Epoch {epoch + 1} / 5 ─ Loss: {running_loss:.4f}")

    # ---------------------------
    # SAVE TRAINED MODEL
    # ---------------------------
    torch.save(model.state_dict(), os.path.join(MODEL_DIR, "model.pth"))
    print("\n==========================================")
    print(" Training complete! Model saved to:")
    print(" backend/models/model.pth")
    print("==========================================\n")


if __name__ == "__main__":
    main()
