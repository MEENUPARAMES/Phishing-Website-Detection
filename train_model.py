import pickle
from sklearn.ensemble import RandomForestClassifier

# Dummy training data
X = [
    [75, 1],   # Legitimate
    [50, 1],
    [120, 0],  # Phishing
    [130, 0],
]
y = [0, 0, 1, 1]  # 0 = Legitimate, 1 = Phishing

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("✅ Model trained and saved as model.pkl")
