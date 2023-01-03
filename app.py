from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        app_id = "c53262b8"
        app_key = "2d98324635192cc9edb8a26daad6dd61"
        language = "en-gb"
        word_id = request.form.get('search_word')
        url = "https://od-api.oxforddictionaries.com/api/v2/entries/" + language + "/" + word_id.lower()
        r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
        response = r.json()

        print(response)
        word = response['word'].title()
        lexical_category = response['results'][0]['lexicalEntries'][0]['lexicalCategory']['text'].lower()
        definition = response['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        definition = definition[0].upper() + definition[1:]
        examples = response['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples']
        synonyms = response['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']

        return render_template('index.html', word=word,
                               lexical_category=lexical_category,
                               definition=definition,
                               examples=examples,
                               synonyms=synonyms,
                               show_result=True)
    return render_template('index.html', show_result=False)


if __name__ == '__main__':
    app.run()
