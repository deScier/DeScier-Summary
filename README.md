# DeScier-Summary

This project is a simple web application that allows users to upload a Word document and generate a summary and extract keywords from it. The application is built using Python, Flask, Summa, and OpenAI's GPT-4.

## Files in the project

app.py: The main Python script that contains the Flask web application, routes, and logic for generating summaries and extracting keywords.
index.html: The main HTML file for the web application. It contains the form to upload the Word document and display the generated summary and keywords.
styles.css: The CSS file that contains the styling for the web application.

## How to run the project

Ensure you have Python 3.x and pip installed on your system.
Clone the repository or download the files.
Open a terminal and navigate to the project folder.
Run pip install -r requirements.txt to install the required dependencies.
Run python app.py to start the Flask web application.
Open your web browser and navigate to http://127.0.0.1:5000/ to access the web application.

## Usage

Select the language of the document you want to summarize.
Upload a Word document (.docx format) using the file input field.
Choose the desired word count for the summary (between 100 and 500 words).
Click the "Summarize" button.
The generated summary and keywords will be displayed below.

## Dependencies

Flask: Web framework for Python
Summa: Library for text summarization and keyword extraction
OpenAI: API for GPT-4, used to generate summaries and translations
Werkzeug: Utility library for WSGI, used to handle file uploads
python-docx: Library for working with Microsoft Word .docx files
NOTE: For the OpenAI API, you will need to obtain an API key and include it in your project.

## Customizing the styles

The styles.css file contains the custom styles for the web application. You can modify the styles in this file to change the appearance of the application to match your preferences or branding. The file includes styles for the layout, fonts, colors, form elements, and buttons.
