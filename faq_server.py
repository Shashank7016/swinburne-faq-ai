# 1. Imports
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, DistilBertModel, DistilBertTokenizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, jsonify
from flask_cors import CORS


# 2. Load GPT-4 Model and Tokenizer for general responses
gpt_model_name = "gpt2-medium"  # Adjust this based on your preference
gpt_tokenizer = GPT2Tokenizer.from_pretrained(gpt_model_name)
gpt_model = GPT2LMHeadModel.from_pretrained(gpt_model_name)
gpt_model.eval()

# 3. Load DistilBERT Model and Tokenizer for question embeddings
distilbert_tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
distilbert_model = DistilBertModel.from_pretrained("distilbert-base-uncased")

# Sample questions and answers
known_questions = [
    "what is the slogan of swinburne online",
    "how do i enroll in a course",
    "what courses do you offer",
    "how much is the tuition fee"
]

known_answers = [
    "The slogan of Swinburne Online is 'Future Ready'.",
    "To enroll in a course, visit our enrollment page and follow the instructions.",
    "We offer a wide range of courses in various fields such as Engineering, Business, Arts, etc.",
    "The tuition fee varies depending on the course. Please visit our fees page for detailed information."
]

# Precompute embeddings for known questions
def compute_embeddings(texts, tokenizer, model):
    inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=512)
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).detach().numpy()
    return embeddings

known_question_embeddings = compute_embeddings(known_questions, distilbert_tokenizer, distilbert_model)

def get_answer(user_question):
    # Get embedding for user's question
    user_question_embedding = compute_embeddings([user_question], distilbert_tokenizer, distilbert_model)

    # Compute similarity scores
    similarities = cosine_similarity(user_question_embedding, known_question_embeddings)

    # Check if there's a known question with similarity above a threshold
    threshold = 0.85
    if similarities.max() > threshold:
        most_similar_idx = similarities.argmax()
        return known_answers[most_similar_idx]
    else:
        # If no similar known question, use GPT-2 to generate a response
        return "Sorry, we don't have the answer to this following question currently."


app = Flask(__name__)
CORS(app)

@app.route("/get-answer", methods=["POST"])
def answer_question():
    data = request.json
    user_question = data.get('question', '')
    response = get_answer(user_question)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000)
