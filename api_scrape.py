import flask
from flask import request, jsonify
from scraping import scrape_url
import parameters
#from scraping import parameters


app = flask.Flask(__name__)

app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route("/api/profile_url", methods=['GET'])
def api_scrapping():
    keyword = request.args.get('keyword')
    linkedin_url = []
    linkedin_url = scrape_url.get(keyword)
    return jsonify(linkedin_url)

app.run()