import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from src.models.baseline_cnn import BaselineCNN

def train_baseline():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # Dummy dataset placeholder for pipeline syntax validation
    # (Replace with SARDataset loader from Phase 2/3)
    X_train = torch.randn(100, 1, 64, 64)
    y_train = torch.randint(0, 10, (100,))
    dataset = TensorDataset(X_train, y_train)
    loader = DataLoader(dataset, batch_size=16, shuffle=True)

    model = BaselineCNN(num_classes=10, in_channels=1).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    os.makedirs("checkpoints", exist_ok=True)
    best_loss = float('inf')

    for epoch in range(5):  # Set to full epochs for production run
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0

        for inputs, labels in loader:
            inputs, labels = inputs.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * inputs.size(0)
            _, predicted = outputs.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()

        epoch_loss = running_loss / total
        epoch_acc = correct / total
        print(f"Epoch [{epoch+1}/5] | Loss: {epoch_loss:.4f} | Acc: {epoch_acc:.4f}")

        if epoch_loss < best_loss:
            best_loss = epoch_loss
            torch.save(model.state_dict(), "checkpoints/baseline_best.pth")

    print("Training complete. Best checkpoint saved to checkpoints/baseline_best.pth")

if __name__ == "__main__":
    train_baseline()