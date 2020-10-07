from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://img.buzzfeed.com/buzzfeed-static/static/2017-08/9/17/asset/buzzfeed-prod-web-10/anigif_sub-buzz-8427-1502313524-1.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2017-08/9/17/asset/buzzfeed-prod-web-02/anigif_sub-buzz-22626-1502313674-1.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2017-08/9/17/asset/buzzfeed-prod-web-06/anigif_sub-buzz-8222-1502313939-1.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2017-08/9/17/asset/buzzfeed-prod-web-05/anigif_sub-buzz-30975-1502314180-1.gif"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")