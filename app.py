from flask import Flask, render_template, request, jsonify
import openai
import requests
from io import BytesIO
from docx import Document

app = Flask(__name__)
openai.api_key = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    file = request.files['file']
    word_count = int(request.form.get('word_count', 100))
    if file:
        # Read the Word document
        document = Document(BytesIO(file.read()))

        # Extract text from the document
        text = "\n".join([para.text for para in document.paragraphs])

        # Use ChatGPT API to generate a summary
        summary = generate_summary(text, word_count)

        # Return the summary as a JSON object
        return jsonify({'summary': summary})

    return 'File not found', 400

def generate_summary(text, word_count):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please summarize the following text in approximately {word_count} words:\n\n{text}\n",
        max_tokens=word_count * 2, # Adjust max_tokens based on the desired word count
        n=1,
        stop=None,
        temperature=0.5,
    )

    summary = response.choices[0].text.strip()
    return summary

if __name__ == '__main__':
    app.run(debug=True)
