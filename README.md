# Mission to Mars
Homework 12 for UMN Data Boot Camp

This assignment was to scrape 4 different websites for data relating to Mars and display the results in a webpage using Bootstrap. I used Beautiful Soup, Splinter, and the pandas `read_html()` method to retrieve the data. It is then stored in a Mongo database where it can be retrieved by the Flask endpoint and rendered using Jinja templates inside of an HTML file styled with Bootstrap. 

![Screenshot of webpage](mission_to_mars.png)

Follow these steps to run the site locally:
1. Clone and navitgate to the repo in a terminal
1. Activate Python virtual environment
1. Launch the Flask app with the command `python app.py`
1. Go to `127.0.0.1/5000` in your browser
1. Click the "Scrape Latest Data" button to pull the most recent data

This code was written using Python 3.8 and requires the following packages:
* flask
* pymongo
* pandas
* splinter
* Beautiful Soup

Note: I ran out of time/energy to figure out how to scrape the hemisphere images so they are hardcoded. I understand the general idea of how I would return these images but I couldn't get the syntax together and decided my energy would be better spent on other class work.