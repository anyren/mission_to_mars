from flask import Flask, render_template, redirect
import pymongo
import scrape

app = Flask(__name__)

# mongo setup
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars


@app.route("/")
def index():
    data = db.mars_data.find_one()
    news_title = data['news_title']
    news_body = data['news_body']
    facts = data['mars_facts_html']
    hemispheres = data['mars_hemispheres']

    return render_template("index.html", mars_facts=facts, title=news_title, body=news_body, hemispheres=hemispheres)
    

@app.route("/scrape")
def scraper():
    data_dict = scrape.scrape_mars()
    db.mars_data.update_one({},{"$set":data_dict},upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)

