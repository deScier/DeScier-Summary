import re
from io import BytesIO
from docx import Document
from flask import Flask, render_template, request, jsonify
from flask_caching import Cache
import nltk
from nltk.tokenize import word_tokenize
import openai

nltk.download('punkt', quiet=True)

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})

openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    file = request.files['file']
    word_count = int(request.form.get('word_count', 100))
    language = request.form.get('language', 'english')

    keywords = []

    if file:
        document = Document(BytesIO(file.read()))
        text = "\n".join([para.text for para in document.paragraphs])
        summary = generate_summary(text, word_count, language)

        if language != 'english':
            summary = translate_text(summary, language)

        keywords = get_keywords_chatgpt(summary, language)  # Change this line

    return jsonify({'summary': summary, 'keywords': keywords})

@cache.memoize(timeout=3600)
def generate_summary(text, word_count, language):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please summarize the following text in exactly {word_count} words:\n\n{text}\n",
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
    )
    long_summary = response.choices[0].text.strip()
    sentences = re.split(r'(?<=[\.\?!])\s+', long_summary)

    reconstructed_summary = ''
    current_word_count = 0
    for sentence in sentences:
        sentence_word_count = len(word_tokenize(sentence))
        if current_word_count + sentence_word_count <= word_count or not reconstructed_summary:
            reconstructed_summary += sentence + ' '
            current_word_count += sentence_word_count
        else:
            break

    return reconstructed_summary.strip()

def get_keywords_chatgpt(text, language, max_keywords=5):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please extract exactly 5 important keywords from the following {language} text:\n\n{text}\n",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    extracted_keywords = response.choices[0].text.strip().split('\n')
    return extracted_keywords[:max_keywords]

@cache.memoize(timeout=3600)
def translate_text(text, target_language):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate the following text from English to {target_language}:\n\n{text}\n",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    translated_text = response.choices[0].text.strip()
    return translated_text

if __name__ == '__main__':
    app.run(debug=True)
