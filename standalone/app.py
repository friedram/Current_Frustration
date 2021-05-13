# https://stackoverflow.com/questions/25149493/how-to-call-another-webservice-api-from-flask
# https://thispointer.com/python-three-ways-to-check-if-a-file-is-empty/
# https://www.geeksforgeeks.org/how-to-create-a-pop-up-message-when-a-button-is-pressed-in-python-tkinter/
# https://stackoverflow.com/questions/23112316/using-flask-how-do-i-modify-the-cache-control-header-for-all-output
# https://dbader.org/blog/python-check-if-file-exists#:~:text=The%20most%20common%20way%20to%20check%20for%20the,search%20engine%20on%20how%20to%20solve%20this%20problem.
# fixing word cloud multi thread issues:
# https://www.shanelynn.ie/using-python-threading-for-multiple-results-queue/
# https://stackoverflow.com/questions/31264826/start-a-flask-application-in-separate-thread
# https://izziswift.com/start-a-flask-application-in-separate-thread/

import os
import requests
import os.path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, jsonify, render_template, redirect, url_for, request
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from urllib.request import urlopen
from flask import flash
import threading
data = 'foo'

from forms import runWordCloudForm, AddGameForm, AddGenreForm, AddCreatorForm, AddPlatformForm, \
    AddEpisodeForm, AddToM2MPlatformGame, \
    EditTheGame, SearchForm, SearchForm2, RemoveGame, RemoveGenre, RemoveCreator, \
    RemovePlatform, RemoveEpisode, RemoveGameAndPlatform, SearchPageForm

#application flask run
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300
app.config['SECRET_KEY'] = 'oTv!5ox8LB#A&@cBHpa@onsKU'


# No cacheing at all for API endpoints.
'''
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
        response.cache_control.public = True
    return response
'''
def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(360.0 * 45.0 / 255.0)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)

    return "hsl({}, {}%, {}%)".format(h, s, l)


@app.route('/', methods=['GET', 'POST'])
def index():
    #flash('in the index')
    try:
        f = open('game.json')
        f.close()
    except IOError:
        print('File is not accessible')
    print('File is accessible')
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def cloudMake():
    print('in cloudMake')
    flash('Word Cloud successfully created')
    return redirect(url_for('index'))



@app.route('/SomeFunction', methods=['POST', 'GET'])
def SomeFunction():
    print('In SomeFunction')
    print("inside if")
    file_content = 0
    file_content2 = 0
    file_content = open("game.json").read()
    file_content2 = open("pokemonSnap_keywords.json").read()
    file_content += file_content2
    # font_path=r'C:\Windows\Fonts\Verdana.ttf',
    print("FileContent")
    wordcloud = WordCloud(
        stopwords=STOPWORDS,
        background_color='white',
        width=1200,
        height=1000,
        color_func=random_color_func
    ).generate(file_content)
    plt.imshow(wordcloud)
    plt.axis('off')
    # plt.show()
    # saves picture file to picture format
    plt.savefig('static/wordCloud.png')
    print("wordCloud.png created")
    flash('Success! Word Cloud has been processed and is loading')
    return redirect(url_for('wordcloud'))
    #return cloudMake()

@app.route("/wordcloud", methods=['POST', 'GET'])
def wordcloud():
    flash('Success! Word Cloud has been processed and is loading')
    return render_template('wordcloud.html')



@app.route("/wordcloud2", methods=['POST', 'GET'])
def wordcloud2():
    try:
        f = open('game.json')
        f.close()
    except IOError:
        print('File is not accessible')
        flash('Files not found or readable. One or more required scraper files (game.json as example) not available - please fix')
        return render_template('wordcloud.html')
    print('File is accessible')
    flash('You created a word cloud')
    print('In SomeFunction')
    print("inside if")
    file_content = 0
    file_content2 = 0
    file_content = open("game.json").read()
    file_content2 = open("pokemonSnap_keywords.json").read()
    file_content += file_content2
    # font_path=r'C:\Windows\Fonts\Verdana.ttf',
    print("FileContent")
    wordcloud = WordCloud(
        stopwords=STOPWORDS,
        background_color='white',
        width=1200,
        height=1000,
        color_func=random_color_func
    ).generate(file_content)
    plt.imshow(wordcloud)
    plt.axis('off')
    # plt.show()
    # saves picture file to picture format
    plt.savefig('static/wordCloud.png')
    print("wordCloud.png created")
    flash('Success! Word Cloud has been processed and is loading')
    return render_template('wordcloud2.html')



@app.route('/restCAT')
def restCAT():
    with urlopen('http://localhost:3002/giveMeACat') as r:
        text = r.read()
    return text

@app.route('/restDOG')
def restDOG():
    with urlopen('http://localhost:3001/giveMeADog') as r:
        text = r.read()
    return text


#if __name__ == '__main__':
#   app.run()

@app.route("/")
def main():
    return data
if __name__ == "__main__":
    threading.Thread(target=app.run).start()