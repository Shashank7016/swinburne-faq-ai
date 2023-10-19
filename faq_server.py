# 1. Imports
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, DistilBertModel, DistilBertTokenizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, jsonify
from flask_cors import CORS
from docx import Document
import re

def read_docx(file_path):
    doc = Document(file_path)
    return ' '.join([para.text for para in doc.paragraphs])

questions_content = read_docx("Questions.docx")
answers_content = read_docx("Answers.docx")

# Splitting the content based on the pattern Q.x
questions_list = re.split(r'Q\.\d+', questions_content)[1:]  # [1:] to skip the content before the first Q.x

def preprocess_text(text):
    # Convert to lowercase and strip whitespace
    text = text.lower().strip()
    # Strip off trailing question marks
    text = text.rstrip('?')
    # Keep only alphanumeric characters, spaces, and question marks
    text = re.sub(r'[^a-z0-9\s\?]', '', text)
    return text

# Process each question
questions_list = [preprocess_text(q) for q in questions_list]

# Splitting the content based on the pattern A.x
answers_list = re.split(r'A\.\d+', answers_content)[1:]  # [1:] to skip the content before the first A.x

# Process each answer
answers_list = [a.strip() for a in answers_list]


# 2. Load GPT-4 Model and Tokenizer for general responses
gpt_model_name = "gpt2-medium"  # Adjust this based on your preference
gpt_tokenizer = GPT2Tokenizer.from_pretrained(gpt_model_name)
gpt_model = GPT2LMHeadModel.from_pretrained(gpt_model_name)
gpt_model.eval()

# 3. Load DistilBERT Model and Tokenizer for question embeddings
distilbert_tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
distilbert_model = DistilBertModel.from_pretrained("distilbert-base-uncased")

# Sample questions and answers
known_questions = questions_list
known_answers = answers_list

# Precompute embeddings for known questions
def compute_embeddings(texts, tokenizer, model):
    inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=512)
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).detach().numpy()
    return embeddings

known_question_embeddings = compute_embeddings(known_questions, distilbert_tokenizer, distilbert_model)

def get_answer(user_question):
    # Preprocess the user's question
    user_question = preprocess_text(user_question)
    
    # Get embedding for user's question
    user_question_embedding = compute_embeddings([user_question], distilbert_tokenizer, distilbert_model)
    # Compute similarity scores
    similarities = cosine_similarity(user_question_embedding, known_question_embeddings)
    # Check if there's a known question with similarity above a threshold
    threshold = 0.7
    most_similar_idx = similarities.argmax()
    
    if similarities.max() > threshold:
        answer = known_answers[most_similar_idx]
    else:
        # If no similar known question, use GPT-2 to generate a response
        answer = "Sorry, we don't have the answer to this question currently."
    
    return answer

app = Flask(__name__)
CORS(app)

@app.route("/get-answer", methods=["POST"])
def answer_question():
    data = request.json
    user_question = data.get('question', '')
    response = get_answer(user_question)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

