from flask import Flask, render_template, request
import json
from machinetranslation import translator
 
app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    get_translation = translator.english_to_french(textToTranslate)
    return get_translation

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    get_translation =translator.french_to_english(textToTranslate)
    return get_translation

@app.route("/")
def renderIndexPage():

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080,debug=True)
