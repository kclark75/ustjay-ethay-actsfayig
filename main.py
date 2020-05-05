import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")
    print(facts[0].getText())

    return facts[0].getText()


def pig_latinizer(quote):
    payload = {'input_text': quote}
    
    response = requests.post("http://hidden-journey-62459.herokuapp.com/piglatinize/",
                             data=payload)
    print(response.url)
    return response.url


@app.route('/')
def home():
    fact = get_fact().strip()
    header = pig_latinizer(fact)
    print(fact)
    print(header)
    return Response(response=header, mimetype='gzip')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port, debug=True)

