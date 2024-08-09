# app.py
from flask import Flask, request, render_template
from translator import translate_text, fetch_translation_models

app = Flask(__name__)

@app.route('/')
def home():
    models = fetch_translation_models()
    return render_template('index.html', models=models)

@app.route('/translate', methods=['POST'])
def translate():
    input_text = request.form['input_text']
    language_pair = request.form['language_pair']
    output_text = translate_text(input_text, language_pair)
    models = fetch_translation_models()
    return render_template('index.html', input_text=input_text, output_text=output_text, models=models, selected_model=language_pair)

if __name__ == "__main__":
    app.run(debug=True)
