import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report


def classify(text: str):
    dataset = pd.read_csv("data/Categoriser/customData.csv")

    # Convert text data into TF-IDF vectors
    vectorizer = TfidfVectorizer()
    vectorized_texts = vectorizer.fit_transform(dataset["Text"])

    # Train a Support Vector Machine (SVM) classifier
    svc = SVC(kernel="linear")
    svc.fit(vectorized_texts, dataset["Intent"])

    vector_in = vectorizer.transform([text])

    # Make predictions on the test set
    predicted = svc.predict(vector_in)
    return predicted


"""
dataset = pd.read_csv("data/Categoriser/customData.csv")
test_data = pd.read_csv("data/Categoriser/test.csv")
test_dta = ["whats the weather like today", "wake me up at 7 am"]

# Convert text data into TF-IDF vectors
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(dataset["Text"])
X_test_tfidf = vectorizer.transform(test_data["Text"])

# Train a Support Vector Machine (SVM) classifier
classifier = SVC(kernel="linear")
classifier.fit(X_train_tfidf, dataset["Intent"])

# Make predictions on the test set
y_pred = classifier.predict(X_test_tfidf)

# Evaluate the model
print("Classification Report:")
print(classification_report(test_data["Intent"], y_pred))

X_test_tfidf = vectorizer.transform(test_dta)
print(classifier.predict(X_test_tfidf))
"""
