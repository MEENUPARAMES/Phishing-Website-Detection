import pickle
from feature_extractor import extract_features  # or from features import extract_features

# Load the model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

def predict_url(url):
    features = extract_features(url)
    feature_values = list(features.values())  # convert dict to list
    prediction = model.predict([feature_values])[0]
    return prediction
