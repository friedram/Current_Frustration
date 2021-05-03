#Andrew(Andy)Friedrich
#CS361
#Githubusername-friedram
#HW3-MVP - Word Cloud & using REST

"""
Works:
Word cloud image created
import two files

Backlog for this week:
-- compare words - use compared common words for word cloud
-- add section for additional STOPWORDS
-- output JPEG to screen
-- output JPEG to HTML

Backlog for future sprint:
-- lower case everything
-- deal with pictures / nonsense characters / unsupported data types - by having called out or ignore?
-- user selection of files
-- adding additional stopwords

"""


# Credit:
# https://programmerbackpack.com/word-cloud-python-tutorial-create-wordcloud-from-text/
# https://stackoverflow.com/questions/42418085/python-wordcloud-from-a-txt-file

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(360.0 * 45.0 / 255.0)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)

    return "hsl({}, {}%, {}%)".format(h, s, l)

file_content=open ("sampleWords.txt").read()
file_content2 = open ("sampleWordsLOL.txt").read()
file_content += file_content2


wordcloud = WordCloud(font_path = r'C:\Windows\Fonts\Verdana.ttf',
                            stopwords = STOPWORDS,
                            background_color = 'white',
                            width = 1200,
                            height = 1000,
                            color_func = random_color_func
                            ).generate(file_content)



#plt.imshow(wordcloud)
#plt.axis('off')
#plt.show()
# saves picture file to picture format
plt.savefig('bank_data.png')
plt.savefig('bank_data.png')
