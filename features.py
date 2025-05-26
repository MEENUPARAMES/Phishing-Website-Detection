# features.py
from urllib.parse import urlparse
import re

def extract_features(url):
    features = []
    parsed = urlparse(url)

    # Example features — replace with real ones used in training
    features.append(len(url))                         # Length of URL
    features.append(url.count('.'))                   # Number of dots
    features.append(1 if 'https' in parsed.scheme else 0)  # Uses HTTPS
    features.append(1 if '@' in url else 0)           # Suspicious '@'
    features.append(1 if '-' in parsed.netloc else 0) # Hyphen in domain
    features.append(len(parsed.path))                 # Length of path

    return features
