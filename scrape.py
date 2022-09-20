import requests
import pandas as pd
#from splinter import Browser
from bs4 import BeautifulSoup
#from webdriver_manager.chrome import ChromeDriverManager

# def scrape_news():
#     # Scrape the Mars News Site and collect the latest News Title and Paragraph Text. 
#     # Assign the text to variables that you can reference later.
#     mns = 'https://redplanetscience.com'
#     # Setup splinter
#     executable_path = {'executable_path': ChromeDriverManager().install()}
#     browser = Browser('chrome', **executable_path, headless=False)
#     browser.visit(mns)
#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')
#     news_title = soup.find('div', class_='content_title').text
#     news_body = soup.find('div', class_='article_teaser_body').text
#     browser.quit()
#     return(news_title, news_body)

def scrape_facts():
    # Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet 
    # including diameter, mass, etc.
    # Use Pandas to convert the data to a HTML table string.
    mf = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(mf)
    mars_facts = tables[1]
    mars_facts_html = mars_facts.to_html()
    mars_facts_html.replace('\n', '')
    return(mars_facts_html)

# def scrape_hemisphere():
#     # Visit the astrogeology site to obtain high-resolution images for each hemisphere of Mars.
#     # You will need to click each of the links to the hemispheres in order to find the image URL to the 
#     # full-resolution image.
#     # Save the image URL string for the full resolution hemisphere image and the hemisphere title containing the 
#     # hemisphere name. 
#     # Use a Python dictionary to store the data using the keys img_url and title.
#     # Append the dictionary with the image URL string and the hemisphere title to a list. This list will contain one 
#     # dictionary for each hemisphere.
#     mh = 'https://marshemispheres.com/cerberus.html'
#     hemisphere_image_urls = [
#     {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced.tif"},
#     {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/cerberus_enhanced.tif"},
#     {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced.tif"},
#     {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced.tif"}]
#     return(hemisphere_image_urls)


    

