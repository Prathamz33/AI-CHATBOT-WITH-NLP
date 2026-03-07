import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load knowledge base
with open("knowledge.txt", "r", encoding="utf-8") as file:
    corpus = file.read().lower()

sent_tokens = nltk.sent_tokenize(corpus)

# Greeting responses
GREETING_INPUTS = ("hello", "hi", "greetings", "hey")
GREETING_RESPONSES = ["Hi there!", "Hello!", "Hey!", "Hi, how can I help you?"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def chatbot_response(user_input):
    user_input = user_input.lower()
    sent_tokens.append(user_input)

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(sent_tokens)

    similarity = cosine_similarity(tfidf[-1], tfidf)
    idx = similarity.argsort()[0][-2]

    flat = similarity.flatten()
    flat.sort()
    score = flat[-2]

    if score == 0:
        response = "I am sorry, I do not understand."
    else:
        response = sent_tokens[idx]

    sent_tokens.pop()
    return response

# Chat Loop
print("AI Chatbot is running! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a great day.")
        break
    elif greeting(user_input) is not None:
        print("Chatbot:", greeting(user_input))
    else:
        print("Chatbot:", chatbot_response(user_input))