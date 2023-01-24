from flask import Flask, request, render_template
from flask_cors import CORS
from json import loads

from process import get_text_from_url, create_summary

app = Flask(__name__)
CORS(app)


class URL:
    def __init__(self, url:str) -> None:
        self.url = url
        self.id = str(hash(url))
        # TODO: Make Async
        self.headers, self.contents = get_text_from_url(url)
    
    def marshal(self) -> dict[str, str]:
        heading = self.url.rsplit('/', 1)[1].replace('-', ' ').capitalize()
        return {"id": self.id, "url":self.url, "heading": heading, "summary": create_summary(self.headers, self.contents)}

url_list: list[URL] = []


@app.route("/")
def get_all_urls():
    global url_list
    return render_template('index.html', url_list=[url.marshal() for url in url_list])

@app.post("/post_urls")
def post_urls():
    global url_list
    data = loads(request.form["json"])
    init_len = len(url_list)
    url_list.extend([URL(url) for url in data if 'premium' not in url])
    return {"action": f"Added {len(url_list)-init_len} URLs"}

@app.route("/clear")
def clear():
    global url_list
    url_list.clear()
    return {"action": "Removed all"}