from flask import Flask, render_template, redirect
import pymongo
# from flask_pymongo import PyMongo
import scrape

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
# mongo = PyMongo(app)

# Create connection variable
conn = 'mongodb://localhost:27017'
# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)
# Connect to a database. Will create one if not already available.
db = client.mars


@app.route("/")
def index():
    # find one document from our mongo db and return it.
    mars_facts = db.facts.find_one()
    # pass that listing to render_template
    return render_template("index.html", mars_facts=mars_facts)
    


@app.route("/scrape")
def scraper():

    # news_title, news_body = scrape.scrape_news()
    # news_content =[news_title, news_body]
    # db.news.update_one({},{"$set":news_content},upsert=True)

    mars_facts_html = scrape.scrape_facts()
    print(mars_facts_html)
    db.facts.update_one({},{"$set":{mars_facts_html:mars_facts_html}}, upsert=True)

    # hemisphere_image_urls = scrape.scrape_hemispheres()
    # db.mars_hem.update_one({}, {"$set": hemisphere_image_urls}, upsert=True)

    # return a message to our page so we know it was successful.
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)

