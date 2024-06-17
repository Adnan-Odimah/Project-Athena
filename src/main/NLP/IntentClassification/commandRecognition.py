""" Contains the classification command for text categories"""

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC


def classify(text: str) -> str:
    """Classifies the text into the proper category to help with processing the command

    Args:
        text (str): The text to classify

    Returns:
        str: The classifcation of the text ["CONVERSATION", "ALARM", etc.]
    """
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
