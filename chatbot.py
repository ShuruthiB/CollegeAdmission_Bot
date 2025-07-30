import json
import random
import nltk
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('punkt')


with open("intents.json") as file:
    data = json.load(file)

X = []
y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        X.append(pattern)
        y.append(intent["tag"])


vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize)
X_vectorized = vectorizer.fit_transform(X)


model = LogisticRegression()
model.fit(X_vectorized, y)


def get_bot_response(user_input):
    # Spell correct user input
    corrected_input = str(TextBlob(user_input).correct())

    input_vect = vectorizer.transform([corrected_input])
    pred_tag = model.predict(input_vect)[0]

    for intent in data["intents"]:
        if intent["tag"] == pred_tag:
            return random.choice(intent["responses"])

    return "Sorry, I didn't understand that."
