import os
import random
from fnmatch import fnmatch
from flask import Flask, jsonify

# configuration variables for pulling the jokes from the site
content_folder = os.getcwd().replace("api","content/posts")
pattern = "*.md"

app = Flask(__name__)

@app.route("/")
def just_joke():
    return get_random_joke().text

@app.route("/html")
def json_joke():
    return "<br />".join(get_random_joke().text.split("\n"))

@app.route("/category/", defaults={'cat_en': None})
@app.route("/category/<cat_en>")
def category_joke(cat_en):
    if cat_en == None:
        return str(categories)
    return filter_by_category(cat_en)

class joke:
    def __init__(self, text, category):
        self.text = text
        self.category = category


jokes = []
categories = [{'bg': "футбол", 'en': "football"}, {'bg': "работа", 'en': "work"}, {'bg': "разни", 'en': "others"}, {'bg': "семейни", 'en': "family"}, {'bg': "училище", 'en': "school"}, {'bg': "за иванчо", 'en': "ivancho"}, {'bg': "за големи", 'en': "nsfw"}]



def get_file_names(folder, mask):
    joke_files = []
    for path, subdirs, files in os.walk(folder):
        for name in files:
            if fnmatch(name, mask):
                joke_files.append(os.path.join(path, name))
    return joke_files


def get_jokes(joke_files):
    for joke_file in joke_files:
        with open(joke_file) as f:
            lines = f.readlines()
            joke_text = []
            joke_cat = ""
            for line in lines:
                if "Category:" in line:
                    joke_cat = line.split(":")[1].strip()
                elif ("Title:" in line) or ("Date:" in line) or ("Tags:" in line) or (line.strip() == "") or (line == "\n"):
                    pass
                else:
                    joke_text.append(line)
            text = "".join(joke_text).replace("&minus;", "-") + "\n"
            jokes.append(joke(text, joke_cat))
    return jokes

def filter_by_category(category):
    try:
        bg_category = list(filter(lambda cat: cat['en'] == category, categories))[0]['bg']
    except IndexError as error:
        return "Category not found!",404
    category_jokes = []
    for joke in jokes:
        if joke.category.lower() == bg_category.lower():
            category_jokes.append(joke.text)
    return random.choice(category_jokes)

def get_random_joke():
    return random.choice(jokes)

def update_jokes_list():
    joke_files_list = get_file_names(content_folder, pattern)
    global jokes
    jokes = get_jokes(joke_files_list)

if __name__ == "__main__":
    update_jokes_list()
    app.run(host='0.0.0.0', port=8888)