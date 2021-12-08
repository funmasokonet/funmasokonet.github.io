import os
import re
import random
from fnmatch import fnmatch
from flask import Flask, jsonify, request

# configuration variables for pulling the jokes from the site
content_folder = os.getcwd().replace("api", "content/posts")
pattern = "*.md"
jokes = []
categories = [{'bg': "футбол", 'en': "football"}, {'bg': "работа", 'en': "work"}, {'bg': "разни", 'en': "others"},
              {'bg': "семейни", 'en': "family"}, {'bg': "училище", 'en': "school"},
              {'bg': "за иванчо", 'en': "ivancho"}, {'bg': "за големи", 'en': "nsfw"}]
app = Flask(__name__)
hits = 0

@app.route("/loaderio-aabdddedc48fc87800a33787c071d90b.txt")
def txt():
    return "loaderio-aabdddedc48fc87800a33787c071d90b"

@app.route("/")
def just_joke():
    global hits
    hits += 1
    return get_random_joke().text


@app.route("/info")
@app.route("/info/")
def count_jokes():
    return "api.masoko.net\nPowered by fun.masoko.net\n{} вица.\n{} hits.\n".format(len(jokes), human_format(hits))


@app.route("/update")
@app.route("/update/")
def update():
    update_jokes_list()
    return "Jokes DB updated\n"


@app.route("/html/")
@app.route("/html")
def json_joke():
    global hits
    hits += 1
    return "<br />".join(get_random_joke().text.split("\n"))


@app.route("/category/", defaults={'cat_en': None, 'html': False})
@app.route("/<html>/category/", defaults={'cat_en': None})
@app.route("/category/<cat_en>/", defaults={'html': False})
@app.route("/<html>/category/<cat_en>/")
def category_joke(html, cat_en):
    global hits
    hits += 1
    if cat_en == None:
        cat = []
        for c in categories:
            cat.append(c["en"])
        return "Налични категории " + ", ".join(cat) + "\n"
    elif html == 'html':
        return "<br />".join(filter_by_category(cat_en).split("\n"))
    return filter_by_category(cat_en)


class joke:
    def __init__(self, text, category):
        self.text = text
        self.category = category


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
                elif ("Title:" in line) or ("Date:" in line) or ("Tags:" in line) or (line.strip() == "") or (
                re.match(r'^\s*$', line)):
                    pass
                else:
                    joke_text.append(line)
            joke_text[-1] = joke_text[-1].strip()
            text = "".join(joke_text).replace("&minus;", "-") + "\n"
            jokes.append(joke(text, joke_cat))
    return jokes


def filter_by_category(category):
    try:
        bg_category = list(filter(lambda cat: cat['en'] == category, categories))[0]['bg']
    except IndexError as error:
        return " Няма такава категория!", 404
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
    jokes = []
    jokes = get_jokes(joke_files_list)

def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

if __name__ == "__main__":
    update_jokes_list()
    app.run(host='0.0.0.0', port=8888)
